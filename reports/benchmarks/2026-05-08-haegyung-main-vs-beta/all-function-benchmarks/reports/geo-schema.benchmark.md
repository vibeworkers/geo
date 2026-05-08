# geo-schema 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-schema-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-schema` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-schema/SKILL.md`, `data/comparison.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-schema`
- 역할: 현재 스키마를 파악하고 Organization, Article, FAQPage 등 구조화 데이터를 제안한다.
- beta output contract: `GEO-스키마-[도메인].md`
- main output contract: `GEO-스키마-[도메인].md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `40.0/100` | PASS | PASS | 567 | 0 |
| beta | `100.0/100` | PASS | PASS | 578 | 3 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_six_domains` | FAIL | PASS |
| `regional_commerce_boundaries` | FAIL | PASS |
| `validator_checks_subskill_references` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `11`
- beta removed lines vs main: `0`
- beta에서 새로 연결된 reference:
  - `../../references/commerce-audit-worksheet.md`
  - `../../references/commerce-readiness.md`
  - `../../references/platform-truth-registry.md`

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

- main gap: schema가 audit formula에 포함되는 방식과 텍스트 설명이 불일치한다.
- site note: root JSON-LD 타입은 MusicGroup 중심이며 title의 해경, og:site_name의 뮤직아카이브와 entity가 분산된다.
- site note: Article/Person 후보는 개별 글에서 더 강하게 관측될 가능성이 있다.
- site note: root에는 SearchAction/WebSite/CollectionPage가 함께 있다.
- measurement boundary: 스키마 제안은 코드 배포 전까지 readiness claim이다.

## 7. External Search Snapshot

이 기능 리포트에서는 외부 검색 결과를 핵심 evidence로 사용하지 않았다.

## 8. 판정

판정: **beta 우세**. `geo-schema` 기준으로 beta는 `100.0/100`, main은 `40.0/100`이다.

