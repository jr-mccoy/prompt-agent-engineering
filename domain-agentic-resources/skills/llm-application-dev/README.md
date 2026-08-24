# LLM Application Development Skills

**Purpose:** Skills for building production-grade LLM-powered applications, including RAG systems, chain orchestration, prompt engineering, and evaluation frameworks.

---

## Overview

This category provides comprehensive skills for AI/ML engineers building applications with Large Language Models. Skills are organized by functional area to help you quickly find the right patterns for your use case.

### Quick Stats

- **Total Skills:** 13
- **Subcategories:** 4 (Chain Patterns, RAG Patterns, Prompt Management, Evaluation)
- **Skills with Bundled Resources:** 6

---

## Subcategories

### Chain Patterns

Skills for orchestrating LLM chains, agents, and multi-step workflows.

| Skill | Description | Resources |
|-------|-------------|-----------|
| [langchain-architecture](langchain-architecture/) | Design LLM applications using the LangChain framework with agents, memory, and tool integration | SKILL.md |
| [langchain-optimization](langchain-optimization/) | Optimize LangChain applications for performance, cost, and reliability with debugging and profiling tools | 2 scripts, 3 refs, 1 asset |

**When to use:** Building conversational agents, multi-step reasoning systems, or applications requiring tool use and memory management. Use `langchain-optimization` when you need to debug slow chains, reduce costs, or profile memory usage.

**Key patterns covered:**
- Agent design with tools and memory
- Chain composition (Sequential, Router, Transform)
- Memory patterns (ConversationBuffer, Summary, Entity, Vector)
- Callback handlers and tracing
- Performance profiling and cost optimization (langchain-optimization)
- Memory profiling and debugging strategies (langchain-optimization)

---

### RAG Patterns

Skills for Retrieval-Augmented Generation, embeddings, and semantic search.

| Skill | Description | Resources |
|-------|-------------|-----------|
| rag-implementation | Build RAG systems with vector databases and semantic search | SKILL.md |
| rag-pipeline-patterns | Advanced RAG optimization with chunking, retrieval tuning, and evaluation metrics (MRR, NDCG, recall@k) | 2 scripts, 4 refs, 1 asset |
| [embedding-strategies](embedding-strategies/) | Select and optimize embedding models for semantic search | SKILL.md |
| hybrid-search-implementation | Combine vector and keyword search for improved retrieval | SKILL.md |
| similarity-search-patterns | Implement efficient similarity search with vector databases | SKILL.md |
| vector-index-tuning | Optimize vector index performance (latency, recall, memory) | SKILL.md |

**When to use:** Building knowledge-grounded applications, document Q&A systems, or any application requiring retrieval of relevant context. Use `rag-pipeline-patterns` for advanced optimization and evaluation.

**Key patterns covered:**
- Chunking strategies (fixed, semantic, recursive)
- Embedding model selection (OpenAI, Cohere, open-source)
- Vector store selection (Pinecone, Weaviate, Chroma, pgvector)
- Retrieval strategies (dense, sparse, hybrid, multi-query)
- Reranking with cross-encoders
- HNSW parameter tuning and quantization
- Advanced retrieval evaluation (MRR, NDCG, recall@k) (rag-pipeline-patterns)
- Chunking analysis and optimization (rag-pipeline-patterns)

---

### Prompt Management

Skills for designing, optimizing, and managing prompts at scale.

| Skill | Description | Resources |
|-------|-------------|-----------|
| [prompt-engineering-patterns](prompt-engineering-patterns/) | Advanced prompt engineering techniques for production | 1 script, 5 refs, 2 assets |
| [prompt-optimizer](prompt-optimizer/) | Transform vague prompts into precise specifications using EARS | 4 refs |

**When to use:** Improving LLM output quality, reducing hallucinations, or establishing prompt templates for teams.

**Key patterns covered:**
- Few-shot learning and chain-of-thought prompting
- System prompt design
- EARS (Easy Approach to Requirements Syntax) methodology
- Prompt template libraries
- Output format control

---

### Evaluation

Skills for testing, benchmarking, and evaluating LLM applications.

| Skill | Description | Resources |
|-------|-------------|-----------|
| [llm-evaluation](llm-evaluation/) | Comprehensive evaluation with automated metrics and human feedback | SKILL.md |
| [promptfoo-evaluation](promptfoo-evaluation/) | Configure Promptfoo for prompt testing and model comparison | 1 ref |

**When to use:** Measuring LLM performance, A/B testing prompts, or establishing quality baselines before production deployment.

**Key patterns covered:**
- Automated evaluation metrics
- LLM-as-judge patterns (llm-rubric)
- Human feedback collection
- Regression testing for prompts
- Model comparison frameworks

---

### Utilities

General-purpose tools supporting LLM application development.

| Skill | Description | Resources |
|-------|-------------|-----------|
| [llm-icon-finder](llm-icon-finder/) | Find AI/LLM model brand icons from lobe-icons library | 2 refs |

---

## Integration Guidance

### With Existing AI/ML Skills

This category integrates with other skill categories for complete application development:

| Integration | Related Skills | Use Case |
|-------------|----------------|----------|
| **Backend Development** | `api-design-principles`, `fastapi-templates` | Expose LLM applications as APIs |
| **Cloud Infrastructure** | `kubernetes-*`, `terraform-*` | Deploy LLM workloads at scale |
| **Observability** | `distributed-tracing`, `prometheus-configuration` | Monitor LLM latency and costs |
| **Security** | `sast-configuration`, `secrets-management` | Secure API keys and prevent prompt injection |
| **Testing** | `python-testing-patterns`, `e2e-testing-patterns` | Test LLM applications reliably |

### Common Integration Patterns

#### 1. RAG Application Stack
```
rag-implementation
  ├── rag-pipeline-patterns       # Advanced optimization & evaluation
  ├── embedding-strategies        # Choose embedding model
  ├── vector-index-tuning         # Optimize retrieval
  ├── hybrid-search-implementation  # Improve recall
  └── llm-evaluation             # Measure quality
```

#### 2. Conversational Agent Stack
```
langchain-architecture
  ├── langchain-optimization       # Performance & debugging
  ├── prompt-engineering-patterns  # Design system prompts
  ├── promptfoo-evaluation        # Test prompts
  └── llm-evaluation             # Monitor production
```

#### 3. Production Deployment Stack
```
llm-application-dev/*
  ├── backend-development/fastapi-templates  # API layer
  ├── cloud-infrastructure/k8s-*            # Deployment
  ├── observability/distributed-tracing     # Monitoring
  └── security/secrets-management           # API key handling
```

### Workflow Recommendations

1. **Start with evaluation:** Use `llm-evaluation` or `promptfoo-evaluation` to establish baselines before building
2. **Design prompts systematically:** Apply `prompt-engineering-patterns` for reliable outputs
3. **Choose RAG patterns by use case:**
   - Simple Q&A → `rag-implementation`
   - High recall needs → `hybrid-search-implementation`
   - Large corpus → `vector-index-tuning` + `embedding-strategies`
4. **Integrate with infrastructure:** Connect to `cloud-infrastructure` and `observability` skills for production readiness

---

## Decision Tree: Which Skill to Use?

```
What are you building?
│
├─→ Document Q&A / Knowledge Base?
│   └─→ Start: rag-implementation
│       └─→ Scale issues? → vector-index-tuning
│       └─→ Poor recall? → hybrid-search-implementation
│       └─→ Need evaluation metrics? → rag-pipeline-patterns
│       └─→ Chunking optimization? → rag-pipeline-patterns
│
├─→ Conversational Agent / Chatbot?
│   └─→ Start: langchain-architecture
│       └─→ Prompt quality issues? → prompt-engineering-patterns
│       └─→ Performance issues? → langchain-optimization
│       └─→ High costs? → langchain-optimization
│       └─→ Memory problems? → langchain-optimization
│
├─→ Prompt Template Library?
│   └─→ Start: prompt-engineering-patterns
│       └─→ Vague requirements? → prompt-optimizer
│
├─→ LLM Testing / Benchmarking?
│   └─→ Start: promptfoo-evaluation
│       └─→ Production monitoring? → llm-evaluation
│       └─→ RAG retrieval metrics? → rag-pipeline-patterns
│
├─→ Embedding Model Selection?
│   └─→ Start: embedding-strategies
│       └─→ Performance tuning? → vector-index-tuning
│       └─→ Model comparison? → rag-pipeline-patterns
│
└─→ Debugging / Optimization?
    ├─→ LangChain chains slow? → langchain-optimization
    ├─→ Agent loops or errors? → langchain-optimization
    ├─→ RAG quality issues? → rag-pipeline-patterns
    └─→ High token costs? → langchain-optimization
```

---

## Usage

These skills provide specialized knowledge for Claude Code. They are automatically invoked when relevant to your task, or can be explicitly referenced.

### Invoking Skills

Skills activate automatically when Claude Code detects relevant context. You can also explicitly request skills:

```
"Use the rag-implementation skill to help me build a document Q&A system"
"Apply prompt-engineering-patterns to improve this prompt"
```

---

## Related Resources

- [Skills Index](../README.md) - Complete skills catalog
- [Agents Index](../../agents/README.md) - Task-specific agents
- [Backend Development Skills](../backend-development/README.md) - API and architecture patterns
- [Cloud Infrastructure Skills](../cloud-infrastructure/README.md) - Deployment patterns
- [Observability Skills](../observability/README.md) - Monitoring patterns

---

**Last Updated:** 2026-01-29
