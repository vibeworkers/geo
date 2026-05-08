# GEO Policy Risk Gate

This gate prevents GEO reports from turning technical readiness into unsafe or
unsupported recommendations. It is an operational quality gate, not legal
advice. Short form: not legal advice.

## Risk Surfaces

| surface | check | output |
| --- | --- | --- |
| robots | Does the recommendation respect crawler directives and platform-specific user agents? | pass / fail / unknown |
| terms | Does the requested crawl, scrape, export, or reuse conflict with visible platform or site terms? | pass / fail / unknown |
| privacy | Does the evidence contain personal, private, logged-in, or connector-derived data? | pass / fail / unknown |
| regulated claims | Does the content touch medical, legal, finance, safety, or other regulated advice? | pass / fail / unknown |
| brand claims | Are brand superiority, ranking, citation, or conversion claims supported by evidence? | pass / fail / unknown |
| commerce eligibility | Is platform transaction eligibility proven, or only inferred from schema/readiness? | pass / fail / unknown |

## Escalation Rules

- If robots or terms are unknown, do not present the action as approved.
- If privacy is involved, separate public evidence from private evidence.
- If regulated claims are involved, avoid advice-like conclusions unless the
  user supplies approved source material.
- If brand claims are inferential, label them as heuristic_signal, not measured
  visibility.
- If commerce eligibility is not proven, mark platform transaction readiness as
  unknown.

## Required Report Fields

- `policy_risk`
- `robots_status`
- `terms_status`
- `privacy_status`
- `regulated_claims_status`
- `brand_claims_status`
- `commerce_eligibility_status`
