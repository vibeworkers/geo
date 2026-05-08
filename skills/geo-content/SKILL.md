---
name: geo-content
description: >
  콘텐츠 품질 및 E-E-A-T(경험·전문성·권위성·신뢰성) 평가.
  페이지 콘텐츠를 분석하여 구글과 AI 검색 엔진이 신뢰할 수 있는 수준인지 진단한다.
  단어 수, 가독성, 저자 신뢰도, 콘텐츠 신선도, AI 생성 여부 지표를 함께 평가한다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "콘텐츠 품질", "E-E-A-T", "신뢰도", "저자", "content".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-content — 콘텐츠 품질 · E-E-A-T 평가

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정하고 그 레벨에 맞춰 출력한다.
> 결과는 선택한 수신자 레벨에 맞는 출력 템플릿으로 전달하고 `GEO-콘텐츠-분석.md`로 저장한다.

---

## 콘텐츠 claim 경계

콘텐츠 품질과 E-E-A-T 점수는 readiness/heuristic 신호다. brand superiority,
regulated claims, medical/legal/finance advice, privacy-sensitive claims는
`../../references/policy-risk-gate.md`로 확인한다. 실제 AI answer inclusion
이나 observed_citation은 `../../references/measurement-capture-template.md`
로 캡처해야 한다.

## 실행 단계

### 1단계: 페이지 콘텐츠 추출

WebFetch로 대상 URL을 로드하고 다음을 추출한다.

- 본문 전체 텍스트 (내비게이션·푸터 제외)
- 제목 구조 (H1, H2, H3 목록)
- 단락·목록·표 개수
- 이미지 수 및 alt 텍스트 유무
- 저자 바이라인 유무 및 저자명
- 작성일·수정일 표시 유무
- 내부 링크 수, 외부 링크 수

---

### 2단계: E-E-A-T 4개 차원 평가

각 차원을 0–25점으로 평가한다. 합산 점수(0–100)가 E-E-A-T 종합 점수다.

#### 경험 (Experience) — 0~25점

직접 경험한 내용인지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 직접 경험 서술 | "제가 실제로 써보니…", 사용 후기, 과정 설명 |
| 원본 데이터 | 자체 조사·실험·측정 결과 포함 여부 |
| 사례 연구 | 구체적 수치·기간·결과가 있는 사례 |
| 전후 비교 | 실제 개선 결과 수치 제시 |
| 구체적 세부 정보 | 날짜·이름·장소·금액 등 구체적 수치 |

#### 전문성 (Expertise) — 0~25점

콘텐츠 작성자의 지식 깊이를 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 저자 바이라인 | 이름이 명시되어 있는가 |
| 저자 프로필 | 자격·경력·전문 분야 안내 링크 |
| 기술 깊이 | 표면적 설명을 넘어 원리·맥락·예외 사항 다룸 |
| 전문 용어 활용 | 해당 분야 용어를 정확하게 사용 |
| 출처 인용 | 외부 권위 자료 링크 또는 각주 |

#### 권위성 (Authoritativeness) — 0~25점

사이트와 저자의 분야 내 평판을 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 어바웃 페이지 | 회사·팀·역사를 충실히 소개하는 페이지 |
| 외부 인용 | 타 사이트에서 이 콘텐츠를 인용·링크하는지 |
| 수상·인증 | 업계 인증서, 수상 내역 |
| 미디어 언급 | 언론사·전문 매체 노출 여부 |
| 콘텐츠 포괄성 | 해당 주제를 여러 페이지에서 깊이 다루는지 |

#### 신뢰성 (Trustworthiness) — 0~25점

가장 중요한 차원이다. 의심스러운 신호는 점수를 크게 깎는다.

| 신호 | 확인 항목 |
|---|---|
| HTTPS | 사이트가 HTTPS로 제공되는가 |
| 연락처 정보 | 이메일·전화번호·주소 중 하나 이상 |
| 개인정보 처리방침 | 접근 가능한 페이지로 연결되는가 |
| 작성일·수정일 | 날짜가 명시되어 있는가 |
| 주장 근거 | 수치·통계에 출처가 있는가 |
| 광고·제휴 고지 | 스폰서·제휴 링크 명시 여부 |

---

### 3단계: 콘텐츠 메트릭 측정

| 항목 | 기준 |
|---|---|
| 단어 수 | 300 미만: 얇음 / 300–800: 단문 / 800–1,500: 표준 / 1,500–3,000: 장문 / 3,000+: 심층 |
| 단락 평균 길이 | 40–80단어 권장. 150단어 초과 시 "긴 단락" 경고 |
| 제목 구조 | H1이 정확히 1개인가, 계층이 논리적인가 |
| 내부 링크 | 관련 콘텐츠로 연결되는 링크가 3개 이상인가 |
| 이미지 alt 텍스트 | 이미지가 있을 때 alt 속성 누락 여부 |

---

### 4단계: AI 생성 콘텐츠 지표 확인

AI 생성 콘텐츠 자체는 문제가 아니지만 E-E-A-T 신호 없이
저품질로 대량 생성된 콘텐츠는 감점 요인이다.

**주의 신호:**
- "오늘날의 디지털 환경에서", "중요한 점은" 등 범용 문구 반복
- 구체적 수치·날짜·이름 없이 일반론만 서술
- 원본 데이터·사례·저자 관점 전혀 없음
- 같은 요점을 다른 표현으로 반복
- 과도한 헤징 표현 ("~할 수도 있습니다", "경우에 따라 다릅니다")

**판정:** 높은 확률로 인간 작성 / 편집된 AI 콘텐츠 / 경량 편집 AI / 무편집 AI

---

### 5단계: 콘텐츠 점수 산출

```
콘텐츠 점수 = (E-E-A-T 합산 × 0.60) +
              (콘텐츠 메트릭 × 0.25) +
              (AI 지표 × 0.15)
```

E-E-A-T 합산 100점 → 콘텐츠 점수 반영 시 60점 기여.
콘텐츠 메트릭과 AI 지표는 각각 25·15점 기여.

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | E-E-A-T 신호 충분, AI 인용 가능성 높음 |
| 60–79 | 양호 | 기본 신뢰도 확보, 일부 보완 필요 |
| 40–59 | 보통 | 전문성·권위성 강화 필요 |
| 20–39 | 미흡 | E-E-A-T 전반 개선 필요 |
| 0–19 | 위험 | AI가 콘텐츠를 신뢰하기 어려운 수준 |

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

콘텐츠의 신뢰도를 일상 언어로 전달한다.
"구글과 AI가 이 글을 얼마나 믿는가"를 중심으로 설명한다.
기술 용어 없이, 개선 방향은 누가 무엇을 해야 하는지로 안내한다.

```markdown
# [페이지 제목] 콘텐츠 신뢰도 분석

분석일: [날짜]  |  분석 URL: [URL]

---

## 종합 신뢰도: [우수 / 양호 / 보통 / 미흡 / 위험]

[한 줄 요약]
예) "글쓴이 정보가 없어 구글과 AI가 이 글을 신뢰하기 어려운 상태입니다."

---

## 신뢰도 항목별 현황

| 확인 항목 | 현황 | 설명 |
|---|---|---|
| 글쓴이가 누구인지 알 수 있나요? | 좋음 / 주의 / 위험 | [한 줄] |
| 실제 경험을 바탕으로 쓴 글인가요? | 좋음 / 주의 / 위험 | [한 줄] |
| 사이트가 해당 분야에서 인정받나요? | 좋음 / 주의 / 위험 | [한 줄] |
| 사이트가 안전하고 투명한가요? | 좋음 / 주의 / 위험 | [한 줄] |
| 글의 양과 구성이 충분한가요? | 좋음 / 주의 / 위험 | [한 줄] |

---

## 지금 개선할 수 있는 것 (마케팅팀)

1. **[조치 제목]**
   왜 중요한가: [이유 1–2문장]
   어떻게 하면 되나요: [구체적인 방법, 기술 용어 없이]

2. **[조치 제목]**
   왜 중요한가: [이유]
   어떻게: [방법]

---

## 다른 팀에 요청할 사항

| 요청 내용 | 담당 | 이유 |
|---|---|---|
| [요청] | 개발팀 / 운영팀 | [이유 한 줄] |
```

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 CMS·FTP에서 직접 수정할 수 있는 방법을 안내한다.
WordPress 기준으로 설명하되, 다른 CMS도 유사하게 적용 가능함을 명시한다.

```markdown
# [페이지 제목] 콘텐츠 품질 분석

분석일: [날짜]  |  URL: [URL]

---

## 콘텐츠 점수: [점수]/100 — [등급]

| E-E-A-T 차원 | 점수 | 주요 발견 |
|---|---|---|
| 경험 (Experience) | [X]/25 | [발견 사항 한 줄] |
| 전문성 (Expertise) | [X]/25 | [발견 사항 한 줄] |
| 권위성 (Authoritativeness) | [X]/25 | [발견 사항 한 줄] |
| 신뢰성 (Trustworthiness) | [X]/25 | [발견 사항 한 줄] |

**콘텐츠 메트릭**
- 단어 수: [X]단어 ([평가])
- 단락 평균 길이: [X]단어 ([평가])
- 제목 구조: [평가]
- AI 콘텐츠 판정: [판정 결과]

---

## 우선순위별 수정 과제

### 즉시 처리 가능

**1. [문제 제목]**
- 현재 상태: [설명]
- 수정 방법 (WordPress 기준):
  1. 관리자 로그인 → 해당 글 편집
  2. [구체적 단계]
  3. 업데이트 저장
- 다른 CMS: [대안 안내]
- 예상 효과: [효과]

### 콘텐츠 개선 (이번 달)

**[제목]**
- 현재 상태: [설명]
- 추가/수정할 내용: [구체적 안내]
- 참고: [예시 또는 기준]

---

## AI 콘텐츠 판정 상세

**판정:** [결과]
**발견된 지표:**
- [지표 1]: [예시]
- [지표 2]: [예시]

**권고:** [콘텐츠 개선 방향]
```

---

### L3 출력 — 개발자

전체 기술 명세와 Person·Article 스키마 코드를 포함한다.

```markdown
# [페이지 제목] Content Quality / E-E-A-T Analysis

Date: [날짜]  |  URL: [URL]

---

## Content Score: [점수]/100

| Dimension | Score | Key Signals Found | Missing |
|---|---|---|---|
| Experience | [X]/25 | [신호 목록] | [누락 항목] |
| Expertise | [X]/25 | [신호 목록] | [누락 항목] |
| Authoritativeness | [X]/25 | [신호 목록] | [누락 항목] |
| Trustworthiness | [X]/25 | [신호 목록] | [누락 항목] |

**Content Metrics**
| Metric | Value | Assessment |
|---|---|---|
| Word Count | [X] | [평가] |
| Avg Paragraph Length | [X] words | [평가] |
| Heading Structure | H1:[X] H2:[X] H3:[X] | [평가] |
| Internal Links | [X] | [평가] |
| Images w/ alt | [X]/[전체] | [평가] |
| AI Content Assessment | [판정] | [근거] |

---

## Critical E-E-A-T Gaps

### [CRITICAL] Author Identity Missing
현재: 저자 바이라인 없음
영향: Google E-E-A-T 평가 불리, AI 인용 시 출처 불명확
해결:
  1. Person 스키마 추가:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "[저자명]",
    "url": "[저자 프로필 URL]",
    "sameAs": [
      "[LinkedIn URL]",
      "[Twitter URL]"
    ],
    "jobTitle": "[직함]",
    "worksFor": {
      "@type": "Organization",
      "name": "[회사명]"
    }
  }
  ```
  2. Article 스키마에 author 연결:
  ```json
  {
    "@type": "Article",
    "author": { "@type": "Person", "name": "[저자명]" },
    "datePublished": "[ISO 날짜]",
    "dateModified": "[ISO 날짜]"
  }
  ```

---

## 구현 우선순위

| 우선순위 | 작업 | 난이도 | 예상 E-E-A-T 효과 |
|---|---|---|---|
| 1 | [작업] | 낮음/보통/높음 | [효과] |
| 2 | [작업] | [난이도] | [효과] |
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
