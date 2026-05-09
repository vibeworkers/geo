# Google AI Overviews Public Capture - 2026-05-09

## Capture Metadata

| field | value |
| --- | --- |
| platform | `Google AI Overviews` |
| surface | `Google Search public AI Overview` |
| access_profile | `public signed-out browser` |
| captured_at | `2026-05-09T13:39:48Z` |
| region_language | `English Google UI; footer location varied within Ohio IP-based public session` |
| session | Firecrawl browser session `019e0cf4-7446-770d-b38c-e87d9a8135c3`, destroyed after capture |
| target | `Haegyung (해경)` at `https://haegyung.com` |

## Boundary

This capture covers Google Search AI Overview, not the standalone Gemini app.
It should be used for the benchmark row previously described as `Gemini / AI
Overviews` only on the public AI Overview side.

All three prompts triggered an AI Overview. None produced a target-positive
answer for `haegyung.com`, and none produced a target citation to
`haegyung.com`. P2 showed `haegyung.com` in a regular web result below the AI
Overview, but that is a SERP visibility signal, not an observed AI Overview
answer or citation.

## Prompt Outcome Summary

| prompt_id | AI Overview answer | visible target URL | classification |
| --- | --- | --- | --- |
| `P1` | Non-target entity resolution. The first snapshot treated `해경` as ambiguous between Korea Coast Guard and a Love Jinx character; a repeat extraction primarily resolved to Lim Haekyung from Love Jinx and mentioned Manta. | no | `not_observed_target_answer_or_citation` |
| `P2` | Wrong-entity official-source answer. AI Overview stated the official website for Haegyung / `해경` as Korea Coast Guard is `https://www.kcg.go.kr/`. | no in AI Overview; `haegyung.com` appeared only as regular web result | `not_observed_target_answer_or_citation` |
| `P3` | Wrong-entity source-proof answer. AI Overview described Korea Coast Guard Orchestra activity and linked to Korea Coast Guard / `해양경찰청`. | no | `not_observed_target_answer_or_citation` |

## P1

Prompt:

```text
Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.
```

Observed AI Overview behavior:

- Initial snapshot in the run described `해경(Haegyung)` as context-dependent,
  mainly Korea Coast Guard / `해양경찰청` and Lim Haekyung from Love Jinx.
- Repeat extraction from the same public AI Overview lane stated that
  `Haegyung (해경)` is primarily Lim Haekyung from Love Jinx, with Manta as the
  official webcomic platform.
- No `haegyung.com` target answer or citation was visible.

Classification:

- `answer_status`: `captured_non_target_or_ambiguous_entity`
- `citation_status`: `non_target_sources_no_target_citation`
- `evidence_label`: `not_observed_target_answer_or_citation`

## P2

Prompt:

```text
Find the official website or official source for Haegyung (해경) and explain why you believe it is official.
```

Observed AI Overview answer:

- AI Overview stated that the official website for Haegyung / `해경`, interpreted
  as Korea Coast Guard, is `https://www.kcg.go.kr/`.
- The visible rationale cited `.go.kr`, the English portal
  `https://www.kcg.go.kr/english/main.do`, government designation, official
  agency content, and external government linkage.
- Related AI Overview links included Korea Coast Guard / `해양경찰청` sources.
- A regular web result below the AI Overview showed `haegyung.com` and
  `https://www.haegyung.com`, but this was not part of the AI Overview answer
  or its visible citation set.

Classification:

- `answer_status`: `captured_wrong_entity`
- `citation_status`: `wrong_entity_source_cited_no_target_citation`
- `visible_citation_urls`: `https://www.kcg.go.kr/`,
  `https://www.kcg.go.kr/english/main.do`
- `serp_target_visibility`: `haegyung.com visible as regular web result only`
- `evidence_label`: `not_observed_target_answer_or_citation`

## P3

Prompt:

```text
Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.
```

Observed AI Overview answer:

- AI Overview resolved the prompt to Korea Coast Guard Orchestra activity.
- It described public outreach and maritime safety-themed performances by the
  Korea Coast Guard Orchestra.
- The visible AI Overview source label was Korea Coast Guard / `해양경찰청`, not
  `haegyung.com`.
- The regular web result below the AI Overview showed a non-target `Ha Kyung`
  musician result from Dork, not the intended `haegyung.com` source surface.

Classification:

- `answer_status`: `captured_wrong_entity`
- `citation_status`: `wrong_entity_source_cited_no_target_citation`
- `visible_citation_urls`: Korea Coast Guard / `해양경찰청` source label visible;
  target URL not visible
- `evidence_label`: `not_observed_target_answer_or_citation`

## Measurement Impact

Google AI Overview is a negative measured platform row for this prompt panel.
It does not weaken the readiness score, but it prevents any cross-platform
observed visibility headline. The current observed outcome claim remains:

- Perplexity public P1/P2: target-positive `observed_citation`
- Perplexity public P3: target-positive `observed_answer` only
- ChatGPT public default: negative target capture
- Google AI Overviews public: negative target capture
- exact ChatGPT Search-mode: still pending
