# GEO Private Surface Routing

This reference separates public crawler/index evidence from private, logged-in,
personalized, or user-provided evidence. GEO reports must not blend these
surfaces without naming the access profile.

## Surface Types

| surface_type | description | safe claim | unsafe claim |
| --- | --- | --- | --- |
| `public_crawler_surface` | Public pages and files available to platform crawlers | Crawlability, public content readiness, public structured data | Private answer behavior or logged-in connector behavior |
| `public_search_surface` | Search index, SERP, AI overview, or public answer surface | Observed public answer/citation for the tested prompt and region | Universal answer behavior |
| `private_connector_surface` | User-authorized connector, workspace, inbox, drive, CRM, or private corpus | Access-limited answer behavior for the permission profile | Public GEO visibility |
| `logged_in_user_surface` | Logged-in browser or account-specific context | Account-specific observation | General market visibility |
| `user_provided_context_surface` | User pasted material or uploaded file in the conversation | Answer quality for that supplied context | Public discoverability or citation |

## Permission Profile

Every private or personalized capture must record a permission profile:

- account type
- connector or data source
- region and language
- whether the answer used private context
- whether the evidence can be quoted, saved, or shared

## Routing Rule

1. If evidence is public, route to crawler, schema, content, platform, or report
   workflows.
2. If evidence is private or logged-in, route to a private evidence note and
   mark public claims as unproven.
3. If the answer depends on user-provided context, label it as
   `user_provided_context_surface`.
4. Do not use private evidence to claim public visibility.

## Output Fields

Reports should include:

- `access_profile`
- `surface_type`
- `private_context_used`
- `shareability`
- `public_visibility_claim_allowed`
