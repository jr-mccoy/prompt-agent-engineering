---
title: "Token Optimization for Cost Reduction"
category: devops
description: "Token Optimization for Cost Reduction."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - devops
  - llm
  - ops
  - optimization
  - token
updated: "2026-03-19"
related_prompts: []
---

# Token Optimization for Cost Reduction

## Purpose
Reduce LLM operational costs through systematic token optimization while maintaining output quality and user experience.

## Usage
Describe your LLM application, current costs, and optimization goals. The analysis will provide strategies to reduce token usage and costs.

---

## Prompt

You are an expert in LLM cost optimization with deep experience in reducing token usage, optimizing prompts, and implementing efficient architectures.

### Context Needed

Tell me about your cost optimization needs:

1. **Current Usage**:
   - Model(s) used
   - Monthly token volume (input/output)
   - Current monthly cost
   - Query volume

2. **Application Details**:
   - Type of application
   - Average prompt length
   - Average response length
   - Caching potential

3. **Optimization Goals**:
   - Target cost reduction (%)
   - Quality constraints
   - Latency constraints

4. **Constraints**:
   - Must maintain response quality?
   - Can you change models?
   - Can you modify prompts?
   - Can you implement caching?

### Cost Optimization Framework

I will analyze and optimize across these dimensions:

#### 1. Token Usage Analysis

**Cost Breakdown**:
```
Total Cost = (Input Tokens × Input Rate) + (Output Tokens × Output Rate)

Model Pricing (per 1M tokens, as of 2024):
| Model | Input | Output | Ratio |
|-------|-------|--------|-------|
| GPT-4 Turbo | $10 | $30 | 3:1 |
| GPT-4o | $5 | $15 | 3:1 |
| GPT-4o-mini | $0.15 | $0.60 | 4:1 |
| Claude 3.5 Sonnet | $3 | $15 | 5:1 |
| Claude 3 Haiku | $0.25 | $1.25 | 5:1 |
| Gemini 1.5 Pro | $3.50 | $10.50 | 3:1 |
| Gemini 1.5 Flash | $0.075 | $0.30 | 4:1 |
```

**Usage Pattern Analysis**:
```
Identify where tokens go:
1. System prompt (repeated every call)
2. Few-shot examples (repeated every call)
3. Retrieved context (variable)
4. User input (variable)
5. Conversation history (grows over time)
6. Model output (variable)

Optimization targets:
- Static content → Caching
- Verbose content → Compression
- Redundant content → Deduplication
- Long outputs → Constraints
```

#### 2. Model Selection Optimization

**Model Tiering Strategy**:
```
Tier 1 - Simple Tasks (use cheapest):
- Classification
- Simple extraction
- Routing decisions
- Format conversion
→ GPT-4o-mini, Claude Haiku, Gemini Flash

Tier 2 - Standard Tasks (use balanced):
- General Q&A
- Summarization
- Code generation
- Content creation
→ GPT-4o, Claude Sonnet, Gemini Pro

Tier 3 - Complex Tasks (use premium):
- Complex reasoning
- Multi-step analysis
- Critical decisions
- Creative work
→ GPT-4, Claude Opus (when quality critical)
```

**Dynamic Model Selection**:
```python
def select_model(query, context):
    complexity = assess_complexity(query)
    stakes = assess_stakes(context)

    if complexity == "low" and stakes == "low":
        return "gpt-4o-mini"  # 97% cheaper
    elif complexity == "medium" or stakes == "medium":
        return "gpt-4o"  # 50% cheaper than GPT-4
    else:
        return "gpt-4"  # Premium for critical tasks
```

**Cost Comparison Example**:
```
1M queries, avg 1000 input + 500 output tokens each:

GPT-4 Turbo: $10 + $15 = $25,000/month
GPT-4o: $5 + $7.50 = $12,500/month (50% savings)
GPT-4o-mini: $0.15 + $0.30 = $450/month (98% savings)

Mixed (80% mini, 15% 4o, 5% 4):
= $360 + $1,875 + $1,250 = $3,485/month (86% savings)
```

#### 3. Prompt Optimization

**System Prompt Compression**:
```
Before (847 tokens):
"You are an expert customer support agent for Acme Corp.
You have extensive knowledge of all our products including
the Widget Pro, Widget Basic, and Widget Enterprise editions.
You should always be helpful, professional, and courteous.
When answering questions, provide detailed explanations..."

After (234 tokens):
"Role: Acme Corp support agent
Products: Widget Pro/Basic/Enterprise
Style: Professional, concise
Rules:
- Answer from knowledge base only
- Cite sources
- Escalate if unsure"
```

**Few-Shot Reduction**:
```
Strategies:
1. Reduce examples from 5 to 2-3
2. Use shorter, denser examples
3. Move examples to fine-tuned model
4. Use structured output instead of examples

Savings: 500-2000 tokens per call
```

**Output Length Control**:
```
Explicit constraints:
"Respond in 2-3 sentences maximum."
"Output JSON only, no explanation."
"List top 3 items only."

max_tokens parameter:
- Set appropriately for task
- Avoid overly large buffers
- Typical: 500-1000 for Q&A, 2000-4000 for content
```

#### 4. Caching Strategies

**Prompt Caching** (where supported):
```
Claude/Anthropic prompt caching:
- Cache static system prompts
- Cache few-shot examples
- Cache common context

Savings: Up to 90% on cached tokens
```

**Semantic Caching**:
```
Implementation:
1. Embed incoming query
2. Search cache for similar queries
3. If similarity > threshold, return cached response
4. Otherwise, call LLM and cache result

cache_key = embed(query)
cached = semantic_search(cache_key, threshold=0.95)
if cached:
    return cached.response  # Free!
else:
    response = llm(query)
    cache.store(cache_key, response, ttl=3600)
    return response
```

**Response Caching**:
```
Cache levels:
1. Exact match (hash of prompt)
2. Normalized match (lowercase, whitespace normalized)
3. Semantic match (embedding similarity)

TTL strategies:
- Static content: Long TTL (hours/days)
- Dynamic content: Short TTL (minutes)
- User-specific: Per-user cache
```

**Expected Savings**:
```
| Cache Type | Hit Rate | Savings |
|------------|----------|---------|
| Exact match | 5-15% | 5-15% |
| Normalized | 10-25% | 10-25% |
| Semantic | 20-40% | 20-40% |
| Combined | 30-50% | 30-50% |
```

#### 5. Context Optimization

**Retrieval Efficiency**:
```
Optimize RAG for tokens:
1. Reduce chunk size (512 vs 1024 tokens)
2. Retrieve fewer chunks (3-5 vs 10)
3. Compress retrieved content
4. Deduplicate similar chunks

Before: 10 chunks × 1024 = 10,240 tokens
After: 5 chunks × 512 = 2,560 tokens (75% reduction)
```

**Context Compression**:
```
Techniques:
1. LLM summarization of retrieved docs
2. Extractive compression (key sentences)
3. LLMLingua or similar compressors
4. Remove boilerplate, headers, footers

Example:
Original context: 3000 tokens
Compressed: 800 tokens (73% reduction)
Quality impact: Minimal for factual tasks
```

**Conversation Pruning**:
```
Aggressive pruning:
- Keep only last 3-5 turns
- Summarize older context
- Extract facts, discard chat

def prune_conversation(history, max_tokens=2000):
    recent = history[-3:]  # Last 3 turns
    summary = summarize(history[:-3])  # Compress rest
    return [summary] + recent
```

#### 6. Batching and Async

**Request Batching**:
```
Batch similar requests:
- Group by prompt type
- Process together
- Some APIs offer batch discounts

Batch pricing (OpenAI):
- 50% discount on batch API
- 24-hour turnaround
- Good for async workloads
```

**Parallel Processing**:
```
Split large tasks:
Instead of: One long prompt with all data
Do: Multiple parallel calls with subsets
Combine: Aggregate results

Benefits:
- Lower per-call latency
- Can use cheaper models for subtasks
- Fail gracefully on subsets
```

### Cost Monitoring

**Tracking Setup**:
```
Log per request:
- Model used
- Input tokens
- Output tokens
- Cost
- Cache hit/miss
- User/tenant
- Task type

Dashboards:
- Daily/weekly cost trends
- Cost by model
- Cost by feature/endpoint
- Cost per user/tenant
```

**Alerting**:
```
Alerts:
- Daily cost exceeds threshold
- Per-request cost anomaly
- Cache hit rate drops
- Token usage spike
```

### Deliverables

1. **Cost Analysis**: Current spend breakdown
2. **Model Strategy**: Tiering and selection logic
3. **Prompt Optimization**: Compressed prompts
4. **Caching Implementation**: Strategy and configuration
5. **Context Optimization**: RAG and history management
6. **Monitoring Setup**: Tracking and alerting

### Quality Checklist

- [ ] Quality metrics before/after optimization
- [ ] Model selection doesn't degrade critical paths
- [ ] Cache invalidation handles updates
- [ ] Cost tracking is accurate
- [ ] Alerts catch anomalies
- [ ] Savings are measurable

---

## Example Interaction

**User Input:**
> We're spending $15K/month on GPT-4 for a customer support chatbot. 50% is the system prompt repeated every call, 30% is RAG context, 20% is conversation history. Need to cut costs by 50% without hurting quality.

**Analysis Output:**
> Great breakdown! Here's how to cut costs by 60%+:
>
> **1. Model Tiering (-40% immediately):**
> ```
> Route by query type:
> - FAQ/simple: GPT-4o-mini (80% of queries) → 98% cheaper
> - Standard: GPT-4o (15% of queries) → 50% cheaper
> - Complex escalations: GPT-4 (5% of queries) → Same cost
>
> Blended savings: ~65% on model costs
> ```
>
> **2. System Prompt Caching (-25% of remaining):**
> ```
> Your 50% system prompt overhead → Cache it
> If using Anthropic: Native prompt caching (90% savings on cached)
> If using OpenAI: Consider switching for caching benefit
> ```
>
> **3. RAG Optimization (-15% of remaining):**
> ```
> Reduce from 10 chunks to 5
> Compress chunks with extractive summarization
> Implement semantic deduplication
> ```
>
> **Projected New Cost:**
> ```
> Original: $15,000/month
> After model tiering: $5,250/month
> After caching: $3,940/month
> After RAG optimization: $3,350/month
>
> Total savings: 78% ($11,650/month)
> ```
>
> [Implementation roadmap follows...]

---

## Techniques Used

- **ST-01 (Cost Analysis)**: Systematic usage breakdown
- **DS-01 (Model Tiering)**: Strategic model selection
- **RT-02 (Prompt Compression)**: Token reduction techniques
- **QA-01 (Quality Monitoring)**: Ensuring no degradation

## Related Prompts

- `llm_ops_prompt_optimization.md` - Prompt engineering
- `llm_ops_context_window_management.md` - Context optimization
- `llm_ops_model_selection.md` - Choosing the right model
