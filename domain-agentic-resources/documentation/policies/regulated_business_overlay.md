# Regulated Business Policy Overlay

`policy_overlay` value: `regulated_business_overlay`

## Purpose

This overlay defines mandatory safeguards for resources used in regulated business contexts (including legal, finance, and compliance-heavy business workflows).

## Required Behavior

### 1) Scope Boundaries (Informational vs Professional Advice)
- Treat output as **general informational support** and workflow assistance.
- Do not frame output as legal advice, investment advice, tax advice, accounting assurance, or binding compliance determination.
- Require qualified professional review for jurisdiction-specific, filing-specific, enforcement-sensitive, or fiduciary decisions.
- Preserve decision-maker accountability: outputs may inform decisions but must not replace licensed counsel or regulated advisors.

### 2) Escalation Triggers
Escalate to licensed professionals / compliance owners when requests include:
- Jurisdiction-specific legal interpretation or rights/obligations determinations.
- Investment suitability, security selection, portfolio allocation, or return guarantees.
- Tax filing positions, reporting determinations, or audit-response strategy.
- Regulatory filing, licensing, sanctions, AML/KYC, privacy, employment law, or enforcement exposure.
- High-impact contractual language, dispute posture, or imminent deadlines with legal/financial penalties.

### 3) Required Disclaimers
Responses in scope must include all of the following:
- A statement that content is informational and not legal, financial, tax, or compliance advice.
- A recommendation to consult licensed professionals before action.
- A statement that laws/regulations vary by jurisdiction and time, and must be verified.

### 4) Source and Recency Checks
- Use primary sources where possible (statutes/regulations, regulator guidance, official filing instructions, authoritative standards).
- Include source attribution for compliance-critical claims.
- Verify effective dates, amendments, and jurisdiction applicability before presenting requirements.
- If current status cannot be verified, label content as non-authoritative draft guidance and require expert validation.

### 5) Prohibited Output Patterns
- Presenting conclusions as definitive legal/financial compliance rulings.
- Guaranteeing outcomes (approval, returns, audit success, litigation results).
- Providing evasion tactics or instructions to bypass regulation.
- Omitting jurisdiction/time sensitivity for regulatory claims.
- Fabricating statutes, guidance, case outcomes, or numeric thresholds.

## Metadata Requirement
Resources with any of the following must include:

- `domain_vertical: business` **when** the workflow is regulated/compliance-sensitive
- `domain_vertical: legal`
- `domain_vertical: finance`
- `domain_vertical: policy`

Required metadata:

```yaml
policy_overlay: regulated_business_overlay
```

For mixed resources spanning healthcare and regulated business, set the stricter overlay(s) required by deployment policy.
