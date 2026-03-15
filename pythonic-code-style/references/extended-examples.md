# Extended Examples

This file keeps full GOOD/BAD examples for the later rules so `SKILL.md` can stay focused. `SKILL.md` and `source-map.md` remain normative.

## R10

When argument names carry meaning, force them at the call site. (Sources: D19, S7)

GOOD:

```python
# names matter at the call site
def render(template, *, escape=True, indent=2):
    ...


render(page, escape=False, indent=4)
```

BAD:

```python
# caller has to remember positional booleans and numbers
def render(template, escape=True, indent=2):
    ...


render(page, False, 4)
```

## R11

Default values are evaluated once. Use `None`, then create the mutable object inside. (Sources: D18)

GOOD:

```python
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

BAD:

```python
def append_item(item, items=[]):
    items.append(item)
    return items
```

## R12

Annotations are for readers and tools, not runtime enforcement. On supported Python, use built-in generics and `collections.abc` interfaces when the function accepts any object with that protocol. (Sources: D21, D22, V1, V2)

GOOD:

```python
# interface-based annotation
from collections.abc import Mapping, Sequence

def render_table(rows: Sequence[Mapping[str, str]]) -> str:
    ...

# current optional syntax on supported Python
# repo supports Python >= 3.10
def parse_age(value: str) -> int | None:
    ...
```

BAD:

```python
# concrete containers when the function only needs the protocol
from typing import Dict, List

def render_table(rows: List[Dict[str, str]]) -> str:
    ...

# version-mismatched syntax
# repo supports Python 3.9
def parse_age(value: str) -> int | None:
    ...
```

## R13

Reach for `match` when you are dispatching on literals, mappings, sequences, or attribute patterns. Keep ordinary conditionals when they are already the clearest shape. (Sources: D20, V3, S8)

GOOD:

```python
# structural dispatch
match event:
    case {"type": "click", "x": x, "y": y}:
        handle_click(x, y)
    case {"type": "quit"}:
        stop()

# plain conditionals when they are already clearer
if status == 404:
    label = "not found"
elif status >= 500:
    label = "server error"
```

BAD:

```python
# guard-heavy match used as a decorative if-chain
match status:
    case _ if status == 404:
        label = "not found"
    case _ if status >= 500:
        label = "server error"

# repeated manual destructuring of structured data
if event["type"] == "click":
    handle_click(event["x"], event["y"])
elif event["type"] == "quit":
    stop()
```

## R14

Wildcard imports hide where names came from and make code harder to read and analyze. (Sources: D4)

GOOD:

```python
from math import cos, sin
```

BAD:

```python
from math import *
```
