# GEO Experiment Scenarios

## Positive routing probes

### Scenario 1: portable framework planning

- Prompt: "GEO 강의 구조를 어떻게 짜야 할지 기본 틀부터 잡아줘."
- Expected mode: `portable-baseline`
- Expected lane: `framework-source`
- Expected brand: `Vibeworkers.net`
- Expected boundary: stay useful without assuming a local GEO workspace

### Scenario 2: user-provided draft routing

- Prompt: "이 GEO 초안에서 어느 문서가 실제 작업 정본이 되어야 하는지 정리해줘."
- Expected mode: `user-material`
- Expected lane: `working-source`
- Expected boundary: use the user material before bundled references

### Scenario 3: reusable material extraction

- Prompt: "이 GEO 내용을 체크리스트 핸드아웃으로 바꿔줘."
- Expected mode: `user-material`
- Expected lane: `asset-surface`
- Expected boundary: create or revise the reusable material instead of treating the export as SoT

### Scenario 4: evidence review

- Prompt: "이 GEO 주장에 대한 근거 문장과 검증 포인트를 정리해줘."
- Expected mode: `user-material`
- Expected lane: `evidence-note`
- Expected boundary: ground the answer in the supplied proof surface

### Scenario 5: local overlay lookup

- Prompt: "현재 로컬 GEO 작업물 기준으로 검증 노트가 어디에 있는지 찾아줘."
- Expected mode: `local-overlay`
- Expected lane: `evidence-note`
- Expected boundary: only cite local files after the overlay is confirmed

### Scenario 6: derived deliverable question

- Prompt: "최종 HTML이나 슬라이드로 다시 내보낼 수 있나?"
- Expected mode: `user-material` or `local-overlay`
- Expected lane: `derived-deliverable`
- Expected boundary: check build or export preconditions before promising a refresh

## Negative routing probes

### Scenario 7: live crawler audit only

- Prompt: "사이트 URL 하나 줄게, 지금 크롤링해서 robots/schema 점수만 내줘."
- Expected behavior: do not pretend this skill bundles a live crawler; request source material or route to a separate audit workflow

### Scenario 8: pure visual redesign

- Prompt: "랜딩 페이지 비주얼만 다시 그려줘."
- Expected behavior: do not activate this skill unless a GEO working source or GEO material-routing task is involved
