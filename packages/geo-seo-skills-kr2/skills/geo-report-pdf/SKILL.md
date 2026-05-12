---
name: geo-report-pdf
description: >
  GEO 분석 결과를 PDF 출력에 최적화된 마크다운으로 재구성한다.
  Pandoc, wkhtmltopdf, md-to-pdf 등 로컬 변환 도구용 명령어를 함께 제공한다.
  클라이언트 납품 또는 내부 보고용 단일 문서로 완성한다.
  GEO-*.md 분석 파일이 있으면 자동으로 수집하여 반영한다.
  L3(개발자) 전용 스킬.
  트리거: "PDF 보고서", "PDF", "report-pdf", "/geo report-pdf".
audience: L3
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-report-pdf — PDF 보고서 생성

> 실행 시 USER_LEVEL을 확인한다.
> L1 또는 L2인 경우 아래 안내 메시지를 출력하고 실행을 중단한다.
> L3인 경우 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-보고서-[도메인]-[날짜].md`로 저장하고 PDF 변환 명령어를 출력한다.

---

## L1 / L2 접근 안내 (L1·L2이면 이 메시지 출력 후 중단)

```
PDF 보고서 생성은 로컬 변환 도구가 필요한 작업입니다.

현재 레벨에서는 직접 실행이 어렵습니다.

선택 사항:
1. 레벨을 변경하려면 `/geo level` 을 입력하세요.
2. 개발팀에 아래 내용을 전달하세요:

   "GEO 분석 결과를 PDF 보고서로 만들어 주세요.
    명령어: /geo report-pdf"
```

---

## PDF 변환 도구 안내

본 스킬은 마크다운 파일을 생성한다. PDF 변환은 로컬 도구로 처리한다.

| 도구 | 설치 | 변환 명령어 |
|---|---|---|
| **md-to-pdf** (권장) | `npm install -g md-to-pdf` | `md-to-pdf GEO-보고서-[도메인]-[날짜].md` |
| **Pandoc + LaTeX** | `brew install pandoc` | `pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="Noto Sans KR"` |
| **wkhtmltopdf** | `brew install wkhtmltopdf` | `pandoc input.md -o output.html && wkhtmltopdf output.html output.pdf` |
| **VS Code** | Markdown PDF 확장 | 명령 팔레트 → "Markdown PDF: Export (pdf)" |

> 한국어 폰트: Pandoc 사용 시 `-V mainfont="Noto Sans KR"` 또는 `-V mainfont="Apple SD Gothic Neo"` 추가

---

## 실행 단계

### 1단계: 분석 파일 수집

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import glob, os, re

files = sorted(glob.glob('GEO-*.md') + glob.glob('geo-*.md'))
if not files:
    print('분석 파일 없음 — /geo audit 먼저 실행 필요')
else:
    for f in files:
        print(f'  {f}')
"
```

**Claude 웹 환경**

> 현재 대화에서 공유된 GEO 분석 결과나 `/geo audit` 출력 내용을 참조한다.
> 로컬 파일을 읽을 수 없으므로 대화 내 분석 내용을 기반으로 보고서를 작성한다.
> 분석 결과가 없으면 아래 안내를 출력한다.

**파일이 없는 경우:**

```
분석 결과 파일이 없습니다.

아래 명령어로 분석을 먼저 실행하세요:
  /geo audit https://[도메인]

분석 완료 후 다시 /geo report-pdf 를 실행하세요.
```

---

### 2단계: 점수 및 핵심 내용 취합

각 분석 파일에서 점수, 등급, Critical Issues, 우선 조치를 추출한다.

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import glob, re

scores = {}
for f in sorted(glob.glob('GEO-*.md')):
    with open(f, encoding='utf-8') as fp:
        content = fp.read()
    # 점수 패턴 추출
    m = re.search(r'(\d+)/100', content)
    if m:
        scores[f] = int(m.group(1))
    print(f'{f}: {scores.get(f, \"점수 없음\")}')
"
```

---

### 3단계: PDF용 마크다운 구성

분석 파일 내용을 기반으로 PDF 출력에 최적화된 단일 마크다운을 작성한다.

**PDF 마크다운 설계 원칙:**
- 페이지 구분: `---` (수평선) + `\pagebreak` (Pandoc용)
- 표는 최대 5열 이내로 제한 (PDF 너비 초과 방지)
- 코드 블록은 핵심 스니펫만 포함 (길이 제한)
- 이미지 없이 텍스트·표·목록만 사용

---

### 4단계: 보고서 출력 및 PDF 변환 명령어 제공

아래 템플릿에 따라 마크다운 보고서를 작성하고, PDF 변환 명령어를 함께 출력한다.

---

## 출력 템플릿 (L3 전용)

```markdown
---
title: "GEO 분석 보고서"
subtitle: "[도메인]"
date: "[날짜]"
author: "[담당자 또는 팀명]"
---

# GEO 분석 보고서

**대상 사이트:** [도메인]  
**분석일:** [날짜]  
**작성:** [담당자]  

---

## 1. 종합 현황

### GEO 점수 요약

| 영역 | 점수 | 등급 |
|---|---|---|
| GEO 종합 | [X]/100 | [등급] |
| 콘텐츠 품질 | [X]/100 | [등급] |
| AI 인용 가능성 | [X]/100 | [등급] |
| AI 크롤러 접근 | [X]/100 | [등급] |
| 브랜드 언급 | [X]/100 | [등급] |
| 플랫폼 최적화 | [X]/100 | [등급] |
| 기술 SEO | [X]/100 | [등급] |

### 핵심 발견

1. [Critical Issue 1 — 한 줄]
2. [Critical Issue 2 — 한 줄]
3. [Critical Issue 3 — 한 줄]

---

## 2. 영역별 상세 결과

### 2-1. GEO 종합

**점수:** [X]/100 — [등급]

[주요 발견 2~3줄 요약]

**즉시 조치 필요:**
- [조치 1]
- [조치 2]

---

### 2-2. 콘텐츠 품질

**점수:** [X]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| 경험 (Experience) | [X]/25 | [발견] |
| 전문성 (Expertise) | [X]/25 | [발견] |
| 권위성 (Authority) | [X]/25 | [발견] |
| 신뢰성 (Trust) | [X]/25 | [발견] |

---

### 2-3. AI 인용 가능성

**점수:** [X]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| 직접 답변 구조 | [X]/25 | [발견] |
| 콘텐츠 권위성 | [X]/25 | [발견] |
| 기술 인용 신호 | [X]/25 | [발견] |
| 브랜드 명확성 | [X]/25 | [발견] |

---

### 2-4. AI 크롤러 접근

**점수:** [X]/100 — [등급]

| 봇 | 용도 | 현재 상태 |
|---|---|---|
| GPTBot | 학습 | 허용 / 차단 |
| ClaudeBot | 학습 | 허용 / 차단 |
| ChatGPT-User | 검색 | 허용 / 차단 |
| PerplexityBot | 검색 | 허용 / 차단 |
| Google-Extended | 이중 | 허용 / 차단 |

---

### 2-5. 브랜드 언급

**점수:** [X]/100 — [등급]

[주요 발견 2~3줄]

---

### 2-6. 플랫폼 최적화

**점수:** [X]/100 — [등급]

| 플랫폼 | 상태 | 주요 이슈 |
|---|---|---|
| Google AI Overviews | 좋음 / 주의 / 위험 | [이슈] |
| Perplexity | 좋음 / 주의 / 위험 | [이슈] |
| ChatGPT | 좋음 / 주의 / 위험 | [이슈] |
| Bing Copilot | 좋음 / 주의 / 위험 | [이슈] |
| Grok | 좋음 / 주의 / 위험 | [이슈] |

---

### 2-7. 기술 SEO

**점수:** [X]/100 — [등급]

| 항목 | 상태 | 비고 |
|---|---|---|
| HTTPS | ✅ / ❌ | |
| sitemap.xml | ✅ / ❌ | |
| robots.txt | ✅ / ❌ | |
| canonical | ✅ / ❌ | |
| Core Web Vitals | [추정] | LCP / CLS / INP |

---

## 3. 개선 로드맵

### 1주차 — CRITICAL 즉시 처리

| 작업 | 담당 | 공수 | 효과 |
|---|---|---|---|
| [작업] | [담당] | [X]h | [효과] |

> CRITICAL 항목이 없으면 이 섹션은 생략하고 2주차부터 시작한다.

### 2주차 — HIGH 우선 처리

| 작업 | 담당 | 공수 | 효과 |
|---|---|---|---|
| [작업] | [담당] | [X]h | [효과] |

### 3~4주차 — MEDIUM 처리

| 작업 | 담당 | 공수 | 효과 |
|---|---|---|---|
| [작업] | [담당] | [X]h | [효과] |

### 이후 — LOW 순차 개선

| 작업 | 담당 | 공수 | 효과 |
|---|---|---|---|
| [작업] | [담당] | [X]h | [효과] |

---

## 4. 재분석 일정

| 시점 | 명령어 | 목적 |
|---|---|---|
| 1~2주차 완료 후 | `/geo audit https://[도메인]` | CRITICAL·HIGH 개선 효과 확인 |
| 3~4주차 완료 후 | `/geo report https://[도메인]` | 중간 성과 보고서 생성 |
| 4주 이후 | `/geo audit https://[도메인]` | 최종 GEO 점수 측정 |

---

*본 보고서는 분석 시점 기준입니다. AI 검색 환경은 빠르게 변화하므로 3개월 주기 재분석을 권장합니다.*
```

---

## PDF 변환 명령어 (보고서 저장 후 출력)

```bash
# 방법 1: md-to-pdf (가장 간단)
md-to-pdf "GEO-보고서-[도메인]-[날짜].md"

# 방법 2: Pandoc + xelatex (한국어 폰트 지정)
pandoc "GEO-보고서-[도메인]-[날짜].md" \
  -o "GEO-보고서-[도메인]-[날짜].pdf" \
  --pdf-engine=xelatex \
  -V mainfont="Apple SD Gothic Neo" \
  -V fontsize=11pt \
  -V geometry:margin=2cm

# 방법 3: Pandoc → HTML → wkhtmltopdf
pandoc "GEO-보고서-[도메인]-[날짜].md" -o temp.html --standalone
wkhtmltopdf --encoding utf-8 temp.html "GEO-보고서-[도메인]-[날짜].pdf"
rm temp.html

# 변환 도구 설치 확인
which md-to-pdf || echo "미설치: npm install -g md-to-pdf"
which pandoc    || echo "미설치: brew install pandoc"
```
