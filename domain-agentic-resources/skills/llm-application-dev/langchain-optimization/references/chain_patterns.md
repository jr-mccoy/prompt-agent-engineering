# LangChain Chain Patterns Reference

Reference guide for common chain composition patterns and their optimization strategies.

---

## Chain Types Overview

### 1. LLMChain (Basic)

**Structure:** Prompt Template → LLM → Output

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        input_variables=["topic"],
        template="Write about {topic}"
    )
)
```

**Optimization:**
- Enable caching for repeated similar inputs
- Use streaming for long outputs
- Consider using cheaper models for simple prompts

---

### 2. SequentialChain

**Structure:** Chain1 → Chain2 → Chain3 → Output

```python
from langchain.chains import SequentialChain

overall_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["input"],
    output_variables=["final_output"]
)
```

**Optimization:**
- Minimize chain count (each chain = LLM call)
- Combine chains when outputs can be merged into one prompt
- Use `SimpleSequentialChain` for single-output chains

---

### 3. RouterChain

**Structure:** Input → Router → [Chain A | Chain B | Chain C] → Output

```python
from langchain.chains.router import MultiPromptChain

chain = MultiPromptChain(
    router_chain=router,
    destination_chains={"physics": physics_chain, "math": math_chain},
    default_chain=default_chain
)
```

**Optimization:**
- Use classification model or embeddings for routing (cheaper than LLM)
- Cache routing decisions for similar queries
- Implement fallback to default chain

---

### 4. MapReduceChain

**Structure:** [Doc1, Doc2, Doc3] → Map(summarize each) → Reduce(combine) → Output

```python
from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="map_reduce")
```

**Optimization:**
- Batch map operations where possible
- Use cheaper model for map step, better model for reduce
- Consider `refine` chain type for better quality (sequential but higher quality)

---

### 5. RetrievalQA Chain

**Structure:** Query → Retriever → [Docs] → LLM → Answer

```python
from langchain.chains import RetrievalQA

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
```

**Optimization:**
- Optimize retriever k value (fewer docs = faster, less context)
- Use contextual compression to reduce token usage
- Enable streaming for better UX
- Cache common queries

---

## Chain Type Selection Guide

| Use Case | Recommended Chain | Reason |
|----------|-------------------|--------|
| Simple Q&A | LLMChain | Minimal overhead |
| Document Q&A | RetrievalQA | Built-in retrieval |
| Multi-step reasoning | SequentialChain | Clear step separation |
| Large document summary | MapReduceChain | Parallelizable |
| Task routing | RouterChain | Efficient specialization |
| Agent with tools | AgentExecutor | Tool use built-in |

---

## Chain Type Performance Comparison

| Chain Type | LLM Calls | Parallelizable | Caching Benefit |
|------------|-----------|----------------|-----------------|
| LLMChain | 1 | N/A | High |
| SequentialChain | N (chain count) | No | Medium |
| MapReduceChain | N+1 (docs + reduce) | Yes (map step) | Medium |
| RefineChain | N (docs) | No | Low |
| RouterChain | 2 (route + execute) | No | High (routing) |

---

## Anti-Patterns to Avoid

### 1. Chain Explosion
**Problem:** Too many chains for simple tasks
```python
# Bad: 5 chains for what could be 1 prompt
chain1 → chain2 → chain3 → chain4 → chain5
```
**Solution:** Combine into fewer prompts with structured output

### 2. No Caching on Repeated Patterns
**Problem:** Same queries hit LLM repeatedly
**Solution:** Enable `SQLiteCache` or `SemanticCache`

### 3. Using Expensive Models for Simple Tasks
**Problem:** GPT-4 for classification or routing
**Solution:** Use GPT-3.5-turbo or embeddings for simple tasks

### 4. Synchronous Processing of Independent Tasks
**Problem:** Sequential when parallel is possible
**Solution:** Use `asyncio` or batch processing for map operations

---

## Advanced Patterns

### Conditional Chains

```python
def conditional_chain(input_data):
    if should_use_retrieval(input_data):
        return retrieval_chain.invoke(input_data)
    else:
        return simple_chain.invoke(input_data)
```

### Fallback Chains

```python
from langchain.chains import FallbackChain

chain = FallbackChain(
    primary_chain=complex_chain,
    fallback_chain=simple_chain
)
```

### Caching Wrapper

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_chain_invoke(query: str) -> str:
    return chain.invoke({"query": query})["result"]
```

---

## Monitoring Chains

### Token Tracking

```python
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    result = chain.invoke(input)
    print(f"Tokens: {cb.total_tokens}, Cost: ${cb.total_cost}")
```

### Timing

```python
import time

start = time.time()
result = chain.invoke(input)
print(f"Latency: {(time.time() - start) * 1000:.0f}ms")
```

### Logging

```python
import langchain
langchain.debug = True  # Verbose logging
```

---

**Related:** See `debugging_guide.md` for troubleshooting chain issues.
