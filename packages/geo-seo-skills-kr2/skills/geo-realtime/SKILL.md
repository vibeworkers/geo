---
name: geo-realtime
description: >
  Claude Code 전용 확장 계층. Playwright + browser-citation.js로
  AI 플랫폼 7개(Perplexity, Google AIO, Bing Copilot, ChatGPT, Gemini, Claude, Grok)에서
  도메인·브랜드 인용 여부를 실측한다.
  --cp 옵션으로 Tunnel Framework CP 콘텐츠(topics.csv + H2/H3)에서 질문을 자동 추출하여
  CP 사이클과 GEO 실측을 연결한다.
  --track 옵션으로 geo-brand BASELINE에 실측 결과를 기록해 Gap 시계열 추적을 지원한다.
  Claude 웹 환경에서 호출하면 안내 메시지를 출력하고 중단한다.
  트리거: "실측", "browser-citation", "인용 확인", "실시간 인용", "/geo realtime".
audience: L3
allowed-tools: Read, Bash, Write
---

# geo-realtime — AI 인용 실측 (확장 계층)

> **Claude Code 전용:** 이 스킬은 Playwright + browser-citation.js가 필요하다.
> Claude 웹에서 호출하면 아래 메시지를 출력하고 중단한다.
>
> ```
> 이 기능은 Claude Code(터미널)에서만 실행할 수 있습니다.
> Playwright 브라우저 자동화가 필요하므로 웹 환경에서는 지원되지 않습니다.
> Claude Code를 실행한 후 동일 명령어를 다시 입력해 주세요.
> ```

---

## 명령어

```
/geo realtime <url>              도메인 기반 표준 질문 10개로 실측
/geo realtime <url> --cp         CP 콘텐츠에서 질문 추출 후 실측
/geo realtime <url> --cp --track 실측 후 geo-brand BASELINE에 결과 기록
/geo realtime <url> --platforms <목록>  플랫폼 지정 (기본: perplexity,google_aio,bing)
/geo realtime <url> --headed     Chrome 창 표시 모드 (최초 로그인 설정 시 사용)
```

| 옵션 | 설명 | 기본값 |
|---|---|---|
| `--cp` | CP 콘텐츠(topics.csv + H2/H3)에서 질문 자동 추출 | 사용 안 함 |
| `--track` | 실측 결과를 geo-brand BASELINE-*.json에 기록 | 사용 안 함 |
| `--platforms` | 쉼표 구분 플랫폼 목록 | `perplexity,google_aio,bing` |
| `--headed` | Chrome 창 화면 표시 (최초 로그인 설정 시) | headless |

---

## 실행 환경

| 항목 | 내용 |
|---|---|
| 스크립트 | `~/.claude/skills/browser-citation/browser-citation.js` |
| 런타임 | Node.js + Playwright CDP |
| Chrome 프로필 | `~/.claude/skills/browser-citation/chrome-debug-profile/` |
| CDP 포트 | `9222` |
| Tunnel 경로 | `/Users/seomkt/Library/CloudStorage/GoogleDrive-seomkt.kr@gmail.com/내 드라이브/00_tunnel` |

---

## 실행 단계

### 0단계: 환경 확인

실행 전 아래 3가지를 순서대로 검사한다. 하나라도 실패하면 해결 방법을 안내하고 중단한다.

**1. Node.js + Playwright 설치 확인**

```bash
node -e "require('playwright'); console.log('ok')" 2>&1
```

실패 시:
```
Playwright가 설치되지 않았습니다.
다음 명령어로 설치하세요:
  npm install -g playwright && npx playwright install chromium
```

**2. browser-citation.js 존재 확인**

```bash
ls ~/.claude/skills/browser-citation/browser-citation.js 2>&1
```

실패 시:
```
browser-citation.js를 찾을 수 없습니다.
~/.claude/skills/browser-citation/ 경로에 스크립트가 있는지 확인하세요.
```

**3. Chrome CDP 연결 확인**

```bash
curl -s --max-time 3 http://localhost:9222/json/version 2>&1
```

연결 실패 시 자동 시작 시도. 자동 시작도 실패하면:
```
Chrome CDP 연결에 실패했습니다.
Chrome이 실행 중이지 않거나 CDP 포트(9222)가 닫혀 있습니다.
--headed 옵션으로 재실행하거나 Chrome을 수동으로 시작하세요.
```

---

### 1단계: 도메인 및 브랜드명 추출

URL에서 도메인을 추출하고, 홈페이지에서 브랜드명을 감지한다.

```bash
DOMAIN=$(echo "$URL" | sed 's|https\?://||' | sed 's|/.*||')
```

브랜드명 감지 순서:
1. `<meta property="og:site_name">` 값
2. `<title>` 태그 첫 번째 토큰 (` | `, ` - `, ` – ` 기준으로 분리)
3. 감지 실패 시 도메인 사용

---

### 2단계: 질문 생성

#### 기본 모드 (`--cp` 없음)

도메인/브랜드명을 기반으로 표준 질문 10개를 생성한다.

```
[브랜드명]이란 무엇인가요?
[브랜드명]의 주요 기능은 무엇인가요?
[브랜드명] 사용 방법을 알려주세요
[브랜드명] 가격은 얼마인가요?
[브랜드명] 장단점을 비교해주세요
[브랜드명] 대안·경쟁사 추천
[비즈니스 유형] 추천 서비스는?
[비즈니스 유형]에서 [브랜드명] 선택 이유
[브랜드명] 사용 후기·평가
[브랜드명] vs 경쟁사 비교
```

비즈니스 유형은 홈페이지 내용에서 감지한다 (SaaS / 로컬 비즈니스 / 이커머스 / 미디어 / 에이전시).

#### --cp 모드

CP 콘텐츠에서 질문을 추출한다.

```
TUNNEL="/Users/seomkt/Library/CloudStorage/GoogleDrive-seomkt.kr@gmail.com/내 드라이브/00_tunnel"
CP_DIR="$TUNNEL/10_projects/$DOMAIN/04_cp"
```

**a. topics.csv에서 주제 추출**

```bash
# 완료 상태 행의 topic_title 또는 keyword 열 추출 (P0 우선)
cat "$CP_DIR/topics.csv" 2>/dev/null
```

topics.csv에서 추출 기준:
- 상태가 '완료' 또는 'done'인 행 우선
- P0 → P1 → P2 우선순위 순서
- `topic_title` 열 값을 질문 형식으로 변환

**b. 완성 콘텐츠 H2/H3에서 질문 추출**

```bash
grep -h "^## \|^### " "$CP_DIR/contents/"*.md 2>/dev/null | head -30
```

H2/H3 제목을 질문 형식으로 변환하는 규칙:

| 제목 패턴 | 변환 형식 |
|---|---|
| "~하는 방법" | 그대로 사용 |
| "~란", "~이란" | "~이란 무엇인가요?" |
| 명사형 (~기능, ~특징) | "~은 무엇인가요?" |
| 비교형 (~vs~) | "~와 ~의 차이는 무엇인가요?" |
| 기타 | "[제목]에 대해 설명해주세요" |

**c. 최종 질문 선택**

a + b에서 수집된 질문을 중복 제거 후 최대 10개 선택한다.
우선순위: topics.csv P0 완료 → topics.csv P1 완료 → H2 제목 → H3 제목.

topics.csv가 없는 경우 기본 모드 질문 5개 + H2/H3 질문 5개를 혼합한다.

---

### 3단계: browser-citation 실행

추출된 질문 목록을 browser-citation.js에 전달한다.

```bash
TUNNEL="/Users/seomkt/Library/CloudStorage/GoogleDrive-seomkt.kr@gmail.com/내 드라이브/00_tunnel"
SCRIPT="$HOME/.claude/skills/browser-citation/browser-citation.js"
OUTPUT="/tmp/geo-realtime-$(date +%s).json"
KEYWORDS=$(echo "$QUESTIONS" | tr '\n' ',' | sed 's/,$//')

node "$SCRIPT" \
  --domain "$DOMAIN" \
  --keywords "$KEYWORDS" \
  --brand "$BRAND" \
  --platforms "$PLATFORMS" \
  --mode geo \
  --output "$OUTPUT" 2>&1
```

플랫폼 기본값: `perplexity,google_aio,bing`
전체 플랫폼 지정 시: `perplexity,google_aio,bing,chatgpt,gemini,claude,grok`

> 전체 플랫폼 + 10개 질문 기준 예상 소요 시간: 15~25분.
> 로그인 필요 플랫폼(chatgpt·gemini·claude·grok) 미설정 시 해당 플랫폼 건너뛰고 진행한다.
> 최초 로그인 설정: `--headed` 옵션으로 재실행.

---

### 4단계: 결과 분석

browser-citation.js가 출력한 JSON을 파싱하여 인용·미인용을 분류한다.

**판정 유형:**

| 유형 | 설명 |
|---|---|
| `citation_link` | `<a href>` 링크로 인용 (가장 강함) |
| `domain_url` | 답변 텍스트에 도메인 직접 등장 |
| `brand_name` | 브랜드명 언급 (링크 없음) |
| `none` | 미인용 |

**인용률 산출:**

```
플랫폼별 인용률 = 해당 플랫폼에서 인용된 질문 수 / 전체 질문 수 × 100
전체 인용률 = (모든 플랫폼 인용 건수 합계) / (플랫폼 수 × 질문 수) × 100
```

**인용 강도 등급:**

| 인용률 | 등급 | 설명 |
|---|---|---|
| 60% 이상 | STRONG | AI 검색에서 높은 인용 빈도 |
| 40–59% | MODERATE | 일부 플랫폼·질문에서 인용 |
| 20–39% | WEAK | 인용 있으나 산발적 |
| 0–19% | MINIMAL | 거의 인용되지 않음 |

---

### 5단계: --track 처리 (옵션)

`--track` 옵션이 있으면 현재 폴더에서 `GEO-BRAND-BASELINE-*.json`을 찾아 실측 결과를 기록한다.

```bash
ls GEO-BRAND-BASELINE-*.json 2>/dev/null | sort -r | head -1
```

BASELINE 파일이 있으면 `realtime_snapshots` 배열에 항목을 추가한다:

```json
{
  "date": "2026-05-09",
  "source": "geo-realtime",
  "platforms": ["perplexity", "google_aio", "bing"],
  "question_count": 10,
  "overall_citation_rate": 42,
  "by_platform": {
    "perplexity": { "cited": 5, "total": 10, "rate": 50 },
    "google_aio":  { "cited": 3, "total": 10, "rate": 30 },
    "bing":        { "cited": 5, "total": 10, "rate": 50 }
  },
  "cited_questions":   ["질문1", "질문3"],
  "uncited_questions": ["질문2", "질문4", "질문5"]
}
```

BASELINE 파일이 없으면:
```
geo-brand BASELINE 파일을 찾을 수 없습니다.
먼저 /geo brand <url>을 실행하여 BASELINE을 생성하세요.
--track 없이 실측 결과만 보고서에 저장합니다.
```

---

### 6단계: 보고서 생성

결과를 `GEO-REALTIME-[도메인]-[날짜].md`로 저장한다.

---

## 출력 보고서 템플릿

```markdown
# [도메인] AI 인용 실측 보고서

실측일: [날짜]  |  질문 수: [N]개  |  플랫폼: [목록]
모드: [기본 / CP 콘텐츠 기반]

---

## 종합 인용률: [X]% — [STRONG / MODERATE / WEAK / MINIMAL]

| 플랫폼 | 인용 | 전체 | 인용률 | 주요 판정 유형 |
|---|---|---|---|---|
| Perplexity   | [N] | [T] | [X]% | citation_link / domain_url / brand_name |
| Google AIO   | [N] | [T] | [X]% | — |
| Bing Copilot | [N] | [T] | [X]% | — |
| ChatGPT      | [N] | [T] | [X]% | — |
| Gemini       | [N] | [T] | [X]% | — |
| Claude       | [N] | [T] | [X]% | — |
| Grok         | [N] | [T] | [X]% | — |

---

## 인용된 질문

| 질문 | 인용 플랫폼 | 판정 유형 |
|---|---|---|
| [질문] | Perplexity, Bing | citation_link |
| [질문] | Google AIO | domain_url |

---

## 미인용 질문 (콘텐츠 보강 후보)

| 질문 | 미인용 플랫폼 | 권고 조치 |
|---|---|---|
| [질문] | 전체 | /cp prep 재투입 또는 콘텐츠 심화 |
| [질문] | Perplexity, ChatGPT | 해당 질문 키워드로 콘텐츠 보강 |

---

## CP 연동 권고 (--cp 모드일 때만 출력)

미인용 질문 [N]개를 CP 파이프라인에 재투입하면 인용률 개선을 기대할 수 있습니다.

재투입 대상 질문:
1. [질문]
2. [질문]

다음 명령어로 콘텐츠 계획을 시작하세요:
  /cp prep https://[도메인]

---

## BASELINE 업데이트 결과 (--track 모드일 때만 출력)

BASELINE 파일: GEO-BRAND-BASELINE-[도메인]-[날짜].json
ΔGap (이전 대비): +[X]% 또는 -[X]%
추적 스냅샷: [N]회차 기록 완료

---

## 다음 실측 권고

다음 실측 예정: [날짜 + 4주]
명령어: /geo realtime https://[도메인] --cp --track
```

---

## 오류 처리

| 상황 | 대응 |
|---|---|
| Playwright 미설치 | 설치 명령어 안내 후 중단 |
| browser-citation.js 없음 | 경로 확인 안내 후 중단 |
| Chrome CDP 연결 실패 | `--headed` 옵션 재실행 안내 후 중단 |
| topics.csv 없음 | CP 콘텐츠 없음 안내 + 기본 모드 질문 10개로 대체 실행 |
| 로그인 필요 플랫폼 세션 만료 | 해당 플랫폼 건너뜀 + `--headed` 재설정 안내 |
| 질문 수 0개 | H2/H3 없는 경우 — 기본 모드로 자동 전환 안내 |
| BASELINE 파일 없음 (--track) | --track 무시 + 보고서만 저장 |

---

## 연동 스킬

| 스킬 | 관계 |
|---|---|
| `browser-citation` | 내부 호출 — Playwright CDP 실행 주체 |
| `geo-brand` | BASELINE 생성·Gap 측정 (--track 연동) |
| `geo-citability` | WebFetch 기반 인용 가능성 점수와 실측 결과 비교 참조 |
| `cp` | --cp 모드에서 topics.csv + 콘텐츠 파일 읽기 |

---

## 실행 시간 안내

| 플랫폼 수 | 질문 수 | 예상 시간 |
|---|---|---|
| 3개 (perplexity, google_aio, bing) | 10개 | 5~10분 |
| 7개 (전 플랫폼) | 10개 | 15~25분 |

Chrome은 화면 밖(9999,9999)에서 실행되므로 Mac 사용에 제약 없음.
