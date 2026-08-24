---
name: keyword-cluster-generation
description: Group keywords into topic clusters by search intent and SERP overlap, then map clusters to a content architecture (pillar + cluster pages). Use when planning a content site, auditing thin or cannibalizing pages, or moving from keyword-list to topic-authority strategy.
metadata:
  tags:
    - seo
    - content-strategy
    - keyword-research
    - topical-authority
  updated: "2026-05-05"
---

# Keyword Cluster Generation

Keyword lists are not a content plan. Topic clusters are. This skill turns a flat list of keywords into a clustered architecture where each cluster has a pillar page, supporting pages, clear search intent, and no internal cannibalization.

## When to Use This Skill

- Standing up a new content site or section
- Existing site has 200+ pages but ranks for nothing — likely cannibalization or weak topical authority
- Moving from per-keyword content briefs to topic-driven editorial planning
- Auditing whether a competitor's content map covers gaps you don't

## Inputs Required

- A keyword list with at minimum: keyword, monthly search volume, optional difficulty, optional SERP URLs
- Existing site URL (for cannibalization check, optional but useful)
- Business priority signals — which keywords map to revenue (optional)

## Clustering Method

### Step 1: Classify Search Intent

Bucket each keyword into one of:

| Intent | Pattern | SERP signals | Content type |
|---|---|---|---|
| **Informational** | "how to", "what is", "guide", "examples" | Featured snippets, "People also ask", Wikipedia | Articles, guides, tutorials |
| **Navigational** | brand or product name | Brand page dominant | Brand/product page |
| **Commercial** | "best", "vs", "alternatives", "review" | Listicles, comparison pages, review sites | Comparison, review, listicle |
| **Transactional** | "buy", "price", "deal", "near me" | Product pages, e-commerce, local pack | Product, pricing, landing |

**Mixed intent is its own bucket.** "best CRM software" has commercial + informational signals; the SERP usually shows listicles. Note this explicitly.

### Step 2: Cluster by SERP Overlap (preferred when SERP data available)

Two keywords belong in the same cluster if their top-10 SERPs overlap by ≥3 URLs. Google has decided they're answerable by the same page.

```python
# pseudo-code
def cluster_by_serp_overlap(keywords, threshold=3):
    clusters = []
    for kw in keywords:
        placed = False
        for cluster in clusters:
            if len(set(kw.top10_urls) & set(cluster.union_top10)) >= threshold:
                cluster.add(kw)
                placed = True
                break
        if not placed:
            clusters.append(Cluster([kw]))
    return clusters
```

### Step 3: Cluster by Semantic Similarity (fallback when no SERP data)

Use embeddings (OpenAI text-embedding-3-small, sentence-transformers) and a community detection algorithm (Louvain) or simple agglomerative clustering with a similarity threshold ~0.75.

### Step 4: Assign Cluster Roles

Within each cluster, designate:

- **Pillar page** — the broad, comprehensive page targeting the head term ("CRM software")
- **Cluster pages** — supporting pages targeting long-tail variants ("CRM for real estate", "CRM with email integration")
- **Internal links** — every cluster page links to the pillar; the pillar links out to all cluster pages

### Step 5: Cannibalization Check

For an existing site:

```
For each cluster:
  Find all existing URLs that already target any keyword in this cluster
  If multiple URLs target overlapping keywords:
    Decide: consolidate (301), differentiate (rewrite), or kill (404 + remove)
```

Two pages targeting the same intent compete with each other in Google's ranking — the result is neither ranks well.

## Output Schema

```yaml
clusters:
  - cluster_id: crm-software
    intent: commercial
    total_volume: 142000
    pillar:
      target_keyword: "crm software"
      volume: 49500
      url: /crm-software/
      content_type: "comprehensive guide + comparison table"
    cluster_pages:
      - target_keyword: "best crm for small business"
        volume: 14800
        url: /crm-software/small-business/
        intent: commercial
      - target_keyword: "what is crm"
        volume: 9900
        url: /crm-software/what-is-crm/
        intent: informational
      - target_keyword: "crm vs erp"
        volume: 4400
        url: /crm-software/crm-vs-erp/
        intent: commercial
    internal_link_structure:
      pillar_links_to_all_cluster_pages: true
      cluster_pages_link_to_pillar: true
      sibling_links: contextual_only
    cannibalization_risk:
      existing_overlapping_urls: []
```

## Architectural Patterns

### Hub-and-Spoke (most common)

```
/crm-software/                           [pillar]
├── /crm-software/small-business/        [cluster page]
├── /crm-software/enterprise/            [cluster page]
├── /crm-software/free/                  [cluster page]
├── /crm-software/what-is-crm/           [cluster page, informational]
└── /crm-software/crm-vs-erp/            [cluster page, comparison]
```

### Topic Silo (stronger, harder to maintain)

URL structure mirrors the cluster tree, breadcrumbs reinforce hierarchy, and cross-silo linking is discouraged.

### Flat with Tags

Pages live at `/article-slug/`, internal linking carries the topical authority signal. Easier to manage, weaker silo signal — fine for sites where topical authority comes from sheer volume of related content.

## Implementation Checklist

- [ ] Every keyword has an intent classification
- [ ] Clusters are formed by SERP overlap when SERP data is available
- [ ] Each cluster has exactly one pillar page assigned
- [ ] No keyword belongs to two clusters
- [ ] Internal linking plan maps cluster pages → pillar
- [ ] Cannibalization audit complete for existing URLs
- [ ] Cluster prioritization reflects business value, not just search volume
- [ ] Each cluster has an estimated total addressable traffic
- [ ] Output is in a format the editorial team can act on (spreadsheet or CMS)

## Anti-Patterns to Avoid

- **One keyword per page, no clusters** — wastes topical authority, prone to cannibalization
- **Clusters by topic vibes alone** — without SERP overlap or embeddings, topic boundaries are subjective
- **No pillar page** — cluster pages have nothing to link up to
- **Pillar page targets the highest-volume keyword regardless of intent** — if the head term is informational and the cluster is commercial, intent mismatch tanks rankings
- **Ignoring existing cannibalization** — new clusters compete with existing pages; audit first
- **Volume-only prioritization** — high-volume informational keywords often don't convert

## Companion Skills

- `content-brief-scaffolding` — produce a brief for each pillar/cluster page identified
- `core-web-vitals-audit` — performance audit before launching a content push
- `schema-org-markup` — structured data for the resulting pages

## Related Resources

- ../../../domain-business-strategy/research/research_competitive_landscape.md
