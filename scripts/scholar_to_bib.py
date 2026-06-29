#!/usr/bin/env python3
"""Generate publications.bib from a Google Scholar profile via SerpAPI.

Google Scholar has no official API and blocks scraping from datacenter IPs
(e.g. GitHub Actions runners), so we go through SerpAPI's Google Scholar Author
endpoint, which returns the publication list reliably.

Environment variables:
  SERPAPI_KEY        SerpAPI API key (required, store as a GitHub secret)
  SCHOLAR_AUTHOR_ID  Google Scholar author id -- the `user=` value in your
                     profile URL, e.g. for
                     https://scholar.google.com/citations?user=ABCdEfG it is
                     "ABCdEfG" (required)
  OUTPUT             Output path (default: publications.bib)

Note: Scholar exposes title / authors / venue / year / citation count / link,
but usually NOT abstracts or DOIs, so generated entries are intentionally lean.
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
        # Continue only while SerpAPI reports another page.
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


def to_bibtex(article, used_keys):
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
    return year, "@article{" + key + ",\n" + ",\n".join(fields) + ",\n}"


def main():
    api_key = os.environ.get("SERPAPI_KEY")
    author_id = os.environ.get("SCHOLAR_AUTHOR_ID")
    out_path = os.environ.get("OUTPUT", "publications.bib")
    if not api_key or not author_id:
        sys.exit("SERPAPI_KEY and SCHOLAR_AUTHOR_ID environment variables are required")

    articles = fetch_articles(author_id, api_key)
    print("Fetched " + str(len(articles)) + " articles from Google Scholar")

    used_keys, entries = set(), []
    for article in articles:
        entry = to_bibtex(article, used_keys)
        if entry:
            entries.append(entry)

    entries.sort(key=lambda e: e[0], reverse=True)  # newest first
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(text for _, text in entries) + "\n")
    print("Wrote " + str(len(entries)) + " entries to " + out_path)


if __name__ == "__main__":
    main()
