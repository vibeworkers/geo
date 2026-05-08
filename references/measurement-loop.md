# GEO Measurement Loop

Use this reference when a GEO claim moves beyond readiness scoring into
observed answer, citation, referral, or conversion evidence.

The core rule is: do not claim measured visibility, measured citation, measured
traffic, or measured conversion from crawler, schema, `llms.txt`, or content
readiness signals alone.

## Evidence Ladder

| Label | Meaning | Required evidence | Claim boundary |
| --- | --- | --- | --- |
| `readiness_signal` | the site appears prepared for discovery, crawling, extraction, or citation | file review, HTTP result, schema validation, content review, or crawler-access evidence | may support readiness or gap claims only |
| `heuristic_signal` | an indirect proxy such as `llms.txt`, scorecard weight, or platform-readiness checklist | captured config plus adoption caveat | may support prioritization, not actual platform ingestion |
| `observed_answer` | a tested AI answer includes the brand, entity, product, or target page | prompt panel, platform, timestamp, locale/account state when available, and answer capture | observed for that prompt run only |
| `observed_citation` | a tested AI answer cites a target URL or source | answer capture plus visible citation/source URL | observed citation only, not durable ranking |
| `referral_signal` | users or bots arrived from a measurable AI or search surface | analytics export, server log, referrer, UTM, or search-console-like report | traffic signal only, not conversion |
| `conversion_signal` | a downstream action happened after an AI/search discovery path | order, lead, checkout, CRM, or analytics event tied to the path | action outcome for the measured period only |

## Minimum Measurement Workflow

1. Freeze the scope: brand, entity, URL set, product set, market, language, and
   target platforms.
2. Build a prompt panel before changes. Store prompts in English unless a
   specific market-language test is part of the scenario.
3. Capture baseline runs: platform, date, prompt, answer, citation/source
   surfaces, and visible uncertainty.
4. Classify each result with the evidence ladder above.
5. Apply the GEO remediation or content/schema/crawler change.
6. Run the same prompt panel again after an appropriate recrawl or refresh
   window.
7. Compare before/after with separated fields for answer presence, citation
   presence, referral, and conversion.
8. Report confidence explicitly: `readiness only`, `observed answer`,
   `observed citation`, `referral`, or `conversion`.

## Reporting Contract

Every measured GEO claim should state:

- platform and surface tested
- prompt panel or query set
- capture date
- entity, URL, product, or page set
- evidence ladder label
- before/after status when a remediation was tested
- unresolved caveats, including personalization, geography, account state,
  index freshness, and platform volatility

Use `references/measurement-capture-template.md` when the claim needs a
repeatable Prompt Panel, Run Metadata, Capture Table, or Before/After
Comparison artifact.

## Failure Modes

- Treating a score improvement as measured AI visibility.
- Treating `llms.txt` as guaranteed ingestion or citation.
- Treating schema validity as proof of AI shopping or transaction eligibility.
- Reporting one platform result as a cross-platform truth.
- Comparing before/after without a stable prompt panel or capture method.

## Source Anchors

These public documentation families inform the separation between crawling,
answering, citation, shopping, and action surfaces:

- OpenAI crawler documentation: <https://developers.openai.com/api/docs/bots>
- OpenAI Commerce documentation: <https://developers.openai.com/commerce>
- ChatGPT shopping research help: <https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt>
- Google crawler documentation: <https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers>
- Google merchant listing structured data: <https://developers.google.com/search/docs/appearance/structured-data/merchant-listing>
- Anthropic crawler documentation: <https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler>
- Anthropic web search tool documentation: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool>
- Perplexity Instant Buy help: <https://www.perplexity.ai/help-center/en/articles/10352906-what-is-instant-buy>
