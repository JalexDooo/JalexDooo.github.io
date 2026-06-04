# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is **SunLab** — the personal academic CV website for Jindong Sun (Ph.D & Lecturer, Shandong University of Science and Technology). It is built with [Hugo Blox Builder](https://hugoblox.com) using the Academic CV template and deployed to both GitHub Pages (`jalexdooo.github.io`) and a custom domain (`www.jdsun-lab.cn`).

## Commands

```bash
# Install dependencies (required before first run)
pnpm install

# Start local dev server with live reload
pnpm dev          # or: hugo server --disableFastRender

# Build for production
pnpm build        # or: hugo --minify
```

Hugo version required: **0.152.2 Extended**. The package manager is **pnpm** (v10.14.0).

## Architecture

### Content Model

All site content lives in `content/`. Hugo Blox uses YAML front matter to configure page blocks:

- `content/_index.md` — Homepage. A `type: landing` page composed of named `blocks` (e.g. `resume-biography-3`, `collection`, `markdown`, `cta-card`). This is the primary file to edit to change the homepage layout.
- `content/authors/admin/_index.md` — The main author profile (biography, education, work history, skills, social links). Most structured data displayed on the homepage and experience page comes from here.
- `content/publications/` — Each publication is a folder with `index.md` (structured front matter: title, authors, date, DOI, abstract, tags, `featured: true/false`) and optionally `cite.bib` and a featured image.
- `content/blog/` — News/blog posts displayed in the "Recent News" section.
- `content/events/` — Talks and events displayed in the "Recent & Upcoming Talks" section.
- `content/teams/` — Lab team member cards.
- `content/experience.md` — Standalone experience page using `resume-experience`, `resume-skills`, `resume-awards`, `resume-languages` blocks (data sourced from the admin author profile).

### Configuration

- `config/_default/hugo.yaml` — Core Hugo config: site title, base URL, build settings.
- `config/_default/params.yaml` — Theme appearance (color, mode), navbar settings, footer copyright.
- `config/_default/menus.yaml` — Navigation links and their ordering.
- `config/_default/languages.yaml` / `module.yaml` — Language and Hugo module settings.
- `hugoblox.yaml` — Hugo Blox template version pin (`academic-cv`, Hugo `0.152.2`).

### Publication Import Workflow

Publications can be managed via `publications.bib`. Pushing changes to this file on `main` triggers a GitHub Actions workflow (`.github/workflows/`) that runs `academic import` to convert BibTeX entries into Markdown files under `content/publication/` and opens a PR.

### Deployment

- **GitHub Pages**: `.github/workflows/` — builds on push to `main` with Hugo and runs Pagefind for search indexing.
- **Netlify**: `netlify.toml` — alternative deployment target with its own build config.

### Custom Layouts

`layouts/_partials/hooks/` — Hugo partial overrides for Hugo Blox customization.

### Static Assets

- `static/uploads/resume.pdf` — Linked resume PDF.
- `static/uploads/CNAME` — Custom domain config for GitHub Pages.
- `assets/media/` — SVG icons and other media assets.
