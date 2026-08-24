---
title: "Stakeholder Navigation Guide"
category: engineering-workflows/workflows
description: "Analyze a complex organizational or multi-party situation — distilling the issue, mapping agreed facts and disagreements, building a stakeholder matrix, generating three strategic options, and recommending a path with a 72-hour action plan."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-01
difficulty: intermediate
tags:
  - stakeholder-management
  - organizational-dynamics
  - decision-making
  - communication
  - strategy
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md
  - domain-engineering-workflows/workflows/engineering_24_hour_leader_pulse.md
  - domain-engineering-workflows/workflows/engineering_goal_system_designer.md
---

# Stakeholder Navigation Guide

**Objective:** Analyze a messy organizational or multi-party situation and identify the best path forward — distilling the core issue, separating agreed facts from disagreements, mapping each stakeholder's power and interests, generating three strategic options, and recommending one with a concrete 72-hour action plan and risk mitigations.

**When to use:**
- Navigating tricky organizational dynamics or a contested multi-party decision.
- Preparing to move a stalled cross-functional decision forward.
- Mapping stakeholders and influence before a high-stakes conversation.

**When NOT to use:**
- Tracking external industry leaders' statements — use `engineering_24_hour_leader_pulse.md`.
- Pure project scheduling — use `engineering_delivery_sprint_planner.md`.
- Personal goal design — use `engineering_goal_system_designer.md`.

**Audience:** Engineers, leads, and managers navigating organizational or stakeholder politics.

---

## Inputs / Context

The user supplies (wrap pasted material in a `<context>` tag):
1. **Situation context** — emails, meeting notes, background; be thorough.
2. **Your role** — position, authority level, reporting structure.
3. **Decision deadline** — date and why.
4. **Desired outcome** — what success looks like.
5. **Constraints** — what you cannot do or change.

If the context lacks a stakeholder's actual position, infer cautiously and label inferences as assumptions, not facts.

---

## Constraints

### Must
- Distill the situation to a core issue, key tensions, and urgency.
- Separate facts everyone agrees on from explicit points of disagreement (with sides).
- Build a stakeholder matrix: power, current position, underlying interests, levers, relationship, pressure points, best approach.
- Present exactly three strategic options with actions, timeline, pros, cons, and second-order effects.
- Recommend one path with a 72-hour action plan and risk mitigations.

### Must Not
- State a stakeholder's private motivations as fact — label inferences as assumptions.
- Recommend actions that violate the user's stated constraints.
- Assign success probabilities as if precise — present them as rough judgments with reasoning.
- Invent emails, quotes, or events not in the provided context.

---

## Instructions

1. **Distill the situation.** Core issue (2–3 sentences), 3–5 key tension points, urgency level.
2. **Map the landscape.** List undisputed facts and their implications; list points of disagreement with who believes what.
3. **Build the stakeholder matrix.** For each key person: power (H/M/L), position, underlying interests, influence levers, relationship to you, pressure points, best approach.
4. **Develop three options.** For each: 5 concrete actions, timeline, 3 pros, 3 cons, a rough success likelihood (with reasoning), and second-order effects.
5. **Recommend a path.** Choose one (or a hybrid) with rationale; give a first-72-hours action plan and if-X-then-Y risk mitigations.
6. **Self-check before reporting.** Confirm inferences are labeled, constraints respected, and nothing fabricated from outside the context.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't assert a stakeholder's hidden motive as fact — mark it an assumption to verify.
- Don't propose moves that break the user's stated constraints.
- Don't present success probabilities as precise numbers; they're judgments.
- Don't invent emails, statements, or events beyond the provided context.

✅ **DO:**
- Distinguish agreed facts from inferences and disagreements.
- Tie every recommendation to interests and levers you can evidence.
- Keep options within the user's authority and constraints.
- Make the 72-hour plan concrete and reversible where possible.

---

## Output Format

```markdown
## Situation Distillation
- Core issue / key tensions / urgency

## Landscape Analysis
- Agreed facts (+ implications)
- Points of disagreement (sides)

## Stakeholder Matrix
### [Name — Title]
- Power · Position · Underlying interests · Levers · Relationship · Pressure points · Best approach

## Three Strategic Options
### Option N: [name]
- Actions / timeline / pros / cons / rough likelihood (reasoning) / second-order effects

## Recommended Path
- Choice + rationale

## First 72 Hours
1. [Hour 1–4] … 2. [Day 1] … 3. [Day 2] … 4. [Day 3 checkpoint]

## Risk Mitigations
- If X → then Y; backup plan; exit strategy
```

## Example Output

```markdown
## Situation Distillation
- Core issue: Two teams disagree on owning the new billing service before a board demo in 9 days.
- Key tensions: ownership, on-call burden, demo risk. Urgency: high.

## Landscape Analysis
- Agreed facts: demo is committed; service must be stable for it.
- Disagreement: Platform wants ownership long-term; Payments wants it only through demo.

## Stakeholder Matrix
### Dir. of Platform — High power
- Position: take ownership now. Interests: headcount justification. Lever: reliability story. Relationship: neutral. Pressure point: fears being blamed for instability. Best approach: frame a phased handoff that de-risks the demo.

## Three Strategic Options
### Option 1: Phased handoff (collaborative)
- Actions: demo owned by Payments; written handoff plan; joint on-call for 2 weeks; ...
- Pros: de-risks demo, builds trust. Cons: slower clarity. Likelihood: ~moderate-high (both interests partly met). Second-order: sets a precedent for future handoffs.

## Recommended Path
- Option 1 — meets the demo deadline while resolving ownership after, within your authority to broker.

## First 72 Hours
1. Hour 1–4: 1:1 with each director to confirm interests.
2. Day 1: draft phased-handoff proposal.
3. Day 2: joint 30-min alignment.
4. Day 3: circulate agreed plan; confirm demo owner.

## Risk Mitigations
- If Platform refuses phased plan → escalate to shared VP with the demo-risk framing; backup: Payments owns through demo with a dated handoff commitment.
```

---

## Verification

- [ ] Situation distilled to core issue, tensions, urgency.
- [ ] Agreed facts separated from disagreements and from inferences.
- [ ] Stakeholder matrix covers power, interests, levers, and approach per person.
- [ ] Exactly three options with actions, pros/cons, likelihood (reasoned), second-order effects.
- [ ] Recommendation respects stated constraints; 72-hour plan + risk mitigations included.
- [ ] Inferences labeled; nothing fabricated beyond the provided context.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the analyze-and-recommend-a-path goal.
- **ST-02 (Structured Sequential Instructions):** Distill → landscape → matrix → options → recommend.
- **RT-02 (Multi-Dimensional Analysis):** Evaluates power, interests, levers, and second-order effects.
- **DS-06 (Prioritization and Severity Guidance):** Ranks options and sequences the 72-hour plan.
- **CM-01 (Explicit Context Framing):** Role, authority, deadline, and constraints frame every option.

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md` — Execute the chosen path as a delivery plan.
- `domain-engineering-workflows/workflows/engineering_24_hour_leader_pulse.md` — External landscape intelligence.
- `domain-engineering-workflows/workflows/engineering_goal_system_designer.md` — Turn outcomes into tracked goals.
