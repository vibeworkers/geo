# GEO Measurement Capture Template

This template turns GEO outcome checks into repeatable evidence. It is used
after readiness work when the question is whether a brand, page, citation, or
commerce action appeared in an AI or search-assisted answer.

Stored prompts must be English. Conversation notes may be Korean or English.

## Prompt Panel

Use a small prompt panel instead of a single prompt.

| prompt_id | Prompt | intent | expected evidence |
| --- | --- | --- | --- |
| P1 | Compare Brand A and Brand B for the buyer problem described here. | competitive discovery | brand mention, source citation, recommendation position |
| P2 | Which product would you choose for this use case and why? | recommendation | answer inclusion, evidence path, confidence |
| P3 | Find an official source for Brand A pricing, shipping, and returns. | commerce proof | observed_citation, checkout/action availability |
| P4 | What changed since the last crawl or content update? | before/after | delta and evidence_label |

## Run Metadata

Record these fields for every capture:

| field | required | notes |
| --- | --- | --- |
| `run_id` | yes | Stable ID for this measurement run |
| `captured_at` | yes | ISO date or date-time |
| `platform` | yes | ChatGPT, Google AI Overviews, Perplexity, Claude, Copilot, Grok, or another named surface |
| `access_profile` | yes | public, logged-in, private connector, browser, API, or unknown |
| `region_language` | yes | Country, locale, and answer language if known |
| `prompt_id` | yes | Link to the Prompt Panel row |
| `prompt_text` | yes | Stored in English unless the tested task requires a non-English source query |
| `answer_snapshot` | yes | Short excerpt or pointer to a saved capture |
| `evidence_label` | yes | readiness_signal, heuristic_signal, observed_answer, observed_citation, referral_signal, or conversion_signal |
| `confidence` | yes | high, medium, low |
| `evidence_path` | yes | Portable relative path or external URL |

## Capture Table

| prompt_id | platform | access_profile | answer_status | citation_status | brand_position | evidence_label | confidence | evidence_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 |  |  | absent / mentioned / recommended | none / cited / source shown |  |  |  |  |

## Before/After Comparison

| field | before | after | delta | interpretation |
| --- | --- | --- | --- | --- |
| observed answer inclusion |  |  |  |  |
| observed_citation |  |  |  |  |
| referral signal |  |  |  |  |
| conversion signal |  |  |  |  |

## Evidence Labels

- `readiness_signal`: crawler access, schema, content, or feed condition exists.
- `heuristic_signal`: likely improvement based on known platform behavior, but
  not directly observed in an answer.
- `observed_answer`: the brand, page, or product appeared in a captured answer.
- `observed_citation`: the answer included a source/citation that can be saved.
- `referral_signal`: analytics or logs show traffic from the platform.
- `conversion_signal`: analytics or commerce systems show qualified action or
  transaction evidence.

## Close Rule

A measured GEO outcome is closed only when the capture table and before/after
comparison identify `evidence_label`, `confidence`, `evidence_path`, and a
specific platform/access profile.
