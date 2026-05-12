# GEO Deep Audit Ecommerce Glossary

| Term | Definition in this skill |
| --- | --- |
| captured audit finding | A claim already present in the copied raw audit files. It is evidence inside this package, not proof of current live state. |
| readiness score | A heuristic score from `raw/audit_scorecard.csv` or the raw reports. It estimates preparedness, not measured AI visibility. |
| AI crawler access | The audit's interpretation of robots.txt or crawler policy exposure for AI-related bots. |
| citability | The likelihood that available public content can support AI answers or citations, based on the audit pack. |
| live validation | A new check outside the packaged source, such as current robots fetches, HTTP status tests, schema extraction, server logs, or AI answer captures. |
| output brand | The brand displayed on a derived deliverable. It is separate from the provenance of the raw audit pack. |
| raw evidence | The copied source files under `raw/`; these files are not edited by this skill. |
| follow-up measurement | Later evidence about observed answers, observed citations, referral traffic, or conversions. It cannot be inferred from the readiness score alone. |
