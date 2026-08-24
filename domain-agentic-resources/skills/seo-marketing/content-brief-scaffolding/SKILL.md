---
name: content-brief-scaffolding
description: Generate a structured content brief from a target keyword and SERP analysis — search intent, required sections, entity coverage, internal links, schema, and word-count target. Use when assigning a piece to a writer, when SEO and editorial keep producing mismatched output, or when scaling content production beyond one author.
metadata:
  tags:
    - seo
    - content-marketing
    - briefs
    - editorial
  updated: "2026-05-05"
---

# Content Brief Scaffolding

A brief that says "write 1500 words about X with these keywords" produces 1500 words that don't rank. A brief grounded in the actual SERP — what's already ranking, what entities are mentioned, what intent the page must satisfy — produces content that has a chance.

## When to Use This Skill

- Briefing a freelance writer or in-house editorial team
- Standardizing brief format across a content team
- A piece of content was published and didn't rank — diagnose the brief
- Scaling from one writer to a content production line

## Inputs Required

- Primary keyword (the page's target)
- SERP top 10 for the primary keyword (URLs + titles + meta descriptions, or full extracted content)
- Target audience description
- Funnel stage (TOFU / MOFU / BOFU) and conversion intent
- Internal link inventory (related pages on the site)
- Brand voice guidelines (optional but improves output)

## Brief Structure

### 1. Strategic Header

```markdown
# Brief: {Page Title}

**Target keyword:** {primary keyword}
**Search volume:** {monthly volume}
**Keyword difficulty:** {0-100}
**Search intent:** Informational | Commercial | Transactional | Mixed
**Funnel stage:** TOFU | MOFU | BOFU
**Conversion goal:** {newsletter signup | demo request | purchase | none}
**Cluster role:** Pillar | Cluster page
**Pillar page (if cluster):** /url-of-pillar/
**Target word count:** {derived from SERP analysis} ± 15%
**Reading level:** {grade level appropriate for audience}
```

### 2. SERP Analysis Summary

```markdown
## What's Ranking and Why

**Top 10 dominant content type:** {listicle | guide | comparison | tool}

**Common patterns observed:**
- All top 5 include a comparison table
- 8 of 10 include a "how it works" diagram
- Average word count: 2,800
- All include FAQ section
- 6 of 10 have video embeds

**SERP features present:** Featured snippet (paragraph), People Also Ask (4 questions), Image pack

**Competitor we're explicitly trying to beat:** {URL} — strengths to match, weaknesses to exploit
```

### 3. Required Sections

```markdown
## Outline

1. **Introduction** (~150 words)
   - Hook: open with the cost of not solving this problem
   - Define the problem in the audience's language
   - Preview what the article delivers

2. **What is {topic}** (~300 words)
   - Plain-language definition
   - Include this entity: {entity 1}
   - Include this entity: {entity 2}

3. **{Section addressing top "People Also Ask" question}** (~400 words)
   - Direct answer in first sentence (snippet target)
   - Supporting evidence

4. **Comparison table** (markdown table)
   - Required columns: {derived from competitor analysis}
   - Required rows: {top alternatives to compare}

5. **How to choose** (~500 words)
   - Decision framework specific to audience
   - Use case examples

6. **FAQ** (4-6 questions)
   - Answer each question in 40-80 words
   - Questions to include: {pulled from "People Also Ask"}

7. **Conclusion + CTA** (~100 words)
   - Restate the decision framework
   - {specific conversion action}
```

### 4. Entity and Keyword Coverage

```markdown
## Entities to Cover

The following entities appear in 5+ of the top 10 ranking pages and must be addressed:
- {entity 1} — context: {how it relates to topic}
- {entity 2}
- {entity 3}
...

## Secondary Keywords (use naturally, don't force)

- {long-tail variant 1} — used in H2 if natural
- {long-tail variant 2} — used in body
- {related question} — answered in FAQ
```

### 5. Internal Linking

```markdown
## Required Internal Links

Link to these existing pages, with anchor text guidance:

| Target URL | Anchor text guidance | Where in article |
|---|---|---|
| /pillar-page/ | "comprehensive guide to X" | First mention in intro |
| /cluster-page-1/ | descriptive, varied | "How to choose" section |
| /case-study/ | "real-world example" or similar | After comparison table |

## Outbound Links

Cite these authoritative sources where relevant:
- {source 1} — for the {claim} in the {section}
- {source 2}
```

### 6. Structured Data and Metadata

```markdown
## On-Page SEO

**Title tag** (50-60 chars): {draft title}
**Meta description** (140-160 chars): {draft description}
**URL slug:** /{slug}/
**H1:** {primary H1, can match title or vary}

**Schema markup:** Article + FAQPage + (BreadcrumbList from site infrastructure)

**Featured snippet target:**
- Type: {paragraph | list | table}
- Located in: {section name}
- Format: {what the writer must do to win the snippet}
```

### 7. Voice and Style

```markdown
## Voice Guidelines

- Audience persona: {1-line description}
- Reading level: {grade level}
- Tone: {3 adjectives}
- Avoid: {forbidden phrases, clichés, competitor names if any}
- Style sheet: {link to brand style guide}
- Examples of pages that nail the voice: {2-3 internal URLs}
```

### 8. Quality Gates

```markdown
## Editorial Acceptance Checklist

Before submitting, the writer confirms:
- [ ] All required sections present
- [ ] All required entities mentioned
- [ ] Word count within 15% of target
- [ ] All required internal links in place
- [ ] FAQ section present with target questions
- [ ] Featured snippet target text present and well-formatted
- [ ] No phrases from "Avoid" list
- [ ] Reading level matches target (verified with Hemingway or similar)
- [ ] At least one original observation, framework, or data point not in the SERP
```

## Programmatic Brief Generation

For scaled content operations, generate briefs programmatically:

```python
def generate_brief(keyword: str, serp_data: SERPData, site_inventory: list[Page]) -> Brief:
    intent = classify_intent(keyword, serp_data)
    target_word_count = int(median(p.word_count for p in serp_data.top_10) * 1.1)
    entities = extract_common_entities(serp_data.top_10, min_occurrences=5)
    paa_questions = serp_data.people_also_ask
    competitor_outline = extract_dominant_outline(serp_data.top_10)
    internal_links = match_relevant_pages(keyword, site_inventory, top_n=5)

    return Brief(
        keyword=keyword,
        intent=intent,
        target_word_count=target_word_count,
        outline=competitor_outline,
        entities=entities,
        faq_questions=paa_questions,
        internal_links=internal_links,
        ...
    )
```

## Implementation Checklist

- [ ] Brief includes search intent classification
- [ ] Word count target derived from SERP, not arbitrary
- [ ] Required sections grounded in competitor analysis
- [ ] Entity coverage list from top-ranking pages
- [ ] Internal linking guidance with specific anchor text
- [ ] Featured snippet target identified when applicable
- [ ] Schema markup specified
- [ ] Voice guidelines tied to specific exemplar URLs
- [ ] Editorial checklist signed off before publish
- [ ] Brief format is consistent across the team

## Anti-Patterns to Avoid

- **Keyword-stuffing checklists** — modern Google rewards entity coverage, not keyword density
- **Word counts pulled from thin air** — match the SERP, don't pad to "minimum 2000 words"
- **No outline guidance** — writer reinvents the structure, often poorly
- **No entity list** — writer omits the topical signals that get the page indexed for related queries
- **No internal linking plan** — orphaned pages or random anchor text
- **Briefs without examples** — writer has to guess what "matches our voice" means
- **No quality gate** — editorial reviewer has no checklist to evaluate against

## Companion Skills

- `keyword-cluster-generation` — feeds the cluster role and pillar designation into the brief
- `schema-org-markup` — produces the structured data the brief specifies
- `core-web-vitals-audit` — page must perform, or rankings cap regardless of content

## Related Resources

- ../../../domain-creative-writing/ (voice and style references)
