---
title: "Federated Learning Governance"
category: AI-ML/responsible-ai-governance
description: "Govern a federated learning deployment — settling what federation does and does not protect, who is accountable when no one holds the data, how participant heterogeneity and dropout are handled, and what a malicious or careless participant can do to the shared model."
techniques:
  - RT-02
  - CM-02
  - DS-06
  - QA-12
  - ST-02
difficulty: advanced
tags:
  - federated-learning
  - governance
  - cross-silo
  - participant-accountability
  - update-integrity
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_privacy_technique_selection.md
  - domain-AI-ML/responsible-ai-governance/rai_differential_privacy_design.md
  - domain-AI-ML/model-security/mlsec_data_poisoning_backdoor_defense.md
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
---

# Federated Learning Governance

**Objective:** Establish the governance a federated deployment needs but rarely gets — an explicit statement of what federation protects and what it leaves untouched, named accountability for a model no single party holds the data for, handling for heterogeneity and dropout, and controls against a participant who sends bad updates.

**When to Use:**
- Standing up cross-silo federated learning between organizations, or cross-device federation across user endpoints.
- A federated deployment exists and nobody can say who owns the model, who approves a release, or what happens when a participant leaves.
- A privacy review has accepted federation as the answer and you need to check what it actually answered.

**When NOT to Use:**
- The question is whether federation is the right technique — use `rai_privacy_technique_selection.md`.
- The concern is what the trained model reveals about individuals — federation does not address that; use `rai_differential_privacy_design.md`.
- The deployment is single-organization distributed training, which is an infrastructure question rather than a governance one.

## Inputs / Context

- **Participants** — who they are, their legal relationship, and whether they are peers or a coordinator plus clients.
- **Why federation was chosen** — the specific constraint (regulatory, contractual, bandwidth, or trust) that prevents centralization.
- **Data heterogeneity** — how differently distributed the participants' data is, and whether any single participant dominates by volume.
- **Trust model** — whether participants are trusted, semi-trusted, or potentially adversarial, and whether the coordinator is trusted.
- **Availability profile** — expected dropout, connectivity, and whether participation is voluntary per round.
- **Downstream use** — who gets the trained model, and what they may do with it.

## Constraints

**Must:**
- State explicitly, near the top, that federation protects **data movement** and does not by itself bound what the trained model reveals about individuals. Every governance decision downstream depends on that distinction being clear.
- Name a single accountable owner for the shared model — for releases, incidents, and withdrawal — since the natural failure of federation is that everyone contributed and nobody owns it.
- Specify participant exit: what happens to the model when a participant withdraws, whether their contribution can or must be removed, and what is promised contractually.
- Treat participant updates as an integrity surface, with an explicit position on update validation and on a dominant or malicious participant.
- Define contribution and benefit: what each participant gives and gets, and how a participant with little data is treated.

**Must Not:**
- Describe federation as making the deployment private; that claim requires a separate mechanism and its own accounting.
- Assert convergence behaviour, communication-cost figures, or attack-efficacy results from memory; mark any needed figure `[verify against a primary source]` or `[measure in your setting]`.
- Assume model updates are non-sensitive — updates are derived from data and can carry information about it; state the position taken rather than glossing over it.
- Promise removal of a participant's contribution from an already-trained model without stating how, since this is genuinely hard and frequently promised carelessly.
- Treat the coordinator as neutral infrastructure when it sees every update.

**Instructions:**

1. **Record why centralization is impossible.** The specific constraint, in the words of whoever owns it. This bounds everything: a regulatory prohibition and a bandwidth limit lead to different governance.

2. **State the protection boundary plainly.** Federation prevents raw data centralization. It does not prevent the model from memorizing, does not prevent inference from updates, and does not anonymize anything. Write this where a stakeholder will read it, because it is routinely misunderstood as a privacy guarantee.

3. **Assign accountability.** Name the owner of: model releases, incident response, participant admission and removal, and the decision to retire the model. If ownership is a committee, name who signs. A federated model with no owner is the default outcome.

4. **Define the participation contract.** What each participant provides (data characteristics, minimum rounds, availability), what they receive (the model, under what licence, for what use), and what they may not do (redistribute, derive, or extract). State how a participant with much less data is treated, since equal benefit from unequal contribution needs to be an explicit choice.

5. **Address update integrity.** Decide the position on: validating updates before aggregation, bounding any single participant's influence per round, detecting anomalous updates, and what happens when one is found. Note that a participant contributing most of the data has structural influence over the model regardless of protocol — that is a governance question, not a technical one.

6. **Handle heterogeneity and fairness across participants.** Non-identically distributed data means the global model can serve some participants much better than others. Require per-participant evaluation, and define the floor below which a participant is entitled to raise an objection.

7. **Handle dropout and availability.** What happens when a participant misses rounds, leaves mid-training, or rejoins. State whether the model is valid with partial participation and what is disclosed about who participated.

8. **Specify exit and deletion.** On withdrawal: does the model continue to include their contribution, is retraining required, and what was promised? Answer honestly — removing a past contribution generally requires retraining from a checkpoint that predates it, and if that is not feasible, the contract must not promise it.

9. **Decide what the coordinator sees.** The coordinator observes every update. State whether that is acceptable, what it is permitted to log and retain, and whether secure aggregation is required.

10. **Set the review cadence.** When governance is revisited: participant changes, distribution shift, or a scheduled interval.

**Output Format:**

A markdown governance document:
- **Why Federated** — the constraint preventing centralization, and who owns it.
- **Protection Boundary** — what federation does and does not do, stated plainly.
- **Accountability** — named owners for release, incident, admission, retirement.
- **Participation Contract** — table: Participant | Provides | Receives | Restrictions.
- **Update Integrity** — validation, influence bounds, anomaly handling, dominance position.
- **Heterogeneity & Per-Participant Fairness** — evaluation requirement and the objection floor.
- **Dropout & Availability** — partial-participation validity and disclosure.
- **Exit & Deletion** — what is promised, and how it would actually be done.
- **Coordinator Position** — what it sees, logs, retains; secure-aggregation decision.
- **Review Cadence** — triggers and interval.

## Verification

- [ ] The protection boundary states that federation does not bound what the model reveals.
- [ ] A single accountable owner is named for releases, incidents, admission, and retirement.
- [ ] The participation contract states what unequal contributors give and receive.
- [ ] A position on update integrity and on a dominant participant is recorded.
- [ ] Per-participant evaluation is required, with a stated objection floor.
- [ ] Dropout behaviour and partial-participation validity are defined.
- [ ] Exit and deletion are answered honestly, including whether retraining is required.
- [ ] The coordinator's visibility is stated, with a secure-aggregation decision.
- [ ] No convergence, cost, or attack figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Let the deployment be described as private because the data never moves — that sentence has misled more federated projects than any other, and the model can still leak its training records.
- Leave the model unowned because it is shared; "everyone contributed" reliably becomes "nobody is accountable" at the first incident.
- Treat updates as safe to log indefinitely because they are gradients rather than data; they are derived from data.
- Promise a withdrawing participant that their contribution will be removed without knowing whether retraining from a pre-contribution checkpoint is feasible.
- Report only global model performance when participants' data distributions differ — the global average can hide a participant the model does not serve at all.
- Assume the protocol neutralizes a participant who supplies most of the data; volume is structural influence.

✅ **DO:**
- State the protection boundary prominently and in plain language, before any stakeholder infers a privacy guarantee.
- Name a signing owner for each governance decision.
- Record what unequal contributors give and receive as a deliberate, reviewable choice.
- Require per-participant evaluation and give participants a defined basis to object.
- Answer exit honestly, including "retraining would be required and here is what that costs".
- Decide explicitly what the coordinator may see and retain, rather than letting it default to everything.

## Example Output

```markdown
## Federated Learning Governance: Three-Hospital Sepsis Model

### Why Federated
Patient records cannot leave each hospital's environment under the sites' data-sharing
position, as stated by each site's data protection officer. Bandwidth is not the constraint;
the prohibition is. Owner of that constraint: each site's DPO, jointly.

### Protection Boundary
Federation means **raw records never leave a site**. It does **not** mean the trained model is
private: the shared model can memorize, and model updates are derived from patient data.
Patient-level protection in this deployment comes from the differential privacy design, not
from federation. Anyone describing this system as "private because it is federated" is
describing something we have not built.

### Accountability
| Decision | Owner |
|---|---|
| Model release to sites | Joint clinical governance board; signed by the chair |
| Incident response | Site A's ML platform lead (rotating annually) |
| Participant admission / removal | Joint board, unanimous |
| Model retirement | Joint board; any site may force retirement |

### Participation Contract
| Participant | Provides | Receives | Restrictions |
|---|---|---|---|
| Site A (~62% of episodes) | ≥8 of 10 rounds; ICU + ward data | full model | no redistribution, no derivative training |
| Site B (~26%) | ≥8 of 10 rounds; ward only | full model | same |
| Site C (~12%) | ≥6 of 10 rounds; ward only | full model | same |

Site C receives the same model despite contributing least. That is a deliberate choice — the
model is worth more to the smallest site and the collaboration would not exist otherwise — and
it is recorded here so it is not relitigated informally.

### Update Integrity
Trust model: participants are semi-trusted — contractually bound, not adversarial, but capable
of error. Controls: update-norm bounds per round; per-round contribution capped so no site
exceeds a fixed share regardless of data volume; anomalous-update detection with the round
halted and the site contacted, never silently dropped.
**Dominance:** Site A holds ~62% of episodes. Per-round caps limit its influence in any single
round but not its cumulative structural influence over what the model learns. This is a
governance fact, not a bug to be engineered away, and the joint board reviews it annually
against per-site performance.

### Heterogeneity & Per-Participant Fairness
Sites B and C are ward-only; Site A includes ICU. The global model risks fitting A's case mix.
**Required:** every release reports AUC per site, not pooled. **Objection floor:** any site
whose AUC falls more than 0.03 below its own site-local baseline model may block the release.
A federated model that serves a site worse than that site's own model is not worth adopting.

### Dropout & Availability
Rounds proceed with ≥2 of 3 sites. A site missing rounds continues to receive the model. Below
2 sites, training pauses rather than continuing bilaterally — a two-site model presented as the
three-site model would misrepresent its provenance. Participation per round is disclosed to all
sites in the release record.

### Exit & Deletion
On withdrawal, a site's past contributions **remain embedded** in any model already trained.
Removing them requires retraining from a checkpoint predating their first contributed round,
which for a founding site means retraining from scratch — roughly a full training cycle.
The contract therefore promises: no further use of their data in future rounds; retraining from
scratch on request, at the requesting site's cost, with a stated lead time. It does **not**
promise instant removal, because that would be a promise we could not keep.

### Coordinator Position
The coordinator is hosted by Site A, which also participates — so it is not neutral
infrastructure and is not described as such. It sees every per-site update. **Secure
aggregation is required**, so the coordinator observes only the aggregate. Retention: aggregate
updates for 90 days for debugging; per-site raw updates are not retained at all.

### Review Cadence
Annually, and on any of: a participant joining or leaving, a site's case mix shifting materially,
or any release blocked under the objection floor.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** participant × contribution × trust × benefit is the governance grid.
- **CM-02 (Constraint Specification):** the protection-boundary statement and the honest-exit rule are hard constraints on what may be promised.
- **DS-06 (Prioritization and Severity Guidance):** the objection floor and dominance review rank which governance risks get board attention.
- **QA-12 (False Positives Identification):** rejects the standard misreading of federation as a privacy guarantee.
- **ST-02 (Structured Sequential Instructions):** protection boundary and accountability are settled before operational detail.

**Related Prompts:**
- `rai_privacy_technique_selection.md` — establishes what federation was chosen to solve.
- `rai_differential_privacy_design.md` — supplies the protection federation does not.
- `../model-security/mlsec_data_poisoning_backdoor_defense.md` — a participant sending malicious updates is a poisoning problem.
- `rai_governance_framework_design.md` — where this document sits in the organization's wider governance.
