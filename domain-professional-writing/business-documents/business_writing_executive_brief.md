# Executive Brief (Decision Memo)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Decision Making

## Prompt

```
You are writing an executive brief that gets a specific decision made.

CONTEXT:
Decision needed: [WHAT SPECIFIC DECISION ARE YOU REQUESTING]
Decision maker: [WHO WILL APPROVE THIS - name/role]
Decision deadline: [WHEN THIS DECISION NEEDS TO BE MADE]
Background: [WHY THIS DECISION IS NEEDED NOW]

INPUT PROVIDED:
[PASTE YOUR RESEARCH, DATA, ANALYSIS, OPTIONS HERE]

YOUR TASK:
Create a one-page executive brief that enables a fast, informed decision. This document will be read in [TIME FRAME - e.g. "5 minutes before the exec meeting"] and needs to make the decision path obvious.

REQUIRED STRUCTURE:
1. **Decision Request** (First paragraph: what you need decided, by when, why now)
2. **Recommendation** (Your recommended option with one-sentence rationale)
3. **Options Analysis** (3 options max: yours + 2 alternatives, with trade-offs for each)
4. **Key Data** (The 3-5 numbers that matter most for this decision)
5. **Risks** (Top 2 risks of your recommendation + mitigation)

CONSTRAINTS:
- Total length: 500 words maximum (one page)
- Decision request: Must appear in first paragraph, must be specific and binary ("Approve X" not "Consider Y")
- Recommendation: Must be stated before options analysis (don't bury it)
- Options: Exactly 3 options, each with 2-sentence trade-off (what you gain, what you give up)
- Key data: Must include source and date ("$2.4M ARR, Q3 2024 financials")
- Risks: Must be specific and include mitigation ("Risk: 3-week delay. Mitigation: Add contractor resource")
- DO NOT include: lengthy background, process description, multiple recommendations
- DO NOT hedge: Pick one recommendation. Don't say "we could consider" or "might explore"
- Use only data from input - do not estimate ROI or impact you don't have data for

TONE:
- Direct and recommendation-forward, not analysis-heavy
- Use active voice ("We should approve X" not "X could be approved")
- State trade-offs clearly, no optimistic framing
- No diplomatic hedging ("I recommend we approve" not "It might be worth considering")

QUALITY CHECKS - Before outputting, verify:
- [ ] Decision request is in first paragraph and is specific
- [ ] Recommendation is stated clearly before diving into options
- [ ] Exactly 3 options provided, each with clear trade-offs
- [ ] Every data point has source and date
- [ ] Both risks and mitigations are specific (not "may face challenges")
- [ ] No claims without supporting data from inputs
- [ ] If decision maker is risk-averse, I've front-loaded risks
- [ ] Total word count is under 500 words
- [ ] Reading this, someone can make the decision without asking follow-up questions

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Executive briefs exist to enable fast, informed decisions, not to inform. The structure forces decision request first, recommendation second, then supporting analysis.

**Customization Options:**
- Adjust for different decision-makers (risk-averse, data-driven, strategic, ops-focused)
- Modify for different decision types (investment, hiring, product, strategic, technical)
- Add sections for your approval process (discussion questions, sign-off owners)

**Common Pitfalls:**
- Analysis without ask (burying the decision request)
- No clear recommendation (making exec do the work)
- Vague options without clear trade-offs
- Unsourced claims and data
- No risk assessment
