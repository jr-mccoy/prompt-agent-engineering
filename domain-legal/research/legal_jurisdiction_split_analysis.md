---
title: "Jurisdiction Split Analysis (Circuit / State)"
category: legal/research
description: "Map a circuit split or state split on a doctrinal question, identify the camps and their reasoning, locate the user's jurisdiction, and assess trend and Supreme Court / supreme-court-grant likelihood."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - research
  - circuit-split
  - state-split
  - cert-petition
  - jurisdiction-analysis
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_precedent_comparison_table.md
  - domain-legal/research/legal_case_brief_generator.md
---

**Purpose:** Synthesize a doctrinal split across circuits or states on a discrete question, identify the user's controlling rule, and assess strategic implications including cert / discretionary review prospects.

**When to use:** Cert-stage briefing, doctrinal-trend memos, forum-shopping analysis, multi-jurisdiction compliance design, advisory work for clients operating across jurisdictions, training/evaluation tasks.

---

## Your Input

- **Doctrinal question:** [Concretely framed]
- **User's controlling jurisdiction:** [Required]
- **Cases per jurisdiction:** [Citations + relevant text grouped by circuit or state]
- **Pending or recently granted certiorari / discretionary review:** [If known — supply text]
- **Statutory or regulatory provision involved, if any:** [Verbatim]
- **Use case:** [Compliance design / cert-stage brief / advisory memo / forum decision / training task]

---

## Constraints

**Must:**
- Group authorities by their position on the question into **camps** (typically 2–4). Name each camp by the rule it adopts, not by the lead case.
- For each camp: list members, articulate the rule in one sentence, identify the strongest reasoning move, identify outliers, and note the most recent decision.
- Identify the **user's controlling rule** explicitly.
- Note any **intra-jurisdiction tension** (e.g., panel decisions in tension within the same circuit).
- Assess **trend**: is one camp gaining or losing members? Use only what the supplied cases support.
- Assess **review prospects**: does the split satisfy the user's discretionary-review standard (squareness, depth, importance, vehicle)?

**Must Not:**
- Invent decisions to round out a camp.
- Treat a single panel opinion as a circuit's settled rule unless it has been followed.
- Conflate a true split (different rules) with a perceived split (different applications of the same rule).
- Apply federal cert-grant criteria to a state-court discretionary-review question.
- Generate "the trend is moving toward X" without naming the cases that move it.

---

## Instructions

1. **Frame the doctrinal question** in one sentence so each camp's rule answers it.
2. **Cluster authorities into camps** by the rule each adopts. If a case applies a rule but does not articulate it cleanly, place it in the camp whose articulation it most closely tracks, and flag the imprecision.
3. **For each camp**, populate:
   - Rule, in one sentence.
   - Members (jurisdictions and cases).
   - Reasoning core: the doctrinal or interpretive move that justifies the rule.
   - Outliers within the camp: panels that go further or hedge.
   - Most recent decision in the camp.
4. **Identify the user's controlling rule.** Quote the operative language. Note any intra-jurisdiction tension.
5. **Trend assessment.** Which camps have added members recently. Which have lost. Which have a leading judge or scholar pulling toward a new position (only if the supplied text shows it).
6. **Discretionary-review prospects** (only if relevant to use case):
   - Squareness: do the camps actually disagree on the same legal question, or do they differ on application?
   - Depth: how many jurisdictions on each side; how recent.
   - Importance: practical impact, federal/state interest implications.
   - Vehicle: would the user's facts present the issue cleanly?
7. **Strategic implications** for the user's use case (compliance design, brief, forum, advisory).

---

## Output Format

```markdown
## Doctrinal Question

{One sentence.}

## Camps

### Camp A: {Rule label}
- **Rule:** {one-sentence articulation}
- **Members:**
  - {Circuit / state} — {lead case}, {cite}; followed by {...}
  - {...}
- **Reasoning core:** {the move that justifies the rule}
- **Outliers / hedges within camp:** {...}
- **Most recent decision:** {case, date}

### Camp B: {Rule label}
{...}

### Camp C (if any): {Rule label}
{...}

## User's Controlling Rule

- **Jurisdiction:** {...}
- **Camp:** {...}
- **Operative language:** "{quoted}"
- **Intra-jurisdiction tension, if any:** {...}

## Trend Assessment

- {Camp gaining members: which, how recently}
- {Camp losing or shrinking}
- {Influential individual votes / writings, only if in supplied text}

## Discretionary-Review Prospects (if applicable)

| Factor | Assessment |
|--------|------------|
| Squareness | ... |
| Depth | ... |
| Importance | ... |
| Vehicle | ... |

**Composite:** {Strong / Moderate / Weak} candidate for {cert / state-supreme review} because {reason}.

## Strategic Implications

- For compliance design: {...}
- For brief writing: {...}
- For forum selection: {...}
- For advisory: {...}

## Open Items
- Decisions not yet reviewed: {...}
- Pending appeals worth tracking: {...}
- Pinpoints needed: {... `[NEED PIN: ...]` ...}
```

---

## Verification

- [ ] Camps named by their rule, not by the lead case.
- [ ] Each camp's rule expressed in one sentence.
- [ ] User's controlling rule identified with operative quoted language.
- [ ] Trend statements grounded in specific cases, not asserted.
- [ ] Squareness, depth, importance, vehicle each addressed if review-prospect analysis is requested.
- [ ] Intra-jurisdiction tension flagged when present.
- [ ] No invented decisions; missing pinpoints flagged with placeholders.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Counting the same circuit twice via panel decisions | One vote per circuit unless a later panel openly conflicts; even then, identify it as intra-circuit tension |
| Treating dicta in opposing camps as the rule | Pull the rule from holdings; flag dicta separately |
| Calling a divergence a "split" when both camps apply the same rule differently | A true split disagrees on the rule; an application split is rarely cert-worthy on its own |
| Using federal cert criteria for a state-supreme discretionary-review analysis | Use the supplied state's grant criteria |
| Asserting "trend" without the cases | Trend statements must name the case(s) and date(s) that move it |
| Listing a lone district court case in a camp | District court decisions don't bind even within their own district; mark them as such |
| Ignoring an en banc reversal | An en banc opinion supersedes the panel decision in that circuit; mark superseded cases accordingly |
