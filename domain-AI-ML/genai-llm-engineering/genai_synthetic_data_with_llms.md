---
title: "Synthetic Data Generation with LLMs"
category: AI-ML/genai-llm-engineering
description: "Generate synthetic training or evaluation data with LLMs without contaminating eval sets, amplifying bias, or collapsing diversity — with provenance tracking, quality filtering, and a contamination firewall."
techniques:
  - ST-02
  - QA-12
  - CM-02
  - DS-02
  - RT-05
difficulty: advanced
tags:
  - synthetic-data
  - data-generation
  - contamination
  - bias
  - diversity
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_fine_tuning_workflow.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Synthetic Data Generation with LLMs

**Objective:** Design a pipeline that uses an LLM to generate synthetic training or evaluation data — with a strict firewall against contaminating evaluation sets, controls against amplifying the generator's biases and collapsing output diversity, quality filtering, and provenance tracking — so the synthetic data improves models without quietly corrupting the very metrics used to judge them.

**When to Use:**
- You need more training data for fine-tuning, augmentation, or bootstrapping a low-resource task.
- You need eval cases (edge/adversarial) you can't easily collect from real data.
- A real dataset is too small, imbalanced, or privacy-restricted to use directly.

**When NOT to Use:**
- Sufficient high-quality real data exists — prefer it; synthetic data carries the generator's blind spots.
- You're evaluating a model and want ground truth (synthetic eval labels need human validation).

## Inputs / Context

State the generator model + provider + version (and that it should differ from any model being evaluated). Provide what you can:
- **Purpose** — training augmentation, fine-tuning data, eval-set expansion, or cold-start bootstrap.
- **Target distribution** — what real data looks like; the classes/cases/edge conditions needed.
- **Real data on hand** — seed examples, the real eval set, any labels.
- **Risk sensitivity** — fairness/bias concerns, regulated domain, privacy constraints.
- **Validation capacity** — can humans review a sample? Is there a downstream eval to measure usefulness?

## Constraints

**Must:**
- Enforce a contamination firewall: synthetic *training* data must never overlap (exact or near-duplicate) the *evaluation* set, and synthetic *eval* data must be human-validated before it gates anything.
- Control diversity and bias: synthetic data inherits the generator's distribution and blind spots; require diversity checks and bias slices.
- Track provenance: tag every synthetic example with generator+version, prompt, and seed so it's auditable and removable.

**Must Not:**
- Generate eval data with the same model being evaluated and treat it as ground truth (circular, self-flattering).
- Augment a minority class with synthetic copies that are near-duplicates (no real diversity gain; inflates metrics).
- Use synthetic data to fix a bias by generating from a generator that shares the bias, without checking.
- Fabricate that synthetic data improved the model — prove it on a real held-out set.

**Instructions:**

1. **Define the gap synthetic data must fill.** State whether you need volume, class balance, edge/adversarial coverage, or stylistic variety — and the real-data distribution it must match without merely copying.

2. **Set the contamination firewall first.** Reserve a real held-out eval set that no synthetic data derives from. Define dedup/near-duplicate checks (hashing, embedding similarity) between synthetic training data and the eval set. Cross-link `mldata_data_leakage_detector.md` for the leakage discipline.

3. **Design the generation prompt and seeding.** Use real seed examples, vary prompts/personas/parameters to induce diversity, and specify the schema/format. Avoid prompts that collapse outputs to a few templates.

4. **Generate with diversity controls.** Vary temperature, seeds, conditioning attributes, and prompt framings; deduplicate aggressively; measure diversity (distinct n-grams, embedding spread, coverage of target attributes) — not just volume.

5. **Quality-filter the output.** Validate format/schema, remove low-quality, off-distribution, factually wrong, or unsafe examples. For labeled data, validate label correctness (a sample by humans; never assume the generator labeled correctly).

6. **Run bias and fairness checks.** Slice synthetic data by sensitive/relevant attributes and compare to the target distribution; the generator may over- or under-represent groups or encode stereotypes. Adjust generation or filtering to correct, and re-check.

7. **Validate usefulness on real data.** Train/augment with the synthetic data and measure on the *real* held-out eval — synthetic-only improvements are suspect. For synthetic eval cases, have humans confirm a sample before they gate.

8. **Track provenance and enable rollback.** Tag each example with its generator, version, prompt, and seed; keep synthetic and real separable so synthetic data can be removed or down-weighted if it later proves harmful.

**Output Format:**

A markdown generation plan:
- **Gap & Target Distribution** — what's needed + the real distribution to match
- **Contamination Firewall** — reserved real eval + dedup/near-duplicate checks
- **Generation Design** — seeds, prompt/persona variation, schema, diversity parameters
- **Diversity Metrics** — how diversity/coverage is measured
- **Quality Filter** — validity, correctness, safety, label checks
- **Bias/Fairness Checks** — slices + comparison to target + corrective action
- **Usefulness Validation** — real held-out measurement (and human check for synthetic eval)
- **Provenance & Rollback** — tagging + separability

## Verification

- [ ] A real held-out eval set is reserved and a dedup/near-duplicate check guards it from synthetic training data.
- [ ] Synthetic eval data is human-validated before it gates anything; the evaluated model didn't generate its own eval.
- [ ] Diversity and coverage are measured, not just volume; near-duplicates are removed.
- [ ] Bias/fairness slices are checked against the target distribution with corrective action.
- [ ] Usefulness is proven on real held-out data, not on synthetic data alone.
- [ ] Every synthetic example carries provenance and is separable for rollback.

## False-Positive Prevention

❌ **DON'T:**
- Generate eval questions with the same model you're evaluating and call the resulting scores ground truth — it's circular.
- "Balance" a minority class with synthetic near-duplicates; you add rows, not information, and inflate metrics.
- Trust the generator's own labels on synthetic examples without a human spot-check.
- Claim synthetic augmentation worked because the model scored higher — on a real held-out set or it doesn't count.

✅ **DO:**
- Firewall the real eval set and dedup synthetic training data against it (exact + near-duplicate).
- Measure diversity and bias slices; the generator's blind spots propagate into the data.
- Human-validate synthetic eval cases and synthetic labels before they influence decisions.
- Prove usefulness on real held-out data and keep synthetic data tagged and removable.

## Example Output

```markdown
## Synthetic Data Plan: Augment Rare Support-Intent Classes (generator: <provider/model vX>)

### Gap & Target Distribution
3 of 20 intent classes have <50 real examples. Need ~300 each, matching real phrasing variety.

### Contamination Firewall
Real eval set (400 tickets, human-labeled) reserved and frozen. Synthetic train data checked
against it by embedding-similarity (cosine > 0.92 = drop) + exact-hash. Per mldata_data_leakage_detector.

### Generation Design
Seed each prompt with 3 real examples + a varied customer persona; 6 persona templates x temp 0.7–1.0.
Output schema: {text, intent}. Avoid reusing seed phrasing verbatim.

### Diversity Metrics
Distinct-2 n-grams, embedding spread vs real class; coverage of sub-intents. Drop the run if
distinct-2 < real-class baseline.

### Quality Filter
Schema-valid + human spot-check 10% for label correctness + safety scan. Reject off-topic.

### Bias/Fairness Checks
Slice by tone/formality and named entities; generator over-produced formal phrasing -> add casual personas, re-check.

### Usefulness Validation
Train classifier with + without synthetic; measure macro-F1 on the REAL frozen eval.
Ship only if rare-class recall improves with non-overlapping CI and overall F1 doesn't regress.

### Provenance & Rollback
Each row tagged generator+version+prompt+seed; is_synthetic flag enables down-weight/removal.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** firewall → generate → filter → bias check → validate → provenance.
- **QA-12 (False Positives Identification):** core to catching contamination, circular eval, and diversity-collapse.
- **CM-02 (Constraint Specification):** the contamination firewall is the governing constraint.
- **DS-02 (Metric Specification):** diversity, bias slices, and usefulness are measured on defined metrics.
- **RT-05 (Evidence-Based Reasoning):** usefulness is proven on real held-out data, not asserted.

**Related Prompts:**
- `genai_fine_tuning_workflow.md` — consumes synthetic training data under the same leakage discipline.
- `genai_llm_evaluation_design.md` — synthetic eval cases must meet this program's validation bar.
- `domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md` — the leakage/contamination discipline this firewall applies.
