---
title: "Lightweight Health-Check of a Personal Relationship"
category: personal-development/relationships
description: "A quick, low-stakes health-check on a single personal relationship — what's working, what's draining, the give/take balance, and one small move to strengthen it. Designed for maintenance and early-signal catching, not for deciding whether to stay or leave (that's the decision-grade audit it cross-links to)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-20
difficulty: beginner
tags:
  - relationships
  - audit
  - health-check
  - maintenance
  - reflection
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/major-decisions/personal_difficult_relationship_audit.md
  - domain-personal-development/prompts/relationships/relationships_conflict_repair_guide.md
  - domain-personal-development/prompts/relationships/relationships_boundary_setting_script.md
  - domain-personal-development/prompts/relationships/relationships_network_cultivation_plan.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
---

# Lightweight Health-Check of a Personal Relationship

**Objective:** Give the user a fast, honest snapshot of one personal relationship — what's nourishing, what's draining, whether the give/take feels balanced, and one small strengthening move — without the heavy machinery of an exit/stay decision. It's a maintenance and early-warning tool, deliberately lighter than the decision-grade audit it points to.

## When to Use

- Use when: a relationship feels slightly off and you want to name why before it drifts further.
- Use when: you periodically want to check the health of an important relationship (a periodic relationship review).
- Use when: something nagging is hard to articulate and you want a quick structured read.
- Don't use when: you're seriously weighing whether to end, escalate, or significantly distance the relationship — that needs the decision-grade [personal_difficult_relationship_audit.md](../../major-decisions/personal_difficult_relationship_audit.md).
- Don't use when: there's an active rupture to repair — use [relationships_conflict_repair_guide.md](relationships_conflict_repair_guide.md).
- Don't use when: there's any safety concern — that is out of scope (see boundary note).

## Inputs / Context

Gather these. If 1–2 are missing, ask.

1. **The relationship.** Role (not name), how long, how close.
2. **What prompted the check.** A nagging feeling, a routine review, a recent moment.
3. **A few recent interactions** — concrete, good and bad — to ground the read. Optional but improves accuracy.

**Refusal logic:** If the inputs reveal abuse, fear, coercion, or danger, stop the health-check. A "what's working / what's draining" frame is inappropriate for an unsafe relationship and can normalize harm. Name that plainly and route to professional support. Also escalate up — not down — to the decision-grade audit if the user is actually contemplating leaving; a lightweight tool shouldn't carry a heavy decision.

## Instructions

### Step 1 — Snapshot what's working

List 2–4 concrete things that are genuinely good in this relationship right now — specific, recent, observable. Resist generic positives ("they're nice"); anchor to moments.

### Step 2 — Snapshot what's draining

List 2–4 specific things that drain or frustrate — again behaviors and moments, not character labels. Note for each whether it's a recent change or a long-standing pattern.

### Step 3 — Read the give/take balance

Quick gauge of reciprocity over the last while: who initiates, who supports whom, whether effort feels roughly mutual or lopsided. Reciprocity ebbs and flows (one person may be going through something) — distinguish a temporary tilt from a chronic imbalance.

### Step 4 — Score the overall read

Offer a simple read on a small scale — e.g., **Thriving / Solid / Needs attention / Strained** — with one sentence of justification grounded in steps 1–3. This is a temperature reading, not a verdict.

### Step 5 — One small strengthening move

Propose a single, low-effort, specific action to nudge the relationship in a better direction (DS-06): a gesture, a small conversation, a boundary, or a repair. Pick the highest-leverage small move, not a list.

### Step 6 — Escalation flag

If the audit surfaced something heavier than a maintenance issue — a recurring boundary problem, an unresolved rupture, or genuine doubt about continuing — name it and route to the right deeper tool rather than trying to resolve it here.

## Constraints

### Must
- Ground both "working" and "draining" lists in specific, recent behaviors.
- Distinguish temporary tilt from chronic imbalance in the give/take read.
- Give one simple overall read with a one-line justification.
- Offer exactly one small, specific strengthening move.
- Flag and route anything heavier than a maintenance issue.

### Must Not
- Render a stay/leave verdict — route to the decision-grade audit instead.
- Run a health-check on an unsafe relationship — refuse and refer.
- Accept character labels as the substance of the read.
- Pile on multiple action items; one small move only.
- Pathologize normal ebb and flow as a problem.

## False-Positive Prevention

1. **Heavy decision in a light tool.** If the user is really asking "should I leave?", this prompt under-serves it. Escalate to the decision-grade audit.
2. **Label-as-finding.** "They're toxic / amazing" carries no information. Push for the specific moments behind it.
3. **Snapshot mistaken for trend.** A single bad week isn't a strained relationship; a single great day isn't thriving. Note duration.
4. **Mood contamination.** If the user is currently angry, hurt, or infatuated, flag that the read is colored by state and may shift.
5. **Reciprocity rigidity.** Perfectly even give/take isn't the standard; supporting someone through a hard stretch is reciprocity over time, not imbalance.
6. **Safety normalization.** Re-screen for fear/coercion; the working/draining frame must never be applied to an abusive dynamic.

## Expected Output

A compact health-check: what's working, what's draining, the balance read, an overall temperature, one small move, and any escalation flag.

### Output Format

```
## Health-check — [relationship type]

### What's working (specific)
- [...]
- [...]

### What's draining (specific)
- [...] (recent change / long-standing)
- [...]

### Give/take balance
[brief read; temporary tilt vs. chronic imbalance]

### Overall read
[Thriving / Solid / Needs attention / Strained] — [one-line justification]
(Reading may be colored by your current mood: [yes/no])

### One small move
[single, specific, low-effort action]

### Escalation flag
[none, or: this looks heavier than maintenance → route to <tool>]
```

## Example Output

```
## Health-check — close friend (10+ years)

### What's working (specific)
- She remembered my interview last week and texted to check how it went.
- Our monthly calls still go two hours and feel easy.

### What's draining (specific)
- Last three times we made plans, she canceled day-of (recent change — started ~2 months ago).
- I notice I'm the one initiating lately (long-standing, but more pronounced now).

### Give/take balance
Currently tilted toward me initiating, but she's just started a demanding job — likely a temporary tilt rather than a chronic imbalance. Worth watching, not alarming.

### Overall read
Solid — the core connection is strong; the cancellations are a recent friction, probably situational. (Reading colored by current mood: no.)

### One small move
Next time, instead of another open-ended plan, send: "I miss you — want to do a short call this week since things are nuts for you?" — lower the bar so it's easier for her to say yes.

### Escalation flag
None — this is maintenance. If cancellations persist for several more months with no acknowledgment, revisit with the boundary or repair prompt.
```

## Verification

- [ ] "Working" and "draining" lists are grounded in specific, recent behaviors, not labels.
- [ ] The give/take read distinguishes a temporary tilt from a chronic imbalance.
- [ ] A single overall read is given with a one-line justification.
- [ ] Exactly one small, specific strengthening move is offered.
- [ ] Current mood's influence on the read is noted.
- [ ] Anything heavier than maintenance is flagged and routed to the right deeper tool.
- [ ] Inputs re-screened for safety; an unsafe dynamic would have triggered a refusal/referral.

## Techniques Used

- **ST-01 (Clear Objective Statement):** Keeps this a fast temperature read, explicitly not a stay/leave decision.
- **ST-02 (Structured Sequential Instructions):** Working → draining → balance → read → move → escalate, in order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Reads the relationship across positives, drains, and reciprocity.
- **DS-06 (Prioritization and Severity Guidance):** Selects the single highest-leverage small move and flags escalation.
- **CM-02 (Constraint Specification):** Holds the line between a light health-check and a heavy decision tool.
- **QA-20 (Dual-Failure Quality Test):** Guards both false alarm (normal ebb read as crisis) and false calm (real problem dismissed).

## Related Prompts

- [personal_difficult_relationship_audit.md](../../major-decisions/personal_difficult_relationship_audit.md) — The decision-grade version, for stay/leave/escalate decisions.
- [relationships_conflict_repair_guide.md](relationships_conflict_repair_guide.md) — When the check surfaces an unresolved rupture.
- [relationships_boundary_setting_script.md](relationships_boundary_setting_script.md) — When the drain is a recurring behavior needing a limit.
- [relationships_network_cultivation_plan.md](relationships_network_cultivation_plan.md) — When several relationships need attention, not just one.
- [identity_values_clarification.md](../identity/identity_values_clarification.md) — If the check raises whether this relationship fits what you value.
