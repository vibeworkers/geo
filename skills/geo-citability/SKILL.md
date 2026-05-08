---
name: geo-citability
description: >
  AI 인용 가능성 평가. 페이지가 ChatGPT, Perplexity, Google AI Overviews 등
  AI 검색 엔진에 인용될 가능성을 진단한다.
  직접 답변 구조, 콘텐츠 권위성, 기술 인용 신호, 브랜드 명확성 4개 차원으로 평가한다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "인용 가능성", "AI 인용", "citability".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-citability — AI 인용 가능성 평가

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정하고 그 레벨에 맞춰 출력한다.
> 결과는 선택한 수신자 레벨에 맞는 출력 템플릿으로 전달하고 `GEO-인용가능성-분석.md`로 저장한다.

---

## 인용 가능성 경계

인용 가능성 점수는 citation readiness다. 실제 citation이 발생했다는 주장은
`../../references/measurement-capture-template.md`의 observed_citation
capture가 있을 때만 사용한다. citation claim에는 evidence_label,
confidence, evidence_path, platform, access_profile을 함께 기록한다.

## 실행 단계

### 1단계: 페이지 콘텐츠 추출

WebFetch로 대상 URL을 로드하고 다음을 추출한다.

- 본문 전체 텍스트
- 제목 구조 (H1, H2, H3 목록)
- FAQ·정의·요약 단락 유무
- 통계·수치·연구 인용 유무
- 저자 바이라인 및 조직명
- JSON-LD 또는 Microdata 스키마 존재 여부
- Open Graph / Twitter Card 메타 태그
- llms.txt 존재 여부 — Bash로 직접 확인

**llms.txt 확인 방법**

> **Claude Code 환경:** 아래 Bash 스크립트 실행 (HTTP 상태 코드 정확히 확인 가능)
> **Claude 웹 환경:** WebFetch로 `[도메인]/llms.txt` 직접 로드. 404 응답 또는 내용 없으면 미존재로 판단.
> HTTP 헤더 확인이 필요한 경우 외부 도구 활용: https://httpstatus.io/

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from urllib.parse import urlparse
url = '[TARGET_URL]'
parsed = urlparse(url)
llms_url = f'{parsed.scheme}://{parsed.netloc}/llms.txt'
r = requests.get(llms_url, headers={'User-Agent':'GEO-Audit/1.0'}, timeout=15)
print(f'llms.txt STATUS: {r.status_code}')
if r.status_code == 200: print(r.text[:2000])
"
```

**Claude 웹 환경 (WebFetch 대체)**

WebFetch로 아래 URL을 로드한다.
- `https://[도메인]/llms.txt` — 내용이 반환되면 존재, 오류 페이지면 미존재로 판단

---

### 2단계: 인용 가능성 4개 차원 평가

각 차원을 0–25점으로 평가한다. 합산 점수(0–100)가 인용 점수다.

#### 직접 답변 구조 (Direct Answer Structure) — 0~25점

AI가 페이지에서 바로 답변을 추출할 수 있는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 정의 단락 | "[용어]란 ~이다" 형식의 명확한 정의 문장 |
| FAQ 섹션 | 질문-답변 형식 블록 존재 여부 |
| 요약 단락 | 글 첫머리 또는 섹션 시작에 핵심 내용 요약 |
| 단계별 안내 | 번호 목록으로 절차를 명확히 제시 |
| 명제 문장 | "~은 ~이다", "~하려면 ~해야 한다" 형태의 직접 답변 가능 문장 |

#### 콘텐츠 권위성 (Content Authority) — 0~25점

AI가 신뢰할 수 있는 출처로 인식하는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 통계·수치 출처 | 데이터에 출처 링크 또는 각주 |
| 연구·보고서 인용 | 공신력 있는 외부 자료 링크 |
| 전문가 인용 | 이름·소속이 명시된 전문가 발언 |
| 원본 데이터 | 자체 조사·설문·실험 결과 |
| 최신성 | 작성일·수정일 명시, 1년 이내 업데이트 여부 |

#### 기술 인용 신호 (Technical Citation Signals) — 0~25점

AI 크롤러가 페이지를 구조적으로 이해하도록 돕는 기술 요소를 평가한다.

| 신호 | 확인 항목 |
|---|---|
| FAQPage 스키마 | JSON-LD FAQPage 마크업 존재 여부 |
| HowTo 스키마 | 단계별 안내 콘텐츠에 HowTo 마크업 적용 여부 |
| Article 스키마 | datePublished, author, headline 포함 여부 |
| speakable 속성 | 음성 검색·AI 응답용 speakable 지정 여부 |
| llms.txt | 사이트 루트에 llms.txt 존재 여부 |
| Open Graph | og:title, og:description, og:url 완비 여부 |

#### 브랜드 명확성 (Brand Clarity) — 0~25점

AI가 인용 시 출처를 명확히 표기할 수 있는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| 조직명 명시 | 헤더 또는 About 페이지에서 확인 가능한 조직명 |
| 저자 정보 | 저자명, 직함, 프로필 링크 |
| 연락처 | 이메일·전화·주소 중 하나 이상 |
| Organization 스키마 | name, url, logo, sameAs 포함 여부 |
| 소셜 채널 연결 | 공식 SNS 링크로 브랜드 정체성 보강 |

---

### 3단계: 인용 점수 산출

```
인용 점수 = (직접답변구조 × 0.35) +
            (콘텐츠권위성 × 0.30) +
            (기술인용신호 × 0.20) +
            (브랜드명확성 × 0.15)
```

직접 답변 구조와 콘텐츠 권위성이 AI 인용에 가장 큰 영향을 미친다.

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | AI 검색 인용 최적화 상위 수준 |
| 60–79 | 양호 | 기본 인용 구조 갖춤, 개선 여지 있음 |
| 40–59 | 보통 | 주요 인용 신호 미흡 |
| 20–39 | 미흡 | 인용 가능성 낮음, 즉각 개선 필요 |
| 0–19 | 위험 | AI 검색에서 거의 인용되지 않음 |

---

### 4단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-인용가능성-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

AI 검색에서 인용될 가능성을 일상 언어로 전달한다.
"이 글이 ChatGPT나 AI 검색의 답변으로 등장할 가능성"을 중심으로 설명한다.
기술 용어 없이, 개선 방향은 누가 무엇을 해야 하는지로 안내한다.

```markdown
# [페이지 제목] AI 인용 가능성 분석

분석일: [날짜]  |  분석 URL: [URL]

---

## AI 인용 가능성: [높음 / 보통 / 낮음 / 매우 낮음]

[한 줄 요약]
예) "글의 구조가 AI가 답변으로 사용하기 어려운 형태입니다."

---

## 항목별 현황

| 확인 항목 | 현황 | 설명 |
|---|---|---|
| AI가 바로 답변으로 쓸 수 있는 구조인가요? | 좋음 / 주의 / 위험 | [한 줄] |
| 신뢰할 수 있는 데이터와 출처가 있나요? | 좋음 / 주의 / 위험 | [한 줄] |
| AI가 글 구조를 이해하도록 설정되어 있나요? | 좋음 / 주의 / 위험 | [한 줄] |
| AI가 인용 시 출처(브랜드명)를 알 수 있나요? | 좋음 / 주의 / 위험 | [한 줄] |

---

## 지금 개선할 수 있는 것 (마케팅팀)

1. **[조치 제목]**
   왜 중요한가: [이유 1–2문장]
   어떻게: [구체적인 방법, 기술 용어 없이]

2. **[조치 제목]**
   왜 중요한가: [이유]
   어떻게: [방법]

---

## 개발팀 / 운영팀 전달 요청

| 요청 내용 | 담당 | 이유 |
|---|---|---|
| [요청] | 개발팀 / 운영팀 | [이유 한 줄] |
```

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 CMS·FTP에서 직접 수정할 수 있는 방법을 안내한다.
FAQ 섹션 추가, 스키마 삽입 등을 단계별로 설명한다.
WordPress 기준으로 설명하되, 다른 CMS도 유사하게 적용 가능함을 명시한다.

```markdown
# [페이지 제목] AI 인용 가능성 분석

분석일: [날짜]  |  URL: [URL]

---

## 인용 점수: [점수]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| 직접 답변 구조 | [X]/25 | [발견 사항 한 줄] |
| 콘텐츠 권위성 | [X]/25 | [발견 사항 한 줄] |
| 기술 인용 신호 | [X]/25 | [발견 사항 한 줄] |
| 브랜드 명확성 | [X]/25 | [발견 사항 한 줄] |

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

### 기술 설정 (개발팀 요청)

**[제목]**
- 현재 상태: [설명]
- 요청 내용: [개발팀에 전달할 내용]
- 예상 효과: [효과]

---

## llms.txt 현황

**상태:** [존재 / 없음]

[존재 시] 내용 요약: [주요 항목 나열]

[없음 시] 권고: llms.txt 파일을 생성하여 사이트 루트(/llms.txt)에 업로드하세요.
FTP 접속 후 루트 디렉토리에 직접 추가하거나, 개발팀에 요청하세요.
```

---

### L3 출력 — 개발자

전체 기술 명세와 FAQPage·HowTo·speakable 스키마 코드를 포함한다.

```markdown
# [페이지 제목] AI Citability Analysis

Date: [날짜]  |  URL: [URL]

---

## Citability Score: [점수]/100

| Dimension | Score | Key Signals Found | Missing |
|---|---|---|---|
| Direct Answer Structure | [X]/25 | [신호 목록] | [누락 항목] |
| Content Authority | [X]/25 | [신호 목록] | [누락 항목] |
| Technical Citation Signals | [X]/25 | [신호 목록] | [누락 항목] |
| Brand Clarity | [X]/25 | [신호 목록] | [누락 항목] |

---

## Critical Citability Gaps

### [CRITICAL] FAQPage Schema Missing
현재: FAQ 형식 콘텐츠 존재하나 구조화 데이터 없음
영향: AI가 FAQ 항목을 개별 답변으로 인식하지 못해 인용 확률 감소
해결:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "[질문 텍스트]",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "[답변 텍스트]"
        }
      }
    ]
  }
  ```

### [CRITICAL] speakable 미설정
현재: speakable 속성 없음
영향: Google Assistant·Gemini 등 음성 AI에서 이 페이지 콘텐츠 미활용
해결:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "speakable": {
      "@type": "SpeakableSpecification",
      "cssSelector": ["h1", ".article-summary", ".key-points"]
    }
  }
  ```

### [WARNING] llms.txt 없음
현재: /llms.txt → 404
영향: AI 크롤러가 사이트 구조 파악 불가, 중요 페이지 누락 가능성
해결:
  ```
  # llms.txt
  # [사이트명] — AI 크롤러용 안내

  > [사이트 한 줄 설명]

  ## 주요 콘텐츠
  - [섹션명]: [URL]
  - [섹션명]: [URL]

  ## Sitemap
  - [sitemap URL]
  ```
검증: `curl -I https://[도메인]/llms.txt`

---

## 구현 우선순위

| 우선순위 | 작업 | 난이도 | 예상 인용 효과 | 담당 |
|---|---|---|---|---|
| 1 | [작업] | 낮음 / 보통 / 높음 | 높음 / 보통 / 낮음 | [FE/BE/콘텐츠] |
| 2 | [작업] | [난이도] | [효과] | [담당] |
| 3 | [작업] | [난이도] | [효과] | [담당] |
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
