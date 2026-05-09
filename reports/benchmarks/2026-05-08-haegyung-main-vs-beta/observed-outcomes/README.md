# haegyung.com Observed Outcome Capture Scaffold

생성일: `2026-05-09`

## 목적

이 디렉터리는 `haegyung.com`의 readiness benchmark 이후 실제 AI 플랫폼
답변/인용 결과를 담기 위한 observed outcome lane이다.

현재 상태는 `public_search_precheck`, `chatgpt.com` 공개 비로그인 기본 표면의
negative capture, Perplexity 공개 비로그인 표면의 partial positive capture,
그리고 Google Search AI Overview 공개 표면의 negative capture까지다. ChatGPT
capture는 명시적 ChatGPT Search-mode로 확정되지 않았고, `haegyung.com`
target observed answer/citation도 아니다. Perplexity capture는 P1/P2에서
target-positive observed citation을 보였지만, Google AI Overview는 P1/P2/P3
모두 target-negative였다. 따라서 이 디렉터리는 `beta 100/100`을
cross-platform observed visibility claim으로 승격하지 않는다.

## 파일 인벤토리

- `capture-run-manifest.json`: run scope, prompt panel, pending platform matrix
- `observed-answer-captures.json`: pending named-platform rows and public search
  precheck rows
- `observed-citation-evidence.md`: public source and citation-candidate notes
- `chatgpt-public-capture-20260509.md`: public logged-out ChatGPT default-chat
  negative capture for `P1` to `P3`
- `perplexity-public-capture-20260509.md`: public logged-out Perplexity partial
  positive capture for `P1` to `P3`
- `google-ai-overviews-public-capture-20260509.md`: public Google Search AI
  Overview negative capture for `P1` to `P3`

## Claim Boundary

| lane | status | claim |
| --- | --- | --- |
| readiness | complete | `main 10/100`, `beta 100/100` readiness comparison |
| public search precheck | captured | official-source candidates and source-proof candidates exist |
| ChatGPT public default answer | captured negative | target not identified; non-target sources cited |
| ChatGPT Search observed answer | pending | exact Search-mode surface not measured |
| Perplexity observed answer/citation | captured partial positive | P1/P2 observed citation; P3 observed answer only |
| Google AI Overviews observed answer/citation | captured negative | target not identified; non-target sources cited |
| standalone Gemini app observed answer/citation | not in baseline matrix | separate run needed only if this is split from AI Overviews |
| referral / conversion | pending | not measured |

## Prompt Panel

Stored prompts remain English for cross-platform repeatability.

| prompt_id | prompt | intent | expected evidence |
| --- | --- | --- | --- |
| `P1` | `Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.` | entity discovery | `observed_answer`, official-site mention, citation path |
| `P2` | `Find the official website or official source for Haegyung (해경) and explain why you believe it is official.` | official-source retrieval | `observed_citation`, source reasoning, homepage inclusion |
| `P3` | `Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.` | source proof | `observed_citation`, page-level source inclusion |

## Next Capture Rule

The next operator should run `P1` to `P3` on exact ChatGPT Search-mode, and may
rerun Perplexity P3 to expand the hidden source URL. If the standalone Gemini
app must be separated from Google Search AI Overview, record it as a distinct
surface. Save:

- exact platform name and access profile
- region and language state
- answer snapshot or screenshot/export pointer
- visible source/citation URL
- evidence label from `references/measurement-loop.md`

Only rows with saved target-positive answer or target citation evidence may be
labeled `observed_answer` or `observed_citation`.
