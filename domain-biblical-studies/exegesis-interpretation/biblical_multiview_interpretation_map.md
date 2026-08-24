---
title: "Multi-View Interpretation Map — Lay Out Competing Readings of a Contested Passage"
category: biblical-studies/exegesis-interpretation
description: "Map the major competing interpretations of a contested passage or question side by side, each with its strongest textual basis, key assumptions, and the interpretive stream that holds it — taking no side, attributing positions to identifiable streams rather than fabricated scholar names, and marking where the disagreement is genuinely unresolved."
techniques:
  - RP-03
  - RT-02
  - RT-03
  - QA-04
  - QA-05
difficulty: advanced
tags:
  - interpretation
  - multi-view
  - hermeneutics
  - neutrality
  - contested-passages
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/theology-research/biblical_interpretive_views_comparison.md
  - domain-biblical-studies/theology-research/biblical_difficult_passage_analysis.md
---

# Multi-View Interpretation Map

**Objective:** For a contested passage or interpretive question, lay out the major credible readings side by side — each with its strongest textual support, load-bearing assumptions, and the interpretive stream that characteristically holds it — so the user can see the genuine shape of the disagreement without being steered to a verdict.

> **STRONG-GUARD prompt.** Attributing positions to *named scholars or quoted sources* is a fabrication trap. This prompt attributes readings to *identifiable interpretive streams* and flags any named-person/quoted attribution as verify-required.

**When to use:**
- A passage has more than one serious reading and you want them mapped fairly.
- Preparing to teach or preach a disputed text and you need to represent views honestly.
- You suspect you've only heard one tradition's reading and want the others.

**When NOT to use:**
- You want the standard exegetical workflow on a non-contested passage — use `biblical_passage_exegesis_workflow.md`.
- The question is doctrinal/topical across many texts — use `biblical_doctrine_study_neutral.md` or `biblical_interpretive_views_comparison.md`.

**Audience:** Pastors (P), seminary/academic (A), and equipped group leaders (G).

---

## Inputs / Context

1. **The passage / question.** Reference and the text in a named translation (pasted by the user), plus the specific point in dispute.
2. **Views already known (optional).** Any readings the user has encountered, so the map can place and complete them.
3. **Declared tradition (optional).** If supplied, the model may note which view that stream typically holds and why — but must still present the alternatives fully and refrain from ruling.
4. **Scope.** How many views to map and how deep.

---

## Constraints

### Must
- Identify the **2–5 major credible readings**, no straw men. Steelman each: present each view in the form its best advocates would recognize.
- For each view give: the reading, its strongest textual basis (by address), its load-bearing assumption(s), and the interpretive stream(s) that hold it.
- Mark where the disagreement turns (the pivot — a word, a structure, a background assumption, a canonical link).
- State which view(s), if any, have broader scholarly support and which are minority — labeled, not ranked as "right."
- Acknowledge uncertainty: name what evidence would move the question and what remains genuinely unresolved.

### Must Not
- Take a side, declare a winner, or present one reading as the plain meaning (unless the user declared a tradition — and even then, present alternatives fully).
- Fabricate named scholars, commentators, councils, or quotations. Attribute to streams; flag any name/quote as verify-required.
- Invent the textual basis, cross-references, or original-language data supporting a view. Reference by address; route language claims to the word-study prompt.
- Manufacture a false middle ("the truth is somewhere in between") when the views are genuinely exclusive.

### Tradition-neutral stance (Must / Must Not)
- **Must:** present each position fairly, attributed to an identifiable stream; treat each as a position, not fact; label confidence and support level.
- **Must Not:** privilege/endorse one stream as correct; collapse real disagreement into false consensus.

---

## Instructions

### Step 1 — State the dispute precisely
Name exactly what is contested (not the whole passage — the specific interpretive crux). One sentence.

### Step 2 — Enumerate the views
List the 2–5 major credible readings. For each, a one-line statement of the reading.

### Step 3 — Build each view's case
For each view: strongest textual basis (by address), load-bearing assumption(s), the stream(s) that hold it, and its best response to the strongest objection. Steelman, don't straw-man.

### Step 4 — Locate the pivot
Identify what the disagreement actually turns on — the word, syntactic ambiguity, structural reading, historical assumption, or canonical connection that, if settled, would settle the dispute.

### Step 5 — Support landscape
Note which views are widely held vs. minority (labeled, not endorsed), and where each tradition tends to land — descriptively.

### Step 6 — Uncertainty & what would move it
State what is genuinely unresolved and what kind of evidence or argument would shift the balance. Do not resolve it artificially.

---

## Output Format

```
# Interpretation Map — [reference / question]

## The dispute
> [precise statement of the crux]

## Views
### View 1 — [label]
- Reading: [..]
- Strongest basis (by address): [..]
- Load-bearing assumption: [..]
- Held by: [stream(s)] (named advocates? verify-required)
- Best answer to its strongest objection: [..]

### View 2 — [label]
[same structure]
[... up to 5]

## The pivot
- The disagreement turns on: [word / structure / background / canonical link]

## Support landscape
- Widely held: [..] | Minority: [..] | Tradition tendencies (descriptive): [..]

## Genuinely unresolved
- What remains open: [..]
- What would move the question: [..]
```

---

## Verification

- [ ] 2–5 credible views, each steelmanned (no straw men).
- [ ] Each view: reading + basis (by address) + assumption + stream.
- [ ] The interpretive pivot identified.
- [ ] No side taken; no view presented as the plain meaning (unless tradition declared).
- [ ] No fabricated scholars/quotes; names/quotes flagged verify-required.
- [ ] No invented textual basis or cross-references.
- [ ] Genuine uncertainty acknowledged; no false middle.

---

## False-Positive Prevention

❌ **DON'T:**
- Quietly favor the reading you find most persuasive.
- Straw-man a view so another looks obviously correct.
- Attribute a reading to a specific named scholar or quote you can't verify.
- Invent the verses or Greek/Hebrew data a view supposedly rests on.
- Split the difference when the views are mutually exclusive.

✅ **DO:**
- Steelman every view in its advocates' own terms.
- Attribute to interpretive streams; flag any name/quote as verify-required.
- Cite supporting texts by address and mark them verify-required.
- Name the pivot the disagreement turns on.
- Leave genuinely open questions open, with what would move them.

---

## Techniques Used

- **RP-03 (Multi-Persona Debate):** Each competing interpretation is given its own voice — stated in the form its best advocates would recognize, with its strongest textual basis and its best response to the strongest objection — producing a structured debate between steelmanned positions rather than a critique of straw men.
- **RT-02 (Multi-Dimensional Analysis Framework):** Each view is analyzed across multiple dimensions: the reading, its textual basis, its load-bearing assumptions, the streams that hold it, and its response to objections — preventing shallow summaries that omit crucial information.
- **RT-03 (Tree of Thoughts):** Generates and lays out 2–5 interpretive approaches simultaneously, compares them by textual support and underlying assumptions, then identifies the interpretive pivot — the branch point where the readings diverge.
- **QA-04 (Uncertainty Acknowledgment):** Explicitly requires naming what remains genuinely unresolved and what evidence would move the question; prohibits manufacturing a false middle when views are mutually exclusive.
- **QA-05 (Citation Requirements):** All textual bases are referenced by address and marked verify-required; named scholars or quotations must be flagged verify-required rather than asserted as confirmed attributions.
