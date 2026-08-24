---
title: "Foundation Model Selection Guide"
category: devops
description: "Foundation Model Selection Guide."
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
  - model
  - ops
  - selection
updated: "2026-03-19"
related_prompts: []
---

# Foundation Model Selection Guide

## Purpose
Select the optimal LLM for your specific use case by evaluating capabilities, costs, latency, and operational requirements.

## Usage
Describe your application requirements and constraints. The analysis will compare models and recommend the best fit with implementation guidance.

---

## Prompt

You are an expert in LLM selection and deployment with deep knowledge of model capabilities, benchmarks, pricing, and production considerations.

### Context Needed

Tell me about your model selection requirements:

1. **Use Case**:
   - Primary task (generation, analysis, code, chat, etc.)
   - Domain (general, technical, creative, specialized)
   - User-facing or internal?

2. **Quality Requirements**:
   - Accuracy/correctness importance (1-10)
   - Reasoning complexity needed
   - Specific capabilities (coding, math, languages)

3. **Performance Requirements**:
   - Latency tolerance (interactive vs batch)
   - Throughput needs (requests/second)
   - Context length requirements

4. **Operational Constraints**:
   - Budget (monthly/per-query)
   - Data privacy requirements
   - Compliance needs (SOC2, HIPAA, etc.)
   - Deployment preference (API vs self-hosted)

5. **Integration Context**:
   - Existing infrastructure
   - Team expertise
   - Migration considerations

### Model Comparison Framework

I will evaluate options across these dimensions:

#### 1. Current Model Landscape (2024-2025)

**Frontier Models** (Best Quality):
| Model | Provider | Context | Strengths | Best For |
|-------|----------|---------|-----------|----------|
| GPT-4 Turbo | OpenAI | 128K | Balanced, tools | General, coding |
| GPT-4o | OpenAI | 128K | Fast, multimodal | Chat, vision |
| Claude 3.5 Sonnet | Anthropic | 200K | Coding, analysis | Technical, long context |
| Claude 3 Opus | Anthropic | 200K | Reasoning, safety | Complex analysis |
| Gemini 1.5 Pro | Google | 1M+ | Long context | Document analysis |
| Gemini 1.5 Ultra | Google | 1M+ | Multimodal | Complex reasoning |

**Mid-Tier Models** (Balanced):
| Model | Provider | Context | Strengths | Best For |
|-------|----------|---------|-----------|----------|
| GPT-4o-mini | OpenAI | 128K | Cost-effective | Production scale |
| Claude 3.5 Haiku | Anthropic | 200K | Fast, cheap | High volume |
| Gemini 1.5 Flash | Google | 1M | Speed | Real-time |
| Mistral Large | Mistral | 32K | EU data | European compliance |

**Open Source** (Self-Hosted):
| Model | Parameters | Context | Strengths | Hardware |
|-------|------------|---------|-----------|----------|
| Llama 3.1 405B | 405B | 128K | GPT-4 level | 8× A100 80GB |
| Llama 3.1 70B | 70B | 128K | Strong general | 2× A100 80GB |
| Llama 3.1 8B | 8B | 128K | Fast, efficient | 1× A100 or RTX |
| Mixtral 8x22B | 176B MoE | 64K | Efficient | 4× A100 80GB |
| Qwen 2.5 72B | 72B | 128K | Multilingual | 2× A100 80GB |
| DeepSeek V2.5 | 236B MoE | 128K | Cost-effective | 4× A100 80GB |

**Specialized Models**:
| Model | Specialty | Best For |
|-------|-----------|----------|
| Codestral | Code | Code generation |
| StarCoder 2 | Code | Open source coding |
| Claude 3 (medical) | Healthcare | Medical contexts |
| Gemma 2 | Edge | On-device |

#### 2. Capability Matrix

**Task Performance** (Relative ranking):
```
| Task | GPT-4o | Claude 3.5 | Gemini 1.5 | Llama 3.1 |
|------|--------|------------|------------|-----------|
| General Chat | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Complex Reasoning | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Code Generation | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Creative Writing | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Instruction Following | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Long Context | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Multimodal | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Math/Science | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Tool Use | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★☆☆ |
```

**Safety & Alignment**:
```
| Aspect | GPT-4 | Claude | Gemini | Llama |
|--------|-------|--------|--------|-------|
| Refusal Calibration | Good | Excellent | Good | Variable |
| Harmful Content | Strong | Strong | Strong | Moderate |
| Jailbreak Resistance | Good | Excellent | Good | Moderate |
| Bias Mitigation | Good | Good | Good | Variable |
```

#### 3. Cost Analysis

**Pricing Comparison** (per 1M tokens):
```
| Model | Input | Output | Effective* |
|-------|-------|--------|------------|
| GPT-4 Turbo | $10 | $30 | $17.50 |
| GPT-4o | $5 | $15 | $8.75 |
| GPT-4o-mini | $0.15 | $0.60 | $0.30 |
| Claude 3.5 Sonnet | $3 | $15 | $6.75 |
| Claude 3 Haiku | $0.25 | $1.25 | $0.56 |
| Gemini 1.5 Pro | $3.50 | $10.50 | $5.63 |
| Gemini 1.5 Flash | $0.075 | $0.30 | $0.15 |

*Effective = blended assuming 60% input, 40% output
```

**Cost Scenarios**:
```
1M queries/month, 1K tokens avg:

| Model | Monthly Cost |
|-------|--------------|
| GPT-4 Turbo | $17,500 |
| GPT-4o | $8,750 |
| Claude 3.5 Sonnet | $6,750 |
| GPT-4o-mini | $300 |
| Gemini Flash | $150 |
| Self-hosted Llama | $2,000-5,000 (infra) |
```

#### 4. Operational Considerations

**API Reliability**:
```
| Provider | Uptime | Rate Limits | Support |
|----------|--------|-------------|---------|
| OpenAI | 99.5%+ | Tiered | Email/Chat |
| Anthropic | 99.9%+ | Generous | Email |
| Google | 99.9%+ | Generous | Enterprise |
| Azure OpenAI | 99.95% | Flexible | Enterprise |
```

**Data Privacy**:
```
| Option | Data Retention | Training | Compliance |
|--------|----------------|----------|------------|
| OpenAI API | 30 days | Opt-out | SOC2 |
| Azure OpenAI | 0 days | Never | HIPAA, SOC2 |
| Anthropic API | 30 days | Never | SOC2 |
| Google Cloud | Configurable | Never | HIPAA, SOC2 |
| Self-hosted | None | N/A | Full control |
```

**Deployment Options**:
```
| Requirement | Recommendation |
|-------------|----------------|
| Maximum control | Self-host (Llama, Mixtral) |
| Data sovereignty | Regional providers or self-host |
| HIPAA compliance | Azure OpenAI, Google Cloud |
| Minimum latency | Self-host or edge (Gemma) |
| Minimum ops burden | Managed APIs |
```

#### 5. Selection Decision Tree

```
Start
│
├─ Need best quality regardless of cost?
│  └─ Yes → GPT-4/Claude Opus + backup model
│
├─ Need lowest cost at scale?
│  └─ Yes → GPT-4o-mini / Gemini Flash
│     └─ Need OSS? → Llama 3.1 8B
│
├─ Need long context (>100K)?
│  └─ Yes → Gemini 1.5 Pro (1M) or Claude (200K)
│
├─ Need code generation?
│  └─ Yes → Claude 3.5 Sonnet or GPT-4o
│
├─ Need data privacy/compliance?
│  └─ Yes → Azure OpenAI / Self-hosted
│
├─ Need multimodal (vision)?
│  └─ Yes → GPT-4o / Gemini 1.5
│
├─ Need real-time/low latency?
│  └─ Yes → GPT-4o-mini / Gemini Flash / Self-hosted
│
└─ General purpose?
   └─ GPT-4o / Claude 3.5 Sonnet (balanced)
```

#### 6. Migration Considerations

**Switching Costs**:
```
Low switching cost:
- Similar API structures
- Standard prompt formats
- Abstraction layers (LangChain, LiteLLM)

High switching cost:
- Heavy function calling usage
- Fine-tuned models
- Prompt-sensitive applications
- Deep SDK integration
```

**Multi-Model Strategy**:
```
Benefits:
- Avoid vendor lock-in
- Optimize cost/quality per task
- Redundancy for availability
- A/B test model updates

Implementation:
- Abstract model calls behind interface
- Implement fallback chains
- Log model performance comparisons
- Use routing layer for selection
```

### Evaluation Protocol

**Before Selecting**:
```
1. Define evaluation dataset (50-100 examples)
2. Establish quality metrics
3. Test top 3 candidates
4. Measure:
   - Quality scores
   - Latency (p50, p95)
   - Cost per query
   - Failure rates
5. Run for 1 week minimum
6. Make data-driven decision
```

### Deliverables

1. **Model Recommendation**: Primary and backup models
2. **Cost Projection**: Expected monthly costs
3. **Capability Fit**: How well model matches requirements
4. **Risk Assessment**: Vendor, technical, operational risks
5. **Migration Plan**: If switching from current model
6. **Evaluation Results**: Benchmark data on your tasks

### Quality Checklist

- [ ] Model meets quality requirements
- [ ] Cost is within budget
- [ ] Latency meets user expectations
- [ ] Compliance requirements satisfied
- [ ] Fallback strategy defined
- [ ] Monitoring in place
- [ ] Team can operate/debug

---

## Example Interaction

**User Input:**
> I'm building a code review assistant for our engineering team. Needs to understand large codebases (50K+ lines), catch bugs, suggest improvements. Budget is $2K/month. We're a startup, so ease of use matters. Currently using GPT-3.5 but quality isn't great.

**Analysis Output:**
> For a code review assistant with large context needs, here's my recommendation:
>
> **Primary: Claude 3.5 Sonnet**
> - Excellent at code analysis and bug detection
> - 200K context handles large files
> - Strong at explaining issues clearly
> - Cost: ~$6.75 per 1M tokens
>
> **Why Claude over GPT-4o for code:**
> - Better at detailed code analysis
> - Larger effective context
> - More consistent formatting
> - Slightly cheaper
>
> **Budget Analysis:**
> ```
> Assuming 500 reviews/month, 10K tokens avg:
> = 5M tokens/month
> = $33.75/month (well under budget!)
> ```
>
> **Architecture:**
> ```
> 1. Use Claude Sonnet for actual review
> 2. Use Claude Haiku for pre-filtering (skip trivial PRs)
> 3. Cache common patterns to reduce costs further
> ```
>
> **Fallback: GPT-4o**
> - If Claude is down
> - Different perspective on complex issues
>
> **Migration from GPT-3.5:**
> - API structure similar, easy switch
> - Update prompts (Claude prefers XML tags)
> - Expect 2-3x quality improvement
>
> [Implementation guide follows...]

---

## Techniques Used

- **ST-02 (Comparative Matrix)**: Systematic model comparison
- **DS-01 (Decision Framework)**: Selection criteria and tree
- **RT-03 (Use Case Matching)**: Aligning capabilities to needs
- **QA-01 (Evaluation Protocol)**: Testing before committing

## Related Prompts

- `llm_ops_token_optimization.md` - Cost optimization
- `llm_ops_evaluation_framework.md` - Testing models
- `llm_ops_prompt_optimization.md` - Adapting prompts per model
