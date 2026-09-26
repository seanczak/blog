# Blog

The docs below define how to work here. Each is listed with an `@` so it's loaded at the start of every session: Claude Code pulls `@` files in automatically, through this file and `CLAUDE.md`. Any other agent should read all of them before its first action.

Token counts were measured 2026-09-26 (Claude Code 2.1.283) as the extra startup context each import adds on its own. All seven together add ~11.1K tokens on top of a ~29.4K baseline (~40.5K total). They're rough and not kept current, so they may drift a little as the docs change; that's expected and needs no flagging. Re-measure (method in `docs/agent_guidelines.md`) only when the human asks.

- @docs/agent_guidelines.md (1.3K tokens): your role, reading context documents, numbers, figures, keeping the docs current, tools, git.
- @docs/writing_style.md (1.5K tokens): register, structure, and voice for notes, outlines, posts, docs, and chat.
- @docs/coding_style.md (2.5K tokens): Python and SQL conventions for code in `src/`.
- @docs/repo_structure.md (0.8K tokens): the repo root and keeping it clean.
- @docs/content_curation.md (2.1K tokens): idea directories in `content/`, notes → outline → post, naming, what gets tracked or kept in `notshared/`.
- @docs/publishing_with_jekyll.md (2.3K tokens): post front matter, publishing, `_config.yml` and `jekyll/`, local preview.
- @docs/site_design.md (0.7K tokens): style, header, landing-page tree, archive and article pages.

## Skills

Skills live in `.claude/skills/<name>/SKILL.md`. Claude Code discovers them automatically; other agents should open the matching `SKILL.md` when a request fits. There is one so far:

| Skill | Use when |
|---|---|
| `make-figure` | any image goes into an idea's `img/`: a chart from a data file (it also saves a rerunnable plot script in `src/`), or a photo, diagram or imported figure. Every image is compressed with its helper |
