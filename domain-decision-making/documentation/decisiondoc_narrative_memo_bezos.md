---
title: "Narrative Decision Memo — Six-Page Amazon-Style Prose Memo"
category: decision-making/documentation
description: "Produce a narrative (prose, not bullets) decision memo in the Amazon six-pager tradition: problem, context, options, recommendation, and a mandatory FAQ. Designed to be read silently in the first minutes of a meeting and then interrogated. The FAQ is where the document does its hardest work — it pre-answers the questions a sharp, skeptical reader would raise. Distinct from the structured options memo: this is narrative-first, optimized for silent reading and live challenge."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - decision-documentation
  - narrative-memo
  - six-pager
  - executive-communication
  - faq
updated: "2026-05-10"
reasoning:
  styles: [narrative, dialectical, persuasive]
  stakes: high
  horizon: variable
  uncertainty: variable
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: org
  output_format: narrative
  user_role: [executive, founder, pm, strategist, analyst]
  mode: [synthesize, document, decide]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-decision-making/documentation/decisiondoc_one_pager.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
---

# Narrative Decision Memo (Six-Pager)

**Objective:** Produce a **narrative** decision memo — written in complete prose paragraphs, not bullet fragments — in the tradition of the Amazon six-pager. The memo is meant to be **read silently** for the first ten-or-so minutes of a meeting and then **interrogated** by the room. Its discipline is twofold: (1) prose forces the author to make the logic connect — you cannot hide a gap behind a bullet — and (2) a **mandatory FAQ** forces the author to surface and answer the questions a sharp, skeptical reader would actually raise. The FAQ is not an afterthought; it is where the memo does its hardest work and where weak reasoning gets exposed before the room exposes it.

This is distinct from `decisiondoc_options_memo.md`, which is a rigid structured artifact optimized for scanning. The narrative memo is optimized for *deep silent reading and live challenge* — a different instrument for higher-stakes, more contested decisions.

**When to use:**
- A high-stakes decision where senior people will read carefully and then push hard.
- A "read it in the room, then discuss" meeting culture (the memo replaces a presentation).
- A decision contested enough that the reasoning must survive a hostile read.
- Strategy shifts, large investments, reorganizations, major product or market bets.

**When NOT to use:**
- A decision small enough that prose-craft is overkill — use the one-pager or a log entry.
- An audience that won't read a long document — use `decisiondoc_one_pager.md`.
- You need a scannable matrix for quick comparison rather than a read-and-debate artifact — use the structured options memo.
- The deliberation hasn't happened yet. Write the memo to communicate a worked-through position, not to think out loud.

**Audience:** Executives, founders, PMs, and strategists writing for a room of senior readers who will read silently and interrogate.

---

## Inputs / Context

1. **The decision** and why it's on the table now.
2. **The recommendation** (the memo argues a position; it is not neutral).
3. **The options**, including the status quo / do-nothing.
4. **The evidence** — data, analysis, customer/market signal — that the prose will weave in.
5. **The skeptics** — who will read this critically, and what they'll attack. This feeds the FAQ.
6. **The decision owner** and the decision timeline.

---

## Structure (six-pager flow)

1. **Introduction / problem** — what decision, why now, what's at stake.
2. **Context / background** — the situation, the relevant history, the data, in prose.
3. **Options** — the realistic paths, each described fairly (steelmanned), including status quo.
4. **Recommendation** — the argued position and why it beats the alternatives, in prose.
5. **FAQ** — the mandatory engine room: the hardest anticipated questions, answered in full.
6. **Appendix** (does not count toward the page budget) — tables, models, raw data, detail.

Target ~6 pages of narrative (excluding appendix). Prose throughout; tables allowed only in the appendix.

---

## Constraints

### Must
- Write in **complete prose paragraphs**. No bullet lists in the body (Introduction through Recommendation). Bullets and tables live in the appendix only.
- Make the argument **connect** — each paragraph should follow from the last. A reader should be carried, not assembled.
- Present options **fairly**: steelman every option, including the ones you reject and including the status quo.
- Make the **FAQ mandatory and substantive.** It must contain the genuinely hard questions — the ones a skeptic would actually ask — and answer each in full prose, not deflect. A FAQ of soft questions is a tell that the memo is hiding from scrutiny.
- In the FAQ, include at least one question of the form "**Why not [the most attractive alternative]?**" and at least one "**What would have to be true for this to be wrong?**"
- Keep the **narrative body to roughly six pages**; push detail to the appendix.
- Name the **decision owner** and the **timeline**.
- Lead the Introduction with enough that a reader knows the decision and the recommendation within the first paragraph — silent reading rewards an early thesis.

### Must Not
- Revert to bullet fragments in the body to dodge the work of making prose cohere. The prose discipline is the point.
- Stuff a soft, self-serving FAQ. The FAQ exists to pre-empt the strongest objections, not to lob softballs.
- Strawman the rejected options or omit the status quo.
- Bury the recommendation so deep that a silent reader is lost. State the thesis early, then earn it.
- Let the appendix smuggle the real argument. The body must stand on its own; the appendix supports, it doesn't substitute.
- Exceed the page budget with narrative — discipline of length forces prioritization.

---

## Instructions

### Step 1 — Introduction / problem (prose)
Open with the decision and the recommendation thesis in the first paragraph. Then: why this decision, why now, what's at stake if it's made well or badly.

### Step 2 — Context / background (prose)
Tell the relevant story: the situation, the history that matters, the data — woven into sentences, not dumped as a list. The reader should finish this section understanding the world the decision lives in.

### Step 3 — Options (prose)
Describe each realistic path in its own paragraph(s). Steelman each, including status quo / do-nothing. The reader should feel each option's appeal before reading why you rejected the others.

### Step 4 — Recommendation (prose)
Argue the position. Why it beats each alternative on the dimensions that matter. Where it concedes ground, say so plainly — a memo that admits its option's weaknesses reads as more trustworthy and survives interrogation better.

### Step 5 — FAQ (the engine room)
Draft 6–12 questions a skeptical senior reader would actually ask. Prioritize the painful ones. Mandatory inclusions:
- "Why not [most attractive alternative]?"
- "What would have to be true for this recommendation to be wrong?" (the disconfirming conditions)
- At least one question on cost / risk / second-order effects.
- At least one on "why now / why not wait?"
Answer each in full prose. An answer that deflects ("we'll figure that out later") is a flag to either resolve the question or move the decision's confidence down.

### Step 6 — Appendix
Move all tables, models, MCDA output, raw data, and granular detail here. The body references the appendix; it doesn't depend on the reader having read it.

### Step 7 — Owner and timeline
State who decides and by when. Note how the meeting should run (silent read duration, then discussion).

### Step 8 — Read-aloud test
Re-read the body as if hostile. Where a paragraph asserts without support, either support it or move it to the FAQ as an acknowledged open question.

---

## False-Positive Prevention

1. **Bullet relapse.** Slipping into bullet fragments to avoid making prose cohere. Body is prose; lists live in the appendix.
2. **Softball FAQ.** Filling the FAQ with easy questions. The FAQ must contain the hardest anticipated objections, including "why not the best alternative" and "what would make this wrong."
3. **Buried thesis.** Forcing the silent reader to hunt for the recommendation. State it in the first paragraph, then earn it.
4. **Strawmanned options.** Rejecting alternatives by weakening them. Steelman each, including status quo.
5. **Appendix-as-argument.** Putting the real reasoning in the appendix so the body looks clean. The body must stand alone.
6. **Confidence theater.** Prose that never concedes a weakness reads as marketing. Name what the recommendation gives up.
7. **Deflecting answers.** FAQ answers that punt ("TBD," "out of scope"). Either answer, or lower the stated confidence and flag the open question.
8. **Length sprawl.** A "six-pager" running fifteen pages. The page discipline forces prioritization; respect it.

---

## Output Format

```
# [Decision title]
**Decision owner:** [name / role]  |  **Decision by:** [date]
**Meeting format:** silent read (~10 min), then discussion

## 1. Introduction
[Prose. First paragraph states the decision and the recommendation thesis, why now, what's at stake.]

## 2. Context
[Prose. The situation, relevant history, and data woven into narrative.]

## 3. Options
[Prose. Each realistic path, steelmanned, in its own paragraph(s), including status quo.]

## 4. Recommendation
[Prose. The argued position; why it beats each alternative; the weaknesses it honestly concedes.]

## 5. FAQ
**Q: Why not [most attractive alternative]?**
[Full prose answer.]

**Q: What would have to be true for this recommendation to be wrong?**
[Full prose answer — the disconfirming conditions.]

**Q: [hard question on cost / risk / second-order effect]**
[Full prose answer.]

**Q: Why now — why not wait?**
[Full prose answer.]

**Q: [additional hard questions, 6–12 total]**
[Full prose answers.]

## Appendix (excluded from page budget)
- [Tables, MCDA output, models, raw data, detailed cost breakdowns, sources]
```

---

## Verification

- [ ] Body (Intro → Recommendation) is prose; no bullet fragments outside the appendix.
- [ ] Recommendation thesis appears in the first paragraph.
- [ ] Every option steelmanned, including status quo / do-nothing.
- [ ] FAQ present and substantive, with the hard questions — not softballs.
- [ ] FAQ includes "why not [best alternative]?" and "what would make this wrong?".
- [ ] Recommendation honestly concedes at least one weakness.
- [ ] Tables/models/data pushed to the appendix; body stands alone.
- [ ] Body held to ~six pages.
- [ ] Decision owner and timeline named.
- [ ] No deflecting FAQ answers left unflagged.
