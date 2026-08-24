---
title: "Process Harsh Criticism by Separating the Sting From the Signal"
category: personal-development/resilience
description: "Take a piece of harsh criticism or feedback, split delivery from content, decompose it into discrete testable claims, verdict each against a fixed truth taxonomy weighted by source credibility, and decide the one change to make — or that none is warranted."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - resilience
  - criticism
  - feedback
  - signal-extraction
  - source-credibility
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/resilience/resilience_rejection_recovery.md
  - domain-personal-development/prompts/resilience/resilience_failure_reframe.md
  - domain-personal-development/prompts/agency/agency_feedback_extraction.md
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
  - domain-personal-development/prompts/emotional-fitness/emotionalfitness_disappointment_processing.md
---

# Process Harsh Criticism by Separating the Sting From the Signal

**Objective:** Turn a stinging criticism into a set of verdicted claims — separating how it was delivered from whether it is true — and decide the single change worth making, or a defended decision to change nothing.

**When to use:** The user received harsh feedback, a cutting review, or a blunt personal critique and can't tell how much of it is real. Useful when the tone is clouding the content, or when the user is tempted to either fully accept or fully dismiss it. **Not for this:** feedback on the user's own shipped work that they want to mine neutrally — use `agency_feedback_extraction.md`; or their own failure — use `resilience_failure_reframe.md`.

**Audience:** An individual processing criticism aimed at them. Not for evaluating someone else's critique of a third party, and not clinical. If the criticism has triggered pervasive, self-defining shame, hopelessness, or any thought of self-harm, this is not a substitute for professional support — see `domain-psychology/` and a licensed professional. In the US, call or text 988.

---

## Inputs Required

1. **The criticism, verbatim.** The actual words, not a paraphrase. Paraphrase leaks the user's interpretation into the data.
2. **The source.** Who said it, their standing/expertise on this topic, and any conflicting incentive (competitor, rival, someone who benefits from the user shrinking).
3. **The delivery.** How it landed — cruel, blunt, careless, or fair — kept separate from content.
4. **What it's about** — the specific work, trait, or behavior targeted.
5. **The user's reaction, verbatim**, and whether they've heard this from anyone else before (pattern check).

If input 1 is a paraphrase or input 2 is missing, ask for the exact words and the source before proceeding. Both are load-bearing for the verdicts.

---

## Instructions

### Step 1 — Separate delivery from content

State plainly: a cruel tone does not make a claim false, and a kind tone does not make it true. Set the delivery (input 3) aside explicitly so the sting stops arbitrating the truth. Acknowledge the sting is real without letting it vote.

### Step 2 — Decompose into discrete claims

Break the criticism (input 1) into separate, specific claims rather than one blob. "This is lazy and derivative and you clearly didn't try" is three claims, not one. Vague globs ("it's just bad") get flagged as untestable.

### Step 3 — Verdict each claim

Assign every claim a verdict from this fixed taxonomy:

| Verdict | Criterion | Implied action |
|---|---|---|
| **True + worth changing** | Accurate and the fix's benefit exceeds its cost. | Candidate for the one change. |
| **True + not worth changing** | Accurate but low-stakes or costly to fix. | Note, don't act. |
| **Partly true / distorted** | A real kernel wrapped in exaggeration. | Extract the kernel; drop the exaggeration. |
| **False / projection** | Contradicted by evidence, or about the critic. | Release. |
| **Taste / unfalsifiable** | Preference with no fact to test. | Weigh by whether the audience shares the taste. |

### Step 4 — Weight by source credibility and pattern

For claims that survive as true or partly true, weight them: does the source have standing, data, and low conflicting incentive (input 2), and has anyone else independently said the same (input 5)? A single low-credibility voice with a conflicting incentive gets down-weighted; a pattern across credible sources gets up-weighted.

### Step 5 — Decide one change (or none)

Pick **exactly one** change — the highest-weighted "true + worth changing" claim — and make it specific and bounded. If nothing clears the bar, decide explicitly to change nothing and state why. Both are valid decisive outputs; a list of "things to consider" is not.

---

## Constraints

### Must
- Separate delivery from content before verdicting.
- Decompose the criticism into discrete claims.
- Verdict every claim with the fixed taxonomy.
- Weight surviving claims by source credibility and cross-source pattern.
- Output exactly one change or a defended decision to change nothing.

### Must Not
- Accept a claim because it was delivered with authority or force.
- Reject a claim solely because the delivery was cruel.
- Treat one critic's taste as established fact.
- Over-correct to appease a low-credibility, conflicted source.
- Diagnose any condition or moralize about the critic's character beyond noting incentive.

---

## False-Positive Prevention

1. **Don't let harsh equal correct.** A confident, brutal delivery is not evidence of accuracy — the loudest critic is not automatically right.
2. **Don't let cruel equal false.** Dismissing true signal because it was delivered unkindly protects the ego and discards the lesson. Test the content anyway.
3. **Don't promote taste to fact.** "I didn't like it" is unfalsifiable; weigh it by audience fit, not truth.
4. **Don't over-weight a conflicted source.** A rival who benefits from the user shrinking gets their incentive named and their claims down-weighted.
5. **Don't mistake one loud voice for a pattern.** A pattern needs independent sources (input 5); one person repeating themselves is still one data point.
6. **Don't process clinical shame as criticism.** If the critique has become a pervasive, self-defining verdict, that's beyond this tool — refer (see Audience).

---

## Output Format

```
## Delivery vs. content
Delivery: [cruel / blunt / fair]. Set aside — it does not vote on truth. The sting is real; the content is judged separately.

## Claims and verdicts
| Claim (from verbatim) | Verdict | Weight (source + pattern) |
|---|---|---|
| ... | True+worth / True+not / Partly / False / Taste | high/med/low — [why] |

## The decision
[One specific, bounded change — the highest-weighted true+worth claim.]
OR: Change nothing, because [defended reason].

Predicted check: after acting (or deciding not to), the criticism reads as a set of sorted claims, not one undifferentiated verdict on you.
```

---

## Verification

- [ ] Delivery is separated from content before any verdict.
- [ ] The criticism is decomposed into discrete claims.
- [ ] Every claim carries a fixed-taxonomy verdict.
- [ ] Surviving claims are weighted by source credibility and cross-source pattern.
- [ ] Output is exactly one change or a defended "change nothing," not a menu.
- [ ] No "harsh = true" or "cruel = false" reasoning; taste kept distinct from fact.
- [ ] Clinical boundary honored; referral issued if shame is pervasive/clinical.
