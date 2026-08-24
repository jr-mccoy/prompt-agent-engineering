# LangChain Debugging Guide

Comprehensive troubleshooting guide for common LangChain issues.

---

## Quick Diagnostics

### Enable Verbose Logging

```python
import langchain
langchain.debug = True  # Full debug output

# Or use LangSmith tracing
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"
```

### Check Token Usage

```python
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    result = chain.invoke(input)
    print(f"Tokens: {cb.total_tokens}")
    print(f"Cost: ${cb.total_cost}")
```

---

## Common Issues by Category

### 1. Agent Issues

#### Issue: Agent Loops Indefinitely

**Symptoms:**
- Same action repeated
- Agent never finishes
- Timeout errors

**Causes:**
- Poor tool descriptions
- No clear termination condition
- Tool returning unhelpful results

**Solutions:**
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=10,  # Hard limit
    early_stopping_method="generate",  # Try to output when stuck
    handle_parsing_errors=True
)
```

**Prevention:**
- Write clear, specific tool descriptions
- Include example inputs in tool docstrings
- Add "when NOT to use" in descriptions

---

#### Issue: Wrong Tool Selection

**Symptoms:**
- Agent picks calculator for text tasks
- Wrong tool for the job
- Inefficient tool sequences

**Causes:**
- Ambiguous tool descriptions
- Overlapping tool capabilities
- Missing the right tool

**Solutions:**
```python
# Better tool descriptions
@tool
def search_database(query: str) -> str:
    """
    Search the internal company database for employee or project information.
    Use this for questions about people, teams, or internal projects.
    Do NOT use for general knowledge questions or calculations.

    Example: "Find all projects in the engineering team"
    """
    return database.search(query)
```

---

#### Issue: Parsing Errors

**Symptoms:**
- "Could not parse LLM output"
- Agent crashes on output
- Malformed action strings

**Causes:**
- LLM not following output format
- Extra text in response
- JSON parsing failures

**Solutions:**
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True,  # Retry on parse errors
    # Or custom handler:
    handle_parsing_errors="I couldn't parse that. Please format as Action: ... Action Input: ..."
)
```

---

### 2. Chain Issues

#### Issue: Context Window Exceeded

**Symptoms:**
- "Maximum context length exceeded"
- Token limit errors
- Truncated responses

**Causes:**
- Too much memory/history
- Large documents in context
- Inefficient prompts

**Solutions:**
```python
# Use bounded memory
from langchain.memory import ConversationSummaryBufferMemory
memory = ConversationSummaryBufferMemory(max_token_limit=2000, llm=llm)

# Compress retrieved documents
from langchain.retrievers import ContextualCompressionRetriever
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)
```

---

#### Issue: Slow Chain Execution

**Symptoms:**
- High latency
- Timeout in production
- Poor user experience

**Causes:**
- Too many LLM calls
- Large prompts
- No caching

**Solutions:**
```python
# Enable caching
from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache
set_llm_cache(SQLiteCache(database_path=".langchain.db"))

# Use streaming for perceived performance
llm = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

# Batch operations
results = llm.generate(["prompt1", "prompt2", "prompt3"])
```

---

#### Issue: Inconsistent Outputs

**Symptoms:**
- Different results for same input
- Unpredictable behavior
- Hard to debug

**Causes:**
- High temperature
- No seed setting
- Non-deterministic tools

**Solutions:**
```python
# Set temperature to 0 for determinism
llm = ChatOpenAI(temperature=0)

# Use model seed if available
llm = ChatOpenAI(model_kwargs={"seed": 42})

# Cache for consistency
set_llm_cache(InMemoryCache())
```

---

### 3. Retrieval Issues

#### Issue: Irrelevant Retrieved Documents

**Symptoms:**
- Retrieved docs don't match query
- Poor answer quality
- Hallucinations due to bad context

**Causes:**
- Poor embedding quality
- Bad chunking strategy
- Query not matching document style

**Solutions:**
```python
# Use hybrid search
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.3, 0.7]
)

# Add reranking
from sentence_transformers import CrossEncoder
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Use query transformation
from langchain.retrievers.multi_query import MultiQueryRetriever
retriever = MultiQueryRetriever.from_llm(base_retriever, llm)
```

---

#### Issue: Missing Relevant Documents

**Symptoms:**
- "I don't have information about that"
- Known docs not retrieved
- Low recall

**Causes:**
- k too low
- Semantic gap between query and docs
- Documents not indexed

**Solutions:**
```python
# Increase k
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# Use HyDE for query transformation
hyde = HypotheticalDocumentEmbedder.from_llm(llm, base_embeddings)

# Verify indexing
print(f"Total documents: {vectorstore._collection.count()}")
```

---

### 4. Memory Issues

#### Issue: Memory Not Persisting

**Symptoms:**
- Context lost between calls
- Agent "forgets" earlier conversation
- Memory appears empty

**Causes:**
- New memory instance each call
- Memory not passed to chain
- Wrong memory key

**Solutions:**
```python
# Ensure same memory instance
memory = ConversationBufferMemory(memory_key="history")

chain = ConversationChain(
    llm=llm,
    memory=memory,  # Must be same instance
    verbose=True
)

# Verify memory key matches prompt
print(chain.prompt.input_variables)  # Should include memory_key
```

---

#### Issue: Memory Growing Too Large

**Symptoms:**
- Increasing latency over time
- Token limits hit
- High costs

**Causes:**
- Using unbounded memory
- No cleanup strategy
- Large messages

**Solutions:**
```python
# Use bounded memory
memory = ConversationBufferWindowMemory(k=10)

# Or use summary memory
memory = ConversationSummaryMemory(llm=cheap_llm)

# Add token monitoring
def check_memory_size(memory):
    tokens = count_memory_tokens(memory)
    if tokens > 3000:
        print(f"WARNING: Memory at {tokens} tokens")
```

---

## Debugging Workflow

### Step 1: Isolate the Problem

```python
# Test LLM directly
response = llm.invoke("Test prompt")
print(response)

# Test retriever directly
docs = retriever.get_relevant_documents("test query")
print(docs)

# Test memory directly
memory.save_context({"input": "test"}, {"output": "response"})
print(memory.load_memory_variables({}))
```

### Step 2: Enable Tracing

```python
# Local debugging
import langchain
langchain.debug = True

# Or custom callback
class DebugCallback(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"LLM Input: {prompts}")

    def on_llm_end(self, response, **kwargs):
        print(f"LLM Output: {response}")
```

### Step 3: Check Intermediate Steps

```python
# For agents
result = agent_executor.invoke(
    {"input": "query"},
    return_intermediate_steps=True
)
for step in result["intermediate_steps"]:
    print(f"Action: {step[0]}")
    print(f"Result: {step[1]}")
```

### Step 4: Test with Minimal Example

```python
# Reduce to simplest case that reproduces issue
simple_chain = LLMChain(llm=llm, prompt=simple_prompt)
result = simple_chain.invoke({"input": "test"})
```

---

## Error Message Reference

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| "Maximum context length exceeded" | Too much input | Reduce memory, compress docs |
| "Could not parse LLM output" | Malformed agent response | handle_parsing_errors=True |
| "Rate limit exceeded" | Too many API calls | Add retry logic, reduce calls |
| "Invalid API key" | Auth issue | Check OPENAI_API_KEY |
| "Model not found" | Wrong model name | Verify model string |
| "Tool X not found" | Tool not in list | Add tool to tools list |

---

## Production Debugging Tips

1. **Always set timeouts:**
   ```python
   llm = ChatOpenAI(request_timeout=30)
   ```

2. **Add error logging:**
   ```python
   try:
       result = chain.invoke(input)
   except Exception as e:
       logger.error(f"Chain failed: {e}", exc_info=True)
       raise
   ```

3. **Use LangSmith for production tracing:**
   - Visual debugging of chains
   - Token usage tracking
   - Latency analysis

4. **Implement graceful degradation:**
   ```python
   try:
       return primary_chain.invoke(input)
   except:
       return fallback_chain.invoke(input)
   ```

---

**Related:** See `chain_analyzer.py` for automated performance analysis.
