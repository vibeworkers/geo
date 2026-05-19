# GEO Report Template Contract

Every consolidated GEO report should expose its claim type, evidence quality,
and unresolved boundary conditions. This contract applies to markdown reports,
proposal summaries, PDF-ready reports, and executive handoffs.

## Required Metadata

| field | required | meaning |
| --- | --- | --- |
| `report_id` | yes | Stable report identifier |
| `generated_at` | yes | Date or date-time of synthesis |
| `scope` | yes | Site, brand, product, corpus, or workflow scope |
| `score_type` | yes | readiness, heuristic, observed, referral, conversion, or mixed |
| `evidence_label` | yes | Label from `references/measurement-loop.md` |
| `confidence` | yes | high, medium, low |
| `evidence_path` | yes | Relative path or external URL proving the claim |
| `last_verified` | yes | Date the platform or evidence claim was checked |
| `measurement_status` | yes | not measured, ready to measure, observed_answer, observed_citation, referral_signal, or conversion_signal |
| `commerce_status` | yes | not applicable, product/schema only, merchant/catalog ready, checkout/action ready, or platform eligible |
| `private_surface_status` | yes | public only, private evidence separated, private evidence used, or unknown |
| `regional_context` | yes | default, named region, named language, or unknown |
| `policy_risk` | yes | pass, caution, blocked, or unknown |

## Section Order

1. Executive conclusion
2. Scope and evidence
3. Platform truth and access profile
4. Measurement status
5. Commerce/action status when applicable
6. Regional and situational context when applicable
7. Policy risk gate
8. Prioritized remediation plan
9. Claim boundary ledger: measured facts, interpretation, assumptions, unknowns
10. Actor-first handoff when applicable
11. Remaining gaps and next verification

## Claim Labels

- Use `score_type=readiness` for crawler, schema, content, and technical setup.
- Use `score_type=heuristic` for likely but unobserved platform behavior.
- Use `score_type=observed` only when answer or citation evidence was captured.
- Use `score_type=referral` only when analytics or logs show platform traffic.
- Use `score_type=conversion` only when action or commerce systems show the
  conversion evidence.

## Claim Boundary Ledger

Every report should keep the following categories separable:

- measured facts: crawler output, captured answers, analytics, logs, validator
  output, or explicitly provided source text
- interpretation: the reasoning that connects measured facts to readiness,
  priority, or risk
- assumptions: unverified conditions accepted for the current report
- unknowns: missing evidence that could change the recommendation

If space is limited, use a compact table:

| boundary | entries |
| --- | --- |
| measured facts | |
| interpretation | |
| assumptions | |
| unknowns | |

Do not present interpretation as measurement. Do not present assumptions as
verified facts.

## Actor-First Handoff

When a report or proposal includes a handoff, identify the receiving actor:

| actor | required handoff content |
| --- | --- |
| decision maker | conclusion, risk, budget or priority implication, owner |
| operator | exact surface, action sequence, verification step, fallback |
| builder | file, command, schema, API, test, rollback or failure mode |

Audience-specific wording may change packaging, but it must not remove
evidence labels, source paths, confidence, or unresolved gaps.

## Fail Conditions

- A report fails if it has a score without `evidence_label`.
- A report fails if it makes platform-specific claims without `last_verified`.
- A report fails if it mixes private and public evidence without
  `private_surface_status`.
- A report fails if commerce claims omit `commerce_status`.
- A report fails if policy risk is unknown but presented as safe.
- A report fails if measured facts and interpretation are collapsed into one
  unsupported claim.
- A handoff fails if the next action has no actor or owner.
