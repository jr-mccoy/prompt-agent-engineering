# Study Tracks

Four instantiated specialization curricula. These are not generators — each sequences phases by prerequisite, pairs every phase with a build and a demonstrable checkpoint, and makes evaluation rigor a recurring deliverable rather than a final step.

**4 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- You have chosen a specialization and want the path laid out.
- A generated study plan felt too abstract to act on.

**Not here:**
- Your path does not match one of the four — use [`../mllearn_study_path_designer.md`](../mllearn_study_path_designer.md) to generate one.
- You want to reproduce a specific paper — [`../paper-reproductions/`](../paper-reproductions/README.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`mllearn_study_track_computer_vision.md`](mllearn_study_track_computer_vision.md) | An instantiated, phased computer-vision curriculum — image classification → detection/segmentation → modern architectures → deployment — with prerequisite gates, a build per phase, and checkpoints the learner can demonstrate. |
| [`mllearn_study_track_nlp_llm.md`](mllearn_study_track_nlp_llm.md) | An instantiated, phased NLP→LLM curriculum — text representation → transformers → fine-tuning → RAG/evaluation — with prerequisite gates, a build per phase, and checkpoints the learner can demonstrate. |
| [`mllearn_study_track_reinforcement_learning.md`](mllearn_study_track_reinforcement_learning.md) | An instantiated, phased RL curriculum — MDPs/tabular methods → value/policy methods → deep RL → evaluation/safety — with prerequisite gates, an environment/build per phase, and checkpoints, with RL's distinctive evaluation pitfalls made explicit. |
| [`mllearn_study_track_mlops.md`](mllearn_study_track_mlops.md) | An instantiated, phased MLOps curriculum — reproducible training → experiment tracking/registry → CI/CD → serving → monitoring — anchored to building one end-to-end pipeline, with prerequisite gates and demonstrable checkpoints. |

## Conventions

- **Prefix:** `mllearn_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/learning-ai-ml/study-tracks`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Resource types, not names.** Each track describes what kind of resource to seek at each phase and tells the learner to verify the current canonical one; no course, book, or benchmark fact is invented.
- **Every phase has a build and a checkpoint** — something made, and something demonstrable.

## What lives elsewhere

- The generator for paths these four do not cover → [`../mllearn_study_path_designer.md`](../mllearn_study_path_designer.md).
- The practitioner prompts a track points into → the lifecycle subdirectories of [`domain-AI-ML/`](../../README.md).
