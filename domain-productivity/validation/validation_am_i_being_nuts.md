---
title: "Am I Being Nuts? — Full Reality-Grounding Assessment"
category: "productivity/validation"
description: "A comprehensive 10-section reality check for high-stakes decisions that grounds a claim or plan against base rates, evidence quality, disconfirmation, social-isolation risk, and incentive bias — without therapy, flattery, or fabricated consensus."
techniques:
  - ST-01
  - QA-02
  - RT-02
  - DS-02
  - QA-20
difficulty: advanced
tags:
  - validation
  - reality-check
  - decision-quality
  - anti-fabrication
  - calibration
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_quick_reality_check.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
  - domain-productivity/validation/validation_final_gate.md
---

# Am I Being Nuts? — Full Reality-Grounding Assessment

**Objective:** Subject a high-stakes claim or plan to a rigorous, 10-section reality check that catches self-deception and dangerous thinking patterns before they cause harm — grounding in evidence, base rates, and disconfirmation rather than reassurance.

**When to use:**
- Before a major life decision (career move, relationship, large purchase, relocation).
- When committing significant money, reputation, or irreversible time.
- When you've been working intensely and may have lost outside perspective.
- Anytime you feel unusually certain and want that certainty stress-tested.

**When NOT to use:**
- Low-stakes, easily reversible choices — use `validation_quick_reality_check.md` instead.
- Acute mental-health crises — this is a decision-quality tool, not clinical support; route to a professional.
- When you've already decided and only need execution help (say so explicitly).

**Audience:** Founders, professionals, and individuals facing consequential decisions who want a single rigorous grounding pass.

---

## Inputs / Context

1. **The claim or plan** — one paragraph stating what you believe or intend to do.
2. **Stakes** — what happens if you're wrong (money, reputation, relationships, time, health).
3. **Timeline** — when you must act, and whether the deadline is real or self-imposed.
4. **Verification so far** — what you've already done to check the claim.
5. **Reversibility** — can the decision be unwound, and at what cost.

---

## Constraints

### Must
- Prioritize preventing self-deception over being kind; deliver calibration, not reassurance.
- For every factual claim, cite a source or label it `uncertain` / `inference` / `guess`.
- Separate evidence into Verified / Observed-not-verified / Inferred / Wishcasting buckets.
- Name the single weakest link in the reasoning.
- Surface genuine disconfirming evidence and the strongest hostile-expert objection.
- If mental-health patterns can't be reliably judged, say so and stay in observable-behavior + decision-risk territory.
- Tie the final STOP/GO to reversibility plus verification strength.

### Must Not
- Offer comfort, pep talk, or "you've got this."
- Invent expert consensus, fabricate "10 experts would say…" polling, or manufacture statistics.
- Present a guess or inference as an established fact.
- Rubber-stamp the plan because it sounds plausible or confident.
- Pad the assessment with sections that have no substantive finding.

---

## Instructions

1. **Collect inputs.** Gather the claim, stakes, timeline, verification-so-far, and reversibility (see Inputs).
2. **Run the assessment prompt** below verbatim against the inputs.

   ```
   AM I BEING NUTS? — Ground me in reality.

   Rules:
   - Your job is to prevent self-deception, not to be kind.
   - No reassurance. No "you've got this." Just calibration.
   - For factual claims: cite sources or label uncertain/inference/guess.
   - Do not invent expert consensus or "10 experts would say…" polling.
   - If you can't reliably judge mental health, say so and stay in decision-quality territory.

   INPUTS
   A) My claim / plan (one paragraph): [ ]
   B) Stakes — what happens if I'm wrong? (money, reputation, relationships, time): [ ]
   C) Timeline — when do I have to act, and is the deadline real?: [ ]
   D) What I've done so far to verify: [ ]
   E) Reversibility — can I unwind this?: [ ]

   ASSESSMENT

   1) CLAIM SHAPE (FALSIFIABILITY)
   - Turn my plan into 1–3 testable statements.
   - Define what counts as success, failure, and ambiguous.

   2) BASE RATE + ALTERNATIVES
   - What's the base rate for something like this working? Label it as
     a guess if you don't have a real figure.
   - Give 3 alternative explanations that fit the facts with fewer
     assumptions than my preferred story. Which is most likely?

   3) EVIDENCE AUDIT (4 buckets, as a table)
   - Verified (checkable, sourced)
   - Observed but not verified (I saw/heard it; no independent confirmation)
   - Inferred (my interpretation)
   - Wishcasting (what I want to be true)
   Then: name the single weakest link.

   4) EXPERTISE BOUNDARY (AUDIT CAPACITY)
   - What skills are required to evaluate this properly?
   - Do I have them? If not, who does (specific role)?
   - What would an expert do in 30 minutes to check whether this is nonsense?

   5) DISCONFIRMATION PASS (BREAK IT)
   - List the 5 most likely failure modes.
   - State the strongest objection a hostile-but-competent expert would raise.
   - Name the specific evidence that would falsify me. Does it exist?
   - If this is wrong, what's the most likely reason?

   6) SOCIAL / REALITY-CONTACT CHECK (answer honestly)
   - Am I currently isolated from feedback?
   - Am I discounting critics because they "don't get it"?
   - Am I substituting AI agreement for human review?
   - Am I avoiding the one person who could tell me I'm wrong?

   7) INCENTIVE + EMOTION CHECK
   - What do I gain by believing this?
   - What am I afraid will happen if I slow down and verify?
   - Where might ego, urgency, or identity be driving this?

   8) CALIBRATED CONFIDENCE SCORE (1–10 with justification)
   1 = speculation / thin evidence; 5 = plausible but uncertain;
   9–10 = strongly supported. Then: what would need to be true to move it +2?

   9) ACTION PLAN (GROUNDING)
   - 2 cheap tests (today)
   - 1 medium test (this week)
   - 1 expensive/definitive test (if warranted)
   - STOP/GO tied to reversibility: low-reversibility + weak verification → STOP
     and name the next step.

   10) RED FLAGS (flag only if genuinely present)
   - Rapid escalation in stakes without new evidence
   - Certainty outpacing verification
   - "Me + the AI vs everyone else"
   - Refusal to engage with strongest counterarguments
   - Grandiosity without falsifiable checks
   - Sleep/health neglect framed as "the price of truth"
   (If you can't assess health, say so; focus on observable behavior + decision risk.)
   ```

3. **Self-check before output.** Re-read the draft: confirm no reassurance leaked in, every factual claim is sourced or labeled, no fake consensus appears, red flags are only listed if actually present, and the STOP/GO follows from reversibility + verification.
4. **Deliver** the assessment in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Manufacture a clean base rate ("works ~70% of the time") when no real figure exists.
- Invent objections or "experts agree…" consensus to look thorough.
- Present inference or wishcasting as Verified evidence.
- Soften the confidence score to make the user feel better.
- List every red flag as "present" to seem rigorous (or none, to seem agreeable).

✅ **DO:**
- Label uncertain figures as guesses and say what would be needed to replace them.
- Point objections to source *types* (specs, case law, audit logs, benchmarks) rather than fake authorities.
- Quarantine wishcasting in its own bucket and name the weakest link plainly.
- Give a number you'd actually defend, then state what would move it +2.
- Flag a red flag only when the evidence in the inputs supports it.

---

## Output Format

```
# Am I Being Nuts? — Assessment

## 1. Claim shape (falsifiability)
- Testable statement(s): [...]
- Success / failure / ambiguous: [...]

## 2. Base rate + alternatives
- Base rate: [figure or "guess — no reliable figure"]
- Simpler alternatives: 1) [...] 2) [...] 3) [...]
- Most likely: [...]

## 3. Evidence audit
| Bucket | Items |
|--------|-------|
| Verified | [...] |
| Observed, not verified | [...] |
| Inferred | [...] |
| Wishcasting | [...] |
- Weakest link: [...]

## 4. Expertise boundary
- Skills required: [...]
- Do I have them?: [...]
- Who can verify (specific role): [...]
- 30-minute expert check: [...]

## 5. Disconfirmation pass
- Failure modes (5): [...]
- Strongest hostile-expert objection: [...]
- Falsifying evidence (and whether it exists): [...]

## 6. Social / reality-contact check
- [honest answers, one line each]

## 7. Incentive + emotion check
- [honest answers, one line each]

## 8. Calibrated confidence: X/10
- Justification: [...]
- To move +2: [...]

## 9. Action plan
- Cheap (today): [2]
- Medium (this week): [1]
- Definitive (if warranted): [1]
- STOP / GO: [decision + reason + next step]

## 10. Red flags
- [only those genuinely present, or "None detected in the inputs provided"]
```

---

## Example Output

```
# Am I Being Nuts? — Assessment

Claim: "I should quit my job next month to go full-time on my SaaS side
project; it has 40 paying users and I'm certain it'll replace my salary
within 6 months."

## 1. Claim shape (falsifiability)
- Testable: (a) MRR will reach my salary equivalent within 6 months of
  going full-time; (b) churn stays below 5%/month.
- Success = MRR ≥ take-home pay by month 6. Failure = MRR < 50% of it.
  Ambiguous = somewhere between.

## 2. Base rate + alternatives
- Base rate: guess — I don't have a reliable figure for "indie SaaS at 40
  users replaces a full salary in 6 months." Anecdotally it's uncommon;
  treat as low until you find real cohort data.
- Simpler alternatives: 1) growth has been driven by a one-time launch
  bump, not a repeatable channel; 2) the 40 users skew toward friends /
  early discounts and won't renew at full price; 3) you're conflating
  "people signed up" with "people will keep paying."
- Most likely: #1 — no evidence yet of a repeatable acquisition channel.

## 3. Evidence audit
| Bucket | Items |
|--------|-------|
| Verified | 40 active paid subscriptions this month (Stripe export) |
| Observed, not verified | "Users love it" (a few enthusiastic emails) |
| Inferred | Growth will continue linearly |
| Wishcasting | It'll replace my salary in 6 months |
- Weakest link: no proven, repeatable channel that produces new paying
  users every week without a launch event.

## 4. Expertise boundary
- Skills required: cohort/retention analysis, CAC/LTV modeling, runway math.
- Do I have them?: partially — I can pull Stripe data but haven't modeled
  cohorts or churn.
- Who can verify: a founder who's run a subscription business, or an
  operator who can read a cohort table.
- 30-minute expert check: pull last 3 monthly cohorts, look at month-2 and
  month-3 retention; if it's falling off a cliff, the thesis is dead.

## 5. Disconfirmation pass
- Failure modes: (1) churn spikes after the launch cohort; (2) no channel
  beyond the one HN post; (3) full-price conversion is far below trial;
  (4) burn exceeds runway before MRR catches up; (5) you lose health
  insurance and a setback forces a fire-sale return to employment.
- Strongest objection: "You have one launch spike and zero evidence of
  repeatable acquisition; 40 users is a hobby, not a business model yet."
- Falsifying evidence: flat-to-declining new-paid-users in weeks with no
  launch event. This data exists — you just haven't looked at it weekly.

## 6. Social / reality-contact check
- Isolated from feedback?: Somewhat — you've mostly discussed this with
  the AI and supportive friends.
- Discounting critics?: Yes — you dismissed a mentor's "wait for runway"
  as too conservative.
- Substituting AI agreement for human review?: Risk present.
- Avoiding the one person who'd say no?: Your spouse, per your own framing.

## 7. Incentive + emotion check
- Gain from believing it: escape from a job you dislike; identity as a
  "founder."
- Fear if you slow down: that the momentum/excitement will fade.
- Driver: urgency and identity more than verified economics.

## 8. Calibrated confidence: 3/10
- Justification: one verified data point (40 paid users), no channel proof,
  no cohort/runway model, and a real downside (lost income + insurance).
- To move +2: show 8 consecutive weeks of new paid users without a launch
  event, plus month-3 retention above 90%.

## 9. Action plan
- Cheap (today): pull 3 monthly cohorts and chart retention; chart weekly
  new-paid-users for the last 8 weeks.
- Medium (this week): build a simple runway model (savings ÷ monthly burn)
  and a CAC estimate from your real acquisition.
- Definitive (if warranted): run the project nights/weekends for 2 more
  months and require a repeatable channel before quitting.
- STOP / GO: STOP on quitting next month. Reversibility is LOW (lost income,
  insurance, re-hiring friction) and verification is WEAK. Next step: get the
  cohort + runway numbers in front of someone who's operated a subscription
  business before you set a quit date.

## 10. Red flags
- Certainty outpacing verification (present).
- "Me vs the cautious people" framing (present — dismissing the mentor).
- Possible AI-agreement substitution for human review (present).
- No grandiosity or health-neglect signal in the inputs provided.
```

---

## Verification

- [ ] Claim restated as 1–3 falsifiable statements with success/failure defined.
- [ ] Base rate given with a real figure or explicitly labeled a guess.
- [ ] Evidence sorted into all four buckets; weakest link named.
- [ ] Expertise boundary names a specific verifying role, not "someone smart."
- [ ] Disconfirmation lists 5 failure modes and the strongest hostile objection.
- [ ] Social-isolation and incentive checks answered honestly, not skipped.
- [ ] Confidence score has justification and a concrete +2 condition.
- [ ] Action plan tiers tests by cost; STOP/GO follows from reversibility + verification.
- [ ] Red flags listed only when genuinely present.
- [ ] No reassurance, no invented consensus, no statistics presented as fact.

---

## Techniques Used
- **ST-01 (Role Definition):** Casts the model as a calibration engine whose job is to prevent self-deception, not comfort.
- **QA-02 (Adversarial Verification):** Drives the disconfirmation pass, failure-mode enumeration, and hostile-expert objection.
- **RT-02 (Explicit Uncertainty Quantification):** Forces the 1–10 calibrated confidence score and "label guesses as guesses."
- **DS-02 (Evidence-Based Reasoning):** Structures the four-bucket evidence audit and source-type grounding.
- **QA-20 (Dual-Failure / Both-Directions Check):** Surfaces both over-confidence (rubber-stamping) and reflexive doubt via the red-flag and incentive checks.

---

## Related Prompts
- `domain-productivity/validation/validation_quick_reality_check.md` — the fast 2-minute version for lower-stakes calls.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — a focused attack-the-conclusion pass.
- `domain-productivity/validation/validation_final_gate.md` — the pre-commitment STOP gate for irreversible decisions.
