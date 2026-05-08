# GEO Platform Truth Registry

This registry is the package-level source map for platform, crawler, and
commerce-surface claims. It does not replace official documentation. It records
which packaged GEO guidance is safe to state, which claims are only heuristic /
adoption-dependent, and which claims require fresh verification before use.

## Registry Contract

Every platform claim used by `geo` reports should carry:

- `source_url`
- `last_verified`
- `confidence`
- `control_scope`
- `package_action`

If a platform token or crawler identity is unclear, mark it as `확인 필요`
instead of treating it as a supported optimization target.

## Current Platform Facts

| platform | surface | token_or_crawler | role | control_scope | source_url | last_verified | confidence | package_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OpenAI | training crawler | `GPTBot` | May crawl public pages for model improvement depending on site controls | `robots.txt` allow/disallow for `GPTBot` | <https://developers.openai.com/api/docs/bots> | 2026-05-07 | high | Mention as training-crawler access, not as a search or citation guarantee |
| OpenAI | search crawling | `OAI-SearchBot` | Search-related crawler for surfacing and linking public web content in OpenAI products | `robots.txt` allow/disallow for `OAI-SearchBot` | <https://developers.openai.com/api/docs/bots> | 2026-05-07 | high | Use for search visibility readiness, not model training claims |
| OpenAI | user-triggered fetch | `ChatGPT-User` | User-action fetcher when a ChatGPT user asks for or provides access to content | User interaction plus web access, not durable indexing | <https://developers.openai.com/api/docs/bots> | 2026-05-07 | high | Separate from crawler/index readiness and private connector evidence |
| Google | search crawler | `Googlebot` | Google Search 포함 public crawling and indexing surface | Google Search crawler controls | <https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers> | 2026-05-07 | high | Use for search crawlability and indexability, not AI answer inclusion |
| Google | crawler classification | `Google-Extended` | Standalone product token for controls outside normal Google Search crawling | Product-specific control, not a replacement for `Googlebot` | <https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers> | 2026-05-07 | high | Do not label as a dual training+search crawler |
| Google | merchant result surface | merchant listing structured data | Product and merchant listing eligibility signal | Structured data plus merchant/feed/business requirements | <https://developers.google.com/search/docs/appearance/structured-data/merchant-listing?hl=en> | 2026-05-07 | high | Route to commerce readiness, not Product schema alone |
| Anthropic | training/usage crawler | `ClaudeBot` | Anthropic crawler token documented for web crawling controls | `robots.txt` allow/disallow for `ClaudeBot` | <https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler> | 2026-05-07 | high | Mention as Anthropic crawler access where relevant |
| Anthropic | search crawling | `Claude-SearchBot` | Anthropic web-search crawler token for search retrieval contexts | `robots.txt` allow/disallow for `Claude-SearchBot` | <https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler> | 2026-05-07 | high | Separate search retrieval from training crawler claims |
| Anthropic | user-triggered fetch | `Claude-User` | User-requested access token for Claude browsing or user action contexts | User interaction and access context | <https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler> | 2026-05-07 | high | Separate from public crawler readiness and citation measurement |
| IndexNow | indexing notification | `IndexNow` protocol | URL change notification protocol, not an AI ingestion guarantee | Host key and submit endpoint | <https://www.indexnow.org/documentation> | 2026-05-07 | high | Label as indexing-notification readiness only |
| Perplexity | commerce action | Instant Buy | Platform-specific transaction/action surface | Merchant and platform eligibility, not generic Product schema | <https://www.perplexity.ai/help-center/en/articles/10352906-what-is-instant-buy> | 2026-05-07 | medium | Route to commerce readiness and platform eligibility checks |
| xAI / Grok | crawler/search tokens | Grok crawler tokens | Public package lacks captured official token proof | Unknown | fresh official source required | 2026-05-07 | low | Mark as 확인 필요 before producing a platform-specific implementation step |

## Reporting Rules

- Use `platform_truth_source` when a report relies on a platform-specific fact.
- Use `last_verified` whenever an official-source fact is stated.
- Use `confidence=low` and `package_action=확인 필요` when the package has no
  captured official source for a token or control surface.
- Label non-measured implementation readiness as heuristic / adoption-dependent
  when platform ingestion, citation, or transaction behavior is not observed.
- Do not infer measured AI visibility from crawler access alone.
- Do not use public crawler evidence to claim private connector, logged-in user,
  or personalized answer behavior.
