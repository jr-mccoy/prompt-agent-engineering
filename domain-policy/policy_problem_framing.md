---
title: "Policy Problem Framing — Define the Problem Before Generating Options"
category: policy/problem-definition
description: "Frame a policy problem before anyone proposes solutions. Forces specification of who is affected (with magnitude), the measured current state, the no-action trajectory, the contested framings held by different stakeholders, root causes versus symptoms, what has already been tried, and the policy window. Counters the most common upstream failure: solving a misframed problem efficiently. Pre-condition for policy_options_memo.md."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - policy
  - problem-framing
  - root-cause
  - public-policy
  - agenda-setting
updated: "2026-06-18"
reasoning:
  styles: [analytic, structural, dialectical, causal]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: politically_charged
  collaboration: small_team
  output_format: structured
  user_role: [policy, analyst, executive, advocate]
  mode: [diagnose, synthesize, document]
related_prompts:
  - domain-policy/policy_options_memo.md
  - domain-policy/policy_stakeholder_coalition_map.md
  - domain-research-academic/research_evidence_map.md
---

# Policy Problem Framing

**Objective:** Produce a framed problem statement that is sharp enough to generate options against, and that surfaces the framings *not* chosen and why. A policy problem is rarely self-evident: the same facts support multiple framings, each of which implies a different solution set. Choosing a framing is a consequential, often invisible act. This prompt makes the framing explicit, defensible, and auditable so that downstream options analysis is not silently constrained by an unexamined frame.

This is the upstream step before `policy_options_memo.md`, which assumes a problem is already framed. Frame first; generate options second.

**When to use:**
- A policy debate is happening but the problem is being argued through proposed solutions ("we need X") rather than stated as a condition.
- Multiple stakeholders are talking past each other and you suspect they are framing the same problem differently.
- Before commissioning options analysis, modeling, or a memo — to set the frame the options will be judged against.
- An existing policy effort is failing and you want to test whether the problem was misframed from the start.

**When NOT to use:**
- The problem is genuinely uncontested and well-measured, and you only need options — go straight to `policy_options_memo.md`.
- You are framing a private operational problem, not public policy — use a general decision-framing tool.
- The task is advocacy for a predetermined position; this prompt will surface inconvenient framings you may not want.

**Audience:** Policy analysts, government affairs leads, foundation and NGO program staff, legislative staff, advocates, and civic-minded individuals who need to define a problem rigorously before it hardens into a solution.

---

## Inputs / Context

1. **The apparent problem.** However it is currently being stated, even if stated as a solution ("we need rent control").
2. **Jurisdiction and scope.** Geographic, sectoral, temporal boundaries.
3. **Available data.** Statistics, studies, administrative records, comparable jurisdictions — and gaps.
4. **Stakeholders.** Who has a stake and who is talking about this.
5. **Prior attempts.** What policies, programs, or interventions have addressed this before, here or elsewhere.
6. **Why now.** What event, trend, deadline, or coalition has put this on the agenda.

---

## Constraints

### Must
- State the problem as an **empirical condition** (something measurable about the world), not as the absence of a preferred policy.
- Quantify **who is affected and by how much** — specific populations, counts or rates, severity — not "many people."
- Establish the **current state with data**, and the **no-action trajectory** (what happens if nothing changes) as a separate claim.
- Surface **at least two competing framings** held by real stakeholders, each with the solution set it implies.
- Distinguish **root causes** from **symptoms** explicitly, with a causal chain.
- Document **what has been tried** and what is known about why it succeeded or failed.
- Name the **policy window** — why this is actionable now — and how durable that window is.
- End with the **chosen framing AND the framings rejected**, each with a stated reason.

### Must Not
- Frame the problem as "we lack policy X." That smuggles the answer into the question.
- Use aggregate or averaged language that hides distribution ("the average renter") when the problem is concentrated.
- Collapse the contested framing into a single neutral-sounding statement that one faction would reject.
- Treat a symptom (visible, measurable) as the root cause because it is easier to act on.
- Assume the no-action trajectory is "things stay the same" — most problems worsen or shift under no action.
- Present the policy window as permanent. Windows close.

---

## Instructions

1. **Restate the apparent problem and strip the solution.** Take the problem as given, then rewrite it as a condition in the world. If the original says "we need X," ask "what condition would X address?" and state that condition. Flag if the original was solution-shaped.
2. **Specify who is affected, with magnitude.** Name the populations, count or rate them, and characterize severity. Break out concentration: is this 2% of people severely affected or 40% mildly affected? The answer changes the problem.
3. **Establish current state with data.** State the measured baseline. Cite the source and its quality. Where data is missing, say so and note what proxy is being used.
4. **Project the no-action trajectory.** What happens over the relevant horizon if no policy changes? Is the problem worsening, stable, or self-correcting? On what evidence? This is the bar any option must beat.
5. **Surface competing framings.** Identify how different stakeholders frame the same facts. For each framing: state it, name who holds it, and list the solution set it implies. (E.g., "housing shortage → build more" vs. "affordability gap → subsidize demand" vs. "displacement → protect tenants.")
6. **Separate root causes from symptoms.** Build a causal chain from visible symptoms back toward structural causes. Mark which level is symptom and which is root. Note where the chain is speculative.
7. **Inventory what has been tried.** List prior interventions here and in comparable jurisdictions, with outcomes and the leading explanation for each outcome. Distinguish "didn't work" from "wasn't tried at scale" from "worked but politically reversed."
8. **Characterize the policy window.** Why now? What opened it (crisis, election, court ruling, budget cycle, coalition)? How long is it likely to stay open? What would close it?
9. **Commit to a framing and document the rejects.** State the framing you adopt and why. Then list the framings you rejected, each with the reason — including framings that are politically dominant but you judge to be wrong, and your basis for that judgment.

---

## False-Positive Prevention

1. **Solution-as-problem.** The problem statement names a missing policy rather than a condition. Test: could two people who disagree about the solution both accept this problem statement? If not, it's solution-shaped.
2. **Magnitude hand-waving.** "A growing crisis affecting countless families" with no numbers. Replace every vague quantifier with a count, rate, or explicit "unknown — here's the proxy."
3. **Averaged-away distribution.** Reporting a mean that hides a concentrated harm. Always check whether the problem is concentrated and report the concentration.
4. **Static no-action assumption.** Treating "do nothing" as "stays the same." Most problems have a trajectory; project it.
5. **Single-framing capture.** Adopting the politically dominant framing without naming alternatives. If you can't articulate the strongest competing framing, you haven't framed yet.
6. **Symptom-as-root.** Naming the visible, measurable symptom as the cause because it's actionable. Push the causal chain at least one level past the obvious.
7. **Prior-attempt amnesia.** Framing as if the problem is new when it has been addressed before. Absence of a prior-attempts section is a red flag.
8. **Window blindness.** Failing to state why now, leading to a frame that's analytically clean but politically inert.
9. **Rejected-framing erasure.** Omitting the framings not chosen. The reject list is the auditable core of the framing decision.
10. **False neutrality.** Writing a problem statement so anodyne that no stakeholder objects — which usually means it's too vague to generate options.

---

## Output Format

```
# PROBLEM FRAMING — [topic]
Jurisdiction / scope: [...]
Date framed: [date]

## Problem statement (as a condition)
[One paragraph stating the problem as a measurable condition in the world, not as a missing policy.]
Original framing (if solution-shaped): "[...]" → restated as condition above.

## Who is affected
| Population | Count / rate | Severity | Concentration note |
|------------|--------------|----------|--------------------|
| [...]      | [...]        | [...]    | [concentrated / diffuse + detail] |

## Current state (with data)
- Baseline: [measure] = [value] (source: [...], quality: [strong/moderate/weak])
- Data gaps: [...] (proxy used: [...])

## No-action trajectory
- Over [horizon]: [worsening / stable / self-correcting]
- Basis: [...]
- This is the bar options must beat.

## Competing framings
| Framing | Held by | Solution set it implies |
|---------|---------|-------------------------|
| [A]     | [...]   | [...]                   |
| [B]     | [...]   | [...]                   |
| [C]     | [...]   | [...]                   |

## Causes: root vs symptom
Symptom level: [...]
→ caused by: [...]
→ caused by: [...] (root)
Speculative links: [...]

## What has been tried
| Intervention | Where / when | Outcome | Leading explanation |
|--------------|--------------|---------|---------------------|
| [...]        | [...]        | [...]   | [...]               |

## Policy window
- Why now: [event / trend / coalition]
- Durability: [open until ...; closes if ...]

## Chosen framing
[The framing adopted, stated, with reasoning.]

## Framings rejected
| Rejected framing | Reason rejected |
|------------------|-----------------|
| [...]            | [...]           |

## Hand-off note for options analysis
[What the options memo should optimize for, given this frame.]
```

---

## Verification

- [ ] Problem stated as an empirical condition, not a missing policy.
- [ ] Affected populations quantified with magnitude and concentration.
- [ ] Current state backed by data with source quality noted.
- [ ] No-action trajectory projected as a distinct claim.
- [ ] At least two competing framings surfaced, each with its implied solution set.
- [ ] Root causes distinguished from symptoms via an explicit causal chain.
- [ ] Prior attempts inventoried with outcomes and explanations.
- [ ] Policy window named, with durability.
- [ ] Chosen framing stated AND rejected framings listed with reasons.
- [ ] No solution-shaped problem statement.
- [ ] No averaged-away distribution.
- [ ] Hand-off note connects the frame to downstream options work.
