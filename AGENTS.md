# Blog

## Preview and GitHub

- Preview: `/home/sfronczak/snap/code/259/.local/share/gem/ruby/3.0.0/bin/jekyll serve --host 127.0.0.1 --port 4001`, then open `http://127.0.0.1:4001/blog/`.
- GitHub CLI: `/home/sfronczak/.local/bin/gh`.
- The visible name is **Sean Fronczak**; GitHub username/base path remain `seanczak` and `/blog`.

## Design and behavior

- Quiet editorial style: grey base, turquoise (`#087f86`) for content links/interaction, opaque gold (`#c6a34b`) for 2px structural dividers and portrait trim.
- Header: portrait, name, then Posts / About / LinkedIn. Header links are charcoal and turquoise only on hover.
- Homepage: chronological posts with a sticky right-hand Categories filter; no hero, “Writing” heading, or card-heavy design.
- Articles: categories appear beneath the title; the right-hand “On this page” TOC is generated from `##`–`######` headings and hides below `56rem` viewport width.
- Implement dynamic state programmatically and deterministically. Do not use DOM-position selectors (for example `:first-child`) for filtered/sorted state; derive it from visible data and apply explicit classes. Generated figures/assets need a checked-in reproducible script.

## Posts

Create `_posts/YYYY-MM-DD-short-title.md` with `layout`, `title`, `date`, `description`, and `categories` front matter. Descriptions and categories power the archive/filter. Ask the human for one to three categories if they have not specified them; do not invent them. Posts sort newest first by `date`.

Use `##`–`######` headings for the automatic TOC; add an explicit heading ID only when a stable anchor is needed, e.g. `## Introduction {#introduction}`.
