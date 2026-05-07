---
name: geo-audit
description: >
  GEO + SEO 전체 감사. 대상 사이트를 5개 영역(AI 가시성, 플랫폼 최적화,
  기술 SEO, 콘텐츠 품질, 스키마 마크업)으로 종합 분석하고
  GEO 점수(0-100)와 우선순위별 개선 과제를 제공한다.
  모든 레벨(L1/L2/L3)에서 동일한 깊이로 분석하며 출력 방식만 달라진다.
  트리거: "전체 감사", "사이트 분석", "종합 점검", "audit".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-audit — GEO·SEO 전체 감사

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정하고 그 레벨에 맞춰 출력한다.
> 분석 결과는 선택한 수신자 레벨에 맞는 출력 템플릿으로 전달하고 `GEO-감사-보고서.md`로 저장한다.

---

## 실행 단계

### 1단계: 사이트 기본 정보 수집

WebFetch로 홈페이지를 로드하고 다음을 추출한다.

- 사이트명 — `<title>`, `og:site_name`, H1 순서로 확인
- 메인 내비게이션 링크 목록
- `/sitemap.xml` 존재 여부
- `/robots.txt` 존재 여부
- 비즈니스 유형 감지

**비즈니스 유형 감지 기준**

| 유형 | 감지 신호 |
|---|---|
| SaaS | 가격 페이지, "무료 체험", `/dashboard`, API 문서 링크 |
| 로컬 비즈니스 | 전화번호, 주소, 지도 임베드, "근처", 영업시간 |
| 이커머스 | 장바구니, 상품 목록, "구매하기", 재고 표시 |
| 미디어 / 블로그 | 바이라인, 날짜, 카테고리, 댓글 |
| 에이전시 | 포트폴리오, 사례 연구, "서비스 소개", 고객사 로고 |
| 기타 | 위 유형에 해당하지 않으면 일반 기준 적용 |

---

### 2단계: 5개 영역 순차 분석

모든 레벨에서 동일하게 실행한다. 각 영역 분석 시 해당 서브스킬의 지시를 따른다.

| 순서 | 영역 | 서브스킬 | 산출 점수 |
|---|---|---|---|
| 1 | AI 크롤러 접근 | geo-crawlers | 크롤러 점수 /100 |
| 2 | AI 인용 가능성 | geo-citability | 인용 점수 /100 |
| 3 | 콘텐츠 품질 / E-E-A-T | geo-content | 콘텐츠 점수 /100 |
| 4 | 기술 SEO | geo-technical | 기술 점수 /100 |
| 5 | 플랫폼 최적화 | geo-platform-optimizer | 플랫폼 점수 /100 |

---

### 3단계: 종합 GEO 점수 산출

```
GEO 점수 = (인용 점수 × 0.25) + (크롤러 점수 × 0.20) +
           (콘텐츠 점수 × 0.20) + (기술 점수 × 0.15) +
           (스키마 점수 × 0.10) + (플랫폼 점수 × 0.10)
```

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | AI 검색 최적화 상위 수준 |
| 60–79 | 양호 | 기본 최적화 완료, 개선 여지 있음 |
| 40–59 | 보통 | 주요 개선 과제 다수 존재 |
| 20–39 | 미흡 | 즉각적인 조치 필요 |
| 0–19 | 위험 | AI 검색에서 거의 노출되지 않음 |

---

### 4단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-감사-보고서.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

기술 용어 없이 비즈니스 언어로 작성한다.
점수 수치는 제거하고 상태 표현(좋음 / 주의 / 위험)을 사용한다.
모든 액션 아이템은 "누가 무엇을 해야 하는가" 형태로 작성한다.

```markdown
# [사이트명] AI 검색 노출 현황 보고서

분석일: [날짜]

---

## 종합 현황: [우수 / 양호 / 보통 / 미흡 / 위험]

[점수 등급에 따른 한 줄 요약]
예) "현재 사이트는 AI 검색에서 경쟁사 대비 노출이 낮은 상태입니다."

---

## 지금 당장 해야 할 일

1. **[조치 제목]** — 담당: [개발팀 / 운영팀 / 마케팅팀]
   왜 중요한가: [비즈니스 관점 1–2문장]
   요청 내용: [담당자에게 전달할 구체적 요청]

2. **[조치 제목]** — 담당: [담당]
   왜 중요한가: [이유]
   요청 내용: [요청]

3. **[조치 제목]** — 담당: [담당]
   왜 중요한가: [이유]
   요청 내용: [요청]

---

## 항목별 현황

| 확인 항목 | 현황 | 한 줄 설명 |
|---|---|---|
| AI 봇이 사이트를 볼 수 있나요? | 좋음 / 주의 / 위험 | [설명] |
| 글이 AI 검색에 인용되나요? | 좋음 / 주의 / 위험 | [설명] |
| 콘텐츠 신뢰도는 충분한가요? | 좋음 / 주의 / 위험 | [설명] |
| 브랜드가 AI에 알려져 있나요? | 좋음 / 주의 / 위험 | [설명] |
| 주요 AI 플랫폼에 노출되나요? | 좋음 / 주의 / 위험 | [설명] |

---

## 개발팀 / 운영팀 전달 요청 목록

아래 내용을 해당 담당자에게 전달해 주세요.

| 작업 내용 | 이유 | 우선순위 |
|---|---|---|
| [작업] | [이유 한 줄] | 높음 / 보통 |
| [작업] | [이유 한 줄] | 높음 / 보통 |
```

---

### L2 출력 — 웹마스터 / 운영자

점수와 상태를 함께 표시한다.
파일 경로, FTP 작업, CMS 설정 방법을 단계별로 안내한다.
수정 전후 내용을 명확히 보여준다.

```markdown
# [사이트명] GEO-SEO 감사 보고서

분석일: [날짜]  |  대상: [URL]  |  비즈니스 유형: [유형]

---

## 종합 GEO 점수: [점수]/100 — [등급]

| 영역 | 점수 | 상태 |
|---|---|---|
| AI 인용 가능성 | [X]/100 | 좋음 / 주의 / 위험 |
| AI 크롤러 접근 | [X]/100 | 좋음 / 주의 / 위험 |
| 콘텐츠 품질 | [X]/100 | 좋음 / 주의 / 위험 |
| 기술 SEO | [X]/100 | 좋음 / 주의 / 위험 |
| 플랫폼 최적화 | [X]/100 | 좋음 / 주의 / 위험 |

---

## 우선순위별 개선 과제

### 즉시 처리 (이번 주)

**1. [문제 제목]**
- 현재 상태: [현황 설명]
- 수정 방법:
  1. FTP 접속 → [경로] 이동
  2. [파일명] 열기
  3. 다음 내용으로 수정:
     ```
     [수정 전 내용]
     ```
     ↓ 변경
     ```
     [수정 후 내용]
     ```
  4. 저장 후 브라우저에서 확인
- 예상 효과: [개선 기대 효과]
- 소요 시간: [예상 시간]

### 단기 처리 (이번 달)

**[문제 제목]**
[동일 형식]

### 중장기 처리

**[문제 제목]**
[동일 형식]

---

## 영역별 상세 결과 요약

### AI 크롤러 접근
[주요 발견 사항 3–5줄]

### AI 인용 가능성
[주요 발견 사항]

### 콘텐츠 품질
[주요 발견 사항]

### 기술 SEO
[주요 발견 사항]

### 플랫폼 최적화
[주요 발견 사항]
```

---

### L3 출력 — 개발자

전체 기술 명세, 점수 breakdown, 코드 스니펫을 포함한다.
영역별 상세 분석 결과를 빠짐없이 출력한다.

```markdown
# [사이트명] GEO-SEO Audit Report

Date: [날짜]  |  URL: [URL]  |  Business Type: [유형]

---

## GEO Score: [점수]/100 — [등급]

| Category | Raw Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | [X]/100 | 25% | [X] |
| Brand Authority | [X]/100 | 20% | [X] |
| Content Quality | [X]/100 | 20% | [X] |
| Technical | [X]/100 | 15% | [X] |
| Structured Data | [X]/100 | 10% | [X] |
| Platform Opt. | [X]/100 | 10% | [X] |
| **합계** | | | **[점수]/100** |

---

## Critical Issues

### [CRITICAL] [문제 제목]
- 현재 상태: `[현재 값]`
- 영향 범위: [영향 설명]
- 해결 방법:
  ```[언어]
  [코드 또는 설정 스니펫]
  ```
- 검증 방법: [확인 명령 또는 도구]

---

## 영역별 상세 분석

### AI Crawler Access
[geo-crawlers 전체 출력]

### AI Citability
[geo-citability 전체 출력]

### Content Quality / E-E-A-T
[geo-content 전체 출력]

### Technical SEO
[geo-technical 전체 출력]

### Platform Optimization
[geo-platform-optimizer 전체 출력]

---

## 구현 우선순위 매트릭스

| 우선순위 | 작업 | 난이도 | 예상 효과 | 담당 |
|---|---|---|---|---|
| 1 | [작업] | 낮음 | 높음 | [FE/BE/DevOps] |
| 2 | [작업] | 보통 | 높음 | [담당] |
| 3 | [작업] | 낮음 | 보통 | [담당] |
```

---

## Setup

This restored execution skill is bundled inside the local `geo` execution
bundle under `skills/`.

Use it after the representative `geo` router has confirmed a direct execution
request, or invoke this subskill explicitly in a compatible agent surface that
loads nested skill directories.

## Dependencies and Permissions

This skill uses the tool boundary declared in frontmatter `allowed-tools`.

Network reads and local report writes are expected when the workflow runs.
External APIs are not required beyond the HTTP or browser-access checks already
named in the skill body.

## Source and License Notes

This restored execution surface preserves the original GEO-SEO execution
workflow inside the current repository's local execution bundle.

Repository-level reuse terms are inherited from `../../LICENSE`.
