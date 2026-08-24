# GenAI & LLM Engineering

Building systems *with* language models rather than training them — RAG design and its retrieval depth, evaluation and judging, guardrails, observability, cost and latency, structured output, and the interfaces through which a model reaches tools. The domain's largest non-agentic subdirectory.

**30 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Designing or debugging a retrieval-augmented system.
- Deciding between prompting, RAG, and fine-tuning.
- Evaluating an LLM system, or building the judge that evaluates it.
- Exposing tools or an MCP server to a model.

**Not here:**
- The question is prompt craft — patterns, templates, hallucination control at the prompt level → `domain-prompt-engineering/`.
- The system is an autonomous agent with a loop and delegated privileges — [`../agentic-ai-systems/`](../agentic-ai-systems/README.md).
- The model is being trained rather than applied — [`../deep-learning/`](../deep-learning/README.md).

## Prompts


**Decide the approach**

| Prompt | Use it to |
|---|---|
| [`genai_finetune_vs_rag_vs_prompt_decision.md`](genai_finetune_vs_rag_vs_prompt_decision.md) | Decide among prompt engineering, retrieval-augmented generation, and fine-tuning for an LLM task using a structured tradeoff across knowledge type, behavior change, cost, latency, and maintenance — escalating only when a cheaper option provably fails. |
| [`genai_fine_tuning_workflow.md`](genai_fine_tuning_workflow.md) | Run a disciplined fine-tuning workflow for LLMs — data prep, method choice (full SFT vs LoRA vs QLoRA), training, evaluation against a held-out set, and an honest is-it-worth-it gate. |
| [`genai_retrieval_augmented_finetuning.md`](genai_retrieval_augmented_finetuning.md) | Decide among fine-tuning, RAG, and RAFT (both together), and if RAFT, design training data with gold plus distractor documents so the model learns to ground answers in retrieved context, cite, and reject irrelevant retrievals — instead of memorizing facts that go stale. |

**Design RAG**

| Prompt | Use it to |
|---|---|
| [`genai_rag_system_design.md`](genai_rag_system_design.md) | Design a retrieval-augmented generation system across ingestion, chunking, retrieval, reranking, prompt assembly, and grounded citation — with an evaluation plan baked into the design. |
| [`genai_chunking_strategy.md`](genai_chunking_strategy.md) | Design and evaluate a chunking strategy for RAG — size, overlap, structure-awareness, and metadata — matched to document type and query type, and proven on a retrieval eval set rather than guessed. |
| [`genai_embedding_model_selection.md`](genai_embedding_model_selection.md) | Select an embedding model for retrieval by evaluating candidates on your own queries and corpus — domain fit, dimensionality, cost, and latency — rather than trusting a public leaderboard rank. |
| [`genai_graphrag_knowledge_graph_design.md`](genai_graphrag_knowledge_graph_design.md) | Decide whether graph-structured retrieval earns its construction and maintenance cost — identifying the query classes vector retrieval genuinely cannot serve, and designing extraction, traversal, and graph upkeep against those queries alone. |

**Fix retrieval**

| Prompt | Use it to |
|---|---|
| [`genai_rag_retrieval_quality_debug.md`](genai_rag_retrieval_quality_debug.md) | Root-cause a RAG system's bad answers by isolating the failing stage — retrieval, chunking, generation, or grounding — using a decision tree and stage-by-stage evidence rather than guesswork. |
| [`genai_query_rewriting_expansion.md`](genai_query_rewriting_expansion.md) | Improve retrieval by transforming the query before it reaches the index — diagnosing which failure the rewriting must fix, choosing among expansion, decomposition, and hypothetical-document techniques, and measuring retrieval rather than end-answer quality. |
| [`genai_reranking_strategy.md`](genai_reranking_strategy.md) | Add a reranking stage to a retrieval pipeline — verifying first that recall is high enough for reranking to help, choosing the reranker against the latency budget, and measuring the position of the correct document rather than aggregate relevance. |
| [`genai_vector_index_tuning.md`](genai_vector_index_tuning.md) | Tune an approximate-nearest-neighbour index for the recall the application actually needs — measuring recall against exact search rather than assuming it, navigating the recall/latency/memory/build-time trade explicitly, and re-tuning when the corpus changes. |

**Ground the answer**

| Prompt | Use it to |
|---|---|
| [`genai_citation_grounding_attribution.md`](genai_citation_grounding_attribution.md) | Make a generated answer verifiably traceable to its sources — distinguishing citation presence from citation correctness, verifying that each cited passage actually supports its claim, and handling the claims no retrieved source supports. |
| [`genai_structured_output_function_calling.md`](genai_structured_output_function_calling.md) | Make LLM structured output and function/tool calling reliable: schema design, output validation, constrained decoding, retry/repair on failure, and graceful handling of invalid or hallucinated calls. |
| [`genai_structured_extraction_at_scale.md`](genai_structured_extraction_at_scale.md) | Design an LLM extraction pipeline that runs over many documents — schema-constrained decoding, validation-and-repair loops, field-level precision/recall evaluation, batch throughput and cost, and explicit handling of partial or uncertain fields — so schema-valid output is never mistaken for semantically-correct output. |

**Evaluate**

| Prompt | Use it to |
|---|---|
| [`genai_llm_evaluation_design.md`](genai_llm_evaluation_design.md) | Design an end-to-end LLM evaluation program: task rubrics, golden and adversarial sets, blended human + automated scoring with judge calibration, and regression gates wired into CI. |
| [`genai_rag_evaluation_harness.md`](genai_rag_evaluation_harness.md) | Build a grounded evaluation harness for a RAG system — separating retrieval quality (precision/recall) from faithfulness/groundedness and end-answer quality, anchored to a golden set with human calibration. |
| [`genai_llm_as_judge_design.md`](genai_llm_as_judge_design.md) | Build a reliable LLM-as-judge: a rubric-anchored evaluator with controls for position, verbosity, and self-preference bias, calibrated against human labels with a reported agreement statistic before it is trusted to gate. |

**Control and observe**

| Prompt | Use it to |
|---|---|
| [`genai_guardrails_design.md`](genai_guardrails_design.md) | Design layered input/output guardrails for an LLM application — safety, PII, jailbreak, topical scope, and grounding — with explicit failure actions, measurable thresholds, and an evaluation set, without over-blocking legitimate use. |
| [`genai_prompt_injection_defense.md`](genai_prompt_injection_defense.md) | Defend an LLM application against prompt injection and data exfiltration — direct and indirect injection via retrieved/tool content — with privilege separation, input/output controls, and a defense-in-depth posture validated by adversarial testing. |
| [`genai_llm_observability_tracing.md`](genai_llm_observability_tracing.md) | Design observability for an LLM application — request/span tracing, token and cost accounting, latency, and online quality signals — so production behavior is debuggable, attributable, and evaluable in prod. |

**Context, cost and scale**

| Prompt | Use it to |
|---|---|
| [`genai_context_window_strategy.md`](genai_context_window_strategy.md) | Manage long-context LLM prompts: decide what to include, how to order it against lost-in-the-middle, when to compress or summarize, and how to budget tokens — proven by position-sensitivity testing, not assumption. |
| [`genai_long_context_strategy.md`](genai_long_context_strategy.md) | Decide among chunk-and-retrieve, native long-context windows, and hierarchical summarization for a workload — accounting for lost-in-the-middle recall, positional effects, and the cost/latency growth of large contexts — rather than assuming a big window solves everything. |
| [`genai_llm_cost_latency_optimization.md`](genai_llm_cost_latency_optimization.md) | Cut LLM cost and latency without quality loss: model routing, caching, batching, prompt compression, and distillation — each gated by an eval that proves quality held, with cost/latency measured before and after. |
| [`genai_multilingual_design.md`](genai_multilingual_design.md) | Design a multilingual LLM system — tokenizer/script coverage, cross-lingual transfer, unified vs language-specific models, and per-language evaluation — so quality holds across the full language set instead of collapsing on low-resource languages. |
| [`genai_synthetic_data_with_llms.md`](genai_synthetic_data_with_llms.md) | Generate synthetic training or evaluation data with LLMs without contaminating eval sets, amplifying bias, or collapsing diversity — with provenance tracking, quality filtering, and a contamination firewall. |

**Tool interfaces**

| Prompt | Use it to |
|---|---|
| [`genai_mcp_tool_interface_design.md`](genai_mcp_tool_interface_design.md) | Design tool and server interfaces a model can use correctly — naming and describing tools for a reader with no context, shaping responses so a model can act on them, and treating tool output as untrusted content that enters the model's context. |

**Vector-DB playbooks**

| Prompt | Use it to |
|---|---|
| [`genai_pgvector_vector_db_playbook.md`](genai_pgvector_vector_db_playbook.md) | Stand up vector search in PostgreSQL with pgvector for RAG/embedding workloads — schema and index choice (HNSW/IVFFlat), distance metric matching, hybrid search, ingestion, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks. |
| [`genai_pinecone_vector_db_playbook.md`](genai_pinecone_vector_db_playbook.md) | Design a RAG/embedding retrieval layer on Pinecone — index/namespace design, metric matching, metadata filtering, upserts, hybrid search, and a retrieval-quality vs. infra-health evaluation plan — without inventing version-specific API behavior, pod/pricing specs, or benchmark numbers. |
| [`genai_weaviate_vector_db_playbook.md`](genai_weaviate_vector_db_playbook.md) | Design a RAG/embedding retrieval layer on Weaviate — collection schema, vectorizer vs. bring-your-own-vectors, metric matching, native hybrid (BM25 + vector) search, multi-tenancy, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks. |
| [`genai_milvus_vector_db_playbook.md`](genai_milvus_vector_db_playbook.md) | Design a high-scale RAG/embedding retrieval layer on Milvus — collection schema and partitions, index type selection (HNSW/IVF/DiskANN-family), metric matching, scalar filtering, sharding/consistency, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks. |

## Conventions

- **Prefix:** `genai_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/genai-llm-engineering`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Vendor playbooks** stay version-neutral *inside* the named stack; API, pricing, and quota specifics are flagged for verification rather than asserted.
- **Model-neutral:** prompts do not assume a provider or model family; the user names theirs.

## What lives elsewhere

- Prompt patterns, RAG prompt templates, hallucination control at the prompt level → `domain-prompt-engineering/{rag-prompts,hallucination-control,instruction-design}/`.
- LLM *application* security review at the app layer → `domain-software-engineering/analysis/security/security_llm_application_review.md`.
- Serving-side LLM inference optimization (KV cache, speculative decoding) → [`../model-optimization-efficiency/mlopt_llm_inference_serving_optimization.md`](../model-optimization-efficiency/mlopt_llm_inference_serving_optimization.md).
- Ready-to-run LLM app scaffolds → `domain-agentic-resources/skills/llm-application-dev/`.
