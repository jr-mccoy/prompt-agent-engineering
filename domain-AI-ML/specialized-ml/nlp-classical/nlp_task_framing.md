---
title: "Classical NLP Task Framing"
category: AI-ML/specialized-ml/nlp-classical
description: "Frame a text task before choosing a method — deciding what the unit of prediction is, whether the label set is closed, and whether an LLM or a trained classical model is the right instrument for this volume, latency, and stability profile."
techniques:
  - RT-10
  - ST-02
  - CM-02
  - QA-12
  - DS-02
difficulty: intermediate
tags:
  - task-framing
  - text-classification
  - nlp
  - llm-vs-classical
  - label-design
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_classification_design.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_ner_extraction_design.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_topic_modeling_approach.md
  - domain-AI-ML/problem-framing-scoping/mlframe_problem_to_ml_task_translator.md
---

# Classical NLP Task Framing

**Objective:** Turn a text-processing need into a well-formed task before any method is chosen — fixing the unit of prediction, deciding whether the label set is closed, and making the LLM-versus-trained-model decision on volume, latency, stability, and explainability rather than on defaults in either direction.

**When to Use:**
- A text task has been described in business terms and nobody has decided what is being predicted about what.
- The team is about to reach for an LLM without having asked whether the task needs one.
- A previous text project underperformed and the suspicion is that it was framed wrong.

**When NOT to Use:**
- The task is already framed and you need the method design — go to `nlp_text_classification_design.md`, `nlp_ner_extraction_design.md`, or `nlp_topic_modeling_approach.md`.
- The task is generative — summarization, drafting, conversation — this directory covers analysis of existing text.
- You need the general is-this-an-ML-problem check — use `../../problem-framing-scoping/mlframe_is_this_an_ml_problem.md`.

## Inputs / Context

- **The need in business terms** — what someone wants to happen, before it is a modelling task.
- **Text characteristics** — length, language(s), domain vocabulary, quality (clean prose, OCR, transcripts, user-generated).
- **Volume and latency** — documents per day and the response time required, which dominate the method decision.
- **Label availability** — whether labelled examples exist, could be created, or must be derived.
- **Label stability** — how often the categories change, which decides whether a trained model is a liability.
- **Explainability requirement** — whether a human must be able to see why a decision was made.

## Constraints

**Must:**
- Fix the **unit of prediction** explicitly — document, paragraph, sentence, span, or entity pair. Ambiguity here produces labelled data that cannot train anything, and it is the most common framing failure in text projects.
- Determine whether the label set is **closed** (fixed categories), **open** (new categories appear), or **hierarchical**, since this rules methods in and out immediately.
- Make the LLM-versus-trained-model decision on **volume, latency, stability, cost, and explainability together** — not on capability alone, on which an LLM usually wins while losing on the others.
- Require that a human can perform the task from the definition alone; if annotators cannot agree, no method will resolve it.
- State what happens to text that fits no category, since real corpora always contain some.

**Must Not:**
- Assert accuracy expectations, model comparisons, or throughput figures from memory; mark quantities `[measure on your data]`.
- Choose a method before the unit and the label set are fixed.
- Assume an LLM is the answer for high-volume, low-latency, stable-label classification — a trained classifier is frequently far cheaper and faster there, and this directory exists for those cases.
- Assume a trained classifier is the answer where labels shift monthly and no labelled data exists.
- Frame as classification something that is genuinely extraction, or as extraction something that is genuinely classification.

**Instructions:**

1. **Restate the need as a decision.** What action follows the model's output, and who takes it? A text task with no consequent action is an analysis request, not a modelling task.

2. **Fix the unit of prediction.** Document, paragraph, sentence, span, or pair. Write the annotation instruction that follows from it — if that instruction is hard to write, the unit is wrong. This is the step that most often needs a second attempt.

3. **Classify the task type.**
   - *Classification* — assign a category to a unit. One label or several?
   - *Extraction* — locate spans and their types.
   - *Discovery* — find structure without a predefined label set.
   - *Similarity / matching* — relate two pieces of text.
   Mis-framing between the first two is common: "find the contract's termination clause" is extraction; "does this contract have a termination clause" is classification, and they need different data.

4. **Characterize the label set.** Closed and stable; closed but revised periodically; open with new categories arriving; or hierarchical. Then check the labels are mutually exclusive if the framing assumes single-label, and that a human can separate them.

5. **Test human agreement.** Have two people label the same 50 units from the definition alone. Low agreement means the task is under-defined, and that must be fixed before any method choice — no model resolves a definition annotators cannot apply.

6. **Decide LLM versus trained model on all five axes.**
   | Factor | Favours a trained classical model | Favours an LLM |
   |---|---|---|
   | Volume | high — per-item cost dominates | low |
   | Latency | tight | relaxed |
   | Label stability | stable | shifting |
   | Labelled data | exists or is cheap to make | none, and expensive |
   | Explainability | required | not required |
   Score honestly. The common error is choosing an LLM on capability while the workload sits firmly in the left column, and a smaller error is defending a classical model where labels change every month.

7. **Consider the hybrid.** LLM to bootstrap labels, trained model to serve at volume; or trained model for the confident majority with LLM escalation for the rest. This is frequently the strongest answer and is skipped because it requires two components.

8. **Define the null class.** What happens to text matching no category: an explicit `other` class, an abstention, or a confidence threshold. Real corpora always contain some, and a framing without this produces a model that must assign something.

9. **Set the success measure and the baseline.** The metric that matches the consequent action, and the simplest baseline — keyword rules, majority class — that a model must beat to be worth building.

**Output Format:**

A markdown framing:
- **Decision & Action** — what follows the output, and who acts.
- **Unit of Prediction** — the unit, and the annotation instruction that follows.
- **Task Type** — classification, extraction, discovery, or matching, with the reason.
- **Label Set** — closed/open/hierarchical; exclusivity; the null class.
- **Human Agreement** — measured agreement and any definition fixes needed.
- **Method Decision** — the five-axis table, scored, with the verdict.
- **Hybrid Option** — considered, with a verdict.
- **Success Measure & Baseline** — metric and the bar to beat.

## Verification

- [ ] A consequent action and its owner are named.
- [ ] The unit of prediction is fixed and its annotation instruction is writable.
- [ ] Task type is chosen with a reason, and classification/extraction are not confused.
- [ ] The label set is characterized, and exclusivity is checked where single-label is assumed.
- [ ] Human agreement is measured before any method decision.
- [ ] The method decision scores all five axes, not capability alone.
- [ ] A hybrid option is explicitly considered.
- [ ] A null class or abstention path exists.
- [ ] A baseline is named that the model must beat.
- [ ] No accuracy or throughput figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Choose an LLM because it can do the task — it can do almost any text task, which is exactly why capability is the least informative axis in the decision.
- Skip the human-agreement check; if two annotators disagree on a third of cases, the task is under-defined and every subsequent metric is measuring that confusion.
- Leave the unit of prediction implicit — "classify the document" and "classify each paragraph" produce entirely different datasets, and the ambiguity usually surfaces after labelling has begun.
- Frame extraction as classification to simplify the labelling; you lose the location information the downstream consumer needs and will not get it back.
- Build a closed-label classifier where new categories appear monthly — you have committed to a retraining treadmill.
- Omit the null class; the model is then forced to assign a category to text that belongs in none, and it will do so confidently.

✅ **DO:**
- Start from the action the output triggers; a task with no action does not need a model.
- Write the annotation instruction as the test that the unit of prediction is right.
- Measure human agreement first and fix the definition before choosing anything.
- Score all five axes and let volume, latency, and stability outweigh capability.
- Consider the hybrid seriously — LLM for labels or escalation, trained model for volume.
- Define the null class and the baseline before the first experiment.

## Example Output

```markdown
## Task Framing: Routing Inbound Insurance Correspondence
~14,000 letters and emails per day, mixed quality including OCR of scanned mail.

### Decision & Action
Each item is routed to one of 9 processing queues. A mis-route costs a handling cycle and delays
the customer. Action owner: the mailroom automation, with a human review queue for low confidence.

### Unit of Prediction
**The document.** Annotation instruction: *"Read the correspondence. Which single queue should
handle it? If more than one applies, choose the one that must act first."*

The instruction is writable and unambiguous, which is the test. An earlier attempt framed the
unit as the paragraph and the instruction could not be written — a letter's routing depends on
the whole document, not on any one paragraph, and the labelling would have produced data that
trained nothing.

### Task Type
**Single-label classification.** Not extraction: the downstream consumer needs the queue, not the
location of the text that implies it. Had the requirement been "highlight the sentence that
justifies the routing", that would be extraction and would need span-level labels.

### Label Set
**Closed, 9 queues, revised roughly annually** when the operations structure changes.
Exclusivity: checked — two queues (claims-new and claims-supplementary) overlap in practice, and
the definition needed a tiebreak rule before labelling could proceed.
**Null class:** `unclassifiable` for illegible OCR and genuinely out-of-scope mail — real intake
always contains some, and forcing an assignment would send illegible scans to a real queue.

### Human Agreement
Two operations staff labelled the same 50 documents from the definition alone `[measure]`. Focus
the disagreement analysis on the claims-new / claims-supplementary pair; if agreement is low
there, the tiebreak rule is not yet doing its job and no model will recover the distinction.

### Method Decision
| Factor | This task | Favours |
|---|---|---|
| Volume | **14,000/day** | **trained model** — per-item LLM cost is significant at this volume |
| Latency | overnight batch acceptable | neutral |
| Label stability | **annual revision** | **trained model** |
| Labelled data | 3 years of historical routing decisions available | **trained model** |
| Explainability | required for audit of mis-routes | **trained model** |

**Verdict: trained classical classifier.** Four of five axes point the same way. An LLM would
handle the task capably and would be the wrong instrument — high volume, stable labels, abundant
existing labels, and an explainability requirement all argue against it. This is precisely the
case `specialized-ml/nlp-classical/` exists for.

### Hybrid Option
**Adopt.** Trained classifier serves the confident majority; low-confidence documents and the
`unclassifiable` class escalate to an LLM for a second opinion before reaching human review. This
keeps per-item cost low while giving the hard tail better treatment than a threshold alone.
The LLM is also used once, offline, to help label the ambiguous historical cases that the
tiebreak rule newly disambiguates.

### Success Measure & Baseline
Metric: **macro-F1 across the 9 queues**, not accuracy — the queue distribution is heavily skewed
and accuracy would be dominated by the largest queue while the small ones failed silently.
Also tracked: mis-route rate on the two overlapping claims queues specifically.
**Baseline to beat:** current keyword rules `[measure their macro-F1]`. If a trained model cannot
beat the existing rules on this data, the framing or the labels are the problem, not the method.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** unit → task type → label set → method is a decision path where each step constrains the next.
- **ST-02 (Structured Sequential Instructions):** framing is completed before any method is considered.
- **CM-02 (Constraint Specification):** the writable-annotation-instruction and five-axis rules bound the framing.
- **QA-12 (False Positives Identification):** the human-agreement check rejects tasks that are under-defined rather than hard.
- **DS-02 (Metric Specification):** the success metric is chosen against the skew and the consequent action.

**Related Prompts:**
- `nlp_text_classification_design.md` — once framed as classification.
- `nlp_ner_extraction_design.md` — once framed as extraction.
- `nlp_topic_modeling_approach.md` — once framed as discovery.
- `../../problem-framing-scoping/mlframe_problem_to_ml_task_translator.md` — the domain-general version of this move.
