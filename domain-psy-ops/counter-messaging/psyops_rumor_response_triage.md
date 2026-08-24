---
title: "Rumor Response Triage — Whether Answering Would Do More Harm Than Silence"
category: psy-ops/counter-messaging
description: "Decide whether to respond to a false or hostile claim at all, weighing current reach against the reach a response would create, the audience that matters, and the cost of silence. Treats 'monitor and do not respond' as a decision with owners and tripwires rather than as inaction, and blocks the reflex to respond to everything visible to the communications team."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - crisis-communications
  - amplification
  - decision
  - counter-messaging
updated: "2026-07-28"
reasoning:
  styles: [evaluative, analytic, adversarial]
  stakes: high
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: team
  output_format: response_decision
  user_role: [communications, executive, policy, trust_and_safety]
  mode: [decide, assess, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_debunk_and_correction_design.md
  - domain-psy-ops/counter-messaging/psyops_crisis_communication_integrity_plan.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Rumor Response Triage

**Objective:** Decide whether to respond to a false or hostile claim **at all**. This decision comes before any correction design and is more consequential than the wording of any response, because responding converts a claim's audience from whoever found it into whoever follows you. For a claim with small reach, the response is routinely the moment of widest exposure — the organization introduces the accusation to its own customers, staff, and regulators under a headline it wrote itself.

The counterweight is that **silence is not free**, and the "do not amplify" principle is regularly used to justify not answering things that genuinely needed answering. Silence reads as confirmation to people already exposed, it leaves staff and partners without a line to use, it cedes the record to whoever is speaking, and it gets harder to break the longer it runs. The choice is a genuine trade, not a rule.

The structural problem the triage is designed against is that **the communications team's field of view is not the audience's**. Everything looks urgent from inside a monitoring dashboard. The question is never "have we seen this" but "has anyone who matters seen this, and would our answer reach them or introduce it to them."

**When to use:**
- A false or hostile claim is circulating and someone is asking whether to respond.
- Pressure is building internally to say something, and you want the decision made deliberately.
- You have responded to similar claims before and want to know whether it helped.
- You need to justify a decision not to respond to an executive who wants action.

**When NOT to use:**
- You have already decided to respond and need the correction built — use `psyops_debunk_and_correction_design.md`.
- You are in an active, fast-moving crisis with multiple claims — use `psyops_crisis_communication_integrity_plan.md`.
- The claim is true. Then this is not a response question; it is a remediation and disclosure question.

**Audience:** Communications leads, executives, policy and trust-and-safety teams.

---

## Inputs / Context

1. **The claim.** Exactly as stated, and whether it is false, partly true, or unverified. If unverified, that is the first thing to resolve.
2. **Current reach.** Actual, measured — unique accounts and estimated humans, not impressions or post counts.
3. **Trajectory.** Growing, flat, or decaying, over what period. A decaying claim usually needs nothing.
4. **Who has seen it that matters.** Regulators, large customers, your own staff, journalists, investors. This is the decisive input.
5. **Your reach.** How many people your response would reach who have not encountered the claim.
6. **Cost of silence.** What happens if you say nothing: to staff, partners, the record, and any legal or regulatory process.
7. **Prior responses.** What happened last time you engaged with something similar.

---

## Constraints

### Must
- Compare **claim reach against response reach** in the same units, and state how many people a response would newly expose.
- Identify whether **anyone with power over your outcomes** has encountered it. This usually decides the question on its own.
- Assess **trajectory**, and treat a decaying claim differently from a growing one.
- Cost **silence explicitly** — it is a choice with consequences, not a null option.
- Consider **narrow response** options between silence and public statement: briefing staff, responding to the specific journalist, answering the regulator directly, replying only where it circulates.
- Make **"monitor, do not respond"** a real decision with a named owner and **tripwires** that would change it.
- Check the **internal-pressure** source: whether the urgency comes from the audience or from executive discomfort.
- Record the decision and its **reasoning**, so a later review can assess the call rather than the outcome.

### Must Not
- Respond by reflex because the claim is false and visible to the team. Falsity does not settle the response question.
- Use "don't amplify" to avoid answering something that has genuinely reached people who matter. That is the principle's most common abuse.
- Treat impressions or post counts as reach. Resolve to unique accounts and estimated humans.
- Decide by executive discomfort. Note it as a factor and keep it separate from the assessment.
- Fabricate reach figures, trajectory data, or claims about prior response outcomes.
- Choose silence for a claim that is true or partly true. That is a disclosure decision and delay compounds it.
- Leave "no response" undated and unowned, which is how it becomes permanent by default.

---

## Instructions

### Step 1 — Resolve the truth status first
False, partly true, or unverified. If unverified, resolve it before deciding anything. If true or partly true, exit this prompt — the question is disclosure and remediation, not response.

### Step 2 — Measure actual reach
Unique accounts and estimated unique humans. Strip impressions and repetition. Most claims that feel enormous inside a dashboard have reached very few people outside a small community.

### Step 3 — Establish trajectory
Growing, flat, or decaying, and over what window. Most claims decay without intervention, and a decaying claim rarely justifies a response.

### Step 4 — Identify exposure among those who matter
Have regulators, major customers, staff, journalists, or investors encountered it? A claim with tiny public reach that has reached your regulator is a response case. A viral claim that has reached nobody with power over you may not be.

### Step 5 — Calculate the amplification delta
How many people would a response reach who have not seen the claim? If the response reaches ten or a hundred times the claim's audience, the response *is* the exposure event.

### Step 6 — Cost the silence
What breaks if you say nothing: staff without a line, partners asking, the record going uncontested, a regulatory process proceeding on one account, and the increasing difficulty of speaking later.

### Step 7 — Consider the narrow options
Between silence and a public statement: brief staff internally, respond to the one journalist, answer the regulator directly, reply only in the thread where it circulates, or prepare a holding line used only on enquiry. These carry most of the benefit at a fraction of the amplification.

### Step 8 — Decide with tripwires, then run the adversarial check
State the decision, its owner, and the specific tripwires that would change it. Then argue the opposite decision and record why it lost.

---

## False-Positive Prevention

1. **Reflex response.** Answering because the claim is false and the team can see it. Visibility inside a monitoring tool is not reach.
2. **"Don't amplify" as avoidance.** Using the principle to duck something that has genuinely reached people who matter. Check the who-matters question before invoking it.
3. **Impressions read as reach.** Counting post counts and impressions rather than unique humans, which inflates urgency dramatically.
4. **Executive discomfort as input.** Deciding because a senior person is upset. Record it, keep it out of the assessment.
5. **Trajectory ignored.** Responding to a claim that was already decaying, and restarting it.
6. **Silence for a true claim.** Choosing not to respond to something substantially accurate, which converts a problem into a cover-up.
7. **Binary framing.** Treating this as speak-or-silent and missing the narrow options that carry most of the benefit.
8. **Unowned non-decisions.** "Monitor for now" with no owner, no tripwires, and no review date, which becomes permanent silence by accident.

---

## Output Format

```
# Response triage — [claim]

## Truth status
[False / partly true / unverified]
**If true or partly true → exit: this is a disclosure and remediation decision.**

## Reach (actual)
- Unique accounts: [n]
- Estimated unique humans: [n]
- Impressions/post counts: [recorded but not used as reach]

## Trajectory
[Growing / flat / decaying, over what window]

## Exposure among those who matter
| Audience with power over our outcomes | Encountered it? | Evidence |
|---|---|---|
| Regulator | | |
| Major customers | | |
| Our own staff | | |
| Journalists | | |

## Amplification delta
[People our response would reach who have not seen the claim: n]
[Ratio to claim reach: ...] → **the response would/would not be the exposure event**

## Cost of silence
| What breaks | Severity |
|---|---|
| Staff without a line | |
| Record uncontested | |
| Regulatory process on one account | |
| Harder to speak later | |

## Options considered
| Option | Reach | Amplification cost | Benefit |
|---|---|---|---|
| No response, monitor | | none | |
| Internal staff briefing | | low | |
| Respond to specific journalist | | low | |
| Direct response to regulator | | none | |
| Reply in-thread only | | low | |
| Public statement | | high | |

## Decision
[Chosen option] — owner: [name] — review date: [date]

## Tripwires that change this
- [Specific observable, e.g. "any national outlet enquiry"]
- [Specific observable, e.g. "reaches our own staff channels"]

## Internal pressure check
[Is the urgency coming from the audience, or from internal discomfort? — recorded separately]

## Adversarial check
[The case for the opposite decision, and why it lost]
```

---

## Verification

- [ ] Truth status is resolved first, and true or partly-true claims exit to disclosure rather than response.
- [ ] Reach is stated in unique accounts and estimated humans, with impressions excluded from the assessment.
- [ ] Trajectory is assessed and factored in.
- [ ] Exposure among audiences with power over outcomes is established explicitly.
- [ ] The amplification delta is calculated and stated.
- [ ] The cost of silence is itemized rather than treated as zero.
- [ ] Narrow options between silence and public statement were considered.
- [ ] The decision has a named owner, a review date, and specific observable tripwires.
- [ ] Internal pressure is recorded separately from the assessment.
- [ ] No reach figure, trajectory, or prior-outcome claim was fabricated.
