---
title: "Thematic / Topical Study Across Passages — Without Proof-Texting"
category: biblical-studies/study-methods-teaching
description: "Gather and organize the passages that bear on a biblical theme or topic, weighing each by how directly it addresses the theme and in what context, while guarding against proof-texting and refusing to invent cross-references. Distinguishes passages that genuinely teach the theme from those merely associated with it."
techniques:
  - RT-02
  - RT-05
  - DS-19
  - QA-05
difficulty: intermediate
tags:
  - topical-study
  - thematic
  - cross-reference
  - anti-proof-texting
  - anti-fabrication
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_topical_theology_synthesis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md
  - domain-biblical-studies/theology-research/biblical_theme_canonical_trajectory.md
---

# Thematic / Topical Study Across Passages

**Objective:** Assemble the passages relevant to a theme or topic, organized and weighted by how directly and contextually each addresses it — so the study reflects what Scripture actually teaches on the theme rather than a string of proof-texts.

> **STRONG-GUARD prompt.** Topical studies invite fabricated cross-references and proof-texting (citing verses out of context to support a point). This prompt references every passage by address, marks them verify-required, and weighs context.

**When to use:**
- Studying what the Bible says about a topic (e.g., generosity, fear, the Sabbath).
- Preparing a topical lesson or sermon responsibly.
- Checking a topical claim that rests on a verse list.

**When NOT to use:**
- You want a doctrinal synthesis across traditions — use `biblical_topical_theology_synthesis.md`.
- You want one theme's development across the canon — use `biblical_theme_canonical_trajectory.md`.

**Audience:** Group leaders (G), pastors (P), seminary/academic (A).

---

## Inputs / Context

1. **The theme/topic.** Stated precisely.
2. **Passages in hand (optional).** Any the user already has, to organize and assess.
3. **Declared tradition (optional).** May shape emphasis; contested passages handled descriptively.

---

## Constraints

### Must
- Reference every passage **by address** and mark it **verify-required** (existence + wording + that it actually addresses the theme in context).
- Weight passages: **central** (directly teaches the theme), **supporting** (relevant in context), **associated** (mentions a keyword but is about something else).
- Read each candidate in its own context before counting it; flag any that only appear relevant via a keyword.
- Note tensions or development across passages rather than forcing a single flat answer.

### Must Not
- Invent chapter:verse references or claim a passage teaches the theme when context says otherwise (proof-texting).
- Quote passages from memory as authoritative; reference by address.
- Force a tradition's topical conclusion.

### Tradition-neutral stance (Must / Must Not)
- **Must:** present the topical picture descriptively, noting where traditions emphasize different passages or readings.
- **Must Not:** assemble a verse list engineered to prove one tradition's position.

---

## Instructions

### Step 1 — Define the theme
State the topic precisely; note sub-questions it raises.

### Step 2 — Gather candidates
List candidate passages by address with a one-line note on relevance. Mark all verify-required.

### Step 3 — Context check & weighting
For each, assess (in context) whether it is central / supporting / associated. Drop or downgrade keyword-only matches.

### Step 4 — Organize
Group the central/supporting passages into the facets of the theme they address.

### Step 5 — Tensions & development
Note where passages add nuance, qualify each other, or show development across the canon.

### Step 6 — Honest summary
Summarize what the gathered passages collectively support — and where the picture is partial or contested.

---

## Output Format

```
# Topical Study — [theme]

## Candidate passages (all verify-required)
| Address | Weight | In-context relevance |
|---------|--------|----------------------|
| [addr]  | central/supporting/associated | [note] |

## Organized by facet
- [facet]: [addresses]

## Tensions / development
- [..]

## Honest summary
- Collectively supported: [..] | Partial/contested: [..]
```

---

## Verification

- [ ] Every passage by address and marked verify-required.
- [ ] Each weighted central/supporting/associated after a context check.
- [ ] Keyword-only matches downgraded or dropped.
- [ ] Tensions/development noted, not flattened.
- [ ] No invented references; no proof-texting; no tradition forced.

---

## False-Positive Prevention

❌ **DON'T:**
- Produce a long verse list from memory and present it as established.
- Count a passage because it contains a keyword, ignoring its actual subject.
- Flatten genuine tension into a single tidy doctrine.

✅ **DO:**
- Reference by address, mark verify-required, and check context.
- Weight passages central > supporting > associated.
- Preserve tensions and note where the picture is contested.
