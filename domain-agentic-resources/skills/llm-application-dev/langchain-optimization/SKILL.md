---
name: langchain-optimization
description: Optimize LangChain applications for performance, cost, and reliability. Use when debugging slow chains, reducing token costs, profiling memory usage, improving agent reliability, or troubleshooting LangChain workflows. Triggers on "LangChain slow", "chain performance", "reduce LLM costs", "debug agent", "memory issues", "optimize chains".
metadata:
  tags:
    - ai-applications
    - debugging
    - langchain
    - llm
    - optimization
    - performance
  updated: "2026-04-11"
---
# LangChain Optimization

Master performance tuning, cost optimization, and debugging techniques for production LangChain applications.

## Purpose

This skill provides advanced optimization patterns for LangChain applications that are already functional but need improvement in performance, cost efficiency, or reliability. It complements the foundational `langchain-architecture` skill by focusing specifically on optimization and troubleshooting.

## When to Use This Skill

Use this skill when you need to:
- Debug slow or unresponsive LangChain chains
- Reduce LLM API costs in production
- Profile and optimize memory consumption
- Troubleshoot agent decision-making issues
- Improve chain reliability and error handling
- Implement caching strategies for LangChain
- Monitor and trace chain execution

## When NOT to Use This Skill

Do NOT use this skill when:
- Building a new LangChain application from scratch (use `langchain-architecture`)
- Implementing basic RAG systems (use `rag-implementation`)
- Selecting embedding models (use `embedding-strategies`)
- You haven't identified a specific performance problem yet

---

## Performance Optimization Patterns

### 1. Chain Execution Profiling

**Identify bottlenecks before optimizing:**

```python
import time
from langchain.callbacks.base import BaseCallbackHandler
from typing import Dict, Any, List

class PerformanceProfiler(BaseCallbackHandler):
    """Profile LangChain chain execution times."""

    def __init__(self):
        self.timings: Dict[str, List[float]] = {}
        self.current_chain: str = None
        self.chain_start: float = None

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs):
        self.current_chain = serialized.get("name", "unknown")
        self.chain_start = time.time()

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs):
        if self.chain_start:
            elapsed = time.time() - self.chain_start
            if self.current_chain not in self.timings:
                self.timings[self.current_chain] = []
            self.timings[self.current_chain].append(elapsed)

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs):
        self._start_timer("llm_call")

    def on_llm_end(self, response, **kwargs):
        self._end_timer("llm_call")

    def on_retriever_start(self, serialized: Dict[str, Any], query: str, **kwargs):
        self._start_timer("retrieval")

    def on_retriever_end(self, documents, **kwargs):
        self._end_timer("retrieval")

    def _start_timer(self, name: str):
        self._current_start = time.time()
        self._current_name = name

    def _end_timer(self, name: str):
        elapsed = time.time() - self._current_start
        if name not in self.timings:
            self.timings[name] = []
        self.timings[name].append(elapsed)

    def get_report(self) -> str:
        report = ["Performance Report", "=" * 50]
        for name, times in self.timings.items():
            avg = sum(times) / len(times)
            total = sum(times)
            report.append(f"{name}:")
            report.append(f"  Calls: {len(times)}")
            report.append(f"  Avg: {avg:.3f}s")
            report.append(f"  Total: {total:.3f}s")
        return "\n".join(report)

# Usage
profiler = PerformanceProfiler()
chain.invoke({"query": "test"}, config={"callbacks": [profiler]})
print(profiler.get_report())
```

### 2. LLM Call Optimization

**Reduce latency and costs with strategic caching:**

```python
from langchain.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
import hashlib

# Simple in-memory cache (development)
set_llm_cache(InMemoryCache())

# Persistent SQLite cache (production)
set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))

# Custom semantic cache for similar queries
from langchain.cache import SemanticCache
from langchain.embeddings import OpenAIEmbeddings

set_llm_cache(SemanticCache(
    embedding=OpenAIEmbeddings(),
    score_threshold=0.95,  # High threshold for semantic similarity
    redis_url="redis://localhost:6379"
))
```

**Batch LLM calls when possible:**

```python
from langchain.llms import OpenAI

llm = OpenAI(batch_size=20)  # Process 20 prompts per API call

# Use generate() for batching
prompts = ["Summarize: " + doc for doc in documents]
results = llm.generate(prompts)
```

### 3. Memory Optimization

**Choose the right memory type for your use case:**

| Memory Type | Token Cost | Use Case | Max History |
|-------------|------------|----------|-------------|
| `ConversationBufferMemory` | High | Short chats (<10 turns) | All |
| `ConversationBufferWindowMemory` | Medium | Bounded context needs | Last k |
| `ConversationSummaryMemory` | Low | Long sessions | Compressed |
| `ConversationSummaryBufferMemory` | Medium | Hybrid approach | Recent + summary |
| `VectorStoreRetrieverMemory` | Low | Semantic relevance | Top k similar |

**Memory profiling:**

```python
from langchain.memory import ConversationBufferMemory
import tiktoken

def count_memory_tokens(memory: ConversationBufferMemory, model: str = "gpt-4") -> int:
    """Count tokens in memory to prevent context overflow."""
    encoding = tiktoken.encoding_for_model(model)
    history = memory.load_memory_variables({})
    history_str = str(history.get("history", ""))
    return len(encoding.encode(history_str))

# Automatic memory trimming
class TokenLimitedMemory(ConversationBufferMemory):
    max_tokens: int = 4000
    model: str = "gpt-4"

    def save_context(self, inputs, outputs):
        super().save_context(inputs, outputs)
        self._trim_if_needed()

    def _trim_if_needed(self):
        while count_memory_tokens(self, self.model) > self.max_tokens:
            # Remove oldest message pair
            if self.chat_memory.messages:
                self.chat_memory.messages.pop(0)
                if self.chat_memory.messages:
                    self.chat_memory.messages.pop(0)
```

### 4. Streaming for Perceived Performance

```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI

# Enable streaming for user-facing responses
llm = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# Custom streaming handler for web applications
class WebSocketStreamHandler(BaseCallbackHandler):
    def __init__(self, websocket):
        self.websocket = websocket

    async def on_llm_new_token(self, token: str, **kwargs):
        await self.websocket.send_json({"type": "token", "content": token})
```

---

## Cost Optimization Strategies

### 1. Token Usage Tracking

```python
from langchain.callbacks import get_openai_callback
from dataclasses import dataclass
from typing import Optional

@dataclass
class CostTracker:
    total_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_cost: float = 0.0

    def update(self, cb):
        self.total_tokens += cb.total_tokens
        self.prompt_tokens += cb.prompt_tokens
        self.completion_tokens += cb.completion_tokens
        self.total_cost += cb.total_cost

tracker = CostTracker()

with get_openai_callback() as cb:
    result = chain.invoke({"query": "test"})
    tracker.update(cb)

print(f"Cost: ${tracker.total_cost:.4f}")
print(f"Tokens: {tracker.total_tokens}")
```

### 2. Model Tiering

**Use cheaper models for simple tasks:**

```python
from langchain.chat_models import ChatOpenAI

# Routing based on task complexity
class TieredLLM:
    def __init__(self):
        self.cheap = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.expensive = ChatOpenAI(model="gpt-4", temperature=0)

    def route(self, task_type: str):
        expensive_tasks = ["reasoning", "analysis", "code_generation"]
        return self.expensive if task_type in expensive_tasks else self.cheap

# Automatic complexity detection
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

complexity_prompt = PromptTemplate(
    input_variables=["query"],
    template="Rate this query's complexity (simple/complex): {query}\nRating:"
)

def smart_route(query: str, tiered_llm: TieredLLM) -> ChatOpenAI:
    rating = tiered_llm.cheap.predict(complexity_prompt.format(query=query))
    return tiered_llm.expensive if "complex" in rating.lower() else tiered_llm.cheap
```

### 3. Prompt Compression

```python
from langchain.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever

# Compress retrieved documents before sending to LLM
compressor = LLMChainExtractor.from_llm(
    ChatOpenAI(model="gpt-3.5-turbo")  # Use cheap model for compression
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever(search_kwargs={"k": 10})
)

# Returns compressed, relevant portions only
docs = compression_retriever.get_relevant_documents("query")
```

---

## Debugging Techniques

### 1. Verbose Tracing

```python
import langchain
langchain.debug = True  # Enable detailed logging

# Or use LangSmith for production tracing
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"
```

### 2. Agent Debugging

```python
from langchain.agents import AgentExecutor

# Capture agent thought process
class AgentDebugger(BaseCallbackHandler):
    def __init__(self):
        self.steps = []

    def on_agent_action(self, action, **kwargs):
        self.steps.append({
            "type": "action",
            "tool": action.tool,
            "input": action.tool_input,
            "log": action.log
        })

    def on_agent_finish(self, finish, **kwargs):
        self.steps.append({
            "type": "finish",
            "output": finish.return_values,
            "log": finish.log
        })

    def on_tool_error(self, error, **kwargs):
        self.steps.append({
            "type": "error",
            "error": str(error)
        })

    def get_trace(self):
        return self.steps

debugger = AgentDebugger()
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    callbacks=[debugger],
    handle_parsing_errors=True,  # Don't crash on parse errors
    max_iterations=10,  # Prevent infinite loops
    early_stopping_method="generate"  # Try to generate output when stuck
)
```

### 3. Common Issues & Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Agent loops | Same action repeated | Add max_iterations, improve tool descriptions |
| Parsing errors | "Could not parse output" | Use handle_parsing_errors=True, simplify output format |
| Wrong tool selection | Agent picks wrong tool | Improve tool descriptions, add examples |
| Context overflow | Token limit exceeded | Use memory trimming, compress context |
| Slow responses | High latency | Enable streaming, add caching, batch calls |
| High costs | Unexpected bills | Add token tracking, use model tiering |

---

Error Recovery Patterns (RobustChain with tenacity retry + fallback chain) and Testing Patterns (Chain Testing + Agent Testing with pytest examples) are in the reference file.

See [references/error-recovery-and-testing.md](references/error-recovery-and-testing.md)

---

## Production Checklist

Before deploying LangChain applications:

- [ ] **Performance profiled** - Know where time is spent
- [ ] **Caching enabled** - LLM cache for repeated queries
- [ ] **Memory bounded** - Token limits on conversation history
- [ ] **Cost tracking** - Monitor token usage and costs
- [ ] **Error handling** - Graceful fallbacks for failures
- [ ] **Timeouts set** - Prevent hanging requests
- [ ] **Logging configured** - Tracing for debugging
- [ ] **Tests written** - Unit and integration tests
- [ ] **Rate limiting** - Protect against abuse
- [ ] **Input validation** - Sanitize user inputs

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/chain_analyzer.py` | Analyze chain execution performance |
| `scripts/memory_profiler.py` | Profile memory usage and token consumption |
| `references/chain_patterns.md` | Common chain composition patterns |
| `references/memory_strategies.md` | Memory type selection guide |
| `references/debugging_guide.md` | Troubleshooting common issues |
| `references/error-recovery-and-testing.md` | Error Recovery Patterns (RobustChain with retry/fallback), Chain Testing (output format, edge cases, token limits), Agent Testing (tool selection, iteration limits) |
| `assets/langchain_decision_tree.md` | When to use which LangChain component |

## Verification

To validate your LangChain optimization is effective:

1. **Latency**: p95 response time improved by >= 20% compared to baseline
2. **Cost**: Token cost per request reduced by >= 15% through caching/model tiering
3. **Reliability**: Chain success rate >= 95% on representative test queries
4. **Memory**: No token limit errors after 20+ conversation turns
5. **Regression**: All existing chain tests still pass after optimization changes
6. **Monitoring**: LangSmith or callback-based tracing configured for production

## Related Skills

- `langchain-architecture` - Foundational LangChain patterns (use first)
- `rag-architecture` - RAG pipeline design and optimization
- `vector-search-optimization` - Vector database and index tuning
- `prompt-engineering-patterns` - Prompt optimization techniques
- `llm-evaluation` - Evaluate chain quality
- `promptfoo-evaluation` - A/B testing for prompts
