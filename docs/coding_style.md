# Coding Style

Covers Python and SQL, which here means the scripts under each idea's `src/`. These are defaults, not a checklist. Where a number appears, it's the point to pause and reconsider, not a quota. The overriding rule: write what a seasoned software engineer would sign off on.

## Organizing code

### Separation of concerns

- Reading inputs, transforming them, and producing output are distinct concerns. Each gets its own function, and typically its own module.
- When it's unclear where a seam belongs, ask the human rather than guessing.
- The layout will shift as a project grows. Agree on seams with the human; when new code no longer fits them, propose a restructure instead of forcing it in.

### Layout and names

- Keep the tree shallow. Module and directory names should say what's in them: `feature_encoding` over `utils`, `chart_styles` over `helpers`. A reader should be able to guess where something lives, and therefore whether it already exists, from the name alone.

### What stays out of logic

- Settings, sample or fixture data, lookup tables and environment-specific values are not written inline in function bodies. When they're needed, they get their own file; check with the human first, since something simpler may do.
- Queries live in `.sql` files, typically in a `sql/` folder beside the Python that reads them at runtime. This keeps editor highlighting and diffs readable and fits the one-statement-per-file rule under SQL.

## Don't Repeat Yourself (DRY)

Aim for one authoritative copy of every rule and value. This is a working habit, not a reason to search the whole repo before each change.

- Check the existing helper modules before writing a new function, mapping or utility.
- A given computation (a currency conversion, a timestamp format) is implemented once. If more than one module needs it, it moves to a shared location.
- The same goes for values. Constants, paths and strings that recur are defined in one place and imported. A literal pasted in three places breaks as easily as logic pasted in three places.
    - A small constants module is enough to start. A bigger project can graduate to a settings class that reads a YAML file and derives paths and per-environment values from it.
- Code that's no longer used is removed. Commenting it out "for later" isn't an option; git keeps history.

## Python

### Layout and characters

- PEP 8: four-space indents (never tab characters), lines up to 88 columns.
- `snake_case` for functions and variables, `PascalCase` for classes, `UPPER_CASE` for module constants.
- ASCII only in names, strings and comments; no emoji or emoji-like symbols.
- Use f-strings, `enumerate()` rather than hand-kept counters, and `is` when comparing with `None`, `True` or `False`.

### Naming

- A name should say what the thing is. Generic placeholders (`data`, `result`, `temp`, `stuff`, `thing`, `x`) and truncations (`mgr`, `cfg_v`) don't. One-letter names are reserved for loop indices in numerical code (`i`, `j`).
- Functions are named for what they do and start with a verb: `read_invoices`, `estimate_churn`.
- Booleans are named as questions with an `is_`, `has_`, `can_` or `should_` prefix.
- If a variable's type isn't obvious from context, a suffix records it: `_df` for a DataFrame, `_ser` for a Series, `_str` for a string standing in for something else (a date, say). Plain numbers seldom need one.
- A concept keeps the same name everywhere it appears. Objects that turn up across modules (the settings instance, the paths holder, the pipeline runner) get one fixed name each.

### Documentation and types

- Public functions, methods and classes carry a docstring covering arguments, return value and raised exceptions.
    - One line usually does it; a trivial helper may need none.
    - Non-obvious logic deserves a longer explanation.
    - A class docstring may run longer, describing its state, its operations and how they relate.
- Every parameter and return value is type-annotated.
- Docstrings, comments and `--help` text describe what the code actually does. If the text gives a parameter a meaning, the code honors exactly that meaning.

### Errors and resources

- Catch named exception types only; a bare `except:` is never used.
- A caught exception is at minimum logged, never dropped silently.
- Files, connections and similar handles are opened in `with` blocks.

### Functions and classes

- Functions are verbs and classes are nouns. A class groups some state with the operations on it, for example a dataset kept in several forms together with the conversions between them.
- A function does one job. Past roughly 40–50 lines, or with a long `if/elif` chain, check whether it's doing two, and pull the extra one out.
- A long argument list (roughly 5–8 or more) suggests too many responsibilities, or arguments that belong together in a dataclass.
- When a chain of functions keeps handing the same objects along, a class holding them is often clearer. Survey the whole module before introducing one; a premature class costs more than it saves.
- `__init__` stays light. Plain containers are dataclasses; derived values are `@property`.
- One or two levels of inheritance are fine. Anything deeper gets discussed with the human first.

### Imports and dependencies

- Import names explicitly (`from package import name`); never `import *`.
- Imports go at the top of the module, not inside functions, unless the human asks otherwise.
- Dependencies are declared in the project manifest, such as `pyproject.toml`.

### Secrets

- The repo is public. Passwords, tokens and keys never appear in code; they're read from a gitignored location suited to the tool.
- Logs and printed output never reveal them either: no URLs with embedded credentials, no tokens, no personal data.

### Testing

To be written.

### Logging

To be written.

### Commits

- A commit message states what changed and the reason.
- Remove disabled code, debug prints, breakpoints and anything resembling a credential before committing.
- More to follow.

## SQL

- One statement per file, runnable without edits.
- Structure is built from CTEs (`WITH` clauses), not nested subqueries: the query then unfolds in reading order, which makes it simpler to extend and debug. Keep indentation consistent.
- Every join names its type and condition (`INNER JOIN t ON ...`, `LEFT JOIN t ON ...`). No comma-separated `FROM` lists, no accidental cross joins.
- With more than one table in a query, alias each table and prefix each column with its alias.
- Keywords in upper case (`SELECT`, `FROM`, `GROUP BY`), identifiers in lower case, so structure and names are easy to tell apart.
- The select list has one column per line, and each line ends with its comma (trailing, not leading).
- Point out performance opportunities to the human:
    - a large table scanned several times in one query may be better read once into a temp table or a single CTE
    - aggregating one side before a join can shrink the rows going in, provided the output is provably unchanged
