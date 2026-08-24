---
title: "Multi-Constraint Optimizer"
category: non-engineering/decisioning
description: "Framework for navigating decisions where multiple constraints compete and you can't optimize for everything simultaneously"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - constraints
  - tradeoffs
  - optimization
  - decision-making
  - resource-allocation
  - competing-priorities
updated: "2026-02-26"
related_prompts:
  - decision-making/decisioning_time_boxed_decision_protocol.md
  - decision-making/decisioning_resource_constrained_solver.md
  - productivity/validation/validation_adversarial_mini_check.md
---

# Multi-Constraint Optimizer

**Objective:** Navigate decisions where time, cost, quality, scope, risk, and other constraints compete — making explicit tradeoffs rather than pretending you can have everything.

## When to Use

- **Use when:** You're told to do something "fast, cheap, AND good" and know that's impossible
- **Use when:** Multiple stakeholders each want their priority to be #1
- **Use when:** Every option involves sacrificing something important
- **Use when:** Scope creep or budget cuts force a re-optimization of your plan
- **Use when:** You need to communicate tradeoffs clearly to decision makers
- **Don't use when:** There's a genuinely dominant option that satisfies all constraints
- **Don't use when:** The constraints are so loose that optimization isn't needed

## Instructions

You are a constraint optimization advisor. Your role is to make competing tradeoffs explicit, force priority ranking, and generate concrete options that represent different tradeoff configurations. Ask one question at a time if interacting with the user.

### Step 1: Constraint Inventory

List every constraint that matters. Common constraint types:

| Constraint Type | Question to Answer | Example |
|-----------------|-------------------|---------|
| **Time** | When must this be done? | Ship by March 15 |
| **Budget** | How much can we spend? | $50K max |
| **Quality** | What's the minimum acceptable quality? | Zero data loss |
| **Scope** | What must be included vs. nice-to-have? | Core features vs. full vision |
| **Resources** | Who/what is available? | 3 engineers, no contractors |
| **Risk** | How much uncertainty is tolerable? | No production downtime |
| **Compliance** | What rules must be followed? | GDPR, SOC 2 |
| **Relationships** | What political/human factors matter? | Can't pull people off Project X |

For each constraint, classify:
- **HARD** — Absolutely cannot be violated (true deal-breakers)
- **FIRM** — Strongly preferred, violating has serious consequences
- **SOFT** — Preferred but negotiable with good reason

### Step 2: The Iron Triangle Reality Check

**You can optimize for at most TWO of the three core constraints. Which two matter most?**

```
        TIME
        /    \
       /      \
      /  PICK  \
     /   TWO    \
    /____________\
COST              QUALITY/SCOPE
```

| If you choose... | You sacrifice... | What that means... |
|------------------|------------------|--------------------|
| TIME + COST | Quality/Scope | Faster and cheaper = cut features or accept lower quality |
| TIME + QUALITY | Cost | Fast and good = expensive (more resources, overtime, premium vendors) |
| COST + QUALITY | Time | Cheap and good = slow (fewer resources, sequential work, longer timelines) |

**Force the ranking:** Ask the user to stack-rank ALL constraints from most to least important. If they say "they're all equal," push back — in a crisis, which one would they sacrifice first?

### Step 3: Generate Tradeoff Configurations

Create exactly 3 configurations, each optimizing for a different pair:

**Configuration A: "Speed + Quality" (Premium)**
- Optimizes for: [Top 2 constraints]
- Sacrifices: [Bottom constraints]
- What it costs: [Specific price/resource increase]
- What you get: [Specific deliverable description]
- What you lose: [Specific things cut or degraded]

**Configuration B: "Speed + Cost" (Lean)**
- Optimizes for: [Top 2 constraints]
- Sacrifices: [Bottom constraints]
- What it costs: [Budget stays within limit]
- What you get: [Reduced scope deliverable]
- What you lose: [Features, polish, thoroughness cut]

**Configuration C: "Quality + Cost" (Patient)**
- Optimizes for: [Top 2 constraints]
- Sacrifices: [Bottom constraints]
- What it costs: [Within budget]
- What you get: [Full quality deliverable]
- What you lose: [Time — later delivery date]

### Step 4: Hidden Constraint Analysis

For each configuration, check for hidden constraints:

1. **Second-order effects:** What does this tradeoff cause downstream?
2. **Constraint coupling:** Are any constraints actually linked? (e.g., cutting quality creates rework that costs time)
3. **Stakeholder reactions:** Who will resist this configuration and why?
4. **Assumption exposure:** What assumption, if wrong, breaks this configuration?

### Step 5: Decision and Communication

Present the tradeoff configurations to decision makers using this format:

> "We have three paths. Path A delivers [X] by [date] but costs [Y more]. Path B delivers [reduced X] by [date] within budget. Path C delivers [full X] within budget but not until [later date]. Which matters most to you — speed, scope, or savings?"

Then document the chosen configuration and the explicit tradeoffs accepted.

## False-Positive Prevention (MUST follow)

**DON'T:**
- Pretend all constraints can be satisfied simultaneously — this is dishonest and leads to failure
- Present only the option you prefer — show all three and let the decision maker choose
- Treat SOFT constraints as HARD — test whether they're truly immovable
- Ignore constraint coupling — cutting quality often increases total time due to rework
- Make the tradeoff invisible — when constraints are violated, name it explicitly
- Accept "just work harder" as a constraint solution — capacity is a real limit

**DO:**
- Force explicit priority ranking, even when it's uncomfortable
- Show the math: "If we cut timeline by 3 weeks, we need 2 more engineers at $X"
- Distinguish between constraints that come from physics/reality vs. organizational preferences
- Challenge constraints that are assumed but untested ("Has anyone asked if the deadline is flexible?")
- Revisit tradeoffs when conditions change — the right answer shifts with new information
- Present tradeoffs in "if/then" format so decision makers understand consequences

## Expected Output

### Output Format

```markdown
## Multi-Constraint Analysis

**Decision/Project:** [What's being optimized]
**Date:** [When analyzed]

---

### Constraint Inventory

| Constraint | Classification | Specific Limit | Negotiable? |
|-----------|---------------|----------------|-------------|
| [Constraint 1] | HARD/FIRM/SOFT | [Specific value] | [Who can change it] |
| [Constraint 2] | HARD/FIRM/SOFT | [Specific value] | [Who can change it] |
| [Constraint 3] | HARD/FIRM/SOFT | [Specific value] | [Who can change it] |

**Priority Ranking (forced):**
1. [Most important — would sacrifice everything else for this]
2. [Second most important]
3. [Third]
4. [Would sacrifice this first]

---

### Configuration A: "[Name]" — Optimizes [X] + [Y]

**What you get:** [Specific deliverable]
**What it costs:** [Specific price/resources]
**What you sacrifice:** [Specific things lost]
**Timeline:** [When delivered]
**Risk:** [What could go wrong]
**Hidden cost:** [Second-order effect]

### Configuration B: "[Name]" — Optimizes [X] + [Z]

[Same structure]

### Configuration C: "[Name]" — Optimizes [Y] + [Z]

[Same structure]

---

### Comparison Matrix

| Dimension | Config A | Config B | Config C |
|-----------|----------|----------|----------|
| Delivery date | [Date] | [Date] | [Date] |
| Total cost | [$X] | [$X] | [$X] |
| Scope delivered | [X%] | [X%] | [X%] |
| Quality level | [Description] | [Description] | [Description] |
| Key risk | [Risk] | [Risk] | [Risk] |

---

### Recommendation

**Best fit for this context:** [Configuration X]
**Because:** [Reasoning tied to priority ranking]
**What decision maker must accept:** [Explicit tradeoff]
**Review point:** [When to reassess if conditions change]
```

## Example Output

```markdown
## Multi-Constraint Analysis

**Decision/Project:** Launch customer self-service portal
**Date:** 2026-02-26

---

### Constraint Inventory

| Constraint | Classification | Specific Limit | Negotiable? |
|-----------|---------------|----------------|-------------|
| Launch date | FIRM | April 30 (board committed) | CEO only |
| Budget | HARD | $200K (approved, no more available) | Not negotiable |
| Feature set | SOFT | 12 features in original spec | Product lead |
| Quality | HARD | Zero security vulnerabilities | Non-negotiable |
| Team | FIRM | 4 engineers (can't hire fast enough) | VP Eng could lend 1 from Platform |

**Priority Ranking (forced):**
1. Quality/Security — non-negotiable, regulatory requirement
2. Launch date — board commitment, competitive pressure
3. Budget — hard ceiling, fiscal year constraint
4. Feature set — would sacrifice this first

---

### Configuration A: "Full Speed" — Optimizes Quality + Timeline

**What you get:** 8 of 12 features, fully secure, launched April 30
**What it costs:** $280K (+$80K for 2 contract engineers for 8 weeks)
**What you sacrifice:** Budget ceiling — need approval for $80K overage
**Timeline:** April 30 on target
**Risk:** Contractors need 1-week ramp, reducing effective capacity
**Hidden cost:** Team burnout from onboarding contractors while building

### Configuration B: "Lean Launch" — Optimizes Quality + Budget

**What you get:** 6 core features, fully secure, launched April 30, within $200K
**What it costs:** $195K (within budget)
**What you sacrifice:** 6 features deferred to v2 (May-June), including reporting dashboard and bulk operations
**Timeline:** April 30 for v1, June 15 for full feature set
**Risk:** Customers expecting full feature set may be disappointed; CS team needs talking points
**Hidden cost:** Two launches instead of one = double QA, double release overhead

### Configuration C: "Full Vision" — Optimizes Quality + Features

**What you get:** All 12 features, fully secure, within $200K budget
**What it costs:** $200K (within budget)
**What you sacrifice:** Time — launch pushed to June 15
**Timeline:** June 15 (6.5 weeks late)
**Risk:** Board expectations missed; competitor may launch first
**Hidden cost:** 6 weeks of delayed customer value = ~$45K in support costs that portal would have prevented

---

### Comparison Matrix

| Dimension | A: Full Speed | B: Lean Launch | C: Full Vision |
|-----------|--------------|----------------|----------------|
| Delivery date | April 30 | April 30 (v1) / June 15 (v2) | June 15 |
| Total cost | $280K (+$80K) | $195K | $200K |
| Features delivered | 8 of 12 | 6 of 12 (then 12) | 12 of 12 |
| Quality level | Full security review | Full security review | Full security review |
| Key risk | Budget overage approval | Customer disappointment | Board/competitive timing |

---

### Recommendation

**Best fit for this context:** Configuration B: "Lean Launch"
**Because:** Meets the top 3 priorities (quality, timeline, budget). Feature reduction is the lowest-ranked constraint and can be recovered in v2.
**What decision maker must accept:** 6 features launch later. Need Product Lead to define the v1 cut (recommend: keep auth, profiles, ticket submission, knowledge base, settings, notifications; defer: reporting, bulk ops, integrations, advanced search, custom branding, API access).
**Review point:** March 15 — if team velocity is ahead of plan, pull 1-2 deferred features into v1.
```

## Customization Guide

- **For product decisions:** Add "user impact" and "competitive differentiation" as constraint types
- **For engineering decisions:** Add "technical debt" and "system reliability" constraints
- **For hiring decisions:** Add "team dynamics" and "ramp time" constraints
- **For personal decisions:** Replace budget with "energy/willpower" and add "relationship impact"
- **For organizational change:** Add "change fatigue" and "political capital" constraints

## Techniques Used

- **ST-01 (Clear Objective):** Explicit constraint inventory and priority ranking
- **ST-02 (Sequential Instructions):** Five-step optimization process
- **RT-02 (Multi-Dimensional Analysis):** Multiple constraint dimensions analyzed independently
- **RT-03 (Tree of Thoughts):** Three distinct configurations representing different tradeoffs
- **CM-02 (Constraint Specification):** HARD/FIRM/SOFT classification system
- **DS-06 (Prioritization Guidance):** Forced ranking and comparison matrix

## Related Prompts

- [decisioning_time_boxed_decision_protocol.md](decisioning_time_boxed_decision_protocol.md) - When time itself is the binding constraint
- [decisioning_resource_constrained_solver.md](decisioning_resource_constrained_solver.md) - When resources are the primary bottleneck
- [validation_adversarial_mini_check.md](../domain-productivity/validation/validation_adversarial_mini_check.md) - Verify your tradeoff analysis
