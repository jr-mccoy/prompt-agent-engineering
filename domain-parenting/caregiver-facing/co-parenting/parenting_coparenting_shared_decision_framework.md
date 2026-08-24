---
title: "Shared Decision Framework for Co-Parents"
category: parenting/co-parenting
description: "Build a framework for making joint co-parenting decisions — medical, school, activities, religion, big purchases — and for resolving disagreements: what needs joint sign-off vs. day-to-day discretion, how to propose and decide, and what to do at impasse (mediation before court). Organizes the parents' own choices; not legal advice."
techniques:
  - DS-01
  - ST-02
  - ST-03
  - CM-01
  - QA-02
difficulty: intermediate
intended_use: model-testing
tags:
  - parenting
  - co-parenting
  - cross-age
  - decision-making
  - mediation
updated: "2026-06-01"
related_prompts:
  - domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_message_composer_biff.md
  - domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_consistency_across_homes.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_parenting_plan_builder.md
  - domain-parenting/caregiver-facing/co-parenting/parenting_coparenting_information_handoff_brief.md
---

**Purpose:** Help two parents set up a clear, repeatable way to make the decisions that affect their children together — sorting what genuinely requires joint sign-off from what each parent can decide on their own time, defining a simple propose-and-decide process, and naming what happens when they hit an impasse (mediation before court, not court first). The output is a decision map and a process, written neutrally and centered on the child.

**When to use:** Recurring fights about who gets to decide what; a specific upcoming decision (school choice, a procedure, a sport, religious instruction, a big purchase) you need a process for; you want to reduce friction by agreeing in advance which decisions are "joint" and which are "yours during your time"; you're building or revising a parenting plan and need the decision-making section.

**When NOT to use:** You need to know what your custody order actually says about decision authority, or whether a decision is legally yours to make → that is legal advice; check your order with an attorney/mediator. There's a safety emergency or the disagreement is really about an unsafe situation (see Safety Block).

---

## Safety Block

Stop and use a different pathway if:
- A decision involves a child's immediate safety or a medical emergency → act to protect the child first; in a true emergency either parent should act and notify the other; emergencies 911.
- The "disagreement" includes threats, coercion, or one parent using decisions to control the other → National Domestic Violence Hotline 1-800-799-7233 (US); consult an advocate. A framework cannot fix coercive control.
- A child is being harmed or denied needed care by a decision → Childhelp National Child Abuse Hotline 1-800-422-4453; emergencies 911; document and route to counsel.
- A child is in mental-health crisis and the parents are stuck on whether to get help → 988 Suicide & Crisis Lifeline (US); get the child seen; do not let a decision standoff delay care.

This framework organizes how reasonable parents decide together. It is not a substitute for your custody order, an attorney, or emergency action.

---

## Core Principles

1. **Separate "joint" from "day-to-day" up front.** Most friction comes from not knowing which is which. A few decisions truly need both parents; most don't. Agreeing on the line in advance prevents fights in the moment.
2. **Decide the process, not just the outcome.** You can't pre-agree every future decision, but you can agree *how* you'll decide — who proposes, how much notice, how you signal yes/no, what happens if you disagree.
3. **The standard is the child's best interest, not the parents' even split.** Decisions aren't about fairness between parents or keeping score; they're about what serves the child.
4. **Propose early, decide on a timeline.** Last-minute decisions create conflict. Build in notice periods so neither parent feels ambushed.
5. **Impasse has a path: mediation before court.** Disagreement is normal; it doesn't mean litigation. Name a graduated path so a stuck decision doesn't default to a lawsuit.
6. **Emergencies override the process.** Either parent can act to protect the child in a genuine emergency and must promptly inform the other.

---

## Your Input

- **Children:** [ages; any special medical/educational needs]
- **Decision categories that matter for you:** [medical / education / activities / religion / big purchases / travel / tech]
- **What you currently fight about deciding:** [be specific]
- **A specific decision on the table now (if any):**
- **What your order/plan says about decisions (if known):** [describe; don't assume legal effect]
- **Conflict level / ability to discuss:** [low / moderate / high]
- **Preferred channel for proposing decisions:** [app / email]

---

## Constraints

**Must:**
- Map each decision category as **joint sign-off**, **notify-only**, or **day-to-day discretion**.
- Define a propose-and-decide process with notice periods and a yes/no signal.
- Include an impasse path that ends at mediation/parenting coordinator before court.
- Include an emergency clause (act + notify).
- Center every decision on the child's interest, not parental fairness.

**Must Not:**
- Badmouth or characterize the other parent to or near the kids.
- Use the child as a messenger, tiebreaker, or decision-maker about adult matters.
- Coach the parent to seize authority, outmaneuver, or disadvantage the other parent.
- Assert what a court will rule or that a term is "enforceable" — flag legal questions for counsel.
- Diagnose or label the other parent.

---

## Instructions

### Stage 1 — Confirm Scope
Restate which decision categories the parent wants to map, flag anything that's a legal question about authority (route to counsel/their order), and confirm whether the other parent is available to agree to a process.

### Stage 2 — Map the Decision Categories
For each category, propose a default tier:
- **Joint sign-off:** non-emergency medical procedures, school choice/major changes, religious instruction, activities with big time/money/travel commitments, big purchases affecting both homes.
- **Notify-only:** routine appointments, minor activities, day-trips — one parent decides, informs the other.
- **Day-to-day discretion:** food, bedtime, screen time, clothing, friends over — whoever has the child decides.
Adjust based on the parents' order and reality.

### Stage 3 — Design the Propose-and-Decide Process
Specify: who can raise a decision, how it's proposed (channel + what info to include), the notice period by decision size, how the other parent signals agreement or objection, and a default timeline for a response (silence ≠ consent for joint items).

### Stage 4 — Build the Impasse Path
Define the graduated steps: direct discussion → written proposal with options → neutral input (pediatrician/teacher for fact questions) → mediation or parenting coordinator → court as last resort. *Whether your order requires a specific dispute process — confirm with counsel.*

### Stage 5 — Emergency Clause
State plainly: in a genuine emergency, either parent acts to protect the child and notifies the other as soon as possible. This overrides the process.

### Stage 6 — Draft the Proposal Message (if needed)
If there's a live decision, draft the neutral, child-first proposal the parent can send (route phrasing to `parenting_coparenting_message_composer_biff.md`).

---

## Output Format

```markdown
# Shared Decision Framework — [Children's initials]

## Decision map
| Category | Tier | Notes |
|---|---|---|
| Non-emergency medical | Joint sign-off | |
| School choice / major changes | Joint sign-off | |
| Religion / instruction | Joint sign-off | *confirm with counsel if disputed* |
| Big activities / big purchases | Joint sign-off | |
| Routine appointments / minor activities | Notify-only | |
| Food / bedtime / screens / clothes | Day-to-day | whoever has the child |

## Propose-and-decide process
- Who can raise: [both]
- How / channel: [app/email, include: what, why, options, cost/time]
- Notice periods: [big = X weeks; routine = Y days]
- Signaling yes/no: [explicit confirmation; silence ≠ consent for joint items]
- Response timeline: [by when]

## Impasse path
direct → written options → neutral fact input → mediation/coordinator → court (last resort)
*Confirm any required process with counsel.*

## Emergency clause
Either parent may act to protect the child in a true emergency and must notify the other promptly.

## Live decision (if any)
[Neutral, child-first proposal message — route phrasing to BIFF composer.]
```

---

## Verification

- [ ] Every category mapped to joint / notify-only / day-to-day?
- [ ] Propose-and-decide process has notice periods and a yes/no signal?
- [ ] Impasse path ends at mediation/coordinator before court?
- [ ] Emergency clause present (act + notify)?
- [ ] Decisions framed around the child's interest, not parental fairness?
- [ ] Legal-authority questions flagged for counsel, not guessed?
- [ ] Child never used as tiebreaker or messenger?
- [ ] No coaching to seize authority or disadvantage the other parent?
- [ ] No diagnosis or label of the other parent?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Fight every small choice as if it's "joint" | Sort joint vs. day-to-day in advance |
| Spring big decisions at the last minute | Use agreed notice periods |
| Treat the other parent's silence as a yes | Require explicit confirmation for joint items |
| Make the child the tiebreaker | Adults decide; the child isn't a vote |
| Jump straight to court at impasse | Step through mediation/coordinator first |
| Score decisions for "fairness" between parents | Decide on the child's best interest |
| Claim a decision is "legally mine" without checking | Flag authority questions for counsel |
| Send the child to deliver the proposal | Propose adult-to-adult on the agreed channel |
| Use a decision to control the other parent | Keep the process about the child, not power |
| Label them "controlling" or "unfit" | Describe the decision, not their character |

---

## Adaptations

**By age band:**
- **0–3:** Most decisions are medical/routine and joint; emphasize the notify-and-notice discipline so neither parent is blindsided about appointments or milestones.
- **4–8:** School entry, activities, and early medical decisions cluster here; build the school-decision process carefully.
- **9–12:** Activities and tech decisions grow; the child can offer input on activities (not on adult matters); name how that input is weighed.
- **13–18:** Teens reasonably weigh in on their own activities, medical choices appropriate to their maturity, and religion; build a process for incorporating their voice without making them the decider, and note that some health decisions shift legally with age. *Confirm with counsel.*

**By profile:**
- **High-conflict co-parent:** Maximize the day-to-day tier (less to coordinate); make joint decisions strictly written with options and deadlines; default impasse to a parenting coordinator/mediator; pair with `parenting_coparenting_high_conflict_response_strategy.md`.
- **Child with ADHD/autism:** Medical, therapy, and educational (IEP/504) decisions are frequent and high-stakes — build a tight joint process and clean information handoff for these.
- **Anxious child:** Decide adult disagreements away from the child; present decisions to the child as settled, not contested.
- **Unsafe/absent-parent context:** Joint decision-making may be limited or inappropriate; see Safety Block and `parenting_coparenting_with_unsafe_or_absent_parent.md`; check your order with counsel.

---

## Cross-References

- `parenting_coparenting_message_composer_biff.md` — phrase the actual decision proposals neutrally.
- `parenting_coparenting_consistency_across_homes.md` — for day-to-day rules rather than big decisions.
- `parenting_custody_parenting_plan_builder.md` — embed this decision map into a full parenting plan.
- `parenting_coparenting_information_handoff_brief.md` — share the facts a joint decision needs.
- `parenting_coparenting_high_conflict_response_strategy.md` — when decisions repeatedly hit impasse.
