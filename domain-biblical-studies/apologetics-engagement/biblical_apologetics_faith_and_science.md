---
title: "Faith and Science Question Framing"
category: biblical-studies/apologetics-engagement
description: "Frame a specific faith-and-science question by presenting the range of believing-scholar positions — young earth, old earth, evolutionary creation, etc. — as positions held by identifiable traditions and scholars, never presenting one as THE scientific or THE biblical position."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - faith-and-science
  - origins
  - evolution
  - creation
  - cosmology
  - believing-scholars
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_interpretive_views_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_genre_aware_reading.md
  - domain-biblical-studies/learner-self-study/biblical_learner_honest_questions_doubt_explorer.md
---

# Faith and Science Question Framing

> **STRONG-GUARD prompt.** The model must not fabricate scientific findings, misrepresent scientific consensus, or attribute scientific positions to researchers who do not hold them. The model must not fabricate theological positions or attribute views to scholars or traditions that do not hold them. The model must not invent historical evidence for or against any position. The model must not present one faith-and-science position as having "won" — every position is presented as held by identifiable traditions and scholars, with its strengths, weaknesses, and the state of the conversation verify-required.

**Objective:** Frame a specific faith-and-science question by presenting the range of positions held by believing scholars and traditions — so the user sees the landscape of serious Christian engagement with science, understands what each position claims and on what basis, and can investigate further. The model never presents one position as THE scientific or THE biblical position.

**When to use:**
- Someone asks about creation and evolution, age of the earth, cosmology, neuroscience and the soul, or any other faith-and-science question.
- You are preparing to teach or preach on a faith-and-science topic and want to present the range of believing-scholar positions fairly.
- You want to understand what serious Christian scholars in different traditions actually argue (not internet caricatures).

**When NOT to use:**
- You want to compare Christianity with naturalism as a worldview — use `biblical_apologetics_comparative_worldview.md`.
- You want exegesis of Genesis 1-3 specifically — use exegesis-interpretation prompts with genre awareness.
- You want to address the specific objection "science disproves God" — use `biblical_apologetics_objection_engagement.md`.

**Audience:** Pastor/preacher (P), seminary/academic (A), self-directed learner (S).

---

## Inputs / Context

1. **The question.** Which faith-and-science question? (Origins/creation/evolution, age of earth, cosmology/Big Bang, Adam and Eve historicity, flood/geology, neuroscience and soul/mind, miracles and natural law, human uniqueness/image of God, animal suffering, bioethics, AI and personhood, etc.)
2. **Specific tension (optional).** If a specific tension prompted the question ("my biology professor says X, my pastor says Y"), state it.
3. **Depth.** Survey (landscape of positions) or deep (trace the biblical, theological, and scientific reasoning for each position).
4. **Tradition (optional).** If the user identifies their tradition, note it — but all positions are presented.

---

## Constraints

### Must
- Present each position as held by identifiable traditions and named scholars (verify-required).
- Present the biblical reasoning for each position — which texts, which hermeneutical approach, which genre reading.
- Present the scientific reasoning for each position — what scientific evidence does each position engage with, and how.
- Distinguish between what is scientific consensus, what is debated within science, and what is a theological/philosophical question that science does not adjudicate.
- Acknowledge that believing scholars hold each of these positions in good faith.

### Must Not
- Present one position as THE scientific position — note what is consensus vs. debated.
- Present one position as THE biblical position — note that different hermeneutical approaches yield different readings.
- Fabricate scientific studies, findings, or researcher positions.
- Fabricate theological positions or attribute views to scholars who do not hold them.
- Dismiss any position as "obviously wrong" or "anti-science" or "anti-Bible" — describe and let the user evaluate.
- Conflate scientific questions with theological questions (e.g., "how" vs. "why," mechanism vs. meaning).

### Tradition-neutral stance (Must / Must Not)
- **Must:** present young earth, old earth, evolutionary creation, and other positions as held by serious Christians with identifiable theological commitments and scholarly credentials.
- **Must Not:** use language that signals one position is more intellectually respectable or more biblically faithful than others.

---

## Instructions

### Step 1 — Clarify the question
Restate the faith-and-science question. Identify what type of question it is: a scientific question, a biblical-interpretive question, a theological question, or (most often) a combination.

### Step 2 — Distinguish what science says from what theology asks
Before presenting positions, clarify:
- What does current scientific consensus say on the relevant empirical question? (Verify-required — do not fabricate.)
- What theological/philosophical question does science not adjudicate?
- Where does the tension between faith and science actually lie — and where is it a false conflict based on category confusion?

### Step 3 — Map the believing-scholar positions
Present each major position, attributed to traditions and named scholars:
- **Position name** (e.g., young earth creationism, old earth creationism, evolutionary creation, framework interpretation, etc.).
- **Who holds it** — which traditions, organizations, and named scholars (verify-required).
- **Biblical reasoning** — which texts, which genre reading, which hermeneutical principles.
- **Scientific engagement** — how does this position engage with the relevant scientific evidence?
- **Strengths** — what does this position do well?
- **Challenges** — what are the strongest objections from other believing scholars?

### Step 4 — Note common ground among believing scholars
Despite their differences on this question, where do believing scholars typically agree?
- Common theological commitments (God as creator, human dignity, Scripture's authority — though they interpret these differently).
- Common concerns (intellectual honesty, pastoral care, avoiding false dichotomies).

### Step 5 — Identify next steps for the user
- What resources from each tradition would help the user investigate further?
- What questions should the user consider in forming their own position?

---

## Output Format

```
# Faith and Science — [question]

## What science says and what theology asks
- Scientific consensus (VERIFY): [..]
- Theological question science does not adjudicate: [..]
- Where the actual tension lies: [..]

## Believing-scholar positions
### [Position 1]
- Held by: [traditions/scholars — VERIFY]
- Biblical reasoning: [texts, genre, hermeneutic]
- Scientific engagement: [..]
- Strengths: [..] | Challenges: [..]

### [Position 2]
[..]

### [Position 3]
[..]

## Common ground among believing scholars
- Shared commitments: [..] | Shared concerns: [..]

## For further investigation
- [resources from each tradition]
- [questions to consider in forming a position]

## Verify-required items
- Scientific claims: [VERIFY against current peer-reviewed literature]
- Scholar attributions: [VERIFY — do not trust model memory]
- Organization positions: [VERIFY against current official statements]
```

---

## Verification

- [ ] Each position is attributed to identifiable traditions and scholars.
- [ ] Biblical reasoning is traced for each position with texts cited by address.
- [ ] Scientific consensus is distinguished from scientific debate.
- [ ] No position is presented as THE scientific or THE biblical position.
- [ ] All scientific claims and scholar attributions are verify-required.
- [ ] Common ground among believing scholars is identified.
- [ ] No fabricated studies, findings, or position attributions.

---

## False-Positive Prevention

DON'T:
- Present one position as intellectually superior or more biblically faithful — let each speak for itself.
- Fabricate scientific consensus or misrepresent where scientists actually disagree.
- Conflate scientific and theological questions — keep the categories distinct.

DO:
- Present each position as held by serious Christians in good faith.
- Distinguish scientific consensus from scientific debate from theological/philosophical questions.
- Flag every empirical claim and scholar attribution as verify-required.
