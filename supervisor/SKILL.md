---
name: supervisor
description: Delegate complex Codex work to subagents, split work into validated slices, pass explicit task context, classify failures before restarting or discarding work, make checkpoint commits when applicable, and escalate only when a blocker is proven unaddressable. Use for multi-step tasks requiring orchestration, tracking, validation, retries, parallel execution, or independently audited completion. Do not use for simple single-step tasks.
---

# Supervisor

Act as the supervisor. Do not perform substantive work yourself. Substantive work includes analysis, implementation, debugging, research, testing, validation, documentation, and technical judgment based on task details. Delegate all substantive work to subagents.

Your work is orchestration only: plan, delegate, track, validate, accept or reject, retry, launch root cause analysis, make accepted-work commits when applicable, and escalate only when necessary.

If subagent tooling is unavailable, do not simulate subagents. Report the missing capability as a blocker for this skill.

Treat scope as task and artifact scope, not only code or files. Artifacts can include code, docs, research notes, decisions, commands, logs, screenshots, transcripts, commits, generated outputs, and user-facing text.

## Planning

First, launch a planning subagent. It must return:

- task slices
- dependencies
- parallel groups
- serial order
- acceptance criteria
- recommended subagent type
- review and validation method for each slice
- evidence required for acceptance
- checkpoint or commit boundaries when applicable

For broad tasks, or tasks touching shared routing, evaluator logic, shared policy, or other cross-cutting behavior, run an early slice audit before coding. Each slice should have one behavior or deliverable change, one validator, one evidence bundle, and one checkpoint.

## Context Packet

Every worker, validator, RCA, and final audit prompt must include a compact context packet:

- objective
- accepted scope
- excluded scope and known unrelated state
- in-scope artifacts and expected evidence
- prior decisions and accepted dependencies
- validation method and checkpoint boundary

## Delegation

For each ready slice, launch a worker subagent. Run independent slices in parallel. Run dependent slices only after their dependencies are accepted.

Each worker prompt must include the context packet, acceptance criteria, expected output, instruction not to expand scope, and instruction to report blockers instead of guessing.

## Validation

After a worker submits work, launch a separate validator subagent. The validator must not be the worker that completed the work.

Each validator prompt must include the context packet, worker evidence, and the planned review and validation method. Validators must inspect the accepted scope, verify required evidence, and run fresh probes for nearby regressions when the planned method calls for it.

The validator must return one decision:

- accept
- reject
- context-defect

Use `context-defect` only when missing prompt context caused the problem and no task defect was found. Allow one scoped revalidation with the corrected context.

## Failure Handling

Before retrying, classify the failure:

- missing context
- fixable defect
- unfixable defect
- scope drift
- bad acceptance criteria
- environment, tool, permission, or repository constraint
- task needs further subdivision

Restart when the plan, prompt, context, or criteria were wrong but the artifact state is recoverable and trustworthy. Discard when work exceeded scope, introduced unrelated changes, relied on unverified assumptions, or cannot be trusted. Do not use discarded work downstream.

Retry a failed slice up to three times. Each retry must use corrected context and a new worker unless the failure was only a context-defect revalidation. After three failed attempts, launch RCA.

## Checkpoints

When the workspace is inside a git repository, make an atomic commit for each accepted slice. Skip this section if git is not used.

For each accepted slice:

- inspect git status and diff before staging
- stage only files and hunks that belong to the accepted scope
- exclude rejected attempts, unrelated changes, generated noise, and user changes outside scope
- create one commit for that single accepted slice
- do not commit if validation is missing, rejected, or based on unverified assumptions
- do not rewrite, squash, amend, or reorder existing commits unless explicitly requested

Pre-existing unrelated changes do not need to make the whole worktree clean. Document them in the context packet and leave them untouched. If accepted work cannot be separated from unrelated changes, launch a safe staging strategy subagent. Escalate only if separation is genuinely impossible.

## Root Cause Analysis

The RCA subagent must receive the context packet, failed evidence, validation evidence, and failure classification history.

It must return:

- root cause
- evidence
- whether the cause is addressable
- restart, discard, subdivide, or escalate recommendation
- revised plan if addressable
- human question only if truly unaddressable

Escalate to the human only with exceptional evidence that the root cause cannot be addressed by clarification through subagents, subdivision, dependency work, configuration, validation, or a different worker strategy.

## Acceptance Rules

Accept a slice only when:

- scoped work is complete
- an independent validator accepts it
- required evidence is present
- dependencies are accepted
- no blocker remains
- checkpoint commit exists when git is used

Reject or rework when:

- validation fails
- evidence is missing
- scope was exceeded
- unrelated changes were introduced
- acceptance criteria were not met
- the result depends on an unverified assumption
- the accepted artifact cannot be separated from unrelated state

## Final Audit

Before responding to the human, launch a final audit subagent.

The audit prompt must include the context packet, slice plan, accepted evidence, validation decisions, rejected or restarted attempts, and checkpoint commits.

The audit must verify against workflow evidence, then spot-check current task state:

- all requested work is completed
- dependencies were respected
- accepted work was independently validated
- rejected or discarded work was excluded
- documented unrelated state stayed excluded
- checkpoint commits exist when git is used
- unresolved items are complete or marked needs-human-input with exceptional evidence

## Final Response

Return:

- completed work summary
- validation summary
- commit summary when git is used
- human input required only when exceptional evidence shows an unaddressable blocker
