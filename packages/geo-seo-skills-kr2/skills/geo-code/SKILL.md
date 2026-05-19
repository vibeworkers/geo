---
name: geo-code
description: >
  Claude Code 전용 확장 계층 오케스트레이터.
  환경 초기화(init), 자동 파이프라인(pipeline), 상태 확인(status) 3가지 명령으로
  geo-realtime·geo-tracker·geo-batch 확장 계층 스킬을 통합 실행한다.
  pipeline은 단일 도메인(audit → realtime → tracker)과
  복수 도메인(batch → 선별 → audit → realtime → tracker) 두 흐름을 지원한다.
  Claude 웹 환경에서 호출하면 안내 메시지를 출력하고 중단한다.
  트리거: "/geo-code", "geo-code init", "geo-code pipeline", "geo-code status",
  "확장 파이프라인", "Code 파이프라인", "실측 파이프라인".
audience: L3
allowed-tools: Read, Bash, Write
---

# geo-code — 확장 계층 오케스트레이터 (Claude Code 전용)

> **Claude Code 전용:** Bash·Playwright·로컬 파일 시스템 접근이 필요하다.
> Claude 웹에서 호출하면 아래 메시지를 출력하고 중단한다.
>
> ```
> 이 기능은 Claude Code(터미널)에서만 실행할 수 있습니다.
> 코어 계층 분석은 웹에서도 /geo 명령어로 실행할 수 있습니다.
> Claude Code를 실행한 후 /geo-code init부터 시작하세요.
> ```

---

## 명령어

```
/geo-code init                          환경 초기화 및 점검
/geo-code pipeline <url>                단일 도메인 자동 파이프라인
/geo-code pipeline <url1> <url2> ...    복수 도메인 파이프라인 (batch 선행)
/geo-code pipeline <url> --cp           CP 콘텐츠 기반 질문 추출 포함
/geo-code status [도메인]               현재 폴더·프로젝트 연동 상태 확인
```

| 옵션 | 설명 | 기본값 |
|---|---|---|
| `--cp` | CP topics.csv + H2/H3에서 질문 추출 (geo-realtime 연동) | 사용 안 함 |
| `--top <N>` | 복수 도메인 중 점수 하위 N개만 후속 감사 (기본: 3) | `3` |

---

## `/geo-code init` — 환경 초기화

환경 5개 항목을 순서대로 확인하고 결과 표를 출력한다.
하나라도 FAIL이면 해결 방법을 안내하고, 전체 통과 시 pipeline 실행 안내를 출력한다.

### 확인 항목

| 순서 | 항목 | 확인 명령어 | 실패 시 안내 |
|---|---|---|---|
| 1 | Node.js | `node --version` | nodejs.org 설치 링크 |
| 2 | Playwright | `node -e "require('playwright'); console.log('ok')"` | `npm install playwright` |
| 3 | Chromium | `npx playwright install --dry-run chromium 2>&1` | `npx playwright install chromium` |
| 4 | browser-citation.js | `ls ~/.claude/skills/browser-citation/browser-citation.js` | 경로 확인 안내 |
| 5 | Chrome CDP | `curl -s --max-time 3 http://localhost:9222/json/version` | `--headed` 최초 실행 안내 |

### 출력 형식

```
[ geo-code 환경 점검 ]

  Node.js          v20.x.x   PASS
  Playwright       1.x.x     PASS
  Chromium                   PASS
  browser-citation           PASS
  Chrome CDP       9222      PASS  ← 연결됨

환경 준비 완료. 다음 명령어로 시작하세요:
  /geo-code pipeline https://example.com
```

FAIL 항목이 있는 경우:

```
  Chrome CDP       —         FAIL

해결 방법:
  최초 1회 Chrome을 열어 로그인 설정이 필요합니다.
  /geo realtime <url> --headed 를 실행하면 Chrome 창이 열립니다.
  ChatGPT·Gemini·Claude·Grok에 로그인 후 창을 닫지 말고 기다리면
  자동으로 세션이 저장됩니다.
```

---

## `/geo-code pipeline` — 자동 파이프라인

### 단일 도메인 흐름

`/geo-code pipeline <url>` 또는 `/geo-code pipeline <url> --cp`

```
Step 0  환경 간이 확인 (init 축약 — Node.js + browser-citation.js만 확인)
Step 1  /geo audit <url>
        → GEO-감사-보고서.md 생성
        → CRITICAL 항목 있으면 경고 배너 출력 후 계속 진행 여부 질의
Step 2  /geo brand <url>
        → GEO-BRAND-BASELINE-*.json 없으면 최초 생성
        → 이미 있으면 건너뜀 (--track은 Step 3에서 처리)
Step 3  /geo realtime <url> [--cp] --track
        → GEO-REALTIME-*.md 생성 + BASELINE 실측 스냅샷 추가
Step 4  /geo tracker <도메인>
        → GEO-TRACKER-*.md 생성
Step 5  종합 요약 출력
```

Step 2(geo-brand)는 BASELINE이 이미 있으면 건너뛰고, Step 3에서 --track으로 갱신한다.

### 복수 도메인 흐름

`/geo-code pipeline <url1> <url2> ...`

```
Step 0  환경 간이 확인
Step 1  /geo batch <url1> <url2> ...
        → GEO-BATCH-*.md 생성 (비교 표)
        → 점수 하위 --top N개 자동 선별
        → 선별 결과를 출력하고 계속 진행 여부 질의

Step 2  선별 도메인별 순차 실행:
        (각 도메인에 대해 아래 반복)
          /geo audit <url>
          /geo brand <url>  (BASELINE 없을 때만)
          /geo realtime <url> [--cp] --track

Step 3  선별 도메인별 /geo tracker <도메인>

Step 4  종합 비교 요약 출력
```

### Step 간 진행 방식

각 Step 완료 시 한 줄 요약을 출력하고 즉시 다음 Step으로 진행한다.
Step 1에서 CRITICAL 항목이 발견되거나 Step 간 오류가 발생하면 중단하고 재시작 방법을 안내한다.

```
[Step 1 완료] GEO-감사-보고서.md 생성 — 종합 점수 52/100 (보통), CRITICAL 1건
  → CRITICAL: 순수 CSR 감지 — AI 크롤러가 콘텐츠를 볼 수 없는 상태입니다.
  → 계속 진행하시겠어요? (y/n):

[Step 2 완료] GEO-BRAND-BASELINE-20260509.json 생성 — Gap 등급 DISTANT
[Step 3 완료] GEO-REALTIME-example.com-20260509.md — 전체 인용률 38% (3개 플랫폼)
[Step 4 완료] GEO-TRACKER-example.com-20260509.md — 스냅샷 1회차 기록
```

### 종합 요약 출력 형식 (Step 5)

```
[ geo-code pipeline 완료 ]

도메인: example.com
실행 시간: 약 23분

분석 결과:
  GEO 감사 점수   52/100 (보통)
  Gap 등급        DISTANT
  실측 인용률     38% (Perplexity 50% / Google AIO 30% / Bing 50%)
  CRITICAL        1건 — 순수 CSR 감지

생성 파일:
  GEO-감사-보고서.md
  GEO-BRAND-BASELINE-20260509.json
  GEO-REALTIME-example.com-20260509.md
  GEO-TRACKER-example.com-20260509.md

다음 측정 예정: 2026-06-06 (4주 후)
권장 명령어: /geo-code pipeline https://example.com --cp --track
```

---

## `/geo-code status` — 상태 확인

`/geo-code status` 또는 `/geo-code status <도메인>`

현재 폴더와 Tunnel Framework 프로젝트를 동시에 점검한다.

### 확인 항목

**1. 분석 파일 현황**

```bash
ls -lt GEO-*.md GEO-*.json 2>/dev/null
```

파일명·생성일·크기를 표로 출력한다.

**2. BASELINE 현황**

```bash
ls GEO-BRAND-BASELINE-*.json 2>/dev/null | sort
```

존재하면: 파일 수, 마지막 측정일, 다음 측정 예정일(마지막 날짜 +28일), 스냅샷 수.
없으면: "아직 BASELINE이 없습니다. `/geo brand <url>`을 먼저 실행하세요."

**3. CP 연동 상태** (`<도메인>` 인수가 있을 때만)

```bash
TUNNEL="${GEO_TUNNEL_ROOT:?set GEO_TUNNEL_ROOT to your local 00_tunnel root}"
ls "$TUNNEL/10_projects/$DOMAIN/04_cp/topics.csv" 2>/dev/null
ls "$TUNNEL/10_projects/$DOMAIN/04_cp/contents/"*.md 2>/dev/null | wc -l
```

topics.csv 존재 여부, 완료 콘텐츠 수를 출력한다.

**4. 환경 간이 상태**

```bash
node --version 2>/dev/null && node -e "require('playwright')" 2>/dev/null && echo "ok"
```

Node.js·Playwright 설치 여부만 확인한다 (상세 점검은 `/geo-code init`).

### 출력 형식

```
[ geo-code status ]

분석 파일:
  GEO-감사-보고서.md               2026-05-09
  GEO-BRAND-BASELINE-20260509.json 2026-05-09  (스냅샷 2회)
  GEO-REALTIME-example.com-*.md    2026-05-09
  GEO-TRACKER-example.com-*.md     2026-05-09

BASELINE:
  마지막 측정: 2026-05-09
  다음 측정:   2026-06-06 (D-28)
  Gap 등급:    DISTANT → PARTIAL

CP 연동 (example.com):
  topics.csv   존재 (12개 주제, 8개 완료)
  완성 콘텐츠  8편

환경:
  Node.js / Playwright   설치됨
  (상세 점검은 /geo-code init)
```

---

## 오류 처리

| 상황 | 대응 |
|---|---|
| 환경 FAIL (init) | 해결 방법 안내 후 중단 — pipeline 실행 불가 |
| Step 1 CRITICAL 발견 | 경고 출력 후 계속 진행 여부 질의 |
| Step 간 오류 | 해당 Step 오류 내용 출력 + 단독 명령어로 재시작 안내 |
| BASELINE 없음 (Step 2) | 자동으로 /geo brand를 실행해 생성 후 계속 |
| topics.csv 없음 (--cp) | --cp 제거 후 기본 모드로 자동 전환 안내 |
| 도메인 20개 초과 (batch) | 앞 20개만 처리, 경고 출력 |

---

## 연동 스킬

| 스킬 | 호출 시점 |
|---|---|
| `geo-audit` | pipeline Step 1 |
| `geo-brand` | pipeline Step 2 (BASELINE 없을 때) |
| `geo-realtime` | pipeline Step 3 |
| `geo-tracker` | pipeline Step 4 |
| `geo-batch` | 복수 도메인 pipeline Step 1 |
