---
title: "AI/ML Domain Triage Router"
category: AI-ML/problem-framing-scoping
description: "Classify what an ML situation actually is — a framing question, a data problem, a training failure, an evaluation doubt, a serving constraint, a production incident, or a governance requirement — and emit an ordered prompt sequence, so the domain is consumed by route rather than exhaustively."
techniques:
  - RT-10
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: intermediate
tags:
  - triage
  - routing
  - entry-point
  - problem-diagnosis
  - workflow
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
---

# AI/ML Domain Triage Router

**Objective:** Work out what an ML situation actually is before working on it — separating the presenting complaint from the underlying problem, deciding whether this is a framing, data, training, evaluation, serving, production, security, or governance question, and emitting a short ordered sequence of prompts to run rather than a list of everything relevant.

**When to Use:**
- Entering `domain-AI-ML/` without knowing which of its fifteen subdirectories applies.
- A situation is described in symptoms — "the model isn't working", "our AI project is stuck" — rather than in a diagnosis.
- Several things seem wrong and you need an order rather than a list.

**When NOT to Use:**
- You already know the specific question — go directly to the prompt; this router is overhead.
- The question is whether to use ML at all — that is `mlframe_is_this_ml_problem.md`, and this router will send you there anyway.
- The problem is not about a model — check the boundary table in the domain README first.

## Inputs / Context

- **The presenting complaint** — in the user's own words, before any reframing.
- **Lifecycle position** — idea, in development, in evaluation, deployed, or degrading in production.
- **What has already been tried** — since a repeated failure means the diagnosis was wrong, not the effort insufficient.
- **What is measured today** — offline metrics, production metrics, or nothing.
- **Who is asking** — practitioner, product owner, or leadership, which changes which prompt is useful even for the same underlying problem.
- **Constraint pressure** — cost, latency, quality, compliance, or time.

## Constraints

**Must:**
- Distinguish the **presenting complaint** from the **underlying problem**; they differ often enough that routing on the complaint is the main way people end up in the wrong subdirectory.
- Emit **at most three prompts, ordered**, with the reason each comes where it does. A list of everything relevant is what the README already provides, and it is not a route.
- Route to `mlframe_is_this_ml_problem.md` whenever the situation may not need a model at all, regardless of how far along the project is.
- Check for the two failures that masquerade as other problems — **data leakage** and **train/serve skew** — before routing to modelling or serving work, because both present as something else.
- Route outside the domain when the boundary table says so, and name the destination.

**Must Not:**
- Route on the presenting complaint alone when a common misdiagnosis applies to it.
- Emit a long list of relevant prompts; the value of triage is subtraction.
- Assume the sophisticated diagnosis; the most common causes of "the model isn't working" are ordinary and cheap to check.
- Route to a security or governance prompt without a stated exposure or requirement.
- Skip the "already tried" question — a repeated failure indicates a wrong diagnosis, and re-routing to the same place repeats it.

**Instructions:**

1. **Capture the complaint verbatim.** Do not reframe it yet. The words used carry information about which lifecycle stage the person believes they are in, which is itself diagnostic.

2. **Establish the lifecycle position.** Idea, development, evaluation, deployment, or production degradation. This narrows the candidate set sharply.

3. **Ask what has already been tried.** If a fix has been attempted and failed, the diagnosis was wrong. Route to a diagnostic prompt rather than to a second attempt at the same fix.

4. **Test for the common misdiagnoses.** Each of these presents as something else:

   | Presenting complaint | Frequently actually |
   |---|---|
   | "Accuracy dropped in production" | train/serve skew, or a pipeline change, not model decay |
   | "The model is great offline, bad live" | leakage in the offline evaluation |
   | "We need a better model" | the metric does not match the decision, or no baseline exists |
   | "The model is biased" | a slice with too little data to conclude anything |
   | "We need more data" | the model has plateaued; labels are not the constraint |
   | "Inference is too expensive" | over-provisioned model for the actual difficulty distribution |
   | "The AI project is stuck" | it was never framed as a decision anyone would act on |

   Check the applicable row before routing on the complaint's face value.

5. **Classify into a route.** Framing, data, features, modelling, evaluation, optimization, serving, production, GenAI/RAG, agentic, security, governance, leadership, or learning. Where two apply, order them by which would invalidate the other's work if left unresolved — a leakage problem invalidates every modelling result, so it goes first.

6. **Check the domain boundary.** If the question is really statistical study design, regulatory interpretation, clinical validity, prompt craft, or whole-system agentic authoring, route out and name the destination. Cite the boundary table rather than deciding ad hoc.

7. **Emit at most three prompts, ordered**, each with the reason for its position and what its output feeds. Stop at three; if more seem necessary, the situation contains several problems and should be split.

8. **State the stopping condition.** What result from the first prompt would mean the rest are unnecessary. This is what makes the route a route rather than a plan.

9. **Name what was ruled out.** The routes considered and rejected, briefly, so the person can challenge the triage rather than accept it.

**Output Format:**

A markdown triage:
- **Presenting Complaint** — verbatim.
- **Lifecycle Position** — where this sits.
- **Already Tried** — and what a repeated failure implies.
- **Misdiagnosis Check** — the applicable row, and the verdict.
- **Classification** — the route, with the reason.
- **Boundary Check** — in-domain or routed out, with destination.
- **Sequence** — table: Order | Prompt | Why here | Feeds.
- **Stopping Condition** — what would make the rest unnecessary.
- **Ruled Out** — routes considered and why not.

## Verification

- [ ] The complaint is captured verbatim before reframing.
- [ ] Lifecycle position is established.
- [ ] "Already tried" is asked, and a repeated failure redirects to diagnosis.
- [ ] The applicable misdiagnosis row is checked.
- [ ] Leakage and train/serve skew are ruled out before modelling or serving routes.
- [ ] The boundary table is consulted and out-of-domain questions are routed out by name.
- [ ] At most three prompts are emitted, ordered, each with a reason.
- [ ] A stopping condition is stated.
- [ ] Rejected routes are named.

## False-Positive Prevention

❌ **DON'T:**
- Route "accuracy dropped in production" straight to retraining — train/serve skew and pipeline changes are more common and cost nothing to rule out, while a retrain costs a cycle and may fix nothing.
- Accept "we need more data" without checking the learning curve; if the model has plateaued, more labels change nothing and the money is spent.
- Emit eight relevant prompts; that is the README's job, and it leaves the person exactly where they started.
- Route to a bias audit on a slice with a handful of examples — the finding will be noise, and it will be treated as a result.
- Assume the interesting diagnosis; the boring causes are more common and cheaper to eliminate first.
- Re-route to a fix that has already been tried and failed, without changing the diagnosis.

✅ **DO:**
- Separate the complaint from the problem, and check the misdiagnosis table before routing.
- Rule out leakage and skew first — both invalidate whatever comes after them.
- Order by what would invalidate what, not by apparent severity.
- Stop at three prompts and split the situation if more are needed.
- State what result would end the investigation early.
- Show the rejected routes so the triage can be argued with.

## Example Output

```markdown
## Triage: "Our fraud model is getting worse and we need to retrain it"

### Presenting Complaint
Verbatim: *"Our fraud model is getting worse and we need to retrain it. Precision has dropped
about 8 points over two months. Can you help us set up more frequent retraining?"*

The complaint arrives with its own diagnosis and its own fix attached. That is the thing to
examine first.

### Lifecycle Position
**Deployed, degrading in production.** Model has been live 14 months.

### Already Tried
A retrain was run six weeks ago. **Precision recovered briefly, then declined again.**

This is the most informative fact available. A fix that works temporarily and then fails means
the diagnosis is wrong — something is changing that retraining does not address. Routing to
"more frequent retraining" would repeat a fix already shown to be insufficient, at higher cost.

### Misdiagnosis Check
| Presenting | Frequently actually |
|---|---|
| "Accuracy dropped in production" | **train/serve skew, or a pipeline change, not model decay** |

Applicable. Genuine concept drift usually degrades steadily and is corrected by retraining;
degradation that returns after a retrain points at a feature-pipeline difference or a change in
an upstream data source. **Verdict: do not route to retraining. Route to diagnosis.**

### Classification
**Production**, then **data**. Ordered that way because a feature-pipeline or upstream-source
problem would invalidate any modelling work done first — retraining on skewed features produces
a model that degrades again, which is precisely the observed pattern.

### Boundary Check
In-domain. Not `domain-finance/` — this is model behaviour, not regulated model validation. Were
the question "does our fraud model meet SR 11-7 validation expectations", that would route to
`responsible-ai-governance/rai_model_risk_management_sr1107.md` and to the model risk function.

### Sequence
| Order | Prompt | Why here | Feeds |
|---|---|---|---|
| 1 | `production-monitoring/mlmonitor_performance_degradation_triage.md` | separates skew, pipeline change, upstream data change, and genuine drift — the fix depends entirely on which | the diagnosis everything else depends on |
| 2 | `production-monitoring/mlmonitor_feedback_loop_detection.md` | fraud labels come from a review queue the model populates; the model may be shaping its own training data | whether retraining can work at all |
| 3 | `data-for-ml/mldata_data_contract_design.md` | **only if** step 1 finds an upstream change — prevents recurrence rather than repairing this instance | a durable fix |

### Stopping Condition
**If step 1 finds train/serve skew or an upstream schema change, stop.** Steps 2 and 3 are
unnecessary, the retraining plan is unnecessary, and the fix is in the feature pipeline. That
outcome would explain the observed pattern completely: a retrain temporarily fits the skewed
features, then degrades as they drift further.

### Ruled Out
- **`mlmonitor_retraining_trigger_strategy.md`** — this is where the request pointed, and it is
  premature. It becomes the right prompt *only* if step 1 confirms genuine concept drift.
- **`mleval_eval_result_skepticism_audit.md`** — offline and online metrics agreed at launch, so
  the offline evaluation is not the suspect here.
- **`rai_bias_detection_audit.md`** — no fairness concern was raised, and precision decline
  affects all segments similarly per the complaint.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** complaint → lifecycle → already-tried → misdiagnosis check → route is the decision path.
- **ST-02 (Structured Sequential Instructions):** diagnosis precedes routing, so the emitted sequence rests on evidence rather than on the complaint's own framing.
- **CM-02 (Constraint Specification):** the at-most-three-prompts and rule-out-leakage-first rules bound the output.
- **QA-12 (False Positives Identification):** the misdiagnosis table is the whole defence against routing on the presenting complaint.
- **DS-06 (Prioritization and Severity Guidance):** ordering is by what would invalidate what, not by apparent severity.

**Related Prompts:**
- `mlframe_is_this_ml_problem.md` — where this routes when the situation may not need a model.
- `../model-evaluation-validation/mleval_eval_result_skepticism_audit.md` — the standard second stop when offline and live disagree.
- `../data-for-ml/mldata_data_leakage_detector.md` — ruled out early because it invalidates everything downstream.
- `../production-monitoring/mlmonitor_performance_degradation_triage.md` — the production-side diagnostic this most often routes to.
