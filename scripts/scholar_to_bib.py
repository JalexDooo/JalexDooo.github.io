#!/usr/bin/env python3
"""Sync publications from a Google Scholar profile via SerpAPI (add-new-only).

Google Scholar has no official API and blocks scraping from datacenter IPs
(e.g. GitHub Actions runners), so we go through SerpAPI's Google Scholar Author
endpoint, which returns the publication list reliably.

Strategy: preserve hand-curated pages. We write the full library to OUTPUT for
reference, but only emit entries whose (normalised) title is NOT already present
under EXISTING_DIR to NEW_OUTPUT. The workflow imports NEW_OUTPUT only, so
existing pages -- with their abstracts and featured images -- are left untouched.

Environment variables:
  SERPAPI_KEY        SerpAPI API key (required, store as a GitHub secret)
  SCHOLAR_AUTHOR_ID  Google Scholar author id -- the `user=` value in your
                     profile URL (required)
  OUTPUT             Full library bib path (default: publications.bib)
  NEW_OUTPUT         New-entries-only bib path (default: new_publications.bib)
  EXISTING_DIR       Dir of existing pages (default: content/publications)
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request

API = "https://serpapi.com/search.json"
MAX_ARTICLES = 1000  # safety cap


def fetch_articles(author_id, api_key):
    """Page through the author's full publication list."""
    articles = []
    start = 0
    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": api_key,
            "num": 100,
            "start": start,
            "sort": "pubdate",  # newest first
        }
        url = API + "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = json.load(resp)
        if data.get("error"):
            sys.exit("SerpAPI error: " + str(data["error"]))
        batch = data.get("articles") or []
        if not batch:
            break
        articles.extend(batch)
        if "next" not in (data.get("serpapi_pagination") or {}):
            break
        start += len(batch)
        if start >= MAX_ARTICLES:
            break
    return articles


def format_authors(raw):
    """'X An, J Sun, Y Zhang' -> 'An, X and Sun, J and Zhang, Y' (BibTeX form)."""
    out = []
    for name in (raw or "").split(","):
        name = name.strip()
        if not name:
            continue
        parts = name.split()
        if len(parts) >= 2:
            out.append(parts[-1] + ", " + " ".join(parts[:-1]))
        else:
            out.append(name)
    return " and ".join(out)


def clean_venue(venue, year):
    """Scholar's 'publication' field often trails a volume/year -- trim the year."""
    venue = (venue or "").strip()
    if year:
        venue = re.sub(r",?\s*" + re.escape(year) + r"\s*$", "", venue).strip()
    return venue.rstrip(",").strip()


def slugify(text):
    return (re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_").lower() or "ref")[:40]


def normalize_title(title):
    """Collapse a title to lowercase alphanumerics for robust matching."""
    return re.sub(r"[^a-z0-9]+", "", (title or "").lower())


def build_record(article, used_keys):
    title = (article.get("title") or "").strip()
    if not title:
        return None
    year = (article.get("year") or "").strip()
    authors = format_authors(article.get("authors", ""))
    venue = clean_venue(article.get("publication", ""), year)
    link = (article.get("link") or "").strip()
    cited = (article.get("cited_by") or {}).get("value")

    first_author = authors.split(",")[0] if authors else "ref"
    base = slugify(first_author + "_" + year + "_" + title.split(" ")[0])
    key, n = base, 2
    while key in used_keys:
        key = base + "_" + str(n)
        n += 1
    used_keys.add(key)

    fields = ["\ttitle = {" + title + "}"]
    if authors:
        fields.append("\tauthor = {" + authors + "}")
    if year:
        fields.append("\tyear = {" + year + "}")
    if venue:
        fields.append("\tjournal = {" + venue + "}")
    if link:
        fields.append("\turl = {" + link + "}")
    if cited is not None:
        fields.append("\tnote = {Cited by " + str(cited) + "}")
    bibtex = "@article{" + key + ",\n" + ",\n".join(fields) + ",\n}"
    return {"year": year, "title": title, "norm": normalize_title(title), "bibtex": bibtex}


def parse_title(path):
    """Read the `title:` value from a page's YAML front matter (handles folding)."""
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError:
        return ""
    if not lines or lines[0].strip() != "---":
        return ""
    parts, capturing = [], False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if capturing:
            if re.match(r"^\S", line):  # next top-level key -> title ended
                break
            parts.append(line.strip())
            continue
        m = re.match(r"^title:\s*(.*)$", line)
        if m:
            parts.append(m.group(1).strip())
            capturing = True
    return " ".join(p for p in parts if p).strip()


def existing_titles(directory):
    """Normalised titles of every page already present in `directory`."""
    found = set()
    if not os.path.isdir(directory):
        return found
    for name in os.listdir(directory):
        index = os.path.join(directory, name, "index.md")
        if os.path.isfile(index):
            norm = normalize_title(parse_title(index))
            if norm:
                found.add(norm)
    return found


def main():
    api_key = os.environ.get("SERPAPI_KEY")
    author_id = os.environ.get("SCHOLAR_AUTHOR_ID")
    out_path = os.environ.get("OUTPUT", "publications.bib")
    new_path = os.environ.get("NEW_OUTPUT", "new_publications.bib")
    existing_dir = os.environ.get("EXISTING_DIR", "content/publications")
    if not api_key or not author_id:
        sys.exit("SERPAPI_KEY and SCHOLAR_AUTHOR_ID environment variables are required")

    articles = fetch_articles(author_id, api_key)
    print("Fetched " + str(len(articles)) + " articles from Google Scholar")

    used_keys, records = set(), []
    for article in articles:
        rec = build_record(article, used_keys)
        if rec:
            records.append(rec)
    records.sort(key=lambda r: r["year"], reverse=True)  # newest first

    # Full library, for reference.
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(r["bibtex"] for r in records) + "\n")

    # New-only: titles not already present as curated pages.
    have = existing_titles(existing_dir)
    new = [r for r in records if r["norm"] not in have]
    with open(new_path, "w", encoding="utf-8") as fh:
        fh.write(("\n\n".join(r["bibtex"] for r in new) + "\n") if new else "")

    print("Library: %d total, %d already present, %d new" % (len(records), len(have), len(new)))
    for r in new:
        print("  + NEW: " + r["title"])


if __name__ == "__main__":
    main()
