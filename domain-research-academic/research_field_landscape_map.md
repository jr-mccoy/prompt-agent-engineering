---
title: "Field Landscape Map — Lineages, Labs, Methods, Fault Lines, and Emerging Areas"
category: research-academic/landscape
description: "Map a research field for someone entering it. Surfaces the major research lineages or schools, key labs / institutions / individuals, dominant methodologies per lineage, fault lines (where lineages disagree), recent influential papers, and emerging vs declining sub-areas. Designed for fast orientation in a new field."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - landscape-mapping
  - field-orientation
  - research
  - lineages
  - methods
updated: "2026-05-10"
reasoning:
  styles: [synthetic, taxonomic, structural]
  stakes: variable
  horizon: days_to_weeks
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: structured_field_map
  url_role: [researcher, student, journalist, founder, analyst, policy]
  mode: [synthesize, audit]
related_prompts:
  - domain-research-academic/research_question_formulation.md
  - domain-research-academic/research_literature_review_plan.md
  - domain-business-strategy/research/research_industry_trends.md
---

# Field Landscape Map

**Objective:** Map a research field for someone orienting to it for the first time (or returning after a long gap). Identify major **lineages or schools** (different theoretical / methodological traditions), the **key labs / institutions / individuals** anchoring each, the **dominant methodologies** per lineage, the **fault lines** (where lineages disagree), the **recent influential papers** per lineage, and the **emerging vs declining sub-areas**. Goal: someone can use the map to know who to read, what tradition each piece comes from, and where the live debates are.

**When to use:**
- Entering a new field for research, journalism, investment, or career pivot.
- Returning to a field after years away (lineages shift).
- Preparing to attend a major conference and wanting to know the politics.
- Evaluating prospective hires / advisors / collaborators by their lineage.
- Mapping for strategic decisions (e.g., where to fund, where to hire, where to invest).

**When NOT to use:**
- A specific narrow research question (use literature review / hypothesis generator).
- Fields too small to have multiple lineages.
- Operational rather than research questions.

**Audience:** Researchers, students, journalists, founders / investors evaluating science-based opportunities, policy analysts, anyone orienting to a new intellectual landscape.

---

## Inputs / Context

1. **Field / sub-field name.**
2. **Why orienting:** research, hiring, investing, journalism, career.
3. **Existing knowledge level.**
4. **Time budget for the orientation.**
5. **Sources available** (databases, key contacts, prior reading).

---

## Constraints

### Must
- Identify **3–6 major lineages** in the field. A lineage is a coherent tradition with shared assumptions, methods, or theoretical commitments — not just a topic.
- For each lineage: **founders / canonical figures**, **current anchor labs and individuals**, **canonical methods**, **2–4 recent influential papers**, **what they fight about with adjacent lineages**.
- Identify **fault lines** explicitly: theoretical, methodological, empirical, normative.
- Identify **emerging sub-areas** (rising attention, new conferences, new funding) and **declining sub-areas** (paradigms going out of favor or losing funding).
- Mark uncertainties: where the mapper isn't sure (e.g., "this lineage is fragmenting; current state unclear").
- Produce **starter reading list per lineage** for someone wanting to go deeper.

### Must Not
- Confuse topic with lineage (climate change is a topic; complex systems vs equilibrium economics is lineage-level).
- Pick lineages by author popularity rather than by tradition coherence.
- Pretend a fragmenting lineage is unified.
- Conceal where the mapper is uncertain.
- Map the field as if neutral observers — every map has a perspective; surface it.

---

## Instructions

### Step 1 — Define field boundaries
What's in, what's out. Often the boundary itself is contested.

### Step 2 — Identify lineages
Walk back to canonical works, founders, signature methods. Each lineage gets:
- Name (often informal — what people call it)
- Defining commitment (what makes it distinct)
- Founders / canonical figures
- Anchor institutions / labs today
- Active key individuals (assistant prof to senior)

### Step 3 — Method profiles per lineage
- Dominant methodology (experimental, observational, theoretical, computational, ethnographic, etc.)
- Distinguishing methodological commitments
- What methods they would *not* accept

### Step 4 — Recent influential papers per lineage
2–4 per lineage from the last 5 years that anchor current discussion. Annotate each with one-line significance.

### Step 5 — Fault lines
Map disagreements:
- **Theoretical:** different fundamental commitments
- **Methodological:** different views on what counts as evidence
- **Empirical:** disagreement on what the data shows
- **Normative:** different views on what the field is for

For each fault line: who's on which side, what's at stake.

### Step 6 — Emerging and declining
- Emerging sub-areas: signs are new conferences, new journals, new funding lines, junior researchers clustering, citation acceleration
- Declining: signs are aging cohort, funding cuts, journal consolidations, methodological obsolescence

### Step 7 — Cross-field interactions
Where this field touches adjacent fields. Often the most interesting work happens at boundaries.

### Step 8 — Starter reading per lineage
For someone wanting to go deeper into a single lineage: 1–2 books, 2–4 papers, 1 review article, 1 critique from outside the lineage.

### Step 9 — Mapper perspective and limits
Acknowledge the mapper's vantage point, what's plausibly missing, where current state is unclear.

---

## False-Positive Prevention

1. **Topic-lineage confusion.** "AI safety" is a topic; "alignment-as-control vs alignment-as-cooperation" might be lineages within it.
2. **Popularity ≠ lineage.** A famous individual may not represent a coherent tradition.
3. **Single-perspective map.** Insiders vs outsiders to a lineage will map differently. Triangulate.
4. **Fault-line concealment.** Pretending the field is unified hides what matters most.
5. **Static-map illusion.** Fields evolve; mark a date and acknowledge map ages.
6. **No-uncertainty signal.** Every field map has uncertain regions. Mark them.
7. **Emerging-area inflation.** Hype can look like emergence. Distinguish funding / conference signals from social-media buzz.
8. **Founder-only focus.** Current anchor people matter as much as canonical founders for orientation.

---

## Output Format

```
# Field landscape — [field name]

## Boundary
- In scope: [...]
- Out of scope: [...]
- Boundary contested? [yes — by whom / no]

## Lineages

### Lineage 1: [name]
- Defining commitment: [...]
- Founders / canonical figures: [...]
- Anchor institutions / labs today: [...]
- Active key individuals: [...]
- Dominant method: [...]
- Recent influential papers (2–4):
  - [Citation] — [significance]
  - [...]

### Lineage 2: [name]
[Same structure]

[3–6 lineages total]

## Fault lines
| Fault line | Type | Sides | At stake |
|------------|------|-------|----------|
| [name]     | theoretical | [Lineage A vs Lineage B] | [...] |
| [...]      | methodological | [...] | [...] |

## Emerging sub-areas
- [name] — signs: [conferences / funding / clusters]

## Declining sub-areas
- [name] — signs: [...]

## Cross-field interactions
- [Field X] — interaction at: [...]
- [Field Y] — interaction at: [...]

## Starter reading per lineage
### For [Lineage 1]
- Books: [1–2]
- Papers: [2–4]
- Review: [1]
- Outside critique: [1]

### For [Lineage 2]
[Same]

## Mapper perspective and limits
- Vantage point: [insider / outsider, partial expert]
- Plausibly missing: [...]
- Currently unclear: [...]
- Map date: [yyyy-mm-dd]
```

---

## Verification

- [ ] 3–6 lineages identified, distinguished by commitment not topic.
- [ ] Per-lineage: founders, current anchors, methods, recent papers.
- [ ] Fault lines explicit with sides and stakes.
- [ ] Emerging vs declining sub-areas with signal evidence.
- [ ] Cross-field interactions noted.
- [ ] Starter reading per lineage including outside critique.
- [ ] Mapper perspective and limits acknowledged.
- [ ] Map dated.
- [ ] No topic-lineage confusion.
