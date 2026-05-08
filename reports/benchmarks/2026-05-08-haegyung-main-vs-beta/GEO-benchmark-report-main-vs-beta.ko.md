# GEO 벤치마크 리포트: main vs beta

## 1. 리포트 개요

| 항목 | 내용 |
| --- | --- |
| 리포트 ID | `geo-benchmark-main-vs-beta-20260508` |
| 작성일 | `2026-05-08` |
| 대상 사이트 | `https://haegyung.com` |
| 기준 브랜치 | `main@a652637` |
| 비교 브랜치 | `beta@2d896ac` |
| 비교 목적 | GEO 스킬 패키지가 사이트 진단과 리포트 산출을 얼마나 안정적으로 수행할 수 있는지 비교 |
| 측정 유형 | branch readiness, all-function readiness, local validator runtime, live browser probe |
| 핵심 근거 | `data/comparison.json`, `data/browser-performance.json`, `all-function-benchmarks/benchmark-index.json` |

## 2. Executive Summary

이번 벤치마크의 결론은 명확하다. `beta`는 `main`보다 GEO 진단 리포트를 만들 준비도가 훨씬 높다.

다만 이 결과는 “`beta`가 사이트 자체를 빠르게 만든다”는 의미가 아니다. `main`과 `beta`는 `haegyung.com`을 진단하는 GEO 스킬 패키지의 두 표면이고, 라이브 사이트 성능 수치는 두 브랜치에 공통으로 적용된다.

요약하면 다음과 같다.

| 비교 축 | main | beta | 판정 |
| --- | ---: | ---: | --- |
| Branch diagnostic readiness | `10/100` | `100/100` | beta 우세 |
| 전체 GEO 기능 readiness 평균 | `39.2/100` | `100.0/100` | beta 우세 |
| reference 수 | `7` | `17` | beta 우세 |
| local validator runtime | `49.6ms` | `87.9ms` | main이 더 빠름 |
| clean snapshot validator | PASS | PASS | 동률 |

`main`은 더 빠르게 validator를 통과하지만, 검증 범위가 좁다. `beta`는 validator 시간이 약 `38.3ms` 더 걸리지만, 측정 경계, 리포트 계약, 플랫폼 truth, private/public evidence, regional/commerce/policy 경계까지 포함한다.

## 3. 점수 체계

이번 점수는 실제 AI 검색 노출 성과 점수가 아니다. 정확한 의미는 다음과 같다.

> GEO 스킬 패키지가 `haegyung.com` 진단을 근거 있는 리포트로 닫을 준비가 되어 있는가?

기능별 점수 산식은 아래와 같다.

```text
기능별 readiness = 통과한 기준 수 / 해당 기능에 배정된 기준 수 * 100
```

주요 평가 기준은 다음 항목들이다.

| 기준 | 의미 |
| --- | --- |
| `skill_exists` | 해당 GEO 서브스킬이 존재하는가 |
| `validator_pass` | 패키지 validator가 통과하는가 |
| `audit_six_domains` | 감사 영역이 crawler, citability, content, technical, schema, platform 6개로 정렬되는가 |
| `audit_measurement_boundary` | readiness, heuristic, observed answer/citation, referral, conversion을 분리하는가 |
| `audit_report_contract` | report metadata와 evidence label 계약을 강제하는가 |
| `crawler_search_user_split` | search crawler, training crawler, user-triggered fetch를 구분하는가 |
| `google_extended_correct_boundary` | Google-Extended를 검색 크롤러로 오판하지 않는가 |
| `grok_uncertainty_marked` | Grok 계열처럼 근거가 불확실한 항목을 확인 과제로 남기는가 |
| `stale_anthropic_ai_removed` | 오래된 Anthropic crawler taxonomy를 제거하거나 보정했는가 |
| `policy_private_boundaries` | public/private evidence와 policy risk를 분리하는가 |
| `regional_commerce_boundaries` | 지역/언어/commerce/action readiness를 분리하는가 |
| `validator_checks_subskill_references` | validator가 서브스킬 reference 연결까지 확인하는가 |

## 4. Branch Readiness Benchmark

| surface | rev | validator | validator time | references | readiness |
| --- | --- | --- | ---: | ---: | ---: |
| `main-clean-baseline` | `a652637` | PASS | `49.6ms` | `7` | `10/100` |
| `beta` | `2d896ac` | PASS | `87.9ms` | `17` | `100/100` |

### 해석

`main`은 기본 패키지 일관성은 통과한다. 그러나 최신 GEO 리포트에서 필요한 측정/정책/플랫폼/리포트 계약이 부족하다.

`beta`는 다음 보강을 포함한다.

- `measurement-loop.md`
- `measurement-capture-template.md`
- `report-template-contract.md`
- `platform-truth-registry.md`
- `policy-risk-gate.md`
- `private-surface-routing.md`
- `regional-situational-routing.md`
- `commerce-readiness.md`
- `commerce-audit-worksheet.md`
- `implementation-completion-plan.md`

따라서 `beta`는 “분석 결과를 주장하는 방식”까지 관리한다. 이 점이 `main`과의 핵심 차이다.

## 5. 전체 GEO 기능 벤치마크

총 14개 GEO 서브스킬을 비교했다.

| skill | main | beta | delta |
| --- | ---: | ---: | ---: |
| `geo-audit` | `28.6` | `100.0` | `+71.4` |
| `geo-brand-mentions` | `40.0` | `100.0` | `+60.0` |
| `geo-citability` | `50.0` | `100.0` | `+50.0` |
| `geo-compare` | `40.0` | `100.0` | `+60.0` |
| `geo-content` | `50.0` | `100.0` | `+50.0` |
| `geo-crawlers` | `28.6` | `100.0` | `+71.4` |
| `geo-llmstxt` | `50.0` | `100.0` | `+50.0` |
| `geo-platform-optimizer` | `25.0` | `100.0` | `+75.0` |
| `geo-proposal` | `33.3` | `100.0` | `+66.7` |
| `geo-prospect` | `40.0` | `100.0` | `+60.0` |
| `geo-report` | `33.3` | `100.0` | `+66.7` |
| `geo-report-pdf` | `50.0` | `100.0` | `+50.0` |
| `geo-schema` | `40.0` | `100.0` | `+60.0` |
| `geo-technical` | `40.0` | `100.0` | `+60.0` |

### 기능별 주요 판정

가장 큰 개선은 `geo-platform-optimizer`다. `main`은 플랫폼별 crawler/search/user-triggered fetch, Google-Extended, Grok uncertainty, private/policy/regional 경계를 충분히 나누지 못한다. `beta`는 이 경계를 reference와 validator 기준으로 고정한다.

다음으로 개선폭이 큰 기능은 `geo-audit`와 `geo-crawlers`다. `beta`는 6개 감사 도메인과 최신 crawler taxonomy를 기준으로 리포트를 닫을 수 있다.

`geo-report`, `geo-proposal`, `geo-report-pdf`도 크게 개선됐다. 이유는 리포트가 단순 요약문이 아니라 `score_type`, `evidence_label`, `confidence`, `measurement_status`, `policy_risk`를 갖춘 evidence-bearing artifact로 바뀌었기 때문이다.

## 6. 라이브 사이트 성능 측정

대상 URL은 `https://haegyung.com`이고 최종 URL은 `https://www.haegyung.com/`이다.

| 항목 | 값 |
| --- | --- |
| 캡처 시각 | `2026-05-07T21:01:17Z` |
| homepage HTTP | `200` |
| median response | `2558.5ms` |
| HTML bytes | `700038` |
| lang | `ko-KR` |
| H1 / H2 | `5` / `166` |
| JSON-LD types | `CollectionPage`, `ImageObject`, `MusicGroup`, `SearchAction`, `WebSite` |
| llms.txt | HTTP `200`, `14525` bytes |
| sitemap_index.xml | HTTP `200` |

브라우저 probe 결과는 다음과 같다.

| viewport | wall | responseStart | responseEnd | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| desktop | `5509ms` | `3018ms` | `3338ms` | `4178ms` | `5506ms` | `87` | `2117920` | `153738` |
| mobile | `4892ms` | `2416ms` | `2731ms` | `3649ms` | `4890ms` | `89` | `2218311` | `220029` |

### 라이브 사이트 성능 해석

사이트는 정상 렌더링된다. 그러나 full-page 높이가 desktop `153738`, mobile `220029`로 매우 크다. 이는 사람의 스캔 비용과 AI crawler의 대표 surface 파악 비용을 모두 높인다.

`loadEnd`는 desktop `5506ms`, mobile `4890ms`다. HTML 크기 `700038` bytes, decoded resource bytes 약 `2.1~2.2MB`를 고려하면, 홈페이지 범위 축소와 대표 surface 정리가 우선 과제다.

PageSpeed Insights API는 HTTP `429 quota exceeded`로 실패했기 때문에 Core Web Vitals 공식값은 이 리포트에서 주장하지 않는다.

## 7. 핵심 리스크

### 7.1 main의 리스크

`main`은 기본 validator는 통과하지만, 최신 GEO 리포트에서 필요한 claim boundary가 부족하다. 특히 다음 항목이 약하다.

- readiness와 observed evidence 분리
- 플랫폼별 crawler truth 분리
- public/private evidence 분리
- policy risk gate
- regional/commerce/action readiness 분리
- report metadata 계약

따라서 `main`은 단순 baseline으로는 충분하지만, 실제 납품 가능한 벤치마크 리포트 표면으로는 부족하다.

### 7.2 beta의 리스크

`beta`는 readiness 기준으로 강하다. 그러나 실제 AI 플랫폼 성과가 검증된 것은 아니다.

아직 없는 증거:

- ChatGPT Search observed answer
- Perplexity observed citation
- Gemini/AI Overviews observed inclusion
- referral log
- conversion signal
- Core Web Vitals official PSI 결과

따라서 `beta`의 `100/100`은 “측정 가능하게 리포트를 만들 준비가 됐다”는 뜻이지, “AI 검색 성과가 100점”이라는 뜻이 아니다.

### 7.3 haegyung.com의 리스크

사이트 자체에서는 다음 리스크가 보인다.

- title은 `해경`, og:site_name은 `뮤직아카이브`, schema는 `MusicGroup` 중심이라 대표 entity가 분산됨
- H2가 `166`개로 root page의 정보 범위가 과도하게 넓음
- full-page scrollHeight가 매우 커서 스캔 효율이 낮음
- OG image와 Twitter image가 비어 있어 공유/인용 preview 신호가 약함

## 8. 결론

이번 벤치마크의 결론은 다음과 같다.

1. GEO 스킬 패키지의 진단/리포트 표면으로는 `beta`를 기준으로 삼는 것이 맞다.
2. `main`은 빠르지만 검사 범위가 좁고, 최신 GEO claim boundary를 충분히 표현하지 못한다.
3. `beta`는 validator runtime이 조금 늘었지만, 리포트 품질과 측정 가능성이 크게 개선됐다.
4. 라이브 사이트 성능 리스크는 브랜치 차이가 아니라 `haegyung.com` 자체의 구조 문제다.
5. 다음 단계는 readiness 비교가 아니라 observed platform benchmark다.

## 9. 다음 측정 제안

다음 단계에서는 아래 순서로 실제 관측 벤치마크를 진행하는 것이 좋다.

1. ChatGPT Search, Perplexity, Gemini/AI Overviews용 prompt panel 정의
2. observed answer inclusion 캡처
3. observed citation 캡처
4. referral log 또는 analytics 신호 확인
5. Core Web Vitals 공식 측정 재시도
6. homepage 대표 surface 축소 후 before/after 비교

## 10. 산출물 인벤토리

| 산출물 | 역할 |
| --- | --- |
| `data/comparison.json` | branch readiness와 라이브 사이트 HTTP/head/structure 스냅샷 |
| `data/browser-performance.json` | 브라우저 성능 probe 지표 |
| `all-function-benchmarks/benchmark-index.json` | 14개 GEO 기능별 benchmark index |
| `all-function-benchmarks/GEO-all-functions-benchmark-comparison.md` | 전체 기능 비교 리포트 |
| `per-target-reports/*.md` | branch comparison과 대상별 GEO 종합 리포트 |
| `GEO-benchmark-report-main-vs-beta.ko.md` | 본 리포트 |
