# GEO 전체 기능 벤치마크 비교 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-all-functions-benchmark-comparison-20260508` |
| generated_at | `2026-05-08` |
| scope | GEO `skills/geo-*` 전체 기능의 clean `main` vs `beta` readiness 비교 |
| score_type | `readiness` |
| evidence_label | `all_subskill_contract_diff + live_public_site_snapshot + search_snapshot` |
| confidence | `high` |
| evidence_path | `all-function-benchmarks/benchmark-index.json`, `all-function-benchmarks/reports/*.benchmark.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `caution` |

## 1. Executive Conclusion

GEO 패키지의 14개 서브스킬 전체를 기준으로 보면 `beta`가 clean `main`보다 전반적으로 우세하다. 차이는 코드 실행 속도보다 report/measurement/crawler/platform/policy 경계의 완성도에서 발생한다.

이번 비교는 clean `main@a652637`과 `beta@2d896ac`의 readiness 비교다. 기능 차이는 `beta`에 포함된 reference 및 subskill 계약 보강에서 나온다.

## 2. 전체 점수표

| skill | main | beta | delta | added lines | removed lines | report |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `geo-audit` | `28.6` | `100.0` | `71.4` | `33` | `5` | [reports/geo-audit.benchmark.md](reports/geo-audit.benchmark.md) |
| `geo-brand-mentions` | `40.0` | `100.0` | `60.0` | `6` | `0` | [reports/geo-brand-mentions.benchmark.md](reports/geo-brand-mentions.benchmark.md) |
| `geo-citability` | `50.0` | `100.0` | `50.0` | `7` | `0` | [reports/geo-citability.benchmark.md](reports/geo-citability.benchmark.md) |
| `geo-compare` | `40.0` | `100.0` | `60.0` | `15` | `5` | [reports/geo-compare.benchmark.md](reports/geo-compare.benchmark.md) |
| `geo-content` | `50.0` | `100.0` | `50.0` | `8` | `0` | [reports/geo-content.benchmark.md](reports/geo-content.benchmark.md) |
| `geo-crawlers` | `28.6` | `100.0` | `71.4` | `82` | `37` | [reports/geo-crawlers.benchmark.md](reports/geo-crawlers.benchmark.md) |
| `geo-llmstxt` | `50.0` | `100.0` | `50.0` | `9` | `2` | [reports/geo-llmstxt.benchmark.md](reports/geo-llmstxt.benchmark.md) |
| `geo-platform-optimizer` | `25.0` | `100.0` | `75.0` | `40` | `16` | [reports/geo-platform-optimizer.benchmark.md](reports/geo-platform-optimizer.benchmark.md) |
| `geo-proposal` | `33.3` | `100.0` | `66.7` | `23` | `0` | [reports/geo-proposal.benchmark.md](reports/geo-proposal.benchmark.md) |
| `geo-prospect` | `40.0` | `100.0` | `60.0` | `33` | `15` | [reports/geo-prospect.benchmark.md](reports/geo-prospect.benchmark.md) |
| `geo-report` | `33.3` | `100.0` | `66.7` | `32` | `6` | [reports/geo-report.benchmark.md](reports/geo-report.benchmark.md) |
| `geo-report-pdf` | `50.0` | `100.0` | `50.0` | `11` | `2` | [reports/geo-report-pdf.benchmark.md](reports/geo-report-pdf.benchmark.md) |
| `geo-schema` | `40.0` | `100.0` | `60.0` | `11` | `0` | [reports/geo-schema.benchmark.md](reports/geo-schema.benchmark.md) |
| `geo-technical` | `40.0` | `100.0` | `60.0` | `12` | `0` | [reports/geo-technical.benchmark.md](reports/geo-technical.benchmark.md) |

## 3. Ranking By Improvement

| rank | skill | delta | interpretation |
| ---: | --- | ---: | --- |
| 1 | `geo-platform-optimizer` | `75.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 2 | `geo-audit` | `71.4` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 3 | `geo-crawlers` | `71.4` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 4 | `geo-proposal` | `66.7` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 5 | `geo-report` | `66.7` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 6 | `geo-brand-mentions` | `60.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 7 | `geo-compare` | `60.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 8 | `geo-prospect` | `60.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 9 | `geo-schema` | `60.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 10 | `geo-technical` | `60.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 11 | `geo-citability` | `50.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 12 | `geo-content` | `50.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 13 | `geo-llmstxt` | `50.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |
| 14 | `geo-report-pdf` | `50.0` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |

## 4. 공통 라이브 사이트 리스크

- `https://haegyung.com`은 `https://www.haegyung.com/`로 수렴하고 HTTP 200이다.
- robots.txt, llms.txt, sitemap_index.xml은 모두 접근 가능하다.
- title은 `해경`, og:site_name은 `뮤직아카이브`, schema는 `MusicGroup` 중심이라 대표 entity가 분산되어 있다.
- desktop/mobile full-page scrollHeight가 각각 `153738`, `220029`로 매우 크다.
- PageSpeed Insights는 HTTP `429 quota exceeded`로 공식 Core Web Vitals를 확보하지 못했다.

## 5. External Sources Used

| source | use |
| --- | --- |
| [Search result: haegyung.com root](https://www.haegyung.com/) | brand/root visibility |
| [Search result: introduce page](https://www.haegyung.com/introduce/) | profile/entity surface |
| [Search result: Cake.me profile](https://www.cake.me/Gyung) | external profile mention |
| [Search result: about.me profile](https://about.me/ThinkHacker) | external profile mention |

## 6. Decision

전체 기능 벤치마크의 기준 표면은 `beta`를 채택한다. `main`은 portable baseline으로 유지할 수 있지만, 모든 GEO 기능을 실제 리포트 산출물로 연결하려면 beta의 report contract, measurement boundary, platform truth, policy/private/regional 경계가 필요하다.
