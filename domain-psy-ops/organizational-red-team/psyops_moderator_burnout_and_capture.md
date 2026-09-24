---
title: "Moderator Burnout and Capture — Sustained Hostile Attention as an Attrition Strategy"
category: psy-ops/organizational-red-team
description: "Review how exposed a community's moderators and trust-and-safety staff are to sustained hostile attention used as an attrition strategy — harassment that wears people down until they quit, go quiet, or start appeasing the loudest faction. Assesses structure, not individuals: exposure of moderator identities, how decisions are attributed, workload and rotation, escalation and support paths, and the early signs of capture. Outputs findings and countermeasures only."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - moderation
  - trust-and-safety
  - staff-wellbeing
  - organizational-red-team
updated: "2026-09-24"
reasoning:
  styles: [systems, analytic, protective, adversarial]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: exposure_review_with_countermeasures
  user_role: [trust_and_safety, community_manager, moderator, operations]
  mode: [assess, design, decide]
related_prompts:
  - domain-psy-ops/organizational-red-team/psyops_community_moderation_resilience_review.md
  - domain-psy-ops/organizational-red-team/psyops_org_influence_threat_model.md
  - domain-legal/personal-self-advocacy/harassment-stalking/legalprep_digital_safety_threat_evidence_organizer.md
---

# Moderator Burnout and Capture

**Objective:** Review how exposed a community's moderators and trust-and-safety staff are to **sustained hostile attention used as an attrition strategy**. The goal of that strategy is rarely to win an argument. It is to make moderating unbearable — through volume, personal attacks, doxxing, false reports, and relentless relitigating of decisions — until moderators **quit**, **go quiet** and stop enforcing against the faction applying the pressure, or **start appeasing** it. The last outcome is the most dangerous because it is the least visible: a moderation team that has been captured still looks like a moderation team.

`psyops_community_moderation_resilience_review.md` reviews whether a community's mechanics convert volume into consensus. This prompt reviews the **people who hold the line** and the structures around them: whether moderator identities are exposed, whether decisions are attributed to individuals or to the team, how workload and exposure are rotated, whether escalation and support paths exist and are used, and whether the early signs of capture are being watched.

The framing is structural for the same reason the community review is. Blaming individual moderators for burning out or "going soft" misreads a predictable outcome of design. And the review applies the domain's constraint strictly: it outputs **findings and countermeasures**, never a map of which moderators are most vulnerable for anyone to use.

**When to use:**
- Your moderators or trust-and-safety staff are under sustained harassment, or have been.
- Moderator turnout, turnover, or enforcement consistency has dropped, and you want to know whether pressure is the cause.
- A faction seems to be getting its way with moderators more than its size would explain.
- You are designing a moderation program and want to build resilience in from the start.

**When NOT to use:**
- You want to review the community's mechanics — voting, reporting, visibility — rather than the moderators' exposure — use `psyops_community_moderation_resilience_review.md`.
- You need a broader threat model of who targets your organization — use `psyops_org_influence_threat_model.md`.
- An individual moderator needs to document threats against them — see `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_digital_safety_threat_evidence_organizer.md`.
- A moderator is in distress now — route them to support and professional help first; this is a structural review, not care.

**Audience:** Trust-and-safety leads, community managers, moderation coordinators, and operations staff.

---

## Inputs / Context

1. **The moderation structure.** Paid, volunteer, or mixed; team size; how decisions are made and communicated.
2. **Identity exposure.** Which moderators are identifiable by name, handle, photo, or linkable accounts, and whether that is by choice.
3. **Decision attribution.** Whether actions are signed by individuals, by the team, or by a generic account.
4. **Workload and exposure.** Volume per moderator, exposure to hostile or disturbing content, rotation, and time off.
5. **Hostile attention observed.** Types — volume, personal attacks, doxxing, false reports, off-platform contact — and duration. Describe behavior; do not name private individuals.
6. **Support and escalation.** What exists for moderators under attack: security, legal, wellbeing support, leadership backing — and whether it is actually used.
7. **Enforcement patterns over time.** Consistency, reversals, appeal outcomes, and any change after pressure campaigns.

---

## Constraints

### Must
- Assess **structure and exposure**, not individual moderators' resilience or character.
- Review **identity exposure**, **decision attribution**, **workload and rotation**, **support and escalation**, and **capture indicators** as separate findings.
- Treat **capture** — enforcement quietly bending toward the loudest faction — as a primary risk, and look for it in enforcement patterns rather than in anyone's stated intent.
- Pair every finding with a **countermeasure**, and state what each countermeasure costs.
- Include **volunteer moderators** on equal terms with paid staff; they are usually more exposed and less supported.
- Route individual distress to **support and professional help**, and harassment evidence to the linked documentation prompt.
- Run an **alternative-explanation pass**: burnout and inconsistency have ordinary causes — overload, unclear policy, disturbing content — unrelated to any campaign.
- End with an **adversarial check** against your own findings.

### Must Not
- Produce a ranking of which moderators are most vulnerable, most exposed, or most likely to give in.
- Name private individuals as members of a harassment campaign or as operators.
- Diagnose moderators, or assess their mental health.
- Recommend countermeasures that require moderators to give up their own safety or privacy.
- Treat enforcement changes after a campaign as capture without checking for legitimate policy or context changes.
- Include any content that describes how to apply pressure to moderators effectively.
- Invent incident counts, turnover figures, or enforcement statistics.

---

## Instructions

### Step 1 — Map the structure
Record team composition, paid versus volunteer, decision process, and how decisions reach users. This is the baseline everything else is measured against.

### Step 2 — Assess identity exposure
For each category of moderator (not each person), how identifiable are they, and by choice or by default? Note linkable personal accounts and any off-platform exposure. Default exposure that moderators did not choose is a finding.

### Step 3 — Assess decision attribution
Are decisions signed by individuals? Individually attributed decisions give attackers a person to target; team-attributed decisions spread the load. Note where individual attribution is required and why.

### Step 4 — Assess workload, exposure, and rotation
Volume, exposure to hostile and disturbing content, rotation off high-pressure queues, and real time off. Sustained exposure without rotation is a predictable path to attrition regardless of any campaign.

### Step 5 — Assess support and escalation
What happens when a moderator is targeted: security help, account protection, legal routes, wellbeing support, and visible leadership backing. Note whether each exists on paper only or is actually used.

### Step 6 — Look for capture indicators
Compare enforcement patterns before, during, and after pressure: reversals, inconsistent application to one faction, appeals won by volume rather than merit, moderators recusing or going inactive on particular topics. Record indicators, not conclusions.

### Step 7 — Alternative-explanation pass
For each finding, write the ordinary account: overload, unclear or changing policy, disturbing content load, ordinary volunteer turnover. Note what the campaign reading explains that the ordinary one does not.

### Step 8 — Countermeasures and adversarial check
Pair each finding with a countermeasure and its cost — team attribution, pseudonymity by default, rotation, escalation to paid staff, pre-committed backing, policy clarity. Then argue that your findings overstate the campaign and understate ordinary overload, and adjust.

---

## False-Positive Prevention

1. **Overload read as attack.** Burnout from ordinary volume and content exposure attributed to a campaign that is not the main cause.
2. **Policy change read as capture.** Enforcement shifting because policy or context legitimately changed.
3. **Loud users read as coordinated.** A vocal, persistent group of real members read as an organized attrition effort.
4. **Individual framing.** Treating burnout or inconsistency as a personal failing rather than a predictable outcome of exposure and structure.
5. **Volunteer blind spot.** Reviewing paid staff protections and assuming volunteers are covered.
6. **Paper support.** Counting support that exists in policy but is not used, known, or reachable when needed.
7. **Countermeasure cost ignored.** Recommending pseudonymity or team attribution without noting accountability or transparency trade-offs.
8. **Capture denial.** Dismissing capture because moderators say they are unaffected; capture is visible in patterns, not in self-report.

---

## Output Format

```
# Moderator attrition and capture review — [community]

## Structure baseline
Composition: [paid / volunteer / mixed] · Size: [...] · Decision process: [...]

## Findings
| Area | Finding | Severity | Countermeasure | Cost |
|---|---|---|---|---|
| Identity exposure | [...] | [low/med/high] | [...] | [...] |
| Decision attribution | [...] | | | |
| Workload and rotation | [...] | | | |
| Support and escalation | [...] | | | |
| Capture indicators | [...] | | | |

## Hostile attention observed (behavior only)
[Types and duration — no private individuals named]

## Capture indicators
| Indicator | Observed? | Alternative explanation |
|---|---|---|
| Reversals following pressure | | |
| Inconsistent enforcement toward one faction | | |
| Appeals won by volume | | |
| Topic-specific recusal or inactivity | | |

## Volunteer-specific findings
[...]

## Alternative-explanation pass
[Ordinary overload, policy change, content exposure — what they explain]

## Adversarial check
[The case that I have overstated the campaign — and what changed]

## Routing
Individual distress → support and professional help
Threat evidence → legalprep_digital_safety_threat_evidence_organizer.md
```

---

## Verification

- [ ] Structure and exposure are assessed, not individual moderators.
- [ ] Identity exposure, attribution, workload, support, and capture are separate findings.
- [ ] Capture indicators are drawn from enforcement patterns, with alternative explanations.
- [ ] Every finding has a countermeasure and a stated cost.
- [ ] Volunteer moderators are reviewed on equal terms.
- [ ] The alternative-explanation pass covers overload, policy change, and content exposure.
- [ ] Individual distress and threat evidence are routed out.
- [ ] The adversarial check argues against the campaign reading.
- [ ] No vulnerability ranking of moderators, no diagnosis, and no pressure technique appears.
- [ ] No private individual is named, and no incident counts or statistics were invented.
