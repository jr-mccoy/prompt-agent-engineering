# LangChain Component Decision Tree

Quick reference for selecting the right LangChain components.

---

## Chain Type Selection

```
What are you building?
│
├─→ Simple prompt → response?
│   └─→ LLMChain
│       - Single prompt template
│       - Direct LLM call
│
├─→ Multiple sequential steps?
│   ├─→ Steps share variables?
│   │   └─→ SequentialChain
│   │       - Pass outputs between chains
│   │       - Named input/output variables
│   │
│   └─→ Steps are independent?
│       └─→ SimpleSequentialChain
│           - Just chain outputs → inputs
│
├─→ Need to route to different chains?
│   ├─→ Based on classification?
│   │   └─→ RouterChain + MultiPromptChain
│   │
│   └─→ Based on embeddings?
│       └─→ EmbeddingRouterChain
│
├─→ Document Q&A?
│   ├─→ Few documents?
│   │   └─→ RetrievalQA (chain_type="stuff")
│   │
│   ├─→ Many documents?
│   │   ├─→ Need parallel processing?
│   │   │   └─→ RetrievalQA (chain_type="map_reduce")
│   │   │
│   │   └─→ Need incremental refinement?
│   │       └─→ RetrievalQA (chain_type="refine")
│   │
│   └─→ Very large documents?
│       └─→ RetrievalQA (chain_type="map_rerank")
│
├─→ Autonomous task completion?
│   └─→ AgentExecutor
│       - Tools for external actions
│       - Self-directed reasoning
│
└─→ Chat with memory?
    └─→ ConversationChain
        - Built-in memory management
        - Chat-optimized prompts
```

---

## Memory Type Selection

```
How long are your conversations?
│
├─→ Short (<10 messages)
│   └─→ ConversationBufferMemory
│       ✓ Simple
│       ✓ Complete history
│       ✗ Grows unbounded
│
├─→ Medium (10-50 messages)
│   ├─→ Need complete recent history?
│   │   └─→ ConversationBufferWindowMemory (k=10-15)
│   │       ✓ Bounded token usage
│   │       ✓ Recent context preserved
│   │       ✗ Loses old context
│   │
│   └─→ Need summary of old context?
│       └─→ ConversationSummaryBufferMemory
│           ✓ Recent + summarized old
│           ✓ Good balance
│           ✗ Extra LLM calls for summary
│
├─→ Long (50+ messages)
│   ├─→ Sequential history matters?
│   │   └─→ ConversationSummaryMemory
│   │       ✓ Handles infinite conversations
│   │       ✗ Lossy compression
│   │       ✗ Extra LLM calls
│   │
│   └─→ Semantic relevance matters?
│       └─→ VectorStoreRetrieverMemory
│           ✓ Retrieves relevant past
│           ✓ Scales indefinitely
│           ✗ May miss chronological context
│
└─→ Tracking specific entities?
    └─→ ConversationEntityMemory
        ✓ Structured entity tracking
        ✓ Good for CRM-style context
        ✗ Complex setup
```

---

## Agent Type Selection

```
What does your agent need to do?
│
├─→ Use tools based on descriptions?
│   ├─→ Simple tool selection?
│   │   └─→ ZERO_SHOT_REACT_DESCRIPTION
│   │       - Most common
│   │       - Tool descriptions guide selection
│   │
│   └─→ Need conversation history?
│       └─→ CONVERSATIONAL_REACT_DESCRIPTION
│           - Maintains chat context
│           - Better for multi-turn
│
├─→ Use OpenAI function calling?
│   ├─→ Single function output?
│   │   └─→ OPENAI_FUNCTIONS
│   │       - Structured outputs
│   │       - Reliable parsing
│   │
│   └─→ Multiple function outputs?
│       └─→ OPENAI_MULTI_FUNCTIONS
│
├─→ Complex reasoning required?
│   ├─→ Break down into sub-questions?
│   │   └─→ SELF_ASK_WITH_SEARCH
│   │       - Decomposition
│   │       - Sequential reasoning
│   │
│   └─→ Plan then execute?
│       └─→ Plan-and-Execute Agent
│           - Creates plan first
│           - Executes steps
│
└─→ Structured/typed inputs?
    └─→ STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
        - Multi-input tools
        - Pydantic validation
```

---

## Retriever Selection

```
What's your retrieval need?
│
├─→ Basic semantic search?
│   └─→ vectorstore.as_retriever()
│       - search_type="similarity" (default)
│       - Simple and fast
│
├─→ Need diversity in results?
│   └─→ search_type="mmr"
│       - Maximal Marginal Relevance
│       - Balances relevance + diversity
│
├─→ Have rich metadata?
│   └─→ SelfQueryRetriever
│       - Auto-generates filters
│       - "Find 2024 engineering docs"
│
├─→ Keywords matter for matching?
│   └─→ EnsembleRetriever (BM25 + dense)
│       - Hybrid search
│       - Best of both worlds
│
├─→ Query might be vague?
│   └─→ MultiQueryRetriever
│       - Generates query variations
│       - Higher recall
│
├─→ Need precise match + full context?
│   └─→ ParentDocumentRetriever
│       - Small chunks for matching
│       - Returns large parent chunks
│
└─→ Documents are very long?
    └─→ ContextualCompressionRetriever
        - Extracts relevant portions
        - Reduces token usage
```

---

## Caching Strategy

```
What's your caching need?
│
├─→ Development/testing?
│   └─→ InMemoryCache
│       - Fast
│       - Resets on restart
│
├─→ Production, single server?
│   └─→ SQLiteCache
│       - Persistent
│       - Simple setup
│
├─→ Production, multiple servers?
│   └─→ RedisCache
│       - Distributed
│       - Shared across instances
│
└─→ Semantic similarity matching?
    └─→ SemanticCache
        - Cache similar queries
        - Requires embeddings
```

---

## Quick Reference Table

| Use Case | Primary Component | Supporting Components |
|----------|-------------------|----------------------|
| Chatbot | ConversationChain | Memory, (Retriever) |
| Doc Q&A | RetrievalQA | VectorStore, Embeddings |
| Task Agent | AgentExecutor | Tools, Memory |
| Summarization | MapReduceChain | TextSplitter |
| Classification | LLMChain | PromptTemplate |
| Multi-step | SequentialChain | Multiple LLMChains |

---

## Common Combinations

### Customer Support Bot
```python
memory = ConversationSummaryBufferMemory(max_token_limit=2000)
retriever = EnsembleRetriever(bm25, dense)
chain = ConversationalRetrievalChain(retriever, memory)
```

### Code Assistant
```python
memory = ConversationBufferWindowMemory(k=10)
tools = [search_code, run_tests, write_file]
agent = AgentExecutor(agent, tools, memory)
```

### Research Assistant
```python
retriever = MultiQueryRetriever(base_retriever, llm)
compression = ContextualCompressionRetriever(compressor, retriever)
chain = RetrievalQA(llm, retriever=compression)
```

---

## Anti-Pattern Warnings

| Don't Do | Why | Do Instead |
|----------|-----|------------|
| Buffer memory for long chats | Token overflow | Use Summary or Window |
| Agent for simple Q&A | Unnecessary complexity | Use LLMChain |
| MapReduce for few docs | Wasted LLM calls | Use "stuff" chain |
| Dense-only for technical docs | Miss exact matches | Use hybrid search |
| No caching in production | Wasted API calls | Add SQLite/Redis cache |

---

**Last Updated:** 2026-01-29
