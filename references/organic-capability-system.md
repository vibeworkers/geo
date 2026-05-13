# GEO Organic Capability System

This reference defines how the beta branch combines beta-A and beta-B without
turning them into separate user-facing products.

## System Rule

`geo` is the single representative system.

The physical folders under `skills/` and `packages/` are ownership and
maintenance boundaries. They are not separate product surfaces and must not
produce disconnected closeouts for one user request.

The root `geo` system owns:

- source priority and context mode selection
- request routing and sequence-dependent autopilot
- evidence-state boundaries
- policy, regional, private-surface, and commerce/action gates
- one claim boundary ledger
- one report and handoff contract

## Capability Stack

| Layer | Surface | Role |
| --- | --- | --- |
| Core operating contract | `SKILL.md`, `references/*.md` | Intake, source order, gates, autopilot, evidence labels, report contract |
| Commerce capability | `packages/geo-deep-audit-ecommerce/` | Deep audit for ecommerce and commerce readiness |
| KR2 capability | `packages/geo-seo-skills-kr2/` | Korean, multilingual, platform, crawler, AI-readiness, and local Code extension capability |
| Local execution bundle | `skills/geo-*` | Portable execution workflows routed by the representative `geo` surface |

`packages/geo-deep-audit-ecommerce/` keeps its current physical compatibility
path. Its semantic capability handle inside the `geo` system is
`deep-audit-ecommerce`.

`packages/geo-seo-skills-kr2/` keeps its package identity for portability. Its
semantic capability handle inside the `geo` system is `kr2`.

## Composition Rules

1. Start every task through the root `geo` operating contract.
2. Use `references/sequence-dependent-autopilot.md` for all-in requests before
   choosing a capability.
3. Use `deep-audit-ecommerce` when the target is ecommerce, commerce,
   product/category pages, merchant/catalog readiness, checkout/action
   readiness, or shopping-related GEO.
4. Use `kr2` when the target involves Korean, multilingual routing,
   region/platform behavior, crawler policy, AI citation readiness, realtime
   capture, tracking, batch scans, or `/geo-code` extension work.
5. When a request touches both commerce and KR2 concerns, run them as one GEO
   workflow with one evidence ledger and one report contract.
6. When a KR2 request targets an ecommerce or commerce property, import the
   deep-audit-ecommerce rubric before closing readiness.
7. When a commerce audit targets Korean, multilingual, AI-platform, crawler,
   realtime, or tracking concerns, import the KR2 evidence boundary and source
   index before closing readiness.
8. Do not upgrade `Readiness` or `Heuristic` to `Measured` unless direct
   platform output, citation URL, log, screenshot, referral, conversion, or
   equivalent raw observation is captured.
9. Do not make `cogarch`, `~/.cogarch`, `OPERATIONS.md`, or hidden session
   state required for normal GEO package execution.

## Organic Routing Examples

| User intent | Organic route |
| --- | --- |
| `geo audit this ecommerce site for Korean AI visibility` | `geo core -> sequence autopilot -> deep-audit-ecommerce -> kr2 -> one report` |
| `geo check KR2 readiness for this product category site` | `geo core -> kr2 -> deep-audit-ecommerce commerce rubric -> one evidence ledger` |
| `geo run the whole process for this commerce brand` | `geo core -> all-in autopilot -> deep-audit-ecommerce + kr2 as needed -> verification -> one closeout` |
| `geo-code pipeline for a Korean shopping site` | `geo core -> kr2 geo-code -> deep-audit-ecommerce context import -> measured/readiness split` |

## Closeout Rule

For a single user request, the final result must not be a pasted bundle of a
deep-audit report plus a KR2 report. It must be a single GEO judgment flow:

1. scope and source surfaces
2. capability path used
3. measured facts
4. interpretation
5. assumptions
6. unknowns
7. action priority
8. verification evidence
9. unresolved blockers

This keeps beta-A's execution discipline and beta-B's KR2 capability active as
one organic `geo` system.
