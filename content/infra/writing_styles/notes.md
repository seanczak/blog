2026-09-26, requested by Sean Fronczak: observations on his blog writing style, drawn from the posts moved onto the blog so far. Not yet folded into `docs/style_guides/writing.md`; its "blog document specific styles" section stays as just the link to Part 1 for now.

# Blog writing style: observations

## Sources

All six posts were read in full while they were imported or edited (Medium originals via the RSS feed, Part 1 from its notes).

| Written | Post | Weight |
|---|---|---|
| 2020-11-06 | [What in the World Happened in Virginia Tuesday Night?!](../../statistics/2020_election_series/01_virginia/_posts/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night.md) | older |
| 2020-11-09 | [Calling Elections Early: Fake News or Statistics?](../../statistics/2020_election_series/00_calling_elections_early/_posts/2020-11-09-calling-elections-early-fake-news-or-statistics.md) | older |
| 2020-11-09 | [How Swing-able is Texas Anyways?](../../statistics/2020_election_series/02_texas/_posts/2020-11-09-how-swing-able-is-texas-anyways.md) | older |
| 2020-11-09 | [What Took So Long in the Swing States?](../../statistics/2020_election_series/03_swing_states/_posts/2020-11-09-what-took-so-long-in-the-swing-states.md) | older |
| 2021-01-01 | [An Approximation for Financial Independence](../../personal_finance/00_base_model/_posts/2021-01-01-an-approximation-for-financial-independence.md) | older |
| 2026-09-19 | [Agentic Coding for ML Model Pipelines - Part 1](../../ai/ai_code_workflow/00_production_code_for_ds/_posts/2026-09-19-agentic-coding-for-ml-pipelines-part-1.md) | current voice |

Timeline matters: the first five are Medium posts from 2020–2021. Part 1 is the only one written recently, and the author confirmed it's closest to how he writes now, so it carries the most weight. Everything below is one reader's interpretation of a small sample, not a checked rule.

## Traits in the current voice (Part 1)

| Trait | Where it shows |
|---|---|
| Prose-led; lists only for true enumerations | Body is paragraphs; bullets only for the series roadmap and the three payoffs |
| Opens by framing a question against a past baseline | "Go back to 2020… The question is: do coding agents break that paradigm?" |
| First person, experience as evidence | "In my experience this can happen fast"; the dead-code anecdote |
| Speculation about causes is flagged as speculation | "I imagine…", "perhaps…", "I'd also imagine the labs…" |
| Explicit scope of the advice | The bold **Scoping note:** on throwaway analysis code |
| Owns subjectivity; rules offered as personal practice | "this could be a really polarizing topic… here are a few guidelines I use" |
| Bold one-line lead-in per rule, then a short paragraph | **Avoid vague, throwaway names.** and the rest |
| Concrete before/after examples | `raw_invoices` instead of `data`, `retry_count` instead of `val` |
| Each tip tied to why it matters | Naming matters because PR review is the bottleneck |
| Light, casual register with small humor | "wrangle agents", "reaallllly", parenthetical asides |
| Written as a series | Roadmap of parts; short conclusion ending "stay tuned" |
| Frequent em dashes | Throughout |

## Traits only in the 2020–2021 posts (possibly outdated)

- Rhetorical questions every few lines ("Well, why not?", "How?").
- Exclamation marks and ALL CAPS for emphasis ("NOT EVERYONE VOTES!!!").
- Playful section titles ("Oh, Confound it!", "Marbles again?").
- Blockquotes as pull quotes ("The statistician… has no clothes.").
- Stage directions ("{deep inhaling}", "{big exhale}").
- One analogy carried through a whole series (marbles → bags within bags → Russian dolls).
- Continuous with Part 1: parenthetical humor, stretched spellings, stated assumptions, series cross-links, short takeaway endings.

## Open questions

- **Section titles.** `docs/style_guides/writing.md` says titles "name the question being asked", scoped to exploratory `notes.md`. Part 1's titles state the answer ("Software Engineering Principles are Stable in an Agentic World"). A blog section would need to say which applies to posts.
- **Which traits to adopt.** Undecided which of the current-voice traits become rules for posts, and whether any older traits carry forward.
