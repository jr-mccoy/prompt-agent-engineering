---
title: "Bias-Specific Audit — Test a Conclusion Against a Named Cognitive Bias"
category: reasoning-craft/epistemic
description: "Audit a conclusion or analysis against a single named cognitive bias (confirmation, availability, anchoring, survivorship, hindsight, base-rate neglect, narrative fallacy, sunk cost, attribution error). Each bias has its own diagnostic, evidence pattern to look for, and remediation. Targeted audit beats generic 'check for bias' instruction."
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
  - bias-detection
  - cognitive-bias
  - critical-thinking
  - audit
updated: "2026-05-10"
reasoning:
  styles: [adversarial, diagnostic, structural]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: per_bias_diagnostic
  user_role: [analyst, researcher, executive, founder, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
---

# Bias-Specific Audit

**Objective:** Audit a conclusion, forecast, or analysis against one or more named cognitive biases. Each bias has its own diagnostic questions, the pattern of evidence that suggests it's at work, and a targeted remediation. Targeted bias audits substantially outperform generic "check for bias" instructions because each bias's signature is different.

**When to use:**
- A conclusion is about to be acted on and you want a final adversarial check.
- The user suspects a specific failure mode (e.g., "am I anchored on the first option?", "is this just hindsight?") and wants the diagnostic for that bias.
- After a major analysis, before publication or presentation.
- A team disagreement might be diagnosable as a specific bias on one side.

**When NOT to use:**
- The conclusion is well-vetted by external evidence and the audit would be theater.
- The user wants to use bias accusations to dismiss a rival's view (use `epistemic_disagreement_diagnosis.md` instead — the right move is to model the disagreement, not weaponize bias language).

**Audience:** Analysts, researchers, executives, founders, anyone shipping a load-bearing conclusion.

---

## Inputs / Context

1. **The conclusion or analysis under audit.** State it concisely. Include the key reasoning.
2. **The bias(es) to test against.** One or more from the catalog below. If unsure which apply, run the screening step first.
3. **How the conclusion was formed.** Self-generated, derived from data, adopted from an expert, etc.
4. **Stakes.** Higher stakes warrant more bias-audits.

---

## Bias catalog (with diagnostics)

### Confirmation bias
**Signature:** evidence cited primarily supports the conclusion; little or no engagement with disconfirming evidence.
**Diagnostic questions:**
- What evidence did I look for? Was the search symmetric (sought confirming AND disconfirming)?
- Can I name the strongest evidence *against* my conclusion? Do I weight it as seriously as the confirming evidence?
- If my conclusion were false, what evidence would I expect to see — and do I see any of it?
**Remediation:** Run `epistemic_evidence_against_yourself.md`. Weight disconfirming evidence at the same standard as confirming.

### Availability heuristic
**Signature:** estimate or probability anchored on recent, vivid, or memorable cases rather than base rates.
**Diagnostic questions:**
- What examples come to mind? Are they recent / vivid / personally salient?
- Is there a base rate I'm not using? What does it say?
- Would my estimate change if I had a longer time window of comparable cases?
**Remediation:** Run `reasoning_reference_class_forecast.md`. Establish base rate before incorporating salient cases.

### Anchoring
**Signature:** estimate clusters near the first number presented, even when the first number was arbitrary or known to be biased.
**Diagnostic questions:**
- What was the first number I saw? Is my estimate within 30% of it?
- If I started from a very different anchor (e.g., 10x lower or higher), would I land in a similar place?
- Is the first number I'm anchored on actually informative, or is it noise?
**Remediation:** Generate the estimate from scratch using independent decomposition (Fermi); compare to anchored estimate.

### Survivorship bias
**Signature:** conclusions drawn from successful or surviving cases; failed or absent cases not in the dataset.
**Diagnostic questions:**
- What cases am I not seeing? Where do failed cases go?
- What's the base rate of survival in this reference class? If only 10% survive, the survivors' patterns may not be replicable.
- Are the survivors' attributes the *cause* of survival, or are they correlated with confounders?
**Remediation:** Construct the population of attempts (not survivors). Compare attempts → outcomes, not survivor attributes.

### Hindsight bias
**Signature:** treating an outcome as having been more predictable than it actually was; judging past decisions by outcome rather than ex-ante reasoning.
**Diagnostic questions:**
- If I had been making this decision at the time with only the information then available, what would I have estimated?
- Am I evaluating the decision or the outcome?
- Would I judge a similar decision differently if it had a different outcome despite identical information?
**Remediation:** Reconstruct the ex-ante information set. Evaluate decision quality separately from outcome quality (a good decision can have a bad outcome and vice versa).

### Base-rate neglect
**Signature:** specific case information dominates over base rates; conclusion ignores how often the diagnosed pattern actually occurs.
**Diagnostic questions:**
- What is the base rate of the phenomenon I'm diagnosing?
- How specific are the case features compared to the base rate? (Highly specific features can move the estimate, but most "specific" features are common.)
- If the base rate is 1% and I'm at 80%, what's the diagnostic ratio doing the work — and is it justified?
**Remediation:** Establish the base rate explicitly. Use a Bayesian update (`reasoning_bayesian_belief_update.md`).

### Narrative fallacy
**Signature:** events explained as a coherent story; randomness, luck, and uncorrelated factors disappear into the narrative.
**Diagnostic questions:**
- Could a similarly satisfying narrative have been built around the *opposite* outcome?
- Where is luck / randomness / external factor in this story? If absent, suspicious.
- Did the actors actually intend the outcomes I'm attributing to their strategy, or am I reading intention backward from outcome?
**Remediation:** List the role of luck / external factors / counterfactual paths. Run `reasoning_counterfactual_analysis.md`.

### Sunk cost fallacy
**Signature:** decision driven by what's already been invested rather than expected forward value.
**Diagnostic questions:**
- If I had not already invested anything, would I make this same decision today?
- Is the value of continuing forward-looking, or is it the cost of admitting the prior investment was wasted?
- What would a fresh analyst with no prior commitment recommend?
**Remediation:** Reframe as "given today's situation and zero prior commitment, what's the best action?" Sunk costs are sunk by definition.

### Fundamental attribution error
**Signature:** overattributing *others'* behavior to disposition or character while underweighting situational causes.
**Diagnostic questions:**
- Am I attributing this person's behavior to who they are when situational factors might explain it?
- Would I explain my own similar behavior the same way? If not, why is the asymmetry justified?
- What about the situation I might not be seeing?
**Remediation:** Generate 2–3 situational explanations for the behavior before settling on a character explanation.

### Optimism / planning fallacy
**Signature:** estimates of cost / time / probability of success systematically more favorable than the reference class predicts.
**Diagnostic questions:**
- What did comparable past projects actually cost / take / achieve?
- Is my estimate inside the historical range, or am I claiming this case is exceptional? What evidence supports the exception?
**Remediation:** Run `reasoning_reference_class_forecast.md`.

---

## Constraints

### Must
- Name the specific bias being audited. Generic "bias check" is not allowed.
- Run the bias's diagnostic questions verbatim.
- Look for the bias's *signature* in the actual conclusion, not abstract speculation.
- Produce one of three verdicts per bias: **clear evidence of bias**, **possible / mixed signals**, **no evidence found**.
- For "clear evidence" or "possible", run the targeted remediation.
- Distinguish bias *presence* from bias *significance*. A small confirmation-bias signature in a low-stakes conclusion may not be worth fixing.

### Must Not
- Conclude "no bias" without running the diagnostic. The audit requires showing the work.
- Use bias language to dismiss conclusions you disagree with for other reasons.
- Stack so many biases that the audit becomes paralysis. 1–3 targeted audits beat 10 cursory ones.
- Confuse "the conclusion has features that *could* indicate bias" with "the conclusion *is* biased." Many features have non-bias explanations.

---

## Instructions

### Step 1 — State the conclusion under audit
One paragraph: the conclusion, the reasoning, the action depending on it.

### Step 2 — Pick the bias(es)
Either named by the user, or selected via screening:
- Decision driven by a forecast → optimism, anchoring, base-rate neglect
- Conclusion drawn from a sample → survivorship, availability
- Evaluation of a past decision → hindsight, narrative
- Continuing investment in something existing → sunk cost
- Inference about another person → attribution error
- Strong intuition without disconfirming search → confirmation

### Step 3 — Run the diagnostic
For each bias, walk through its diagnostic questions. Record answers verbatim.

### Step 4 — Verdict per bias
- **Clear evidence:** the signature is present; remediation is needed.
- **Possible / mixed:** signature partially present, but alternative explanations exist; flag and proceed cautiously.
- **No evidence:** diagnostic questions returned clean answers.

### Step 5 — Remediation
For "clear" or "possible" verdicts, apply the bias-specific remediation.

### Step 6 — Significance
Even if bias is present, ask: how much would it move the conclusion? In low-stakes contexts, small biases may be noted and ignored. In high-stakes contexts, even small biases warrant correction.

### Step 7 — Updated conclusion
Restate the conclusion after remediation. Note what changed and what didn't.

---

## False-Positive Prevention

1. **Bias-spotting theater.** "Confirmation bias possible" without running the diagnostic is theater. Always show the diagnostic answers.
2. **Bias-as-rhetoric.** Using bias language to win arguments rather than diagnose reasoning. Bias audit is an internal tool; don't deploy it externally as a debate move.
3. **Diagnosis without remediation.** Identifying a bias and then ignoring it. Each "clear" verdict requires the targeted remediation.
4. **Too many biases at once.** Auditing 10 biases produces noise. 1–3 targeted audits beat broad screening.
5. **Confusing structural critique with bias.** Sometimes a conclusion has weaknesses that aren't bias-driven (missing data, model limitations). Bias is a specific claim; don't expand it to mean "anything wrong."
6. **Self-exempt audit.** Auditing only the conclusions you're skeptical of. Apply the audit symmetrically to conclusions you favor.
7. **Significance inflation.** Treating every bias finding as fatal. Some biases are present-but-small; the audit should rate magnitude.

---

## Output Format

```
# Bias audit — [conclusion]

## Conclusion under audit
[One paragraph: conclusion, reasoning, action depending on it]

## Bias 1: [name]

### Signature definition
[What this bias looks like in conclusions]

### Diagnostic answers
- Q1: [the question] → [answer]
- Q2: [the question] → [answer]
- Q3: [the question] → [answer]

### Verdict
[Clear evidence / Possible / No evidence] — because [one sentence]

### Significance
[Low / moderate / high — how much it would move the conclusion]

### Remediation (if applicable)
[Targeted action; reference companion prompt if useful]

## Bias 2: [name]
[Repeat structure]

…

## Updated conclusion (post-remediation)
[Restated conclusion]
- What changed: [delta]
- What did not change: [delta]
- Net effect on action: [continue as planned / modify / pause / abandon]
```

---

## Verification

- [ ] Each bias being audited is named explicitly.
- [ ] Diagnostic questions for each bias are answered verbatim.
- [ ] Each bias produces one of three verdicts (clear / possible / no evidence).
- [ ] "Clear" or "possible" verdicts trigger the targeted remediation.
- [ ] Significance is rated, not just presence.
- [ ] Updated conclusion explicitly notes what changed and didn't.
- [ ] No bias language used to dismiss without running the diagnostic.
- [ ] No more than 3 biases audited per pass (or justification for more).
- [ ] Self-exempt check: audit applied to favored conclusion, not just disfavored ones.
