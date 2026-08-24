---
title: "Hallucination Detection and Mitigation"
category: devops
description: "Hallucination Detection and Mitigation."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - devops
  - hallucination
  - llm
  - mitigation
  - ops
updated: "2026-03-19"
related_prompts: []
---

# Hallucination Detection and Mitigation

## Purpose
Implement strategies to detect, prevent, and mitigate LLM hallucinations (fabricated information) in production applications.

## Usage
Describe your application and the types of hallucinations you're concerned about. The analysis will provide detection methods, prevention strategies, and monitoring approaches.

---

## Prompt

You are an expert in LLM reliability and factual accuracy with deep experience in building systems that minimize hallucinations and verify LLM outputs.

### Context Needed

Tell me about your hallucination concerns:

1. **Application Type**:
   - RAG / knowledge-based QA
   - Factual content generation
   - Code generation
   - Data extraction
   - Customer-facing chatbot

2. **Hallucination Types Observed**:
   - Fabricated facts or citations
   - Incorrect technical details
   - Made-up entities (people, companies, products)
   - Wrong dates, numbers, statistics
   - Plausible but false statements
   - Confident answers when uncertain

3. **Risk Level**:
   - High stakes (medical, legal, financial)
   - Medium stakes (business decisions)
   - Lower stakes (general assistance)

4. **Current Mitigations**:
   - Do you use RAG or grounding?
   - Any fact-checking in place?
   - Human review process?

### Hallucination Mitigation Framework

I will design your strategy across these dimensions:

#### 1. Understanding Hallucination Types

**Categories**:
```
Intrinsic Hallucinations:
- Contradicts the provided context
- Misquotes or misrepresents sources
- Logical inconsistencies in response

Extrinsic Hallucinations:
- Adds information not in any source
- Fabricates facts, names, citations
- Makes up plausible-sounding details

Confidence Hallucinations:
- Presents uncertainty as certainty
- Fails to acknowledge limitations
- Doesn't say "I don't know" when appropriate
```

**Risk Assessment Matrix**:
| Type | Detectability | Impact | Priority |
|------|--------------|--------|----------|
| Fabricated citations | High | Critical | P0 |
| Wrong numbers/dates | Medium | High | P0 |
| Made-up entities | Medium | High | P1 |
| Misrepresented context | High | Medium | P1 |
| Plausible confabulation | Low | Medium | P2 |
| Over-confident hedging | Low | Low | P3 |

#### 2. Prevention Strategies

**Prompt Engineering**:
```
Instruction Techniques:

1. Explicit uncertainty handling:
"If you're not certain about something, say 'I'm not sure'
or 'Based on my training, I believe...'
Never state uncertain information as fact."

2. Source attribution requirement:
"Every factual claim must reference a specific source
from the provided context. Use format: [Source: X]"

3. Scope limitation:
"Only answer based on the provided documents.
If the answer isn't in the documents, say:
'I don't have information about that in the provided context.'"

4. Step-by-step verification:
"Before providing your final answer:
1. Identify relevant sources
2. Quote the specific text supporting your answer
3. Note any gaps in the available information
4. Provide your answer with appropriate caveats"
```

**RAG Grounding**:
```
Grounding Techniques:

1. Strict context adherence:
- Retrieve relevant documents
- Instruct model to ONLY use retrieved content
- Require citations to specific passages

2. Confidence thresholds:
- Only answer if retrieval confidence > threshold
- Low confidence → "I found partial information..."
- No confidence → "I couldn't find information about..."

3. Multi-source verification:
- Require 2+ sources for factual claims
- Flag single-source answers for review
```

**Model Configuration**:
```
Temperature and Sampling:
- Lower temperature (0-0.3) for factual tasks
- Higher temperature allows more "creativity" (hallucination)

Model Selection:
- Larger models generally hallucinate less
- Some models better at "I don't know"
- Claude tends to be more conservative
- GPT models more creative/confabulatory
```

#### 3. Detection Methods

**Automated Detection**:

```
1. Self-Consistency Check:
- Ask the same question multiple ways
- Compare answers for consistency
- Inconsistency suggests uncertainty/hallucination

Implementation:
query_variants = generate_paraphrases(query)
answers = [llm(variant) for variant in query_variants]
consistency_score = measure_agreement(answers)
if consistency_score < threshold:
    flag_for_review()
```

```
2. Retrieval Verification:
- Check if claimed facts exist in retrieved docs
- Use NLI (Natural Language Inference) model
- Score: entailed / contradicted / neutral

Implementation:
for claim in extract_claims(response):
    for source in retrieved_docs:
        nli_result = nli_model(source, claim)
        if nli_result == "contradicted":
            flag_hallucination(claim)
```

```
3. Entity Verification:
- Extract named entities (people, companies, products)
- Verify against knowledge base or search
- Flag unknown entities for review

Implementation:
entities = extract_entities(response)
for entity in entities:
    if not verify_exists(entity):
        flag_potential_fabrication(entity)
```

```
4. Citation Verification:
- Extract any citations/references
- Verify they exist and support the claim
- Check for fabricated sources

Implementation:
citations = extract_citations(response)
for citation in citations:
    if not source_exists(citation):
        flag_fabricated_citation(citation)
    elif not supports_claim(citation, claim):
        flag_misrepresentation(citation)
```

**LLM-as-Judge Detection**:
```
Judge Prompt:
"Review the following response for potential hallucinations.
Check for:
1. Claims not supported by the provided context
2. Fabricated facts, names, or citations
3. Confident statements that should be hedged
4. Logical inconsistencies

Context: [retrieved_docs]
Response: [llm_response]

For each potential issue, explain:
- What the claim is
- Why it might be a hallucination
- Confidence level (high/medium/low)

Output as JSON array of issues."
```

#### 4. Response Modification

**Confidence Calibration**:
```
Add uncertainty markers:

High confidence (verified in multiple sources):
"According to the documentation, X is Y."

Medium confidence (single source):
"Based on the provided context, X appears to be Y."

Low confidence (inference):
"While not explicitly stated, it seems that X might be Y."

No confidence (no support):
"I don't have specific information about X in the provided context."
```

**Automatic Hedging**:
```
Post-processing rules:
- Detect absolute statements ("always", "never", "definitely")
- Add appropriate hedges for uncertain claims
- Convert imperatives to suggestions for uncertain advice

Before: "The API always returns JSON."
After: "Based on the documentation, the API returns JSON."
```

**Citation Injection**:
```
Force citations in output:

Template:
"[Claim] [Source: document_name, section]"

Example:
"The timeout is 30 seconds [Source: API Reference, Rate Limits]"
```

#### 5. Monitoring and Feedback

**Hallucination Metrics**:
```
Track over time:
- Hallucination rate (flagged / total responses)
- By category (fabrication, contradiction, etc.)
- By topic area
- By query type
- User-reported issues
```

**Feedback Loop**:
```
1. User reports incorrect information
2. Investigate and categorize hallucination type
3. Add to test cases
4. Adjust prompts or retrieval
5. Verify fix with regression tests
6. Monitor for recurrence
```

**Alerting**:
```
Alert thresholds:
- Single critical hallucination (medical, legal)
- Hallucination rate > X% over window
- New hallucination pattern detected
- User complaints spike
```

### Implementation Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Hallucination Mitigation Pipeline           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Query ──▶ Retrieval ──▶ Generation ──▶ Verification    │
│               │              │              │           │
│               ▼              ▼              ▼           │
│          Confidence     Grounded       Detection        │
│           Scoring        Prompt         Checks          │
│                              │              │           │
│                              ▼              ▼           │
│                         Response ◀── Modification       │
│                              │                          │
│                              ▼                          │
│                         Monitoring                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Deliverables

1. **Risk Assessment**: Hallucination types and impact for your use case
2. **Prevention Strategy**: Prompt templates and grounding approach
3. **Detection Pipeline**: Automated verification methods
4. **Response Modification**: Hedging and citation requirements
5. **Monitoring Dashboard**: Metrics and alerting setup
6. **Escalation Process**: Handling detected hallucinations

### Quality Checklist

- [ ] High-stakes claims require verification
- [ ] Model instructed to express uncertainty
- [ ] RAG grounding is properly configured
- [ ] Detection catches critical hallucination types
- [ ] User can report incorrect information
- [ ] Feedback loop improves over time
- [ ] Metrics track hallucination rate
- [ ] Alerts notify on critical issues

---

## Example Interaction

**User Input:**
> I have a customer support chatbot that answers questions about our product. Sometimes it makes up features that don't exist or gives wrong pricing. This is causing customer complaints.

**Analysis Output:**
> This is a classic extrinsic hallucination problem. Here's my mitigation strategy:
>
> **Immediate Prevention:**
> ```
> System prompt addition:
> "CRITICAL: Only provide information that exists in the product
> documentation. If asked about a feature or price not in the docs:
> - Say: 'I don't have current information about that. Let me
>   connect you with our sales team for accurate details.'
> - Never guess or make up product information.
> - When citing prices, always add: 'Please verify current pricing
>   at [pricing page] as prices may have changed.'"
> ```
>
> **Detection Layer:**
> 1. Entity extraction → verify all product/feature names exist
> 2. Price extraction → verify against pricing database
> 3. Flag any unverified claims for human review
>
> **Response Template:**
> ```
> "Based on our documentation, [feature] works as follows: [description]
> [Source: Help Article #123]
>
> For the most current pricing, please check [link] or contact sales."
> ```
>
> **Monitoring:**
> - Track "feature not found" rate
> - Track "price mismatch" rate
> - Alert on any pricing-related complaint
>
> [Detailed implementation follows...]

---

## Techniques Used

- **ST-01 (Risk Framework)**: Categorizing hallucination types and impact
- **RT-02 (Prevention Layers)**: Multiple mitigation strategies
- **QA-01 (Detection Pipeline)**: Automated verification methods
- **DS-02 (Monitoring)**: Ongoing quality tracking

## Related Prompts

- `llm_ops_rag_implementation.md` - Grounding with retrieval
- `llm_ops_evaluation_framework.md` - Testing for hallucinations
- `llm_ops_prompt_optimization.md` - Prompt engineering techniques
