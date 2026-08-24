# Data for ML

Everything about the data before a model sees it — curation, labelling, splitting, leakage, imbalance, augmentation, versioning, contracts, and the two techniques for getting labels when buying them is not viable. Most model failures are data failures wearing a modelling costume.

**19 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Assembling or auditing a training set.
- Results look too good, which is usually leakage.
- Labels are the constraint and you must decide how to get more.
- An upstream producer keeps breaking your pipeline.

**Not here:**
- The question is which features to build from the data — [`../feature-engineering/`](../feature-engineering/README.md).
- The concern is what the model reveals about the data — [`../model-security/`](../model-security/README.md) or [`../responsible-ai-governance/`](../responsible-ai-governance/README.md).
- The data is adversarially manipulated rather than merely poor — [`../model-security/mlsec_data_poisoning_backdoor_defense.md`](../model-security/mlsec_data_poisoning_backdoor_defense.md).

## Prompts


**Curate and audit**

| Prompt | Use it to |
|---|---|
| [`mldata_dataset_curation_plan.md`](mldata_dataset_curation_plan.md) | Plan how to assemble and curate a dataset for a defined ML task — sources, sampling, coverage, quality gates, and governance — so the data reflects the deployment population and is defensible later. |
| [`mldata_data_quality_audit.md`](mldata_data_quality_audit.md) | Audit a dataset across completeness, validity, consistency, uniqueness, timeliness, and outliers — producing severity-ranked, evidence-backed findings with concrete remediation before the data trains a model. |
| [`mldata_sampling_bias_audit.md`](mldata_sampling_bias_audit.md) | Detect sampling and selection bias between the training sample and the deployment population — per-segment coverage gaps, selection mechanisms, and shift — with evidence-backed, severity-ranked findings. |
| [`mldata_datasheet_authoring.md`](mldata_datasheet_authoring.md) | Author a Datasheet for a dataset across motivation, composition, collection, preprocessing, uses, distribution, and maintenance — documenting limitations and known biases honestly, not just contents. |

**Split and leakage**

| Prompt | Use it to |
|---|---|
| [`mldata_train_test_split_strategy.md`](mldata_train_test_split_strategy.md) | Choose a leak-safe split scheme — random, stratified, grouped, or temporal — and ratios that match how the model will be used, so offline validation reflects production performance. |
| [`mldata_data_leakage_detector.md`](mldata_data_leakage_detector.md) | Systematically hunt for train/test contamination, target leakage, and temporal leakage that inflate offline metrics and collapse in production. |

**Get labels**

| Prompt | Use it to |
|---|---|
| [`mldata_labeling_guideline_designer.md`](mldata_labeling_guideline_designer.md) | Write annotation guidelines that maximize inter-annotator agreement — precise label definitions, decision rules, worked edge cases, and positive/negative examples — before annotation begins. |
| [`mldata_annotation_quality_review.md`](mldata_annotation_quality_review.md) | Assess label quality with the right agreement metric (Cohen's/Fleiss' kappa, Krippendorff's alpha), gold-set accuracy, and a disagreement-adjudication plan — separating noisy annotators from ambiguous guidelines. |
| [`mldata_active_learning_strategy.md`](mldata_active_learning_strategy.md) | Design an active learning loop that spends labelling budget where it changes the model — checking first that labelling is the binding constraint, choosing an acquisition strategy against the failure it must fix, and guarding the biased-pool problem the loop creates. |
| [`mldata_weak_supervision_strategy.md`](mldata_weak_supervision_strategy.md) | Generate training labels programmatically from heuristics, existing signals, and domain rules — estimating labelling-function accuracy without ground truth, handling correlated sources honestly, and keeping a hand-labelled set the weak labels can never contaminate. |

**Shape the distribution**

| Prompt | Use it to |
|---|---|
| [`mldata_class_imbalance_strategy.md`](mldata_class_imbalance_strategy.md) | Choose among resampling, class-weighting, threshold-moving, and the right metrics for imbalanced data — driven by the cost of each error type, not by reflexively rebalancing to 50/50. |
| [`mldata_data_augmentation_plan.md`](mldata_data_augmentation_plan.md) | Design modality-appropriate augmentation (image, text, audio, tabular, time-series) that expands coverage and improves robustness without distorting the target distribution or corrupting labels. |
| [`mldata_synthetic_data_strategy.md`](mldata_synthetic_data_strategy.md) | Decide when and how to use synthetic data — weighing fidelity, privacy guarantees, and distribution-shift risk — and how to validate that it helps rather than quietly degrades the model. |

**Version and contract**

| Prompt | Use it to |
|---|---|
| [`mldata_data_versioning_lineage.md`](mldata_data_versioning_lineage.md) | Design data versioning and end-to-end lineage so any model's training data can be reconstructed, audited, and traced from raw source to trained artifact for reproducibility and compliance. |
| [`mldata_data_contract_design.md`](mldata_data_contract_design.md) | Design an explicit data contract between upstream producers and downstream ML consumers — schema, semantics/units, freshness/SLA, ownership, quality expectations, and a versioned breaking-change policy — reasoning only from stated inputs. |
| [`mldata_schema_evolution_strategy.md`](mldata_schema_evolution_strategy.md) | Define how an ML pipeline's input/feature schema may change over time — backward vs forward compatibility, additive vs breaking changes, version negotiation, migration/backfill, deprecation windows — while protecting train/serve consistency and historical reproducibility. |
| [`mldata_data_contract_enforcement_ci.md`](mldata_data_contract_enforcement_ci.md) | Operationalize a data contract: validate on producer change in CI, check records at ingestion runtime, block merges on breaking-change detection, quarantine violating records, and route alerts to owners — without silent acceptance or over-strict pipelines that halt on benign changes. |

**Tool playbooks**

| Prompt | Use it to |
|---|---|
| [`mldata_dvc_data_versioning_playbook.md`](mldata_dvc_data_versioning_playbook.md) | Stand up DVC for dataset versioning and reproducible ML pipelines — remote storage, tracked data/artifacts, pipeline DAG (dvc.yaml), git-coupled data versions, and train/serve consistency — without inventing version-specific command behavior. |
| [`mldata_lakefs_data_versioning_playbook.md`](mldata_lakefs_data_versioning_playbook.md) | Stand up lakeFS for git-like versioning over object-storage data lakes — repositories, branches, commits, merges, and CI-style data validation hooks — so ML datasets are reproducible and isolated, without inventing version-specific API behavior. |

## Conventions

- **Prefix:** `mldata_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/data-for-ml`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Tool playbooks** stay version-neutral *inside* the named stack; version-specific API, pricing, and quota facts are flagged "verify against current docs" rather than asserted.

## What lives elsewhere

- Feature construction and feature stores → [`../feature-engineering/`](../feature-engineering/README.md).
- Data platform architecture and general pipeline engineering → `domain-software-engineering/devops/`.
- Deletion requests reaching trained models → [`../responsible-ai-governance/rai_machine_unlearning_deletion.md`](../responsible-ai-governance/rai_machine_unlearning_deletion.md).
