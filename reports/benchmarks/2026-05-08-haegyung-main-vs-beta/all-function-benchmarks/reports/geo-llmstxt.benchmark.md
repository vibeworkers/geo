# geo-llmstxt 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-llmstxt-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-llmstxt` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-llmstxt/SKILL.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-llmstxt`
- 역할: llms.txt 존재, 구조, sitemap 연결, AI용 요약 품질을 평가한다.
- beta output contract: `GEO-llmstxt-분석.md`
- main output contract: `GEO-llmstxt-분석.md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `50.0/100` | PASS | PASS | 448 | 0 |
| beta | `100.0/100` | PASS | PASS | 455 | 2 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_measurement_boundary` | FAIL | PASS |
| `policy_private_boundaries` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `9`
- beta removed lines vs main: `2`
- beta에서 새로 연결된 reference:
  - `../../references/measurement-capture-template.md`
  - `../../references/policy-risk-gate.md`

## 5. haegyung.com 공통 관측값

| signal | value |
| --- | --- |
| `target_url` | https://haegyung.com |
| `captured_at` | 2026-05-07T21:01:17Z |
| `homepage_status` | 200 |
| `final_url` | https://www.haegyung.com/ |
| `response_ms_median` | 2558.5 |
| `html_bytes` | 700038 |
| `title` | 해경 - 낮이건 밤이건 우리의 길을 비추는 존재를 빚어간다. |
| `description_length` | 28 |
| `html_lang` | ko-KR |
| `og_site_name` | 뮤직아카이브 |
| `og_image` |  |
| `h1_count` | 5 |
| `h2_count` | 166 |
| `schema_types` | CollectionPage, ImageObject, MusicGroup, SearchAction, WebSite |
| `llms_exists` | True |
| `llms_bytes` | 14525 |
| `sitemap_exists` | True |

### Browser Performance

| viewport | wall | responseStart | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| desktop | `5509ms` | `3018ms` | `4178ms` | `5506ms` | `87` | `2117920` | `153738` |
| mobile | `4892ms` | `2416ms` | `3649ms` | `4890ms` | `89` | `2218311` | `220029` |

## 6. 기능별 해석

- main gap: llms.txt의 platform adoption/heuristic 경계가 약하다.
- site note: llms.txt는 HTTP 200, 14525 bytes, sitemap mention 있음으로 관측됐다.
- site note: 응답 헤더에 x-robots-tag noindex,nofollow가 있어 해석 경계가 필요하다.
- site note: llms.txt는 adoption-dependent 보조 신호다.
- measurement boundary: llms.txt 존재는 AI 플랫폼 노출 보장이 아니다.

## 7. External Search Snapshot

이 기능 리포트에서는 외부 검색 결과를 핵심 evidence로 사용하지 않았다.

## 8. 판정

판정: **beta 우세**. `geo-llmstxt` 기준으로 beta는 `100.0/100`, main은 `50.0/100`이다.
