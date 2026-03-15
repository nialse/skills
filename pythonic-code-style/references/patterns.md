# Quick Pattern Index

This file is only a fast lookup sheet. `SKILL.md` and `source-map.md` remain the authority.

## R0

Version-gate the recommendation before using modern syntax or stdlib features. See `R0`, `V1`, `V2`, `V3`, and `V4`.

## R1

Use direct iteration, `enumerate()`, `zip(..., strict=True)`, and `mapping.items()`. See `R1`, `D8`, `D9`, `D10`, and `S1`.

## R2

Use comprehensions for simple result creation. Do not use them for side effects or dense branching. See `R2`, `D11`, and `S4`.

## R3

Use truthiness for emptiness and `is None` for sentinel checks. See `R3`, `D2`, `D7`, and `S2`.

## R4

Prefer EAFP when the action is the check, and catch the narrowest expected exception. See `R4`, `D3`, and `D12`.

## R5

Use `get()`, `setdefault()`, `defaultdict()`, or EAFP according to the mapping intent. See `R5`, `D16`, `D17`, `D12`, and `S5`.

## R6

Use `with`, `Path`, `''.join(...)`, and `startswith()` or `endswith()`. See `R6`, `D5`, `D6`, `D14`, and `D15`.

## R7

Remember that in-place mutators return `None`. See `R7` and `D28`.

## R8

Prefer protocol-oriented code. If you must check types, prefer `isinstance()`. See `R8`, `D13`, `D23`, `D27`, and `S3`.

## R9

Use plain attributes for plain data, `property()` for managed attributes, and `@dataclass` for record-like classes. See `R9`, `D24`, `D25`, `D26`, and `S6`.

## R10

Use keyword-only parameters when names matter at the call site. See `R10`, `D19`, and `S7`.

## R11

Never use mutable default arguments. See `R11` and `D18`.

## R12

Keep typing modern and honest. Use built-in generics and `collections.abc` interfaces when supported and appropriate. See `R12`, `D21`, `D22`, `V1`, and `V2`.

## R13

Use `match` when the structure is the subject. Use `if` and `elif` when they are already clearer. See `R13`, `D20`, `V3`, and `S8`.

## R14

Avoid wildcard imports. See `R14` and `D4`.
