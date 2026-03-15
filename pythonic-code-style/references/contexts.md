# Context Routes

This file applies the core rules in `SKILL.md` to the code shapes named in the skill description. `SKILL.md` and `source-map.md` remain normative.

## Modules

Prioritize:
- `R0` for version-safe syntax and annotations in shared code
- `R6` for filesystem and resource helpers
- `R8` and `R12` for protocol-oriented, honest public function signatures
- `R14` for explicit imports and readable module surfaces

Use this route when reviewing ordinary Python modules that are imported by other code.

## Scripts

Prioritize:
- `R0` so distributed scripts do not assume unsupported syntax
- `R1` and `R2` for straightforward data flow instead of index-heavy loops or side-effect comprehensions
- `R6` for file handling and path manipulation
- `R11` so helper functions in scripts do not leak shared mutable state

Use this route when the main concern is batch jobs, one-off utilities, or executable Python files.

## Tests

Prioritize:
- `R1` and `R2` for readable setup and assertions
- `R3` for correct `None` handling in expectations
- `R6` for temporary files, fixtures, and resource cleanup
- `R8` only when runtime type is actually what the test is asserting
- `R11` for helper defaults used across tests

Use this route when test readability and correctness matter more than cleverness.

## Notebooks

Prioritize:
- `R0` when the notebook will be shared, exported, or run in mixed environments
- `R1` and `R2` for simple, scan-friendly cell logic
- `R3` for explicit sentinel handling in optional inputs
- `R6` for file reads, writes, and path work
- `R7` to avoid assigning the result of in-place mutation during exploratory work

Use this route when reviewing notebooks or notebook-style code cells.

## CLIs

Prioritize:
- `R0` for distributed command-line tools
- `R3` for distinguishing omitted values from explicit falsey values
- `R6` for paths and file resources
- `R10` when flags or options are threaded through helper functions
- `R11` for accumulators and option defaults

Use this route when the code's public entry point is a command-line interface.

## Libraries

Prioritize:
- `R0` for public syntax compatibility
- `R8` and `R12` for protocol-based, stable type surfaces
- `R10` when named options improve API clarity
- `R14` for explicit package exports

Use this route when reviewing reusable packages intended for other callers.

## APIs

Prioritize:
- `R3` so `None` remains distinct from `0`, `False`, empty strings, and empty collections
- `R5` for optional request data and defaults
- `R8` and `R12` for interface-based parameter typing
- `R10` when option names matter at the call site
- `R13` only when dispatch is truly structural

Use this route when reviewing application-facing service code or API handlers.
