# RAG Architecture — Advanced Chunking, Retrieval, and Evaluation

## Chunking Strategies (3 and 4)

### 3. Document Structure-Aware Chunking

```python
from langchain.text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
]

md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

# Each chunk includes header metadata
chunks = md_splitter.split_text(markdown_doc)
# chunks[0].metadata = {"h1": "Main Title", "h2": "Section"}
```

### 4. Parent-Child Chunking

```python
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore

# Small chunks for retrieval, large chunks for context
child_splitter = RecursiveCharacterTextSplitter(chunk_size=200)
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=InMemoryStore(),
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

# Retrieves on small chunks, returns parent chunks
retriever.add_documents(documents)
results = retriever.get_relevant_documents("query")
```

---

## Advanced Retrieval Patterns (3, 4, and 5)

### 3. Self-Query Retrieval (Metadata Filtering)

```python
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

metadata_field_info = [
    AttributeInfo(name="category", description="Document category: 'technical', 'policy', 'faq'", type="string"),
    AttributeInfo(name="date", description="Document publication date", type="date"),
    AttributeInfo(name="author", description="Document author name", type="string")
]

retriever = SelfQueryRetriever.from_llm(
    llm=ChatOpenAI(temperature=0),
    vectorstore=vectorstore,
    document_contents="Company documentation and policies",
    metadata_field_info=metadata_field_info
)

# Query: "What technical docs did John write in 2024?"
# Auto-generates filter: category='technical' AND author='John' AND date>=2024
```

### 4. Hypothetical Document Embeddings (HyDE)

```python
from langchain.chains import HypotheticalDocumentEmbedder
from langchain.prompts import PromptTemplate

hyde_prompt = PromptTemplate(
    input_variables=["question"],
    template="""Write a paragraph that would answer this question:
Question: {question}

Answer paragraph:"""
)

hyde_embeddings = HypotheticalDocumentEmbedder.from_llm(
    llm=ChatOpenAI(temperature=0),
    base_embeddings=OpenAIEmbeddings(),
    prompt=hyde_prompt
)

vectorstore = Chroma.from_documents(documents, hyde_embeddings)
```

### 5. Contextual Compression

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever()
)

# Returns only relevant parts of documents
compressed_docs = compression_retriever.get_relevant_documents("query")
```

---

## RAG Prompt Engineering

### Contextual Prompt with Citations

```python
prompt_template = """Answer the question based on the context below. Include citations using [1], [2], etc.
If you cannot answer based on the context, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer (with citations):"""
```

### With Confidence Scoring

```python
prompt_template = """Answer the question using the context. Provide a confidence score (0-100%) for your answer.

Context:
{context}

Question: {question}

Answer:
Confidence:"""
```

---

## Evaluation Metrics

### Core Retrieval Metrics

```python
import numpy as np
from typing import List

def mean_reciprocal_rank(results: List[List[str]], relevant: List[List[str]]) -> float:
    """Calculate Mean Reciprocal Rank (MRR)."""
    mrrs = []
    for res, rel in zip(results, relevant):
        for i, doc_id in enumerate(res):
            if doc_id in rel:
                mrrs.append(1.0 / (i + 1))
                break
        else:
            mrrs.append(0.0)
    return np.mean(mrrs)

def recall_at_k(results: List[List[str]], relevant: List[List[str]], k: int) -> float:
    """Calculate Recall@k."""
    recalls = []
    for res, rel in zip(results, relevant):
        res_k = set(res[:k])
        rel_set = set(rel)
        if len(rel_set) > 0:
            recalls.append(len(res_k & rel_set) / len(rel_set))
        else:
            recalls.append(1.0)
    return np.mean(recalls)

def ndcg_at_k(results: List[List[str]], relevant: List[List[str]], k: int) -> float:
    """Calculate Normalized Discounted Cumulative Gain (NDCG@k)."""
    def dcg(scores):
        return sum((2**s - 1) / np.log2(i + 2) for i, s in enumerate(scores))

    ndcgs = []
    for res, rel in zip(results, relevant):
        rel_set = set(rel)
        scores = [1 if doc_id in rel_set else 0 for doc_id in res[:k]]
        ideal_scores = sorted(scores, reverse=True)
        dcg_score = dcg(scores)
        idcg_score = dcg(ideal_scores)
        ndcgs.append(dcg_score / idcg_score if idcg_score > 0 else 0)
    return np.mean(ndcgs)
```

### Evaluation Benchmarks

| Metric | Poor | Acceptable | Good | Excellent |
|--------|------|------------|------|-----------|
| MRR | < 0.3 | 0.3-0.5 | 0.5-0.7 | > 0.7 |
| Recall@5 | < 0.5 | 0.5-0.7 | 0.7-0.85 | > 0.85 |
| NDCG@5 | < 0.4 | 0.4-0.6 | 0.6-0.8 | > 0.8 |
| Latency (p95) | > 500ms | 200-500ms | 100-200ms | < 100ms |

### Context Window Optimization

```python
import tiktoken

def adaptive_context_selection(
    documents: list,
    max_tokens: int = 3000,
    model: str = "gpt-4"
) -> list:
    """Select documents that fit within token budget."""
    encoding = tiktoken.encoding_for_model(model)
    selected = []
    current_tokens = 0

    for doc in documents:
        doc_tokens = len(encoding.encode(doc.page_content))
        if current_tokens + doc_tokens <= max_tokens:
            selected.append(doc)
            current_tokens += doc_tokens
        else:
            break

    return selected
```

---

## Production Checklist

Before deploying RAG pipelines:

- [ ] **Chunking strategy validated** - Tested multiple strategies on your data
- [ ] **Embedding model benchmarked** - Evaluated on representative queries
- [ ] **Retrieval metrics established** - MRR, Recall@k baselines set
- [ ] **Reranking evaluated** - Tested impact on quality vs latency
- [ ] **Hybrid search considered** - BM25 + dense if exact terms matter
- [ ] **Context window managed** - Token budgets enforced
- [ ] **Metadata filtering implemented** - For scoped retrieval
- [ ] **Evaluation pipeline automated** - Regression testing on retrieval
- [ ] **Monitoring configured** - Track retrieval latency and quality
- [ ] **Fallback strategies defined** - Handle empty/poor retrieval
