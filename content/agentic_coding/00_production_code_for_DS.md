# Agentic Coding for ML Model Pipelines - Part 1: The Principles

## Software Engineering Principles are Stable in an Agentic World

Go back to 2020. Development velocity bottlenecked on quality and maintainability: those who applied software first principles wrote maintainable code that could be extended, while those who didn't lost time to rework and debugging — patching new features in rather than building cleanly on top of what already existed.

The question is: do coding agents break that paradigm?  They let *anyone* generate functioning code extremely quickly, right?

Unfortunately, while this code may "function," it won't necessarily be written with respect to any set of principles.  Therefore, as the codebase builds, it becomes harder to extend, challenging to debug, and the agent itself can lose track of its own structure. The net effect is actually *slower* delivery — complex bugs, duplicated logic, a slower PR process, and an inability to build on prior work. In my experience this can happen fast.

So in an agentic coding world the fundamentals of software engineering are incredibly stable. In fact, they matter more than ever.

## Introducing the series

This series covers how I wrangle agents into writing maintainable, extendable code. This article starts with a few small readability tips — quick ways to clean up code. The follow-ups each take a single topic that's important enough to warrant its own article:

- **Part 2: DRY / write it once** — keeping the agent from repeating logic or hard-coding strings and parameters inline. Define each thing in one place; then a change (or building off that logic) only has to happen in that single spot, and everything else pulls from it.
- **Part 3: Principled organization** — singly-responsible functions structured around separation of concerns and generalization. The payoff: code that's easy to traverse and debug, where complex functionality gets built by reusing existing code rather than adding more spaghetti.
- **Part 4: Agentic coding best practices** — how to actually wrangle agents into doing the above and get the productivity boost everyone talks about. The earlier articles build to this one.

**Scoping note:** everything here applies to code meant to be maintained and extended — e.g. a model pipeline. It does *not* apply to throwaway analysis code, where minimal intervention can actually be the right call: nothing gets built on top of it, so there's no maintenance cost to defer. I plan to write separately on how I no longer use Jupyter notebooks for EDA in the agentic era.

## Miscellaneous Readability Tips

These are simple fixes, but still important — in my experience agents genuinely fall short on them. I'm collecting them here as a grab-bag and may add more as I think of them.

### YAGNI — remember to remove stale code

Agents seem reluctant to delete code. I imagine it might be that they're post-trained to produce functioning code and so perhaps a codebase with some an unreferenced functions still passes the unit tests. Thus, there may be little signal pushing them to remove them. I'd also imagine the labs don't want their agents accidentally deleting whole modules or codebases of their users.  As a result, they might've erred toward leaving too much stale code rather than cutting too much functional code.

There's a funny acronym in software development for the opposite instinct: YAGNI — "you aren't gonna need it." It's aimed at the temptation to keep a function around *just in case I need it later*. You won't, usually — and dead code confuses agents and humans alike. I have an interesting anecdote about that...

I once discovered a case where, to the human eye, the "real" implementation lived in the obvious spot — properly named, well-scaffolded, all the production safeguards (connection checks and other fail-safes) wired into it. The only problem, it was dead - not referenced anywhere else in the code. The agent had kept assuming that the correctly-named function was the live one, and the code that actually ran was hidden somewhere less obvious with none of those safeguards attached. When I raised it with a teammate it surprised them too — they'd been adding those fail-safe measures for a while, all onto code that never executed.

So the simple tip: do your best to prompt the agent to delete stale code because leaving it around can cause real problems down the road. (This is what git is for anyways if you reaallllly want it back later.)

### Naming Conventions

I'll admit that refactoring an active codebase toward appropriately named elements can feel daunting — but done in small chunks it's manageable, especially today when the agent does it for you.

This matters more now because in the agentic coding world we're bottlenecked by PR review more than by code writing. Someone (maybe you, maybe a teammate) has to read this code and give the agent feedback — so readability pays off directly. Do a little at a time and eventually you'll find you're:

- making the code more readable for your reviewers,
- saving time in debugging,
- building more complex functionality on a foundation you're constantly improving (e.g. being able to trace similarly named elements across the codebase is a huge productivity boost)

Obviously each dev team is going to land on their own conventions and this could be a really polarizing topic, but here are a few guidelines I use. The point is to get the agent to follow *some* sort of reasonable convention so that you are able to acheive those gains listed above.

**Avoid vague, throwaway names.** 

Names like `temp`, `val`, `item`, `info`, `mgr`, or the ever-present `data` tell a reader nothing — and agents reach for them constantly. Swap them for something that says what the thing actually is: `raw_invoices` instead of `data`, `retry_count` instead of `val`, `customer_name` instead of `item`. Single-letter names get the same treatment; the only ones I'll keep are `i`/`j` as indices in a genuinely mathy loop.

**Name functions and classes by their role.** 

I think of functions as *verbs* and classes as *nouns*, and stick to that for the most part. Take a training dataset `TrainingDset`: it's a class, so it holds the relevant attributes which might be nouns like: the dataframes for wrangling features into a training ready form. But it also holds methods alongside the attributes that act on them. These are verbs like - `split_dataset` or `reformat_timestamps`.

A good habit that falls out of this: start every function name with a strong imperative verb that says what it does — `load_raw_invoices`, `encode_categoricals`, `compute_churn_rate`. If the best name you can come up with is a bare verb like `prep_dataframe()`, that's usually a hint the function is doing too much to name cleanly.

**Encode a variable's type in its name.** 

Append the type — or a short slug of it — to the variable name so the form is obvious at a glance. If a date is represented as a string, I tack a little `_str` on the end; if it's a month-level representation, include that too (e.g. `month_str`). I lean on this especially with pandas objects, where it's otherwise hard to tell whether something is a `dict`, a `tuple`, or actually a dataframe — so `_df` for dataframes and `_ser` for series really helps.

**Be consistent.** 

Once you've named things well, use the same name for the same concept everywhere — especially when it's referenced in multiple places. It makes the code much easier to debug and extend. For example, one convention I've settled on across a lot of my projects: an instance of the config class is always `cfg` (or `self.cfg` when it's inside a class).
