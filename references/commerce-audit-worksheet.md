# GEO Commerce Audit Worksheet

Use this worksheet when a GEO request touches product discovery, shopping
answers, lead generation, checkout/action readiness, Instant Buy, or any
commerce-like conversion surface.

Product schema alone does not prove commerce readiness.

## Product Identity

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Product name, SKU, model, or variant is clear |  | pass / fail / unknown |  |
| Canonical product URL exists |  | pass / fail / unknown |  |
| Product images and descriptions are crawlable |  | pass / fail / unknown |  |
| Category and use case are answer-ready |  | pass / fail / unknown |  |

## Schema Readiness

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Product structured data exists and validates |  | pass / fail / unknown |  |
| Offer, price, availability, shipping, and returns are present where applicable |  | pass / fail / unknown |  |
| Merchant listing structured data requirements are checked separately |  | pass / fail / unknown |  |

## Merchant Facts

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Business identity, seller, or merchant profile is clear |  | pass / fail / unknown |  |
| Trust, policy, refund, and support pages are reachable |  | pass / fail / unknown |  |
| Contact and service region are explicit |  | pass / fail / unknown |  |

## Catalog / Feed

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Product catalog or feed exists where the target platform requires it |  | pass / fail / unknown |  |
| Inventory and price freshness process is documented |  | pass / fail / unknown |  |
| Platform-specific merchant/feed requirements are identified |  | pass / fail / unknown |  |

## Checkout / Action

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Checkout, purchase, booking, contact, or lead action is reachable |  | pass / fail / unknown |  |
| Platform transaction eligibility is verified from official docs or account state |  | pass / fail / unknown |  |
| Action handoff is measured or prepared for measurement |  | pass / fail / unknown |  |

## Measurement Readiness

| check | evidence | status | gap |
| --- | --- | --- | --- |
| Prompt panel exists for shopping/action questions |  | pass / fail / unknown |  |
| Analytics can distinguish referral_signal from conversion_signal |  | pass / fail / unknown |  |
| Before/after capture window is defined |  | pass / fail / unknown |  |

## Output

Close with:

- `commerce_status`
- `schema_status`
- `catalog_status`
- `checkout_action_status`
- `measurement_readiness`
- `platform_eligibility_status`
