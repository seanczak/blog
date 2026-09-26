# Blog

Workspace for exploring ideas and source for https://seanczak.github.io/blog/. GitHub Pages builds the site with Jekyll from `main`, so pushing to `main` publishes. The repo is public; private material goes in `notshared/`.

- `content/<area>/<idea>/`: one directory per idea, with notes, an outline, and a nested `_posts/` for the published article.
- `jekyll/`: layouts, CSS, images, landing page, archive, About page, the topic tree data, and local preview tooling.
- `docs/`: repo conventions.
- `notshared/`: gitignored private scratch space.
- `_config.yml`: Jekyll config; stays at the root because GitHub Pages reads it there.

## Docs

Agents read all of these at the start of every session. The entry point is [AGENTS.md](AGENTS.md), so the same instructions work in both Codex and Claude Code: Codex reads AGENTS.md natively, and [CLAUDE.md](CLAUDE.md) only imports it. AGENTS.md lists each doc as an `@` import, which Claude Code loads automatically; Codex opens them from the listed paths.

| Doc | Covers |
|---|---|
| [docs/workspace/agent_guidelines.md](docs/workspace/agent_guidelines.md) | how agents work here: role, context documents, numbers, figures, keeping docs current, tools, git |
| [docs/workspace/repo_structure.md](docs/workspace/repo_structure.md) | the repo root and keeping it clean |
| [docs/workspace/content_structure.md](docs/workspace/content_structure.md) | idea directories: notes → outline → post, naming, what isn't tracked |
| [docs/style_guides/writing.md](docs/style_guides/writing.md) | how to write notes, outlines, posts, docs, and chat replies |
| [docs/style_guides/coding.md](docs/style_guides/coding.md) | Python and SQL conventions |
| [docs/site/publishing.md](docs/site/publishing.md) | GitHub Pages, local preview, post front matter |
| [docs/site/design.md](docs/site/design.md) | style, header, landing-page tree, archive and article pages |

## Preview locally

```bash
jekyll/serve.sh
```

Then open http://127.0.0.1:4001/blog/. The first run installs the same Jekyll version GitHub Pages uses into `jekyll/vendor/`.
