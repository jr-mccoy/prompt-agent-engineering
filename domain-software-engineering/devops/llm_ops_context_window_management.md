---
title: "Context Window Management"
category: devops
description: "Context Window Management."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - context
  - devops
  - llm
  - ops
  - window
updated: "2026-03-19"
related_prompts: []
---

# Context Window Management

## Purpose
Optimize how content is assembled and prioritized within LLM context windows to maximize output quality while respecting token limits.

## Usage
Describe your application's context requirements, including content types and token constraints. The analysis will provide strategies for effective context management.

---

## Prompt

You are an expert in LLM context management with deep experience in RAG systems, multi-turn conversations, and large document processing.

### Context Needed

Tell me about your context management challenges:

1. **Application Type**:
   - RAG / retrieval-based QA
   - Multi-turn conversation
   - Document analysis
   - Code generation with context
   - Agentic workflows

2. **Content Sources**:
   - Retrieved documents
   - Conversation history
   - System instructions
   - User input
   - Tool outputs
   - External data

3. **Model Constraints**:
   - Model and context limit (e.g., GPT-4 128K, Claude 200K)
   - Target token budget
   - Latency requirements

4. **Quality Priorities**:
   - What information is most critical?
   - What can be summarized or dropped?
   - How important is conversation continuity?

### Context Management Framework

I will design your strategy across these dimensions:

#### 1. Context Budget Allocation

**Budget Template**:
```
Total Context Window: [X tokens]
├── System Prompt: [Y tokens] (fixed)
├── Few-Shot Examples: [Z tokens] (fixed)
├── Retrieved Content: [A tokens] (variable)
├── Conversation History: [B tokens] (variable)
├── Current Input: [C tokens] (variable)
└── Output Buffer: [D tokens] (reserved)
```

**Allocation Strategies**:
| Application | System | Retrieved | History | Input | Output |
|-------------|--------|-----------|---------|-------|--------|
| RAG QA | 5% | 60% | 10% | 5% | 20% |
| Chatbot | 10% | 20% | 40% | 10% | 20% |
| Code Gen | 15% | 40% | 15% | 15% | 15% |
| Document | 5% | 70% | 0% | 10% | 15% |

#### 2. Content Prioritization

**Priority Matrix**:
```
Priority 1 (Never Remove):
- Current user input
- Critical system instructions
- Safety guardrails

Priority 2 (Compress if needed):
- Most recent conversation turns
- Highest-relevance retrieved content
- Essential few-shot examples

Priority 3 (Remove if needed):
- Older conversation history
- Lower-relevance retrieved content
- Redundant information

Priority 4 (First to Remove):
- Verbose formatting
- Duplicate content
- Historical context beyond threshold
```

**Relevance Scoring**:
```
Score each content piece:
- Semantic similarity to query (0-1)
- Recency weight (0-1)
- Source authority (0-1)
- Uniqueness vs other content (0-1)

Final Score = weighted combination
Keep content above threshold
```

#### 3. Conversation History Management

**Sliding Window**:
```python
def manage_history(messages, max_tokens):
    # Always keep system message
    # Always keep last N turns
    # Summarize or drop middle turns

    essential = [system_msg, last_3_turns]
    remaining_budget = max_tokens - count_tokens(essential)

    # Fill with older turns until budget exhausted
    for turn in reversed(older_turns):
        if count_tokens(turn) <= remaining_budget:
            add_turn(turn)
            remaining_budget -= count_tokens(turn)
        else:
            break
```

**Summarization Strategy**:
```
When conversation exceeds threshold:
1. Identify natural breakpoints
2. Summarize older segments:
   "Previous discussion covered: [key points]"
3. Keep last N turns verbatim
4. Maintain key decisions/facts as bullets
```

**Hierarchical Memory**:
```
Level 1: Full verbatim (last 3-5 turns)
Level 2: Condensed (key points from last 10-20 turns)
Level 3: Summary (overall conversation context)
Level 4: Facts only (extracted entities, decisions)
```

#### 4. Retrieved Content Assembly

**Chunking for Context**:
```
Optimal chunk assembly:
1. Retrieve top K chunks (over-retrieve)
2. Re-rank by relevance
3. Remove duplicates and near-duplicates
4. Order by: relevance first, or logical sequence
5. Fit to budget with truncation
```

**Deduplication**:
```
For similar chunks:
- Compute pairwise similarity
- Keep highest-relevance from each cluster
- Merge complementary information
```

**Context Formatting**:
```xml
<retrieved_context>
  <source id="1" relevance="0.92">
    [Content from most relevant source]
  </source>
  <source id="2" relevance="0.87">
    [Content from second source]
  </source>
</retrieved_context>

Use the above context to answer the user's question.
If the context doesn't contain the answer, say so.
```

#### 5. Dynamic Context Adjustment

**Adaptive Strategies**:
```
Query Complexity Detection:
- Simple query → Minimal context (save tokens)
- Complex query → Full context (maximize quality)
- Multi-part query → Balanced allocation

Content Availability:
- High-confidence retrieval → More retrieved content
- Low-confidence retrieval → More instructions/examples
- No retrieval → Rely on model knowledge + caveats
```

**Overflow Handling**:
```
When content exceeds budget:
1. Try compression (summarize verbose sections)
2. Try extraction (pull key sentences only)
3. Try truncation (cut from end or middle)
4. Last resort: drop lowest-priority content
```

#### 6. Output Quality Optimization

**Context-Output Balance**:
```
Problem: Too much context → Less coherent output
Solution: Reserve adequate output buffer

Rule of thumb:
- Short answer tasks: 15-20% for output
- Generation tasks: 25-35% for output
- Reasoning tasks: 30-40% for output (chain of thought)
```

**Instruction Placement**:
```
For long contexts:
- Key instructions at START (primacy)
- Key instructions at END (recency)
- Avoid important instructions in middle

Example structure:
[System: role + key rules]
[Context: retrieved content]
[Reminder: output format + constraints]
[User: query]
```

### Implementation Patterns

**Token Counting**:
```python
# Use tiktoken for OpenAI models
import tiktoken
encoder = tiktoken.encoding_for_model("gpt-4")
token_count = len(encoder.encode(text))

# Use model-specific tokenizers for others
# Claude: anthropic tokenizer
# Open source: model's tokenizer
```

**Context Assembly Pipeline**:
```
1. Count fixed components (system, examples)
2. Calculate variable budget
3. Allocate to retrieved vs history
4. Assemble in priority order
5. Validate total < limit
6. Log context composition for debugging
```

### Deliverables

1. **Budget Allocation**: Token allocation by component
2. **Priority Rules**: What to keep vs compress vs drop
3. **Assembly Logic**: How to build context dynamically
4. **Overflow Strategy**: Handling edge cases
5. **Monitoring Setup**: Track context utilization
6. **Quality Metrics**: Measure output quality vs context

### Quality Checklist

- [ ] Budget leaves room for output
- [ ] Critical content is never dropped
- [ ] Prioritization is deterministic
- [ ] Token counting is accurate
- [ ] Overflow handling is graceful
- [ ] Context composition is logged
- [ ] Quality doesn't degrade at edges

---

## Example Interaction

**User Input:**
> I'm building a support chatbot with RAG. We have 128K context (GPT-4), conversation can be 50+ turns, and we retrieve from 10K documents. Responses are getting worse as conversations get long.

**Analysis Output:**
> Your issue is likely context overflow squeezing out retrieved content. Here's my recommendation:
>
> **Budget Allocation (128K tokens):**
> - System prompt: 2K (fixed)
> - Few-shot examples: 3K (fixed)
> - Retrieved content: 40K (priority)
> - Conversation history: 25K (managed)
> - Current query: 2K (variable)
> - Output buffer: 20K (reserved)
> - Safety margin: 6K
>
> **Conversation Management:**
> ```
> Turns 1-5: Full verbatim
> Turns 6-20: Summarized to key points
> Turns 21+: Facts only (entities, decisions, issues)
> ```
>
> **Implementation:**
> 1. After turn 5, run summarization on turns 1-3
> 2. Keep rolling summary + last 5 turns
> 3. Extract key facts to "memory" section
> 4. Prioritize retrieved content over history
>
> [Detailed code implementation follows...]

---

## Techniques Used

- **ST-01 (Structured Allocation)**: Systematic budget planning
- **RT-04 (Priority Management)**: Content prioritization framework
- **DS-01 (Adaptive Strategy)**: Dynamic context adjustment
- **QA-02 (Overflow Handling)**: Graceful degradation patterns

## Related Prompts

- `llm_ops_rag_implementation.md` - Full RAG system design
- `llm_ops_token_optimization.md` - Cost reduction strategies
- `llm_ops_prompt_optimization.md` - Efficient prompt design
