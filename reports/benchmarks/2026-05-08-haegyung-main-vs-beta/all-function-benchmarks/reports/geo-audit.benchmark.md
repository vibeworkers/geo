# geo-audit 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-audit-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-audit` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-audit/SKILL.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-audit`
- 역할: crawler, citability, content, technical, schema, platform signals를 종합 감사한다.
- beta output contract: `GEO-감사-보고서.md`
- main output contract: `GEO-감사-보고서.md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `28.6/100` | PASS | PASS | 318 | 0 |
| beta | `100.0/100` | PASS | PASS | 346 | 8 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_six_domains` | FAIL | PASS |
| `audit_measurement_boundary` | FAIL | PASS |
| `audit_report_contract` | FAIL | PASS |
| `policy_private_boundaries` | FAIL | PASS |
| `regional_commerce_boundaries` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `33`
- beta removed lines vs main: `5`
- beta에서 새로 연결된 reference:
  - `../../references/commerce-audit-worksheet.md`
  - `../../references/commerce-readiness.md`
  - `../../references/measurement-capture-template.md`
  - `../../references/measurement-loop.md`
  - `../../references/policy-risk-gate.md`
  - `../../references/private-surface-routing.md`
  - `../../references/regional-situational-routing.md`
  - `../../references/report-template-contract.md`

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

- main gap: 5-domain 텍스트와 schema 포함 공식 사이의 불일치, report/measurement boundary 부족.
- site note: 홈페이지는 HTTP 200이고 robots meta는 follow,index다.
- site note: H1 5개, H2 166개로 entry surface가 매우 넓다.
- site note: JSON-LD 타입은 CollectionPage, ImageObject, MusicGroup, SearchAction, WebSite다.
- site note: full-page scrollHeight가 desktop 153738, mobile 220029로 비정상적으로 크다.
- measurement boundary: full audit readiness이며 실제 AI answer/citation 관측은 별도 capture가 필요하다.

## 7. External Search Snapshot

이 기능 리포트에서는 외부 검색 결과를 핵심 evidence로 사용하지 않았다.

## 8. 판정

판정: **beta 우세**. `geo-audit` 기준으로 beta는 `100.0/100`, main은 `28.6/100`이다.
