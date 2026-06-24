---
name: orwell-six-writing-rules
description: Rewrite, review, and draft English prose using George Orwell's six writing rules from "Politics and the English Language", with researched modern plain-language examples and counterexamples. Use when a user asks for Orwell-style clarity, plain English, removal of stale metaphors, shorter wording, tighter prose, active voice, jargon reduction, or a writing review grounded in Orwell's six rules while preserving meaning and voice.
---

# Orwell Six Writing Rules

Use this skill to make prose clearer, shorter, and harder to misunderstand without flattening the author's voice.

Read `references/rules-and-examples.md` before applying the rules. It contains the rule cards, source IDs, good examples, bad examples, and counterexamples for cases where a mechanical rewrite would damage the text.

## Workflow

1. Identify the text's purpose, audience, and constraints from the user request or surrounding context.
2. Preserve factual meaning, needed nuance, domain terms, legal force, and the author's recognizable tone.
3. Apply the six-rule pass in this order:
   - remove stale or mixed imagery unless the figure is useful and fresh
   - replace long words only when a shorter word says the same thing
   - cut words that add no meaning, force, rhythm, or politeness
   - prefer active voice when the actor matters
   - replace jargon or foreign/scientific terms when an everyday equivalent is accurate for the audience
   - break any rule that would make the sentence false, ugly, evasive, childish, or imprecise
4. For rewrites, return the revised text first unless the user asks for analysis.
5. For reviews, lead with the highest-impact issues, quote only the local phrase being discussed, and give a concrete replacement.
6. Use source IDs from `references/rules-and-examples.md` when explaining or defending a recommendation.

## Output Modes

Rewrite mode:

```text
Revised:
<cleaned text>
```

Review mode:

```text
Issue: <rule id and short diagnosis>
Original: <short phrase or sentence>
Revision: <replacement>
Reason: <one sentence, with source IDs if useful>
```

Teaching mode:

Use the GOOD, BAD, and COUNTEREXAMPLE patterns from `references/rules-and-examples.md`. Keep examples close to the user's domain instead of reusing generic office prose.

## Guardrails

Do not turn every text into spare bureaucratic plain English. Orwell's rules are a clarity test, not a demand that all prose sound the same.

Do not remove precise technical terms, legal terms, terms of art, or vivid voice just because they are long or specialized.

Do not treat every "be" verb as passive voice. Passive voice needs a passive construction, usually a form of "be" or "get" plus a past participle.
