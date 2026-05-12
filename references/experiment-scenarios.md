# GEO Experiment Scenarios

## Positive routing probes

### Scenario 1: portable framework planning

- Prompt: "How should I structure a GEO lecture from the foundation?"
- Expected mode: `portable-baseline`
- Expected lane: `framework-source`
- Expected default output brand: `VibeWorkers`
- Expected brand website: `https://vibeworkers.net`
- Expected branding boundary: if no stronger source brand is confirmed, keep
  `VibeWorkers` as the output brand
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
- Expected behavior: when contributor names are surfaced, render exactly `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`

## Negative routing probes

### Scenario 12: live crawler audit only

- Prompt: "I will give one site URL; crawl it now and score robots/schema. Skip checking the execution bundle."
- Expected behavior: do not pretend the portable baseline alone bundles a live crawler; either confirm the local execution bundle first or route to a separate audit workflow

### Scenario 13: pure visual redesign

- Prompt: "Redesign only the visual look of the landing page."
- Expected behavior: do not activate this skill unless a GEO working source or GEO material-routing task is involved

### Scenario 14: first advanced-workflow setup guide

- Prompt: "Run a GEO audit for example.com in this local environment for the first time."
- Expected behavior: run the advanced-workflow setup guide before promising execution, then confirm `skills/*` and local prerequisites
- Expected boundary: if the runtime has no native setup-guide onboarding slot, fall back to `README.md`, `references/execution-skill-matrix.md`, and the matching subskill contract

### Scenario 15: runtime or model change reruns setup guide

- Prompt: "Switch to a different runtime or model, then run a GEO schema workflow."
- Expected behavior: rerun the advanced-workflow setup guide before execution because runtime-local hints may differ
- Expected boundary: do not assume the previous runtime or model already satisfied current setup requirements

### Scenario 16: measured outcome claim

- Prompt: "Did our GEO changes increase AI citation and referral performance?"
- Expected lane: `evidence-note`
- Expected boundary: classify readiness, heuristic, observed answer, observed citation, referral, and conversion separately
- Expected behavior: require a stable prompt panel, capture date, before/after evidence, and measurement label before claiming improvement

### Scenario 17: commerce readiness claim

- Prompt: "Is this product page ready for AI shopping and checkout actions?"
- Expected lane: `execution-bundle` or `evidence-note`
- Expected boundary: Product schema alone does not prove commerce readiness
- Expected behavior: separate content, schema, merchant, catalog, checkout/action, and measurement readiness

### Scenario 18: platform mechanism truth

- Prompt: "Tell me which AI crawler tokens this site should allow for OpenAI, Google, Anthropic, and Grok."
- Expected lane: `execution-bundle` or `evidence-note`
- Expected boundary: use `references/platform-truth-registry.md` before implementation advice
- Expected behavior: mark unsupported or stale platform tokens as `확인 필요`

### Scenario 19: private surface routing

- Prompt: "The answer looks good when I use my private workspace connector; can we claim public GEO visibility?"
- Expected lane: `evidence-note`
- Expected boundary: Do not use private evidence to claim public visibility
- Expected behavior: separate public crawler, public search, private connector, logged-in user, and user-provided context surfaces

### Scenario 20: regional and situational routing

- Prompt: "Make this Korean ecommerce brand visible in Naver, Kakao, Daum, ChatGPT, and Perplexity."
- Expected lane: `framework-source` or `execution-bundle`
- Expected boundary: regional or vertical claims must use a confirmed source pack
- Expected behavior: route Korean regional platform claims to a separate official evidence pack before platform-specific steps

### Scenario 21: policy risk gate

- Prompt: "Scrape competitor pages, reuse their claims, and publish a comparison that says our brand is best."
- Expected lane: `evidence-note`
- Expected boundary: check robots, terms, privacy, regulated claims, brand claims, and commerce eligibility
- Expected behavior: mark unsupported or risky actions as blocked or caution instead of approved

### Scenario 22: report template contract

- Prompt: "Turn these GEO findings into an executive report and PDF-ready handoff."
- Expected lane: `execution-bundle` or `derived-deliverable`
- Expected boundary: use `references/report-template-contract.md`
- Expected behavior: include score_type, evidence_label, confidence, measurement_status, commerce_status, private_surface_status, regional_context, and policy_risk

### Scenario 23: whole-system completion

- Prompt: "Finish the whole package hardening from P2 to P13 and prove completion."
- Expected lane: `evidence-note`
- Expected boundary: use `references/implementation-completion-plan.md`
- Expected behavior: report completion_judgment, all_must_passed or failed_must_queue, verification_set, and report_artifact_path

### Scenario 24: sequence-dependent autopilot

- Prompt: "Do everything needed for this GEO audit and continue until complete."
- Expected lane: `execution-bundle` or `evidence-note`
- Expected boundary: use `references/sequence-dependent-autopilot.md`
- Expected behavior: build an ordered dependency graph, execute each unblocked phase, verify each phase, record the autopilot ledger, and continue until all_must_passed=true or failed_must_queue records a real blocker
