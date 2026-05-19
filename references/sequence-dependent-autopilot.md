# GEO Sequence-Dependent Autopilot

This reference defines how `geo` should handle all-in requests when the user
does not know the package workflow.

The goal is guided completion: if the user asks GEO to do the whole task, GEO
builds the ordered process, executes each unblocked step, verifies the result,
and continues until every required process is complete or a real blocker is
reached.

## Trigger Contract

Use this autopilot when the user asks for the whole process with wording such
as:

- `전부 해줘`
- `전체 진행`
- `전체 수행`
- `끝까지 해줘`
- `알아서 다 해줘`
- `처음부터 끝까지`
- `do everything`
- `run the whole process`
- `continue until complete`

Do not use this autopilot when the user asks only for explanation, review,
brainstorming, or a read-only first pass. If the user explicitly sets a
read-only or review-only boundary, preserve that boundary until the user
unlocks execution.

## Ordered Process

Run the sequence in this order:

1. Intake lock
   - Lock `goal / scope / surface / success / evidence target`.
   - Ask only the minimum question needed when one of those fields is missing
     and no safe default exists.
2. Source and mode selection
   - Choose `portable-baseline`, `user-material`, or `local-overlay`.
   - Preserve source order before touching derived output.
3. Dependency graph
   - Build an ordered dependency graph from the selected lane,
     `references/execution-skill-matrix.md`, and applicable references.
   - Mark each phase as `pending`, `in_progress`, `passed`, `blocked`, or
     `skipped_with_reason`.
4. Preflight
   - Check required files, `skills/*`, credentials, tools, network need,
     permissions, and output surfaces for the next phase only.
5. Execute next unblocked phase
   - Perform the smallest safe step that advances the dependency graph.
   - Delegate to the matching `skills/geo-*` subskill only after it is
     confirmed present.
6. Verify phase
   - Run the smallest validation that proves the phase, such as a validator,
     source check, rendered artifact check, crawler evidence, report contract
     check, or `git diff --check`.
7. Record ledger
   - Record phase status, evidence path or command, measured facts,
     interpretation, assumptions, unknowns, and next phase.
8. Continue
   - Repeat steps 4-7 until every required phase is `passed` or a blocker is
     recorded.
9. Closeout
   - Report `completion_judgment`, `all_must_passed` or
     `failed_must_queue`, `verification_set`, remaining gaps, and handoff
     owner.
   - Use `all_must_passed=true` only when every required phase passed.

## Stop Conditions

Stop and ask the user only when the next required action is blocked by:

- destructive file or data operations that were not requested
- credentials, payment, account approval, or external system decisions
- missing source material that cannot be inferred safely
- legal, medical, financial, or policy-risk judgment that requires the user or
  a qualified owner
- validation failure where the smallest safe fix is unclear
- an explicit user interruption, pause, or changed scope

Routine continuation, local validation, non-destructive file edits requested by
the user, and retrying the next safe phase are not blockers.

## Autopilot Ledger

Use this compact ledger shape when reporting or writing a handoff:

```yaml
autopilot:
  trigger: all-in request wording
  scope: task scope
  source_mode: portable-baseline | user-material | local-overlay
  phases:
    - id: phase-id
      depends_on: []
      status: pending | in_progress | passed | blocked | skipped_with_reason
      owner: geo | geo-subskill | user | external-system
      evidence:
        - command_or_path_or_url
      measured_facts:
        - fact
      interpretation:
        - implication
      assumptions:
        - assumption
      unknowns:
        - unknown
      next_action: next phase or blocker
  completion_judgment: pass | blocked
  all_must_passed: true | false
  failed_must_queue:
    - failed item
```

## Completion Rule

If the user asks for the whole task, do not stop after producing a plan.
Continue through implementation, validation, and closeout until all required
phases pass or a stop condition applies.

Do not require the user to know the names of subskills, references, gates, or
commands. GEO must choose the next process step from the ordered dependency
graph.
