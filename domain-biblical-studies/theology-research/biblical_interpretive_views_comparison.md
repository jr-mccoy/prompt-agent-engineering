---
title: "Comparing Interpretive Views (Debate Format) — Steelman Each Side"
category: biblical-studies/theology-research
description: "Stage a fair, structured comparison of the major positions on a disputed biblical or theological question — each steelmanned with its best arguments and evidence, its responses to objections, and the points where the evidence is genuinely contested — without declaring a winner or fabricating sources."
techniques:
  - RP-03
  - RT-03
  - RT-05
  - QA-04
difficulty: advanced
tags:
  - debate
  - interpretation
  - comparison
  - steelman
  - neutrality
  - anti-fabrication
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_doctrine_study_neutral.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
  - domain-biblical-studies/theology-research/biblical_difficult_passage_analysis.md
  - domain-biblical-studies/theology-research/biblical_position_stress_test.md
---

# Comparing Interpretive Views (Debate Format)

**Objective:** Set the major positions on a disputed question against each other in a structured, fair debate — each steelmanned, each responding to the others — so the user sees where the real strengths, weaknesses, and unresolved cruxes lie, without being handed a verdict.

> **STRONG-GUARD prompt.** A debate format invites fabricated scholars, quotations, councils, and citations marshaled to win for each side. This prompt steelmans positions by attributing them to identifiable streams, references texts by address, and flags any named source as verify-required.

**When to use:**
- A question is genuinely disputed and you want a rigorous, balanced comparison.
- Preparing to teach/write on a controversy responsibly.

**When NOT to use:**
- You want the doctrine's landscape more descriptively — use `biblical_doctrine_study_neutral.md`.
- The dispute is about one passage's reading — use `biblical_multiview_interpretation_map.md`.

**Audience:** Seminary/academic (A), pastors (P).

---

## Inputs / Context

1. **The disputed question.** Stated precisely.
2. **Positions to compare.** Which views (2–4).
3. **Declared tradition (optional).** May note where that stream lands; all views still steelmanned and no verdict given.

---

## Constraints

### Must
- Steelman each position: its best case, biblical/logical support (by address, verify-required), and strongest evidence.
- Give each position's **response** to the others' strongest arguments (a real exchange, not parallel monologues).
- Identify the **cruxes** — the specific points where the question is actually decided and where evidence is genuinely contested.
- Acknowledge uncertainty; state what would move the balance.

### Must Not
- Declare a winner or let one side's case be stronger by neglect.
- Invent scholars, quotations, councils, citations, or cross-references.
- Build a straw man or a false middle.

### Tradition-neutral stance (Must / Must Not)
- **Must:** treat each as a serious position, fairly represented and attributed.
- **Must Not:** endorse one as correct; manufacture consensus.

---

## Instructions

### Step 1 — State the question
One precise sentence.

### Step 2 — Opening cases
Each position's best case with support (by address, verify-required).

### Step 3 — Exchange
Each position's response to the others' strongest points.

### Step 4 — Cruxes
The specific points the question turns on, and where evidence is genuinely contested.

### Step 5 — Honest close
What remains unresolved and what would shift the balance — no verdict.

---

## Output Format

```
# Views Comparison — [question]

## The question
> [precise]

## Opening cases
- [Position A / stream]: [best case + support (address, verify)]
- [Position B / stream]: [best case + support]

## Exchange
- A responds to B: [..] | B responds to A: [..]

## Cruxes
- The question turns on: [..] | Genuinely contested evidence: [..]

## Honest close
- Unresolved: [..] | What would move it: [..]
```

---

## Verification

- [ ] Each position steelmanned with support by address (verify-required).
- [ ] A real exchange of responses, not parallel monologues.
- [ ] Cruxes and contested evidence identified.
- [ ] No winner declared; no false middle.
- [ ] No fabricated scholars/quotes/councils/citations.

---

## False-Positive Prevention

❌ **DON'T:**
- Give one side the last word or the stronger treatment.
- Quote scholars or sources from memory as established.
- Resolve the debate with a tidy verdict the evidence doesn't warrant.

✅ **DO:**
- Steelman every position and stage a genuine exchange.
- Cite support by address and mark verify-required.
- Name the cruxes and leave the contested question open.
