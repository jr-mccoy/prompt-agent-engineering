---
title: "Uncertainty Acknowledgment Audit — Match Stated Certainty to Actual Evidence"
category: reasoning-craft/epistemic
description: "Audit a draft (memo, paper, recommendation) for false certainty, flagging every claim where the certainty stated exceeds the evidence available — bare assertions that should be probabilistic, quantitative claims missing intervals, inferential leaps missing limitations, and attribution inflation ('research suggests' when it's one paper). The goal is calibrated certainty, not hedging everywhere. Counters both overconfidence and its overcorrection into mush where every sentence is buried in qualifiers."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - calibration
  - uncertainty
  - false-certainty
  - audit
updated: "2026-05-21"
reasoning:
  styles: [analytical, evaluative, diagnostic]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: annotated_audit_with_edits
  user_role: [analyst, researcher, executive, writer, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_claim_inference_separator.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
  - domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md
---

# Uncertainty Acknowledgment Audit

**Objective:** Audit a document for false certainty. Walk through and flag every claim where the certainty stated exceeds the evidence available, then suggest a calibrated edit. Target the common patterns: flat assertions ("X is") that should be probabilistic ("X is likely, given Y"), quantitative claims missing confidence intervals or ranges, inferential leaps missing their limitations, and attribution inflation (writing "research suggests" or "studies show" when it's actually one unreplicated paper). The aim is *calibrated* certainty — certainty matched to evidence — not hedging everywhere, which is its own failure mode.

**When to use:**
- Before publishing a memo, paper, recommendation, or forecast where overstated certainty would be costly or damage credibility.
- Reviewing your own draft, where you're the worst-placed person to notice your own overconfidence.
- Auditing a document that *feels* too confident but you can't pinpoint where.
- Editing a document that's overcorrected into qualifier-soup and needs certainty *restored* where evidence supports it.

**When NOT to use:**
- The document is exploratory or explicitly speculative and labeled as such — auditing a brainstorm for certainty is a category error.
- You need to separate claims from inferences first — use `epistemic_claim_inference_separator.md`, then audit certainty on what remains.
- The task is to assess the underlying evidence quality, not the language — use `epistemic_evidence_quality_score.md`.

**Audience:** Analysts, researchers, executives, and writers shipping a document whose credibility depends on calibrated claims.

---

## Inputs / Context

1. **The draft.** Provided verbatim so claims can be quoted and edited.
2. **The evidence behind it.** What actually supports each major claim (so the audit can compare stated certainty to real support).
3. **The audience and stakes.** Who reads it and what happens if a claim is wrong — higher stakes warrant tighter calibration.
4. **House style on hedging (optional).** Some venues want crisp assertions; the audit calibrates within that style rather than fighting it.

---

## Certainty mismatch patterns

- **Bare assertion** — a contestable claim stated as flat fact ("the rollout failed because of pricing"). Should carry the probability and the basis.
- **Missing interval** — a number with no range or error ("conversion will rise 30%"). Should give a range or confidence.
- **Missing limitation** — an inferential leap with no scope condition ("this generalizes to all markets"). Should state where it holds and doesn't.
- **Attribution inflation** — vague attribution inflating an evidence base ("research suggests," "it's well known," "studies show") when it's one source or none. Should name the actual support.
- **Certainty laundering** — a tentative source claim restated more confidently than the source stated it.
- **Overcorrection / qualifier-soup** — so many hedges that a well-supported claim reads as weak. Should *raise* certainty to match the evidence.

---

## Constraints

### Must
- Quote each flagged claim and name the **specific mismatch pattern**.
- Compare stated certainty to **actual evidence** — flag a claim only where the language and the support diverge.
- Provide a **calibrated edit** for each flag: the rewrite that matches certainty to evidence (which sometimes means *increasing* certainty).
- Catch **both directions**: overstatement (too certain) and overcorrection (too hedged given strong evidence).
- Prioritize **load-bearing claims** — the ones the document's conclusion or recommendation depends on — over incidental phrasing.
- Preserve the document's voice; calibrated does not mean timid or jargon-laden.

### Must Not
- Add hedges everywhere as a reflex. Blanket hedging is a failure mode equal to overconfidence; it destroys signal.
- Flag stylistic confidence that the evidence actually supports. A well-supported claim stated plainly is correct, not overconfident.
- Rewrite into qualifier-soup ("it may possibly be the case that perhaps…"). Calibrated edits are crisp.
- Audit certainty without reference to the evidence — that's just generic hedging advice.
- Treat all claims equally; an overstated aside matters far less than an overstated recommendation.

---

## Instructions

### Step 1 — Identify the load-bearing claims
List the claims the document's conclusion or recommendation rests on. These get the closest audit.

### Step 2 — Compare stated certainty to evidence
For each major claim, ask: how strong is the actual support, and how strong does the language make it sound? Flag divergences in either direction.

### Step 3 — Classify the mismatch
For each flag, name the pattern: bare assertion, missing interval, missing limitation, attribution inflation, certainty laundering, or overcorrection.

### Step 4 — Write the calibrated edit
Rewrite the claim to match certainty to evidence. For overstatement, add the probability/range/limitation/actual-source. For overcorrection, strip excess hedges and state the claim with the confidence the evidence warrants.

### Step 5 — Check attribution honesty
Find every "research suggests / studies show / it's known" and verify the support behind it. Replace inflated attributions with the real basis ("one 2024 study found…").

### Step 6 — Severity and priority
Rate each flag by how much it would mislead a reader or damage credibility. Foreground the load-bearing ones.

### Step 7 — Calibration summary
State the document's overall calibration: is it systematically overconfident, systematically over-hedged, or mixed? Note the pattern so the author can correct the habit, not just the instances. Hand forecasting-language calibration to `forecasting_calibration_self_audit.md` if relevant.

---

## False-Positive Prevention

1. **Reflexive hedging.** Adding "may," "might," "possibly" to every sentence. Blanket hedging is the overcorrection failure mode; it erases the signal calibration is meant to preserve.
2. **Penalizing supported confidence.** Flagging a plainly stated claim that the evidence fully backs. Confidence matched to strong evidence is correct.
3. **Qualifier-soup edits.** Rewriting into unreadable strings of caveats. Calibrated edits are crisp and specific, not mushy.
4. **Evidence-free audit.** Recommending hedges without checking the actual support. The audit compares language *to evidence*; without the evidence it's just stylistic nagging.
5. **One-direction blindness.** Only catching overconfidence and missing over-hedging. Both miscalibrate; audit both.
6. **Flat prioritization.** Spending equal effort on an overstated aside and an overstated recommendation. Weight by how load-bearing and how misleading.
7. **Attribution rubber-stamp.** Letting "research suggests" pass without checking what research. This phrase is the most common certainty-laundering device.
8. **Voice destruction.** Calibrating a document into timidity. Preserve the author's voice while fixing the certainty.

---

## Output Format

```
# Uncertainty acknowledgment audit — [document]

## Load-bearing claims
[The claims the conclusion/recommendation depends on]

## Flags
| # | Quoted claim | Mismatch pattern | Actual evidence | Calibrated edit | Severity |
|---|--------------|------------------|-----------------|-----------------|----------|
| 1 | "[verbatim]" | bare assertion   | [real support]  | "[rewrite]"     | high     |
| 2 | "[verbatim]" | overcorrection   | [strong support]| "[crisper rewrite, more certainty]" | med |
| 3 | "[verbatim]" | attribution inflation| [one paper]     | "[name the source]" | high |
| … |              |                  |                 |                 |          |

## Attribution check
| Phrase used        | Actual support | Replacement                |
|--------------------|----------------|----------------------------|
| "research suggests"| one 2024 study | "a 2024 study found…"      |

## Calibration summary
- Overall pattern: [systematically overconfident / over-hedged / mixed]
- Habit to correct: [the recurring move]
- Net: [document is shippable after edits / needs evidence before key claims can stand]
```

---

## Verification

- [ ] Load-bearing claims identified and audited most closely.
- [ ] Each flag quotes the claim and names a specific mismatch pattern.
- [ ] Stated certainty compared to actual evidence, not flagged in the abstract.
- [ ] Calibrated edit provided for each flag.
- [ ] Both overconfidence and over-hedging caught.
- [ ] Attribution phrases ("research suggests," etc.) verified against real support.
- [ ] Edits are crisp, not qualifier-soup; author's voice preserved.
- [ ] Overall calibration pattern summarized so the habit can be corrected.
