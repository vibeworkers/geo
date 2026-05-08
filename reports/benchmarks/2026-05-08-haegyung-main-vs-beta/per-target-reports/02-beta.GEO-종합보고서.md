# beta GEO 진단 준비도 리포트

## Report Metadata

| field | value |
| --- | --- |
| report_id | `geo-branch-perf-beta-20260508` |
| generated_at | `2026-05-08` |
| scope | `beta` 표면이 `https://haegyung.com` 진단에 제공하는 기능 |
| score_type | `readiness` |
| evidence_label | `local_contract_validation + live_public_site_snapshot` |
| confidence | `high` |
| evidence_path | `data/comparison.json`, `data/browser-performance.json` |
| last_verified | `2026-05-07T21:04:14Z` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR` |
| policy_risk | `pass` |

## 1. Executive Conclusion

`beta`는 `https://haegyung.com` 진단에 필요한 비교 준비도가 높습니다.

`beta@2d896ac`는 measurement, commerce, private surface, regional, policy risk, report contract 경계를 추가하고, crawler taxonomy를 search/user/training 기준으로 보정합니다. 따라서 `main`보다 단순 validator 통과를 넘어 “무엇을 측정했고, 무엇은 아직 관측하지 않았는지”를 보고서에서 분리하기 좋습니다.

## 2. Scope And Evidence

| 항목 | 값 |
| --- | --- |
| 비교 대상 | `beta` |
| branch | `beta` |
| rev | `2d896ac` |
| validator | PASS |
| validator elapsed | `87.9ms` |
| reference count | `17` |
| readiness score | `100/100` |
| 기준 파일 | `data/comparison.json` |

추가된 핵심 reference set:

- `references/measurement-loop.md`
- `references/measurement-capture-template.md`
- `references/report-template-contract.md`
- `references/commerce-readiness.md`
- `references/commerce-audit-worksheet.md`
- `references/private-surface-routing.md`
- `references/regional-situational-routing.md`
- `references/policy-risk-gate.md`
- `references/platform-truth-registry.md`
- `references/implementation-completion-plan.md`

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
| title | `해경 - 낮이건 밤이건 우리의 길을 비추는 존재를 빚어간다.` |
| og:site_name | `뮤직아카이브` |
| JSON-LD types | `CollectionPage`, `ImageObject`, `MusicGroup`, `SearchAction`, `WebSite` |
| llms.txt | HTTP `200`, `14525` bytes, sitemap mention 있음 |
| sitemap_index.xml | HTTP `200`, `913` bytes |

robots.txt 기준 주요 봇 접근은 모두 허용으로 파싱됐습니다. 이 관측은 public-only evidence이며, private/logged-in/connector 표면은 이번 비교에 사용하지 않았습니다.

## 4. Measurement Status

이번 점수는 `readiness`입니다. 직접 LLM 답변/citation/referral/conversion 측정은 아직 하지 않았습니다.

공통 브라우저 성능 관측:

| viewport | wall | responseStart | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| desktop | `5509ms` | `3018ms` | `4178ms` | `5506ms` | `87` | `2117920` | `153738` |
| mobile | `4892ms` | `2416ms` | `3649ms` | `4890ms` | `89` | `2218311` | `220029` |

시각 증거:

- `not-versioned/haegyung-desktop.png`
- `not-versioned/haegyung-mobile.png`

PageSpeed Insights는 mobile/desktop 모두 HTTP `429 quota exceeded`로 Core Web Vitals를 확보하지 못했습니다.

## 5. Commerce And Action Status

이번 사이트 비교에서는 커머스/action conversion을 주장하지 않습니다. 다만 `beta`는 commerce 관련 reference와 worksheet를 보유하므로 향후 product/schema, merchant/catalog, checkout/action claim을 분리해 보고할 수 있습니다.

## 6. Regional And Situational Context

한국어 사이트이며 `regional_context=named language: ko-KR`로 분류합니다. `beta`는 regional/situational routing reference를 포함하므로 지역/언어/vertical claim을 명시적으로 분리할 수 있습니다.

## 7. Policy Risk Gate

`beta`의 policy risk는 `pass`입니다. 이유는 crawler별 경계, private/public evidence 분리, policy-risk gate reference가 보고서 계약에 연결되어 있기 때문입니다.

## 8. Prioritized Remediation Plan

| 우선순위 | 항목 | 이유 |
| --- | --- | --- |
| 즉시 | `beta@2d896ac`를 기준으로 GEO 리포트 생성 | report contract가 있어 한국어 보고서/증거/미측정 항목 분리가 가능함 |
| 즉시 | PageSpeed 대체 측정 또는 quota 회복 후 재측정 | CWV 공식값이 없으므로 성능 판단의 공식 근거가 비어 있음 |
| 단기 | 대표 surface 정렬 이슈 분리 분석 | `해경` title과 `뮤직아카이브` site_name, `MusicGroup` schema가 섞여 있음 |
| 단기 | full-page height 리스크 분석 | desktop `153738`, mobile `220029` scrollHeight는 성능/스캔 효율 리스크임 |

## 9. Remaining Gaps And Next Verification

`beta`는 branch readiness 기준으로는 pass입니다. 남은 갭은 브랜치 기능이 아니라 라이브 사이트의 공식 성능 측정 부재와 대표 surface/entity 정렬 문제입니다.
