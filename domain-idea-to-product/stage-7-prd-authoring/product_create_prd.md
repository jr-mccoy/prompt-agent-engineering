---
title: "Create a PRD via Interrogation (MVP-First)"
category: professional-communication/product
description: "Interrogative PRD builder that gathers requirements through disciplined questioning, pushes back on scope, and produces an MVP-centric Product Requirements Document with explicit out-of-scope calls."
techniques:
  - ST-01
  - ST-02
  - RT-01
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - product-management
  - prd
  - requirements
  - mvp
  - scope-control
  - stakeholder-alignment
updated: "2026-04-23"
related_prompts:
  - domain-professional-communication/prompts/product_rigorous_prd_evaluation_and_scoring.md
  - domain-professional-communication/prompts/product_delivery_sprint_planner.md
  - domain-professional-communication/prompts/product_market_size_calculator.md
  - domain-professional-communication/templates/prd_template.md
---

# Create a PRD via Interrogation (MVP-First)

**Objective:** Produce a Product Requirements Document for a proposed feature or product by first interrogating the requester — surfacing the problem, target user, success criteria, and real constraints — before writing a single requirement. Default to the smallest MVP that can prove the hypothesis; push back on scope creep by name.

**When to use:**
- A stakeholder has pitched a feature in one sentence ("we should let users X") and you need a real PRD.
- A document called a "PRD" is circulating but reads as a solution spec with no problem statement.
- You are the product owner and need to pressure-test your own idea before asking engineering to estimate.
- A prior PRD was built, engineering shipped it, and no one can agree on whether it worked.

**Do not use this prompt** to write marketing copy, launch plans, or go-to-market strategy. Those are downstream of a completed PRD.

**Audience:** Product managers, founders, or technical leads who own the requirements surface for a feature. Assumes the reader can name a real user segment and has at least a rough hypothesis about the value.

---

## Inputs / Context

Ask the requester the following **before** drafting any PRD sections. If the requester cannot answer a given question, record the gap explicitly — do not invent an answer.

1. **One-sentence feature pitch.** What is being built, in the requester's words.
2. **Problem statement.** What user pain or business problem this is supposed to solve. If the answer is "users want it" or "competitor X has it," that is a red flag — ask again.
3. **Target user segment.** Who specifically. A role, a tier, a persona — not "our users."
4. **Current behavior.** What the user does today to get the same outcome. If the answer is "nothing," that is a strong signal the problem may not exist.
5. **Success criteria.** One or two measurable outcomes (a metric moved, a behavior adopted, a cost reduced). If the requester offers only qualitative ("it'll feel better"), push for a measurable leading indicator.
6. **Constraints.** Deadline, headcount, platform limitations, legal/compliance surfaces, dependencies on other teams.
7. **What's been tried.** Prior attempts, abandoned experiments, or adjacent features that failed.
8. **Decision record.** Who is the single accountable decision-maker for this PRD? Who must sign off before engineering starts?

If the requester has answered fewer than 5 of the 8, **stop** and return the gaps. Do not proceed to draft.

---

## Constraints

### Must
- Interrogate before drafting. The first output is a numbered question set covering any gap in the 8 inputs above.
- Put the **problem statement** before the solution. If the problem reduces to "we want to build X," name that and ask what user outcome X serves.
- Propose the **smallest MVP** that can test the core hypothesis, and explicitly list what is **not** in the MVP.
- Name the single hypothesis being tested in one sentence ("If we ship X, then Y user segment will do Z, measured by W").
- Every requirement must be testable. "Fast" is not a requirement; "response returns within 400ms on p95" is.
- Attach an **out-of-scope** section. Features that were discussed and cut belong here, so reviewers can see the scope decisions explicitly.
- Include a **we won't ship this if** section: the real failure conditions that would cause the team to pull the feature.

### Must Not
- Invent answers for fields the requester did not provide. Mark them `[GAP — needs answer from {role}]`.
- List "nice-to-have" requirements in the MVP section. If it is nice-to-have, it is v2.
- Use the phrase "users want" without naming which user segment and what they do today instead.
- Write implementation details (API shapes, database schemas, UI layout) unless the requester explicitly asked for a technical PRD. Default to a user-facing PRD.
- Assume a launch date. A PRD ends at "ready for engineering sizing," not at a ship plan.
- Skip the interrogation even if the requester insists they "already thought about it." If they have, the answers will be fast.

---

## Instructions

### Step 1 — Interrogation pass

Before drafting, review the 8 inputs above. For every gap, generate a specific question targeted at the role most likely to know the answer. Format:

```
Gaps to close before drafting:
1. [Input #] — [Question]. Best asked of: [role].
2. ...
```

If fewer than 5 inputs are answered, return this list and stop. Do not draft a PRD on speculation.

### Step 2 — Hypothesis statement

Reduce the feature to a single testable hypothesis in this form:

> If we ship **[feature/change]** for **[specific user segment]**, then they will **[observable behavior change]**, measured by **[metric with threshold]** within **[timeframe]**.

If you cannot write this sentence cleanly, the PRD is not ready. Name the piece that is missing and stop.

### Step 3 — MVP scope decision

List every capability discussed. For each, decide:
- **In MVP** — required to test the hypothesis.
- **v2** — worth doing later; does not block the test.
- **Out of scope** — discussed and rejected; name the reason.

Err toward fewer in-MVP items. If the MVP has more than five in-MVP items, ask whether the hypothesis is actually multiple hypotheses stacked.

### Step 4 — Draft the PRD

Write the full document using the Output Format below. Every requirement must be testable. Every assumption must be tagged.

### Step 5 — Self-audit

Before returning the PRD, walk the Verification checklist at the bottom. Mark any `[GAP]` tags inline so the reader sees them without hunting.

---

## False-Positive Prevention

1. **Don't accept "users want this" as a problem statement.** Ask what the user does today. If the answer is "nothing" or "a manual workaround we invented," the problem is a hypothesis, not a fact.
2. **Don't let scope inflate during drafting.** Once the MVP list is set, new capabilities that surface go to v2 or out-of-scope, not the MVP section.
3. **Don't convert vague outcomes into specific-looking requirements.** "Make onboarding smoother" is not a requirement. "Reduce step 3 drop-off from 40% to under 25%" is.
4. **Don't hide assumptions inside prose.** Every assumption ("users have Slack installed," "admin role is already defined") goes in the Assumptions section with a risk note.
5. **Don't skip the out-of-scope section because "everyone knows."** Sign-off gets cleaner when the cuts are written down.
6. **Don't assume stakeholder alignment because no one objected in the meeting.** If you did not hear a stakeholder say "yes, ship this," mark them as unconfirmed.

---

## Output Format

```
# PRD: [Feature Name]

**Status:** Draft / Review / Approved
**Author:** [Name]
**Decision-maker:** [Name + role]
**Last updated:** [Date]

## 1. Problem
- Who has the problem: [specific user segment]
- What they do today: [current behavior]
- Why it's worth solving now: [business/user rationale]

## 2. Hypothesis
If we ship [X] for [segment], then [behavior] will change, measured by [metric with threshold] within [timeframe].

## 3. Success criteria
- Primary metric: [metric, baseline, target, how measured]
- Secondary / leading indicators: [metric, threshold]
- Guardrail metrics: [metrics that must not regress]

## 4. MVP scope (in)
- [Requirement] — testable by [method]
- [Requirement] — testable by [method]
- (target: ≤ 5 items)

## 5. v2 (out of MVP, planned)
- [Item] — reason deferred: [reason]

## 6. Out of scope (rejected)
- [Item] — reason: [reason]

## 7. Assumptions
- [Assumption] — risk if wrong: [impact]

## 8. Dependencies
- [Team / system / data source] — owner: [name] — confirmed: [Y/N]

## 9. We won't ship this if
- [Failure condition 1]
- [Failure condition 2]

## 10. Open questions / gaps
- [GAP] [Question] — waiting on: [role]

## 11. Stakeholder sign-off
| Role | Name | Status (unconfirmed / approved / blocked) |
|------|------|-------------------------------------------|
```

If any section is a `[GAP]`, keep it in the output with the tag visible. Do not silently omit.

---

## Verification

Run this list before returning the PRD:

- [ ] Problem statement names a specific user segment and their current behavior (not "users want").
- [ ] Hypothesis fits the If / Then / Measured by / Within structure.
- [ ] MVP has no more than five requirements, each testable.
- [ ] Out-of-scope section exists and is non-empty (if everything is in scope, scope was not considered).
- [ ] Every assumption has a risk-if-wrong note.
- [ ] No implementation details unless explicitly requested.
- [ ] Every `[GAP]` is labeled with who needs to answer it.
- [ ] "We won't ship this if" has at least two concrete failure conditions.
- [ ] Sign-off table names every stakeholder whose blessing is required; unconfirmed ones are marked unconfirmed.

If any box is unchecked, the PRD is not ready for engineering sizing. Return with the gaps explicit.
