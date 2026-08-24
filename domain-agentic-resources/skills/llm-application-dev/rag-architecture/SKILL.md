---
name: rag-architecture
description: Design and optimize Retrieval-Augmented Generation (RAG) systems for production LLM applications. Covers end-to-end RAG architecture including chunking strategies, retrieval patterns, reranking, prompt engineering, and evaluation metrics. Use when building knowledge-grounded AI, document Q&A systems, or optimizing existing RAG quality. Triggers on "RAG", "chunking strategy", "retrieval evaluation", "MRR", "NDCG", "recall@k", "reranking", "document Q&A".
metadata:
  tags:
    - ai-applications
    - chunking
    - debugging
    - embedding
    - evaluation
    - llm
    - pipeline
    - rag
    - retrieval-augmented-generation
    - reranking
  updated: "2026-04-11"
---
# RAG Architecture

Master Retrieval-Augmented Generation (RAG) from initial implementation through production optimization — chunking, retrieval, reranking, evaluation, and prompt engineering in one skill.

## Purpose

This skill provides comprehensive patterns for building and optimizing RAG pipelines. It covers foundational setup, advanced chunking strategies, embedding model selection, sophisticated retrieval patterns, reranking techniques, RAG-specific prompt engineering, and evaluation metrics.

## When to Use This Skill

Use this skill when you need to:
- Build Q&A systems over proprietary documents
- Create chatbots with current, factual information
- Implement semantic search with natural language queries
- Reduce hallucinations with grounded responses
- Choose optimal chunking strategies for your document types
- Implement hybrid or multi-stage retrieval
- Add reranking to improve top-k results
- Evaluate RAG performance with proper metrics (MRR, NDCG, recall@k)
- Debug poor retrieval or irrelevant context issues

## When NOT to Use This Skill

Do NOT use this skill when:
- Choosing or tuning vector databases and indexes (use `vector-search-optimization`)
- Selecting or benchmarking embedding models (use `embedding-strategies`)
- Optimizing LangChain chains generally (use `langchain-optimization`)
- Issues are with the LLM response, not retrieval (use `prompt-engineering-patterns`)

---

## Quick Start

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 1. Load documents
loader = DirectoryLoader('./docs', glob="**/*.txt")
documents = loader.load()

# 2. Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = text_splitter.split_documents(documents)

# 3. Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. Create retrieval chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
    return_source_documents=True
)

# 5. Query
result = qa_chain({"query": "What are the main features?"})
print(result['result'])
print(result['source_documents'])
```

---

## Chunking Strategies

### Strategy Selection Framework

```
Document Type?
│
├─→ Structured (Markdown, HTML, Code)
│   └─→ Use: Header-based or AST-based splitting
│
├─→ Conversational (Chat logs, Q&A)
│   └─→ Use: Semantic chunking with speaker boundaries
│
├─→ Technical Documentation
│   └─→ Use: Recursive splitting with larger chunks (1000-1500 tokens)
│
├─→ Legal/Dense Text
│   └─→ Use: Sentence-based with high overlap (30-40%)
│
└─→ Mixed Content
    └─→ Use: Hybrid approach with document-type detection
```

### Tuning Guidelines

| Parameter | Small Chunks (200-500) | Medium (500-1000) | Large (1000-2000) |
|-----------|------------------------|-------------------|-------------------|
| Retrieval Precision | High | Medium | Lower |
| Context Completeness | Low | Medium | High |
| Token Cost | Low | Medium | Higher |
| Best For | Specific Q&A | General Q&A | Summarization |

### 1. Recursive Character Splitting (General Purpose)

```python
from langchain.text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=[
        "\n\n",        # Paragraphs first
        "\n",          # Then lines
        ". ",          # Then sentences
        ", ",          # Then clauses
        " ",           # Then words
        ""             # Finally characters
    ]
)

# Language-specific separators
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=1000,
    chunk_overlap=200
)
```

### 2. Semantic Chunking

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import OpenAIEmbeddings

splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",  # or "standard_deviation", "interquartile"
    breakpoint_threshold_amount=95
)
```

**Breakpoint Types:**

| Type | Description | When to Use |
|------|-------------|-------------|
| `percentile` | Break at Nth percentile of distances | Consistent chunk counts |
| `standard_deviation` | Break at N std devs above mean | Outlier-based boundaries |
| `interquartile` | Break at IQR-based threshold | Robust to outliers |

Chunking Strategies 3–4 (Structure-Aware with `MarkdownHeaderTextSplitter`, Parent-Child with `ParentDocumentRetriever`), Advanced Retrieval Patterns 3–5 (Self-Query metadata filtering, HyDE, Contextual Compression), RAG Prompt Engineering templates, Evaluation Metrics (MRR, Recall@k, NDCG@k implementations + benchmarks + context window optimization), and the Production Checklist are in the reference file.

See [references/advanced-chunking-retrieval-evaluation.md](references/advanced-chunking-retrieval-evaluation.md)

---

## Advanced Retrieval Patterns

### 1. Hybrid Search (Dense + Sparse)

```python
from langchain.retrievers import BM25Retriever, EnsembleRetriever

bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 10

dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

hybrid_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.3, 0.7]  # Tune based on your data
)
```

**Weight Tuning:**

| Document Type | BM25 Weight | Dense Weight |
|---------------|-------------|--------------|
| Technical docs (exact terms matter) | 0.4-0.5 | 0.5-0.6 |
| Conversational (semantic meaning) | 0.2-0.3 | 0.7-0.8 |
| Mixed content | 0.3 | 0.7 |

### 2. Multi-Query Retrieval

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""Generate 3 different versions of the question to retrieve relevant documents.
Original question: {question}

Alternative questions:"""
)

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=ChatOpenAI(temperature=0.3),
    prompt=QUERY_PROMPT
)
```

---

## Reranking Patterns

### 1. Cross-Encoder Reranking

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_documents(query: str, documents: list, top_k: int = 5):
    pairs = [[query, doc.page_content] for doc in documents]
    scores = reranker.predict(pairs)
    scored_docs = list(zip(documents, scores))
    scored_docs.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, score in scored_docs[:top_k]]

# Usage: over-fetch then rerank
initial_docs = vectorstore.similarity_search(query, k=20)
reranked_docs = rerank_documents(query, initial_docs, top_k=5)
```

### 2. Cohere Rerank

```python
import cohere

co = cohere.Client("your-api-key")

def cohere_rerank(query: str, documents: list, top_k: int = 5):
    docs_text = [doc.page_content for doc in documents]
    results = co.rerank(query=query, documents=docs_text, top_n=top_k, model="rerank-english-v2.0")
    return [documents[r.index] for r in results.results]
```

### 3. Maximal Marginal Relevance (MMR)

```python
# Built into most vector stores - balances relevance with diversity
results = vectorstore.max_marginal_relevance_search(
    query,
    k=5,              # Return 5 documents
    fetch_k=20,       # Consider top 20
    lambda_mult=0.5   # Balance: 1.0=relevance, 0.0=diversity
)
```

---

## Best Practices

1. **Chunk Size**: Balance between context and specificity (500-1000 tokens)
2. **Overlap**: Use 10-20% overlap to preserve context at boundaries
3. **Metadata**: Include source, page, timestamp for filtering and debugging
4. **Hybrid Search**: Combine semantic and keyword search for best results
5. **Reranking**: Improve top results with cross-encoder
6. **Citations**: Always return source documents for transparency
7. **Evaluation**: Continuously test retrieval quality and answer accuracy
8. **Monitoring**: Track retrieval metrics in production

## Common Issues

- **Poor Retrieval**: Check embedding quality, chunk size, query formulation
- **Irrelevant Results**: Add metadata filtering, use hybrid search, rerank
- **Missing Information**: Ensure documents are properly indexed
- **Slow Queries**: Optimize vector store, use caching, reduce k
- **Hallucinations**: Improve grounding prompt, add verification step

## Verification

To validate your RAG system is production-ready:

1. **Retrieval Quality**: MRR >= 0.5 and Recall@5 >= 0.7 on your test set
2. **Answer Quality**: Spot-check 20+ queries for groundedness and accuracy
3. **Latency**: p95 retrieval latency < 500ms
4. **Edge Cases**: Test with empty results, out-of-domain queries, ambiguous questions
5. **Regression**: Automated evaluation pipeline runs on every chunking/retrieval change
6. **Token Budget**: Context never exceeds model limit; adaptive selection in place

## Related Skills

- `embedding-strategies` - Deep dive on embedding model selection and optimization
- `vector-search-optimization` - Vector database implementation, index tuning, and hybrid search
- `llm-evaluation` - End-to-end RAG and LLM output evaluation
- `langchain-architecture` - LangChain framework patterns for RAG chains
- `langchain-optimization` - Optimizing LangChain-based RAG applications

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-chunking-retrieval-evaluation.md` | Chunking Strategies 3–4 (Structure-Aware, Parent-Child), Advanced Retrieval Patterns 3–5 (Self-Query, HyDE, Contextual Compression), RAG Prompt Engineering templates (citations + confidence scoring), Evaluation Metrics (MRR/Recall@k/NDCG@k implementations + benchmarks table + adaptive context selection), Production Checklist (10 items) |
