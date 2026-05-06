# GEO Execution Skill Matrix

This repository restores the download execution bundle as a confirmed local
overlay under `skills/*`.

`SKILL.md` remains the representative `geo` router. Execution-intent requests
should route through the matching subskill only after `skills/*` is confirmed.

## Restored execution subskills

| Skill | Primary use | Typical trigger | Access profile | Typical output |
| --- | --- | --- | --- | --- |
| `geo-audit` | full GEO + SEO audit across crawler, citability, content, technical, and platform signals | `전체 감사`, `사이트 분석`, `/geo audit` | `L1/L2/L3` | `GEO-감사-보고서.md` |
| `geo-brand-mentions` | external brand mention visibility across media, communities, and AI-visible sources | `브랜드 언급`, `brand mentions`, `/geo brand` | `L1/L2/L3` | mention visibility assessment |
| `geo-citability` | AI citation likelihood for answer-ready, authoritative pages | `인용 가능성`, `citability`, `/geo citability` | `L1/L2/L3` | citation score and gaps |
| `geo-compare` | side-by-side GEO gap analysis versus competitors | `경쟁사 비교`, `compare`, `/geo compare` | `L2/L3` | comparative gap analysis |
| `geo-content` | content quality and E-E-A-T review | `콘텐츠 품질`, `E-E-A-T`, `/geo content` | `L1/L2/L3` | content trust findings |
| `geo-crawlers` | robots, bot access, `llms.txt`, and crawlability review | `크롤러`, `robots.txt`, `/geo crawlers` | `L1/L2/L3` | crawler access findings |
| `geo-llmstxt` | `llms.txt` audit and generation template | `llms.txt`, `/geo llmstxt` | `L2/L3` | `llms.txt` recommendation or template |
| `geo-platform-optimizer` | platform-specific exposure review for Google AI Overviews, Perplexity, ChatGPT, Copilot, and Grok | `플랫폼 최적화`, `/geo platform` | `L1/L2/L3` | platform scorecard |
| `geo-proposal` | client or internal improvement proposal from GEO findings | `제안서`, `proposal`, `/geo proposal` | `L3` | sprint roadmap proposal |
| `geo-prospect` | lightweight prospect scan for sales or consulting discovery | `잠재 고객`, `prospect`, `/geo prospect` | `L3` | prospect scan summary |
| `geo-report` | consolidated GEO report synthesis from individual findings | `보고서`, `report`, `/geo report` | `L1/L2/L3` | consolidated roadmap report |
| `geo-report-pdf` | print-ready markdown packaging for PDF delivery | `PDF 보고서`, `/geo report-pdf` | `L3` | PDF-oriented report markdown |
| `geo-schema` | JSON-LD schema generation and validation | `스키마`, `JSON-LD`, `/geo schema` | `L3` | `GEO-스키마-[도메인].md` |
| `geo-technical` | technical SEO diagnosis and remediation guidance | `기술 SEO`, `Core Web Vitals`, `/geo technical` | `L2/L3` | technical remediation notes |

## Routing rules

1. Use the representative `geo` entrypoint first.
2. Choose `portable-baseline`, `user-material`, or `local-overlay`.
3. If the request is execution-intent and `skills/*` is present, map it to the
   matching subskill above.
4. If the execution bundle is absent, do not promise the audit/report/schema
   workflow from the portable baseline alone.
5. Keep generated reports and exports downstream from the execution subskill
   that produced or justified them.
