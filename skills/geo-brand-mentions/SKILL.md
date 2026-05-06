---
name: geo-brand-mentions
description: >
  브랜드 언급 평가. 외부 사이트·언론·커뮤니티·AI 플랫폼에서 브랜드가
  얼마나 자주, 얼마나 권위 있는 곳에서 언급되는지 진단한다.
  AI 모델은 외부 언급을 학습 데이터로 사용하므로, 자사 사이트 최적화와 별개로
  브랜드 인지도가 AI 응답에 직접 영향을 미친다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "브랜드 언급", "브랜드 인지도", "AI 브랜드", "brand mentions", "/geo brand".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-brand-mentions — 브랜드 언급 평가

> 실행 시 USER_LEVEL을 확인한다. 설정되지 않은 경우 레벨 선택을 먼저 요청한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-브랜드언급-분석.md`로 저장한다.

---

## 핵심 전제

AI 모델은 자사 사이트만 학습하지 않는다.
외부 사이트에서의 브랜드 언급이 학습 데이터에 포함되며,
이것이 AI가 해당 브랜드를 "아는지" 여부를 결정한다.
자사 사이트의 robots.txt를 아무리 최적화해도
외부 언급이 없으면 AI 브랜드 인지도는 낮을 수 있다.

---

## 실행 단계

### 1단계: 브랜드 기본 정보 수집

분석 대상 브랜드명과 주요 키워드를 확인한다.

- 브랜드명 (한국어·영문)
- 대표 제품·서비스명
- 핵심 인물 (CEO, 창업자 등)
- 업종·카테고리 키워드

---

### 2단계: 외부 언급 현황 조사

WebFetch로 아래 채널의 언급 현황을 확인한다.

#### 2-1. 백과사전·위키

- Wikipedia (영문): `https://en.wikipedia.org/wiki/[브랜드명]`
- 나무위키 (한국어): `https://namu.wiki/w/[브랜드명]`
- 항목 존재 여부, 내용 분량, 마지막 수정일 확인

#### 2-2. 언론·미디어

WebFetch로 아래 사이트에서 브랜드명 검색 결과를 확인한다.

| 채널 유형 | 확인 방법 |
|---|---|
| 종합 언론사 | 브랜드명 포함 기사 존재 여부 |
| 업종 전문 미디어 | 해당 분야 전문지·블로그 언급 |
| 해외 미디어 | 영문 언론사 언급 여부 |

#### 2-3. AI 플랫폼 직접 노출 확인

자동화 불가 영역이다. 아래 질문을 각 플랫폼에서 직접 테스트하도록 사용자에게 안내한다.

**테스트 질문 예시:**
- "[브랜드명]이 뭐야?"
- "[업종] 분야에서 [브랜드명] 어때?"
- "[브랜드명] 장단점 알려줘"

**테스트 대상 플랫폼:**

| 플랫폼 | 특성 |
|---|---|
| ChatGPT (GPT-4o) | 학습 기반 응답, 지식 컷오프 있음 |
| Perplexity AI | 실시간 검색 기반, 출처 표시 |
| Google Gemini | Google 인덱스 + 학습 혼합 |
| Claude | 학습 기반, 최신 정보 제한 |
| Grok | X(Twitter) 데이터 포함 |

**판정 기준:**

| 결과 | 의미 |
|---|---|
| 브랜드명·설명·특징 정확히 답변 | AI 인지도 높음 |
| 브랜드명은 알지만 정보 부정확 | AI 인지도 보통, 정보 개선 필요 |
| "모르겠다" 또는 다른 브랜드와 혼동 | AI 인지도 낮음 |
| 전혀 모름 | AI 인지도 없음 |

#### 2-4. 소셜·커뮤니티

- X(Twitter): 브랜드명 언급 빈도 및 맥락
- LinkedIn: 브랜드 공식 페이지, 직원 언급
- 업종 커뮤니티·포럼: 관련 토론 존재 여부
- YouTube: 브랜드 관련 영상 수

---

### 3단계: 브랜드 언급 4개 차원 평가

각 차원을 0–25점으로 평가한다. 합산 점수(0–100)가 브랜드 언급 점수다.

#### 언론·미디어 권위성 — 0~25점

| 신호 | 확인 항목 |
|---|---|
| 종합 언론사 기사 | 주요 언론사 3곳 이상 기사 존재 여부 |
| 전문 미디어 언급 | 업종 전문지·블로그 5곳 이상 언급 |
| 해외 미디어 언급 | 영문 언론 언급 여부 |
| 기사 최신성 | 6개월 이내 언급 존재 여부 |
| 백과사전 항목 | Wikipedia 또는 나무위키 항목 존재 여부 |

#### AI 플랫폼 직접 인지도 — 0~25점

| 신호 | 확인 항목 |
|---|---|
| ChatGPT 인지 | 브랜드명 질문 시 정확한 응답 여부 |
| Perplexity 인지 | 검색 결과에 브랜드 포함 여부 |
| Gemini 인지 | 브랜드 관련 정보 제공 여부 |
| 응답 정확도 | 설명이 실제와 일치하는지 여부 |
| 출처 표시 | Perplexity 등에서 자사 사이트 출처 인용 여부 |

#### 커뮤니티·소셜 존재감 — 0~25점

| 신호 | 확인 항목 |
|---|---|
| 소셜 계정 활성도 | 공식 SNS 계정 존재 및 최근 활동 여부 |
| 사용자 자발적 언급 | 브랜드명 자연 언급 빈도 |
| 커뮤니티 토론 | 업종 포럼·커뮤니티 내 브랜드 논의 |
| 리뷰·평가 | G2, 카카오맵, 네이버 플레이스 등 외부 리뷰 |
| 유튜브 콘텐츠 | 제3자 제작 브랜드 관련 영상 |

#### 브랜드 정체성 명확성 — 0~25점

AI가 브랜드를 혼동 없이 식별할 수 있는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 브랜드명 유일성 | 동일·유사 이름의 다른 브랜드와 혼동 가능성 |
| Organization 스키마 | 자사 사이트에 sameAs 속성 포함 여부 |
| 공식 채널 연결 | 사이트·SNS·위키 간 상호 링크 |
| 일관된 브랜드 서술 | 채널마다 동일한 브랜드 설명 사용 여부 |
| 핵심 인물 연결 | 창업자·대표의 공개 프로필과 브랜드 연결 |

---

### 4단계: 브랜드 언급 점수 산출

```
브랜드 언급 점수 = (언론미디어권위성 × 0.35) +
                  (AI플랫폼인지도 × 0.30) +
                  (커뮤니티소셜 × 0.20) +
                  (브랜드정체성 × 0.15)
```

언론·미디어 권위성과 AI 플랫폼 직접 인지도가 가장 큰 영향을 미친다.

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | AI가 브랜드를 잘 인식, 외부 언급 풍부 |
| 60–79 | 양호 | 기본 인지도 갖춤, 언급 확대 여지 있음 |
| 40–59 | 보통 | 주요 채널 언급 부족 |
| 20–39 | 미흡 | AI 인지도 낮음, 적극적 개선 필요 |
| 0–19 | 위험 | AI가 브랜드를 모르거나 혼동함 |

---

### 5단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-브랜드언급-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

"AI가 우리 브랜드를 얼마나 알고 있는가"를 중심으로 전달한다.
외부 언급의 중요성을 비즈니스 언어로 설명하고,
마케팅팀이 직접 실행할 수 있는 PR·콘텐츠 조치를 안내한다.

```markdown
# [브랜드명] AI 브랜드 인지도 분석

분석일: [날짜]  |  브랜드: [브랜드명]

---

## AI 브랜드 인지도: [높음 / 보통 / 낮음 / 매우 낮음]

[한 줄 요약]
예) "주요 AI 서비스에서 이 브랜드를 잘 모르거나 정보가 부정확한 상태입니다."

---

## AI 서비스별 브랜드 인식 현황

| AI 서비스 | 인식 수준 | 내용 |
|---|---|---|
| ChatGPT | 잘 앎 / 부정확 / 모름 | [한 줄] |
| Perplexity | 잘 앎 / 부정확 / 모름 | [한 줄] |
| Gemini | 잘 앎 / 부정확 / 모름 | [한 줄] |
| Grok | 잘 앎 / 부정확 / 모름 | [한 줄] |

> 위 결과는 직접 테스트가 필요합니다. 각 서비스에서 "[브랜드명]이 뭐야?"를 질문해 확인하세요.

---

## 외부 언급 현황

| 채널 | 현황 | 설명 |
|---|---|---|
| 언론·뉴스 기사 | 풍부 / 부족 / 없음 | [한 줄] |
| 전문 미디어·블로그 | 풍부 / 부족 / 없음 | [한 줄] |
| Wikipedia / 나무위키 | 있음 / 없음 | [한 줄] |
| 소셜·커뮤니티 | 활발 / 보통 / 미흡 | [한 줄] |

---

## 지금 할 수 있는 것 (마케팅팀)

1. **[조치 제목]**
   왜 중요한가: [이유 1–2문장]
   어떻게: [구체적인 방법, 예: 보도자료 배포, 게스트 기고 등]

2. **[조치 제목]**
   왜 중요한가: [이유]
   어떻게: [방법]

---

## AI 브랜드 인지도 높이는 방법 (참고)

AI는 외부 언급을 학습합니다. 자사 사이트 최적화와 함께 아래를 병행하면 효과적입니다.
- 언론·전문 미디어에 브랜드 기사·인터뷰 게재
- 업종 커뮤니티에서 전문가로 활동 (기고, 토론 참여)
- Wikipedia 항목 생성 (중립적 관점, 출처 기반)
- 소셜 채널에서 일관된 브랜드 메시지 유지
```

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 Organization 스키마, sameAs 속성 추가 방법을 안내한다.
CMS에서 직접 처리할 수 있는 기술 조치와 콘텐츠 팀에 요청할 사항을 분리한다.

```markdown
# [브랜드명] 브랜드 언급 분석

분석일: [날짜]  |  브랜드: [브랜드명]  |  대상 URL: [URL]

---

## 브랜드 언급 점수: [점수]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| 언론·미디어 권위성 | [X]/25 | [발견 사항 한 줄] |
| AI 플랫폼 인지도 | [X]/25 | [발견 사항 한 줄] |
| 커뮤니티·소셜 존재감 | [X]/25 | [발견 사항 한 줄] |
| 브랜드 정체성 명확성 | [X]/25 | [발견 사항 한 줄] |

---

## AI 플랫폼 직접 테스트 결과

> 아래는 수동 테스트가 필요합니다. 각 AI 서비스에서 "[브랜드명]이 뭐야?"를 직접 질문하세요.

| AI 서비스 | 인식 수준 | 정확도 |
|---|---|---|
| ChatGPT | [테스트 결과] | [정확 / 부정확 / 미확인] |
| Perplexity | [테스트 결과] | [정확 / 부정확 / 미확인] |
| Gemini | [테스트 결과] | [정확 / 부정확 / 미확인] |
| Grok | [테스트 결과] | [정확 / 부정확 / 미확인] |

---

## 즉시 처리 — Organization 스키마 추가

**사이트에 브랜드 정체성 스키마 추가**
- 현재 상태: [Organization 스키마 존재 / 없음]
- 수정 방법 (WordPress 기준):
  1. 관리자 → 외모 → 테마 파일 편집기 → header.php
  2. `<head>` 태그 안에 아래 스키마 추가
  3. 저장 후 [Google Rich Results Test](https://search.google.com/test/rich-results)에서 확인
- 다른 CMS: `<head>` 태그에 직접 삽입 또는 플러그인 활용
- 예상 효과: AI가 브랜드 정체성을 구조화된 데이터로 인식

---

## 콘텐츠팀 / 마케팅팀 요청 사항

| 작업 | 이유 | 우선순위 |
|---|---|---|
| [작업] | [이유 한 줄] | 높음 / 보통 |
| [작업] | [이유 한 줄] | 높음 / 보통 |
```

---

### L3 출력 — 개발자

전체 기술 명세, Organization·Person 스키마 코드, sameAs 구성을 포함한다.

```markdown
# [브랜드명] Brand Mention Analysis

Date: [날짜]  |  Brand: [브랜드명]  |  URL: [URL]

---

## Brand Mention Score: [점수]/100

| Dimension | Score | Key Findings | Missing |
|---|---|---|---|
| Press & Media Authority | [X]/25 | [발견 목록] | [누락 항목] |
| AI Platform Recognition | [X]/25 | [발견 목록] | [누락 항목] |
| Community & Social | [X]/25 | [발견 목록] | [누락 항목] |
| Brand Identity Clarity | [X]/25 | [발견 목록] | [누락 항목] |

---

## AI Platform Test Results

| Platform | Response Quality | Accuracy | Notes |
|---|---|---|---|
| ChatGPT | High / Medium / Low / None | Accurate / Inaccurate | [메모] |
| Perplexity | High / Medium / Low / None | Accurate / Inaccurate | [메모] |
| Gemini | High / Medium / Low / None | Accurate / Inaccurate | [메모] |
| Grok | High / Medium / Low / None | Accurate / Inaccurate | [메모] |

---

## Critical Gaps

### [CRITICAL] Organization Schema Missing
현재: Organization 스키마 없음
영향: AI가 브랜드 정체성을 구조화된 데이터로 인식하지 못함
해결:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "[브랜드명]",
    "url": "https://[도메인]",
    "logo": "https://[도메인]/logo.png",
    "description": "[브랜드 한 줄 설명]",
    "foundingDate": "[설립연도]",
    "sameAs": [
      "https://www.linkedin.com/company/[슬러그]",
      "https://twitter.com/[계정]",
      "https://www.youtube.com/@[채널]",
      "https://ko.wikipedia.org/wiki/[항목명]"
    ],
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "customer service",
      "email": "[이메일]"
    }
  }
  ```

### [CRITICAL] Person Schema Missing (핵심 인물)
현재: 대표자·창업자 Person 스키마 없음
영향: AI가 브랜드와 핵심 인물을 연결하지 못함
해결:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "[이름]",
    "jobTitle": "[직함]",
    "worksFor": {
      "@type": "Organization",
      "name": "[브랜드명]"
    },
    "sameAs": [
      "https://www.linkedin.com/in/[프로필]",
      "https://twitter.com/[계정]"
    ]
  }
  ```

### [WARNING] Wikipedia 항목 없음
현재: Wikipedia · 나무위키 항목 없음
영향: AI 학습 데이터에서 브랜드 권위성 신호 약함
권고: 중립적 관점·출처 기반으로 항목 생성. 직접 작성 시 중립성 위반 주의.

---

## 구현 우선순위

| 우선순위 | 작업 | 난이도 | 예상 브랜드 효과 | 담당 |
|---|---|---|---|---|
| 1 | Organization 스키마 추가 | 낮음 | 높음 | FE |
| 2 | sameAs 채널 연결 정비 | 낮음 | 높음 | FE / 마케팅 |
| 3 | Person 스키마 추가 | 낮음 | 보통 | FE |
| 4 | Wikipedia 항목 생성 | 보통 | 높음 | 마케팅 |
| 5 | 언론 기고·보도자료 배포 | 높음 | 높음 | 마케팅 |
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
