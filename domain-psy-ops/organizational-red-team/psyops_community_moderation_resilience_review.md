---
title: "Community Resilience Review — Design Against Brigading and Manufactured Consensus"
category: psy-ops/organizational-red-team
description: "Review a community or platform's structural resilience to brigading, manufactured consensus, and moderation capture: which mechanisms convert volume into visibility or sanction, how new-account and vote-based influence is bounded, and whether reporting can be weaponized against the people it exists to protect. Assesses design, not participants."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - community-management
  - trust-and-safety
  - platform-design
  - moderation
updated: "2026-07-28"
reasoning:
  styles: [systems, analytic, adversarial]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: design_review_with_mitigations
  user_role: [trust_and_safety, community_manager, product, moderator]
  mode: [assess, design, decide]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-psy-ops/influence-operations/psyops_inauthentic_account_signal_assessment.md
  - domain-psy-ops/organizational-red-team/psyops_org_influence_threat_model.md
---

# Community Resilience Review

**Objective:** Review a community or platform's **structural** resilience to brigading, manufactured consensus, and moderation capture. The subject is design, not people: which mechanisms convert raw volume into visibility, credibility, or sanction; how much influence a new or low-investment account can exert; whether reporting and flagging can be turned against the users they exist to protect; and whether moderation itself can be captured by a determined faction.

The framing matters because the alternative — hunting for bad actors — scales badly, produces false positives against real members, and leaves the exploitable mechanism in place for the next group. **A community whose design converts volume into consensus will be captured eventually**, by whoever wants it most, and no amount of enforcement fixes that. Structural mitigations are durable; enforcement is a treadmill.

The counterweight is that every anti-brigading mitigation has a cost, usually paid by newcomers and by minority views. Reputation gating, rate limits, and slow modes all preserve incumbents. A community perfectly resistant to manipulation is usually one nobody new can join, and design that entrenches the existing majority is its own kind of capture — it just does not feel like one to the people already inside.

**When to use:**
- Your community has been brigaded, or you expect it to be.
- Reports and flags are being used tactically against particular members.
- A faction appears to be steering discussion or moderation.
- You are designing community mechanics and want to anticipate the failure modes.

**When NOT to use:**
- You need to assess whether specific accounts are coordinated — use `../influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md`.
- You are assessing account automation — use `../influence-operations/psyops_inauthentic_account_signal_assessment.md`.
- The exposure is organizational rather than community-mechanical — use `psyops_org_influence_threat_model.md`.

**Audience:** Trust-and-safety staff, community managers, product designers, and volunteer moderators.

---

## Inputs / Context

1. **The community.** Size, purpose, membership model, and how someone joins.
2. **The mechanics.** Voting, ranking, reputation, flagging, reporting, visibility rules, and what each one actually controls.
3. **Moderation model.** Who moderates, how they are selected, what powers they hold, and what appeal exists.
4. **Account creation.** Cost and friction to make a new account, and what a new account can immediately do.
5. **Incident history.** Prior brigading, vote manipulation, report abuse, or moderator capture, and how each was handled.
6. **Who is currently underserved.** Which members already struggle to be heard — because every mitigation will affect them first.

---

## Constraints

### Must
- Assess **mechanisms, not members**. The finding is about what the design permits.
- Trace every path by which **volume converts into outcome**: visibility, ranking, credibility, sanction, removal.
- Assess **new-account capability** — what someone can do within minutes of joining, which bounds the cost of an attack.
- Assess **report and flag weaponization**, including whether reports are visible to moderators as coordinated and whether false reporting carries any cost.
- Assess **moderator selection and capture**: how moderators are chosen, whether a faction can accumulate positions, and what check exists on them.
- Assess **appeal and reversal**, including how a wrongly sanctioned member gets heard.
- State the **cost of every mitigation**, specifically its effect on newcomers and minority views.
- Distinguish **brigading from a genuine influx** — real events bring real people, and treating them as an attack is a failure mode with its own harm.

### Must Not
- Produce guidance on brigading, vote manipulation, evading detection, or capturing moderation.
- Recommend mitigations that entrench incumbents without stating that cost explicitly.
- Treat unpopular or minority views as attacks. A view held by few is not manufactured, and the mechanisms that suppress brigading suppress dissent identically.
- Recommend surveillance of members beyond what moderation requires and what the community has been told about.
- Fabricate platform mechanics, prior incidents, or effectiveness claims about specific interventions.
- Assume enforcement scales. Any recommendation resting on moderators noticing more will fail under load.
- Name individual members as brigaders.

---

## Instructions

### Step 1 — Map volume-to-outcome paths
Every mechanism where more accounts produce a different result: ranking, visibility, trending, auto-removal thresholds, report-triggered actions. These are the attack surface and they are usually more numerous than expected.

### Step 2 — Cost the attack
For each path, how many accounts and how much effort would change an outcome? If a dozen accounts can remove a post or bury a view, the community is trivially capturable regardless of anyone's intentions.

### Step 3 — Assess new-account capability
What can an account do in its first hour, day, and week? Compare against account creation cost. This ratio is the single most useful number in the review.

### Step 4 — Assess report weaponization
Can coordinated reports trigger automatic action? Do moderators see report clustering as a signal that reports themselves are coordinated? Does false reporting cost anything? Report abuse is under-modeled and disproportionately targets the members moderation exists to protect.

### Step 5 — Assess moderation capture
How are moderators selected and removed? Can an aligned group accumulate positions over time? Who moderates the moderators, and what happens when the capture is gradual and each individual step looks reasonable?

### Step 6 — Assess appeal and reversal
How does a wrongly actioned member get heard, how long does it take, and does anyone track reversal rates? A high reversal rate that nobody measures means the community is losing members invisibly.

### Step 7 — Design mitigations and cost each one
Structural options: rate limits, reputation gating, participation-weighted visibility, report-clustering detection, slow modes, and moderator term limits or rotation. For each, state the cost — who it excludes, and how it affects newcomers and minority views.

### Step 8 — Distinguish influx from brigade, then run the adversarial check
Define in advance how you will tell a genuine influx from a coordinated one, since the response differs entirely. Then argue that the proposed mitigations mainly protect incumbents, and adjust.

---

## False-Positive Prevention

1. **Minority views read as brigading.** The most damaging error. Anti-manipulation mechanisms suppress unpopular views and coordinated ones identically, and the community will not notice the difference.
2. **Genuine influx treated as attack.** Real events bring real newcomers with real opinions. Locking down in response drives away exactly the growth the community needed.
3. **Enforcement assumed to scale.** Mitigations resting on moderators noticing more, which fails precisely when volume is highest.
4. **Incumbent entrenchment unstated.** Reputation gating and rate limits preserve the existing majority. That is sometimes the right trade, but it must be stated, not smuggled in.
5. **Report abuse unmodeled.** Assessing content manipulation while ignoring that the reporting system is the easiest thing to weaponize and hits vulnerable members hardest.
6. **Gradual capture missed.** Looking for a coup when moderation capture happens through a series of individually reasonable appointments.
7. **Member-level findings.** Naming individuals as brigaders instead of identifying the mechanism that made the brigade effective.
8. **Appeal ignored.** Building detection with no reversal path, so every false positive is permanent and invisible.

---

## Output Format

```
# Community resilience review — [community]

## Volume-to-outcome paths
| Mechanism | What volume changes | Accounts needed to shift an outcome | Effort |
|---|---|---|---|
| [ranking] | visibility | [n] | low |

## New-account capability
| Time since creation | What the account can do |
|---|---|
| 1 hour | |
| 1 day | |
| 1 week | |
**Account creation cost:** [...] → **attack cost ratio:** [...]

## Report weaponization
- Coordinated reports trigger automatic action? [yes/no]
- Report clustering visible to moderators as a signal? [yes/no]
- Cost of false reporting? [...]
- Who is most exposed to report abuse here? [...]

## Moderation capture
[Selection, removal, accumulation risk, check on moderators, gradual-capture exposure]

## Appeal and reversal
[Path, time, reversal rate tracked? — untracked reversals mean invisible member loss]

## Mitigations, with costs
| Mitigation | Effect | Cost — who it excludes | Effect on newcomers and minority views |
|---|---|---|---|
| [rate limit] | | | |

## Influx vs brigade — decided in advance
[How we will tell a genuine influx from a coordinated one, and the different response to each]

## Currently underserved members
[Who already struggles to be heard, and how each mitigation affects them]

## Adversarial check
[The case that these mitigations mainly protect incumbents — and what was adjusted]
```

---

## Verification

- [ ] Findings attach to mechanisms; no individual member is named as a brigader.
- [ ] Every volume-to-outcome path is traced with an attack cost.
- [ ] New-account capability is assessed against account creation cost.
- [ ] Report weaponization is assessed, including who is most exposed to it.
- [ ] Moderation capture includes the gradual-accumulation path, not just a coup scenario.
- [ ] Appeal and reversal are assessed, including whether reversal rates are tracked.
- [ ] Every mitigation states its cost and its effect on newcomers and minority views.
- [ ] A criterion for distinguishing genuine influx from brigading is defined in advance.
- [ ] No mitigation rests on enforcement scaling with volume.
- [ ] No guidance on brigading, vote manipulation, evasion, or moderation capture appears anywhere.
