# geo-prospect 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-prospect-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-prospect` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-prospect/SKILL.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-prospect`
- 역할: 도메인의 GEO 현황을 빠르게 스캔해 영업/컨설팅 기회를 도출한다.
- beta output contract: `GEO-잠재고객-[도메인]-[날짜].md, GEO-잠재고객-배치-[날짜].md`
- main output contract: `GEO-잠재고객-[도메인]-[날짜].md, GEO-잠재고객-배치-[날짜].md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `40.0/100` | PASS | PASS | 357 | 0 |
| beta | `100.0/100` | PASS | PASS | 375 | 5 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_measurement_boundary` | FAIL | PASS |
| `regional_commerce_boundaries` | FAIL | PASS |
| `policy_private_boundaries` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `33`
- beta removed lines vs main: `15`
- beta에서 새로 연결된 reference:
  - `../../references/commerce-audit-worksheet.md`
  - `../../references/measurement-capture-template.md`
  - `../../references/platform-truth-registry.md`
  - `../../references/policy-risk-gate.md`
  - `../../references/regional-situational-routing.md`

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

- main gap: prospect scan claim의 source freshness와 regional context 분리 부족.
- site note: 빠른 스캔 기준으로는 crawler access 양호, content/entity 정렬과 performance scan risk가 큰 기회다.
- site note: 외부 검색 결과에는 자사 도메인과 외부 프로필이 함께 나타난다.
- measurement boundary: 영업 스캔은 lightweight triage이며 full audit을 대체하지 않는다.

## 7. External Search Snapshot

| source | use |
| --- | --- |
| [Search result: haegyung.com root](https://www.haegyung.com/) | brand/root visibility |
| [Search result: introduce page](https://www.haegyung.com/introduce/) | profile/entity surface |
| [Search result: Cake.me profile](https://www.cake.me/Gyung) | external profile mention |
| [Search result: about.me profile](https://about.me/ThinkHacker) | external profile mention |

## 8. 판정

판정: **beta 우세**. `geo-prospect` 기준으로 beta는 `100.0/100`, main은 `40.0/100`이다.
