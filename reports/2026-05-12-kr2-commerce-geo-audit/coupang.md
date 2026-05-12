# Coupang GEO-SEO 개별 감사 보고서

대상: https://www.coupang.com/
분석일: 2026-05-12 KST
상태: 미흡
GEO 점수: 22 / 100

## 1. 측정된 사실

| 항목 | 결과 |
|---|---|
| Homepage HEAD | HTTP/2 403 |
| Edge/WAF | AkamaiGHost |
| Homepage body | `Access Denied` |
| `/robots.txt` | Access Denied HTML 반환 |
| `/llms.txt` | HTTP/2 403 |
| 콘텐츠/메타 태그 측정 | 차단으로 미측정 |

## 2. 해석

쿠팡은 일반 사용자 브라우저에서는 접근 가능할 수 있지만, 이번 비로그인 자동화 감사 요청에는 홈페이지와 robots/llms 표면이 모두 차단됐다. GEO 관점에서는 “AI 검색 시스템이 공개 대표 페이지와 크롤링 정책을 안정적으로 읽을 수 있는가”가 핵심인데, 현재 관측값은 가장 큰 리스크가 접근성임을 보여준다.

robots.txt 자체가 HTML Access Denied로 반환되면 crawler 정책을 정상적으로 해석하기 어렵다. Google 문서 기준으로 robots.txt는 호스트 최상위의 텍스트 규칙이어야 하며, AI crawler도 각 provider가 문서화한 user-agent별 정책을 robots.txt 또는 접근 정책으로 확인한다.

## 3. 영역별 점수

| 영역 | 점수 | 근거 |
|---|---:|---|
| AI 크롤러 접근 | 5 | homepage, robots.txt, llms.txt 모두 403/Access Denied |
| AI 인용 가능성 | 15 | 대표 페이지 본문을 확인할 수 없어 직접 인용 가능성 낮음 |
| 콘텐츠 품질 | 40 | 콘텐츠 자체는 미측정. 브랜드 규모 때문에 기본값은 주되 검증 불가 패널티 적용 |
| 기술 SEO | 25 | HTTPS는 응답하지만 crawler 정책 표면이 차단됨 |
| 스키마 | 20 | HTML 접근 차단으로 Organization/Product schema 확인 불가 |
| 플랫폼 최적화 | 20 | AI 플랫폼별 접근 정책 확인 불가 |

## 4. 우선 조치

| 심각도 | 조치 | 담당 |
|---|---|---|
| CRITICAL | `/robots.txt`는 Akamai 차단 없이 plain text로 반환되게 분리 | 인프라/보안 |
| CRITICAL | 대표 homepage와 주요 카테고리 landing page에 대해 검색/AI crawler allowlist 정책 수립 | 인프라/SEO |
| HIGH | `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Googlebot`, `Yeti` 접근 정책을 명시 | SEO/인프라 |
| HIGH | `/llms.txt` 제공 여부 결정. 제공한다면 핵심 카테고리, 정책, 브랜드 설명, sitemap 경로를 명시 | SEO/콘텐츠 |
| MEDIUM | 차단 해제 후 Organization/WebSite/Product/Breadcrumb schema 재감사 | 개발/SEO |

## 5. 재감사 조건

- `https://www.coupang.com/robots.txt`가 200 text/plain 또는 유효한 robots text로 응답
- homepage가 비로그인 검색/AI crawler 정책상 허용되는 방식으로 200 또는 의도된 canonical redirect 반환
- `/llms.txt`가 200 또는 명시적 404 정책으로 확정
