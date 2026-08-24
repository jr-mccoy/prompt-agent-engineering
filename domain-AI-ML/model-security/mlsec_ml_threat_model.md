---
title: "ML System Threat Model"
category: AI-ML/model-security
description: "Build a defensive threat model for a deployed ML model by walking a six-category attack taxonomy across the training, artifact, and inference surfaces, judging applicability from the model's actual exposure, and attaching a mitigation with its own detection signal."
techniques:
  - RT-02
  - DS-06
  - CM-02
  - QA-12
  - AG-44
difficulty: advanced
tags:
  - threat-model
  - attack-surface
  - adversarial-ml
  - model-security
  - defensive-security
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_adversarial_robustness_assessment.md
  - domain-AI-ML/model-security/mlsec_data_poisoning_backdoor_defense.md
  - domain-AI-ML/model-security/mlsec_secure_inference_endpoint_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_agentic_threat_model.md
---

# ML System Threat Model

**Objective:** Produce a defensive threat model for a specific ML model in a specific deployment — walking a six-category taxonomy across the training, artifact, and inference surfaces, deciding each threat's applicability from what an attacker can actually reach, scoring exposure and impact, and attaching each applicable threat one mitigation plus the signal that would tell you the mitigation failed.

**When to Use:**
- Before exposing a model through an API, a product surface, or a partner integration.
- When a model is trained on data you do not fully control, or built from weights you did not produce.
- As the entry point to this directory — it decides which of the deeper `mlsec_*` prompts you actually need.

**When NOT to Use:**
- The attack surface is an autonomous agent's tools, memory, and delegated privileges rather than the model — use `../agentic-ai-systems/aiagent_agentic_threat_model.md`.
- The concern is the surrounding application (authn/z, output handling, injection at the app layer) — use `domain-software-engineering/analysis/security/security_llm_application_review.md`.
- You want a fairness, privacy-compliance, or governance review rather than a security one — use `../responsible-ai-governance/`.

## Inputs / Context

This prompt is for defensive, authorized security review only. Provide what you can; the model degrades gracefully and names what it could not assess:
- **Model & task** — architecture family, what it predicts, and how the prediction is consumed downstream.
- **Deployment surface** — who can query it, at what rate, and what they see back (label only, score, top-k, logits, explanation).
- **Training data provenance** — who contributed it, whether any of it is user-submitted, scraped, or third-party.
- **Artifact provenance** — pretrained weights, their source, and the serialization format.
- **Retraining loop** — whether production data or user feedback flows back into training, and what reviews it.
- **Consequence of a wrong or manipulated prediction** — the thing that makes an attack worth mounting.

## Constraints

**Must:**
- Walk all six categories and state for each threat whether it applies to *this* deployment and why, grounded in what the attacker can reach — not in whether the attack exists in the literature.
- Derive attacker capability explicitly (query access, rate, output granularity, data-contribution ability, artifact access) before scoring any threat, since every score depends on it.
- Give each applicable threat one concrete mitigation **and** the observable signal that would show the mitigation has failed.
- State the residual risk that remains after mitigation, in terms of what the attacker can still achieve.

**Must Not:**
- Produce attack code, payloads, working exploits, or step-by-step offensive procedures — this is defensive modelling.
- Assert attack success rates, CVE identifiers, benchmark figures, or named incidents from memory; where a specific number would change the decision, mark it `[verify against a primary source]`.
- Score a threat as low-exposure because the team has not seen it, or as high because it is prominent in the literature — exposure comes from the surface, not from familiarity.
- Recommend a mitigation whose only evidence is that it appears in a paper's defence section; note when a defence has known adaptive-attack bypasses.

**Instructions:**

1. **Confirm scope and intent.** State that this is a defensive, authorized review of the named model and deployment. Summarize the model, its consumers, and the decision it drives.

2. **Derive the attacker capability profile.** Before any scoring, write down what an attacker can actually do: query or not; at what volume; what the response reveals (label / score / top-k / logits / explanations); whether they can contribute training data; whether they can reach the artifact or the training pipeline; whether they are an insider. Everything downstream is scored against this profile.

3. **Category 1 — Evasion at inference.** Adversarial examples crafted to flip a prediction; perturbation budget realistic for this input channel (an attacker who controls a JPEG upload has a different budget from one who controls a physical scene). Assess whether an attacker benefits from a flipped prediction, and whether they get feedback to iterate.

4. **Category 2 — Training-data integrity.** Poisoning that degrades accuracy, targeted poisoning that changes specific predictions, and backdoors that implant a trigger. Assess by asking who can put bytes into the training set and what reviews them — user-submitted content, scraped corpora, third-party feeds, and the production feedback loop are the surfaces.

5. **Category 3 — Model confidentiality.** Extraction and functional stealing via query access. Score against the capability profile: richer outputs and higher rate limits move this up. State what the model is worth to a competitor, since that governs whether the query budget is worth spending.

6. **Category 4 — Data confidentiality.** Membership inference, attribute inference, and model inversion — what the model leaks about the records it trained on. Assess sensitivity of the training data, overfitting signals, and whether per-example influence is plausibly recoverable.

7. **Category 5 — Artifact and supply chain.** Provenance of pretrained weights, unsafe deserialization formats, dependency and framework integrity, and the integrity of the artifact between training and serving. Note where an artifact is trusted purely because of where it was downloaded from.

8. **Category 6 — Availability and abuse.** Query-cost amplification, sponge inputs that maximize compute per request, and abuse of the model as a free service. Assess against the cost model of inference.

9. **Score and rank.** For each applicable threat give exposure (from the capability profile) and impact (from the downstream consequence). Rank so the register drives work order rather than reading as a list.

10. **Attach mitigations and detection.** One concrete, deployment-specific mitigation per applicable threat, plus the signal that would reveal its failure. Apply the impossible-vs-tedious test: if the mitigation only raises attacker cost, say so explicitly and state the new cost.

11. **Route onward.** Name which deeper `mlsec_*` prompt to run for each high-ranked threat, and state which categories were assessed as not applicable so the omission is deliberate and reviewable.

**Output Format:**

A markdown threat model:
- **Scope & Intent** — defensive/authorized statement, model summary, decision it drives.
- **Attacker Capability Profile** — query access, rate, output granularity, data contribution, artifact access, insider assumption.
- **Threat Register** — table: Category | Threat | Mechanism (described, not weaponized) | Applies here? (why) | Exposure | Impact | Mitigation | Failure signal.
- **Priority Order** — ranked applicable threats with the reasoning for the top three.
- **Residual Risk** — what an attacker can still achieve after mitigation.
- **Not Applicable** — categories ruled out, each with its reason.
- **Onward Routing** — which `mlsec_*` prompt to run next, and why.

## Verification

- [ ] The attacker capability profile is written before any threat is scored, and scores refer back to it.
- [ ] All six categories are walked; every threat is marked applicable or not with a stated reason.
- [ ] No attack code, payloads, or offensive procedures appear anywhere.
- [ ] No CVE, success rate, or incident is asserted from memory; unknowns are marked `[verify against a primary source]`.
- [ ] Every applicable threat has one concrete mitigation **and** a failure signal.
- [ ] Mitigations with known adaptive-attack bypasses are labelled as cost-raising rather than preventive.
- [ ] Residual risk is stated in terms of what the attacker can still do, not as "risk accepted".
- [ ] Not-applicable categories are listed explicitly rather than silently dropped.

## False-Positive Prevention

❌ **DON'T:**
- Score evasion as high simply because adversarial examples are famous — if a flipped prediction gains the attacker nothing, the threat is low here regardless of literature volume.
- Rule out poisoning because "we control our data" without tracing every path bytes take into the training set, including the production feedback loop.
- Treat a downloaded checkpoint as trusted because the hosting platform is reputable — provenance is a chain, not a domain name.
- Report extraction risk without reference to what the response actually reveals; a label-only endpoint and a logits endpoint are different systems.
- Assert an attack "succeeds ~90% of the time" or name a CVE from memory to make a threat feel concrete.
- Call a threat mitigated when the mitigation only makes the attack slower and noisier.

✅ **DO:**
- Ground every applicability judgment in the capability profile — what this attacker can reach, at what rate, with what feedback.
- Trace training-data provenance to every contributor, and name the review that stands between a contributor and the training set.
- Score impact from the downstream decision the prediction drives, so a low-exposure threat with severe impact still surfaces.
- Mark quantities you cannot verify as `[verify against a primary source]` and let the decision proceed without them.
- Say plainly when a mitigation raises cost rather than preventing the attack, and state the new cost.
- List the categories you ruled out, so a reviewer can challenge the omission.

## Example Output

```markdown
## ML Threat Model: Resume-Screening Classifier v4 (internal API, recruiter-facing)
Defensive, authorized review. Gradient-boosted classifier scores applicants 0–100;
recruiters see the score and top-3 contributing features. Retrained quarterly on
recruiter accept/reject feedback.

### Attacker Capability Profile
| Dimension | This deployment |
|---|---|
| Query access | Indirect — an applicant submits a resume, cannot call the API |
| Rate | ~1 submission/role; unlimited across roles over time |
| Output visibility | None to the applicant; score + top-3 features to recruiters |
| Data contribution | **Yes** — every submitted resume can enter the retraining set |
| Artifact access | No (internal registry, SSO-gated) |
| Insider | Recruiter can see scores and features; cannot retrain |

### Threat Register
| Cat | Threat | Mechanism | Applies? | Exposure | Impact | Mitigation | Failure signal |
|---|---|---|---|---|---|---|---|
| 1 Evasion | Keyword-stuffed resume flips score | input crafted to hit learned proxies | Yes — direct incentive | Med | Med | feature-plausibility checks; cap single-feature contribution | score distribution skews toward the cap |
| 2 Poisoning | Feedback-loop poisoning | coordinated submissions shift the quarterly retrain | Yes — applicant text enters training | Low | High | per-cohort drift gate before promotion; label audit sample | retrain-vs-prior slice deltas exceed gate |
| 3 Extraction | Model stealing | no query access | **No** — applicants cannot query | — | — | — | — |
| 4 Membership | Prior-applicant inference | top-3 features shown to recruiters | Yes — recruiter-side | Low | High | suppress features traceable to a single record | feature explanations reference rare tokens |
| 5 Supply chain | Unsafe artifact load | registry pickle deserialization | Yes | Low | High | safe serialization format + hash pinning at load | load-time hash mismatch |
| 6 Availability | Cost amplification | inference cost trivial per request | **No** | — | — | — | — |

### Priority Order
1. **Feedback-loop poisoning** — low exposure, but it is the only threat that persists into
   every future prediction, and the retrain path currently has no gate.
2. **Membership inference via explanations** — the top-3 feature display is the leak surface,
   and the training data is applicant PII.
3. **Evasion via keyword stuffing** — highest exposure, but the impact is bounded by the
   recruiter review that follows the score.

### Residual Risk
Evasion cannot be eliminated while the model reads free text an applicant authors. The
mitigation bounds how much any single feature can move the score; a sophisticated applicant
can still shift it within that cap. Poisoning gates detect distribution shift, not a slow
patient campaign below the gate threshold — `[verify: choose the gate threshold from your own
historical retrain deltas, not from a default]`.

### Not Applicable
- **Extraction (Cat 3)** — no query path exists from outside; revisit if a self-service
  applicant-facing score is ever exposed.
- **Availability (Cat 6)** — per-request compute is negligible and the endpoint is internal.

### Onward Routing
- Poisoning → `mlsec_data_poisoning_backdoor_defense.md`
- Membership inference → `mlsec_membership_inference_defense.md`
- Artifact loading → `mlsec_ml_supply_chain_audit.md`
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** the six-category taxonomy crossed with the capability profile is the analysis structure.
- **DS-06 (Prioritization and Severity Guidance):** exposure × impact produces a work order rather than a list.
- **CM-02 (Constraint Specification):** the defensive-only, no-fabrication, and mitigation-plus-signal rules bound the output.
- **QA-12 (False Positives Identification):** separates threats that apply to this deployment from those that merely exist.
- **AG-44 (Impossible-vs-Tedious Control Test):** forces each mitigation to declare whether it prevents or merely costs.

**Related Prompts:**
- `mlsec_adversarial_robustness_assessment.md` — deepens Category 1 once evasion ranks.
- `mlsec_data_poisoning_backdoor_defense.md` — deepens Category 2.
- `mlsec_secure_inference_endpoint_design.md` — the serving-side controls for Categories 3 and 6.
- `../agentic-ai-systems/aiagent_agentic_threat_model.md` — the agent-side counterpart when tools and delegation are in scope.
