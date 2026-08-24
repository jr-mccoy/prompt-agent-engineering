---
title: "Inauthentic Account Signals — Assessing Automation Without Accusing People"
category: psy-ops/influence-operations
description: "Assess behavioral signals of automation or identity misrepresentation on a set of accounts, while treating every alternative explanation — a heavy user, a scheduled feed, a non-native speaker, a marketer, a lonely person — as a live hypothesis. Built around the fact that 'bot' accusations are usually wrong and land on real people. Outputs account-level behavioral findings with confidence bands, never a person-level verdict."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - automation
  - trust-and-safety
  - false-positives
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, evidential, adversarial]
  stakes: high
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: single_domain
  collaboration: solo_or_team
  output_format: signal_assessment_with_alternatives
  user_role: [analyst, trust_and_safety, moderator, researcher]
  mode: [assess, audit, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-psy-ops/influence-operations/psyops_attribution_confidence_assessment.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
---

# Inauthentic Account Signal Assessment

**Objective:** Assess whether specific accounts show evidence of **automation** or **identity misrepresentation** — and do it under the assumption that you are probably looking at real people. This prompt carries the heaviest false-positive discipline in the domain for a specific reason: "bot" is the most casually thrown and most frequently wrong accusation in online discourse, and it lands overwhelmingly on real humans. Heavy posters, non-native English speakers, people with unusual sleep schedules, marketers using scheduling tools, and lonely people who post constantly all trip the popular heuristics. Being wrong here is not a neutral analytic error: it dismisses a real person's speech as machine output.

The assessment therefore produces **account-level behavioral findings with confidence bands**, never a person-level verdict, and it requires that every signal be paired with its most likely innocent explanation before it counts toward anything.

**When to use:**
- You need to assess specific accounts for automation as part of a larger integrity investigation.
- Someone has claimed a set of accounts are bots and you need to check it.
- You are building an enforcement recommendation that has to survive appeal and scrutiny.
- You want to talk someone out of a bot accusation using evidence.

**When NOT to use:**
- The question is coordination across a cluster rather than automation of individuals — use `psyops_coordinated_inauthentic_behavior_indicators.md`.
- You want to attribute a network to a sponsor — use `psyops_attribution_confidence_assessment.md`.
- You are simply annoyed by an account. That is not an analytic question, and this prompt will not help.

**Audience:** Trust-and-safety and platform integrity staff, moderators, researchers, and analysts who must justify a conclusion about specific accounts.

---

## Inputs / Context

1. **The accounts.** Identifiers as you will handle them, plus how they came to your attention — a report, a search, a cluster, or your own irritation.
2. **Observable behavior.** Posting cadence, timing distribution, content mix, interaction patterns, account age, profile completeness.
3. **What you can and cannot see.** Whether you have platform-side data (device, IP, registration, client) or only public surface signals. This bounds everything.
4. **The population context.** What ordinary accounts in this community look like on the same measures.
5. **The consequence.** What will happen if you conclude inauthenticity — a takedown, a report, a public claim — which sets the required confidence.

---

## Constraints

### Must
- Pair **every signal with its most likely innocent explanation**, written before the signal is scored.
- Distinguish the three separate questions: **is it automated**, **is it misrepresenting identity**, and **is it coordinated with others**. An account can be any combination, including automated and entirely legitimate.
- State the **observability bound** explicitly: public-surface analysis cannot establish automation, only behavior consistent with it.
- Use **confidence bands** on behavior, never binary bot/not-bot labels.
- Calibrate against the **population baseline** — heavy legitimate users are far more extreme than analysts expect.
- Set the **confidence threshold by consequence**: a public accusation requires materially more than an internal note.
- Explicitly consider the **non-native speaker, scheduling tool, brand account, and heavy user** explanations for any account flagged on language or cadence.
- Note that **disclosed automation is legitimate** — bots that identify as bots are not inauthentic.

### Must Not
- Label an account a bot. The finding is "behavior consistent with automation at X confidence," and the difference is not pedantry.
- Name, publish, or list account identifiers in a way that invites harassment of the account holder.
- Treat non-native or unusual English as an inauthenticity signal. This is the most discriminatory heuristic in common use and it targets immigrants and non-native speakers.
- Treat high volume, odd hours, a default avatar, a recent creation date, or a follower-ratio anomaly as sufficient individually. Each has an enormous legitimate population.
- Fabricate account metadata: creation dates, post counts, follower numbers, device or client fingerprints.
- Infer automation from **opinions held**. Believing something unpopular is not a bot signal, and treating it as one is a way of dismissing people.
- Recommend enforcement without stating the observability bound and the false-positive cost.

---

## Instructions

### Step 1 — State how the accounts came to your attention
If it was because they disagreed with you or annoyed you, record that plainly. It is the strongest predictor of a false positive in this analysis.

### Step 2 — Fix the observability bound
List what data you actually have. Public-surface only means you can assess behavioral consistency and nothing more; say so before analyzing.

### Step 3 — Build the population baseline
Sample ordinary accounts from the same community and measure cadence, timing spread, content mix, and account age. Establish what the top few percent of legitimate heavy users look like — that is your real comparison, not the median.

### Step 4 — Score cadence and timing
Posting volume, inter-post intervals, and the daily distribution. Look for the specific signatures automation produces: near-constant intervals, activity with no diurnal cycle at all, and bursts at exact clock boundaries. Note that scheduling tools produce the same pattern for legitimate users.

### Step 5 — Score content and interaction
Content mix, originality versus reshares, and whether interactions are responsive to what they reply to. Non-responsiveness is a stronger automation signal than volume, since it is harder for a human to fake and harder for a simple bot to avoid.

### Step 6 — Score identity signals separately
Profile provenance: reused stock or generated images, biography inconsistencies, claimed affiliations. Keep this separate from automation — a real person with a fake profile picture is a different finding from a script.

### Step 7 — Write the innocent explanation for every scored signal
Explicitly, one per signal. Then check whether any signal survives its innocent reading on its own. If none does, the assessment is "insufficient."

### Step 8 — Adversarial check and finding
Argue that every account here is a real person with an unusual posting habit. Then state findings per account with confidence bands, the observability bound, and — if recommending action — the false-positive cost of being wrong about this specific account.

---

## False-Positive Prevention

1. **Heavy user misread as bot.** The single most common error. Legitimate power users post at volumes and hours that look mechanical; the top percentile of normal is extreme.
2. **Language used as a signal.** Flagging non-native phrasing, translation artifacts, or unusual idiom. This heuristic discriminates against real people and must never contribute to a finding.
3. **Disagreement as a signal.** Assessing accounts because of what they argue. Opinions are not automation evidence, and this is how the accusation gets used to dismiss inconvenient speech.
4. **Scheduling mistaken for scripting.** Regular intervals from Buffer, Hootsuite, or a cross-post integration look identical to a bot on the surface.
5. **New account bias.** Treating recent creation as suspicious. Everyone's account was new once, and events drive genuine signup waves.
6. **Ratio heuristics.** Follower-following ratios and default avatars have enormous legitimate populations, especially among casual and older users.
7. **Observability overreach.** Asserting automation from public data alone, which cannot establish it. State the bound and stay inside it.
8. **Aggregation laundering.** Rolling weak per-account signals into a confident cluster-level claim. Weak signals do not become strong by being counted together across accounts.

---

## Output Format

```
# Account signal assessment

## How these accounts came to attention
[Report / search / cluster / analyst irritation — stated honestly]

## Observability bound
[Exactly what data is available; what conclusions are therefore unavailable]

## Population baseline
[Community norms + the top-percentile legitimate heavy user profile — the real comparison]

## Per-account assessment
| Account ref | Automation signals | Innocent explanation | Identity signals | Innocent explanation | Confidence (automation) | Confidence (identity misrep.) |
|---|---|---|---|---|---|---|
| A1 | [signal] | [most likely benign account] | [signal] | [benign account] | low | low |

## Signals that survive their innocent explanation
[Listed, or "none — assessment is insufficient"]

## Findings
[Per account, as behavior statements: "behavior consistent with automation, moderate confidence" —
never "is a bot." Disclosed automation noted as legitimate where present.]

## If action is recommended
- Threshold applied: [given the consequence]
- False-positive cost: [what happens to a real person if this account is wrongly actioned]

## Adversarial check
[The case that every one of these is a real person with unusual habits]

## Unknowns
[All [VERIFY] items — metadata not observable at this access level]
```

---

## Verification

- [ ] Every scored signal has a written innocent explanation, produced before scoring.
- [ ] No account is labeled a bot; findings are behavior statements with confidence bands.
- [ ] The observability bound is stated, and no conclusion exceeds it.
- [ ] The baseline includes top-percentile legitimate heavy users, not just the median.
- [ ] Language, phrasing, and non-native English contributed nothing to any finding.
- [ ] Opinions and viewpoints contributed nothing to any finding.
- [ ] Automation, identity misrepresentation, and coordination are assessed as three separate questions.
- [ ] Scheduling tools, brand accounts, and cross-posting integrations were considered for every cadence signal.
- [ ] No account metadata was invented; unknowns are `[VERIFY]`.
- [ ] If action is recommended, the false-positive cost to a real person is stated explicitly.
