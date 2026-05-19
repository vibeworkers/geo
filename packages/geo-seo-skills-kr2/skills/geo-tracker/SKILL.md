---
name: geo-tracker
description: >
  Claude Code 전용 확장 계층. 현재 폴더의 GEO-BRAND-BASELINE-*.json 파일을
  날짜순으로 읽어 5개 Gap 지표(포지셔닝 반영률·SOV·BCI·채널 인용률·맥락 일치율)와
  geo-realtime 실측 인용률의 시계열 변화를 추적한다.
  추이 분석(개선·정체·악화), 등급 변화, 다음 측정 권고를 제공한다.
  Claude 웹 환경에서 호출하면 안내 메시지를 출력하고 중단한다.
  트리거: "추적", "트래커", "tracker", "시계열", "gap 변화", "/geo tracker".
audience: L3
allowed-tools: Read, Bash, Write
---

# geo-tracker — Gap 시계열 추적 (확장 계층)

> **Claude Code 전용:** 로컬 BASELINE 파일 접근이 필요하다.
> Claude 웹에서 호출하면 아래 메시지를 출력하고 중단한다.
>
> ```
> 이 기능은 Claude Code(터미널)에서만 실행할 수 있습니다.
> 로컬 파일 시스템의 BASELINE 데이터가 필요하므로 웹 환경에서는 지원되지 않습니다.
> Claude Code를 실행한 후 동일 명령어를 다시 입력해 주세요.
> ```

---

## 명령어

```
/geo tracker <도메인>               전체 BASELINE 이력으로 시계열 보고서 생성
/geo tracker <도메인> --weeks <N>   최근 N주 데이터만 표시 (기본: 전체)
/geo tracker <도메인> --export      시계열 데이터를 CSV로 추가 저장
```

| 옵션 | 설명 | 기본값 |
|---|---|---|
| `--weeks <N>` | 최근 N주 범위로 제한 | 전체 이력 |
| `--export` | `GEO-TRACKER-[도메인]-[날짜].csv` 추가 저장 | 사용 안 함 |

---

## 실행 단계

### 1단계: BASELINE 파일 수집

현재 폴더에서 BASELINE 파일을 모두 찾아 날짜순으로 정렬한다.

```bash
ls GEO-BRAND-BASELINE-*.json 2>/dev/null | sort
```

파일이 없으면:
```
GEO-BRAND-BASELINE-*.json 파일을 찾을 수 없습니다.
먼저 /geo brand <url>을 실행하여 BASELINE을 생성하세요.
```

파일이 1개뿐이면:
```
BASELINE 파일이 1개입니다. 시계열 비교를 위해 최소 2개가 필요합니다.
4주 후 /geo brand <url> --track 또는 /geo realtime <url> --cp --track을
실행하면 두 번째 스냅샷이 기록됩니다.
현재 단일 스냅샷 현황만 출력합니다.
```

`--weeks N` 옵션이 있으면 오늘 기준 N주 이전 날짜보다 오래된 파일은 제외한다.

---

### 2단계: 데이터 추출

각 BASELINE JSON에서 지표를 추출하고 시계열 배열을 구성한다.

**추출 대상 필드:**

| 필드 | 설명 |
|---|---|
| `date` | 측정일 |
| `gap_grade` | INVISIBLE / DISTANT / PARTIAL / ALIGNED / ANCHORED |
| `positioning_reflection` | 포지셔닝 반영률 (0–100) |
| `sov` | 노출 점유율 (0–100) |
| `bci` | 단독 브랜드 인식 강도 (0–100) |
| `channel_citation` | 자사 채널 인용률 (0–100) |
| `context_match` | 맥락 일치율 (0–100) |
| `realtime_snapshots` | geo-realtime --track 기록 배열 (있을 경우) |

**realtime_snapshots 통합:**

`realtime_snapshots` 배열이 있으면 각 스냅샷에서 `overall_citation_rate`를 별도 추적한다.
BASELINE 지표와 동일 날짜면 같은 행에 표시, 다른 날짜면 별도 행으로 추가한다.

---

### 3단계: 추이 분석

수집된 시계열 데이터를 기반으로 아래 항목을 계산한다.

**지표별 변화:**

```
Δ값 = 최신 값 - 최초 값
Δ값(기간) = 최신 값 - 직전 값
추세 = Δ값(기간) > 0 → ↑ / < 0 → ↓ / = 0 → →
```

**등급 변화:**

Gap 등급 순서: INVISIBLE → DISTANT → PARTIAL → ALIGNED → ANCHORED

```
등급 변화 = 최신 등급 순위 - 최초 등급 순위
+1 이상 → 개선 / 0 → 정체 / -1 이하 → 악화
```

**트렌드 판정 기준:**

| 판정 | 기준 |
|---|---|
| 개선 중 | 최근 2개 스냅샷에서 종합 점수 +5 이상 |
| 정체 | 최근 2개 스냅샷 간 변화 ±4 이내 |
| 악화 | 최근 2개 스냅샷에서 종합 점수 -5 이하 |

종합 점수: 5개 지표 단순 평균.

---

### 4단계: 다음 측정 권고

마지막 BASELINE 날짜 기준 +28일(4주)을 다음 측정 예정일로 설정한다.
이미 지났으면 "측정 예정일이 지났습니다. 즉시 실행을 권장합니다."를 출력한다.

---

### 5단계: CSV 내보내기 (--export)

`--export` 옵션이 있으면 아래 형식으로 CSV를 추가 저장한다.

```csv
date,gap_grade,positioning_reflection,sov,bci,channel_citation,context_match,realtime_citation_rate
2026-05-07,DISTANT,32,18,24,0,44,
2026-06-04,PARTIAL,51,27,38,8,67,42
```

파일명: `GEO-TRACKER-[도메인]-[날짜].csv`

---

### 6단계: 보고서 생성

`GEO-TRACKER-[도메인]-[날짜].md`로 저장한다.

---

## 출력 보고서 템플릿

```markdown
# [브랜드명] Gap 시계열 추적 보고서

생성일: [날짜]  |  추적 기간: [최초 날짜] ~ [최신 날짜]  |  스냅샷: [N]회

---

## 현재 등급: [등급] ([최초 등급] → [최신 등급], [+N/-N]단계)

트렌드: [개선 중 / 정체 / 악화]

---

## 지표별 시계열

| 날짜 | 등급 | 포지셔닝 | SOV | BCI | 채널 인용 | 맥락 일치 | 실측 인용률 |
|---|---|---|---|---|---|---|---|
| [날짜] | DISTANT | 32 | 18 | 24 | 0 | 44 | — |
| [날짜] | PARTIAL | 51 | 27 | 38 | 8 | 67 | 42% |

---

## 지표별 변화 요약

| 지표 | 최초 | 최신 | 전체 변화 | 직전 대비 | 추세 |
|---|---|---|---|---|---|
| 포지셔닝 반영률 | 32 | 51 | +19 | +19 | ↑ |
| SOV | 18% | 27% | +9% | +9% | ↑ |
| BCI | 24 | 38 | +14 | +14 | ↑ |
| 채널 인용률 | 0% | 8% | +8% | +8% | ↑ |
| 맥락 일치율 | 44 | 67 | +23 | +23 | ↑ |
| 실측 인용률 | — | 42% | — | — | — |

---

## 개선된 Gap

[개선 확인된 항목 목록]

---

## 남은 Gap

[여전히 낮은 지표 + 권고 조치]

---

## 다음 측정 권고

다음 측정 예정일: [날짜]
권장 명령어:
  /geo brand https://[도메인] --track
  /geo realtime https://[도메인] --cp --track
```

---

## 오류 처리

| 상황 | 대응 |
|---|---|
| BASELINE 파일 없음 | `/geo brand` 먼저 실행 안내 후 중단 |
| 파일 1개 | 단일 스냅샷 현황 출력 + 다음 측정 안내 |
| JSON 파싱 실패 | 해당 파일 건너뜀 + 파일명 경고 출력 |
| 필드 누락 | 해당 지표 `—`으로 표시, 추이 계산 제외 |

---

## 연동 스킬

| 스킬 | 관계 |
|---|---|
| `geo-brand` | BASELINE 파일 생성 주체 (--track으로 갱신) |
| `geo-realtime` | realtime_snapshots 기록 주체 (--track 옵션) |
