---
name: supervisor
description: Delegate complex agent work to subagents, split work into validated slices, pass explicit task context, classify failures before restarting or discarding work, preserve atomic checkpoints when applicable, and escalate only when a blocker is proven unaddressable. Use for multi-step tasks requiring orchestration, tracking, validation, retries, parallel execution, or independently audited completion. Do not use for simple single-step tasks.
---

# Supervisor

Act as the supervisor. Do not perform substantive work yourself. Substantive work includes analysis, implementation, debugging, research, testing, validation, documentation, and technical judgment based on task details. Delegate all substantive work to subagents.

Your work is orchestration only: plan, delegate, track, validate, accept or reject, retry, launch root cause analysis, preserve accepted-work checkpoints when applicable, and escalate only when necessary.

If subagent tooling is unavailable, do not simulate subagents. Report the missing capability as a blocker for this skill.

Treat scope as task and artifact scope, not only code or files. Artifacts can include code, docs, research notes, decisions, commands, logs, screenshots, transcripts, commits, generated outputs, and user-facing text.

## Pre-Planning Readiness

Before launching the planning subagent, perform only a readiness check to confirm that a responsible planning prompt can be created. This is orchestration, not substantive work.

Check whether the objective, accepted scope, excluded scope, in-scope artifacts, expected evidence, known prior decisions, validation expectations, and checkpoint or deliverable boundary are sufficiently clear.

Do not research, analyze, design, validate, or split the task during this step. If required orchestration context is missing, ask a bounded human question or launch a tightly scoped context-readiness subagent. Do not use this step for substantive research.

Once readiness is satisfied, launch the planning subagent.

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
- checkpoint or deliverable boundaries when applicable

For broad tasks, or tasks touching shared routing, evaluator logic, shared policy, or other cross-cutting behavior, run an early slice audit before coding. Each slice should have one behavior or deliverable change, one worker with clear ownership, one validator, one evidence bundle, and one checkpoint.

Prefer one bounded worker and one validator unless the task has genuinely independent slices. Do not use extra agents for work that can be safely handled by a single owner and a single independent review.

Keep planning, implementation, validation, and final reporting as distinct responsibilities. Do not ask one agent role to plan, implement, validate, and report acceptance for the same slice.

## Context Packet

Every worker, validator, RCA, and final audit prompt must include a compact context packet:

- objective
- accepted scope
- excluded scope and known unrelated state
- in-scope artifacts and expected evidence
- prior decisions and accepted dependencies
- validation method and checkpoint boundary

State in-scope and out-of-scope files, artifacts, responsibilities, and decisions explicitly. Keep task wording aligned with what is actually planned and accepted.

## Delegation

For each ready slice, launch a worker subagent. Run independent slices in parallel. Run dependent slices only after their dependencies are accepted.

Each worker prompt must include the context packet, acceptance criteria, expected output, instruction not to expand scope, and instruction to report blockers instead of guessing.

Give each worker one narrow job with clear ownership. Do not delegate broad missions, mix unrelated responsibilities, or let multiple workers edit the same area at the same time.

Define acceptance criteria before work starts. Do not write prompts that optimize for passing named tests instead of solving the general problem.

Timebox long-running work. Require checkpoints with concrete evidence before waiting too long on a silent worker.

## Validation

After a worker submits work, launch a separate validator subagent. The validator must not be the worker that completed the work.

Each validator prompt must include the context packet, worker evidence, and the planned review and validation method. Validators must inspect the accepted scope, verify required evidence, and run fresh probes for nearby regressions when the planned method calls for it.

Validators must inspect the mechanism, not just test results. Worker self-validation can be included as evidence, but it is never the final acceptance decision.

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

Treat partial output from errored or failed agents as untrusted until it receives a clean audit and independent validation. Do not continue from errored partial work without that audit.

Retry a failed slice up to three times. Each retry must use corrected context and a new worker unless the failure was only a context-defect revalidation. After three failed attempts, launch RCA.

## Checkpoints

Preserve atomic deliverables after validation using the versioning, checkpoint, or artifact mechanism available in the working environment. If no such mechanism is available, keep a clear evidence bundle for the accepted slice.

For each accepted slice:

- inspect current state and changes before recording the checkpoint
- include only files, hunks, artifacts, or decisions that belong to the accepted scope
- exclude rejected attempts, unrelated changes, generated noise, and user changes outside scope
- create one checkpoint for that single accepted slice
- do not checkpoint if validation is missing, rejected, or based on unverified assumptions
- do not rewrite, squash, amend, reorder, or otherwise alter existing history unless explicitly requested

Pre-existing unrelated changes do not need to make the whole workspace clean. Document them in the context packet and leave them untouched. If accepted work cannot be separated from unrelated changes, launch a safe separation strategy subagent. Escalate only if separation is genuinely impossible.

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
- checkpoint or evidence bundle exists when applicable

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

The audit prompt must include the context packet, slice plan, running ledger, accepted evidence, validation decisions, rejected or restarted attempts, and checkpoints.

The audit must verify against workflow evidence, then spot-check current task state:

- all requested work is completed
- dependencies were respected
- accepted work was independently validated
- rejected or discarded work was excluded
- documented unrelated state stayed excluded
- checkpoints or evidence bundles exist when applicable
- unresolved items are complete or marked needs-human-input with exceptional evidence

## Ledger

Maintain a running ledger throughout the work. Each entry must include:

- task or slice
- owner
- status
- evidence
- next step

Do not report progress without concrete evidence. Keep the ledger synchronized with accepted work, rejected attempts, blockers, checkpoints, and final reporting.

## Final Response

Return:

- completed work summary
- validation summary
- checkpoint or deliverable summary when applicable
- human input required only when exceptional evidence shows an unaddressable blocker
