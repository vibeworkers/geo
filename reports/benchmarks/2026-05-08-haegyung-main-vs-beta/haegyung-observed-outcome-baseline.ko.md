# haegyung.com Observed Outcome 기준선

## Report Metadata

| field | value |
| --- | --- |
| report_id | `haegyung-observed-outcome-baseline-20260509` |
| generated_at | `2026-05-09` |
| scope | `https://haegyung.com` observed outcome lane baseline for `main@a652637` and `beta@2d896ac` |
| score_type | `readiness` |
| evidence_label | `readiness_signal` |
| confidence | `high` |
| evidence_path | `GEO-benchmark-report-main-vs-beta.ko.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `references/measurement-loop.md`, `references/measurement-capture-template.md`, `references/report-template-contract.md` |
| last_verified | `2026-05-09` |
| measurement_status | `ready to measure` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR; stored prompts: English` |
| policy_risk | `caution` |

## 1. Executive Conclusion

`beta 100/100`은 readiness 결과로만 유효하다. `haegyung.com`의 observed
outcome lane은 아직 측정되지 않았다.

이 기준선은 두 레인을 분리해 유지한다.

- readiness lane: `main 10/100`, `beta 100/100`
- observed outcome lane: `main not measured`, `beta not measured`

최소 1개의 `observed_answer` 또는 `observed_citation` capture artifact가
생기기 전까지는 통합 headline score를 발행하지 않는다.

## 2. Scope And Evidence

이 문서는 기존 public benchmark bundle을 source surface로 사용한다. measured
AI answer inclusion, measured citation, referral, conversion은 아직 주장하지
않는다.

근거 앵커:

- `GEO-benchmark-report-main-vs-beta.ko.md` defines the current branch score as
  readiness rather than real AI-search performance.
- `data/branch-readiness.json` shows that `beta` reached `100/100` by expanding
  the contract and reference surface.
- `references/measurement-loop.md` defines the evidence ladder from
  `readiness_signal` to `conversion_signal`.
- `references/measurement-capture-template.md` defines the required Prompt
  Panel, Run Metadata, Capture Table, and Before/After Comparison.

## 3. Platform Truth And Access Profile

Observed outcome 점검은 public surface부터 시작해야 한다.

| platform | default access_profile | target evidence | notes |
| --- | --- | --- | --- |
| ChatGPT Search | `public` or `logged-in` | `observed_answer`, `observed_citation` | Record account state because result composition can vary. |
| Perplexity | `public` or `logged-in` | `observed_citation` | Capture visible source URLs, not only answer text. |
| Gemini / AI Overviews | `public browser` | `observed_answer`, `observed_citation` | Region and trigger volatility must be recorded. |

후속 run이 private connector, internal analytics, account-only surface를
사용하면 evidence를 `public only` 상태 밖으로 분리하고 별도 label로
기록해야 한다.

## 4. Measurement Status

현재 상태는 `observed`가 아니라 `ready to measure`다.

첫 measured lane은 commerce panel이 아니라 entity-discovery 및 source-proof
panel로 시작해야 한다. 현재 public evidence만으로는 `haegyung.com`을
checkout-oriented surface로 확정할 수 없기 때문이다.

### Prompt Panel

Stored prompt는 플랫폼 간 재실행 안정성을 위해 영어로 유지한다.

| prompt_id | Prompt | intent | expected evidence |
| --- | --- | --- | --- |
| `P1` | `Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.` | entity discovery | `observed_answer`, official-site mention, citation path |
| `P2` | `Find the official website or official source for Haegyung (해경) and explain why you believe it is official.` | official-source retrieval | `observed_citation`, source reasoning, homepage inclusion |
| `P3` | `Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.` | source proof | `observed_citation`, page-level source inclusion |
| `P4` | `What changed on Haegyung (해경)'s official website since the last crawl or content update? If uncertain, say so and cite the source you used.` | before/after delta | answer delta, citation path, uncertainty handling |

### Minimum Run Set

- baseline capture: `ChatGPT Search`, `Perplexity`, `Gemini / AI Overviews`
- prompts per platform: `P1`, `P2`, `P3`
- optional delta prompt after content or structure changes: `P4`
- minimum baseline matrix: `3 platforms x 3 prompts = 9 captured runs`

## 5. Run Metadata And Capture Table Requirements

모든 run은 measurement template의 아래 필드를 보존해야 한다.

- `run_id`
- `captured_at`
- `platform`
- `access_profile`
- `region_language`
- `prompt_id`
- `prompt_text`
- `answer_snapshot`
- `evidence_label`
- `confidence`
- `evidence_path`

각 captured run에 answer snapshot과 portable evidence path가 모두 있어야
measured lane이 열린다.

## 6. Before/After Comparison Rule

모든 GEO 변경 전후에 같은 prompt panel을 사용한다. 아래 필드는 하나의
headline으로 뭉치지 말고 분리해서 비교한다.

- observed answer inclusion
- observed citation
- referral signal
- conversion signal

rerun window가 recrawl 또는 platform refresh를 반영하기에 너무 짧으면,
결과는 `readiness` 또는 `heuristic` 상태에 머물러야 한다.

## 7. Headline Guard

observed capture가 생기기 전까지 안전한 summary format은 아래와 같다.

- `readiness`: `main 10/100`, `beta 100/100`
- `observed outcome`: `not measured`

위험한 summary 예시는 아래와 같다.

- `beta GEO performance is 100/100`
- `beta proved AI answer dominance`
- `beta achieved citation visibility`

이 주장은 현재 bundle에 없는 measured evidence를 요구한다.

## 8. Prioritized Verification Plan

1. Capture `P1` to `P3` on `ChatGPT Search` and save answer plus citation
   evidence.
2. Capture the same panel on `Perplexity` and preserve visible source URLs.
3. Capture the same panel on `Gemini / AI Overviews` with region noted.
4. Classify each row as `readiness_signal`, `observed_answer`, or
   `observed_citation`.
5. Only after answer/citation capture exists, attach referral or conversion
   evidence from analytics or commerce systems.

## 9. Remaining Gaps And Next Verification

현재 갭:

- no named AI platform `observed_answer` capture
- no named AI platform `observed_citation` capture
- no referral log
- no conversion signal
- initial scaffold and public-source precheck:
  `observed-outcomes/README.md`

다음 검증은 `observed-outcomes/observed-answer-captures.json`의 pending
matrix에 ChatGPT Search, Perplexity, Gemini / AI Overviews 실제 답변과
visible citation을 채워 observed lane을 `ready to measure`에서
`observed_answer` 또는 `observed_citation`으로 이동시키는 데 초점을 둬야
한다.
