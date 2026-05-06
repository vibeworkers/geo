---
name: geo-report
description: >
  GEO 종합 보고서 생성. 개별 스킬 분석 결과를 취합하여
  공유·보고·추적에 적합한 형태의 종합 보고서를 만든다.
  geo-audit 이후 자동으로 실행되거나 단독으로 실행할 수 있다.
  L1은 경영진·팀장 공유용 요약, L2는 작업 체크리스트,
  L3는 기술 명세 전체를 포함하는 구현 로드맵을 생성한다.
  트리거: "보고서", "리포트", "report", "요약", "/geo report".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-report — GEO 종합 보고서 생성

> 실행 시 USER_LEVEL을 확인한다. 설정되지 않은 경우 레벨 선택을 먼저 요청한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-종합보고서.md`로 저장한다.

---

## geo-audit와의 관계

| 스킬 | 역할 |
|---|---|
| geo-audit | 5개 영역 분석을 오케스트레이션하고 종합 GEO 점수 산출 |
| geo-report | 분석 결과를 수신자(레벨)에 맞는 보고서 형태로 재구성·저장 |

geo-audit 직후 실행하면 최신 분석 결과를 반영한다.
단독 실행 시에는 현재 폴더의 `GEO-*.md` 파일을 읽어 취합한다.

---

## 실행 단계

### 1단계: 분석 결과 수집

현재 작업 폴더에서 기존 분석 파일을 읽는다.

```
읽기 대상 파일 (존재하는 경우):
- GEO-감사-보고서.md
- GEO-콘텐츠-분석.md
- GEO-인용가능성-분석.md
- GEO-크롤러-분석.md
- GEO-브랜드언급-분석.md
- GEO-플랫폼-분석.md
```

파일이 없는 경우: 사용자에게 먼저 `/geo audit [URL]`을 실행하도록 안내한다.

---

### 2단계: 점수 취합

각 분석 파일에서 점수를 추출하고 종합 GEO 점수를 계산한다.

```
종합 GEO 점수 = (인용 점수 × 0.25) +
               (크롤러 점수 × 0.20) +
               (콘텐츠 점수 × 0.20) +
               (기술 점수 × 0.15) +
               (스키마 점수 × 0.10) +
               (플랫폼 점수 × 0.10)
```

분석 파일이 일부만 있는 경우: 존재하는 점수만 사용하고 누락 항목을 명시한다.

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | AI 검색 최적화 상위 수준 |
| 60–79 | 양호 | 기본 최적화 완료, 개선 여지 있음 |
| 40–59 | 보통 | 주요 개선 과제 다수 존재 |
| 20–39 | 미흡 | 즉각적인 조치 필요 |
| 0–19 | 위험 | AI 검색에서 거의 노출되지 않음 |

---

### 3단계: 개선 과제 우선순위 정렬

각 분석에서 도출된 개선 과제를 아래 기준으로 분류한다.

| 우선순위 | 기준 |
|---|---|
| 즉시 (이번 주) | 난이도 낮음 + GEO 효과 높음 |
| 단기 (이번 달) | 난이도 보통 + 효과 높음, 또는 난이도 낮음 + 효과 보통 |
| 중장기 | 난이도 높음, 또는 효과 낮음 |

---

### 4단계: 레벨별 보고서 작성 및 저장

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-종합보고서.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

1페이지 분량의 경영진·팀장 공유용 요약 보고서다.
점수 수치 없이 상태 표현을 사용하고, 즉시 실행 가능한 조치 3가지를 제시한다.
기술적 세부 내용은 생략하고 비즈니스 영향 중심으로 작성한다.

```markdown
# [사이트명] AI 검색 노출 현황 요약 보고서

분석일: [날짜]  |  작성: GEO 분석 스킬

---

## 종합 현황: [우수 / 양호 / 보통 / 미흡 / 위험]

[2–3문장 요약]
예) "현재 사이트는 ChatGPT와 Perplexity에서 기본 노출은 되지만,
콘텐츠 신뢰도와 브랜드 인지도가 낮아 경쟁사 대비 AI 검색 노출이 부족한 상태입니다.
주요 문제 3가지를 개선하면 60일 내 가시적인 변화를 기대할 수 있습니다."

---

## 영역별 현황

| 확인 영역 | 현황 | 한 줄 설명 |
|---|---|---|
| AI 봇이 사이트를 볼 수 있나요? | 좋음 / 주의 / 위험 | [설명] |
| AI 검색에 글이 인용되나요? | 좋음 / 주의 / 위험 | [설명] |
| 콘텐츠 신뢰도는 충분한가요? | 좋음 / 주의 / 위험 | [설명] |
| AI가 브랜드를 알고 있나요? | 좋음 / 주의 / 위험 | [설명] |
| 주요 AI 플랫폼에 노출되나요? | 좋음 / 주의 / 위험 | [설명] |

---

## 지금 당장 해야 할 일 (Top 3)

1. **[조치 제목]** — 담당: [마케팅팀 / 개발팀 / 운영팀]
   왜 중요한가: [이유 1–2문장]
   요청 내용: [담당자에게 전달할 구체적 요청]

2. **[조치 제목]** — 담당: [담당]
   왜 중요한가: [이유]
   요청 내용: [요청]

3. **[조치 제목]** — 담당: [담당]
   왜 중요한가: [이유]
   요청 내용: [요청]

---

## 개발팀 / 운영팀 전달 목록

아래 내용을 해당 담당자에게 전달해 주세요.

| 작업 내용 | 담당 | 이유 | 우선순위 |
|---|---|---|---|
| [작업] | 개발팀 | [이유 한 줄] | 높음 |
| [작업] | 운영팀 | [이유 한 줄] | 보통 |

---

*이 보고서는 GEO 분석 스킬로 자동 생성됐습니다. 상세 분석 결과는 담당자에게 요청하세요.*
```

---

### L2 출력 — 웹마스터 / 운영자

영역별 점수와 함께 전체 작업 목록을 체크리스트 형태로 제공한다.
완료 시 체크하며 진행 상황을 추적할 수 있도록 구성한다.

```markdown
# [사이트명] GEO 종합 분석 보고서

분석일: [날짜]  |  URL: [URL]

---

## 종합 GEO 점수: [점수]/100 — [등급]

| 영역 | 점수 | 상태 |
|---|---|---|
| AI 인용 가능성 | [X]/100 | 좋음 / 주의 / 위험 |
| AI 크롤러 접근 | [X]/100 | 좋음 / 주의 / 위험 |
| 콘텐츠 품질 | [X]/100 | 좋음 / 주의 / 위험 |
| 브랜드 언급 | [X]/100 | 좋음 / 주의 / 위험 |
| 플랫폼 최적화 | [X]/100 | 좋음 / 주의 / 위험 |

---

## 전체 작업 체크리스트

### 즉시 처리 (이번 주)

- [ ] **[작업명]** — [영역] | 예상 시간: [X분]
  방법: [한 줄 설명]

- [ ] **[작업명]** — [영역] | 예상 시간: [X분]
  방법: [한 줄 설명]

- [ ] **[작업명]** — [영역] | 예상 시간: [X분]
  방법: [한 줄 설명]

### 단기 처리 (이번 달)

- [ ] **[작업명]** — [영역]
  방법: [한 줄 설명]

- [ ] **[작업명]** — [영역]
  방법: [한 줄 설명]

### 개발팀 요청 사항

- [ ] **[작업명]** — 우선순위: [높음 / 보통]
  요청 내용: [한 줄]

- [ ] **[작업명]** — 우선순위: [높음 / 보통]
  요청 내용: [한 줄]

### 중장기 과제

- [ ] **[작업명]** — [영역]
  설명: [한 줄]

---

## 영역별 핵심 발견

### AI 크롤러 접근
[3–5줄 요약]

### AI 인용 가능성
[3–5줄 요약]

### 콘텐츠 품질
[3–5줄 요약]

### 브랜드 언급
[3–5줄 요약]

### 플랫폼 최적화
[3–5줄 요약]

---

*체크리스트 완료 후 `/geo audit [URL]`을 다시 실행하여 점수 변화를 확인하세요.*
```

---

### L3 출력 — 개발자

전체 기술 명세와 구현 로드맵을 포함한다.
영역별 점수 breakdown, Critical Issues, 코드 스니펫 링크, 구현 우선순위 매트릭스를 제공한다.

```markdown
# [사이트명] GEO Technical Report

Date: [날짜]  |  URL: [URL]  |  Business Type: [유형]

---

## GEO Score: [점수]/100 — [등급]

| Category | Raw Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | [X]/100 | 25% | [X] |
| Crawler Access | [X]/100 | 20% | [X] |
| Content Quality | [X]/100 | 20% | [X] |
| Technical SEO | [X]/100 | 15% | [X] |
| Structured Data | [X]/100 | 10% | [X] |
| Platform Opt. | [X]/100 | 10% | [X] |
| **합계** | | | **[점수]/100** |

---

## Critical Issues (즉시 조치 필요)

### [CRITICAL] [문제 제목] — [영역]
- 현재: [현재 상태]
- 영향: [영향 설명]
- 해결:
  ```[언어]
  [코드 스니펫]
  ```
- 검증: [확인 방법]

### [CRITICAL] [문제 제목] — [영역]
[동일 형식]

---

## 구현 로드맵

### Sprint 1 — 즉시 처리 (난이도 낮음, 효과 높음)

| 작업 | 영역 | 파일/위치 | 예상 시간 | 담당 |
|---|---|---|---|---|
| [작업] | [영역] | [파일 경로] | [X시간] | [FE/BE/DevOps] |
| [작업] | [영역] | [파일 경로] | [X시간] | [담당] |

### Sprint 2 — 단기 처리 (이번 달)

| 작업 | 영역 | 설명 | 담당 |
|---|---|---|---|
| [작업] | [영역] | [설명] | [담당] |

### Sprint 3 — 중장기

| 작업 | 영역 | 설명 | 담당 |
|---|---|---|---|
| [작업] | [영역] | [설명] | [담당] |

---

## 영역별 상세 분석 링크

- AI Citability: `GEO-인용가능성-분석.md`
- Crawler Access: `GEO-크롤러-분석.md`
- Content Quality: `GEO-콘텐츠-분석.md`
- Brand Mentions: `GEO-브랜드언급-분석.md`
- Platform Optimization: `GEO-플랫폼-분석.md`

---

## 재분석 명령어

```bash
# 전체 재분석
/geo audit [URL]

# 영역별 재분석
/geo content [URL]
/geo crawlers [URL]
/geo citability [URL]
/geo brand [URL]
/geo platform [URL]
```
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
