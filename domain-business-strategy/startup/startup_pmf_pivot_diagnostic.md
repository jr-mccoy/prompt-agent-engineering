---
title: "Product-Market Fit & Pivot Diagnostic"
category: startup/business-operations
description: "Diagnoses whether a product has real product-market fit using the Sean Ellis test and the effort test, detects false-PMF from ephemeral launch energy, and recommends adjust, pivot, or return-to-idea after stalled iteration."
techniques:
  - RT-02
  - RT-05
  - DS-02
  - QA-08
  - QA-12
difficulty: intermediate
tags:
  - pmf
  - pivot
  - sean-ellis-test
  - retention
  - startup
updated: "2026-06-19"
related_prompts:
  - domain-business-strategy/startup/startup_ai_native_lifecycle_navigator.md
  - domain-business-strategy/startup/startup_testable_hypothesis_sharpener.md
  - domain-productivity/validation/validation_am_i_being_nuts.md
---

# Product-Market Fit & Pivot Diagnostic

**Objective:** Determine whether a product has genuine product-market fit — using the Sean Ellis test and the effort test, and screening out false-PMF from ephemeral sources — and, if fit is absent after enough iteration, recommend whether to adjust, pivot, or return to the idea stage, with reasoning.

**When to Use:**
- You need an honest read on whether traction is real PMF or noise.
- You have run several iteration cycles without clear PMF movement and must decide adjust vs. pivot.
- Launch energy looked strong but you are unsure it predicts week-6 or week-12 behavior.

**When NOT to Use:**
- You are still pre-launch with no active users to survey — establish problem-solution fit first (use `startup_ai_native_lifecycle_navigator.md`).
- You only need to locate your overall lifecycle stage (use the navigator) rather than test PMF specifically.

**Source:** Framework adapted from Anthropic, *The Founder's Playbook: Building an AI-Native Startup* (2026) — a vendor report — figures attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the diagnosis degrades gracefully if some are missing:
- **Active-user signal** — who actively uses the product and how you would survey them.
- **Retention/revenue/referral data** — cohort retention, paid conversion, organic referral.
- **Launch-energy sources** — where early interest came from (friends, an investor's portfolio, a forum spike, organic demand).
- **Effort to retain** — how much founder intervention (outreach, incentives, follow-up) keeps users active.
- **Iteration history** — number of meaningful iteration cycles run and what changed each time.

## Constraints

**Must:**
- Run the Sean Ellis test: ask active users "How would you feel if you could no longer use this product?"; treat >40% answering "very disappointed" as a meaningful PMF indicator.
- Run the effort test: judge whether retention is founder-pushed (constant intervention) or product-pulled (the product does that work on its own).
- Define product-specific false positives and screen them before declaring PMF.

**Must Not:**
- Read ephemeral launch energy (founder's friends, an investor's portfolio buyers, a forum spike) as PMF.
- Call signups, gross revenue, or enthusiasm "PMF" without activation, retention, and repeat usage behind them.
- Recommend a pivot before at least 3 iteration cycles without meaningful PMF movement.

**Instructions:**

1. **Apply the Sean Ellis test.** Survey active users with "How would you feel if you could no longer use this product?" and assess the share answering "very disappointed" against the >40% threshold as a meaningful PMF indicator.

2. **Apply the effort test.** Determine whether retention requires constant founder intervention (outreach, incentives, follow-up) — the pre-PMF signature — or whether the product "starts doing that work on its own." When things begin pulling instead of pushing, something real has changed.

3. **Screen for false PMF.** Check whether early energy came from ephemeral sources that don't predict week-6/week-12 behavior, and define product-specific false positives: signups without activation, revenue without retention, enthusiasm without repeat usage.

4. **Render the PMF verdict.** Combine the two tests and the false-positive screen into a verdict: genuine PMF, partial/uncertain, or no PMF.

5. **Run the pivot diagnostic (only after 3+ stalled cycles).** If PMF is absent after at least three iteration cycles without meaningful movement, ask: (a) Is there a segment responding differently from the rest? (b) Is the gap between designed value and experienced value a POSITIONING problem or a PRODUCT problem? (c) What would have to be true for the current product to find genuine PMF, and is that realistic?

6. **Map answers to a recommendation.** Translate the diagnostic into adjust (messaging/onboarding/feature emphasis), pivot (segment or value prop), or return to the idea stage.

7. **Run the adversarial step.** Make the strongest case AGAINST the founder's own traction — argue the most skeptical reading of the data — then state what survives that challenge.

**Output Format:**

A markdown diagnostic brief:
- **PMF Verdict** — genuine / partial / none, with the two tests' results
- **False-Positive Check** — which ephemeral sources / vanity signals were ruled out
- **Pivot Diagnostic** — segment, positioning-vs-product, what-would-have-to-be-true (if applicable)
- **Recommendation** — adjust / pivot / return-to-idea, with reasoning
- **Adversarial Case** — the strongest argument against the traction + what survives it

## Verification

- [ ] The Sean Ellis test is applied with the >40% "very disappointed" threshold.
- [ ] The effort test distinguishes founder-push from product-pull.
- [ ] Ephemeral launch energy and vanity signals are screened out.
- [ ] The pivot diagnostic runs only after 3+ stalled iteration cycles.
- [ ] The recommendation (adjust/pivot/return) follows from the diagnostic answers.
- [ ] An adversarial case against the traction was made and addressed.

## False-Positive Prevention

❌ **DON'T:**
- Declare PMF from a launch-day spike of friends and a forum thread.
- Count signups or gross revenue as fit without activation and retention behind them.
- Pivot on the first weak week before genuine iteration has occurred.
- Accept the founder's optimistic read without arguing the skeptical one.

✅ **DO:**
- Require >40% "very disappointed" plus product-pull retention before calling it PMF.
- Define and rule out product-specific false positives (signups w/o activation, revenue w/o retention).
- Run the pivot diagnostic only after 3+ stalled cycles, then map to adjust/pivot/return.
- Make the strongest case against the traction and report what survives.

## Example Output

```markdown
## PMF & Pivot Diagnostic: Freelancer Invoicing App

### PMF Verdict
Partial / uncertain. Sean Ellis test: 28% "very disappointed" — below the 40% threshold. Effort test: retention still requires weekly founder nudges — product-push, not pull.

### False-Positive Check
Ruled out: launch came largely from the founder's Slack communities (ephemeral). Signups (2,400) high but only 9% activated — vanity signal.

### Pivot Diagnostic (after 4 stalled cycles)
- Segment: solo design freelancers show 51% "very disappointed" vs. 28% overall — a responding segment.
- Gap: experienced value lags designed value mainly at onboarding — leans POSITIONING + onboarding, not core product.
- What would have to be true: that the broad "all freelancers" market values automation as much as designers do — not supported.

### Recommendation
Adjust toward pivot: narrow to solo design freelancers (segment pivot) and rework onboarding/positioning before considering a deeper product pivot.

### Adversarial Case
Skeptical read: the 51% designer signal is a small sub-sample and could be noise. What survives: even discounted, designers retain with far less founder intervention — worth a focused test.
```

**Techniques Used:**
- **RT-02 (Role/Stakeholder Framing):** reasons from the founder weighing fit honestly against the data.
- **RT-05 (Reflexive Stress-Testing):** the adversarial step argues against the founder's own traction.
- **DS-02 (Decision-Criteria Specification):** the Sean Ellis and effort tests are the explicit decision rules.
- **QA-08 (Comparative Evaluation):** compares designed vs. experienced value and segment responses.
- **QA-12 (False Positives Identification):** screens vanity signals and ephemeral launch energy from real PMF.

**Related Prompts:**
- `startup_ai_native_lifecycle_navigator.md` — places this PMF test within the full lifecycle gates.
- `startup_testable_hypothesis_sharpener.md` — sharpens the pivot hypotheses into testable form.
- `validation_am_i_being_nuts.md` — a sanity check on the founder's read of the traction.
