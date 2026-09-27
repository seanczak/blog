# Blog

The docs below define how to work here. Each is listed with an `@` so it's loaded at the start of every session: Claude Code pulls `@` files in automatically, through this file and `CLAUDE.md`. Any other agent should read all of them before its first action.

Token counts were measured 2026-09-26 (Claude Code 2.1.283) as the extra startup context each import adds on its own. All seven together add ~11.1K tokens on top of a ~29.4K baseline (~40.5K total). They're rough and not kept current, so they may drift a little as the docs change; that's expected and needs no flagging. Re-measure (method in `docs/workspace/agent_guidelines.md`) only when the human asks.

- @docs/workspace/agent_guidelines.md (1.3K tokens): your role, reading context documents, numbers, figures, keeping the docs current, tools, git.
- @docs/workspace/repo_structure.md (0.8K tokens): the repo root and keeping it clean.
- @docs/workspace/content_structure.md (2.1K tokens): idea directories in `content/`, notes → outline → post, naming, what gets tracked or kept in `notshared/`.
- @docs/style_guides/writing.md (1.5K tokens): register, structure, and voice for notes, outlines, posts, docs, and chat.
- @docs/style_guides/coding.md (2.5K tokens): Python and SQL conventions for code in `src/`.
- @docs/site/publishing.md (2.3K tokens): post front matter, publishing, `_config.yml` and `jekyll/`, local preview.
- @docs/site/design.md (0.7K tokens): style, header, landing-page tree, archive and article pages.

## Skills and subagents

Skills live in `.claude/skills/<name>/SKILL.md` and subagents in `.claude/agents/<name>.md`. Claude Code discovers both automatically; other agents should open the matching file when a request fits and follow its steps themselves.

| Skill or subagent | Use when |
|---|---|
| `make-figure` (skill) | any image goes into an idea's `img/`: a chart from a data file (it also saves a rerunnable plot script in `src/`), or a photo, diagram or imported figure. Every image is compressed with its helper |
| `pages-build-check` (subagent) | after a push to `main` that changes the built site (see `docs/site/publishing.md`), in the background, with the pushed SHA. Reports the Pages build outcome and the hard-refresh reminder |
