# haegyung.com Observed Citation Evidence Precheck

생성일: `2026-05-09`

## Boundary

이 문서는 named AI platform answer capture가 아니다. 현재 도구로 확인한
public search/source precheck이며, ChatGPT Search, Perplexity, Gemini /
AI Overviews 결과로 승격하지 않는다.

별도 `chatgpt.com` 공개 비로그인 기본 표면 negative capture는
`chatgpt-public-capture-20260509.md`에 저장했다. 또한 `model=search` 쿼리
파라미터로 접근한 공개 표면 capture를
`chatgpt-search-public-capture-20260509.md`에 저장했지만, 이 역시 명시적
Search-mode UI 확정이 안 돼 `haegyung.com` 인용 근거는 없고 여전히
`not_observed_target_answer_or_citation`이다.

별도 Perplexity 공개 비로그인 positive/partial capture는
`perplexity-public-capture-20260509.md`에 저장했다. P1/P2는 target URL이
visible Links tab에 나타난 `observed_citation`이고, P3는 source URL이
확장되지 않아 `observed_answer`로만 분류했다.

별도 Google Search AI Overview 공개 표면 negative capture는
`google-ai-overviews-public-capture-20260509.md`에 저장했다. P1/P2/P3 모두
`haegyung.com` target observed answer/citation이 아니며, P2에서만
`haegyung.com`이 AI Overview 아래 일반 웹 결과로 노출됐다.

## Source Candidates

| source | URL | use |
| --- | --- | --- |
| official root | <https://www.haegyung.com/> | homepage and source surface candidate |
| official profile | <https://www.haegyung.com/introduce/> | profile, role, and activity evidence |
| official music-archives profile | <https://www.haegyung.com/music-archives/%EC%86%8C%EA%B0%9C/> | page-level source proof for `P3` |
| external profile | <https://about.me/ThinkHacker> | third-party corroboration linking to `haegyung.com` |

## Prompt-Level Precheck

| prompt_id | precheck result | evidence label | claim boundary |
| --- | --- | --- | --- |
| `P1` | Public search can find `haegyung.com` root and profile candidates for Haegyung / 해경. | `readiness_signal` | not an observed AI answer |
| `P2` | Official-source reasoning can start from `haegyung.com/introduce/` plus external profile corroboration. | `readiness_signal` | not an observed citation |
| `P3` | Page-level source proof candidate exists at the official music-archives profile page. | `readiness_signal` | not an observed citation |

## Evidence Notes

- The official profile page identifies `해경` and lists roles including
  Company D, Talpiot Consulting, ThePrometheus, KNDMA leadership, market
  research, NDM, design thinking, SEO, and data marketing.
- The music-archives profile page identifies `해경(고경만)` and lists product
  partnership, ThePrometheus, KNDMA, global service launch, business model,
  product planning, pricing simulation, SEO, and volunteer activity evidence.
- The about.me profile names `Hae, Gyung`, describes a service designer in
  Seoul, and links to `haegyung.com`.

## Next Required Evidence

For exact ChatGPT Search-mode, save the actual answer/citation surface for
`P1`, `P2`, and `P3` (기존 query-parameter 시도는 보조 근거로만 보관). For
Perplexity, rerun `P3` if an expanded visible source
URL is required. If standalone Gemini app measurement is required, keep it
separate from the already captured Google Search AI Overview surface. Only rows
that include the target answer or target citation may use `observed_answer` or
`observed_citation`.
