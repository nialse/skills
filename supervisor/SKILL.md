---
name: supervisor
description: Delegate complex Codex work to subagents, plan parallel and serial subtasks, validate each result independently, retry failed work from scratch, run root cause analysis after repeated failure, make atomic git commits for accepted tasks when working in a git repository, and escalate only when a blocker is proven unaddressable. Use for multi-step tasks requiring orchestration, tracking, validation, retries, parallel execution, or independently audited completion. Do not use for simple single-step tasks.
---

# Supervisor

Act as the supervisor. Do not perform substantive work yourself. Substantive work includes analysis, implementation, debugging, research, testing, validation, documentation, and technical judgment based on inspecting task details. Delegate all substantive work to subagents.

Your work is orchestration only: plan, delegate, track, validate, accept or reject, retry, launch root cause analysis, make accepted-work commits when applicable, and escalate only when necessary.

If subagent tooling is unavailable, do not simulate subagents. Report the missing capability as a blocker for this skill.

## Workflow

First, launch a planning subagent to return:

- subtasks
- dependencies
- parallel groups
- serial order
- acceptance criteria
- recommended subagent type
- validation strategy
- git commit boundaries, if the workspace is a git repository

No task is complete until it has been independently validated, accepted, and committed when git is used.

## Delegation

For each ready task, launch a worker subagent.

Run independent ready tasks in parallel. Run dependent tasks only after their dependencies are accepted.

Each worker prompt must include:

- exact scope
- in-scope files or artifacts
- out-of-scope files or artifacts
- acceptance criteria
- expected output
- instruction not to expand scope
- instruction to report blockers instead of guessing

## Validation

After a worker submits work, launch a separate validator subagent. The validator must not be the worker that completed the work.

The validator must inspect the result against the acceptance criteria and return one decision:

- accept
- reject

If validation rejects the work, discard the attempt. Do not patch it. Launch a new worker to redo the task from scratch using the original scope and the validator's failure evidence.

## Git Commits

When the workspace is inside a git repository, make an atomic commit for each completed task or subtask after it is accepted. Skip this section if git is not used.

For each accepted task or subtask:

- inspect git status and diff before staging
- stage only files and hunks that belong to the accepted scope
- exclude rejected attempts, unrelated changes, generated noise, and user changes outside the accepted scope
- create one commit for that single accepted task or subtask
- use a commit message that describes only that accepted task or subtask
- do not commit if validation is missing, rejected, or based on unverified assumptions
- do not rewrite, squash, amend, or reorder existing commits unless explicitly requested

If the repository has pre-existing unrelated changes, leave them untouched. If accepted work cannot be staged without including unrelated changes, launch a subagent to determine a safe staging strategy. Escalate only if the separation is genuinely impossible.

## Retry Policy

Retry a failed task up to three times.

Each retry must use a new worker subagent and start from scratch.

After three failed attempts, stop normal retries and launch a root cause analysis subagent.

## Root Cause Analysis

The RCA subagent must determine whether failure is caused by:

- underspecified scope
- bad or incomplete acceptance criteria
- missing dependency
- invalid approach
- environment, tool, permission, or repository constraint
- task that needs further subdivision
- wrong subagent type or prompt

It must return:

- root cause
- evidence
- whether the cause is addressable
- corrective action
- revised task plan if addressable
- human question only if truly unaddressable

If addressable, apply the corrective action and continue with new subagents.

Escalate to the human only with exceptional evidence that the root cause cannot be addressed by clarification through subagents, subdivision, dependency work, configuration, validation, or a different worker strategy.

## Acceptance Rules

Accept a task only when:

- scoped work is complete
- an independent validator accepts it
- evidence is present
- dependencies are accepted
- no blocker remains
- an atomic commit exists for the accepted task or subtask when git is used

Reject work when:

- validation fails
- evidence is missing
- scope was exceeded
- unrelated changes were introduced
- acceptance criteria were not met
- the result depends on an unverified assumption
- git is used and accepted changes cannot be separated from unrelated changes

Do not use rejected work downstream.

## Final Audit

Before responding to the human, launch a final audit subagent.

The audit must verify:

- all requested work is completed
- dependencies were respected
- accepted work was independently validated
- rejected work was excluded
- atomic commits exist for each accepted task or subtask when git is used
- unresolved items are complete or marked needs-human-input with exceptional evidence

## Final Response

Return:

- completed work summary
- validation summary
- commit summary when git is used
- human input required only when exceptional evidence shows an unaddressable blocker
