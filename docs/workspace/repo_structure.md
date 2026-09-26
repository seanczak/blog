# Repo Structure

```text
blog/
├── content/      # ideas: notes, outlines, and posts (docs/workspace/content_structure.md)
├── docs/         # repo conventions: workspace/, style_guides/, site/ (listed below)
├── jekyll/       # how the site is built and served (docs/site/)
├── notshared/    # gitignored private scratch space
├── _config.yml   # Jekyll config; GitHub Pages reads it only from the root
├── .gitignore
├── README.md
├── AGENTS.md     # agent entry point; indexes these docs
└── CLAUDE.md     # imports AGENTS.md for Claude Code
```

## Keep the top level clean

The root holds only what's listed above. Everything else goes one level down: the Jekyll `Gemfile` and preview script live in `jekyll/`, and figure scripts live in their idea's `src/`. Before adding a file or directory at the root, check whether it fits in an existing directory, and ask the human if it doesn't.

## Where the details are

| Doc | Covers |
|---|---|
| [workspace/agent_guidelines.md](agent_guidelines.md) | how agents work here: role, context documents, numbers, figures, keeping docs current, tools, git |
| [workspace/content_structure.md](content_structure.md) | `content/`: idea directories, notes → outline → post, naming, what isn't tracked |
| [style_guides/writing.md](../style_guides/writing.md) | how to write notes, outlines, posts, docs, and chat replies |
| [style_guides/coding.md](../style_guides/coding.md) | Python and SQL conventions |
| [site/publishing.md](../site/publishing.md) | `jekyll/` and `_config.yml`: GitHub Pages, local preview, post front matter |
| [site/design.md](../site/design.md) | how the site looks and its pages behave: style, header, landing-page tree, archive, articles |

The repo is public. `notshared/` is gitignored at every depth, so anything private goes in the nearest `notshared/`.
