# External Evidence Source Index

This package treats evidence as external when it comes from primary standards,
official product documentation, academic literature, technical reports, or
explicitly labelled local-market sources. Internal package notes may organize
judgment, but they are not sufficient by themselves to justify a claim.

## Evidence Source Priority

| Tier | Source type | Use |
|---|---|---|
| P0 | Standards and protocols | Normative engineering basis |
| P1 | Official product/company documentation | Platform behavior, crawler identity, webmaster controls |
| P2 | Academic papers and empirical technical studies | Mechanism, limitation, uncertainty, measurement design |
| P3 | Expert technical reports and professional publications | Secondary engineering interpretation |
| L | Korean/local-market sources | Local context, market clue, implementation reference; not primary unless the claim is about Korean institutions or services |

## Evidence Maturity Matrix

| Maturity | Meaning | Examples | Package claim boundary |
|---|---|---|---|
| Established standard | Ratified standard, protocol, or long-standing public web protocol | RFC 9309, W3C JSON-LD 1.1, Sitemaps.org protocol | Can support engineering readiness claims, not downstream ranking or AI citation guarantees |
| Accepted official implementation | Official platform documentation for a search engine, AI vendor, browser automation tool, or webmaster system | Google Search Central, OpenAI bots, Anthropic crawler docs, Perplexity robots docs, Playwright | Can support platform-specific checks; must be reverified when bot names, policies, or UI behavior are volatile |
| Accepted search quality framework | Official quality guidance used to evaluate content usefulness, trust, and expertise | Google helpful content, E-E-A-T, Search Quality Rater Guidelines | Can support heuristic content review, not measured ranking or citation claims |
| Empirical caution | Academic or technical study that measures crawler behavior, compliance, or uncertainty | arXiv crawler/robots studies | Can justify conservative limits and measurement requirements; cannot replace current platform docs |
| Emerging/proposal | Public proposal or community convention that is not a ratified web standard or broadly guaranteed platform requirement | llms.txt | Can support drafts and implementation experiments only |
| Local official implementation | Official local-market search/platform documentation | NAVER Search Advisor, Baidu robots docs | Primary only for that local service behavior; label as local implementation reference elsewhere |

## Core Engineering Principles

| Principle | Evidence class | External basis | Package implication |
|---|---|---|---|
| Robots exclusion is a crawler instruction protocol, not access control | P0 | RFC 9309, Robots Exclusion Protocol, https://www.rfc-editor.org/rfc/rfc9309 | `robots.txt` findings are readiness evidence, not proof of measured AI visibility or security control |
| Sitemaps describe crawlable URL discovery hints, not guaranteed indexing | P0/P1 | Sitemaps.org protocol, https://www.sitemaps.org/protocol.html; Google sitemap docs, https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview | Sitemap findings are readiness evidence and must not be treated as indexation or citation proof |
| Crawler identity and robots handling must be platform-specific | P1 | OpenAI crawler docs, https://platform.openai.com/docs/bots; Anthropic crawler docs, https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler; Perplexity robots.txt docs, https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt | Bot recommendations must cite the platform source and distinguish training, search, and user-triggered agents |
| JSON-LD and schema structured data improve machine readability but do not prove AI citation | P0/P1 | W3C JSON-LD 1.1 Recommendation, https://www.w3.org/TR/json-ld11/; schema.org schemas, https://schema.org/docs/schemas.html; Google structured data docs, https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data | Schema findings are readiness evidence unless a platform output is captured |
| Helpful, reliable, people-first content and E-E-A-T are quality evaluation concepts, not direct measured AI ranking factors | P1 | Google helpful content docs, https://developers.google.com/search/docs/fundamentals/creating-helpful-content; Google E-E-A-T update, https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t | Content quality scoring is heuristic unless tied to measured search or AI output |
| Multilingual targeting needs explicit language/region signals | P1 | Google localized versions/hreflang docs, https://developers.google.com/search/docs/specialty/international/localized-versions; managing multi-regional sites, https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites | `hreflang`, localized URLs, and sitemap alternates are readiness evidence |
| Browser automation can capture observed platform output, but only stored raw observations count as measured evidence | P1 | Playwright documentation, https://playwright.dev/docs/intro | `/geo realtime` may claim `Measured` only when it stores platform output, citation URLs, screenshots, or logs |
| `llms.txt` is an emerging proposal, not an adopted standard | P3 | llms.txt proposal, https://llmstxt.org | `/geo llmstxt` may draft and inspect files, but must not claim standard compliance or guaranteed platform adoption |
| AI crawler behavior is empirically unstable and must be measured when visibility is claimed | P2 | Scrapers selectively respect robots.txt directives, arXiv:2505.21733, https://arxiv.org/abs/2505.21733; The Liabilities of Robots.txt, arXiv:2503.06035, https://arxiv.org/abs/2503.06035 | Do not infer citation or index inclusion from robots readiness alone |

## Platform and Bot Source Map

| Platform / bot | Primary source | Evidence role | Notes |
|---|---|---|---|
| OpenAI `GPTBot`, `OAI-SearchBot`, `ChatGPT-User` | https://platform.openai.com/docs/bots | P1 official | Distinguish training crawler, search crawler, and user-triggered requests |
| Anthropic `ClaudeBot`, `anthropic-ai` | https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | P1 official | Training crawler and robots.txt control basis; check current docs before release |
| Perplexity `PerplexityBot` | https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt | P1 official | Official statement of robots.txt handling; empirical behavior may still require logs |
| Google robots.txt interpretation | https://developers.google.com/search/reference/robots_txt | P1 official | Search crawler interpretation and error handling basis |
| Google `Google-Extended` | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers | P1 official | Product-token behavior must be verified against current Google docs before release |
| Bingbot / Bing Webmaster | https://learn.microsoft.com/en-us/bingwebmaster/ | P1 official | Bing-based search readiness and webmaster tooling basis |
| Applebot / Applebot-Extended | https://support.apple.com/en-euro/119829 | P1 official | Applebot search/Siri/Spotlight and Applebot-Extended training opt-out distinction |
| NAVER `Yeti` | https://searchadvisor.naver.com/guide/seo-basic-robots; https://searchadvisor.naver.com/guide/seo-basic-firewall | P1/L official local | Korean search implementation reference; Korean source is primary for NAVER behavior |
| Baiduspider | https://www.baidu.com/search/robots_english.html | P1 official | China search crawler readiness basis |
| W3C JSON-LD | https://www.w3.org/TR/json-ld11/ | P0 standard | Data model and syntax basis for JSON-LD usage |
| Sitemaps.org | https://www.sitemaps.org/protocol.html | P0/P1 protocol | Sitemap XML protocol basis; readiness only |
| schema.org | https://schema.org/docs/schemas.html | P1 official | Vocabulary basis for Organization, Product, Article, FAQPage, LocalBusiness |
| llms.txt | https://llmstxt.org | P3 proposal | Useful implementation reference, not an adopted web standard |

## Claims Requiring Live Verification Before Release

| Claim area | Why volatile | Required evidence before treating as current |
|---|---|---|
| Naver AI Briefing market share or rollout percentage | Product and market metrics change quickly | NAVER official announcement, investor material, or clearly labelled local-market report with date |
| Naver AI Tab launch state | Product beta/GA status changes quickly | NAVER official announcement or dated local-market source labelled as local context |
| ClovaX service status | Product lifecycle claim | NAVER official notice if available; otherwise local-market secondary source labelled as local context |
| xAI/Grok crawler names | Documentation availability and bot names change | xAI official crawler documentation or server-log measurement |
| Meta AI crawler names | Documentation availability and bot names change | Meta official crawler documentation or server-log measurement |
| Yahoo Japan AI crawler behavior | Search provider and crawler delegation may change | LY/Yahoo Japan official crawler documentation or confirmed webmaster docs |

## Citation Rule for Package Outputs

When a recommendation depends on an external platform behavior, cite the source
family in the output or label the claim as `heuristic` / `requires live
verification`. Do not present internal tables as the source of truth unless they
point to an external source row in this index.
