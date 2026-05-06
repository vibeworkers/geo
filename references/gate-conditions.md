# GEO Gate Conditions

## Gate 1: GEO-domain trigger

- Entry condition: the request is about GEO strategy, GEO teaching material,
  GEO evidence, GEO assets, or GEO deliverables.
- Exit condition: the request is accepted into a GEO routing flow.
- Fail condition: the request is unrelated to GEO or belongs to a different
  design/system domain.

## Gate 2: Context mode selection

- Entry condition: GEO-domain trigger passed.
- Exit condition: the request is classified as `portable-baseline`,
  `user-material`, or `local-overlay`.
- Fail condition: the response assumes a local workspace or misses a stronger
  user-provided source.

## Gate 3: Owning surface selection

- Entry condition: context mode is known.
- Exit condition: the request is mapped to `framework-source`,
  `working-source`, `evidence-note`, `asset-surface`, or
  `derived-deliverable`.
- Fail condition: the request mixes surfaces without a lead lane.

## Gate 4: Source-order protection

- Entry condition: an owning surface is selected.
- Exit condition: the workflow preserves `confirmed working source ->
  supporting evidence or framework -> derived output`.
- Fail condition: the workflow jumps straight to an export or invents a source.

## Gate 5: Derived-output readiness

- Entry condition: the request touches a derived output.
- Exit condition: build or export preconditions are either confirmed or
  explicitly marked as missing.
- Fail condition: the response promises a refresh without checking
  prerequisites.

## Gate 6: Evidence closure

- Entry condition: the answer or change plan is ready.
- Exit condition: at least one confirmed source surface proves the claim.
- Fail condition: the response closes with generic GEO commentary only.
