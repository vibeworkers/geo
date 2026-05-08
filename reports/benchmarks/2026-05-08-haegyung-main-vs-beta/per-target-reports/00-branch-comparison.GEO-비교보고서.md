# GEO 브랜치별 리포트 비교

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-branch-perf-comparison-20260508` |
| generated_at | `2026-05-08` |
| scope | `main-clean-baseline` vs `beta`의 `https://haegyung.com` 진단 준비도 비교 |
| score_type | `readiness` |
| evidence_label | `per_target_report_synthesis + local_contract_validation + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `per-target-reports/01-main-clean-baseline.GEO-종합보고서.md`, `per-target-reports/02-beta.GEO-종합보고서.md` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `caution` |

## 1. Executive Conclusion

비교 기준을 `main@a652637` vs `beta@2d896ac`로 잡으면 `beta`가 명확히 우세합니다.

초기 probe는 beta commit 직전에 수행됐고, 같은 GEO readiness surface가 `beta@2d896ac`로 커밋됐다. 따라서 이 보존본은 `main` baseline과 `beta` branch surface의 readiness 비교로 읽어야 합니다.

## 2. Per-target Report Inventory

| 비교 대상 | 리포트 산출물 |
| --- | --- |
| main-clean-baseline | `per-target-reports/01-main-clean-baseline.GEO-종합보고서.md` |
| beta | `per-target-reports/02-beta.GEO-종합보고서.md` |
| 비교 요약 | `per-target-reports/00-branch-comparison.GEO-비교보고서.md` |

## 3. Score Comparison

| 항목 | main-clean-baseline | beta | 판정 |
| --- | ---: | ---: | --- |
| validator | PASS | PASS | 동률 |
| validator elapsed | `49.6ms` | `87.9ms` | main이 빠르지만 기능 검증 범위가 좁음 |
| reference count | `7` | `17` | beta 우세 |
| readiness score | `10/100` | `100/100` | beta 우세 |
| changed surface | clean baseline | `beta@2d896ac` | beta가 비교 대상의 실질 변경 표면 |

## 4. Check Matrix

| Check | main-clean-baseline | beta | 해석 |
| --- | --- | --- | --- |
| `validator_pass` | PASS | PASS | 둘 다 portable package 기본 검증은 통과 |
| `new_reference_set_complete` | FAIL | PASS | beta는 신규 reference set 포함 |
| `audit_six_domains` | FAIL | PASS | beta는 schema 포함 6-domain audit와 일치 |
| `audit_measurement_boundary` | FAIL | PASS | beta는 측정/미측정 claim 분리 가능 |
| `audit_report_contract` | FAIL | PASS | beta는 report-template-contract 연결 |
| `crawler_search_user_split` | FAIL | PASS | beta는 search/user/training crawler 경계 보강 |
| `google_extended_correct_boundary` | FAIL | PASS | beta 우세 |
| `grok_uncertainty_marked` | FAIL | PASS | beta 우세 |
| `stale_anthropic_ai_removed` | FAIL | PASS | beta 우세 |
| `policy_private_boundaries` | FAIL | PASS | beta 우세 |
| `regional_commerce_boundaries` | FAIL | PASS | beta 우세 |
| `validator_checks_subskill_references` | FAIL | PASS | beta validator coverage 우세 |

## 5. Shared Live Site Evidence

두 브랜치 모두 같은 라이브 사이트 관측값을 사용합니다.

| 항목 | 값 |
| --- | --- |
| target | `https://haegyung.com` |
| final URL | `https://www.haegyung.com/` |
| homepage HTTP | `200` |
| median response | `2558.5ms` |
| HTML bytes | `700038` |
| lang | `ko-KR` |
| H1 / H2 | `5` / `166` |
| images missing alt | `0` |
| llms.txt | HTTP `200`, sitemap mention 있음 |
| sitemap_index.xml | HTTP `200` |
| desktop loadEnd | `5506ms` |
| mobile loadEnd | `4890ms` |
| desktop scrollHeight | `153738` |
| mobile scrollHeight | `220029` |

## 6. Interpretation

`main`은 빠르게 validator를 통과하지만, 통과 범위가 좁습니다. 성능 비교 리포트에서 필요한 “근거 유형”, “관측 여부”, “플랫폼 정책 경계”, “private/public evidence 분리”, “지역/언어 맥락”을 충분히 표현하지 못합니다.

`beta`는 validator 시간이 더 길지만, 검증 범위가 넓어졌습니다. 이번 목적이 단순 빌드 속도 비교가 아니라 사이트 진단 리포트 품질 비교이므로, `beta`가 목적에 더 맞습니다.

## 7. Remaining Gaps

- PageSpeed Insights가 HTTP `429`로 실패하여 Core Web Vitals 공식값은 아직 없습니다.
- beta 수치는 초기 staged probe를 `beta@2d896ac`로 정규화한 값입니다.
- 다음 branch-to-branch 재측정에서는 beta clean worktree에서 validator timing을 다시 캡처하면 더 엄밀합니다.

## 8. Decision

이번 비교의 기준 리포트는 `beta`를 채택합니다. `main`은 baseline/대조군으로 유지하되, 실제 `haegyung.com` 진단 산출물은 `beta`의 report contract와 measurement boundary를 기준으로 작성하는 것이 맞습니다.
