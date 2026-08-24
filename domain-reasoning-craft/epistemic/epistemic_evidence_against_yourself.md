---
title: "Evidence Against Yourself — Generate the Strongest Disconfirming Case for Your Own Position"
category: reasoning-craft/epistemic
description: "For a position the user holds, generate the strongest empirical, theoretical, and structural evidence *against* it. Distinct from steelmanning the opponent's view: this prompt focuses on disconfirming the user's own claim, including evidence the user has not yet encountered. Used as a final adversarial check before commitment."
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
  - disconfirmation
  - red-team
  - adversarial
  - belief-update
updated: "2026-05-10"
reasoning:
  styles: [adversarial, falsificationist, dialectical]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: structured_disconfirmation_table
  user_role: [analyst, founder, executive, researcher, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
  - domain-reasoning-craft/epistemic/epistemic_bias_specific_audit.md
  - domain-reasoning-craft/epistemic/epistemic_red_team_briefing.md
  - domain-reasoning-craft/epistemic/epistemic_motivated_reasoning_check.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

# Evidence Against Yourself

**Objective:** Generate the strongest disconfirming case for the user's own position. Search for empirical evidence that contradicts the position, theoretical / mechanistic reasons it would be wrong, and structural / incentive-based reasons it persists despite being wrong. The deliverable is the strongest version of "you're mistaken" — which the user then weighs against the original position to make a final decision.

This is distinct from `reasoning_steelman_construction.md`: steelmanning builds the *opposing position* in its strongest form. This prompt focuses on the *evidence against the user's own claim*, including evidence the user has not yet encountered and reasons the user has not yet considered.

**When to use:**
- Final adversarial check before a high-stakes commitment (investment, hire, public statement, strategic bet).
- The user has been working on a position and wants to see what they've missed.
- Pre-publication review when the goal is surfacing missed disconfirming evidence, not rehearsing a critic's attack.
- Periodic self-audit on a long-running thesis.
- After a `reasoning_bayesian_belief_update` to surface what evidence the user might be filtering out.

**When NOT to use:**
- The user has already done extensive disconfirming work and the next move is decision, not more deliberation.
- The position is well-supported and the only "evidence against" is fringe / non-credible. (Surface and stop; theatrical disconfirmation is worse than none.)
- Time pressure is severe.
- You need to rehearse a specific adversary's attack on a finished artifact — use `epistemic_red_team_briefing.md`.
- You need to audit whether you'd accept your existing evidence if it cut the other way — use `epistemic_motivated_reasoning_check.md`.

**Audience:** Anyone shipping a load-bearing position who wants to confront the strongest version of "you're wrong."

---

## Inputs / Context

1. **The position.** One sentence in the user's words.
2. **The reasoning supporting it.** What evidence and arguments the user is currently weighing.
3. **What the user has already considered as disconfirming.** So we don't repeat their existing list.
4. **Where the user is most likely to be missing evidence.** (Domain blind spot, recency bias, source bubble, professional consensus echo chamber, etc.) Optional but useful.
5. **Stakes.** Higher stakes warrant deeper disconfirmation work.
6. **Current confidence in the position (optional).** Stated as a probability or a qualitative lean; this is the prior compared against in the Update step.

---

## Constraints

### Must
- Surface evidence, mechanisms, and structural reasons that *contradict* the position — not the opposing position's strongest case (that's steelmanning).
- Cover three tracks: **empirical** (data, observations, track record), **theoretical / mechanistic** (reasons the position's mechanism wouldn't work as claimed), **structural** (reasons the position persists *despite* being wrong: incentives, social proof, narrative momentum, professional norms).
- Push the user beyond their existing list of considered-disconfirming evidence. The value is in what they haven't yet engaged.
- Cite or describe evidence concretely, not gesturally. "Some studies show X" is not enough; give the strongest version of X.
- For each piece of disconfirming evidence, force a response: rebut, accept, weight against confirming evidence, or update.
- End with a concrete update statement: did the disconfirming work move the position, and if not, why not.

### Must Not
- Smuggle in fake balance ("on the other hand…") that the user can dismiss. The disconfirming case must be made as strongly as the user's case.
- Generate weak counterarguments. Weak counterarguments make the user feel safer than they should.
- Allow the user to dismiss disconfirming evidence as "considered already" without engaging it freshly.
- Replace this with a list of generic "things to consider." Each item must be *specifically* about the user's position.
- Treat absence of disconfirming evidence as confirmation. Sometimes the evidence simply doesn't exist; that's a finding too.

---

## Instructions

### Step 1 — Restate the position
Write the position in one sentence. List the user's primary supporting evidence in 3–5 bullets. Record the user's current confidence (a probability if stated, otherwise a qualitative lean) — this is the original-confidence figure used in the Update.

### Step 2 — Capture what the user has already considered
Briefly: what disconfirming evidence has the user already weighed and rejected? This is sealed off; we won't waste cycles re-running it.

### Step 3 — Empirical disconfirmation
Search for evidence that contradicts the position:
- Studies, datasets, track records, historical cases that point the other direction.
- Cases where the position was tried and failed.
- Reference classes where the position's expected outcome did not occur.

For each: cite the strongest version. Rate quality (high / medium / low).

### Step 4 — Theoretical / mechanistic disconfirmation
Reasons the mechanism wouldn't work as claimed:
- Hidden assumptions in the position that may not hold.
- Steps in the causal chain that are weaker than they appear.
- Conditions under which the mechanism reverses.
- Failure modes inherent to the proposed mechanism.

### Step 5 — Structural / incentive-based disconfirmation
Reasons the position might be widely held *despite* being wrong:
- Whose interests are served by promoting this position?
- Is there professional / institutional pressure to hold this position?
- Are the loudest proponents of the position those least exposed to its being wrong?
- Is the position narratively satisfying in a way that exceeds its evidential support?
- What would have to be true about the *information environment* for the position to be wrong but widely believed?

### Step 6 — Engagement
For each piece of disconfirming evidence (across all three tracks), the user (or analyst) responds:
- **Rebut:** evidence is real but defeated by counter-evidence (cite it).
- **Accept and reweight:** evidence is real and partially undermines the position; the position is now weaker.
- **Accept and revise:** evidence is sufficient to revise the position substantially.
- **Defer:** evidence is real but cannot be evaluated now; flag for future research.

### Step 7 — Update statement
Did the cumulative disconfirming work move the position?
- **Yes (revised):** state the revised position.
- **Yes (weakened):** state the original position with reduced confidence.
- **No (engaged and held):** state why the disconfirming evidence, while real, doesn't change the position.
- **No (engaged and the position improved):** the disconfirming work surfaced reasons the position is *more* defensible than it appeared. Rare, but possible.

### Step 8 — Residual exposure
After the audit, what's the strongest piece of disconfirming evidence the user is still betting against? This is the position's tail risk; it should be named explicitly.

---

## False-Positive Prevention

1. **Strawman disconfirmation.** Generating weak counterarguments the user can easily dismiss. The disconfirming case must be made at the same standard as the user's case.
2. **Generic disconfirmation.** Generic "biases to watch for" lists. Each piece of disconfirming evidence must be *specifically* about the user's position.
3. **Absorption.** "I considered that already." Re-engage freshly. The disconfirming evidence may have been considered, but the engagement may have been shallow.
4. **Citation theater.** "Some research suggests" is not citation. Either describe the actual evidence or admit the disconfirming case is mechanistic / structural rather than empirical.
5. **Structural-track skip.** Most reasoners do empirical and theoretical tracks but skip structural ("why might this position be widely held but wrong?"). Don't skip — this is where systemic blind spots live.
6. **Premature update.** Updating the position based on weakly-evidenced disconfirmation is as bad as failing to update. Each update should be evidentially proportionate.
7. **Self-flagellation theater.** Performatively accepting all disconfirming evidence to look open-minded. The audit is for honest re-weighting, not display.
8. **Asymmetric standards.** Holding disconfirming evidence to a higher standard than the original supporting evidence. Apply the same evidence rules in both directions.

---

## Output Format

```
# Evidence against — [position]

## Position
> [One sentence]

## Original supporting evidence
- [Bullet]
- [Bullet]
- [Bullet]

## Already-considered disconfirmation (sealed off)
- [What the user has already weighed and rejected]

## Empirical disconfirmation
| # | Evidence                              | Source / quality | Direction        |
|---|---------------------------------------|------------------|------------------|
| 1 | [concrete description of strongest]   | high             | contradicts X    |
| 2 | …                                     |                  |                  |

## Theoretical / mechanistic disconfirmation
| # | Reason mechanism may fail             | Conditions       |
|---|---------------------------------------|------------------|
| 1 | [hidden assumption / weak step]       | [when it bites]  |
| … |                                       |                  |

## Structural / incentive-based disconfirmation
| # | Reason position may persist despite being wrong       |
|---|--------------------------------------------------------|
| 1 | [whose interests / what pressure]                     |
| 2 | [narrative / professional norm]                        |
| … |                                                        |

## Engagement
| # | Disconfirming item        | Response (rebut / accept-reweight / accept-revise / defer) | Reason |
|---|---------------------------|-----------------------------------------------------------|--------|
| E1 | [empirical #1]            | accept-reweight                                           | …      |
| T2 | [theoretical #2]          | rebut                                                      | …      |
| …  |                           |                                                            |        |

## Update
- Original position confidence: [%]
- Updated position confidence: [%]
- Direction of update: [revised / weakened / unchanged / strengthened]
- One-line update statement: [...]

## Residual exposure
- Strongest piece of disconfirming evidence still being bet against: [item]
- This is the position's tail risk if it materializes.
```

---

## Verification

- [ ] All three tracks (empirical, theoretical, structural) are populated.
- [ ] Each piece of disconfirming evidence is specific, not generic.
- [ ] Citations or concrete descriptions are present where claimed (no "some research suggests").
- [ ] User engaged each item with one of four responses (rebut / accept-reweight / accept-revise / defer).
- [ ] Update statement is honest, not performative.
- [ ] Residual exposure is named explicitly.
- [ ] Disconfirming evidence held to same standard as supporting evidence.
- [ ] Already-considered list was sealed off and not re-run.
- [ ] No strawman counterarguments generated.
