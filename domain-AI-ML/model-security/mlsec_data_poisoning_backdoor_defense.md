---
title: "Data Poisoning and Backdoor Defense"
category: AI-ML/model-security
description: "Defend the training set against poisoning and backdoors by tracing every path bytes take into training, placing controls at the contribution boundary rather than only at the model, and separating detectable distribution shift from a patient campaign that stays under the gate."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - data-poisoning
  - backdoor
  - training-integrity
  - feedback-loop
  - provenance
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
  - domain-AI-ML/model-security/mlsec_ml_supply_chain_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
  - domain-AI-ML/production-monitoring/mlmonitor_feedback_loop_detection.md
---

# Data Poisoning and Backdoor Defense

**Objective:** Protect a model's training set from poisoning and backdoors by first tracing every path that lets bytes reach training, then placing controls at the contribution boundary rather than relying on post-hoc model inspection, and finally being explicit that gates catch distribution shift but not a patient campaign that stays beneath them.

**When to Use:**
- Any part of the training set is user-submitted, scraped, crowd-labelled, purchased, or fed by a production feedback loop.
- A model is retrained on a schedule from data that accumulates between runs.
- You are adopting a third-party dataset or a pretrained checkpoint whose training data you cannot inspect.

**When NOT to Use:**
- The training set is fixed, internally produced, and never re-derived — note that and stop; the threat needs a contribution path.
- The concern is label noise or ordinary data quality rather than an adversary — use `../data-for-ml/mldata_data_quality_audit.md`.
- The concern is the artifact rather than the data — use `mlsec_ml_supply_chain_audit.md`.

## Inputs / Context

- **Training-data inventory** — every source, with who can write to it and what review stands between them and the training set.
- **Retraining cadence and trigger** — scheduled, volume-based, or performance-triggered, and what is promoted automatically.
- **Feedback loop** — whether production predictions, user corrections, or downstream outcomes re-enter training, and with what delay.
- **Label pipeline** — who labels, whether labellers are anonymous or contracted, and what adjudication exists.
- **Attacker incentive** — the specific prediction an attacker would want changed, which distinguishes targeted poisoning from indiscriminate degradation.
- **Existing gates** — any drift, quality, or eval gate already standing between a retrain and promotion.

## Constraints

**Must:**
- Enumerate every contribution path before proposing a control; a defense at the model cannot compensate for an unmonitored write path.
- Distinguish the three goals explicitly — **availability poisoning** (degrade overall), **targeted poisoning** (change specific predictions), **backdoor** (implant a trigger) — because they have different detection signatures and different controls.
- Treat the production feedback loop as a first-class contribution path whenever predictions or user corrections re-enter training.
- State for every detection method what it would miss, especially a slow campaign that stays below a drift threshold.
- Require that any promotion gate compares against a **held-out set the contributor cannot influence**.

**Must Not:**
- Assert poisoning-rate thresholds, backdoor-persistence findings, or dataset-contamination figures from memory; mark any needed figure `[verify against a primary source]`.
- Treat overall accuracy on the usual validation set as a poisoning check — targeted poisoning and backdoors are designed to leave it intact.
- Recommend "review the data" without specifying what the reviewer looks for and at what sampling rate.
- Describe a backdoor as absent because a trigger scan found nothing; scans cover the trigger classes they model.
- Generate trigger patterns, poison-crafting procedures, or any content that would help mount the attack.

**Instructions:**

1. **Map contribution paths.** List every route by which bytes enter training: direct upload, scraped corpus, purchased dataset, crowd labelling, partner feed, production feedback, and human correction. For each, record who can write, at what volume, with what identity assurance, and what review exists. Paths with no review are the finding.

2. **Set the attacker goal.** From the incentive, decide which of the three goals is plausible here. An attacker who wants one specific applicant approved is running a different campaign from one who wants the model generally worse, and you cannot defend both with one control.

3. **Score each path by leverage.** How much of the training set can one contributor influence, how identifiable are they, and how long does their contribution persist across retrains? Leverage, not volume, is what makes a path dangerous.

4. **Place contribution-boundary controls.** For the high-leverage paths: identity and rate limits per contributor, per-contributor caps on training-set share, quarantine periods before contributed data becomes eligible, and provenance tags carried through to the training manifest so any example can be traced back.

5. **Design the promotion gate.** Between retrain and deployment: compare against a **clean held-out set the contributor cannot reach**; check per-slice deltas rather than aggregate; check that no cohort's contribution moved a slice disproportionately. State the threshold and say where the threshold came from — historical retrain deltas, not a default.

6. **Add goal-specific detection.** Availability poisoning shows as aggregate degradation. Targeted poisoning shows as a slice or cohort delta with aggregate stable. Backdoors show, if at all, as anomalous behaviour under trigger-class scanning or as unusual influence concentrated in few examples. Name what each check covers and what it does not.

7. **Handle the feedback loop specifically.** If production data re-enters training, the model's own errors become tomorrow's labels. Specify the human adjudication rate, the delay before feedback is eligible, and the check that a cohort is not disproportionately shaping the next retrain.

8. **State the undetectable band.** Be explicit about the campaign that stays under every gate: small share, patient, spread across identities. Say what bounds the damage when detection fails — rollback capability, retrain-from-checkpoint, model versioning, and the ability to recompute the training manifest without a suspect cohort.

9. **Define incident response.** If poisoning is suspected: which model versions are implicated, how a suspect cohort is excluded, how quickly a clean retrain can be produced, and what is served in the interim.

**Output Format:**

A markdown defense plan:
- **Contribution Path Map** — table: Path | Who can write | Volume | Identity assurance | Existing review | Leverage.
- **Attacker Goal** — which of the three, and the incentive behind it.
- **Boundary Controls** — per high-leverage path, with the control and its cost.
- **Promotion Gate** — comparison set, per-slice thresholds, and where the thresholds came from.
- **Detection Coverage** — table: Check | Goal it detects | What it misses.
- **Feedback-Loop Controls** — adjudication rate, eligibility delay, cohort-share check.
- **Undetectable Band** — the campaign that passes every gate, and what bounds its damage.
- **Incident Response** — implicated versions, cohort exclusion, clean-retrain path, interim serving.

## Verification

- [ ] Every contribution path is listed, including the production feedback loop.
- [ ] The attacker goal is named, and controls are matched to that goal rather than generic.
- [ ] Paths are scored by leverage, not by raw volume.
- [ ] The promotion gate compares against a held-out set the contributor cannot influence.
- [ ] Per-slice deltas are gated, not just aggregate accuracy.
- [ ] Every detection method states what it misses.
- [ ] The undetectable band is described explicitly, with what bounds its damage.
- [ ] Gate thresholds are justified from historical deltas, not defaults.
- [ ] No poisoning rates, persistence findings, or contamination figures are asserted from memory.
- [ ] No trigger patterns or poison-crafting procedures appear.

## False-Positive Prevention

❌ **DON'T:**
- Conclude the training set is safe because aggregate validation accuracy is unchanged — that is precisely what targeted poisoning and backdoors preserve.
- Omit the production feedback loop from the path map because it is "our own data"; it is whatever the model plus its users produced, and users include the attacker.
- Score a path as low-risk because contributions are small, when one contributor can supply a large share of a rare slice.
- Claim a backdoor scan cleared the model — it cleared the trigger classes it models, which is a narrower statement.
- Set a drift gate at a round default and treat passing it as evidence; a threshold with no basis in your own retrain history is decoration.
- Present detection as the whole defense when the patient low-share campaign is undetectable by construction.

✅ **DO:**
- Trace every write path to the identity behind it and the review in front of it, and treat unreviewed paths as the primary finding.
- Match controls to the specific attacker goal the incentive supports.
- Score leverage as the share of a *slice* a contributor can influence, not the share of the whole set.
- Gate on per-slice and per-cohort deltas against a contributor-inaccessible held-out set.
- State each check's blind spot next to the check.
- Plan for undetected poisoning: provenance tags, cohort-excludable retrains, and a rollback path that does not require re-collecting data.

## Example Output

```markdown
## Poisoning Defense: Support-Ticket Intent Classifier (quarterly retrain)
Routes tickets to queues. Retrained quarterly on tickets plus agent corrections.

### Contribution Path Map
| Path | Who can write | Volume | Identity assurance | Existing review | Leverage |
|---|---|---|---|---|---|
| Customer ticket text | any account holder | ~40k/qtr | email-verified account | **none** | **High** — free text, no review |
| Agent label correction | 60 contracted agents | ~3k/qtr | named employee | spot-check ~2% | Medium |
| Historical archive | frozen | 500k | n/a | n/a | None (frozen) |
| Purchased intent corpus | vendor | 20k, one-off | contract | one-time sampling | Medium (one-off) |

### Attacker Goal
**Targeted.** The incentive is routing: getting abuse reports classified as `billing` delays
review by roughly a queue cycle. Nobody benefits from the classifier being generally worse,
so availability poisoning is not the campaign to defend against first.

### Boundary Controls
- **Customer ticket text (High):** cap any single account's contribution to ≤0.1% of any
  intent class per retrain; require account age ≥30 days for training eligibility; carry an
  `account_id` provenance tag into the training manifest. Cost: manifest schema change plus a
  filter step; no labelling burden.
- **Agent corrections (Medium):** raise adjudication from 2% to 10% on corrections that *move*
  a label into `billing` or `abuse`, the two classes the incentive touches. Cost: ~120
  adjudications/qtr.
- **Purchased corpus (Medium):** treat as a fixed cohort with its own provenance tag so it can
  be excluded from a retrain without re-collecting anything else.

### Promotion Gate
Compare the retrained model against a **held-out set drawn from the frozen archive** — no
customer-contributed example from the current quarter is eligible, so a contributor cannot
influence the yardstick. Gate on per-class F1 delta and, separately, on the `abuse → billing`
confusion cell. Thresholds set at 2× the largest delta observed across the last six retrains
`[verify: compute these from your own retrain history before first use]`, not at a round number.

### Detection Coverage
| Check | Detects | Misses |
|---|---|---|
| Aggregate accuracy vs held-out | availability poisoning | targeted and backdoor by design |
| Per-class F1 delta | targeted poisoning above the gate | slow campaigns below the threshold |
| `abuse→billing` cell monitor | the specific incentivized flip | any other targeted flip |
| Per-account contribution share | one account with outsized leverage | a coordinated set of accounts |
| Trigger-class scan on text | the trigger families scanned | any trigger family not modelled |

### Feedback-Loop Controls
Agent corrections are the loop. Eligibility delay: corrections become training-eligible after
one full quarter, so a burst is visible before it can act. Cohort-share check: no single agent
may account for more than 5% of corrections in any class. Adjudication as above.

### Undetectable Band
A patient attacker using 40 aged accounts, each contributing under the 0.1% cap, spread across
two quarters, stays under every gate here. What bounds the damage is not detection: it is that
provenance tags make a cohort-excluded retrain possible within one cycle, the archive held-out
set stays clean, and routing errors are reversible by the agent who receives the ticket.

### Incident Response
1. Identify implicated model versions from the training manifest by provenance tag.
2. Exclude the suspect `account_id` cohort and retrain from the last clean manifest.
3. Interim: revert to the previous quarter's model — retained for exactly this reason.
4. Re-run the promotion gate against the archive held-out set before restoring.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** contribution path × attacker goal × leverage is the analysis grid.
- **ST-02 (Structured Sequential Instructions):** path mapping precedes control placement, so no control is proposed for an untraced path.
- **CM-02 (Constraint Specification):** the contributor-inaccessible held-out set and the state-what-it-misses rule are hard constraints.
- **QA-12 (False Positives Identification):** separates a real detection signal from an aggregate metric that poisoning is designed to preserve.
- **DS-06 (Prioritization and Severity Guidance):** leverage scoring ranks which paths get controls first.

**Related Prompts:**
- `mlsec_ml_threat_model.md` — establishes whether poisoning is a live threat before this depth is worth it.
- `mlsec_ml_supply_chain_audit.md` — the artifact-side counterpart when the weights, not the data, are the risk.
- `../data-for-ml/mldata_data_quality_audit.md` — non-adversarial data problems, which look similar and are far more common.
- `../production-monitoring/mlmonitor_feedback_loop_detection.md` — detecting that the model is shaping its own training data at all.
