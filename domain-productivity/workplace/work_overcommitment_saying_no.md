---
title: "Audit Chronic Overcommitment and Build a Decision Rule for Saying No"
category: productivity/workplace
description: "Read a list of the user's recent yeses to find the real reason each one was granted and its true weekly cost, then produce a personal saying-no decision rule and ready-to-send decline scripts for the commitment type they most need to stop accepting."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - productivity
  - overcommitment
  - saying-no
  - boundaries
  - prioritization
updated: "2026-07-23"
related_prompts:
  - domain-productivity/deep-work/deepwork_personal_energy_audit.md
  - domain-productivity/bottlenecks/bottleneck_open_loop_audit.md
  - domain-personal-development/prompts/relationships/relationships_boundary_setting_script.md
  - domain-personal-development/prompts/agency/agency_foundation_session.md
---

# Audit Chronic Overcommitment and Build a Decision Rule for Saying No

**Objective:** Diagnose *why* the user keeps saying yes, price each recent yes at its true recurring cost, and output one personal decision rule plus decline scripts for the single commitment type that is doing the most damage.

**When to use:** The user's calendar and to-do list keep filling faster than they empty, they resent commitments they agreed to, or they notice they say yes fast and regret it later. Useful before a busy quarter, or right after a week where nothing they actually valued got done. Not for a one-off hard conversation about a single relationship — that is `relationships_boundary_setting_script.md`.

**Audience:** An individual auditing their own commitments. Not for managing someone else's workload, and not clinical. If the inability to say no is tied to persistent anxiety, fear, or a sense that refusing will cause harm to you, that is beyond scheduling — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Recent yes log — last 30 days.** 8–15 things the user agreed to where they could plausibly have said no. Each as: *what it was → who asked → how fast they said yes → recurring or one-off → rough time cost per week.* Include work, favors, social, volunteer, and self-imposed commitments. "Attended the standup" (non-optional) does not count; "agreed to run the standup" does.
2. **What got squeezed.** 2–4 things the user wanted to do this month but didn't (a project, exercise, a relationship, rest). These are the true price of the yeses.
3. **The last yes they regret.** One specific recent commitment they wish they'd declined, and what they told themselves in the moment they agreed.
4. **Their current default.** In one line: what happens in their body/mind when someone asks — do they feel obligated, flattered, afraid of disappointing, afraid of missing out, or something else?

If the yes log has fewer than 6 genuinely optional commitments, refuse and ask for more. Overcommitment can't be diagnosed from commitments that were never really choices.

---

## Instructions

### Step 1 — Classify why each yes was granted

Tag every item in input 1 with exactly one **yes-driver** from this fixed taxonomy. Cite the evidence (the speed of the yes, who asked, input 4).

| Yes-driver | What it is |
|---|---|
| **Approval** | Yes to be liked / not disappoint the asker |
| **Identity** | Yes because "I'm the person who helps / delivers / shows up" |
| **FOMO** | Yes to avoid missing an opportunity or being left out |
| **Guilt** | Yes because no felt selfish or ungrateful |
| **Avoidance** | Yes to a small ask to avoid a harder thing you should be doing |
| **Genuine** | Yes you'd make again with full information — the commitment is worth it |

### Step 2 — Price each yes at its true recurring cost

For each non-Genuine yes, compute the honest cost: *time per week × weeks it runs*, plus the switching/dread tax (a recurring commitment costs more than its clock time because it occupies mental space). Sum the weekly hours of the non-Genuine yeses. Set that total against input 2 — name which squeezed item each block of reclaimed time could have covered.

### Step 3 — Find the dominant driver and commitment type

Tally the yes-drivers. One driver almost always dominates. Name it, and name the **commitment type** it clusters around (e.g., "Approval-driven yeses to last-minute work favors," "Identity-driven yeses to volunteer roles"). This pairing — driver + type — is the target. Do not try to fix all six drivers.

### Step 4 — Build the decision rule

Write one **if–then rule** the user can apply at the moment of being asked, aimed at the dominant driver+type. It must be mechanical enough to run without deliberation. Form: *"When [specific type of ask] happens, I [specific default: decline / delay 24h / cap at N hours / require a trade]."* Ground the threshold in the Step 2 numbers, not a round-number guess.

Pair it with one **pause line** the user says out loud to buy time before any yes: e.g., "Let me check my commitments and come back to you tomorrow." This converts a reflexive yes into a decision.

### Step 5 — Write the decline scripts

Produce 2–3 short, sayable decline scripts for the target commitment type: a warm no, a firm no, and a "no-but" (a smaller thing the user would actually do). Each ≤3 sentences, first person, no over-apology, no fabricated excuse. A decline states the no and stops; it does not audition reasons.

### Step 6 — Name the one yes to reverse now

Pick the single existing commitment with the highest weekly cost and a non-Genuine driver, and script one message to exit or renegotiate it this week. This is the decisive move — reclaiming committed time, not just guarding future time.

---

## Constraints

### Must
- Tag every optional yes with exactly one driver from the fixed taxonomy, with evidence.
- Compute recurring cost in weekly hours and tie it to a specific squeezed item from input 2.
- Target one driver+type pairing, not all six.
- Produce one mechanical if–then decision rule with a data-grounded threshold.
- End with one existing commitment to reverse this week, with a script.

### Must Not
- Recommend "just say no more" or "value your time" as advice — every output must be a specific rule, script, or move.
- Moralize about people-pleasing or frame the user as weak for saying yes.
- Fabricate a decline excuse; scripts state a true no, not an invented conflict.
- Diagnose anxiety, trauma, or a personality trait.
- Output a full commitment-management system — the deep version is `domain-productivity/deep-work/`; link across, don't rebuild.

---

## False-Positive Prevention

1. **Don't relabel a Genuine yes as overcommitment.** Some yeses are worth it. If the user would make the choice again fully informed, tag Genuine and leave it alone — the goal isn't a smaller life.
2. **Don't count non-optional obligations.** A yes that was never a real choice (mandatory work, caregiving duty) is not overcommitment; excluding it keeps the audit honest.
3. **Don't average across drivers.** One driver dominates; naming it is the whole point. A tie usually means Step 1 evidence was too thin — push back to the yes log.
4. **Don't treat time cost as the only cost.** A one-hour recurring commitment the user dreads can cost more attention than a five-hour one-off. Weigh the dread/switching tax.
5. **Don't confuse this with a relationship boundary.** If the yeses cluster around one person and the issue is the relationship dynamic, route to `relationships_boundary_setting_script.md` instead of a generic decision rule.
6. **Don't manufacture a decline reason.** "I'm busy that day" when they aren't teaches the user to lie and invites renegotiation. The script declines; it doesn't justify.

---

## Output Format

```
## Why you said yes (last 30 days)
| Commitment | Asker | Yes-driver | Recurring? | ~hrs/week |
|---|---|---|---|---|
| ... | ... | Approval/Identity/FOMO/Guilt/Avoidance/Genuine | Y/N | ... |

Non-Genuine total: ~[X] hrs/week
That time could have covered: [squeezed item from input 2]

## Your dominant pattern
Driver: [name]. Clusters around: [commitment type]. Evidence: [2–3 items].

## Your decision rule
When [specific ask type] happens → I [specific default].
Pause line (say before any yes): "[line]"

## Decline scripts (for [target type])
- Warm no: "[≤3 sentences]"
- Firm no: "[≤3 sentences]"
- No-but: "[≤3 sentences]"

## Reverse this one now
Commitment: [highest-cost non-Genuine one]. Message to send: "[script]".

Predicted check: within two weeks, [X] hrs/week returns and [squeezed item] gets its first block of time.
```

---

## Verification

- [ ] Every optional yes carries exactly one taxonomy driver, backed by evidence.
- [ ] Recurring cost is in weekly hours and tied to a specific squeezed item from input 2.
- [ ] One dominant driver+type pairing is named; the fix targets only it.
- [ ] The decision rule is a mechanical if–then with a data-grounded threshold, plus a pause line.
- [ ] Decline scripts are ≤3 sentences, first-person, with no fabricated excuse.
- [ ] Exactly one existing commitment is selected to reverse this week, with a script.
- [ ] No moralizing, no clinical labels, no generic "say no more" advice.
