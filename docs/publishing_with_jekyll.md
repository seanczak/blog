# Publishing with Jekyll

How the blog is built, rendered and published, and why it's set up this way. For where ideas and their files live, see [content_curation.md](content_curation.md).

## GitHub Pages

- The site is https://seanczak.github.io/blog/, built by GitHub Pages from the repo root on `main` (Settings → Pages → Deploy from a branch → `main`, `/(root)`). Pushing to `main` publishes. There's no CI workflow and no local build step in the deploy.
- Pages uses its legacy builder, which runs **Jekyll 3.10 in safe mode** with the `github-pages` gem's plugins. Local preview pins the same versions through [`jekyll/Gemfile`](../jekyll/Gemfile) (`github-pages` 232, Jekyll 3.10.0, kramdown 2.4.0 as of September 2026; compare with https://pages.github.com/versions.json). (If matching Pages locally stops working, the fallback is a GitHub Actions build that runs whatever Jekyll version is used locally.)
- Safe mode ignores symlinks and third-party plugins. Don't rely on either.
- The visible name is **Sean Fronczak**. The GitHub username and base path stay `seanczak` and `/blog`.

### Preview and verify

- Local preview: `jekyll/serve.sh`, then open `http://127.0.0.1:4001/blog/`. The first run installs the pinned gems into `jekyll/vendor/bundle` (gitignored). Build output goes to `_site/` and `.jekyll-cache/`, also gitignored.
- The `github-pages` plugins render any Markdown file at the repo root as a page, so `README.md`, `AGENTS.md` and `CLAUDE.md` are listed in `exclude`.
- GitHub CLI: `/home/sfronczak/.local/bin/gh`. After a push, check the Pages build with `gh api repos/seanczak/blog/pages/builds/latest --jq '.status+" "+.commit'` and wait for `built` on the pushed commit.

## Repo layout decisions

| Path | Role | Why it's there |
|---|---|---|
| `_config.yml` | Site config | Pages only reads it from the repo root. |
| `jekyll/` | Everything that serves the site: `_layouts/`, `assets/` (CSS, portrait), `index.md` (homepage), `about.md`, plus the local tooling (`Gemfile`, `Gemfile.lock`, `serve.sh`) | Keeps serving machinery out of the way of the writing. `_config.yml` sets `layouts_dir: jekyll/_layouts`. `index.md` and `about.md` set their own `permalink`, so they're served at `/` and `/about/`, not under `/jekyll/`. |
| `content/<area>/<idea>/_posts/` | Published posts | Jekyll picks up `_posts/` folders at any depth, so each post stays next to its notes. The folder must be named exactly `_posts`. |
| `docs/` | Repo conventions | Excluded from the built site. |

There's no top-level `_posts/`. The original placeholder posts were deleted, and the power-analysis post moved to `content/statistics/power_analysis/`.

### `_config.yml`

- `baseurl: "/blog"`: the site lives under `/blog`. Every internal link and asset must go through `relative_url` (see below) or it breaks.
- `permalink: /:year/:month/:day/:title/`: post URLs. Changing this breaks existing links.
- `timezone: America/Los_Angeles`: dates are read in Pacific time. A post dated later today than the moment of the build counts as a future post and is skipped. Date same-day posts `00:00:00`.
- `exclude`: keeps `notshared/`, `docs/`, root Markdown files, the local Jekyll tooling, and each idea's `notes.md`, `outline.md`, `src/` and `notshared/` out of the built site.

## Writing a post

Where a post lives, how it's named and how it grows out of notes and an outline are covered in [content_curation.md](content_curation.md). This section covers what Jekyll needs from the post file itself: `content/<area>/<idea>/_posts/YYYY-MM-DD-short-title.md` with this front matter:

```md
---
layout: post
title: "A Short Title"
date: 2026-09-26 00:00:00 -0700
description: "One line; shown on the homepage."
tags: [one-category, another-category]
---
```

- **Categories go in `tags`, not `categories`.** Jekyll adds every folder above a nested `_posts/` (for example `content`, `statistics`, `power_analysis`) to a post's `categories` and merges them with the front matter, so the real ones can't be picked out. `tags` is never derived from folders. The site still labels them "Categories".
- Use one to three tags. Agents ask the human for them and don't invent new ones.
- `description` and `tags` drive the homepage archive and filter. Posts sort newest first by `date`.
- `published: false` keeps a post in the repo but off the site. Remove the flag to publish.

### Headings and the table of contents

The right-hand "On this page" table of contents is generated from `##` through `######` headings. Add an explicit ID only when a stable anchor is needed: `## Introduction {#introduction}`.

### Links and images

Internal links and assets must go through `relative_url` so they get the `/blog` prefix:

```md
![Power curves]({{ '/content/statistics/power_analysis/img/power-curves.svg' | relative_url }})
```

Every generated figure or asset needs a checked-in reproducible script; see [content_curation.md](content_curation.md) for where `src/` and `img/` go.

## Design and rendering

- Quiet editorial style: grey base, turquoise (`#087f86`) for content links and interaction, opaque gold (`#c6a34b`) for 2px structural dividers and the portrait trim.
- Header: portrait, name, then Posts / About / LinkedIn. Header links are charcoal, and turquoise only on hover.
- Homepage: chronological post list with a sticky right-hand Categories filter. No hero, no "Writing" heading, no card-heavy design.
- Articles: categories appear beneath the title. The table of contents hides below a `56rem` viewport width.
- Implement dynamic state programmatically and deterministically. Don't use DOM-position selectors (for example `:first-child`) for filtered or sorted state. Derive it from visible data and apply explicit classes.
