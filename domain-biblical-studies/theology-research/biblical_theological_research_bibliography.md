---
title: "Theological Research Source Map — Bibliography by Source-Type, Not Invented Titles"
category: biblical-studies/theology-research
description: "Build a research source map for a doctrine or theological question by describing the KINDS of real resources to consult — standard reference works, journal categories, primary vs. secondary sources, confessional vs. critical literature — and how to find and evaluate them, without ever inventing book titles, authors, or article citations. The user assembles and verifies the real bibliography."
techniques:
  - RT-05
  - DS-19
  - QA-04
  - QA-05
  - OC-12
difficulty: intermediate
tags:
  - research-methods
  - bibliography
  - source-evaluation
  - source-type
  - anti-fabrication
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_background_research_brief.md
  - domain-biblical-studies/theology-research/biblical_topical_theology_synthesis.md
  - domain-biblical-studies/theology-research/biblical_interpretive_views_comparison.md
---

# Theological Research Source Map

**Objective:** Help the user assemble a responsible research bibliography on a doctrine or theological question by routing them to the **kinds** of real resources that bear on it and how to evaluate each — without producing a single fabricated title, author, or citation.

> **STRONG-GUARD prompt.** A bibliography request is a direct invitation to hallucinate book titles, authors, dates, and article citations that look authoritative. This prompt outputs **source-types and selection/evaluation criteria only** — never specific titles or citations from memory. Any specific work the user already has is treated as supplied-by-user; everything else is theirs to find and verify.

**When to use:**
- Starting research on a doctrine/question and you need to know what categories of sources to consult and in what order.
- Building the methods/sources scaffolding for a paper before gathering real titles.

**When NOT to use:**
- You want *historical-cultural* background sources (geography, customs, archaeology) — use `biblical_background_research_brief.md`.
- You want the synthesis itself once sources are gathered — use `biblical_topical_theology_synthesis.md`.

**Audience:** Seminary/academic (A), pastors (P).

---

## Inputs / Context

1. **The doctrine/question.** Stated precisely, with the angle you're researching.
2. **Scope/level (optional).** E.g., seminary paper, sermon prep, lay study — sets depth.
3. **Sources in hand (optional).** Real works the user has; treated as supplied-by-user, not endorsed or expanded from memory.
4. **Declared tradition (optional).** May foreground that stream's standard literature categories; alternatives still mapped.

---

## Constraints

### Must
- Describe **source-types** (e.g., standard one-volume and multi-volume reference works, theological dictionaries, monograph categories, peer-reviewed journal categories, primary/confessional documents, critical editions) — by *kind and function*, not by title.
- Distinguish **primary** sources (the documents a tradition itself produced) from **secondary** literature (works about them).
- Distinguish **confessional** literature (written from within a tradition) from **critical/academic** literature, and note that both have a standpoint.
- Provide **selection and evaluation criteria** for each source-type (recency, scholarly reception, peer review, representativeness, bias to watch for).
- Suggest a **search strategy** (where these source-types live: library catalogs, indexed databases, association/journal listings) so the user can find real titles themselves.

### Must Not
- Invent or "recall" specific book titles, authors, publication years, page numbers, or article citations — not even as examples.
- Present any specific work as authoritative or comprehensive from memory.
- Imply the list is exhaustive or that following it substitutes for reading the sources.

### Tradition-neutral stance (Must / Must Not)
- **Must:** map the literature of each relevant stream descriptively, flagging each as confessional or critical.
- **Must Not:** route the user only to one tradition's literature as if it were the field.

---

## Instructions

### Step 1 — Frame the question and scope
State the doctrine/question, the angle, and the research level (depth required).

### Step 2 — Map source-types
List the categories of real resources that bear on the question, by kind and function — reference works, monographs, journals, primary/confessional documents, critical editions.

### Step 3 — Primary/secondary, confessional/critical
For each category, mark primary vs. secondary and confessional vs. critical, and name the standpoint to keep in view.

### Step 4 — Evaluation criteria
Give criteria for choosing and weighing works within each source-type (peer review, reception, recency, representativeness, bias).

### Step 5 — Search strategy & verification
Tell the user where each source-type lives and how to confirm a work is real and well-regarded before citing it; restate that no titles were supplied.

---

## Output Format

```
# Research Source Map — [doctrine/question]

## Question & scope
- Question: [..] | Angle: [..] | Level: [..]

## Source-types to consult (kinds, not titles)
| Source-type (kind/function) | Primary/Secondary | Confessional/Critical | What it gives you | Standpoint to watch |
|-----------------------------|-------------------|------------------------|-------------------|---------------------|
| [..] | [..] | [..] | [..] | [..] |

## Selection & evaluation criteria
- [per source-type: how to choose and weigh]

## Search strategy (find real titles yourself)
- Where these live: [catalogs / databases / association & journal listings]
- Verify before citing: [confirm existence, author, date, reception]

## Note
- No specific titles or citations were supplied; assemble and verify the real bibliography yourself.
```

---

## Verification

- [ ] Output describes source-types by kind/function only — zero specific titles, authors, years, or citations.
- [ ] Primary vs. secondary and confessional vs. critical distinguished for each source-type.
- [ ] Evaluation criteria given per source-type; standpoints flagged.
- [ ] Search strategy points the user to real catalogs/databases to find and verify titles.
- [ ] Multiple relevant streams mapped; not routed to one tradition's literature as "the field."

---

## False-Positive Prevention

❌ **DON'T:**
- Offer "a few key works to start with" by name — every such title is a fabrication risk.
- Recall an author, publication year, or article citation from memory, even as an illustration.
- Present one tradition's standard library as the whole field, or imply the map is exhaustive.

✅ **DO:**
- Describe source-types by kind and function and how to evaluate them.
- Send the user to real catalogs/databases to find titles, and tell them to verify each before citing.
- Map confessional and critical literature across the relevant streams, flagging standpoints.
