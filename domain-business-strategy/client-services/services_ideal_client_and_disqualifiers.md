---
title: "Ideal Client Profile and Disqualifiers"
category: client-services/qualification
description: "Build a two-sided client profile for a services practice — the traits that predict a good engagement and, more importantly, the observable disqualifiers that predict a bad one, expressed as a decision rule you can apply in the first ten minutes of contact"
techniques:
  - CM-02
  - QA-08
  - RT-05
  - OC-03
  - NE-04
difficulty: intermediate
tags:
  - consulting
  - freelance
  - qualification
  - ideal-client
  - disqualifiers
  - red-flags
  - solo-operator
updated: "2026-09-21"
---

# Ideal Client Profile and Disqualifiers

**Objective:** Produce a **two-sided** client profile: the traits that predict an
engagement will go well, and the observable disqualifiers that predict it will not.
Both sides express as decision rules you can apply in the first ten minutes of
contact, before you have invested proposal time.

**When to Use:** Use this after `services_offer_definition_and_boundary.md` and before
you take another discovery call. The symptom it fixes is a practice that is busy and
unprofitable because it cannot say no early — where the worst engagements were
visible as bad from the first email and got taken anyway.

This is **distinct from** `domain-agentic-resources/skills/marketing/customer-research/`
and `skills/marketing/revops/`, which build a *product* ICP and a lead-scoring system
for a sales funnel. Those rank prospects to pursue. This one exists to **turn work
away**: its centre of gravity is the disqualifier list, which a lead-scoring model
does not have, and it is calibrated for a practice where one bad client consumes a
material fraction of total capacity.

---

## Context Gathering

The raw material is your own history. Ask for it specifically:

1. **The good ones**
   - "Name your three best engagements. Not the biggest — the ones you would repeat."
   - "For each: how did they find you? Who was the buyer? What was the trigger?"
   - "What did the client do that made it work?"

2. **The bad ones**
   - "Name your three worst. What did each cost you beyond the fee?"
   - "At what point did you know? What was the earliest signal, honestly?"
   - "Did you see the signal at the time and proceed anyway? Why?"

3. **The economics**
   - "What fraction of your annual capacity does one engagement of this size consume?"
   - "How long does it take you to replace a client that ends badly?"

If the user cannot name three bad engagements, either they are early or they are not
being honest with themselves. Press once: "which engagement would you not repeat at
twice the fee?"

---

## Method

### Step 1 — Extract the earliest signal, not the eventual problem

For each bad engagement, walk backwards from the blow-up to the first moment the
information was available. The output is not "they had unrealistic expectations" —
that is the eventual problem. It is "in the first call they described a six-month
problem and asked whether it could be done in three weeks, and I answered the
question instead of challenging it."

Disqualifiers must be **observable at first contact**. Anything only visible after
you have started is not a disqualifier; it is a continuation condition and belongs in
the offer boundary.

### Step 2 — Separate the four disqualifier families

| Family | What it looks like at first contact |
|---|---|
| **Authority** | No named decision-maker; the contact must "check with" an unnamed party; the buyer is not the person with the problem |
| **Definition** | The problem is described as a solution; the desired outcome changes between sentences; nobody can say what "done" looks like |
| **Economics** | Budget undisclosed after a direct ask; the fee is a large fraction of their total spend; they lead with rate before scope |
| **Conduct** | Urgency disproportionate to the trigger; prior vendor described as the villain with no self-implication; pressure to skip a written scope |

The prior-vendor signal deserves its own note. A client who describes three previous
providers as incompetent is telling you how they will describe you. Weight it.

### Step 3 — Write the rules with thresholds

Each rule takes this shape, and each has a number or an observable event — not a
feeling:

> **[Family] — [name].** If [observable condition], then [decline / probe with this
> specific question / proceed with this specific protection].

Three response tiers, because most signals are not fatal:

- **Decline** — the engagement is not takeable. Say so in the first call.
- **Probe** — one specific question that resolves it. If the answer is unsatisfying,
  it becomes a decline.
- **Proceed with protection** — takeable, but only with a named structural change:
  a paid discovery phase first, milestone payment, a smaller first engagement, a
  written decision-maker sign-off.

The third tier is what stops this becoming a list you ignore. A profile that only
declines will be overridden the first time the pipeline is thin.

### Step 4 — Build the positive profile as a weighting, not a gate

Good-fit traits should rank opportunities, not gate them. Express as a short weighted
list with the evidence that each trait is present. Resist the urge to make this
aspirational: it should describe clients you have actually served well, not the
clients you wish you had.

### Step 5 — Set the concentration rule

One rule that is not about a single client: the maximum share of revenue or capacity
any one client may hold before the next engagement with them requires a deliberate
decision. Cross-reference `services_client_concentration_risk_check.md`.

---

## Output Format

```markdown
## Ideal Client Profile — [practice]

### Good-fit weighting (ranks opportunities)
| Trait | Weight | Observable evidence | Seen in |
|---|---|---|---|

### Disqualifiers (gate opportunities)
| # | Family | Signal, as observed at first contact | Tier | Action |
|---|---|---|---|---|

### The ten-minute rule
Applied to any new inquiry, in order:
1. [first question that separates most of the field]
2. ...
**Decline if:** [the short list]

### Concentration limit
No single client above [N]% of [revenue / capacity]. Next engagement past that line
requires: [explicit decision, with who decides].

### Standard decline message
[reusable text — brief, non-apologetic, refers out where possible]
```

---

## Verification

- [ ] Every disqualifier is observable at or before the first call.
- [ ] At least three disqualifiers are drawn from real past engagements, not theory.
- [ ] Each rule has a tier; the list is not all "decline."
- [ ] The ten-minute rule is short enough to hold in your head during a live call.
- [ ] The decline message does not invent a false reason. Declining honestly and
      briefly preserves the referral; a fabricated scheduling excuse does not.

**False-positive prevention.** Two opposite failures.

*Over-tight:* a profile so restrictive it disqualifies clients you have served well.
Test it against your three best engagements — if the rules would have turned any of
them away, the rule that did it is wrong, and fixing it matters more than the rule's
theoretical appeal.

*Over-loose:* a disqualifier list containing only signals nobody would miss ("client
refuses to sign a contract"). Test against the three worst — if the rules would not
have caught them at first contact, the list is not yet doing its job. Keep iterating
until both tests pass.

Do not treat a single disqualifier as proof. These are base rates, not verdicts: they
tell you what to probe, and the probe result decides.

---

## Related

- `services_offer_definition_and_boundary.md` — the entry conditions these rules test against
- `services_client_concentration_risk_check.md` — the portfolio-level version of the concentration rule
- `services_capacity_and_utilization_planner.md` — why a thin pipeline pressures you to override this
- `../go-to-market/workflow_sales_discovery_call_preparation.md` — running the call once the lead passes
