# LangChain Memory Strategies Reference

Comprehensive guide to selecting and optimizing memory types for LangChain applications.

---

## Memory Type Comparison

| Memory Type | Token Growth | Best For | Trade-offs |
|-------------|--------------|----------|------------|
| ConversationBufferMemory | Linear (unbounded) | Short chats (<10 turns) | Simple but grows indefinitely |
| ConversationBufferWindowMemory | Bounded | Medium chats | Loses old context |
| ConversationSummaryMemory | Logarithmic | Long sessions | Adds LLM calls for summarization |
| ConversationSummaryBufferMemory | Hybrid | Mixed needs | Balance of both |
| ConversationEntityMemory | Variable | Entity tracking | Complex setup |
| VectorStoreRetrieverMemory | Bounded | Semantic relevance | Requires vector store |
| ConversationTokenBufferMemory | Bounded | Token-aware apps | Precise control |

---

## Memory Type Details

### 1. ConversationBufferMemory

**Description:** Stores all messages in full.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    return_messages=True,  # Return as message objects
    memory_key="history"   # Key in chain input
)
```

**Pros:**
- Simple and complete
- No information loss
- No additional LLM calls

**Cons:**
- Unbounded growth
- Will hit context limits
- Higher costs over time

**When to Use:**
- Short conversations (<10 turns)
- Debugging and development
- When complete history is required

---

### 2. ConversationBufferWindowMemory

**Description:** Keeps only the last k conversation turns.

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    k=10,  # Keep last 10 exchanges
    return_messages=True
)
```

**Pros:**
- Predictable token usage
- Simple implementation
- No extra LLM calls

**Cons:**
- Loses older context
- May miss important early information

**When to Use:**
- Medium-length conversations
- When recent context is most relevant
- Bounded latency requirements

**Tuning k:**
| Conversation Type | Suggested k | Reasoning |
|-------------------|-------------|-----------|
| Customer support | 5-10 | Focus on immediate issue |
| Code assistance | 10-15 | Need recent code context |
| General chat | 5-8 | Keep costs reasonable |
| Deep discussion | 15-20 | Maintain thread coherence |

---

### 3. ConversationSummaryMemory

**Description:** Summarizes older messages progressively.

```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(
    llm=llm,  # LLM for summarization
    return_messages=True
)
```

**Pros:**
- Handles very long conversations
- Preserves key information
- Logarithmic token growth

**Cons:**
- Adds LLM calls (cost + latency)
- May lose nuance in summaries
- More complex

**When to Use:**
- Long-running sessions
- When gist matters more than verbatim
- High-value conversations worth extra cost

**Optimization:**
```python
# Use cheaper model for summarization
summary_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
memory = ConversationSummaryMemory(llm=summary_llm)
```

---

### 4. ConversationSummaryBufferMemory

**Description:** Hybrid - keeps recent messages verbatim, summarizes older ones.

```python
from langchain.memory import ConversationSummaryBufferMemory

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=2000,  # Summarize when exceeds
    return_messages=True
)
```

**Pros:**
- Best of both worlds
- Recent context preserved exactly
- Old context compressed

**Cons:**
- Most complex
- Still adds LLM calls

**When to Use:**
- Production applications
- When both recent and historical context matter
- Medium to long conversations

---

### 5. ConversationEntityMemory

**Description:** Tracks information about specific entities mentioned.

```python
from langchain.memory import ConversationEntityMemory

memory = ConversationEntityMemory(
    llm=llm,
    return_messages=True
)

# Tracks: {"John": "CEO of Acme Corp, likes golf", ...}
```

**Pros:**
- Structured knowledge tracking
- Efficient for entity-centric conversations
- Enables entity-specific reasoning

**Cons:**
- Additional LLM calls for extraction
- May miss non-entity information
- Complex to tune

**When to Use:**
- Customer relationship context
- Character tracking in stories
- When entities are the focus

---

### 6. VectorStoreRetrieverMemory

**Description:** Retrieves semantically relevant past interactions.

```python
from langchain.memory import VectorStoreRetrieverMemory

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
memory = VectorStoreRetrieverMemory(retriever=retriever)
```

**Pros:**
- Bounded token usage (only top-k relevant)
- Scales to very long histories
- Semantic relevance over recency

**Cons:**
- Requires vector store setup
- May miss chronologically important context
- Embedding costs

**When to Use:**
- Very long conversation histories
- When semantic relevance > recency
- Knowledge-base style memory

---

### 7. ConversationTokenBufferMemory

**Description:** Keeps messages within a strict token limit.

```python
from langchain.memory import ConversationTokenBufferMemory

memory = ConversationTokenBufferMemory(
    llm=llm,  # For token counting
    max_token_limit=2000
)
```

**Pros:**
- Precise token control
- Prevents context overflow
- Predictable costs

**Cons:**
- Requires token counting
- Loses oldest messages

**When to Use:**
- Strict token budgets
- When preventing overflow is critical
- Cost-sensitive applications

---

## Memory Selection Decision Tree

```
What's your conversation length?
│
├─→ Short (<10 turns)
│   └─→ ConversationBufferMemory
│
├─→ Medium (10-50 turns)
│   ├─→ Need recent context only? → ConversationBufferWindowMemory (k=10-15)
│   └─→ Need historical context? → ConversationSummaryBufferMemory
│
├─→ Long (50+ turns)
│   ├─→ Sequential history matters? → ConversationSummaryMemory
│   └─→ Semantic relevance matters? → VectorStoreRetrieverMemory
│
└─→ Entity-centric conversation?
    └─→ ConversationEntityMemory
```

---

## Token Budget Management

### Estimating Memory Tokens

```python
import tiktoken

def count_memory_tokens(memory, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    history = memory.load_memory_variables({})
    return len(encoding.encode(str(history)))
```

### Token Budget Allocation

| Component | Recommended % | Example (8K context) |
|-----------|---------------|----------------------|
| System Prompt | 10-15% | 800-1200 tokens |
| Memory/History | 40-50% | 3200-4000 tokens |
| Current Input | 10-20% | 800-1600 tokens |
| Response Buffer | 25-30% | 2000-2400 tokens |

### Automatic Trimming

```python
class TokenLimitedMemory(ConversationBufferMemory):
    max_tokens: int = 3000

    def save_context(self, inputs, outputs):
        super().save_context(inputs, outputs)
        while count_memory_tokens(self) > self.max_tokens:
            self.chat_memory.messages.pop(0)
            if self.chat_memory.messages:
                self.chat_memory.messages.pop(0)
```

---

## Common Issues and Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Context overflow | "Token limit exceeded" | Use bounded memory or trimming |
| Lost context | "I don't remember that" | Increase k or use summary memory |
| High latency | Slow responses | Reduce memory size, use caching |
| High costs | Large token bills | Use windowed or summary memory |
| Irrelevant history | Off-topic responses | Use VectorStoreRetrieverMemory |

---

## Best Practices

1. **Start simple:** Begin with ConversationBufferWindowMemory
2. **Monitor token usage:** Track memory growth over time
3. **Set hard limits:** Always have max token enforcement
4. **Use cheaper models for summarization:** GPT-3.5-turbo works well
5. **Test memory behavior:** Verify context is preserved as expected
6. **Consider hybrid approaches:** Combine memory types for complex needs

---

**Related:** See `scripts/memory_profiler.py` for memory analysis tools.
