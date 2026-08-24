# SEO / Marketing Skills

Reusable knowledge bundles for content and growth workflows — keyword strategy, briefs, structured data, and performance auditing. Designed to be invoked by SEO/marketing agents in `agents/seo-marketing/`.

## Skills

| Skill | Use For |
|-------|---------|
| [`keyword-cluster-generation`](keyword-cluster-generation/SKILL.md) | Group keywords by intent and SERP overlap; map to pillar + cluster architecture |
| [`content-brief-scaffolding`](content-brief-scaffolding/SKILL.md) | Structured brief grounded in SERP analysis, with entity coverage and quality gates |
| [`schema-org-markup`](schema-org-markup/SKILL.md) | JSON-LD structured data for Article, Product, FAQPage, LocalBusiness, Organization |
| [`core-web-vitals-audit`](core-web-vitals-audit/SKILL.md) | Field + lab CWV audit, prioritized fix plan, performance budgets |

## Typical Pipeline

```
keyword-cluster-generation → content-brief-scaffolding → (writer produces content)
            │                          │
            ↓                          ↓
      Cluster + pillar map        Per-page brief
                                       │
                                       ↓
                            schema-org-markup → core-web-vitals-audit
                                       │                  │
                                       ↓                  ↓
                                  Rich result         Performance gate
                                  eligibility         before launch
```

## Companion Skills

- `skills/web-development/` — frontend frameworks where these pages live
- `skills/accessibility/` — a11y is a ranking factor and CRO factor
- `skills/content-creation/` — content production templates

## Companion Agents

- `agents/seo-marketing/seo-content-auditor.md`
- `agents/seo-marketing/seo-content-writer.md`
- `agents/seo-marketing/seo-structure-architect.md`
