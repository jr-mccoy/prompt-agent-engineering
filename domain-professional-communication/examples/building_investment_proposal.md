# Worked Example: Building an Investment Proposal

> This example demonstrates the complete process of creating an executive proposal for a technology investment.

---

## The Request

**User says:** "I need to convince my leadership to invest in a new customer analytics platform. We need about $150K and it could reduce churn significantly."

---

## Step 1: Classification

**Task Type:** COMMUNICATE
- This is a persuasion task - convincing stakeholders to approve an investment
- Requires structured argumentation with evidence

**Domain:** Professional Communication
- Business proposal for leadership
- Requires executive-appropriate format
- Must address ROI, risks, and alternatives

**Specific Type:** Executive Proposal / Budget Request

---

## Step 2: Context Analysis

### What We Know (From Request)
- Investment amount: ~$150K
- Benefit: Churn reduction (unquantified)
- Audience: "Leadership" (level unspecified)

### What We Need to Determine

**Critical for Strong Proposal:**

| Information Needed | Why It Matters | If Unknown |
|-------------------|----------------|------------|
| Current churn rate | Quantifies the problem | Must research/estimate |
| Current ARR | Calculates churn cost | Must research/estimate |
| Expected improvement | Quantifies benefit | Use industry benchmarks |
| Decision makers | Shapes framing | Ask user |
| Competing priorities | Anticipates objections | Ask user |
| Previous attempts | Avoids landmines | Ask user |

**Reasonable Assumptions for Example:**
- Churn: 12% annually (typical B2B SaaS)
- ARR: $16.7M (150 customers × $111K ACV)
- Target improvement: 1-2% points (8-15% reduction)
- Decision makers: VP Operations, CFO

---

## Step 3: Quantify the Business Case

### The Math

**Current State:**
- ARR: $16.7M
- Churn rate: 12%
- Annual revenue lost to churn: $2.0M

**Proposed Improvement:**
- Target churn: 11% (conservative 1-point improvement)
- Annual revenue retained: $167K additional

**Wait—that seems low for $150K investment!**

Let's recalculate with more aggressive but supported targets:

**Industry Benchmarks (Customer Health Platforms):**
- Typical churn reduction: 20-30% relative
- 12% churn × 25% reduction = 3% point improvement
- New churn: 9%
- Revenue retained: $500K annually

**Conservative Estimate (for proposal):**
- Assume 20% relative improvement
- 12% → 9.6% = 2.4 point improvement
- Revenue retained: ~$400K annually

**ROI Calculation:**
- Investment: $150K
- Annual return: $400K
- Payback: 4.5 months
- 3-year ROI: 700%

---

## Step 4: Anticipate Objections

**Likely Concerns from Leadership:**

| Objection | Why They'd Raise It | How to Address |
|-----------|---------------------|----------------|
| "We tried analytics before" | Past failures create skepticism | Research what went wrong, explain why this is different |
| "Budget is tight" | Competing priorities | Show fast payback, opportunity cost of delay |
| "IT can't support another tool" | Resource constraints | Vendor-managed, minimal IT involvement |
| "Projections seem optimistic" | Healthy skepticism | Show conservative case, vendor case studies |
| "Why this vendor?" | Due diligence | Include selection criteria |

---

## Step 5: Structure the Proposal

### Using BLUF Format

**First Paragraph Must Contain:**
1. The specific ask ($150K)
2. What it's for (customer analytics platform)
3. Why now (churn costs $2M annually)
4. Expected outcome ($400K annual savings)

### Document Structure

```
1. BLUF (30 seconds to read)
2. Executive Summary (2 minutes to read)
3. Supporting Analysis (for those who dig deeper)
4. Alternatives Considered
5. Risks and Mitigation
6. Next Steps
7. Appendix
```

---

## Step 6: The Complete Prompt

```markdown
# Create Executive Proposal: Customer Analytics Investment

**Objective:** Create a persuasive investment proposal for leadership approval

## Context

**Request:** Approval for ~$150K investment in customer analytics platform

**Business Problem:**
- Current annual churn rate: 12%
- Estimated ARR: $16.7M
- Annual revenue lost to churn: ~$2M
- Customer success team operates reactively (no predictive signals)

**Proposed Solution:**
- Customer health scoring platform
- Aggregates usage, support, and engagement data
- Generates predictive churn risk scores
- Enables proactive intervention

**Expected Outcome:**
- Conservative estimate: 8% relative churn reduction (12% → 11%)
- Revenue retained: $400K annually
- Payback period: ~4.5 months

## Audience

**Primary Decision Makers:**
- VP of Operations (sponsor)
- CFO (budget approval)

**Their Priorities:**
- VP Ops: Customer retention, team efficiency, data-driven decisions
- CFO: ROI, payback period, cost control, risk management

**Organizational Context:**
- Q2 budget planning cycle
- Company focus on retention over acquisition this year
- Previous analytics initiative (2022) had mixed results

## Requirements

**Structure:**
1. BLUF (ask + recommendation + why now + expected outcome)
2. Executive Summary (1 page max)
3. Business case with quantified ROI
4. Investment breakdown
5. Implementation timeline
6. Risks with mitigations
7. Alternatives considered
8. Anticipated objections with responses
9. Next steps if approved

**Tone:**
- Confident but not arrogant
- Data-driven (every claim supported)
- Action-oriented (clear decision needed)
- Acknowledges risks honestly

**Evidence Standards:**
- State assumptions explicitly
- Show calculation methodology
- Include sensitivity analysis
- Cite sources for benchmarks

## Anticipated Objections to Address

1. "We tried analytics before and it didn't work"
   - Address what was different (scope, vendor, data quality)

2. "Budget is tight this year"
   - Show fast payback (4.5 months)
   - Show opportunity cost of delay (~$100K per quarter)

3. "Can IT support another platform?"
   - Vendor-managed implementation
   - Minimal IT involvement (security review, SSO only)

4. "These projections seem optimistic"
   - Show conservative, base, and optimistic scenarios
   - Reference vendor case studies

## Output Format

Create a complete proposal document with:
- Clear section headers
- Tables for financial data
- Bullet points for scanning
- Executive summary that stands alone
- Appendix with detailed calculations

## Quality Criteria

The proposal is successful if:
- [ ] Ask is clear within first 30 seconds of reading
- [ ] ROI is quantified with stated assumptions
- [ ] Every claim has supporting evidence
- [ ] Objections are anticipated and addressed
- [ ] Risks are acknowledged with mitigations
- [ ] Alternatives show rigorous evaluation
- [ ] Next steps are specific and actionable
- [ ] Tone matches executive audience
```

---

## Step 7: Expected Output Quality

### What Good Looks Like

**Opening Paragraph:**
> **Request:** Approval for $150K investment in customer analytics platform (Year 1)
>
> **Recommendation:** Proceed with Q2 implementation targeting 8% churn reduction
>
> **Why Now:** Current 12% churn rate costs us $2M annually. Each quarter of delay represents ~$100K in preventable customer losses.
>
> **Expected Outcome:** $400K annual revenue retained through proactive churn prevention, with payback in 4.5 months.

**Financial Summary Table:**
| Category | Amount | Notes |
|----------|--------|-------|
| Platform license | $80K | Year 1, scales with accounts |
| Implementation | $40K | One-time setup |
| Internal resources | $25K | 0.5 FTE × 3 months |
| Training | $5K | CS team enablement |
| **Total** | **$150K** | |

**ROI Analysis:**
| Scenario | Churn Improvement | Revenue Retained | ROI (Year 1) |
|----------|-------------------|------------------|--------------|
| Conservative | 5% relative | $200K | 33% |
| Base Case | 8% relative | $400K | 167% |
| Optimistic | 15% relative | $600K | 300% |

*Methodology: [Explained in appendix]*

---

## Step 8: Common Mistakes to Avoid

**Mistake 1: Burying the Ask**
- Bad: "After careful analysis of our customer retention challenges..."
- Good: "Request: Approval for $150K investment..."

**Mistake 2: Unsupported Projections**
- Bad: "This will significantly reduce churn"
- Good: "Conservative estimate: 8% reduction based on vendor case studies averaging 15-25%"

**Mistake 3: Ignoring Alternatives**
- Bad: "We should implement Platform X"
- Good: "Three options evaluated: Platform X (recommended), build internally (too slow), hire CSMs (doesn't scale)"

**Mistake 4: Hiding Risks**
- Bad: [No risk section]
- Good: "Key risks: adoption (mitigated by phased rollout), data quality (mitigated by 60-day audit)"

**Mistake 5: Generic Objection Handling**
- Bad: "This is different from past failures"
- Good: "2022 initiative failed due to poor data integration. This platform has native connectors to our stack and dedicated implementation support."

---

## Key Takeaways

1. **Lead with the ask** - Decision makers shouldn't hunt for what you want
2. **Quantify everything** - Replace "significant" with specific numbers
3. **Show your math** - Transparency builds trust
4. **Anticipate pushback** - Address objections before they're raised
5. **Present alternatives** - Shows rigor, enables comparison
6. **Acknowledge risks** - Hidden risks destroy credibility when discovered
7. **Match the audience** - Executives want strategic impact, not technical details
8. **Create urgency** - Why now, not next quarter?

---

*This worked example demonstrates applying Professional Communication domain principles to a common business proposal scenario.*
