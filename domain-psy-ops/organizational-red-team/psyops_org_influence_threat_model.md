---
title: "Organizational Influence Threat Model — Who Would Target Us, and What We Would Do"
category: psy-ops/organizational-red-team
description: "Threat-model an organization's exposure to influence and information attack: which adversaries have motive and means, which channels reach your audiences, what a plausible campaign against you would exploit, and which detection and response capabilities you actually have. Produces findings and countermeasures only — never campaign material — and treats fixing genuine underlying problems as a first-class countermeasure."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - threat-modeling
  - organizational-resilience
  - communications
  - risk
updated: "2026-07-28"
reasoning:
  styles: [analytic, adversarial, systems]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: threat_model_with_countermeasures
  user_role: [executive, communications, trust_and_safety, security, policy]
  mode: [assess, design, decide]
related_prompts:
  - domain-psy-ops/organizational-red-team/psyops_narrative_vulnerability_assessment.md
  - domain-psy-ops/organizational-red-team/psyops_personnel_targeting_exposure_review.md
  - domain-risk/risk_threat_model_non_technical.md
---

# Organizational Influence Threat Model

**Objective:** Build a threat model for your organization's exposure to influence and information attack, on the standard threat-modeling shape: who would do this, why, through what channels, exploiting what, and what you would actually do about it. The deliverable is **findings and countermeasures**. This prompt does not produce campaign material, messaging, personas, or targeting plans — not as illustration, not as a worked example, and not as "what they might say." Modeling an attack does not require writing one, and an organization's threat model is a document that circulates.

The most important and most neglected output is the countermeasure category most teams skip: **fix the real problem**. A large share of what damages organizations in this space is amplification of something genuinely true — a real safety failure, a real pattern of complaints, a real inequity. Communications responses to true criticism fail, and correctly so. The threat model must distinguish exposure that is a **communications problem** from exposure that is an **actual problem being communicated**, because the second one has a different fix and no amount of message discipline substitutes for it.

**When to use:**
- Your organization is entering a period of elevated exposure — a launch, a controversy, a regulatory fight, an election, an acquisition.
- You have been targeted before and want to prepare properly rather than improvise again.
- You are building or justifying a communications-resilience or trust-and-safety capability.
- Leadership wants to know what the realistic risk is, stated in terms they can act on.

**When NOT to use:**
- You are under active attack right now — use `../counter-messaging/psyops_crisis_communication_integrity_plan.md`.
- You want the narrative-specific vulnerability layer only — use `psyops_narrative_vulnerability_assessment.md`.
- You want a general non-technical threat model — use `domain-risk/risk_threat_model_non_technical.md`.
- You are assessing exposure of individual staff — use `psyops_personnel_targeting_exposure_review.md`.

**Audience:** Communications leads, trust-and-safety and security teams, executives, and policy staff.

---

## Inputs / Context

1. **What the organization does**, and who materially wins or loses because of it. This generates the adversary list more reliably than anything else.
2. **Your audiences.** Customers, staff, regulators, investors, communities, partners — and which of them a campaign would actually need to move to hurt you.
3. **Channels.** Where those audiences get information about you, including channels you do not control and cannot see.
4. **History.** Previous attacks, controversies, viral incidents, and how they went.
5. **Known genuine weaknesses.** Real problems that would be damaging if surfaced. This section requires honesty and is the most valuable input in the document.
6. **Current capability.** What detection, escalation, decision authority, and response you actually have — including out-of-hours and at weekends.
7. **Constraints.** Regulatory, legal, and contractual limits on what you can say and how fast.

---

## Constraints

### Must
- Derive adversaries from **material interest**, not from a generic list. Competitors, displaced incumbents, aggrieved former staff, affected communities, activist groups, litigants, and — where genuinely applicable — state actors.
- Assess **motive and means separately**. Many parties have motive; far fewer have means, and conflating them inflates the model into uselessness.
- Distinguish **communications problems from actual problems**, and route the second to a remediation owner rather than to messaging.
- Map **channels you cannot observe** — closed groups, messaging apps, industry forums, employee networks — since these are where most damaging narratives form.
- Assess **detection capability honestly**: how you would learn, how fast, out of hours, and who would tell you.
- Assess **decision authority under time pressure**: who can approve a response at 11pm on a Saturday, which is when this happens.
- Produce **countermeasures across four categories**: fix the real problem, reduce exposure, improve detection, prepare response.
- State **what you will not defend against**, and accept it explicitly.

### Must Not
- Produce sample attack messaging, narratives, personas, ad copy, or targeting parameters — in any section, for any purpose, including as illustration.
- Name individuals as likely attackers. Adversaries are categories and organizations; naming individuals in an internal threat model is defamatory exposure and it leaks.
- Recommend counter-influence, covert response, inauthentic amplification, or reputation management through undisclosed channels.
- Recommend surveillance of employees, critics, or communities.
- Treat legitimate criticism, journalism, regulatory scrutiny, or organized labour as an influence threat. This is the standard way threat models become instruments for suppressing accountability.
- Fabricate adversary capabilities, prior incidents, or intelligence about who is interested in you.
- Let the model justify avoiding a genuine problem by reframing it as an information risk.

---

## Instructions

### Step 1 — Map who materially wins if you are damaged
Work from interest, not from imagination. Who gains contracts, market share, policy outcomes, settlements, or vindication? This produces a far better adversary list than brainstorming.

### Step 2 — Score motive and means separately
For each category: motive strength, and separately the means — money, reach, technical capability, insider access, media relationships. Only categories with both belong in the operative model.

### Step 3 — Identify which audience actually matters
A campaign only hurts you if it moves someone with power over your outcomes: a regulator, a large customer, your own staff, an investor. Identify who that is. Most hostile attention never reaches them and is noise.

### Step 4 — Map channels, including the invisible ones
Where would this travel? Include closed and unobservable channels — messaging groups, industry forums, internal chat, community networks. Note which you would never see directly.

### Step 5 — Inventory genuine weaknesses honestly
What is actually true about your organization that would damage you if surfaced? Every item here gets a remediation owner, not a message. **This is the most valuable section and the one most likely to be softened.** Softening it defeats the exercise.

### Step 6 — Assess detection and decision capability
How would you find out, how fast, and from whom? Then: who can decide and approve a response outside business hours? Test this against a real weekend scenario, and be honest about the answer.

### Step 7 — Build countermeasures in four categories
Fix the real problem (with owners and dates), reduce exposure, improve detection, prepare response. Weight toward the first — it is the only category that removes risk rather than managing it.

### Step 8 — Adversarial check and accepted risk
Argue that this model is inflated and the realistic risk is ordinary criticism you should simply answer well. Then state explicitly what you are choosing not to defend against.

---

## False-Positive Prevention

1. **Criticism reclassified as attack.** The most damaging failure. Journalism, regulators, unions, and unhappy customers are not influence operations, and modeling them as such produces an organization that fixes nothing and attacks its critics.
2. **Motive without means.** Listing everyone who dislikes you. Without means the category is not operative and it inflates the model past usability.
3. **Real problems laundered into comms risk.** Treating a genuine safety, conduct, or equity failure as a narrative to manage. It will not work, and the attempt is usually what turns a problem into a scandal.
4. **State-actor inflation.** Attributing ordinary commercial or activist hostility to sophisticated adversaries, which produces expensive and irrelevant countermeasures.
5. **Detection overestimated.** Assuming you would notice. Most organizations learn from a journalist's call, on a Friday evening.
6. **Authority untested.** A response plan with no one empowered to execute it out of hours, which is the only time it will be needed.
7. **Invisible channels ignored.** Modeling only observable public platforms, missing that the damaging narrative forms in closed groups first.
8. **Model becomes a target list.** Naming individual critics, which converts a defensive document into a liability and, if leaked, into the story.

---

## Output Format

```
# Influence threat model — [organization]

## Who materially benefits from damaging us
| Category | Motive strength | Means | Operative? |
|---|---|---|---|
| [category — never an individual] | high | low | no |

## Audiences that actually matter
[Who must be moved for this to hurt us — regulator, major customer, staff, investors]

## Channel map
| Channel | Audience reached | Observable by us? |
|---|---|---|
| [...] | [...] | no — closed group |

## Genuine weaknesses (honest section)
| What is actually true | Damage if surfaced | Remediation owner | Date |
|---|---|---|---|
| [...] | high | [name/role] | [date] |

*Everything here gets an owner, not a message.*

## Communications problem vs actual problem
| Exposure | Which is it | Route to |
|---|---|---|
| [...] | actual problem | remediation owner |
| [...] | communications problem | comms |

## Detection capability (honest)
- How we would learn: [...]
- Expected time to detection: [...]
- Out of hours / weekend: [...]
- Most likely actual route: [a journalist calls]

## Decision authority under pressure
- Who can approve a response at 11pm Saturday: [name/role]
- Tested? [yes/no]

## Countermeasures
| Category | Action | Owner | Date |
|---|---|---|---|
| Fix the real problem | | | |
| Reduce exposure | | | |
| Improve detection | | | |
| Prepare response | | | |

## Accepted risk — what we will not defend against
[Explicit list]

## Adversarial check
[The case that this model is inflated and the real risk is ordinary criticism we should answer well]
```

---

## Verification

- [ ] No sample attack messaging, narrative, persona, or targeting parameter appears anywhere in the output.
- [ ] Adversaries are categories and organizations; no individual is named.
- [ ] Motive and means are scored separately, and only categories with both are treated as operative.
- [ ] Genuine weaknesses are listed honestly, each with a remediation owner and date.
- [ ] Communications problems and actual problems are separated, with actual problems routed away from messaging.
- [ ] Legitimate criticism, journalism, regulatory scrutiny, and organized labour are not modeled as threats.
- [ ] Detection capability is assessed honestly, including out of hours.
- [ ] Decision authority under time pressure is named and its testedness stated.
- [ ] Countermeasures span all four categories and are weighted toward fixing real problems.
- [ ] No counter-influence, covert response, or surveillance of employees or critics is recommended.
