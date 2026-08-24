---
title: "Claim / Evidence / Warrant Audit — Surface the Unstated Bridges in an Argument"
category: reasoning-craft/reasoning-moves
description: "Audit a passage by extracting every claim, separating the evidence offered, and surfacing the (usually unstated) warrant that bridges evidence to claim. Especially useful for op-eds, position papers, expert testimony, and persuasive writing where the warrants are doing most of the work but are unstated."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - argument-analysis
  - warrant
  - audit
  - critical-thinking
  - rhetoric
updated: "2026-05-10"
reasoning:
  styles: [structural, analytic, dialectical]
  stakes: variable
  horizon: hours
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: claim_evidence_warrant_table
  user_role: [analyst, writer, lawyer, journalist, researcher, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md
  - domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md
  - domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md
---

# Claim / Evidence / Warrant Audit

**Objective:** Audit a passage by extracting every load-bearing claim, separating the evidence offered for it, and surfacing the **warrant** — the (usually unstated) general principle that bridges evidence to claim. Companion to `reasoning_argument_map_toulmin.md` but tighter and more focused: this prompt is for fast warrant-surfacing on real-world persuasive writing, where 80% of the disagreement-power lives in unstated warrants. Use this prompt when the suspect link is the evidence→claim bridge in persuasive prose (the warrants); when the suspect inputs are the starting claims themselves (factual / value / methodological premises), including arguments that cite no evidence at all, use `reasoning_premise_audit.md`.

**When to use:**
- Auditing op-eds, position papers, expert testimony, policy memos, marketing copy.
- Reviewing your own writing before publication to find your unstated warrants.
- Reading scientific abstracts where the data → conclusion bridge is asserted not shown.
- Preparing to challenge an argument: attacking the warrant is often more effective than attacking the evidence.
- Teaching critical reading.

**When NOT to use:**
- Mathematical / formal proofs (warrants are explicit).
- Pure description (no claim being argued).
- Audit-grade need where full Toulmin structure is warranted (use the Toulmin prompt).

**Audience:** Analysts, writers, lawyers, journalists, researchers, anyone reading or writing persuasive prose.

---

## Inputs / Context

1. **The passage.** Op-ed, paragraph, paper section, speech transcript.
2. **What you're trying to do.** Audit your own / understand someone else's / prepare to rebut.
3. **The audience the passage was written for** (sometimes warrants are obvious to one audience and invisible to another).

---

## Constraints

### Must
- Extract **every load-bearing claim** in the passage. Skip throat-clearing and transitions.
- For each claim: list the **evidence** the author offers, then articulate the **warrant** (general principle bridging evidence to claim) — even if the author left it unstated.
- Label warrants as **stated** or **implicit**.
- Score each warrant: **strong** (almost certainly accepted), **contested** (defensible but not universally), **weak** (would not survive scrutiny).
- Identify the **load-bearing warrants** — the ones whose failure would collapse the argument.
- For each contested or weak warrant, write what the author would have to defend if challenged.

### Must Not
- Confuse claim with evidence.
- Confuse evidence with warrant. (Evidence is *this* fact; warrant is the *general principle* that lets the fact support the claim.)
- Treat absence of stated warrant as absence of warrant.
- Score warrant strength based on the conclusion you wish were true.
- Skip implicit warrants because they're not in the text.

---

## Instructions

### Step 1 — Extract load-bearing claims
List every claim the passage actually argues for. Skip context, examples, and rhetorical flourish.

### Step 2 — Per claim, identify evidence and warrant
For each claim:
- **Evidence offered:** facts, data, citations, observations, quotations
- **Warrant (stated):** if the author articulated the bridging principle
- **Warrant (implicit):** if not, articulate what would have to be true for the evidence to support the claim

### Step 3 — Score warrants
| Warrant | Stated/implicit | Strength |
|---------|-----------------|----------|
| [warrant] | implicit | contested |
| ... | ... | ... |

- **Strong:** broadly accepted in the relevant audience.
- **Contested:** defensible but reasonable people would disagree.
- **Weak:** would not survive scrutiny.

### Step 4 — Identify load-bearing warrants
Which claims rest on contested or weak warrants? These are where the argument actually rests; they're also where it's most vulnerable.

### Step 5 — Steelman the contested warrants
For each contested warrant: what's the strongest defense? This separates "warrant the author should be able to defend" from "warrant that's actually broken."

### Step 6 — Implications
- For audit of own writing: which warrants need to be stated and defended explicitly?
- For challenging the argument: which warrant is the most productive attack point?
- For deciding whether to accept the argument: do the load-bearing warrants survive scrutiny?

---

## False-Positive Prevention

1. **Evidence-warrant collapse.** "Studies show X, therefore Y." The warrant is "if studies show X, that implies Y." That warrant deserves examination.
2. **Implicit-warrant denial.** "The author didn't say it, so they don't believe it." False — they assumed it.
3. **Audience-blind warrants.** A warrant that's strong in one audience can be weak in another. Note the audience.
4. **Conclusion-tinted warrant scoring.** Don't score warrants by whether they yield conclusions you like.
5. **Throat-clearing claims.** Don't treat every sentence as a load-bearing claim.
6. **Over-decomposition.** Stop at load-bearing claims; don't atomize endlessly.

---

## Output Format

```
# Claim / evidence / warrant audit — [passage source]

## Audience the passage was written for
- [...]

## Load-bearing claims, evidence, warrants

### Claim 1: [verbatim or paraphrased]
- Evidence offered: [...]
- Warrant (stated/implicit): [stated / implicit]
- Warrant content: [the bridging principle]
- Warrant strength: [strong / contested / weak]
- Steelman of contested warrant: [...]

### Claim 2: [...]
[Same structure]

[etc.]

## Load-bearing warrants
- [warrant] supports claim [N], strength [contested]
- [warrant] supports claim [N], strength [weak]
- ...

## Implications
- For audit of own writing: which warrants to state explicitly: [...]
- For challenging the argument: best attack point: [...]
- For accepting the argument: [argument survives / fails / is contested at warrant level]
```

---

## Verification

- [ ] All load-bearing claims extracted.
- [ ] Per claim: evidence and warrant separated.
- [ ] Implicit warrants articulated, not skipped.
- [ ] Warrant strength scored.
- [ ] Load-bearing warrants identified.
- [ ] Implications section actionable.
- [ ] No claim-evidence-warrant collapses.
