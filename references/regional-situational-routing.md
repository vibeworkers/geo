# GEO Regional And Situational Routing

GEO recommendations change by region, language, vertical, brand maturity, and
commerce model. This reference defines when to use the portable baseline and
when to require a fresh source pack.

## Situation Matrix

| situation | examples | required routing | evidence boundary |
| --- | --- | --- | --- |
| B2B SaaS | product-led SaaS, API platform, enterprise software | content, schema, citability, comparison, report | Use official docs, docs pages, pricing, case studies, and observed answer captures |
| Ecommerce | product catalog, marketplace seller, DTC brand | commerce worksheet, schema, catalog/feed, platform optimizer | Product schema is only one input; merchant and checkout/action readiness are separate |
| Local / Korea | Naver, Kakao, Daum, regional search/social surfaces | regional source pack before platform-specific claims | Naver/Kakao/Daum optimization claims require separate official evidence before use |
| Regulated vertical | medical, finance, legal, safety-sensitive categories | policy risk gate plus evidence confidence ladder | Avoid unsupported outcome claims and mark legal/medical/financial advice boundaries |
| New brand | little third-party coverage or few citations | prospect, content, citability, brand mention baseline | Expect low observed_answer probability; focus on source creation and measurement setup |
| Mature brand | existing mentions, media, reviews, structured product pages | compare, platform optimizer, measurement loop | Compare observed citations and referral/conversion deltas rather than readiness alone |

The `regulated` label should be used whenever the vertical creates advice,
safety, eligibility, or compliance risk.
Use `new brand` when the entity has little third-party coverage. Use
`mature brand` when existing mentions, reviews, citations, or product pages can
support comparison and measurement.

## Regional Evidence Rule

Any region-specific claim about Naver, Kakao, Daum, Baidu, Yandex, or another
non-default platform requires separate official evidence before implementation.

Use the portable baseline only for:

- source-order protection
- measurement labels
- commerce readiness structure
- report contract fields
- policy-risk classification

Do not state a specific regional platform mechanism unless the source pack
supports it.

## Output Fields

- `regional_context`
- `language_context`
- `vertical_context`
- `brand_maturity`
- `requires separate official evidence`
- `regional_claim_status`
