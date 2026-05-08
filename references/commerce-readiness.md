# GEO Commerce Readiness

Use this reference when a GEO audit, report, proposal, schema task, or platform
review touches shopping, product discovery, checkout, lead generation, or other
commercial action surfaces.

The core rule is: Product schema alone does not prove commerce readiness.
Crawler access, valid JSON-LD, and content clarity are necessary readiness
signals, but transaction/action readiness also depends on catalog, merchant,
policy, eligibility, integration, and measurement surfaces.

## Readiness Layers

| Layer | What to check | Evidence examples | Boundary |
| --- | --- | --- | --- |
| Product identity | product name, brand, description, variants, images, canonical URL | page content, canonical tags, image URLs, product copy | helps entity recognition, not transaction eligibility |
| Structured data | Product, Offer, AggregateRating, Review, shipping, return, and merchant-relevant fields where applicable | JSON-LD validation, rendered page inspection, structured-data test output | schema validity is not a platform acceptance guarantee |
| Merchant facts | price, availability, currency, condition, seller, shipping, returns, policies, support | page copy, merchant policy pages, feed fields, platform merchant docs | missing policy facts weaken shopping trust |
| Catalog/feed consistency | product feed, sitemap, canonical URLs, stock, price, and variant consistency | feed export, product sitemap, crawl sample, merchant-center-like diagnostics | inconsistent feeds can break shopping surfaces |
| Checkout/action surface | checkout, buy button, lead form, instant-buy or partner action flow when available | checkout URL, action schema, partner integration, test order or lead event | action eligibility is platform-specific |
| Measurement | product impressions, clicks, AI/search referrals, add-to-cart, checkout, order, lead, and CRM events | analytics, logs, UTM, server events, order/lead records | measurement proves outcomes only for the measured period |

## Platform-Aware Boundaries

- OpenAI Commerce and shopping research surfaces should be treated as separate
  from generic ChatGPT crawling and answer citation until the actual surface is
  tested or documented for the merchant case.
- Google merchant listing structured data supports search shopping eligibility
  signals, but Google Search crawling and `Google-Extended` policy controls are
  not the same mechanism.
- Perplexity Instant Buy should be treated as an action/commerce surface, not a
  generic citation surface.
- Anthropic web search and crawler controls should be separated from checkout or
  commerce action claims unless a specific commerce integration is documented.

## Minimum Audit Questions

1. Which product or service set is in scope?
2. Which commerce surface is being targeted: answer citation, product listing,
   shopping research, instant buy, checkout, lead, or referral?
3. Are price, availability, shipping, returns, seller, and support facts visible
   and consistent?
4. Is Product/Offer structured data present and valid after rendering?
5. Is a product feed, product sitemap, or catalog export available when the
   target surface expects one?
6. Can the action path be tested without assuming platform eligibility?
7. Which measurement event proves the desired result?

## Reporting Contract

Commerce/action recommendations should separate:

- `content_readiness`: entity, product, trust, and answer clarity
- `schema_readiness`: Product/Offer and related structured-data validity
- `merchant_readiness`: price, availability, shipping, returns, and seller facts
- `catalog_readiness`: feed, sitemap, canonical, variant, and stock consistency
- `action_readiness`: checkout, lead, instant-buy, or partner action path
- `measurement_readiness`: analytics, logs, events, and conversion linkage

Use `references/commerce-audit-worksheet.md` when the request needs a
step-by-step Product Identity, Schema Readiness, Merchant Facts, Catalog / Feed,
Checkout / Action, and Measurement Readiness worksheet.

## Source Anchors

- OpenAI Commerce documentation: <https://developers.openai.com/commerce>
- ChatGPT shopping research help: <https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt>
- Google merchant listing structured data: <https://developers.google.com/search/docs/appearance/structured-data/merchant-listing>
- Google crawler documentation: <https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers>
- Perplexity Instant Buy help: <https://www.perplexity.ai/help-center/en/articles/10352906-what-is-instant-buy>
