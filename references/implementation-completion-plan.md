# GEO P2-P13 Implementation Completion Plan

This plan defines the complete functional requirements, judgment conditions,
sequence-dependent work plan, and completion rule for the `geo` package
hardening work.

## Goal

Make the portable `geo` package able to route, execute, report, and verify GEO
work without overclaiming platform mechanisms, measured outcomes, commerce
readiness, private-surface behavior, regional platform behavior, or policy-risk
status.

## Requirement Set

| id | requirement | done condition |
| --- | --- | --- |
| RQ1 | Preserve portable activation, language selection, source-order, and execution-bundle routing | `SKILL.md`, `README.md`, and validator still pass the existing portable baseline checks |
| RQ2 | Keep official platform facts separate from assumptions | `references/platform-truth-registry.md` exists and records `source_url`, `last_verified`, `confidence`, and `package_action` |
| RQ3 | Provide a repeatable measurement capture process | `references/measurement-capture-template.md` defines Prompt Panel, Run Metadata, Capture Table, Before/After Comparison, and `evidence_label` |
| RQ4 | Separate commerce/action readiness from schema validity | `references/commerce-audit-worksheet.md` defines Product Identity, Schema Readiness, Merchant Facts, Catalog / Feed, Checkout / Action, and Measurement Readiness |
| RQ5 | Separate public, private, logged-in, connector, and user-provided answer surfaces | `references/private-surface-routing.md` defines `public_crawler_surface`, `private_connector_surface`, permission profile, and Do not use private evidence boundary |
| RQ6 | Add regional and situational routing without inventing regional platform mechanisms | `references/regional-situational-routing.md` defines B2B SaaS, ecommerce, Naver/Kakao/Daum, regulated, new brand, and mature brand handling |
| RQ7 | Add policy-risk gating | `references/policy-risk-gate.md` defines robots, terms, privacy, regulated claims, brand claims, and commerce eligibility checks |
| RQ8 | Standardize report outputs | `references/report-template-contract.md` requires `score_type`, `evidence_label`, `confidence`, `measurement_status`, `commerce_status`, `private_surface_status`, `regional_context`, and `policy_risk` |
| RQ9 | Connect the new references to the top-level router | `SKILL.md` includes Gates 10-13 and references the new files in External SoT, Canonical SoT, Rubric, and References |
| RQ10 | Connect the new references to existing execution workflows | Existing `skills/geo-*` subskills route audit, platform, schema, report, proposal, and technical claims through the relevant contracts |
| RQ11 | Harden validation so regressions are caught | `scripts/check_geo_skill.py` checks the new files, gates, README references, and reference contract phrases |
| RQ12 | Produce a verification set and patch artifact | `python3 scripts/check_geo_skill.py`, `git diff --check`, stale-claim search, portability search, and patch generation all complete |
| RQ13 | Close with a handoff boundary | The final report records `completion_judgment`, `all_must_passed` or failed queue, verification set, patch path, and release/push boundary |
| RQ14 | Support sequence-dependent autopilot for all-in requests | `references/sequence-dependent-autopilot.md`, `SKILL.md`, gates, scenarios, matrix, README, and validator define all-in trigger handling, ordered dependency graph execution, verification, ledger recording, and stop conditions |

## P2-P13 Sequence

| phase | depends on | action | completion evidence |
| --- | --- | --- | --- |
| P2 | P0/P1 platform and measurement corrections | Add platform truth registry | Platform claims have source_url, last_verified, confidence |
| P3 | P2 | Add measurement capture template | Outcome claims can be captured as observed_answer, observed_citation, referral_signal, or conversion_signal |
| P4 | P3 | Add commerce audit worksheet | Product schema, merchant, catalog, checkout/action, and measurement readiness are separated |
| P5 | P3 | Add private-surface routing | Public visibility claims are not inferred from private connector or user-provided context |
| P6 | P2/P5 | Add regional and situational routing | Regional claims require separate official evidence |
| P7 | P2-P6 | Add policy-risk gate | robots, terms, privacy, regulated claims, brand claims, and commerce eligibility are checked |
| P8 | P3-P7 | Add report template contract | Every report has score_type, evidence_label, confidence, and risk/status fields |
| P9 | P8 | Wire references into `SKILL.md`, `README.md`, glossary, concept map, gates, scenarios, matrix | Router and reference surfaces expose the new contracts |
| P10 | P9 | Update execution subskills | Existing workflows point to measurement, commerce, private, regional, policy, and report contracts |
| P11 | P9/P10 | Harden validator | New omissions fail `scripts/check_geo_skill.py` |
| P12 | P11 | Run targeted verification and create patch bundle | Verification commands pass and patch can be reviewed |
| P13 | P12 | Write closeout report | `completion_judgment=pass` only if all Must checks pass |
| P14 | P13 | Add sequence-dependent autopilot | All-in requests run through ordered dependency graph, phase verification, ledger recording, and stop conditions |

## Adaptive Judgment Criteria

- If an official-source fact is missing or stale, mark it as `확인 필요`
  instead of implementing a platform-specific claim.
- If an outcome is not captured, label it readiness or heuristic, not measured
  visibility.
- If commerce eligibility is not verified, treat schema and product readiness
  as prerequisites only.
- If private or logged-in context is involved, separate it from public GEO
  visibility.
- If a regional platform is named, require a separate official evidence pack
  before giving platform-specific implementation steps.
- If policy status is unknown, report `policy_risk=unknown` or `caution`, not
  safe.
- If a validator fails, fix the smallest missing contract before broad edits.
- If the user asks for all processes, continue through the ordered dependency
  graph until every required phase passes or a stop condition is recorded.

## Completion Rubric

Must:

- all RQ1-RQ14 done conditions are represented in package files
- top-level router exposes Gates 8-13
- top-level router exposes Gate 14 for sequence-dependent autopilot
- existing execution subskills reference the new contracts where relevant
- validator checks the new contracts
- verification set passes locally
- patch bundle and closeout report exist

Should:

- keep new files portable and free of machine-local absolute paths
- avoid adding new subskills when references and existing workflow owners are
  enough
- preserve stored prompts in English
- leave release, push, and publication as explicit handoff actions

## Completion Judgment

Use:

```text
completion_judgment=pass
all_must_passed=true
```

only when every Must item passes. Otherwise use:

```text
completion_judgment=blocked
failed_must_queue=<ordered failed items>
```
