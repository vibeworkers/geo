---
name: geo-batch
description: >
  Claude Code 전용 확장 계층. 복수 도메인을 순차로 빠르게 GEO 스캔하여
  핵심 지표(HTTPS·AI 봇 접근·llms.txt·스키마·렌더링)를 비교 표로 출력한다.
  geo-prospect의 배치 확장판으로, 클라이언트 후보 목록·경쟁사 그룹·포트폴리오 점검에 활용한다.
  Claude 웹 환경에서 호출하면 안내 메시지를 출력하고 중단한다.
  트리거: "배치", "batch", "일괄 스캔", "여러 도메인 분석", "/geo batch".
audience: L3
allowed-tools: Read, Bash, WebFetch, Write
---

# geo-batch — 도메인 배치 스캔 (확장 계층)

> **Claude Code 전용:** Bash + WebFetch 병렬 처리가 필요하다.
> Claude 웹에서 호출하면 아래 메시지를 출력하고 중단한다.
>
> ```
> 이 기능은 Claude Code(터미널)에서만 실행할 수 있습니다.
> 웹 환경에서 복수 도메인을 순차 스캔하려면 /geo audit을 도메인별로 개별 실행하세요.
> ```

---

## 명령어

```
/geo batch <url1> <url2> ...          URL 직접 나열
/geo batch --file <path>              줄바꿈 구분 URL 목록 파일에서 읽기
/geo batch <url1> <url2> --full       간이 스캔 대신 geo-audit 수준 전체 스캔
```

| 옵션 | 설명 | 기본값 |
|---|---|---|
| `--file <path>` | URL 목록 파일 경로 (줄당 1개 URL) | 사용 안 함 |
| `--full` | 각 도메인에 /geo audit 수준 전체 스캔 실행 | 간이 스캔 |

도메인 수 상한: 20개 (초과 시 앞 20개만 처리하고 경고 출력).

---

## 실행 단계

### 1단계: URL 목록 수집

인수 또는 파일에서 URL을 수집하고 도메인을 추출한다.

```bash
# --file 옵션일 때
cat "$FILE_PATH" | grep -v '^#' | grep -v '^$' | head -20
```

각 URL에서 도메인 추출 (`https://` 제거, 경로 제거).  
중복 도메인이 있으면 첫 번째만 유지하고 경고를 출력한다.

---

### 2단계: 도메인별 간이 스캔

각 도메인에 대해 아래 8개 항목을 순차로 확인한다.  
`--full` 옵션이 있으면 각 도메인에 geo-audit 스킬을 호출한다.

| 항목 | 확인 방법 | 판정 기준 |
|---|---|---|
| HTTPS | URL 스킴 확인 | https → PASS / http → FAIL |
| AI 봇 접근 | `/robots.txt` 읽기 → GPTBot·ClaudeBot·PerplexityBot Disallow 여부 | 전체 허용 → PASS / 1개 이상 차단 → WARN / 전면 차단 → FAIL |
| llms.txt | `/llms.txt` 존재 여부 | 200 → PASS / 404 → FAIL |
| sitemap.xml | `/sitemap.xml` 존재 여부 | 200 → PASS / 없음 → WARN |
| Organization 스키마 | 홈페이지 `application/ld+json` 탐색 | 존재 → PASS / 없음 → FAIL |
| 렌더링 방식 | HTML body에 실제 텍스트 존재 여부 | SSR → PASS / CSR 의심 → WARN |
| 메타 description | `<meta name="description">` 존재 여부 | 존재 → PASS / 없음 → WARN |
| OG 태그 | `og:title` + `og:description` 존재 여부 | 둘 다 존재 → PASS / 하나라도 없음 → WARN |

**판정 기호:**

| 기호 | 의미 |
|---|---|
| PASS | 정상 |
| WARN | 개선 권고 |
| FAIL | 즉시 조치 필요 |
| ERR | 접근 실패 (타임아웃·403·연결 오류) |

항목당 타임아웃: 10초. 초과 시 ERR로 처리하고 다음 항목 진행.

---

### 3단계: 점수 산출

도메인별 FAIL 수와 WARN 수로 간이 GEO 점수를 계산한다.

```
간이 점수 = 100 - (FAIL 수 × 15) - (WARN 수 × 5)
최솟값: 0
```

점수 등급:

| 점수 | 등급 |
|---|---|
| 70 이상 | 양호 |
| 40–69 | 보통 |
| 39 이하 | 미흡 |

---

### 4단계: 비교 표 정렬 및 보고서 생성

점수 낮은 순(개선 필요도 높은 순)으로 정렬하여 보고서를 생성한다.  
파일명: `GEO-BATCH-[날짜].md`

---

## 출력 보고서 템플릿

```markdown
# GEO 배치 스캔 보고서

스캔일: [날짜]  |  도메인 수: [N]개  |  소요 시간: 약 [X]분

---

## 도메인별 비교

| 도메인 | 점수 | 등급 | HTTPS | AI봇 | llms.txt | 스키마 | 렌더링 | meta | OG |
|---|---|---|---|---|---|---|---|---|---|
| example.com | 70 | 양호 | PASS | PASS | FAIL | PASS | PASS | PASS | WARN |
| demo.com | 40 | 보통 | PASS | WARN | FAIL | FAIL | WARN | WARN | FAIL |

> PASS=✓  WARN=△  FAIL=✗  ERR=?

---

## 즉시 조치 필요 도메인

| 도메인 | FAIL 항목 | 권고 |
|---|---|---|
| [도메인] | AI봇 전면 차단, llms.txt 없음 | /geo audit으로 상세 분석 권고 |

---

## 다음 단계

점수 낮은 도메인부터 /geo audit으로 상세 분석을 진행하세요.

  /geo audit https://[가장 낮은 도메인]
```

---

## 오류 처리

| 상황 | 대응 |
|---|---|
| URL 목록 파일 없음 | 파일 경로 확인 안내 후 중단 |
| 도메인 20개 초과 | 앞 20개만 처리, 나머지 목록 경고 출력 |
| 전체 도메인 ERR | 네트워크 연결 확인 안내 |
| 단일 도메인 ERR | 해당 행 ERR 표시 후 다음 도메인 진행 |

---

## 연동 스킬

| 스킬 | 관계 |
|---|---|
| `geo-audit` | `--full` 옵션 또는 배치 결과 후속 상세 분석 |
| `geo-prospect` | 단일 도메인 빠른 스캔 (geo-batch의 단일 도메인 버전) |
