# Blog

A Markdown-first Jekyll blog for GitHub Pages. It has no local build step: GitHub Pages builds it when changes are pushed to `main`.

## Publish it

In the GitHub repository, open **Settings → Pages** and select **Deploy from a branch**, then choose `main` and `/(root)`. The published URL will be `https://seanczak.github.io/blog/`.

## Write a post

Add `_posts/YYYY-MM-DD-a-short-title.md`:

```md
---
layout: post
title: "A short title"
date: 2026-09-02 09:00:00 -0700
description: "An optional one-line summary."
categories: [one-topic, another-topic]
---

Write the post in ordinary Markdown.
```

Posts are listed automatically on the homepage in reverse publication order: newest first. The filename and the `date` value determine that order; edit `date` if you want to correct or schedule a publication date. `categories` creates the category labels and makes the post available in the homepage category filter.

The right-hand “On this page” navigation is generated automatically from `##` through `######` headings and indents each level. Give a heading an explicit ID when you want to control its anchor, for example: `## Introduction {#introduction}`.

Put images in `assets/images/` and reference them with:

```md
![Alt text]({{ '/assets/images/example.png' | relative_url }})
```

This keeps image links correct when the site is served from the repository path (`/blog`).
