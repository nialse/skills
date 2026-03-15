# Skill assessment rubric

This document defines the scoring model for skill assessments and applies it to `pythonic-code-style`.

Scale

| Score | Meaning |
| --- | --- |
| 1 | Poor. Serious gaps, weak reliability, or not fit to rely on. |
| 2 | Weak. Some useful material exists, but major gaps or risks remain. |
| 3 | Adequate. Usable with care, but there are meaningful limitations. |
| 4 | Strong. Clearly useful and reliable, with only minor or bounded gaps. |
| 5 | Excellent. Exceptionally solid for its intended use, with clear evidence and low ambiguity. |

Factors

| Factor | Meaning | 1 | 3 | 5 |
| --- | --- | --- | --- | --- |
| C | Completeness. How fully the skill covers the scope it claims to cover. | Fragmentary coverage. Important parts of the stated scope are missing. | Covers the core of the stated scope, but with visible gaps or uneven depth. | Covers the claimed scope thoroughly, with good internal structure and little missing. |
| F | Fitness for use. How easily another agent can use the skill correctly and productively. | Hard to apply, vague, or easy to misuse. | Usable in normal cases, but requires judgment to fill gaps. | Immediately actionable, clear, and hard to misuse. |
| G | Groundedness. How well the guidance is anchored in verifiable authority rather than taste or unsupported assertion. | Mostly opinion or convention with no clear authority trail. | Mix of grounded guidance and unsupported synthesis. | Claims are tightly anchored to verifiable sources, with synthesis called out explicitly. |
| Src | Sourcing. Whether the skill actually cites support for its normative claims. | No meaningful sourcing. | Important claims are sourced, but not systematically. | Normative claims are systematically sourced and the sourcing model is explicit. |
| Xref | Cross-reference quality. Whether the skill points the reader to the right supporting files and establishes a clear authority hierarchy. | No useful navigation, or broken/confusing references. | Basic navigation exists, but authority or usage order is not fully clear. | Clear authority order, useful navigation, and references that help the reader apply the skill correctly. |

Assessment: `pythonic-code-style`

| Factor | Score | Reason |
| --- | --- | --- |
| C | 5 | The skill now covers both the cross-cutting Pythonic rules and the code-shape-specific routes promised by its description. `SKILL.md` defines the core rules and explicitly routes the reader to bundled context guidance for modules, scripts, tests, notebooks, CLIs, libraries, and APIs. See [SKILL.md](pythonic-code-style/SKILL.md) lines 10-27 and the rule set across the rest of the file. The bundled context guide then gives focused application guidance for each named environment. See [contexts.md](pythonic-code-style/references/contexts.md). |
| F | 5 | It is highly usable in practice. The file tells the reader what to treat as authoritative, what to use only as a lookup sheet, and how to apply the rules during review. Each rule includes concise rationale plus GOOD and BAD examples, which makes the skill easy to apply without guesswork. See [SKILL.md](pythonic-code-style/SKILL.md) lines 10-16, 22-555, and 557-561. The quick index further improves operational use. See [patterns.md](pythonic-code-style/references/patterns.md) lines 1-63. |
| G | 5 | Groundedness is unusually strong. The source map states that it was validated against official Python documentation and active PEP pages, distinguishes direct sources from synthesis and version gates, and says that unsourced text should be treated as procedural glue rather than a Python fact. See [source-map.md](pythonic-code-style/references/source-map.md) lines 3-5 and 7-64. That is a strong groundedness model, and the main skill follows it. |
| Src | 5 | The sourcing model is explicit and systematic. `SKILL.md` tells the reader to use the source map as the authority for source IDs, and every rule header carries source IDs. See [SKILL.md](pythonic-code-style/SKILL.md) lines 10-16 and 22-555. The source map then maps every rule `R0` through `R14` to supporting source IDs. See [source-map.md](pythonic-code-style/references/source-map.md) lines 65-83. This is claim-level sourcing, not just a general bibliography. |
| Xref | 5 | Cross-referencing is strong and useful. `SKILL.md` clearly establishes the authority order: `source-map.md` is authoritative for sources, `patterns.md` is only a quick lookup sheet, and the main skill plus source map are normative. See [SKILL.md](pythonic-code-style/SKILL.md) lines 10-16. `patterns.md` points back to the relevant rule IDs and source IDs for each pattern. See [patterns.md](pythonic-code-style/references/patterns.md) lines 3-63. I found no broken links in this skill bundle. |

Summary scorecard

| Skill | C | F | G | Src | Xref |
| --- | --- | --- | --- | --- | --- |
| `pythonic-code-style` | 5 | 5 | 5 | 5 | 5 |

Verification notes

- The skill bundle has a valid structure according to `quick_validate.py`.
- The cross-references used by this skill resolve locally: `SKILL.md` -> `references/source-map.md`, `references/patterns.md`, `references/contexts.md`, and `references/extended-examples.md`.
