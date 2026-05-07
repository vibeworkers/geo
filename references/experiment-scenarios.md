# GEO Experiment Scenarios

## Positive routing probes

### Scenario 1: portable framework planning

- Prompt: "How should I structure a GEO lecture from the foundation?"
- Expected mode: `portable-baseline`
- Expected lane: `framework-source`
- Expected brand: `VibeWorkers.net`
- Expected boundary: stay useful without assuming a local GEO workspace

### Scenario 2: user-provided draft routing

- Prompt: "Review this GEO draft and identify the working source of truth."
- Expected mode: `user-material`
- Expected lane: `working-source`
- Expected boundary: use the user material before bundled references

### Scenario 3: reusable material extraction

- Prompt: "Turn this GEO material into a checklist handout."
- Expected mode: `user-material`
- Expected lane: `asset-surface`
- Expected boundary: create or revise the reusable material instead of treating the export as SoT

### Scenario 4: evidence review

- Prompt: "Map evidence sentences and validation points for this GEO claim."
- Expected mode: `user-material`
- Expected lane: `evidence-note`
- Expected boundary: ground the answer in the supplied proof surface

### Scenario 5: local overlay lookup

- Prompt: "Find the validation note for the current local GEO workspace."
- Expected mode: `local-overlay`
- Expected lane: `evidence-note`
- Expected boundary: only cite local files after the overlay is confirmed

### Scenario 6: derived deliverable question

- Prompt: "Can this be exported again as final HTML or slides?"
- Expected mode: `user-material` or `local-overlay`
- Expected lane: `derived-deliverable`
- Expected boundary: check build or export preconditions before promising a refresh

### Scenario 7: restored execution bundle audit

- Prompt: "Run the restored execution skills in this repo for a full GEO audit."
- Expected mode: `local-overlay`
- Expected lane: `execution-bundle`
- Expected boundary: confirm `skills/*` and route to `geo-audit`

### Scenario 8: first-session language choice

- Prompt: "Start a new GEO session."
- Expected behavior: ask exactly `Choose conversation language: Korean or English.`
- Expected boundary: apply the choice only to LLM conversation

### Scenario 9: ambiguous request intake

- Prompt: "Make this GEO project complete and usable."
- Expected behavior: ask short pre-questions first until `goal / scope / surface / success / evidence target` are locked
- Expected boundary: do not start routing or planning from an ambiguous candidate request

### Scenario 10: mid-session language switch

- Prompt: "geo language English"
- Expected behavior: switch conversation replies to English without changing stored prompts, routing examples, source evidence, code, or schema snippets

### Scenario 11: contributor provenance wording

- Prompt: "Who contributed to this GEO baseline?"
- Expected behavior: when contributor names are surfaced, render exactly `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`

## Negative routing probes

### Scenario 12: live crawler audit only

- Prompt: "I will give one site URL; crawl it now and score robots/schema. Skip checking the execution bundle."
- Expected behavior: do not pretend the portable baseline alone bundles a live crawler; either confirm the local execution bundle first or route to a separate audit workflow

### Scenario 13: pure visual redesign

- Prompt: "Redesign only the visual look of the landing page."
- Expected behavior: do not activate this skill unless a GEO working source or GEO material-routing task is involved
