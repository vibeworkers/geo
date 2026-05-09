# haegyung.com Observed Outcome Capture Scaffold

생성일: `2026-05-09`

## 목적

이 디렉터리는 `haegyung.com`의 readiness benchmark 이후 실제 AI 플랫폼
답변/인용 결과를 담기 위한 observed outcome lane이다.

현재 상태는 `public_search_precheck`까지다. ChatGPT Search, Perplexity,
Gemini / AI Overviews의 실제 답변 화면이나 citation surface는 아직 캡처하지
않았다. 따라서 이 디렉터리는 `beta 100/100`을 observed visibility claim으로
승격하지 않는다.

## 파일 인벤토리

- `capture-run-manifest.json`: run scope, prompt panel, pending platform matrix
- `observed-answer-captures.json`: pending named-platform rows and public search
  precheck rows
- `observed-citation-evidence.md`: public source and citation-candidate notes

## Claim Boundary

| lane | status | claim |
| --- | --- | --- |
| readiness | complete | `main 10/100`, `beta 100/100` readiness comparison |
| public search precheck | captured | official-source candidates and source-proof candidates exist |
| ChatGPT Search observed answer | pending | not measured |
| Perplexity observed citation | pending | not measured |
| Gemini / AI Overviews observed answer/citation | pending | not measured |
| referral / conversion | pending | not measured |

## Prompt Panel

Stored prompts remain English for cross-platform repeatability.

| prompt_id | prompt | intent | expected evidence |
| --- | --- | --- | --- |
| `P1` | `Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.` | entity discovery | `observed_answer`, official-site mention, citation path |
| `P2` | `Find the official website or official source for Haegyung (해경) and explain why you believe it is official.` | official-source retrieval | `observed_citation`, source reasoning, homepage inclusion |
| `P3` | `Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.` | source proof | `observed_citation`, page-level source inclusion |

## Next Capture Rule

The next operator should run `P1` to `P3` on each named platform and save:

- exact platform name and access profile
- region and language state
- answer snapshot or screenshot/export pointer
- visible source/citation URL
- evidence label from `references/measurement-loop.md`

Only rows with saved answer or citation evidence may be labeled
`observed_answer` or `observed_citation`.
