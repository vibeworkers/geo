# GEO Benchmark Process Remediation Checklist

생성일: `2026-05-09`

## 목적

이 문서는 `2026-05-08-haegyung-main-vs-beta` 벤치마크의 **평가 결과 해석**이
아니라 **생성 과정 품질**을 점검하고, 현재 보존본에 적용한 즉시 보정과 다음
런의 필수 개선 항목을 고정한다.

## 현재 판정

### 이미 잘된 점

- readiness와 observed outcome claim boundary를 분리했다.
- per-target report, all-function report, source JSON으로 evidence surface를
  분해했다.
- report metadata에 `score_type`, `measurement_status`, `policy_risk`를 남겼다.

### 실제 process 오류

1. **정규화 간극**
   - 초기 probe는 `beta` commit 직전에 수행됐고, 보존본은 같은 readiness
     surface가 `beta@2d896ac`로 고정됐다고 설명한다.
   - 동일 surface라는 해석은 가능하지만, strict benchmark 재현성 기준에서는
     `measured target`과 `reported target`이 완전히 일치하지 않는다.

2. **evidence inventory drift**
   - 이전 `per-target-reports/README.md`는
     `not-versioned/haegyung-desktop.png`,
     `not-versioned/haegyung-mobile.png`를 근거 파일로 적었지만,
     versioned evidence pack에는 해당 파일이 없다.
   - screenshot을 커밋하지 않는 정책 자체는 허용 가능하지만, 보존본 inventory는
     실제 존재하는 evidence만 가리켜야 한다.

### 개선점은 있지만 즉시 오류로 보긴 어려운 항목

1. benchmark builder 또는 run manifest가 없다.
2. `data/comparison.json`에 branch readiness와 live site snapshot이 함께 있다.
3. binary equal-weight criterion은 readiness gate로는 충분하지만 process
   sensitivity는 낮다.

## 이번 보존본에 즉시 적용한 보정

- `per-target-reports/README.md`에서 존재하지 않는 screenshot path를 제거한다.
- `per-target-reports/02-beta.GEO-종합보고서.md`의 시각 증거 문구를 현재
  versioned evidence pack 기준으로 정정한다.
- screenshot은 임시 실행 산출물이었고, versioned pack에는 JSON/Markdown 값만
  남겼다는 점을 명시한다.
- 현재 보존본 기준으로 채울 수 있는 값만 담은 provisional `run-manifest.json`
  을 추가한다.
- `data/comparison.json`을 대체하지 않고, 감사용 파생 파일
  `data/branch-readiness.json`과 `data/site-http-head-snapshot.json`을
  추가한다.
- `scripts/rebuild_geo_benchmark_pack.py`로 source/provenance artifact와
  report surface를 fresh output dir에 replay할 수 있게 한다.
- root benchmark `README.md`에 process audit 경로를 추가한다.

## 다음 런 필수 체크리스트

### A. 대상 고정

- probe 시작 전에 비교 대상 branch와 commit SHA를 고정한다.
- clean worktree 여부와 worktree root를 함께 기록한다.
- 측정 후 commit을 바꿔서 동일 surface라고 해석해야 하는 상황이면,
  동일성 추정으로 닫지 말고 clean replay를 다시 수행한다.

### B. provenance 저장

아래 필드를 run manifest로 남긴다.

시작 포맷은 `run-manifest.template.json`을 사용한다.

- `run_id`
- `captured_at`
- `operator`
- `cwd`
- `branch`
- `rev`
- `clean_worktree`
- `commands`
- `tool_versions`
- `output_paths`
- `normalization_note`

### C. evidence inventory 규칙

- versioned evidence pack에는 실제 커밋된 파일만 inventory에 적는다.
- 임시 screenshot, 대용량 capture, 비버전 산출물은 `optional ephemeral evidence`
  로 별도 표기한다.
- 임시 산출물을 삭제하거나 커밋하지 않을 경우, 최소한 해시, 경로, 생성 시각,
  대체 보존 근거를 남긴다.

### D. 데이터 분리

가능하면 아래처럼 파일을 분리한다.

- `branch-readiness.json`
- `site-http-head-snapshot.json`
- `browser-performance.json`
- `run-manifest.json`

이렇게 하면 package surface evidence와 live site evidence의 경계를 더 쉽게
감사할 수 있다.

재생성 경로는 `python3 scripts/derive_benchmark_audit_views.py <.../data/comparison.json>`
처럼 고정한다.

전체 pack replay 경로는
`python3 scripts/rebuild_geo_benchmark_pack.py reports/benchmarks/2026-05-08-haegyung-main-vs-beta --output-dir <target-dir>`
처럼 고정한다.

### E. scoring lane 분리

- 현재 binary readiness gate는 유지 가능하다.
- 단, 다음 단계에서는 `readiness lane`과 `observed outcome lane`을 별도
  artifact로 유지한다.
- headline summary는 measured capture가 생기기 전까지 readiness만 표기한다.

## Close Rule

다음 benchmark run은 아래가 모두 충족될 때만 process-healthy로 본다.

- measured target과 reported target이 일치한다.
- inventory에 적힌 evidence file이 실제로 존재한다.
- run manifest가 있다.
- readiness와 observed outcome lane이 분리된다.
- normalization이 필요하면 clean replay 또는 provisional label이 있다.
