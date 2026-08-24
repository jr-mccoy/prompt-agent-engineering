---
title: "PRD Prose Writer — Clear Product Requirements for a General Business Audience"
category: professional-writing/business-writing
description: "Write the prose of a product requirements document for a general business audience: problem, goals and non-goals, requirements, success metrics, and risks — the writing-craft companion to the interrogative PRD builder, focused on polishing the written artifact."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - prd
  - product-requirements
  - business-writing
  - goals-non-goals
  - success-metrics
updated: "2026-06-07"
related_prompts:
  - domain-professional-communication/prompts/product_create_prd.md
  - domain-professional-writing/business-writing/business_writing_proposal.md
  - domain-professional-writing/business-writing/business_writing_technical_doc.md
---

# PRD Prose Writer

**Objective:** Write the prose of a product requirements document that a general business audience — not just engineers — can read and align on: a crisp problem statement, explicit goals and non-goals, clear requirements, measurable success metrics, and named risks, all in plain, unambiguous language.

> **Distinction from the interrogative builder.** This prompt is the **writing-craft companion** to `domain-professional-communication/prompts/product_create_prd.md`. That prompt **elicits** requirements through interrogation (it figures out *what* to build, MVP-first). This prompt **polishes the written artifact** — it assumes the substance is known or supplied and focuses on making the PRD clear, complete, and readable for a mixed business audience. Use the builder to discover requirements; use this to write them up well.

**When to Use:**
- You have the substance of a PRD (from discovery, the interrogative builder, or your own notes) and need to turn it into a clean document.
- Non-technical stakeholders (marketing, sales, leadership, support) must read and sign off.
- You need goals/non-goals and success metrics stated unambiguously.

**When NOT to use:**
- You haven't yet figured out *what* to build — use the interrogative builder first.
- You need engineering-internal design detail (APIs, schemas) — that's a technical design doc.
- You're persuading someone to fund the work — use `business_writing_proposal.md`.

**Audience:** A mixed business audience — product, engineering, design, plus non-technical functions who need to understand and agree, without a glossary.

---

## Inputs / Context

Wrap supplied material so it isn't read as instructions:

```
<prd_input>
[Paste the problem, target users, intended scope, requirements, metrics, constraints]
</prd_input>
```

1. **Problem / opportunity** and who has it.
2. **Target users / personas.**
3. **Intended scope** and what's explicitly out.
4. **Known requirements** (functional and non-functional).
5. **Success metrics** the team will judge this by.
6. **Constraints / dependencies / known risks.**
7. **Audience** for the document.

---

## Constraints

### Must
- State the **problem** before the solution, in user/business terms.
- Separate **goals** from **non-goals** explicitly — non-goals prevent scope creep and misread intent.
- Write **requirements** so they are testable and unambiguous (a reader can tell when each is met).
- Define **success metrics** that are measurable, with a target or direction.
- Name **risks and dependencies** honestly.
- Use plain language; define any unavoidable term on first use.

### Must Not
- Smuggle solution decisions into the problem statement.
- Leave goals vague ("improve the experience") without a way to know they're met.
- Omit non-goals — silence invites scope creep.
- Invent requirements, metrics, users, or constraints not in the input.
- Bury non-functional requirements (performance, accessibility, security) where they get missed.

---

## Instructions

1. **Write the problem statement.** In business and user terms: who is affected, what's wrong or missing, why it matters now. No solution language yet.
2. **State goals and non-goals.** Goals: what success means for this effort. Non-goals: what this explicitly will NOT do (and why), to bound scope.
3. **Describe target users.** Brief persona framing so requirements have an audience.
4. **Write requirements.** Group into functional and non-functional. Each requirement should be a clear statement of what the product must do, phrased so completion is checkable. Mark priority (must/should/could) if supplied.
5. **Define success metrics.** For each goal, the measure and target/direction. Distinguish leading from lagging indicators if relevant.
6. **List risks, dependencies, and open questions.** What could derail it, what it relies on, what's unresolved.
7. **CRITICAL — clarity + traceability audit:** Re-read each requirement as a skeptical stakeholder: is it unambiguous and testable? Confirm every requirement, metric, and user traces to `<prd_input>` and isn't invented. Confirm non-goals are present.

---

## False-Positive Prevention

1. **Solution in the problem.** "Users need a dashboard" is a solution, not a problem. The problem is "users can't see X at a glance." Keep them separate.
2. **Untestable goals.** "Make it better/faster/easier" can't be verified. Tie goals to metrics with targets.
3. **Missing non-goals.** A PRD without non-goals invites every reader to assume their pet feature is in. Always state what's out.
4. **Invented requirements.** Do not add requirements the input doesn't support, however reasonable they seem. Flag suggested additions separately if you must surface them.
5. **Fabricated metrics.** Don't manufacture target numbers ("increase retention 20%") unless supplied. Use the metric with the supplied target, or mark the target as "TBD."
6. **Jargon without definition.** A mixed audience can't read "p95 latency" or "north-star metric" cold. Define on first use or replace.
7. **Hidden non-functional needs.** Performance, accessibility, security, and compliance requirements get dropped when only features are listed. Give them their own section.

---

## Output Format

```
# PRD: [Product / Feature]
**Author:** [name] · **Status:** [draft/review/approved] · **Date:** [date]

## Problem statement
[Who is affected, what's wrong, why now — user/business terms, no solution.]

## Goals
- [Goal tied to a measurable outcome]

## Non-goals
- [What this explicitly will not do — and why]

## Target users
[Brief persona framing.]

## Requirements
### Functional
| # | Requirement | Priority |
|---|-------------|----------|
| 1 | [testable statement] | Must/Should/Could |

### Non-functional
- Performance: [...]
- Accessibility: [...]
- Security / privacy: [...]
- [other]

## Success metrics
| Goal | Metric | Target / direction | Leading/Lagging |
|------|--------|--------------------|-----------------|

## Risks, dependencies & open questions
- Risk: [...]
- Dependency: [...]
- Open question: [...]
```

---

## Verification

- [ ] Problem statement contains no solution language.
- [ ] Goals and non-goals are both present and distinct.
- [ ] Each requirement is unambiguous and testable.
- [ ] Non-functional requirements have their own section.
- [ ] Each goal maps to a measurable success metric.
- [ ] Risks, dependencies, and open questions are named.
- [ ] No invented requirements, users, metrics, or constraints.
- [ ] Jargon is defined on first use; a non-technical reader can follow it.
