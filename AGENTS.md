# Blog workspace notes

GitHub CLI is available at `/home/sfronczak/.local/bin/gh`. Use it for GitHub operations when appropriate.

## Local preview

Jekyll is installed in the user Ruby gem directory. Preview the site with:

```bash
/home/sfronczak/snap/code/259/.local/share/gem/ruby/3.0.0/bin/jekyll serve --host 127.0.0.1 --port 4001
```

Open `http://127.0.0.1:4001/blog/`. Jekyll watches the repository and rebuilds after file changes; refresh the browser to see them. Run the command outside the filesystem sandbox (or with permission to bind the local port).

## Site conventions

- The visible author name is **Sean Fronczak**. The GitHub username and site base path remain `seanczak` and `/blog`.
- Keep the design quiet and editorial: grey is the primary palette, turquoise is a restrained interactive accent, and opaque gold is reserved for structural trim.
- Use `#c6a34b` for the 2px gold dividers (header, post list, footer) and profile-image trim. Do not introduce additional competing accent colors.
- Regular content links use turquoise (`#087f86`). Header navigation links are muted charcoal (`#555f64`) and become turquoise only on hover; do not make them permanently blue/turquoise.
- The homepage is a posts archive with a right-hand, sticky Categories filter. Preserve that layout rather than reintroducing a hero, a “Writing” heading, or card-heavy styling.
- Keep the portrait in the header, at the left of the site title. The right-side header navigation is Posts, About, and LinkedIn.

## Writing posts

Create posts in `_posts/YYYY-MM-DD-short-title.md`. Use this front matter:

```yaml
---
layout: post
title: "Post title"
date: 2026-09-02 10:00:00 -0700
description: "A concise one-sentence archive summary."
categories: [experimentation, statistics]
---
```

- `description` and `categories` are required: they power the homepage listing and its category filters.
- Ask the human which one to three categories a new post should use if they have not specified them; do not invent categories without confirmation.
- Posts are automatically sorted newest first by `date`.
- The right-hand “On this page” navigation is generated automatically from `##` through `######` headings, indenting each level programmatically. Use explicit heading IDs when a stable anchor is useful, for example `## Introduction {#introduction}`. Keep categories beneath the article title; do not put them in the right-hand navigation.
