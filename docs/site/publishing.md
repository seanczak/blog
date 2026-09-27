# Publishing with Jekyll

How the blog is built and published, and why it's set up this way. For where ideas and their files live, see [content_structure.md](../workspace/content_structure.md); for how the site looks and its pages behave, see [design.md](design.md).

## GitHub Pages

- The site is https://seanczak.github.io/blog/, built by GitHub Pages from the repo root on `main` (Settings → Pages → Deploy from a branch → `main`, `/(root)`). Pushing to `main` publishes. There's no CI workflow and no local build step in the deploy.
- Pages uses its legacy builder, which runs **Jekyll 3.10 in safe mode** with the `github-pages` gem's plugins. Local preview pins the same versions through [`jekyll/Gemfile`](../../jekyll/Gemfile) (`github-pages` 232, Jekyll 3.10.0, kramdown 2.4.0 as of September 2026; compare with https://pages.github.com/versions.json). (If matching Pages locally stops working, the fallback is a GitHub Actions build that runs whatever Jekyll version is used locally.)
- Safe mode ignores symlinks and third-party plugins. Don't rely on either.
- The visible name is **Sean Fronczak**. The GitHub username and base path stay `seanczak` and `/blog`.

### Preview and verify

- Local preview: `jekyll/serve.sh`, then open `http://127.0.0.1:4001/blog/`. The first run installs the pinned gems into `jekyll/vendor/bundle` (gitignored). Build output goes to `_site/` and `.jekyll-cache/`, also gitignored.
- The `github-pages` plugins render any Markdown file at the repo root as a page, so `README.md`, `AGENTS.md` and `CLAUDE.md` are listed in `exclude`.
- GitHub CLI: `/home/sfronczak/.local/bin/gh`. After a push that changes the built site (any file Jekyll renders or copies: not under `exclude` in `_config.yml`, not a dotfile or dot-directory such as `.claude/`), start the `pages-build-check` subagent (`.claude/agents/pages-build-check.md`) in the background with the pushed SHA. It polls `gh api repos/seanczak/blog/pages/builds/latest` until that commit is `built` or `errored`. Relay its report to the human, including the hard-refresh reminder (Ctrl+Shift+R): without it the browser may serve the cached page.

## Repo layout decisions

| Path | Role | Why it's there |
|---|---|---|
| `_config.yml` | Site config | Pages only reads it from the repo root. |
| `jekyll/` | Everything that serves the site: `_layouts/` (page shells), `_includes/` (reusable fragments: header, topic tree, archive list, category filter and pills), `_data/` (`tree.yml` for the landing page, `navigation.yml` for header links), `_sass/` (one partial per component, compiled through `assets/css/style.scss`), `assets/js/` (one script per interactive page), `assets/images/`, the pages `index.md`, `archive.md`, `about.md`, `404.md`, plus the local tooling (`Gemfile`, `Gemfile.lock`, `serve.sh`) | Keeps serving machinery out of the way of the writing. `_config.yml` sets `layouts_dir`, `includes_dir`, `data_dir` and `sass.sass_dir` to these folders. `index.md`, `archive.md`, `about.md` and `404.md` set their own `permalink`, so they're served at `/`, `/archive/`, `/about/` and `/404.html`, not under `/jekyll/`. |
| `content/<area>/<idea>/_posts/` | Published posts | Jekyll picks up `_posts/` folders at any depth, so each post stays next to its notes. The folder must be named exactly `_posts`. |
| `docs/` | Repo conventions | Excluded from the built site. |

There's no top-level `_posts/`.

### `_config.yml`

- `baseurl: "/blog"`: the site lives under `/blog`. Every internal link and asset must go through `relative_url` (see below) or it breaks.
- `permalink: /:year/:month/:day/:title/`: post URLs. Changing this breaks existing links.
- `timezone: America/Los_Angeles`: dates are read in Pacific time. A post dated later today than the moment of the build counts as a future post and is skipped. Date same-day posts `00:00:00`.
- `exclude`: keeps `notshared/`, `docs/`, root Markdown files, the local Jekyll tooling, and each idea's `notes.md`, `outline.md`, `src/`, `original_work/` and `notshared/` out of the built site.

## Writing a post

Where a post lives, how it's named and how it grows out of notes and an outline are covered in [content_structure.md](../workspace/content_structure.md). This section covers what Jekyll needs from the post file itself: `content/<area>/<idea>/_posts/YYYY-MM-DD-short-title.md` with this front matter:

```md
---
layout: post
title: "A Short Title"
date: 2026-09-26 00:00:00 -0700
description: "One line; shown on the homepage."
tags: [one-category, another-category]
---
```

- **Categories go in `tags`, not `categories`.** Jekyll adds every folder above a nested `_posts/` (for example `content`, `statistics`, `2020_election_series`, `01_virginia`) to a post's `categories` and merges them with the front matter, so the real ones can't be picked out. `tags` is never derived from folders. The site still labels them "Categories".
- Use one to three tags. Agents ask the human for them and don't invent new ones.
- `description` and `tags` drive the archive and its filter. `description` is also the post's default blurb on the landing page.
- A post appears on the landing page only once it's listed in `jekyll/_data/tree.yml` (see [design.md](design.md)). Posts sort newest first by `date`.
- `published: false` keeps a post in the repo but off the site. Remove the flag to publish.

### Headings and the table of contents

The right-hand "On this page" table of contents is generated from `##` through `######` headings. Add an explicit ID only when a stable anchor is needed: `## Introduction {#introduction}`.

### Links and images

Internal links and assets must go through `relative_url` so they get the `/blog` prefix:

```md
![Statewide totals]({{ '/content/statistics/2020_election_series/01_virginia/img/statewide-totals.png' | relative_url }})
```

#### Renaming breaks links

Several link targets are derived from names, so renaming the name silently moves the target. A link to a missing heading (`#…`) just opens the page at the top; a link to a missing page gets the site's 404 page, which points to the topics and the archive. Before renaming any of these, grep `content/`, `docs/` and `jekyll/` for references to the old form and update them in the same change:

| Renamed | Link target it changes | What breaks |
|---|---|---|
| Post file name or `date` | Post URL `/:year/:month/:day/:title/`, and the `post_url` name | Links and bookmarks to the post. A stale `post_url` fails the build. Once a post has been pushed, keep its old URL alive by adding it to the post's front matter as `redirect_from: [/yyyy/mm/dd/old-slug/]`. |
| Section or group `id` in `jekyll/_data/tree.yml` (titles are safe to rename) | Landing-page anchor `/#<id>` | Links such as `{{ '/#ai-coding' \| relative_url }}` still open the page but no longer jump to or expand the group. |
| A post heading | Its table-of-contents anchor, unless it has an explicit `{#id}` | `#section` links into the post. |
| An idea directory or image file | Asset paths under `/content/...` | Images in the post 404. |

Every generated figure or asset needs a checked-in reproducible script; see [content_structure.md](../workspace/content_structure.md) for where `src/` and `img/` go.
