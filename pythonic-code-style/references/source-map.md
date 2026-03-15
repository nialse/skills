# Source Map

Validated on 2026-03-15 against current official Python documentation on `docs.python.org/3` and active PEP pages on `peps.python.org`.

Every normative rule in `SKILL.md` should cite one or more IDs from this file. If a sentence in the main skill has no source IDs, treat it as procedural glue, not as a style claim.

## Direct Sources

| ID | What it directly supports | Source |
| --- | --- | --- |
| D1 | Readability, explicitness, simplicity, and one obvious way are core Python values | PEP 20: <https://peps.python.org/pep-0020/> |
| D2 | Compare `None` with `is` and `is not`; do not confuse `if x` with `if x is not None` | PEP 8: <https://peps.python.org/pep-0008/> |
| D3 | Avoid bare `except:` when `except Exception:` or a narrower exception is intended | PEP 8: <https://peps.python.org/pep-0008/> |
| D4 | Avoid wildcard imports | PEP 8: <https://peps.python.org/pep-0008/> |
| D5 | Prefer `''.join(...)` over repeated string concatenation in sensitive paths | PEP 8: <https://peps.python.org/pep-0008/> |
| D6 | Prefer `startswith()` and `endswith()` over slice checks | PEP 8: <https://peps.python.org/pep-0008/> |
| D7 | Empty sequences and collections are false; `None` is false too | Truth Value Testing: <https://docs.python.org/3/library/stdtypes.html#truth-value-testing> |
| D8 | `enumerate()` is the built-in way to pair positions with values | Built-in functions: <https://docs.python.org/3/library/functions.html#enumerate> |
| D9 | `zip(..., strict=True)` is recommended when equal length is assumed | Built-in functions: <https://docs.python.org/3/library/functions.html#zip> |
| D10 | `items()`, `sorted()`, and related loop idioms are the tutorial's standard techniques | Tutorial, Data Structures: <https://docs.python.org/3/tutorial/datastructures.html> |
| D11 | List comprehensions are concise list-creation tools | Tutorial, Data Structures: <https://docs.python.org/3/tutorial/datastructures.html> |
| D12 | EAFP is a common Python style; LBYL exists but has tradeoffs | Glossary: <https://docs.python.org/3/glossary.html> |
| D13 | Duck typing avoids unnecessary `type()` and `isinstance()` tests when interface is what matters | Glossary: <https://docs.python.org/3/glossary.html#term-duck-typing> |
| D14 | `with` is the good-practice way to manage files and close them even on exceptions | Tutorial, Input and Output: <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files> |
| D15 | `pathlib.Path` is most likely what you need for filesystem paths | `pathlib`: <https://docs.python.org/3/library/pathlib.html> |
| D16 | `dict.get()` and `dict.setdefault()` provide direct mapping idioms for defaults and insert-on-first-use | `dict` methods: <https://docs.python.org/3/library/stdtypes.html#dict.get> |
| D17 | `defaultdict` supplies missing values from a factory function | `collections.defaultdict`: <https://docs.python.org/3/library/collections.html#collections.defaultdict> |
| D18 | Mutable default argument values are evaluated once | Tutorial, Default Argument Values: <https://docs.python.org/3/tutorial/controlflow.html#default-argument-values> |
| D19 | Special parameters support keyword-only and positional-only API design | Tutorial, Special Parameters: <https://docs.python.org/3/tutorial/controlflow.html#special-parameters> |
| D20 | `match` is for structural pattern matching over values, sequences, mappings, and attributes | Tutorial, `match` Statements: <https://docs.python.org/3/tutorial/controlflow.html#match-statements> |
| D21 | The runtime does not enforce type annotations | `typing`: <https://docs.python.org/3/library/typing.html> |
| D22 | Modern typing docs use built-in generics and `collections.abc` interfaces in annotations | `typing`: <https://docs.python.org/3/library/typing.html> |
| D23 | `collections.abc` describes interfaces in terms of behavior and semantics, not just names | `collections.abc`: <https://docs.python.org/3/library/collections.abc.html> |
| D24 | Plain data attributes are first-class in Python objects | Tutorial, Classes: <https://docs.python.org/3/tutorial/classes.html> |
| D25 | `property()` is for managed attributes | Built-in functions: <https://docs.python.org/3/library/functions.html#property> |
| D26 | `@dataclass` generates record-like boilerplate for user-defined classes | `dataclasses`: <https://docs.python.org/3/library/dataclasses.html> |
| D27 | `isinstance()` is the standard runtime type check and supports union types | Built-in functions: <https://docs.python.org/3/library/functions.html#isinstance> |
| D28 | In-place mutating methods conventionally return `None` | Built-in Types: <https://docs.python.org/3/library/stdtypes.html> |

## Synthesis

These are deliberate inferences from the direct sources above. They are valid guidance, but they are not direct quotations from the docs.

| ID | Synthesis claim | Basis |
| --- | --- | --- |
| S3 | Prefer protocols and duck-typed behavior over rigid exact-type checks when behavior is what matters | D13, D23, D27 |
| S4 | Use comprehensions when they simplify result creation; stop when they become side-effectful or denser than a loop | D11, D1 |
| S5 | Choose `get()`, `setdefault()`, `defaultdict()`, or EAFP according to whether you want a default, insertion, or exceptional absence | D16, D17, D12 |
| S6 | Prefer plain attributes and dataclasses over Java-style getter and setter ceremony for record-like data | D24, D25, D26, D1 |
| S7 | Use keyword-only parameters when names materially improve call-site readability | D19, D1 |
| S8 | Use `match` when structure is the subject; keep `if` and `elif` when that is the simpler shape | D20, D1 |
| S9 | Check the repo's supported Python version before recommending syntax or library features | V1, V2, V3, V4 |
| S1 | Prefer direct iteration, `enumerate()`, `zip()`, and `items()` over index-driven loops when the index is not the real subject | D8, D9, D10, D1 |
| S2 | Use truthiness for emptiness, but switch to `is None` when distinguishing missing from empty | D2, D7 |

## Version Gates

| ID | Feature | Minimum version | Source |
| --- | --- | --- | --- |
| V1 | Built-in generic syntax such as `list[str]` and `dict[str, int]` | Python 3.9 | `typing`: <https://docs.python.org/3/library/typing.html> |
| V2 | Union syntax such as `X | None` | Python 3.10 | `typing`: <https://docs.python.org/3/library/typing.html> |
| V3 | Structural pattern matching with `match` | Python 3.10 | Tutorial, `match` Statements: <https://docs.python.org/3/tutorial/controlflow.html#match-statements> |
| V4 | `zip(..., strict=True)` | Python 3.10 | Built-in functions: <https://docs.python.org/3/library/functions.html#zip> |

## Rule Coverage

| Rule ID | Main claim in `SKILL.md` | Source IDs |
| --- | --- | --- |
| R0 | Version-gate every recommendation | V1, V2, V3, V4, S9 |
| R1 | Iterate over values, not indexes, unless the index itself is the subject | D8, D9, D10, S1 |
| R2 | Use comprehensions for result creation, not side effects or dense control flow | D11, S4 |
| R3 | Use truthiness for emptiness, but use `is None` for sentinel checks | D2, D7, S2 |
| R4 | Prefer EAFP when the action is the check, and catch the narrowest expected exception | D3, D12 |
| R5 | Choose the mapping idiom that matches the intent | D16, D17, D12, S5 |
| R6 | Use the standard library's resource, path, and string helpers | D5, D6, D14, D15 |
| R7 | Remember that in-place mutators return `None` | D28 |
| R8 | Prefer protocols and exact intent over rigid type checks | D13, D23, D27, S3 |
| R9 | Use plain attributes for plain data, `property()` for managed attributes, and `@dataclass` for record-like classes | D24, D25, D26, S6 |
| R10 | Make call sites readable with keyword-only parameters when names matter | D19, S7 |
| R11 | Never use mutable default arguments | D18 |
| R12 | Keep typing modern and honest | D21, D22, V1, V2 |
| R13 | Use `match` when structure is the subject, not as a decorative `if` chain | D20, V3, S8 |
| R14 | Avoid wildcard imports | D4 |

## Context Coverage

These routes help apply the same core rules to the code shapes named in the skill description.

| Context | Primary rules |
| --- | --- |
| modules | R0, R6, R8, R12, R14 |
| scripts | R0, R1, R2, R6, R11 |
| tests | R1, R2, R3, R6, R8, R11 |
| notebooks | R0, R1, R2, R3, R6, R7 |
| CLIs | R0, R3, R6, R10, R11 |
| libraries | R0, R8, R10, R12, R14 |
| APIs | R3, R5, R8, R10, R12, R13 |

## Review Standard

When describing code as "not Pythonic", tie the comment to one or more rows above. If you cannot map the claim to a rule row, present it as a local preference instead of a Python fact.
