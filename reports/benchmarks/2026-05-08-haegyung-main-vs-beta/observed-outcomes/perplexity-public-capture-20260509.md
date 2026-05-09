# Perplexity Public Capture - Haegyung Observed Outcome

Captured at: `2026-05-09T13:35:00Z`

## Boundary

This is a public logged-out Perplexity web capture. Answers were visible without
sign-in. A sign-up dialog appeared after the `P3` run, so the `P3` source URL
could not be expanded from the visible link label in this capture.

## Run Metadata

| field | value |
| --- | --- |
| platform_surface | `perplexity.ai` public search |
| access_profile | `public logged-out` |
| capture_method | Firecrawl isolated browser session accessibility snapshot |
| session_state | Browser session destroyed after capture |
| ui_language | English |
| prompt_language | English prompt with Korean alias `해경` |
| target_entity | Haegyung / 해경 at `https://haegyung.com` |

## Prompt Results

| prompt_id | target outcome | visible source URL status | evidence label | note |
| --- | --- | --- | --- | --- |
| `P1` | target identified | `https://www.haegyung.com/introduce/` visible in Links tab | `observed_citation` | Answer described Haegyung / 해경 as a Korean professional/creator and cited `haegyung.com`. |
| `P2` | target official-source candidate identified | `https://www.haegyung.com` visible in Links tab | `observed_citation` | Answer treated `haegyung.com` as the official-looking source, with an explicit caveat that independent registry proof was not found. |
| `P3` | target source link visible, URL not expanded | link labels `해경` / `haegyung` visible, URL hidden by modal state | `observed_answer` | Answer pointed to the official site and summarized the homepage snippet, but this capture does not prove a visible target URL for `observed_citation`. |

### P1

Prompt: `Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.`

Observed outcome: target-positive. The answer identified Haegyung / 해경 as a
Korean professional/creator, cited `haegyung.com` in the answer, and the Links
tab showed `https://www.haegyung.com/introduce/`.

### P2

Prompt: `Find the official website or official source for Haegyung (해경) and explain why you believe it is official.`

Observed outcome: target-positive with caveat. The answer identified
`haegyung.com` as the best official-looking source and explicitly caveated that
it did not find independent registry or contact-page proof. The Links tab showed
`https://www.haegyung.com`.

### P3

Prompt: `Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.`

Observed outcome: target answer present, citation URL not fully expanded. The
answer pointed to Haegyung's official site and summarized the homepage snippet
about "낮이건 밤이건 우리의 길을 비추는 존재를 빚어간다." The visible answer showed
linked labels `해경` / `haegyung`, but the sign-up modal prevented a confirmed
Links-tab URL capture for this row.

## Interpretation

Perplexity public search gives the first target-positive observed platform
evidence in this benchmark bundle. `P1` and `P2` can be treated as
`observed_citation` rows for the captured run. `P3` should remain
`observed_answer` only until the source URL is expanded in a repeat capture.
