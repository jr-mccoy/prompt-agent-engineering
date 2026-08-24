---
title: "Influence Operation Analysis — Actors, Behavior, Content, Degree, Effect"
category: psy-ops/influence-operations
description: "Assess whether observed activity constitutes a coordinated influence operation, using the ABCDE axes (actors, behavior, content, degree, effect) analyzed separately so that a striking finding on one axis cannot carry the others. Produces a confidence-graded assessment with a mandatory alternative-explanation pass, and treats 'insufficient evidence — this looks organic' as a first-class result. Counters the field's dominant failure mode: inferring a campaign from content you dislike."
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
  - influence-operations
  - disinformation
  - attribution
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, adversarial, evidential, abductive]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: confidence_graded_assessment
  user_role: [analyst, researcher, trust_and_safety, communications, individual]
  mode: [assess, audit, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-psy-ops/influence-operations/psyops_attribution_confidence_assessment.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
---

# Influence Operation Analysis

**Objective:** Determine, from evidence you can actually point at, whether a body of observed activity is a coordinated influence operation — and if so, what kind, run how, at what scale, to what effect. The analysis runs on five axes held deliberately apart: **actors** (who, and are they who they claim), **behavior** (what was done, and is it authentic), **content** (what is being said, and is it true), **degree** (how big, really), and **effect** (did anything change). Separating them is the whole method, because the characteristic analytic error is letting one vivid axis carry the rest — most commonly inferring coordinated actors from content the analyst finds objectionable. False content spread sincerely is not an operation. Coordinated behavior promoting true content still is one. The axes are independent and must be scored independently.

This prompt produces an **assessment**, not a verdict and not a campaign. It grades confidence explicitly, runs a mandatory alternative-explanation pass before concluding, and returns "insufficient evidence — consistent with organic activity" as a legitimate, common, and often correct answer.

**When to use:**
- You have observed a cluster of accounts, outlets, or messaging that looks coordinated and need to assess it rigorously.
- A claim or narrative is spreading and you need to know whether it is being pushed or simply catching on.
- You are documenting suspected inauthentic activity for a platform, editor, regulator, or research write-up.
- You need to talk someone down from — or up to — a conclusion about a campaign, using evidence rather than impression.

**When NOT to use:**
- You are analyzing a single artifact rather than a pattern — use `../technique-analysis/psyops_propaganda_technique_identification.md`.
- You already accept an operation exists and only need attribution graded — use `psyops_attribution_confidence_assessment.md`.
- The question is whether *specific accounts* are automated — use `psyops_inauthentic_account_signal_assessment.md`.
- You want general evidence-quality or source-credibility discipline with no influence-operations framing — use `domain-reasoning-craft/epistemic/`.
- You want to build or run an operation. Nothing here supports that; see this domain's README.

**Audience:** Open-source analysts, trust-and-safety and platform integrity staff, journalists, researchers, communications teams, and informed individuals assessing something they have observed themselves.

---

## Inputs / Context

1. **The observation.** What you actually saw, described before interpretation: accounts, posts, outlets, ads, timing, volumes. Distinguish what you observed directly from what someone reported to you.
2. **The evidence you hold.** Links, archived copies, screenshots, timestamps, exported datasets, platform disclosures. Note explicitly which evidence you have retained versus recall.
3. **The time window.** When it started, when you noticed, and whether you are looking at a live or historical pattern.
4. **The claim or narrative at issue.** What is being asserted, and — separately — whether you know it to be true, false, or unverified.
5. **The affected audience or target.** Who is meant to be reached, and who you observed actually reached.
6. **Your own position.** Whether you, your employer, or your community are a party to the dispute. This is an input because it changes the error you are most likely to make.
7. **Prior public reporting.** Any existing platform disclosure, research, or journalism on this cluster — and whether you have verified it or are relying on it.

---

## Constraints

### Must
- Score the five axes **independently**. Record findings on actors, behavior, content, degree, and effect in separate sections before forming any overall judgment.
- Attach every finding to **specific, retained evidence**. A finding with no evidence pointer is a hypothesis and must be labeled one.
- Run the **alternative-explanation pass** before concluding: for each axis, state the strongest innocent explanation for what was observed, and say what evidence would distinguish it.
- Grade overall confidence as **low / moderate / high** with the basis stated, and grade each axis separately.
- Treat **"insufficient evidence — consistent with organic activity"** as a valid, complete output. Reaching it is a success.
- Distinguish **inauthentic behavior** (the actual signature of an operation) from **disagreeable content** (which is not).
- State **what would change the assessment** — the specific observation that would move it up or down a confidence band.
- Separate **reach** from **effect**. Impressions are not persuasion; virality is not belief change.

### Must Not
- Name a private individual as a covert operative, agent, or paid actor. Assessments attach to accounts, behaviors, and content — not to people's hidden loyalties.
- Infer coordination from **content similarity alone**. People who believe the same thing say similar things; shared talking points travel organically through ordinary media.
- Fabricate any handle, follower count, engagement figure, posting timestamp, funding trail, or prior report. Unknown values are `[VERIFY]` and stay that way.
- Assert attribution to a state, party, company, or named group unless the evidence independently supports it. Beneficiary is not perpetrator; "who gains" is a hypothesis generator, never a finding.
- Let the offensiveness or falsity of the content raise the assessed likelihood of coordination. They are different axes.
- Produce messaging, personas, account content, or targeting guidance of any kind — including as an "illustration of what they would do."
- Treat platform enforcement, media reporting, or a prior researcher's claim as established fact without saying you are relying on it unverified.

---

## Instructions

### Step 1 — Restate the observation before interpreting it
Write what was observed in flat descriptive terms, stripped of the words "campaign," "bot," "coordinated," and "op." If the description collapses without those words, that is a finding about the evidence.

### Step 2 — Inventory and grade the evidence
List each piece of evidence, whether you retained it, and its quality. Mark anything you are relying on secondhand. Archive what is still live before it disappears.

### Step 3 — Axis A: Actors
Who is visibly involved, and is there evidence they are not who they present as? Look for account provenance, creation clustering, recycled identities, undisclosed affiliation. Absence of evidence about actors is extremely common — record it as absence, not as concealment.

### Step 4 — Axis B: Behavior
What was done, and is the *behavior* authentic regardless of content? Timing patterns, cross-platform synchronization, posting cadence, amplification structure, engagement asymmetries. This axis carries the most diagnostic weight and deserves the most evidence.

### Step 5 — Axis C: Content
What is asserted, and is it true, false, misleading, or unverified? Score truth separately from coordination. Note deceptive presentation (fabricated media, decontextualized imagery, impersonation) as distinct from disagreeable opinion.

### Step 6 — Axis D: Degree
How large is it actually? Distinguish account count from post count from reach from unique humans exposed. Correct for the inflation that makes small clusters look large: repetition, bot-inflated metrics, and the analyst's own sampling.

### Step 7 — Axis E: Effect
What, if anything, changed? Belief, behavior, coverage, policy, market, or nothing measurable. Effect is the least-evidenced axis in almost every real case; say so when it is unmeasured rather than inferring it from reach.

### Step 8 — Alternative-explanation pass (mandatory)
For each axis, write the strongest innocent explanation: organic convergence, a shared media diet, a genuine grassroots reaction, commercial spam, ordinary partisan messaging, or your own sampling bias. Then state the observation that would discriminate between the innocent and the coordinated reading. If nothing would discriminate, your confidence is capped at low.

### Step 9 — Adversarial check
Argue the case that there is no operation here and you have pattern-matched noise. Ask specifically: would I have run this analysis if I agreed with the content? If the answer is no, restate the assessment. Then set overall confidence and write what would change it.

---

## False-Positive Prevention

1. **Content-to-actor leap.** Concluding coordinated actors because the content is false, ugly, or hostile. Falsity is Axis C; coordination is Axis B. Sincere people spread false things at enormous scale, unpaid.
2. **Similarity mistaken for coordination.** Treating repeated phrasing as proof of a shared script. Talking points propagate organically through partisan media, group chats, and copy-paste culture. Require timing or structural evidence, not wording alone.
3. **Beneficiary reasoning.** "Who benefits" treated as evidence of who acted. It generates hypotheses and nothing else; the obvious beneficiary is often a bystander and is sometimes the target.
4. **Reach read as effect.** Converting impressions into persuasion. Most exposure changes nothing, most of the reach is inside an already-agreeing audience, and effect is usually unmeasured.
5. **Scale inflation.** Counting posts as people, or a loud cluster as a movement. A few dozen accounts posting constantly can look like thousands. Always resolve to unique accounts and unique humans reached.
6. **Sampling artifact.** Finding a cluster because you searched terms that would only return that cluster. Your search strategy shaped the dataset; state it and test it against a neutral sample.
7. **Absence read as concealment.** Treating missing actor information as evidence of a sophisticated adversary. Most missing information is missing because open-source data is thin, not because it was hidden.
8. **Escalation by repetition.** Each retelling of the assessment losing a hedge until "possible coordination, low confidence" becomes "a documented operation." Confidence must be restated at every hop, and the hedges are part of the finding.

---

## Output Format

```
# Influence operation assessment — [subject]

## Observation (pre-interpretation)
[What was seen, described without campaign vocabulary]

## Evidence inventory
| Evidence | Retained? | Direct/secondhand | Quality |
|---|---|---|---|
| [item] | yes/no | direct | strong/moderate/weak |

## Axis findings
| Axis | Finding | Evidence pointer | Confidence |
|---|---|---|---|
| A — Actors | [finding or "no evidence available"] | [pointer] | low/mod/high |
| B — Behavior | [finding] | [pointer] | low/mod/high |
| C — Content | [true / false / misleading / unverified + deceptive presentation] | [pointer] | low/mod/high |
| D — Degree | [unique accounts / posts / est. reach / est. humans] | [pointer] | low/mod/high |
| E — Effect | [measured change, or "unmeasured"] | [pointer] | low/mod/high |

## Alternative explanations (mandatory)
| Axis | Strongest innocent explanation | Discriminating observation |
|---|---|---|
| [axis] | [innocent reading] | [what would tell them apart] |

## Assessment
[One paragraph. Must be one of: coordinated inauthentic activity assessed at X confidence /
authentic activity with deceptive content / insufficient evidence — consistent with organic activity.]

**Overall confidence:** [low / moderate / high] — basis: [what drives it]

## Attribution
[Only if independently supported. Otherwise: "Not assessed — evidence does not support attribution."]

## What would change this assessment
- Upward: [specific observation]
- Downward: [specific observation]

## Adversarial check
[The case that this is noise, and my answer to it — including the "would I have looked if I agreed?" test]

## Unknowns
[Everything marked [VERIFY], listed and left unresolved]
```

---

## Verification

- [ ] The five axes are scored separately, each with its own evidence pointer and confidence grade.
- [ ] No finding rests on content similarity or content falsity alone.
- [ ] The alternative-explanation pass is present for every axis, with a discriminating observation named.
- [ ] Overall confidence is stated with its basis, and no hedge has been dropped between the axis findings and the assessment.
- [ ] Reach and effect are reported separately; unmeasured effect is labeled unmeasured rather than inferred.
- [ ] Degree resolves to unique accounts and estimated unique humans, not raw post counts.
- [ ] No private individual is named as a covert operative; no attribution is asserted beyond the evidence.
- [ ] Every unknown is marked `[VERIFY]`; no handle, metric, date, or prior report has been invented or filled in plausibly.
- [ ] The adversarial check was run, including the "would I have looked if I agreed with the content?" test.
- [ ] "Insufficient evidence" was available as an outcome and was not avoided for being unsatisfying.
