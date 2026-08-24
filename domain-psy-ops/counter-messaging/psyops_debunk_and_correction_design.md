---
title: "Correction Design — Replacing a False Belief Rather Than Just Denying It"
category: psy-ops/counter-messaging
description: "Design a correction that actually displaces a false belief: leading with the true account, stating the falsehood once and clearly marked, explaining the manipulation, and — critically — supplying an alternative causal story, because a gap left where an explanation was tends to be refilled with the false one. Handles the continued-influence effect and the risk of amplifying by correcting."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - debunking
  - corrections
  - communications
  - counter-messaging
updated: "2026-07-28"
reasoning:
  styles: [design, analytic, evidential]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: correction_design
  user_role: [communications, journalist, policy, educator]
  mode: [design, decide, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md
  - domain-psy-ops/counter-messaging/psyops_prebunking_inoculation_design.md
  - domain-psy-ops/technique-analysis/psyops_propaganda_technique_identification.md
---

# Correction Design

**Objective:** Design a correction that **displaces** a false belief rather than merely contradicting it. The difficulty is well documented: people who accept a correction often continue to reason from the corrected information afterward — the continued-influence effect — because a belief that has been removed leaves an explanatory gap, and a gap tends to get refilled with whatever was there before.

The design therefore does four things in a fixed order. It **leads with the true account** so the first and most memorable content is accurate. It **states the falsehood once, clearly marked**, because pretending the claim does not exist leaves it unaddressed for anyone who already holds it. It **explains the manipulation**, which gives the audience something durable. And it **supplies an alternative causal story** — what actually happened and why — because that is what fills the gap. A correction that only says "this is false" is the version most likely to fail, however accurate it is.

Before any of that, though: **check whether to correct at all.** Correcting a claim in front of an audience that had not encountered it introduces it to them, and for small-reach claims the correction is frequently the moment of widest exposure.

**When to use:**
- A false claim has reached your audience and you have decided a correction is warranted.
- You are correcting your own error and want it to actually land.
- A claim keeps recurring despite previous corrections, and you want to understand why the last one failed.
- You are building a fact-check that must work on people who currently believe the claim.

**When NOT to use:**
- You have not decided whether to respond — use `psyops_rumor_response_triage.md` first. That decision comes before this design.
- The claim has not yet spread to your audience — use `psyops_prebunking_inoculation_design.md`.
- The claim is true or partly true. Then this is not a correction; it is a response, and denial will make it worse.

**Audience:** Communications teams, journalists and fact-checkers, public health and election officials, and educators.

---

## Inputs / Context

1. **The false claim.** Stated exactly as it circulates, in the audience's words rather than yours.
2. **The truth**, in as much detail as you can substantiate, with sources.
3. **The explanatory gap.** What the false claim explains for the people who believe it. This is the most important input and the one usually skipped.
4. **The audience.** Who holds the belief, how strongly, and whether it connects to identity or to a real grievance.
5. **Reach so far.** How widely it has actually spread, and whether your audience has encountered it.
6. **Your standing.** Whether you are trusted by the people who hold the belief, and whether you are implicated in the claim.

---

## Constraints

### Must
- Confirm the **response decision** was made deliberately, and assess amplification risk before designing.
- **Lead with the truth**, not the falsehood. The first sentence carries the accurate account.
- State the false claim **once, explicitly marked as false**, and never repeat it in a headline, a summary, or a caption.
- Supply an **alternative causal explanation** that fills the gap the false claim was filling.
- **Explain the technique** used, which protects against the next instance as well as this one.
- Keep the correction **simpler than the claim**. A correction requiring more effort than the falsehood loses.
- Address the **real grievance** where one underlies the false claim, without conceding the false part.
- Choose the **messenger** the audience actually trusts, which is frequently not the organization implicated.

### Must Not
- Repeat the false claim in the headline, first line, image caption, or social summary. Those are the parts most people see, and repetition builds familiarity, which builds belief.
- Correct with contempt. Ridiculing believers reliably entrenches the belief and forecloses the correction.
- Overclaim certainty. Stating more than the evidence supports produces a correction that later needs correcting — the most expensive failure available.
- Deny a partly-true claim wholesale. Concede the true part precisely, or the whole correction is discredited by the part that was right.
- Fabricate sources or research findings, including about how corrections work.
- Correct at length. Long corrections are read by people who already agree.
- Assume one correction is sufficient. Belief change is gradual and repetition of the *true* account is what does the work.

---

## Instructions

### Step 1 — Confirm the response decision and amplification risk
Has the claim reached your audience? If most of them have not seen it, correcting introduces it. Estimate the reach of the claim versus the reach of your correction.

### Step 2 — Establish what is true, precisely
Including any part of the claim that is accurate. A correction that denies a true element will be dismantled at that element.

### Step 3 — Identify the explanatory gap
What does the false claim explain for the people who hold it? A cause for something that hurt them, an actor to blame, a reason events unfolded as they did. **This is the load-bearing step.** Without an alternative, the gap re-fills with the claim you just removed.

### Step 4 — Build the alternative causal story
What actually happened, and why. Concrete and specific. This is what the audience needs to hold instead — not an absence.

### Step 5 — Structure the correction
Truth first, in the first sentence. Then the false claim once, clearly marked. Then why it is false. Then the technique that made it persuasive. Then the true account again, as the closing content.

### Step 6 — Address the underlying grievance
If the claim attached to a real frustration — and it usually has — acknowledge that directly. Correcting the facts while dismissing the grievance loses the audience regardless of accuracy.

### Step 7 — Choose the messenger and channel
Who does this audience trust? Where do they actually encounter information? An accurate correction on a channel they do not read is not a correction.

### Step 8 — Check the surfaces, then run the adversarial check
Review the headline, the social summary, the image caption, and any push notification — the false claim must not appear in any of them. Then argue that this correction will entrench the belief, and revise.

---

## False-Positive Prevention

1. **Falsehood in the headline.** The single most common error. Headlines and summaries are what most people see, and repetition builds familiarity regardless of the "false" label.
2. **No alternative explanation.** Removing a belief without replacing it. The gap refills with the original claim, which is why some corrections measurably increase belief.
3. **Contempt.** Mockery of believers, which entrenches, and which is usually written for the audience that already agrees.
4. **Correcting to an unexposed audience.** Introducing a claim under the banner of correcting it — often the moment of widest exposure for a small-reach falsehood.
5. **Wholesale denial of a partly-true claim.** The true fragment survives, and it discredits everything attached to the denial.
6. **Overclaiming.** Stating certainty beyond the evidence, producing a correction that itself needs correcting later.
7. **Length.** Comprehensive corrections that only the already-convinced finish reading.
8. **Grievance dismissed.** Correcting the fact while ignoring the real frustration underneath, which reads as confirmation that nobody is listening.

---

## Output Format

```
# Correction design — [claim]

## Response decision
- Has this reached our audience? [yes/no + evidence]
- Claim reach vs correction reach: [...]
- **Correcting is warranted because:** [...]

## What is true (precisely)
[Including any part of the claim that is accurate — conceded exactly]

## The explanatory gap
[What the false claim explains for the people who believe it]

## The alternative causal story
[What actually happened and why — the thing that fills the gap]

## The correction

**Headline / first line (truth only — claim must not appear here):**
"[...]"

**Body:**
1. [The true account, stated first]
2. [The false claim, once, clearly marked as false]
3. [Why it is false — briefly]
4. [The technique that made it persuasive]
5. [The true account again, closing]

**Length check:** [shorter than the claim? yes/no]

## The underlying grievance
[The real frustration this attached to, acknowledged without conceding the false part]

## Messenger and channel
[Who this audience trusts; where they actually encounter information]

## Surface check
| Surface | Contains the false claim? |
|---|---|
| Headline | no |
| Social summary | no |
| Image caption | no |
| Push notification | no |

## Repetition plan
[How the true account gets repeated — one correction is not sufficient]

## Adversarial check
[The case that this correction will entrench the belief — and what was revised]
```

---

## Verification

- [ ] The response decision was made deliberately, with amplification risk assessed.
- [ ] The correction leads with the truth; the false claim appears once, clearly marked.
- [ ] The false claim appears in no headline, summary, caption, or notification — surface check completed.
- [ ] An alternative causal explanation is supplied that fills the explanatory gap.
- [ ] The technique behind the claim is explained.
- [ ] Any true portion of the claim is conceded precisely rather than denied wholesale.
- [ ] The correction is shorter than the claim and contains no contempt for believers.
- [ ] Certainty does not exceed the evidence, and no source or research finding was fabricated.
- [ ] The underlying grievance is acknowledged where one exists.
- [ ] A repetition plan exists, on a channel the audience uses, from a messenger they trust.
