---
title: "Center of Biblical Theology Debate — Survey of Proposals"
category: biblical-studies/biblical-theology-method
description: "Survey the scholarly debate about whether biblical theology has a 'center' (Mitte) — proposals like covenant, kingdom, God's glory, promise, etc. — presenting each proposal as a position held by identifiable scholars/traditions, with strengths and critiques, all verify-required."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - center-of-theology
  - biblical-theology
  - mitte
  - covenant
  - kingdom
  - scholarly-debate
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_theme_canonical_trajectory.md
  - domain-biblical-studies/theology-research/biblical_topical_theology_synthesis.md
  - domain-biblical-studies/theology-research/biblical_interpretive_views_comparison.md
---

# Center of Biblical Theology Debate — Survey of Proposals

> **STRONG-GUARD prompt.** The model routinely fabricates which scholars hold which positions on the center of biblical theology, invents publication dates and titles, and asserts a center as settled when the debate is ongoing. Every attribution of a proposal to a scholar or tradition is verify-required. The model surveys the debate — it does not settle it.

**Objective:** Survey the scholarly debate about whether biblical theology has a "center" (German: Mitte) — mapping the major proposals (covenant, kingdom, God's glory, promise, God's presence, creation, etc.), the arguments for and against each, and the meta-question of whether any single center is even possible — so the user can engage the debate informed by the actual positions rather than model-generated fabrications.

**When to use:**
- You are studying biblical theology as a discipline and want to understand the Mitte debate.
- You are evaluating whether to organize your own biblical-theological work around a central theme.
- You are teaching a course on biblical theology method and need to survey the proposals.
- You encounter a claim that "the center of biblical theology is X" and want to assess it critically.

**When NOT to use:**
- You want to trace a specific theme across the canon — use `biblical_theme_canonical_trajectory.md`.
- You want to compare interpretive positions on a disputed passage — use `biblical_interpretive_views_comparison.md`.
- You want to study a doctrine across traditions — use `biblical_doctrine_study_neutral.md`.
- You want to understand the distinction between biblical and systematic theology — use `biblical_method_biblical_vs_systematic_theology.md`.

**Audience:** Seminary/academic (A).

---

## Inputs / Context

1. **Scope.** Whether the user wants to focus on the Old Testament center debate, the New Testament center debate, or the whole-Bible center debate (these are related but distinct conversations).
2. **Specific proposals of interest (optional).** If the user is already aware of specific proposals (covenant, kingdom, promise, etc.) and wants to focus on certain ones.
3. **Depth.** Survey (map the major proposals and their proponents) or deep (trace the arguments, counter-arguments, and methodological presuppositions behind each proposal).
4. **Tradition (optional).** If the user works within a tradition that foregrounds a particular center, the model can note this — but all proposals receive proportional treatment.

---

## Constraints

### Must
- Present each proposed center as a position held by identifiable scholars or traditions — name names, flag as verify-required.
- For each proposal, identify: what the proposed center is, who holds it, the strongest biblical argument for it, and the strongest critique against it.
- Include the "no center" position (multi-thematic, polyphonic, or anti-center approaches) as a serious scholarly option, not merely a footnote.
- Distinguish between OT-specific, NT-specific, and whole-Bible proposals where relevant.
- Note that confessional commitments often shape which center a scholar proposes — Reformed scholars tend toward covenant, dispensational scholars toward kingdom/dispensation, etc. Present this observation without using it to dismiss any proposal.

### Must Not
- Assert that the debate is settled or that one proposal is the consensus — the debate is ongoing and genuinely contested.
- Fabricate which scholars hold which positions, invent publication dates, attribute proposals to the wrong scholars, or invent book or article titles.
- Present the Mitte question as purely academic with no practical consequences — the choice of center shapes how one reads every passage.
- Reduce the debate to two options ("covenant vs. kingdom") when the landscape is much broader.

### Tradition-neutral stance (Must / Must Not)
- **Must:** give each proposal proportional treatment regardless of its confessional home. A proposal held by a minority tradition receives as serious a treatment as one held by a dominant tradition.
- **Must Not:** use confessional affiliation to discount a proposal ("this is just a Reformed idea" or "this is just a dispensationalist idea"). Note the affiliation descriptively, not dismissively.

---

## Instructions

### Step 1 — Frame the Mitte debate
Explain what the "center of biblical theology" debate is about:
- What does it mean to claim that biblical theology has a "center"? What work does the center do in organizing the discipline?
- When and why did the debate emerge? (verify-required — do not invent dates or attribute the origin to a specific scholar without flagging)
- Why does the debate matter practically — how does the choice of center shape the reading of specific passages and the structure of a biblical theology?

### Step 2 — Map the major proposals
For each major proposed center, provide:
- **The proposal:** what the center is claimed to be, stated clearly.
- **Proponents:** which scholars and/or traditions hold this position (verify-required — every name is flagged).
- **Biblical argument:** the strongest biblical evidence cited for this proposal — which texts, which patterns, which structural features of the canon?
- **Strengths:** what does this proposal explain well? What textual data does it account for?
- **Critiques:** what does this proposal struggle to account for? What textual data does it marginalize or force-fit?

Cover at minimum:
- Covenant
- Kingdom of God / reign of God
- God's glory
- Promise (and fulfillment)
- God's presence
- Creation / new creation
- Election / people of God
- Salvation / redemption
- The "no single center" / polyphonic / multi-thematic position

### Step 3 — Analyze the meta-question
Address the prior question: is a single center even the right way to organize biblical theology?
- Arguments for seeking a center: it provides coherence, avoids fragmentation, reveals the canon's unity.
- Arguments against: it inevitably marginalizes some texts, imports a foreign organizing principle, and may reflect the scholar's tradition more than the text's own structure.
- Middle positions: multiple centers, a center with a circumference, a narrative arc rather than a thematic center.

### Step 4 — Implications for the user
Based on the user's stated scope and tradition:
- If you choose a center, what are you committing to — and what are you risking?
- If you refuse a center, what alternative organizing principle do you adopt — and what are its risks?
- How does your tradition's default center shape the readings you produce, and how can awareness of alternatives improve your work?

---

## Output Format

```
# Center of Biblical Theology Debate — [OT / NT / Whole Bible]

## What the debate is about
- Definition: [..]
- Why it matters: [..]
- Historical emergence (VERIFY-REQUIRED): [..]

## Major proposals
### [Proposal 1, e.g., Covenant]
- Proponents (VERIFY-REQUIRED): [..]
- Biblical argument: [texts by address, patterns cited]
- Strengths: [..]
- Critiques: [..]

### [Proposal 2, e.g., Kingdom of God]
[same structure]

### [Proposal N, e.g., No single center / polyphonic]
[same structure]

## The meta-question — is a center possible?
- Arguments for: [..]
- Arguments against: [..]
- Middle positions: [..]

## Implications
- Choosing a center commits you to: [..]
- Refusing a center commits you to: [..]
- Awareness of alternatives: [..]

## Verify-required items
- Scholar attributions: [VERIFY against published works — do not trust model-generated names]
- Publication claims: [VERIFY all dates, titles, and publication venues]
- Origin of the debate: [VERIFY — do not assert specific dates or founding figures without checking]
```

---

## Verification

- [ ] Each proposed center is attributed to identifiable scholars or traditions, all verify-required.
- [ ] The "no center" position is treated as a serious scholarly option.
- [ ] No proposal is presented as the settled consensus — the debate is framed as ongoing.
- [ ] Strengths and critiques are presented for every proposal, including the user's own tradition if declared.
- [ ] The meta-question (whether a center is possible) is addressed honestly.
- [ ] No fabricated scholar attributions, publication titles, dates, or positions.
- [ ] Confessional affiliations are noted descriptively, not dismissively.
- [ ] Tradition-neutral language is maintained throughout.

---

## False-Positive Prevention

DON'T:
- Assert that one center is the consensus or the "biblical" answer — the debate is genuinely ongoing.
- Fabricate which scholars hold which positions — this is the highest-risk fabrication surface in this prompt.
- Reduce the debate to only two or three proposals when the landscape is broader.

DO:
- Flag every scholar attribution as verify-required — models are unreliable on who-holds-what in this debate.
- Present the "no center" position with as much seriousness as any center proposal.
- Show how confessional location shapes the choice of center without dismissing any proposal on that basis.
