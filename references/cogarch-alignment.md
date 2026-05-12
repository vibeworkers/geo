# GEO Cogarch Alignment Contract

This reference captures the governance patterns that `geo` may borrow from
`cogarch` without depending on `cogarch`, `~/.cogarch`, `OPERATIONS.md`, or
hidden workspace state.

The goal is compatibility, not inheritance.

`geo` remains a portable GEO skill package. `cogarch` remains a broader
governance and knowledge system. This document defines the small shared
decision shape that helps GEO outputs close with clearer evidence, ownership,
and handoff boundaries.

## Adopted Patterns

| Pattern | GEO use | Boundary |
| --- | --- | --- |
| `Goal -> Rubric -> Iteration -> Score -> Next Action` | Close broad GEO requests with an executable judgment loop | Use as a response and report discipline, not as a hidden runtime dependency |
| `measured / interpretation / assumption / unknown` | Separate evidence from claim-making in reports and proposals | Do not collapse proxy readiness into observed visibility |
| owner split | Keep `geo` router, `geo-*` subskills, runtime adapters, and external knowledge systems separate | Do not let the representative router absorb subskill execution ownership |
| actor-first handoff | Package findings for decision makers, operators, or builders | Do not change evidence depth by audience level |
| portable knowledge packet | Make reusable learnings movable across runtimes and repositories | Use relative paths or URLs; do not require machine-local paths |

## Evidence Classification

Every GEO judgment that cites this alignment should separate:

- measured facts: crawler output, captured answers, analytics, logs, validator
  output, or explicitly provided source text
- interpretation: the reasoning that connects measured facts to readiness,
  priority, or risk
- assumptions: unverified conditions accepted for the current plan
- unknowns: missing evidence that could change the recommendation

This separation is mandatory for claims about platform visibility, commerce
readiness, private-surface evidence, regional behavior, and policy risk.

## Owner Split

| Surface | Owner |
| --- | --- |
| representative routing | `geo` |
| advanced workflow execution | matching `skills/geo-*` subskill |
| runtime-specific onboarding or metadata | runtime adapter or metadata file |
| external knowledge system | external system; referenced only as evidence |
| final derived deliverable | confirmed working source or requested output surface |

If a request crosses owners, route from the smallest confirmed source outward:
source evidence, then working contract, then execution subskill, then derived
deliverable.

## Actor-First Handoff

When a report, proposal, or completion summary needs handoff, identify the
actor before choosing the wording:

| Actor | Package |
| --- | --- |
| decision maker | conclusion, risk, budget or priority implication, owner |
| operator | exact surface, action sequence, verification step, fallback |
| builder | file, command, schema, API, test, rollback or failure mode |

Actor-specific packaging changes presentation and action granularity. It must
not remove evidence labels, source paths, confidence, or unresolved gaps.

## Portable Knowledge Packet

Use this packet shape when a GEO learning should be reusable:

```yaml
packet_id: geo-YYYYMMDD-topic
scope: site, brand, corpus, workflow, or report
source_materials:
  - relative_path_or_url
measured_facts:
  - fact
interpretations:
  - implication
assumptions:
  - assumption
unknowns:
  - missing evidence
decisions:
  - decision made in this pass
recommended_actions:
  - next action
validation_evidence:
  - command, artifact, or review evidence
last_verified: YYYY-MM-DD
handoff_owner: decision-maker, operator, builder, or mixed
```

## Fail Conditions

- The package fails portability if this alignment requires `cogarch`,
  `~/.cogarch`, `OPERATIONS.md`, or a hidden global session state.
- A report fails if measured facts and interpretation are not separable.
- A proposal fails if the next action has no actor or owner.
- A knowledge export fails if it lacks source material, validation evidence, or
  `last_verified`.
