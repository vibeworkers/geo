# geo-brand-mentions 개별 벤치마크 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-geo-brand-mentions-20260508` |
| generated_at | `2026-05-08` |
| scope | `geo-brand-mentions` 기능의 clean `main` vs `beta` readiness benchmark for `https://haegyung.com` |
| score_type | `readiness` |
| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `skills/geo-brand-mentions/SKILL.md`, `data/comparison.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. 기능 정의

- 기능명: `geo-brand-mentions`
- 역할: 외부 사이트, 프로필, 커뮤니티, AI-visible source의 브랜드 언급성을 평가한다.
- beta output contract: `GEO-브랜드언급-분석.md`
- main output contract: `GEO-브랜드언급-분석.md`

## 2. 브랜치별 readiness 점수

| surface | score | validator | skill exists | line count | reference count |
| --- | ---: | --- | --- | ---: | ---: |
| main-clean-baseline | `40.0/100` | PASS | PASS | 433 | 0 |
| beta | `100.0/100` | PASS | PASS | 439 | 2 |

## 3. 평가 항목

| criterion | main | beta |
| --- | --- | --- |
| `skill_exists` | PASS | PASS |
| `validator_pass` | PASS | PASS |
| `audit_measurement_boundary` | FAIL | PASS |
| `policy_private_boundaries` | FAIL | PASS |
| `regional_commerce_boundaries` | FAIL | PASS |

## 4. 계약 diff 요약

- beta added lines vs main: `6`
- beta removed lines vs main: `0`
- beta에서 새로 연결된 reference:
  - `../../references/measurement-capture-template.md`
  - `../../references/private-surface-routing.md`

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

- main gap: measured visibility와 private/public mention 분리 계약이 약하다.
- site note: 검색 스냅샷에서 자사 도메인 결과가 다수 노출된다.
- site note: 외부 프로필 표면으로 Cake.me와 about.me가 확인된다.
- site note: 브랜드 문자열은 해경, 고경만, haegyung, 뮤직아카이브로 분산된다.
- measurement boundary: 브랜드 언급 점수는 observed answer inclusion이 아니라 visibility readiness다.

## 7. External Search Snapshot

| source | use |
| --- | --- |
| [Search result: haegyung.com root](https://www.haegyung.com/) | brand/root visibility |
| [Search result: introduce page](https://www.haegyung.com/introduce/) | profile/entity surface |
| [Search result: Cake.me profile](https://www.cake.me/Gyung) | external profile mention |
| [Search result: about.me profile](https://about.me/ThinkHacker) | external profile mention |

## 8. 판정

판정: **beta 우세**. `geo-brand-mentions` 기준으로 beta는 `100.0/100`, main은 `40.0/100`이다.

