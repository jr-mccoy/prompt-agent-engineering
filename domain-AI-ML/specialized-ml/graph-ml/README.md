# Graph ML

Machine learning on relational structure — task framing, link prediction, fraud on heterogeneous graphs, and scaling GNNs past what fits in memory. Graph splits leak in ways tabular splits do not, which is why framing comes first.

**4 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- The data is naturally a graph and the relationships carry the signal.
- Link prediction, node classification, or graph-level prediction.
- A GNN works on a sample and will not scale to the full graph.

**Not here:**
- The graph is being used for *retrieval* to feed a language model — [`../../genai-llm-engineering/genai_graphrag_knowledge_graph_design.md`](../../genai-llm-engineering/genai_graphrag_knowledge_graph_design.md).
- The relational structure is incidental and tabular features suffice — [`../../classical-ml-modeling/`](../../classical-ml-modeling/README.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`graphml_task_framing.md`](graphml_task_framing.md) | Design a graph machine-learning approach — frame the task (node/edge/graph level), choose a GNN family, plan neighbor sampling for scale, and prevent the leakage that graph splits invite. |
| [`graphml_link_prediction_design.md`](graphml_link_prediction_design.md) | Frame a link-prediction task on a graph — define what an edge means, choose a negative-sampling strategy, pick transductive vs inductive (and temporal) splits, and select ranking metrics — without leaking future edges into training. |
| [`graphml_fraud_graph_patterns.md`](graphml_fraud_graph_patterns.md) | Model fraud and abuse on heterogeneous graphs (users/devices/transactions) under extreme label scarcity and adversarial drift — with time-respecting features and operating-point evaluation, not just AUC. |
| [`graphml_gnn_scalability.md`](graphml_gnn_scalability.md) | Scale GNN training to large graphs — choose neighbor sampling vs full-graph training, partition and distribute, and reason about memory/throughput tradeoffs and how sampling changes accuracy and the effective receptive field. |

## Conventions

- **Prefix:** `graphml_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/graph-ml`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- GraphRAG and knowledge-graph retrieval → [`../../genai-llm-engineering/genai_graphrag_knowledge_graph_design.md`](../../genai-llm-engineering/genai_graphrag_knowledge_graph_design.md).
- Fraud detection without graph structure → [`../../classical-ml-modeling/mlmodel_imbalanced_classification_approach.md`](../../classical-ml-modeling/mlmodel_imbalanced_classification_approach.md).
