---
title: "Coordination Indicators — Telling Coordinated Behavior from Organic Convergence"
category: psy-ops/influence-operations
description: "Assess whether a cluster of accounts or outlets is coordinated, using structural indicators that organic convergence does not produce: synchronized timing at implausible resolution, shared infrastructure, identical asset reuse, and unnatural amplification topology. Explicitly ranks message similarity as the weakest indicator, because people who agree say the same things. Requires an organic-explanation pass before any coordination finding."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - coordination
  - network-analysis
  - trust-and-safety
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, evidential, adversarial]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: indicator_scorecard
  user_role: [analyst, trust_and_safety, researcher, moderator]
  mode: [assess, audit, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
  - domain-psy-ops/influence-operations/psyops_inauthentic_account_signal_assessment.md
  - domain-psy-ops/influence-operations/psyops_astroturf_vs_organic_assessment.md
---

# Coordination Indicators

**Objective:** Assess whether a set of accounts, pages, or outlets is **coordinated** — acting under common direction — as opposed to **converging** because the participants independently believe similar things and inhabit the same information environment. The distinction is the hardest and most consequential call in influence analysis, and the evidence for it is structural rather than semantic. Coordination leaves traces in timing, infrastructure, and asset reuse. Agreement leaves traces in wording. Analysts who work from wording produce false positives at scale, because **organic convergence is the normal condition of any community with shared media.**

The indicators are therefore explicitly ranked by strength, and the weakest one — message similarity — is the one that most analyses lean on hardest. A finding of coordination requires at least one strong structural indicator; similarity alone caps the assessment at low confidence permanently, regardless of how striking it looks.

**When to use:**
- You have a cluster of accounts or outlets and need to assess coordination rigorously.
- Someone has asserted a coordinated campaign and you need to check whether the evidence supports it.
- You are preparing a trust-and-safety enforcement recommendation that must survive appeal.
- You need to explain to a non-technical audience why similar messaging is not proof of a campaign.

**When NOT to use:**
- You are assessing whether individual accounts are automated — use `psyops_inauthentic_account_signal_assessment.md`.
- You need the full five-axis operation assessment — use `psyops_influence_operation_analysis.md`.
- The question is specifically whether a movement's grassroots support is real — use `psyops_astroturf_vs_organic_assessment.md`.

**Audience:** Trust-and-safety analysts, platform integrity staff, researchers, moderators, and journalists assessing a suspected network.

---

## Inputs / Context

1. **The cluster.** Which accounts, pages, or outlets are in scope, and — critically — **how you selected them**. Selection method determines what you will find.
2. **The observation window.** Start and end dates, and whether the window was chosen before or after seeing the pattern.
3. **Timing data.** Post timestamps at the finest resolution available, with time zones stated.
4. **Infrastructure signals.** Shared domains, hosting, contact details, registration patterns, cross-linking, app or client fingerprints — whatever is actually observable to you.
5. **Content samples.** The messaging itself, plus any reused assets: identical images, identical typos, identical link shorteners, identical formatting artifacts.
6. **The baseline.** What a comparable *organic* community in this space looks like on the same measures. Without this, every finding is uncalibrated.

---

## Constraints

### Must
- Score indicators by **tier**: strong (shared infrastructure, identical asset reuse including replicated errors, synchronization at sub-minute resolution across many accounts, coordinated creation clustering), moderate (amplification topology inconsistent with organic spread, near-simultaneous cross-platform posting, engagement patterns decoupled from audience), weak (message similarity, shared hashtags, aligned viewpoints, posting the same links).
- Require **at least one strong indicator** for any coordination finding above low confidence.
- Establish a **baseline** from a comparable organic community before calling any pattern anomalous.
- State the **selection method** for the cluster and assess how much of the observed similarity it manufactured.
- Run the **organic-explanation pass**: for each indicator, the strongest account on which this arises without common direction.
- Distinguish **coordination from collusion from campaign**. Activists openly organizing are coordinated and entirely legitimate; the finding is about coordination, not wrongdoing.
- Note whether coordination is **disclosed or concealed** — the concealment is what makes it inauthentic, not the coordination itself.

### Must Not
- Treat message similarity as sufficient. It is the weakest indicator and the most abundant.
- Name private individuals as operatives, paid actors, or agents.
- Fabricate timestamps, infrastructure overlaps, registration dates, or engagement figures. Unobserved values are `[VERIFY]`.
- Infer coordination from shared political position. Agreement is not conspiracy, and this error targets ordinary people with unpopular views.
- Assume time-zone alignment without checking. Apparent synchronization frequently dissolves into "these people are awake at the same time."
- Present open, disclosed organizing as a covert finding. A union, a campaign, a fandom, and a brigading Discord are all coordinated; only some are concealing it.
- Recommend enforcement action on weak-tier indicators alone.

---

## Instructions

### Step 1 — Document the selection method
Write exactly how the cluster was assembled: a search term, a hashtag, a referral, an algorithmic recommendation. Then state what similarity that method guarantees you will find. A cluster gathered by searching a phrase will share that phrase; this is not evidence.

### Step 2 — Build the organic baseline
Identify a comparable community you have no reason to think coordinated, and measure the same indicators on it. Fandoms, hobby groups, and local-news communities all show striking timing and phrasing overlap.

### Step 3 — Score strong indicators
Shared infrastructure, identical asset reuse (especially replicated errors — a shared typo or an identical crop is far stronger than shared wording), sub-minute synchronization across many accounts, and account-creation clustering. Quantify each against the baseline.

### Step 4 — Score moderate indicators
Amplification topology: does spread look like organic diffusion through overlapping audiences, or like simultaneous injection from a flat set of unconnected accounts? Check engagement decoupling — accounts with reach unexplained by their audience.

### Step 5 — Score weak indicators and label them weak
Record message similarity, hashtags, shared links, and viewpoint alignment. Report them as context, and mark explicitly that they cannot carry a finding.

### Step 6 — Check time zones and platform mechanics
Convert all timestamps to a single zone and re-examine. Then account for platform artifacts: scheduling tools, cross-posting integrations, and feed algorithms that produce apparent synchronization from independent behavior.

### Step 7 — Run the organic-explanation pass
For each indicator that survived, write the strongest non-coordinated account. Shared media diet, a single viral source everyone saw, a scheduling tool the whole community uses, a platform recommendation surfacing the same content simultaneously.

### Step 8 — Adversarial check and finding
Argue this is an ordinary community that agrees with itself and you have found the shape of normal group behavior. Then state the finding, its confidence, whether any coordination found is disclosed or concealed, and what evidence would change it.

---

## False-Positive Prevention

1. **Similarity as proof.** The dominant failure. Shared talking points spread organically through media, group chats, and copy-paste; requiring structural evidence is the only defense.
2. **Selection artifact.** Finding a coordinated-looking cluster because you selected on the thing that makes it look coordinated. Always state the method and discount for it.
3. **No baseline.** Calling timing patterns anomalous without knowing what normal looks like. Organic communities are far more synchronized than intuition expects.
4. **Time-zone illusion.** Reading "everyone posted within the same two hours" as coordination when they share a waking day.
5. **Tooling mistaken for direction.** Scheduling apps, cross-posting integrations, and RSS automations produce clean synchronization with no coordinator.
6. **Disclosed organizing framed as covert.** Reporting an openly organized campaign as a hidden network. Concealment is the inauthenticity, not coordination.
7. **Enforcement on weak signals.** Recommending action on similarity, which produces exactly the wrongful takedowns that discredit integrity work.
8. **Person-level attribution.** Sliding from "these accounts show coordination indicators" to naming individuals as paid operatives.

---

## Output Format

```
# Coordination assessment — [cluster]

## Cluster and selection method
[Which accounts; exactly how selected; what similarity that method guarantees]

## Organic baseline
[Comparable uncoordinated community; same measures; what "normal" looks like here]

## Indicator scorecard
| Tier | Indicator | Observed | Baseline | Delta | Evidence pointer |
|---|---|---|---|---|---|
| Strong | Shared infrastructure | [obs] | [base] | [delta] | [pointer] |
| Strong | Identical asset / replicated error reuse | | | | |
| Strong | Sub-minute synchronization (n accounts) | | | | |
| Strong | Account-creation clustering | | | | |
| Moderate | Amplification topology | | | | |
| Moderate | Engagement decoupling | | | | |
| Weak | Message similarity — **cannot carry a finding** | | | | |
| Weak | Shared hashtags / links / viewpoint | | | | |

## Time zone and platform-mechanics correction
[Timestamps normalized; scheduling/cross-posting/algorithmic artifacts ruled in or out]

## Organic-explanation pass
| Surviving indicator | Strongest organic account | What would discriminate |
|---|---|---|

## Finding
[Coordinated (disclosed) / coordinated (concealed) / insufficient evidence — consistent with organic convergence]
**Confidence:** [low / moderate / high] — strong indicators present: [yes/no, which]

## What would change this
- Upward: [...]
- Downward: [...]

## Adversarial check
[The case that this is a normal community agreeing with itself]

## Unknowns
[All [VERIFY] items]
```

---

## Verification

- [ ] The selection method is documented and discounted for.
- [ ] An organic baseline was built and used to calibrate every indicator.
- [ ] Indicators are tiered, and message similarity is explicitly labeled as unable to carry a finding.
- [ ] No confidence above low is asserted without at least one strong structural indicator.
- [ ] Timestamps are normalized to one time zone, and platform/scheduling artifacts are ruled in or out.
- [ ] The organic-explanation pass covers every surviving indicator with a discriminating observation.
- [ ] Disclosed coordination is distinguished from concealed coordination, and legitimate organizing is not reported as covert.
- [ ] No individual is named as an operative or paid actor.
- [ ] No timestamp, infrastructure overlap, or metric was invented; unknowns are `[VERIFY]`.
- [ ] No enforcement recommendation rests on weak-tier indicators.
