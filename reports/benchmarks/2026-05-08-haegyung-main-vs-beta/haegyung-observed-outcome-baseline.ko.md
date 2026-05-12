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
| measurement_status | `partial positive observed capture with Google AI Overview and ChatGPT query-parameter negative capture` |
| commerce_status | `not applicable` |
| private_surface_status | `public only` |
| regional_context | `named language: ko-KR; stored prompts: English` |
| policy_risk | `caution` |

## 1. Executive Conclusion

`beta 100/100`은 readiness 결과로만 유효하다. `haegyung.com`의 observed
outcome lane은 `chatgpt.com` 공개 비로그인 기본 표면에서 negative capture
1세트, `chatgpt.com` query-parameter 탐색 표면에서 non-confirmed negative 1세트,
Perplexity 공개 비로그인 표면에서 partial positive capture 1세트,
Google Search AI Overview 공개 표면에서 negative capture 1세트를 얻었다.

이 기준선은 두 레인을 분리해 유지한다.

- readiness lane: `main 10/100`, `beta 100/100`
- observed outcome lane: `Perplexity P1/P2 observed citation`, `Perplexity P3
  observed answer only`, `ChatGPT public default negative`, `ChatGPT Search
  query-parameter negative`, `Google AI Overviews public negative`, exact ChatGPT
  Search still pending

target-positive capture는 생겼지만, 아직 cross-platform headline score를
발행하지 않는다. exact ChatGPT Search-mode가 남아 있고, 현재는 query-parameter
시도만으로 non-confirmed negative를 받았다. referral/conversion evidence도
없다. standalone Gemini app을 Google Search AI Overview와 분리해야 한다면 별도
surface로 추가 측정해야 한다.

## 2. Scope And Evidence

이 문서는 기존 public benchmark bundle을 source surface로 사용한다. measured
Perplexity public surface의 measured answer inclusion과 P1/P2 citation은
주장할 수 있다. 다만 cross-platform AI visibility, referral, conversion은
아직 주장하지 않는다. `chatgpt-public-capture-20260509.md`는 measured
platform probe지만 wrong-entity/target-absent 결과이므로 positive observed
claim이 아니다.

근거 앵커:

- `GEO-benchmark-report-main-vs-beta.ko.md` defines the current branch score as
  readiness rather than real AI-search performance.
- `data/branch-readiness.json` shows that `beta` reached `100/100` by expanding
  the contract and reference surface.
- `references/measurement-loop.md` defines the evidence ladder from
  `readiness_signal` to `conversion_signal`.
- `references/measurement-capture-template.md` defines the required Prompt
  Panel, Run Metadata, Capture Table, and Before/After Comparison.
- `observed-outcomes/chatgpt-search-public-capture-20260509.md` records a
  non-confirmed `model=search` negative probe.
- `observed-outcomes/perplexity-public-capture-20260509.md` records the first
  target-positive observed platform rows.
- `observed-outcomes/google-ai-overviews-public-capture-20260509.md` records a
  negative public Google Search AI Overview row set.

## 3. Platform Truth And Access Profile

Observed outcome 점검은 public surface부터 시작해야 한다.

| platform | default access_profile | target evidence | notes |
| --- | --- | --- | --- |
| ChatGPT Search | `public` or `logged-in` | `observed_answer`, `observed_citation` | Record account state because result composition can vary. |
| Perplexity | `public` or `logged-in` | `observed_citation` | Capture visible source URLs, not only answer text. |
| Google AI Overviews | `public browser` | `observed_answer`, `observed_citation` | Public Search AI Overview captured negative; region and trigger volatility must be recorded. |

후속 run이 private connector, internal analytics, account-only surface를
사용하면 evidence를 `public only` 상태 밖으로 분리하고 별도 label로
기록해야 한다.

## 4. Measurement Status

현재 상태는 `partial positive observed capture with Google AI Overview and query-parameter
negative capture`다. Perplexity P1/P2는 `observed_citation`, P3는
`observed_answer`로만 분류한다. ChatGPT `model=search` 시도는
`mode confirmation not captured` 조건이 붙은 negative이며 target-negative이다.
Google AI Overview P1/P2/P3는 모두 target-negative이므로 positive
observed label을 붙이지 않는다.

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

- baseline capture: exact `ChatGPT Search`, `Perplexity`, `Google AI Overviews`
- prompts per platform: `P1`, `P2`, `P3`
- optional delta prompt after content or structure changes: `P4`
- minimum baseline matrix: `3 platforms x 3 prompts = 9 captured runs`; after
  this capture, exact ChatGPT Search-mode is the remaining baseline gap

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

남은 named-platform capture가 닫히기 전까지 안전한 summary format은 아래와
같다.

- `readiness`: `main 10/100`, `beta 100/100`
- `observed outcome`: `Perplexity public P1/P2 observed citation; Perplexity P3
  observed answer only; ChatGPT public default negative; ChatGPT Search
  query-parameter negative (mode unconfirmed); Google AI Overviews public negative;
  exact ChatGPT Search pending`

위험한 summary 예시는 아래와 같다.

- `beta GEO performance is 100/100`
- `beta proved AI answer dominance`
- `beta achieved citation visibility`

이 주장은 현재 bundle에 없는 measured evidence를 요구한다.

## 8. Prioritized Verification Plan

1. Capture `P1` to `P3` on exact `ChatGPT Search` and save answer plus
   citation evidence.
2. Rerun Perplexity `P3` only if the expanded visible source URL is required.
3. If needed, capture standalone Gemini app separately from Google Search AI
   Overview and keep it as a distinct surface.
4. Classify each target-positive row as `observed_answer` or
   `observed_citation`; keep wrong-entity rows outside positive observed
   labels.
5. Only after answer/citation capture exists, attach referral or conversion
   evidence from analytics or commerce systems.

## 9. Remaining Gaps And Next Verification

현재 갭:

- target-positive Perplexity `observed_answer` exists for P1/P2/P3
- target-positive Perplexity `observed_citation` exists for P1/P2
- Perplexity P3 still needs expanded visible URL if it must be upgraded from
  `observed_answer` to `observed_citation`
- exact ChatGPT Search-mode capture remains pending; public default ChatGPT
  captured `P1` to `P3` as wrong-entity/target-absent negative evidence
- query-parameter capture is recorded in
  `observed-outcomes/chatgpt-search-public-capture-20260509.md` and remains
  non-confirmed mode
- Google AI Overviews public captured `P1` to `P3` as wrong-entity,
  ambiguous-entity, or target-absent negative evidence
- no referral log
- no conversion signal
- initial scaffold and public-source precheck:
  `observed-outcomes/README.md`
- public default ChatGPT negative capture:
  `observed-outcomes/chatgpt-public-capture-20260509.md`
- query-parameter (non-confirmed mode) ChatGPT Search capture:
  `observed-outcomes/chatgpt-search-public-capture-20260509.md`
- Perplexity public partial positive capture:
  `observed-outcomes/perplexity-public-capture-20260509.md`
- Google AI Overviews public negative capture:
  `observed-outcomes/google-ai-overviews-public-capture-20260509.md`

다음 검증은 `observed-outcomes/observed-answer-captures.json`의 pending
matrix에 exact ChatGPT Search 실제 답변 및 visible citation을 채우고, 필요하면
Perplexity P3 source URL을 확장하는 데 초점을 둬야 한다.
