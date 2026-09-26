why not other methods
- compaction
    - loss control over what it chooses to save
    - similar in cost to just kill the session and reseed with what you want (now its pure context instead of bloated/polluted with all the tool calls and such)
- just kill the session and have it write a summary
    - what happens if its gone squirrely before you write that summary?
- just hold onto the old session - cache tokens are cheap now
    - cache-miss happens after a certain amount of time so it has to reload the whole thing as input tokens
    - how do you share something like that (expect a human to read from it)
    - how do you pass it off to another agent without making it have to read all the garbage tool call stuff and everything
    - you have to rely on their organizational methods instead of being able to use things like git to share and track diffs and all that
    - you can edit these in line





Tracking and creating our own context has been fundamental to how the DS team works. The working doc is your context layer: instead of relying on Claude's components to remember what you want, keep it in a doc that multiple sessions read and write.
- **Saveable:** persists after the session ends.
- **Shared across sessions:** several sessions can work on the same doc at once.
- **Under your control:** you decide what's kept and what's cut.
- **shareable artifacts with colleagues**: creates a nice evidence dump to share - I remember trying out the long context window before (when opus 5.5 came out with cheap cache tokens) and got it up to 500k and it was working out but in the end I needed to share something and show what i just spent 2 hours working on - I cant give someone this conversation and it didnt summarize the evidence very well of all the little mental exercises I did (I had it try agent vs skill implementations) - so I just got left with the idea of what they said to share with colleagues and I'll redo it again later


## Compaction fundamentals

Mechanics:
- **Trigger:**
    - auto: as context approaches the window limit
    - manual: `/compact [focus instructions]`, e.g. `/compact keep the open hypotheses`
    - related: `/context` shows current usage; `/clear` is the no-summary alternative
- **What gets compacted:** the conversation — messages, tool calls, file reads
    - one model pass reads it (e.g. ~300K tokens) and writes a structured summary that replaces it
    - most recent turns are usually kept as-is
    - summary size: not documented; likely a few K–20K tokens (inferred)
- **What's kept verbatim:**
    - system prompt (incl. org managed settings)
    - `CLAUDE.md` / `AGENTS.md` / memory index
- **Lost in the summary:** exact tool outputs, file contents, fine-grained reasoning
    - → Claude may need to re-read files afterward

Cost ([prompt-caching docs](https://code.claude.com/docs/en/prompt-caching.md), [pricing](https://platform.claude.com/docs/en/about-claude/pricing)):
- Input is mostly **cache reads** (0.1× base input price; 0.05× on Opus 5.5) — docs: "a mid-session `/compact` costs a fraction of what the context size suggests and spends most of its time generating the summary."
- Main new cost = summary **output tokens**.
- Next turn pays a one-time **cache write** (1.25× for 5-min TTL, 2× for 1-hr) on the much shorter summary prefix.

### Token rates — which ones this setup hits

Opus 5.5, $/MTok:

| Rate | × base | $/MTok | Billed when | Hit here? |
|---|---|---|---|---|
| Cache read | 0.05× | $0.20 | prefix still cached (within TTL) | yes — bulk of every turn |
| Cache write, 1-hr TTL | 2× | $8 | new tokens each turn; full prefix after TTL expiry | **yes** |
| Cache write, 5-min TTL | 1.25× | $5 | same, shorter TTL | no |
| Plain input (base) | 1× | $4 | tokens outside the cached prefix | ~0 (2 tokens/turn) |
| Output | — | $20 | generated tokens | yes |

- This setup runs a 1-hr TTL (verified 2026-09-25: session transcript `cache_creation` shows only `ephemeral_1h_input_tokens`, 0 on `ephemeral_5m_input_tokens`).
- Sample turn (verified, same transcript): 49,750 cache-read / 719 1-hr write / 2 plain input tokens.
- The write premium over base pays for the processed prefix being held server-side for the TTL. A 1-hr write breaks even after ~2 reuses; the TTL resets on every cache hit.
- → Examples below price all writes at **$8/MTok**. Plain input is effectively never hit in a Claude Code session.

### Compaction cost example

Opus 5.5 (cache read $0.20/MTok, output $20/MTok, 1-hr cache write $8/MTok; summary size assumed):

| Context → summary | Read (cache) | Summary (output) | Cache write, next turn | **Total** | Context after (+ ~27K startup) |
|---|---|---|---|---|---|
| 250K → 10K | $0.05 | $0.20 | $0.08 | **$0.33** | ~37K |
| 250K → 20K | $0.05 | $0.40 | $0.16 | **$0.61** | ~47K |
| 300K → 10K | $0.06 | $0.20 | $0.08 | **$0.34** | ~37K |
| 300K → 20K | $0.06 | $0.40 | $0.16 | **$0.62** | ~47K |

- The 250–300K already includes the ~27K startup (measured, see reseed example below), so the read cost is unchanged; startup stays cached across the compaction (inferred), so only the summary is re-written.
- Summary output is ~60–65% of the cost; context size barely moves it.
- Break-even: each later turn reads ~37–47K instead of ~300K (saves ~$0.05/turn) → pays back in ~7–12 turns.
- Expensive case is a **cold cache**: re-writing 300K to cache = ~$2.40 at the 1-hr cache-write rate (e.g. forgetting to `/compact` before a meeting that outlasts the TTL - or simply warming it back up after that meeting).
- Not yet verified via `/cost` before/after a real `/compact`.

### Reseed-from-docs cost example

Fresh session, Opus 5.5. Dummy scenario: 3 hand-curated md docs, ~10 pages each (~30 pages is a lot of context to get right).

- **Startup:** a clean session loads **~26.6K tokens** before you type anything (measured: `claude -p "Reply with just OK." --output-format json` from `ml_context/`, 2026-09-25).
- **Docs:** 3 × 10 pages ≈ **20–26K tokens** (est., ~0.75 words/token, +30% for the newer tokenizer).

| | Tokens | Cost |
|---|---|---|
| Startup → 1-hr cache write (tokens measured) | 26.6K | $0.21 |
| Docs → 1-hr cache write | 20–26K | $0.16–$0.21 |
| Re-reading the growing prefix across ~4 turns (3 reads + reply) | ~150–200K cache reads | ~$0.03–$0.04 |
| **Total** | **~47–53K context** | **~$0.40–$0.46** |

- About the same cost as one compaction ($0.33–$0.62).
- But the context is very different: ~20–26K of docs **you hand-selected and can read, edit, and share**, vs 10–20K of whatever the model judged most important out of 250–300K.
- A compaction summary can't be reviewed or corrected. If you want to give it feedback, you'd end up having it write to an md doc anyway.

### slack summary

Compaction vs reseeding with a tracking doc worked example assuming either 250k or 300k of a context window that you either compact down to 10 or 20k with /compact (which uses cache token reads) or you simply start a new session and reseed (with "input token reads") with AN ENORMOUS amount of context (say 3 10 page md files).  They are roughly equivalent in cost but in my opinion the reseeding far outweighs in user experience.

- You choose your own 30 pages of context vs trusting the LLM to do a better job than you do at summarizing and throwing out the garbage pieces of the conversation
- the context persists and is also shareable with other sessions later (or other teammates, etc) if you track it with git (vs relying on anthropic tooling to let you find and organize old conversations - not to mention finding relevant pieces of information in a long conversation history)
- you have that ability to hit eject at any moment the LLM starts being squirrel-y (as Nick puts it)
- not to mention this is WAY more expensive if you have cold start from an old session of 300k (vs every morning I can do this reseeding without worrying about it)
- ben response
    - nice analysis. personally, the method described requires more discipline than I have :slightly_smiling_face: Am glad compaction is inline with manual prompting approach. I think the cold start problem relies on discipline to either compact before loosing the cache, or extracting the prompt ahead of time, right? or am I not reading correctly. As an aside, it looks like the TTL for caching in CC is 1 hour by default, tmyk!
    - sean reply - yeah that's definitely how I'd think about it - you'd have to "remember" to do it before you went to lunch or something vs if it just part of your workflow to track things in a doc, its always the same
    - not sent - its in line with - lets not forget that "we are expensive actually" and these workflows shouldn't optimize for cents but for things like predictability, ease of sharing/expanding upon, giving the smart humans more free thinking space etc etc (could you imagine trying to search through a 300k context conversation to find the part you remembered was useful)
- ben on commiting compactions
    - https://code.claude.com/docs/en/hooks#precompact
    - mos def, the hook system is pretty neat, im impressed with CC as far as adaptability
    - so looks like you can get the transcript before an after a compaction event
    - if you wanted to commit it somewhere seems possible
    - sean response - I still feel like you'd be trusting the LLM too much - to determine what it deems is what I want to take from the conversation (a lot of mine are full of ITS responses that aren't always what i wanted) (edited) -- but in a pinch that's really helpful information
