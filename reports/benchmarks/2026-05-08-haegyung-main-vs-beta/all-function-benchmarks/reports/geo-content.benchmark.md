# geo-content 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-content-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-content` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-content/SKILL.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-content`
- 역할: 본문 구조, 저자성, 신뢰도, 신선도, AI 검색용 답변 구조를 평가한다.
- beta output contract: `GEO-콘텐츠-분석.md`
- main output contract: `GEO-콘텐츠-분석.md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `50.0/100` | PASS | PASS | 360 | 0 |
| beta | `100.0/100` | PASS | PASS | 368 | 2 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_measurement_boundary` | FAIL | PASS |
| `policy_private_boundaries` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `8`
- beta removed lines vs main: `0`
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

- main gap: policy-risk gate와 observed answer boundary가 약하다.
- site note: title/description은 한국어로 정렬되어 있으나 og:site_name은 뮤직아카이브다.
- site note: H2가 166개라 root content scope가 넓고 scanning cost가 높다.
- site note: 이미지 missing alt는 0으로 관측된다.
- measurement boundary: 콘텐츠 품질은 readiness/heuristic이며 AI 답변 포함 증거는 아니다.

## 7. External Search Snapshot

이 기능 리포트에서는 외부 검색 결과를 핵심 evidence로 사용하지 않았다.

## 8. 판정

판정: **beta 우세**. `geo-content` 기준으로 beta는 `100.0/100`, main은 `50.0/100`이다.
