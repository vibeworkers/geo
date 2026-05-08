# main-clean-baseline GEO 진단 준비도 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-branch-perf-main-clean-baseline-20260508` |
| generated_at | `2026-05-08` |
| scope | `main-clean-baseline` 브랜치 표면이 `https://haegyung.com` 진단에 제공하는 기능 |
| score_type | `readiness` |
| evidence_label | `local_contract_validation + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `data/comparison.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `caution` |

## 1. Executive Conclusion

`main-clean-baseline`은 GEO 패키지 validator는 통과하지만, 현재 `https://haegyung.com` 같은 공개 사이트를 비교 진단하기에는 준비도가 낮습니다.

핵심 이유는 validator가 통과하더라도 최신 reference set, 6-domain audit, measurement boundary, report contract, crawler search/user/training 분리 같은 비교 진단 기능이 빠져 있기 때문입니다. 따라서 `main`은 “패키지가 깨지지는 않음”을 증명하지만, “성능 비교 진단을 충분히 설명함”까지는 증명하지 못합니다.

## 2. Scope And Evidence

| 항목 | 값 |
| --- | --- |
| 비교 대상 | `main-clean-baseline` |
| rev | `a652637` |
| validator | PASS |
| validator elapsed | `49.6ms` |
| reference count | `7` |
| readiness score | `10/100` |
| 기준 파일 | `data/comparison.json` |

## 3. Platform Truth And Access Profile

공통 라이브 사이트 관측값:

| 항목 | 값 |
| --- | --- |
| 대상 URL | `https://haegyung.com` |
| 최종 URL | `https://www.haegyung.com/` |
| homepage HTTP | `200` |
| median response | `2558.5ms` |
| HTML bytes | `700038` |
| html lang | `ko-KR` |
| robots meta | `follow, index` |
| canonical | `https://www.haegyung.com/` |
| llms.txt | HTTP `200`, `14525` bytes |
| sitemap_index.xml | HTTP `200`, `913` bytes |

robots.txt 기준 주요 봇 접근은 모두 허용으로 파싱됐습니다: `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `Googlebot`, `Google-Extended`, `PerplexityBot`, `Bingbot`, `GrokBot`, `xAI-Grok`, `Grok-DeepSearch`.

## 4. Measurement Status

이 브랜치에서 직접 관측 답변, citation, referral, conversion은 측정하지 않았습니다. 이번 점수는 `readiness` 점수입니다.

공통 브라우저 성능 관측:

| viewport | wall | responseStart | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| desktop | `5509ms` | `3018ms` | `4178ms` | `5506ms` | `87` | `2117920` | `153738` |
| mobile | `4892ms` | `2416ms` | `3649ms` | `4890ms` | `89` | `2218311` | `220029` |

PageSpeed Insights는 mobile/desktop 모두 HTTP `429 quota exceeded`로 Core Web Vitals를 확보하지 못했습니다.

## 5. Commerce And Action Status

이번 비교 범위는 GEO 진단 패키지 준비도와 공개 사이트 접근성입니다. 커머스/action conversion은 적용 대상이 아니므로 `commerce_status=not applicable`입니다.

## 6. Regional And Situational Context

사이트 언어와 리포트 수신 맥락은 한국어입니다. 사이트 `html_lang`은 `ko-KR`이고, title/description도 한국어입니다.

## 7. Policy Risk Gate

`main-clean-baseline`의 risk는 `caution`입니다. 봇 접근 자체는 열려 있지만, 오래된 crawler taxonomy와 platform boundary 부족 때문에 플랫폼별 정책 해석을 안전하게 닫기 어렵습니다.

## 8. Prioritized Remediation Plan

| 우선순위 | 항목 | 이유 |
| --- | --- | --- |
| 즉시 | 6-domain audit 계약 보강 | schema 포함 감사 공식과 텍스트 설명이 맞아야 비교 점수가 안정화됨 |
| 즉시 | measurement/report contract 추가 | 관측값, readiness, heuristic 주장을 분리해야 함 |
| 단기 | crawler taxonomy 갱신 | search/user/training crawler 경계를 잘못 섞으면 robots 해석이 흔들림 |
| 단기 | private/regional/policy boundary 추가 | 공개 사이트 진단이라도 LLM 표면별 claim risk를 분리해야 함 |

## 9. Remaining Gaps And Next Verification

`main-clean-baseline`은 validator pass 외의 비교 진단 Must 대부분을 충족하지 못합니다. 이 브랜치는 “기준선”으로는 유용하지만, 현재 사이트 진단 결과를 설명하는 실행 표면으로는 부족합니다.

