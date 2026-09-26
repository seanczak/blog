
# What is a skill vs agent in .claude/

> Outline — sections to be filled in. Longer version: `ml_context/docs/adr/003_agent_context_management.md`.

## Motivation

This started as a look at the difference between skills and agents. Along the way it became clear they're two of four components for handling repeated work, and the real question is how to design an architecture that combines them:

- **Skills**
- **Agents**
- **Always-loaded context** (`CLAUDE.md` / `AGENTS.md`)
- **Code** — not new, but still the right call for deterministic tasks

The first three are new and are what I want to investigate here.

## Comparing Skills and Agents

### Similarities

Skills and agents are more alike than different. They sit next to each other in `.claude/`:

```
.claude/
├── skills/
│   └── mlc-DS-exploration-agent/
│       └── SKILL.md
└── agents/
    ├── mlc-make-figure/
    │   └── AGENT.md
    └── mlc-query-redshift/
        └── AGENT.md
```

and share the same basics:
- Encode repeatable work or behavior as instructions: a markdown file, YAML frontmatter on top, instructions in the body.
- Discovered the same way: main Claude sees each `name` + `description` and decides when to use it; you can also call either by name.
- Can pin a model and restrict tools in frontmatter.\*

\* A skill's settings last only for the turn it runs in; an agent's apply to its whole run.

### Differences

#### Context handling

A skill keeps adding to the main thread; an agent keeps it clean, at the cost of a hand-off in (the prompt) and out (the report).

| | What the task sees | What the main thread keeps |
|---|---|---|
| **Skill** | • main thread context history<br>• its instructions | Everything: the skill's instructions, every tool call, every output |
| **Agent** | • prompt from main thread<br>• its instructions<br>• a base system prompt\*\* | Only the prompt it wrote + the agent's final report |

\*\* Base system prompt: harness + org settings. Exactly what loads for a custom agent is unverified.

*Side note — forked skills:* a skill with `context: fork` in its frontmatter runs in a clean context instead of the main thread, so it handles context like an agent.

#### Where and how it runs

| | Runs in | Background / foreground | Parallel | Talks with you mid-task |
|---|---|---|---|---|
| **Skill** | Main thread, turn by turn | Foreground only; main thread busy until done | No, unless main Claude spins up one agent per skill call | Yes (e.g. the AI-eng skills that ask you questions) |
| **Agent** | Its own context | Either, set per call with `run_in_background: true/false` | Yes, several per message (foreground or background) | No; returns one final report |

## Other Design Components

All of these components exist so you don't have to repeat yourself (the good kind of engineering laziness), and the design question is which mix is the most cost-efficient for your work. Skills and agents alone won't get you there; there are other components to consider when designing a workflow.

### Don't forget: tracking and creating your own context

Tracking and creating our own context has been fundamental to how the DS team works. The working doc is your context layer: instead of relying on Claude's components to remember what you want, keep it in a doc that multiple sessions read and write.
- **Saveable:** persists after the session ends.
- **Shared across sessions:** several sessions can work on the same doc at once.
- **Under your control:** you decide what's kept and what's cut.
- **shareable artifacts with colleagues**: creates a nice evidence dump to share - I remember trying out the long context window before (when opus 5.5 came out with cheap cache tokens) and got it up to 500k and it was working out but in the end I needed to share something and show what i just spent 2 hours working on - I cant give someone this conversation and it didnt summarize the evidence very well of all the little mental exercises I did (I had it try agent vs skill implementations) - so I just got left with the idea of what they said to share with colleagues and I'll redo it again later

### Third repeatable-task option: always-loaded environment context (`CLAUDE.md` and `AGENTS.md`)

Sometimes called "system" context: in every session from the first turn, never triggered.

Until recently, DS exploration leaned mostly on this option: documentation chained into the context window (`CLAUDE.md` → `AGENTS.md` → other docs), so every session started with the conventions loaded.

**Mechanism:** loaded once at session start and stays at the top of the context window, so it's re-sent, and billed, on every turn (mostly as cache reads, ~0.1× the input price).
  - It sits alongside the org's base system prompt (the Pax8 instructions loaded into every session), which is the part that's closer to an "actual" system prompt.

**Pros:**
- **Right home for repo-wide conventions:** anything every task needs (e.g. file structure, writing style, git rules) is always there, so the per-turn cost is well spent.
- **Least engineered:**
  - Chaining skills and agents into a system takes thinking up front, so it's worth checking there's a payoff first. The best candidates are highly repeatable tasks that are self-contained but still part of a workflow. That's probably true in some cases and not in others.
  - In my experience skills and agents are also still fairly clunky and non-deterministic.
- **Predictable:** a clean session starts with exactly what you expect loaded and ready to go.

**Cons:**
- **Paid for even when unused:** anything only some tasks need is still billed on every turn; put it in a skill or agent so it only loads when used.<br>---- Workarounds:
  - Keep sessions for tasks that don't need these conventions short (few turns).
  - Use a model with cheap cache reads. The up-front write is a few cents; the repeated reads are what add up. Opus 5.5 reads are cheaper than Sonnet 4.6's (\$0.20 vs \$0.30 per M tokens, list prices), so a big model that can handle exploration is also cheap to keep context on.
- **Context rot:** as a session gets long, early instructions (e.g. "use this tone, keep replies short, put units on numbers") get followed less, and you end up repeating yourself.<br>---- Workarounds:
  - Start clean sessions often.
  - using a better model - I feel like sonnet forgets WAY faster than opus and the same with the jump to fable (also felt like the 5 series was really bad at this too)
  - Accept a little repetition; after a reminder or two it picks the preference back up (bullets over walls of text, etc.). In practice it's not much.
- **One model for the whole session:** you can't send a simple task to Sonnet or Haiku. (A skill can override the model for the turn it runs in, then the session model resumes.)<br>---- Workarounds:
  - Run a separate session on a smaller model for the simple tasks, working on the same doc.
- **Foreground only:** you're blocked while it works.<br>---- Workarounds:
  - Run a few sessions at once on the same doc, e.g. one making plots and running queries, another editing text.
  - Start clean sessions often.

### Fourth repeatable-task option: code

Deterministic tasks should still be code, with the LLM wrapped around them for the non-deterministic parts.
- **Redshift queries:** run through a script (`query_redshift.py`), not written out and run by hand each time.
- **GitHub:** the `gh` CLI does the job with much less overhead than the GitHub MCP.
- **Atlassian (Jira / Confluence):** the same may hold for a CLI vs the MCP; not investigated yet.



## Designing an agentic work environment

### Start with the needs of your work

- Interactive persona → skill
- Closed-form subtask (figures, SQL pulls) → agent
- Trivial / one-off → inline

### Models to run

- check how much cheaper opus 5.5 is - basically show that the cost of using opus and these long chain workflows just plummeted the decision to not fill up the cache
    - we need the pax8 system context
    - estimate how much the docs are in the context window at the start from that agents md chain
    - then just say ok if we were running in opus the first turn costs this much to have it all in context and the the next turns cost this much - plot is cost vs turns and put opus 5, 5.5, sonnet 5, 4.6, fable 5
        - could maybe even put in like an assumption that each term is this many input tokens in this output tokens - define the analytical equation and just plot it
        - this also assumes that they take the same amount of time to do the same task which isn't quite right either
    - basically how expensive is it to say hello is the first turn
    - i actaully think 2 plots - one that is this is how expensive it is to have the pax8 org costs and two more for what the just agents.md costs with two different amounts of what you put in there (just to say, be careful with how much you put in there)
    - takeaways from this are probably that opus 5.5 is further democratizing technical work - it started with the models letting everyone code and now you don't even really have to know how to use the models super well in this like ultra efficient think about it way
        - I think one of the things that really stays as a pattern that has stain power, as a pattern is that you should still be tracking your own progress rather than relying on anthropic to do it well, trusting the agents to do it probably isn't the way still
        - the optimal zone is really flat now in terms of the design choices - whereas before it was super spikey and you really needed to know how to do the sophisticated, well-thoughtout orchestration of skills (I think we continue to see this - and so the argument will continue to go in the way of the least engineered solution and just see what the industry does to change and fix things)

- then do a model where we compare agents and skills
    - we have our pax8 org context that will go into the agent
    - we have the amount of cache 

## Takeaway from the test (optional)

- Subagents vs inline, 2 figures, n=2 runs: cost and wall time about even; main context ended ~9k tokens smaller (48.8k vs 58.1k).
- TODO: keep as one line with the small-n caveat, or drop.
