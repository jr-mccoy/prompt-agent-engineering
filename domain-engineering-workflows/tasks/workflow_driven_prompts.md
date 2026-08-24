# The 12 Workflow-Driven Prompts: Job Family Edition

# Implementation Guide: How to Use These Prompts

## Customization Protocol

Each prompt is a **template** - you must customize for your specific situation:

1. **Replace ALL bracketed placeholders**: `[Like this]` must be filled with your actual data
2. **Adjust complexity**: Remove sections that don't apply to your use case
3. **Modify success metrics**: Change targets to match your business reality
4. **Adapt terminology**: Use your company's language and frameworks

## Storage & Versioning

- Save prompts as **living documents** - update as you learn what works
- Version control: Note what you changed and why
- Share with team: Create a central prompt library

## Training Your Team

1. Start with 1-2 prompts per role
2. Run them with real data
3. Refine based on output quality
4. Document what works in your context
5. Scale to more prompts once proven

## Measuring Effectiveness

Track:

- Time saved vs. manual process
- Quality of outputs (accurate? actionable?)
- Adoption rate across team
- Business outcomes achieved

---

**TLDR These 12 prompts represent a workflow-driven alternative to generic templates. They scale with AI capability growth. They embed principles, not just instructions. And they're built for professionals who need actual results, not marketing-friendly simplicity.**

---

## ENGINEERING TEAM (3 Prompts)

### Engineering #1: Technical Debt Assessment & Prioritization

```
You are a senior engineering manager conducting a quarterly technical debt review.

### TASK
Analyze the codebase issues below and create a prioritized technical debt remediation plan.

### INPUT: TECHNICAL DEBT INVENTORY
"""
[ENGINEER PASTES: GitHub issues tagged "tech-debt", architecture concerns,
performance bottlenecks, security findings, testing gaps]
"""

### TEAM CONTEXT
Team Size: [Number]
Sprint Capacity: [Story points per sprint]
Upcoming Major Features: [List]
System Criticality: [Customer-facing/Internal/Infrastructure]

### REQUIRED OUTPUT FORMAT

**PRIORITY 1: CRITICAL PATH BLOCKERS**
(Issues that will prevent upcoming features or pose immediate risk)

Issue: [Specific tech debt item]
- Business Impact: [What breaks/slows if not fixed - quantified]
- Engineering Cost: [Story points + sprint allocation]
- Dependencies: [What this blocks or what blocks this]
- Suggested Timeline: [Sprint number or date]
- Risk if Delayed: [Specific consequence with severity]

[Repeat for 2-3 Priority 1 items]

**PRIORITY 2: ARCHITECTURAL IMPROVEMENTS**
(Issues that increase future development velocity)

[Same format - 3-5 items]

**PRIORITY 3: QUALITY OF LIFE**
(Issues that reduce toil but don't block features)

[Same format - 3-5 items]

**DEFER FOR NOW**
[List items to explicitly not tackle this quarter with brief justification]

### PRIORITIZATION LOGIC
Rank using: (Business Impact × Urgency) / Engineering Cost

Show this calculation for your top 3 recommendations.

### INTEGRATION WITH ROADMAP
For each Priority 1 item, specify:
- Which sprint to schedule it
- Which upcoming feature it should be completed before
- Whether it requires a dedicated sprint or can be integrated with feature work

### COMMUNICATION TEMPLATE
Provide a 3-sentence summary suitable for executive stakeholders that:
1. States total engineering cost for the quarter
2. Highlights biggest risk being mitigated
3. Quantifies expected velocity improvement

### CONSTRAINTS
- Total capacity must not exceed 30% of quarterly sprint capacity
- At least 1 Priority 1 item must be completed by mid-quarter
- No Priority 2 item should be scheduled before all Priority 1 items
- If any item requires >2 sprints, break it into phases

### ASSUMPTIONS TO VALIDATE
List any missing information needed for accurate assessment:
- Code coverage metrics
- Current performance baselines
- Security scan results
- Team velocity history

```

---

### Engineering #2: Production Incident Root Cause Analysis

```
You are a senior site reliability engineer conducting post-incident analysis.

### TASK
Analyze the incident data below and produce a comprehensive root cause analysis with prevention measures.

### INCIDENT DATA
"""
[ENGINEER PASTES: Incident timeline, logs, metrics, alerts, customer impact data,
initial response actions]
"""

### SYSTEM CONTEXT
Service: [Name and purpose]
Architecture: [Microservices/Monolith/Hybrid]
Traffic Volume: [Requests/day or users]
SLA Targets: [Uptime %, latency thresholds]
On-Call Response Time: [Minutes]

### REQUIRED OUTPUT FORMAT

**INCIDENT SUMMARY**
- Start Time: [Timestamp with timezone]
- Detection Time: [Timestamp - how long until detected]
- Resolution Time: [Timestamp]
- Total Duration: [Hours:Minutes]
- Severity: [SEV 1-4 with justification]

**CUSTOMER IMPACT ANALYSIS**
- Users Affected: [Number or percentage]
- Business Impact: [Revenue lost, SLA breach, customer escalations - quantified]
- User Experience: [What customers saw/experienced - 2-3 sentences]
- Downstream Systems: [What other services were affected]

**ROOT CAUSE IDENTIFICATION**

Primary Root Cause: [Single specific technical failure]
- Technical Details: [What failed at the code/infrastructure level]
- Why It Happened: [Configuration error/Code bug/Capacity issue/Dependency failure]
- Why It Wasn't Caught: [Gap in monitoring/testing/review process]

Contributing Factors: [2-4 additional issues that made this worse]
- Factor 1: [Description]
  - How It Contributed: [Specific mechanism]
- Factor 2: [Description]
  - How It Contributed: [Specific mechanism]

**TIMELINE RECONSTRUCTION**

[Create a minute-by-minute timeline showing:]
HH:MM - [Event] - [System state] - [Team action if any]

**PREVENTION MEASURES**

Immediate Actions (Complete within 1 week):
1. [Specific technical fix]
   - Implementation: [Exact change to make]
   - Owner: [Team/person]
   - Verification: [How to confirm it works]

Short-Term Improvements (Complete within 1 month):
[Same format - 2-4 items]

Long-Term Investments (Complete within 1 quarter):
[Same format - 2-3 items]

### SYSTEM IMPROVEMENT RECOMMENDATIONS

Monitoring Enhancements:
- Missing Alert: [What alert would have caught this sooner]
- Dashboard Update: [What metrics need visibility]
- Threshold Adjustment: [What needs tuning]

Testing Gaps:
- Test Scenario: [What test case is missing]
- Load Testing: [What conditions weren't simulated]
- Chaos Engineering: [What failure mode to inject regularly]

### LEARNING DOCUMENTATION

Create a one-paragraph "Incident Lesson" suitable for team wiki:
- What happened (1 sentence)
- Why it matters (1 sentence)
- What changed (1 sentence)

### FOLLOW-UP ACTIONS

List exactly 5 action items in this format:
- Action: [Specific task]
- Owner: [Name or team]
- Due Date: [Specific date]
- Success Criteria: [How we know it's done]
- Tracking: [Ticket number to create]

### COMMUNICATION REQUIREMENTS

Executive Summary (for leadership):
[3 bullets, each 1 sentence]
- What failed and customer impact
- Root cause in business terms
- Cost of prevention vs. cost of recurrence

Customer Communication (if needed):
[2-3 sentence statement if customer notification is required]

### BLAMELESS ANALYSIS REQUIREMENT
Focus on system and process failures, not individual mistakes.
If human error is a factor, identify the system gap that allowed it (missing automation, unclear documentation, inadequate tooling).

```

---

### Engineering #3: API Design Review & Standards Compliance

```
You are a principal engineer reviewing API designs for consistency, scalability, and developer experience.

### TASK
Review the API specification below and provide structured feedback on design quality and standards compliance.

### API SPECIFICATION TO REVIEW
"""
[ENGINEER PASTES: OpenAPI/Swagger spec, endpoint documentation, example requests/responses,
authentication approach, rate limiting design]
"""

### API CONTEXT
API Type: [REST/GraphQL/gRPC]
Audience: [Internal services/External developers/Partners]
Expected Traffic: [Requests/second]
Data Sensitivity: [Public/Internal/PII/Financial]
Versioning Strategy: [URL/Header/None specified]

### REQUIRED OUTPUT FORMAT

**DESIGN PRINCIPLES ASSESSMENT**

For each principle, rate: ✅ Compliant | ⚠️ Needs Improvement | ❌ Non-Compliant

**1. Resource Naming & URL Structure**
Rating: [Symbol]
- Assessment: [2-3 sentences on REST conventions, noun usage, nesting depth]
- Issues Found: [Specific examples of non-compliant endpoints]
- Recommended Fix: [Show corrected endpoint structure]

**2. HTTP Method Usage**
Rating: [Symbol]
- Assessment: [Proper use of GET/POST/PUT/PATCH/DELETE]
- Issues Found: [Examples of incorrect method choices]
- Recommended Fix: [Correct method with justification]

**3. Response Structure Consistency**
Rating: [Symbol]
- Assessment: [Envelope format, error structure, pagination approach]
- Issues Found: [Inconsistencies across endpoints]
- Recommended Fix: [Standard response template to adopt]

**4. Error Handling**
Rating: [Symbol]
- Assessment: [HTTP status codes, error messages, error codes]
- Issues Found: [Missing error cases, vague messages, wrong status codes]
- Recommended Fix: [Complete error response specification]

**5. Authentication & Authorization**
Rating: [Symbol]
- Assessment: [Auth scheme appropriate for use case, scope design]
- Issues Found: [Security gaps, missing auth on endpoints, scope issues]
- Recommended Fix: [Auth implementation requirements]

**6. Versioning Strategy**
Rating: [Symbol]
- Assessment: [Breaking change handling, deprecation path]
- Issues Found: [Missing version strategy or poor implementation]
- Recommended Fix: [Versioning approach with migration plan]

**7. Rate Limiting & Throttling**
Rating: [Symbol]
- Assessment: [Limits appropriate for use case, header communication]
- Issues Found: [Missing limits, no client guidance, unclear policies]
- Recommended Fix: [Rate limit specification with headers]

**8. Documentation Quality**
Rating: [Symbol]
- Assessment: [Completeness, examples, error scenarios]
- Issues Found: [Missing descriptions, no examples, ambiguous parameters]
- Recommended Fix: [Documentation template with required sections]

### CRITICAL ISSUES (Block Release)

List exactly 3-5 issues that must be fixed before launch:

**Issue [N]: [Brief Title]**
- Severity: [Security/Data Loss/Breaking/Performance]
- Current State: [What the API does now]
- Problem: [Why this breaks systems or creates risk]
- Required Fix: [Specific change needed]
- Verification: [How to test the fix]

### SCALABILITY ANALYSIS

**Performance Concerns:**
- Endpoint: [Which endpoint]
- Bottleneck: [N+1 queries/Missing pagination/Expensive operations]
- Impact at Scale: [What happens at 10x current traffic]
- Optimization: [Specific technical solution]

[Repeat for 2-3 performance issues]

**Data Model Issues:**
- Structure: [What's problematic in request/response]
- Growth Problem: [How this breaks with data growth]
- Refactor Needed: [How to restructure]

### DEVELOPER EXPERIENCE EVALUATION

**Ease of Use Score: [1-10]**

Justification:
- Discoverability: [How easy to find what you need]
- Learning Curve: [How quickly can someone be productive]
- Error Recovery: [How helpful are errors]

**Quick Win Improvements:**
[List 3 changes that improve DX with minimal effort]
1. [Change] - Impact: [What it improves]
2. [Change] - Impact: [What it improves]
3. [Change] - Impact: [What it improves]

### STANDARDS COMPLIANCE CHECKLIST

Compare against: [RESTful API standards/Company API guidelines/Industry best practices]

Missing Standards:
- [ ] [Standard requirement not met]
- [ ] [Standard requirement not met]
- [ ] [Standard requirement not met]

Exceeds Standards:
- [What this API does particularly well]

### BREAKING CHANGE ASSESSMENT

If this API updates an existing version:

Breaking Changes Introduced:
- Change: [What changed]
- Breaks: [What client code will fail]
- Migration Path: [How clients should adapt]

[Repeat for each breaking change]

### RECOMMENDED APPROVAL STATUS

**Status: [APPROVED / APPROVED WITH CONDITIONS / REQUIRES REVISION / REJECT]**

Justification: [2-3 sentences explaining the decision]

Conditions for Approval (if applicable):
1. [Must fix X before launch]
2. [Must add Y before launch]
3. [Must document Z before launch]

### IMPLEMENTATION GUIDANCE

Pre-Launch Requirements:
- [ ] Load testing completed at 3x expected traffic
- [ ] Security review sign-off obtained
- [ ] Monitoring and alerting configured
- [ ] Client SDK/documentation published
- [ ] Deprecation strategy documented (if applicable)

### FOLLOW-UP REVIEW

Schedule follow-up review if:
- More than 3 critical issues identified
- Breaking changes need migration validation
- Performance testing reveals bottlenecks

Recommended Review Date: [2-4 weeks depending on issues]

```

---

## PRODUCT MANAGEMENT (2 Prompts)

### Product #1: Feature Requirements Extraction from Stakeholder Conversations

```
You are a senior product manager converting messy stakeholder input into structured, testable requirements.

### TASK
Extract and structure product requirements from the stakeholder notes below.

### STAKEHOLDER INPUT
"""
[PM PASTES: Meeting notes, Slack messages, email threads, customer feedback,
sales calls, support tickets - raw unstructured input]
"""

### CONTEXT
Product: [Name and description]
Current User Base: [Size and segment]
Strategic Priority: [High/Medium/Low]
Timeline Pressure: [Launch deadline if any]
Technical Constraints: [Known limitations]

### REQUIRED OUTPUT FORMAT

**PROBLEM STATEMENT CLARIFICATION**

User Pain Point: [Single sentence describing the core problem]
- Who Experiences This: [Specific user persona/segment]
- Frequency: [How often this happens - daily/weekly/monthly]
- Current Workaround: [What users do today]
- Cost of Problem: [Time wasted/Revenue lost/Churn risk - quantified]

Business Impact:
- Revenue Opportunity: [$ amount or % increase]
- Strategic Alignment: [Which company goal this supports]
- Competitive Pressure: [Do competitors have this / Are we losing deals]

### REQUIREMENTS BREAKDOWN

**USER STORIES (Structured Format)**

Epic: [High-level feature name]

Story 1: [User story title]
- As a: [Specific user type]
- I want to: [Capability]
- So that: [Business outcome]
- Acceptance Criteria:
  1. Given [context], when [action], then [result]
  2. Given [context], when [action], then [result]
  3. [List all testable conditions]
- Priority: [Must Have / Should Have / Nice to Have]
- Effort Estimate: [T-shirt size: S/M/L/XL]

[Repeat for 5-8 stories total]

**FUNCTIONAL REQUIREMENTS**

For each major capability:

Requirement [N]: [What the system must do]
- Input: [What data/actions come in]
- Processing: [What happens in the system]
- Output: [What the user sees/gets]
- Edge Cases: [What happens when X goes wrong]
- Dependencies: [What other features this needs]

### NON-FUNCTIONAL REQUIREMENTS

**Performance:**
- Response Time: [Maximum acceptable latency]
- Throughput: [Transactions/requests per second needed]
- Data Volume: [How much data this handles]

**Security:**
- Data Sensitivity: [What type of data is involved]
- Access Control: [Who can use this feature]
- Compliance: [GDPR/HIPAA/SOC2 considerations]

**Scalability:**
- Initial Load: [Expected usage at launch]
- Growth Projection: [Expected usage in 12 months]
- Breaking Point: [At what scale does this design fail]

### MISSING INFORMATION & QUESTIONS

**Critical Unknowns (Must answer before starting):**
1. [Question about user behavior]
   - Why It Matters: [What decision depends on this]
   - How to Find Out: [Research method needed]

2. [Question about technical feasibility]
   - Why It Matters: [What decision depends on this]
   - Who to Ask: [Engineering/Architecture/Security]

[List 3-5 critical questions]

**Assumptions to Validate:**
- Assumption: [What we're assuming is true]
- Risk if Wrong: [What breaks if assumption is false]
- Validation Method: [How to test this assumption]

[List 3-4 key assumptions]

### OUT OF SCOPE (V1)

Explicitly list what is NOT included:
1. [Feature/capability]
   - Why Deferred: [Rationale for exclusion]
   - Possible Future Version: [V2/V3/Never]

[List 4-6 out of scope items]

### SUCCESS METRICS

**Primary Metric:** [The one metric that determines success]
- Baseline: [Current state]
- Target: [Goal state]
- Measurement: [How we track this]
- Timeline: [When we measure]

**Secondary Metrics:**
- [Metric 2]: Baseline [X] → Target [Y]
- [Metric 3]: Baseline [X] → Target [Y]
- [Metric 4]: Baseline [X] → Target [Y]

**Leading Indicators (Early signals):**
- Week 1: [What to watch]
- Week 4: [What to watch]
- Week 8: [What to watch]

### RISK ASSESSMENT

**Technical Risks:**
- Risk: [What could go wrong technically]
- Probability: [High/Medium/Low]
- Mitigation: [How to reduce risk]

**Market Risks:**
- Risk: [User adoption concern]
- Probability: [High/Medium/Low]
- Mitigation: [How to reduce risk]

**Execution Risks:**
- Risk: [Timeline/resource concern]
- Probability: [High/Medium/Low]
- Mitigation: [How to reduce risk]

### DEPENDENCY MAP

**Upstream Dependencies (What we need first):**
- Dependency: [Feature/system/decision]
- Owner: [Team/person]
- Status: [Complete/In Progress/Not Started]
- Blocker Impact: [What we can't do without this]

**Downstream Impact (What depends on this):**
- Affected System: [What else needs to change]
- Impact Type: [Breaking/Integration/Documentation]
- Coordination Needed: [What other teams need to know]

### STAKEHOLDER ALIGNMENT

**Decision Makers:**
- Final Approval: [Who signs off]
- Technical Approval: [Engineering lead]
- Design Approval: [Design lead]
- Go-to-Market Approval: [Sales/Marketing lead if needed]

**Communication Plan:**
- Weekly Updates: [To whom]
- Launch Announcement: [To whom and when]
- Training Needed: [Which teams need education]

### NEXT STEPS & OWNERSHIP

Immediate Actions (This Week):
1. [Action] - Owner: [Name] - Due: [Date]
2. [Action] - Owner: [Name] - Due: [Date]
3. [Action] - Owner: [Name] - Due: [Date]

Design Phase (Weeks 2-3):
- Wireframes: [Owner] - Due: [Date]
- Technical Spec: [Owner] - Due: [Date]
- User Research: [Owner] - Due: [Date]

### PRD READINESS CHECKLIST

Before moving to engineering:
- [ ] All critical unknowns answered
- [ ] Success metrics approved by leadership
- [ ] Technical feasibility confirmed
- [ ] Design mocks completed
- [ ] Edge cases documented
- [ ] Out-of-scope items agreed upon

```

---

### Product #2: Competitive Feature Analysis & Positioning

```
You are a product strategist analyzing competitive features to inform product roadmap decisions.

### TASK
Analyze the competitive feature landscape below and provide strategic recommendations.

### COMPETITIVE RESEARCH DATA
"""
[PM PASTES: Competitor feature lists, screenshots, pricing pages, customer reviews,
analyst reports, win/loss data, sales objections]
"""

### YOUR PRODUCT CONTEXT
Product: [Name]
Current Capabilities: [List key features]
Target Market: [Segment and size]
Price Point: [Your pricing vs. competitors]
Strategic Position: [Enterprise/Mid-market/SMB, Premium/Value/Budget]

### REQUIRED OUTPUT FORMAT

**COMPETITIVE LANDSCAPE OVERVIEW**

Primary Competitors: [3-5 direct competitors]
- Competitor 1: [Name]
  - Market Position: [Leader/Challenger/Niche]
  - Strengths: [2-3 key advantages]
  - Weaknesses: [2-3 vulnerabilities]
  - Recent Moves: [New features/pricing changes/acquisitions]

[Repeat for each primary competitor]

Emerging Threats: [1-2 new entrants or adjacent players]

### FEATURE COMPARISON MATRIX

Create a detailed comparison table:

| Feature Category | Your Product | Competitor A | Competitor B | Competitor C | Market Expectation |
|-----------------|--------------|--------------|--------------|--------------|-------------------|
| [Category] | [Status] | [Status] | [Status] | [Status] | [Must Have/Nice to Have] |

Status Options: ✅ Full | 🟡 Partial | ❌ Missing | 🚧 In Beta

**Analysis Notes:**
For each category where you're behind:
- Gap Description: [What specifically are we missing]
- Customer Impact: [Who cares about this gap]
- Deal Impact: [Are we losing deals because of this]

### STRATEGIC FEATURE GAPS

Identify exactly 5 feature gaps in priority order:

**Gap [N]: [Feature Name]**

Market Pressure: [High/Medium/Low]
- Evidence: [Customer requests/Lost deals/Market research]
- Competitors Who Have It: [List]
- How They Implement It: [Key differences in their approach]

Customer Segment Impact:
- Primary Affected: [Which customer segment needs this]
- Deal Size: [Average ACV of affected deals]
- Volume: [How many opportunities per quarter]

Build vs. Buy vs. Partner:
- Build Effort: [Engineering months]
- Buy Option: [Available solutions to integrate]
- Partner Option: [Potential partnerships]
- Recommendation: [Which approach and why]

Competitive Advantage Opportunity:
- Their Approach: [How competitors solve this]
- Our Differentiation Angle: [How we could do it better]
- Unique Value: [What we can deliver that they can't]

### FEATURE PARITY ANALYSIS

**Table Stakes Features (Must have to compete):**
1. [Feature] - Status: [We have it / In progress / Missing]
   - If missing, Cost of Absence: [Lost deals, churn risk]
   - Build Effort: [Time/resources]
   - Urgency: [Critical / Important / Monitor]

[List 5-7 table stakes features]

**Differentiators (Where we can win):**
1. [Feature/Capability]
   - Our Advantage: [Why we do this better]
   - Competitive Moat: [How hard to replicate]
   - Customer Value: [Measured impact]

[List 3-5 differentiators]

### POSITIONING STRATEGY

**Current Perception vs. Reality:**

How Market Sees Us:
- Strength: [What we're known for]
- Weakness: [Where we're perceived as lacking]
- Position: [Budget/Mid-market/Premium]

Reality Check:
- Actual Strengths: [Where we objectively excel]
- Actual Gaps: [Where we objectively lag]
- Position Opportunity: [Where we should move]

**Recommended Positioning:**

Primary Message: [One sentence: Who we are and why we win]

Proof Points:
1. [Feature/capability that proves the message]
2. [Customer outcome that validates the message]
3. [Competitive comparison that supports the message]

Target Buyer: [Specific role and company profile]

### WIN/LOSS PATTERN ANALYSIS

**Why We Win:**
[Based on data provided, identify patterns]
- Factor 1: [Specific capability or attribute]
  - Frequency: [% of wins this is mentioned]
  - Example Quote: [From customer/sales]
- Factor 2: [Repeat format]
- Factor 3: [Repeat format]

**Why We Lose:**
[Based on data provided, identify patterns]
- Factor 1: [Missing feature or disadvantage]
  - Frequency: [% of losses this is mentioned]
  - Lost Deal Value: [Average or total]
  - Competitor Who Won: [Pattern if any]
- Factor 2: [Repeat format]
- Factor 3: [Repeat format]

### ROADMAP IMPACT RECOMMENDATIONS

**Immediate Actions (Next Quarter):**

Recommendation 1: [Specific feature/improvement]
- Strategic Rationale: [Why this moves the needle]
- Expected Impact: [Deals saved, churn reduced, expansion enabled]
- Success Metric: [How we measure success]
- Investment: [Engineering effort + timeline]
- Risk of Not Doing: [What we lose]

[Repeat for 2-3 immediate actions]

**Medium-Term Bets (2-3 Quarters):**
[Same format - 2-3 items]

**Strategic Investments (4+ Quarters):**
[Same format - 1-2 items]

### PRICING & PACKAGING IMPLICATIONS

**Competitive Pricing Analysis:**
- Price Position: [Are we premium/parity/discount vs. competitors]
- Value Perception: [Do customers see us as worth the price]
- Packaging Gaps: [Features in wrong tier/missing tiers]

**Recommendations:**
- Pricing Adjustment: [Increase/Maintain/Decrease with rationale]
- Packaging Change: [Move X feature to Y tier because...]
- New Edition: [Create Z tier for W segment because...]

### PARTNERSHIP & ECOSYSTEM STRATEGY

**Integration Opportunities:**
[Based on competitor analysis]
- Partner: [Company/platform]
- Why: [Strategic benefit]
- Alternative: [If we built this ourselves]
- Recommendation: [Partner vs. build decision]

### COMMUNICATION PLAN

**Sales Enablement Needed:**
- Battle Card Update: [New talking points for competitive situations]
- Demo Script: [Features to emphasize against each competitor]
- Objection Handling: [New responses to common objections]

**Marketing Assets:**
- Comparison Page: [What to update on website]
- Case Studies: [Which customer stories to tell]
- Content Topics: [Blog/webinar ideas that position us well]

### MONITORING & REASSESSMENT

**Competitive Intelligence Plan:**
- Watch List: [Which competitors to monitor closely]
- Trigger Events: [What changes would require strategy shift]
- Review Cadence: [How often to update this analysis]

**Early Warning Indicators:**
- Metric: [What to track]
- Threshold: [What number signals concern]
- Response: [What to do if threshold crossed]

### DECISION FRAMEWORK

For leadership review, prioritize the gaps by:

**Priority Score = (Market Pressure × Deal Impact × Strategic Fit) / Build Effort**

Show calculations for top 5 feature gaps.

Recommended top 3 to pursue:
1. [Feature] - Score: [X] - Rationale: [Why this wins]
2. [Feature] - Score: [X] - Rationale: [Why this wins]
3. [Feature] - Score: [X] - Rationale: [Why this wins]

```

---

## SALES TEAM (2 Prompts)

### Sales #1: Discovery Call Preparation from CRM Data

```
You are a sales enablement specialist preparing account executives for high-value discovery calls.

### TASK
Analyze the account data below and create a comprehensive discovery call preparation brief.

### ACCOUNT DATA
"""
[SALES REP PASTES: CRM account info, company details, previous interactions,
website/LinkedIn research, news mentions, tech stack data, contact information]
"""

### CALL CONTEXT
Call Type: [First discovery / Second meeting / Executive briefing]
Attendees: [Names and titles of who will be on the call]
Duration: [30/45/60 minutes]
Your Goal: [Discovery / Demo / Proposal / Close]
Deal Size: [Expected ACV]

### REQUIRED OUTPUT FORMAT

**ACCOUNT INTELLIGENCE SUMMARY**

Company Overview:
- Industry: [Specific vertical]
- Size: [Employees / Revenue]
- Growth Stage: [Startup/Growth/Enterprise/Mature]
- Business Model: [B2B/B2C/Marketplace/etc.]
- Key Products: [What they sell]

Recent Developments:
- [News/funding/leadership changes/product launches from past 90 days]
- Relevance to Us: [How this creates opportunity]

Current Tech Stack:
- [Relevant systems they use]
- Integration Opportunities: [Where we fit]
- Replacement Targets: [What we could displace]

### BUYER PERSONA ANALYSIS

For each attendee on the call:

**[Name] - [Title]**

Role & Responsibilities:
- Scope: [What they own]
- Priorities: [What they care about - based on role]
- Budget Authority: [Yes/No/Influence]

Pain Points (Specific to their role):
1. [Pain point based on industry/role research]
   - Evidence: [Why we think this is a pain]
   - Our Solution: [How we address this]
2. [Repeat for 2-3 pain points per person]

Personal Background:
- Tenure: [Time at company]
- Previous Companies: [Relevant experience]
- LinkedIn Activity: [Recent posts/interests if available]

Communication Style (Predicted):
- Likely Focus: [Technical/ROI/Strategic/Operational]
- Decision Criteria: [What matters most to this person]

### DISCOVERY QUESTION STRATEGY

**Opening Questions (First 10 minutes):**

Build Rapport:
- [Personal/company congratulations based on research]
- [Industry trend question to establish credibility]

Establish Context:
1. [Open question about their current situation]
   - Why Ask: [What you're trying to learn]
   - Follow-up if X: [Next question based on response]
   - Follow-up if Y: [Alternate path]

2. [Question about pain points]
   - Why Ask: [What you're trying to learn]
   - Listen For: [Key phrases that signal opportunity]

**Deep Dive Questions (Minutes 10-35):**

Process Understanding:
3. "Walk me through [specific workflow relevant to your product]"
   - Why Ask: [Uncover inefficiencies]
   - Listen For: [Manual steps, delays, errors]
   - Follow-up: [Quantify the cost of current state]

4. "What have you tried to solve [specific problem]?"
   - Why Ask: [Understand past failed solutions]
   - Listen For: [Budget availability, vendor relationships]
   - Follow-up: [Why those solutions didn't work]

Impact Quantification:
5. "How much time/money does [problem] cost you?"
   - Why Ask: [Build ROI case]
   - Listen For: [Specific numbers]
   - Follow-up: [Impact on revenue/growth/team]

Stakeholder Mapping:
6. "Who else is involved in addressing [problem]?"
   - Why Ask: [Map buying committee]
   - Listen For: [Economic buyer, technical buyer, user buyer]
   - Follow-up: [Decision process and timeline]

**Closing Questions (Minutes 35-45):**

Decision Process:
7. "What does your evaluation process typically look like?"
   - Why Ask: [Understand sales cycle]
   - Listen For: [Steps, stakeholders, criteria, timeline]

8. "What would need to be true for you to move forward?"
   - Why Ask: [Uncover objections early]
   - Listen For: [Budget, timing, competition, authority]

### OBJECTION ANTICIPATION

**Likely Objections Based on Account Profile:**

Objection 1: [Predicted objection]
- Probability: [High/Medium/Low]
- When It Comes Up: [During discovery / After demo / At proposal]
- Handling Strategy:
  - Acknowledge: [Empathetic response]
  - Reframe: [How to position differently]
  - Evidence: [Proof point to share - case study/data/demo]

[Repeat for 4-5 likely objections]

### COMPETITIVE INTELLIGENCE

**Likely Competitors in This Deal:**
- Competitor: [Name]
  - Why They're Likely: [Based on industry/size/tech stack]
  - Their Pitch: [What they'll say]
  - Our Counter: [How we win this specific account]
  - Don't Mention Unless: [When to bring them up]

### VALUE PROPOSITION CUSTOMIZATION

**Standard Value Props:**
[Your product's general benefits]

**Customized for This Account:**

Value Prop 1: [Tailored message]
- Why It Matters Here: [Specific to their situation]
- Proof Point: [Customer story from similar company]
- Quantified Benefit: [Estimated impact with numbers]

Value Prop 2: [Tailored message]
[Same format]

Value Prop 3: [Tailored message]
[Same format]

### CALL FLOW STRUCTURE

**Minutes 0-5: Opening**
- Agenda confirmation
- Rapport building with [specific topic]
- Set expectations for call

**Minutes 5-15: Situation Understanding**
- Ask questions 1-2 from discovery strategy
- Active listening for pain signals
- Take notes on: [Specific things to capture]

**Minutes 15-30: Deep Discovery**
- Ask questions 3-6 based on what you learned
- Quantify impact where possible
- Identify buying committee

**Minutes 30-40: Initial Solution Framing**
- Summarize what you heard
- Connect to how you help (brief, not demo)
- Gauge interest level

**Minutes 40-45: Next Steps**
- Ask questions 7-8 about process
- Propose specific next meeting
- Confirm attendees and agenda

**Minutes 45-50: Buffer/Overflow**

### SUCCESS CRITERIA FOR THIS CALL

**Must Achieve:**
- [ ] Identify at least one quantifiable pain point
- [ ] Map at least 3 members of buying committee
- [ ] Understand their decision timeline
- [ ] Book specific next meeting before hanging up
- [ ] Gain access to technical/economic buyer if not on call

**Nice to Have:**
- [ ] Understand budget parameters
- [ ] Identify competitive alternatives they're considering
- [ ] Get internal champion to advocate

### RED FLAGS TO WATCH FOR

Warning signs this may not be a good fit:
- [Sign] - What to do: [Qualify out / Dig deeper / Adjust approach]
- [Sign] - What to do: [Qualify out / Dig deeper / Adjust approach]
- [Sign] - What to do: [Qualify out / Dig deeper / Adjust approach]

If you see 2+ red flags, consider: [Qualify out vs. Change strategy]

### POST-CALL ACTION PLAN

Immediately After Call:
- [ ] Update CRM with detailed notes
- [ ] Send personalized follow-up email within 2 hours
- [ ] Create/update mutual action plan
- [ ] Schedule internal debrief if enterprise deal

Follow-up Email Template:
[Name],

[Specific reference to something they said - shows you listened]

Based on our discussion, here's what I heard:
- [Pain point 1]
- [Pain point 2]
- [Decision criteria]

Next steps we agreed on:
- [Action from you] by [date]
- [Action from them] by [date]
- [Next meeting] on [date] with [attendees]

[Specific valuable resource based on their interests]

[Your name]

### DEAL QUALIFICATION SCORE

After the call, evaluate:

| Criteria | Score (1-10) | Evidence |
|----------|--------------|----------|
| Budget exists | [Score] | [What they said] |
| Authority identified | [Score] | [Who's involved] |
| Need is urgent | [Score] | [Timeline pressure] |
| Timeline defined | [Score] | [When they want to decide] |

Total Score: [Sum] / 40

Interpretation:
- 30-40: Strong opportunity, prioritize
- 20-29: Qualified opportunity, nurture actively
- 10-19: Weak opportunity, qualify out or slow play
- <10: Disqualify

### INTERNAL STAKEHOLDERS TO LOOP IN

Based on this account profile:
- [ ] Solutions Engineer (for technical deep dive)
- [ ] Customer Success (for implementation planning)
- [ ] Executive Sponsor (if deal >$X)
- [ ] Legal (if complex procurement)
- [ ] Finance (if non-standard terms needed)

### RISK MITIGATION

**Deal Risks Based on Discovery:**
- Risk: [What could derail this]
- Probability: [H/M/L]
- Mitigation: [What to do proactively]

### RESEARCH SOURCES USED

Document where intel came from:
- CRM data: [What you learned]
- LinkedIn: [What you learned]
- Company website: [What you learned]
- News/press: [What you learned]
- Tech stack tools: [What you learned]

Confidence Level: [High/Medium/Low] - [Why]

```

---

### Sales #2: Pipeline Risk Assessment & Deal Prioritization

```
You are a sales operations analyst conducting pipeline health analysis for forecast accuracy.

### TASK
Analyze the pipeline data below and provide risk assessment with prioritization recommendations.

### PIPELINE DATA
"""
[SALES REP OR MANAGER PASTES: CRM export with deals, stages, amounts, close dates,
activities, last contact dates, deal age, stakeholders, next steps]
"""

### TEAM CONTEXT
Quota: [$ amount]
Quarter: [Q# YYYY]
Days Remaining: [Number]
Team Size: [Number of reps]
Current Forecast: [$ amount]

### REQUIRED OUTPUT FORMAT

**PIPELINE HEALTH OVERVIEW**

Total Pipeline Value: [$X]
Weighted Pipeline Value: [$X] (based on stage probabilities)
Quota Attainment Projection: [X%]
Coverage Ratio: [Pipeline $ / Quota = X.XX]

Health Status: [Healthy / At Risk / Critical]
- Justification: [2-3 sentences with specific metrics]

### RISK SEGMENTATION

Classify each deal into risk categories:

**HIGH RISK DEALS (Likely to slip or lose)**

Deal: [Company Name] - [$Amount] - Stage: [Stage] - Close: [Date]
- Risk Score: [1-10]
- Risk Factors:
  - Factor 1: [Specific issue - e.g., "No activity in 14 days"]
    - Impact: [How this affects close probability]
  - Factor 2: [e.g., "Champion left company"]
    - Impact: [How this affects close probability]
  - Factor 3: [e.g., "Pushed close date 2x already"]
    - Impact: [How this affects close probability]
- Recommended Action: [Specific next step with owner and deadline]
- Forecast Recommendation: [Remove from forecast / Reduce probability / Push to next quarter]

[Repeat for all high-risk deals]

**MEDIUM RISK DEALS (Need attention)**

[Same format - deals that could go either way]

**ON TRACK DEALS (Progressing normally)**

[Same format - deals with healthy progression]

### DEAL VELOCITY ANALYSIS

**Stalled Deals:**
[Deals with no meaningful activity in >X days based on stage]

Deal: [Company] - Stalled for: [Days]
- Last Activity: [Date and type]
- Stage: [Current stage]
- Problem Diagnosis: [Why it's stuck]
- Unstick Strategy:
  1. [Specific action to re-engage]
  2. [Escalation if needed]
  3. [Timeline for decision: move forward or disqualify]

**Accelerating Deals:**
[Deals moving faster than average]

Deal: [Company] - Stage Change: [From X to Y in Z days]
- Acceleration Factors: [What's driving speed]
- Watch For: [Potential pitfalls when deals move too fast]
- Capture Strategy: [How to maintain momentum]

### STAGE-BY-STAGE ANALYSIS

For each pipeline stage:

**[Stage Name]** - [X deals] - [$Y total value]

Average Time in Stage: [Days]
Expected Close Rate: [Historical %]
Current Concerns:
- [Specific issue with deals at this stage]

Conversion Bottlenecks:
- Issue: [What's preventing progression]
- Affected Deals: [How many]
- Solution: [What needs to happen]

Required Actions This Week:
- [ ] [Action to move deals forward]
- [ ] [Action to move deals forward]

### ACTIVITY-BASED RISK INDICATORS

**Engagement Health Metrics:**

| Deal | Last Email | Last Call | Last Meeting | Activities (30d) | Risk Level |
|------|-----------|-----------|--------------|------------------|------------|
| [Company] | [Days ago] | [Days ago] | [Days ago] | [Count] | [H/M/L] |

Interpretation:
- Red Flags: [Which patterns indicate trouble]
- Healthy Patterns: [What good engagement looks like]

### STAKEHOLDER COVERAGE ANALYSIS

For deals >$X:

**[Company Name] - [$Amount]**

Buying Committee Coverage:
- Economic Buyer: [Identified? Engaged? Champion status?]
- Technical Buyer: [Identified? Engaged? Concerns?]
- User Buyer: [Identified? Engaged? Advocate?]
- Coach/Champion: [Who? Reliability?]

Coverage Score: [X/4 mapped, Y/4 engaged]
Risk: [What's missing and why it matters]
Action: [How to fill gaps]

### COMPETITIVE INTELLIGENCE IN PIPELINE

Deals with Known Competition:

**[Company] - vs. [Competitor]**
- Their Status: [Stage they're at]
- Our Position: [Winning/Even/Losing]
- Key Differentiator: [Our winning angle]
- Vulnerability: [Where they're beating us]
- Counter Strategy: [Specific actions to win]

### CLOSE DATE INTEGRITY ASSESSMENT

**Deals with Close Dates This Month:**

| Deal | Amount | Date | Days Left | Next Step | Date Set By | Confidence |
|------|--------|------|-----------|-----------|-------------|------------|
| [Co] | [$] | [Date] | [#] | [Step] | [Who] | [%] |

Red Flags:
- [Deals with close dates but no next meeting scheduled]
- [Deals with close dates but missing stakeholders]
- [Deals with close dates but stalled activity]

Realistic Close Forecast:
- Committed: [$X] - [List companies]
- Likely: [$X] - [List companies]
- Possible: [$X] - [List companies]
- Removed: [$X] - [List companies and why]

### RESOURCE ALLOCATION RECOMMENDATIONS

**Deals Requiring Leadership Involvement:**
1. [Company] - [$Amount]
   - Why: [Strategic importance / Large size / Stuck / Competitive]
   - Specific Ask: [Executive meeting / Reference call / Custom terms]
   - Owner: [Which executive] - By When: [Date]

**Deals Needing Solution Engineering:**
[Prioritized list with technical hurdles]

**Deals Ready to Close:**
[Prioritized list needing paperwork/legal/procurement support]

### PIPELINE GENERATION REQUIREMENTS

**Gap Analysis:**
Current Pipeline: [$X]
Required to Hit Quota: [$Y]
Gap: [$Z]

To Close Gap:
- New Deals Needed: [#] (at average deal size of [$X])
- OR Expansion of Existing: [Which deals could grow]
- OR Acceleration Strategy: [How to close faster]

**Lead Source Performance:**
[If data available]
- Source: [Type] - Deals: [#] - Close Rate: [%] - Average: [$]
- Recommendation: [Double down / Maintain / Reduce investment]

### FORECAST ACCURACY CHECK

**Historical Pattern Analysis:**
[If previous quarter data available]

Last Quarter:
- Forecasted: [$X]
- Actual: [$Y]
- Variance: [+/-%]
- Common Slip Reasons: [Pattern in what didn't close]

This Quarter - Avoid Repeats:
- [ ] [Check specific to past slippage pattern]
- [ ] [Check specific to past slippage pattern]

### ACTION PLAN BY ROLE

**For Sales Reps:**

High Priority (This Week):
1. [Action] on [Deal] - Why: [Risk mitigation / Acceleration / Closing]
2. [Action] on [Deal] - Why: [Risk mitigation / Acceleration / Closing]
3. [Action] on [Deal] - Why: [Risk mitigation / Acceleration / Closing]

Medium Priority (This Month):
[List 3-5 actions]

**For Sales Manager:**

Deal Reviews Needed:
- [Deal] with [Rep] - Focus: [Specific risk / strategy]

Coaching Opportunities:
- [Pattern across multiple deals] - Rep Training Needed: [Topic]

Forecasting Adjustments:
- Move [Deal] from [Stage/Forecast Category] to [Stage/Forecast Category]
- Rationale: [Specific evidence]

### PIPELINE HYGIENE ISSUES

Data Quality Problems:
- [ ] [X deals missing next steps]
- [ ] [Y deals with close dates in past]
- [ ] [Z deals with incomplete contact info]

Required CRM Cleanup:
1. [Specific update needed] - Owner: [Who] - By: [Date]

### DEAL PRIORITIZATION FRAMEWORK

**Priority Score = (Deal Size × Close Probability × Strategic Value) / Days to Close**

Calculated Priorities:

| Rank | Company | Score | Amount | Probability | Days Left | Action Required |
|------|---------|-------|--------|-------------|-----------|-----------------|
| 1 | [Co] | [#] | [$] | [%] | [#] | [What to do now] |
| 2 | [Co] | [#] | [$] | [%] | [#] | [What to do now] |
| 3 | [Co] | [#] | [$] | [%] | [#] | [What to do now] |

Focus 80% of efforts on top 5 deals.

### SUCCESS METRICS & TRACKING

Weekly Check-Ins:
- Metric: [What to measure]
- Target: [Number/percentage]
- Action if Below: [What to do]

Example:
- New qualified opportunities added: Target 5/week
- Deals advancing stages: Target 3/week
- High-risk deals re-engaged: Target 2/week

### QUARTER-END STRATEGY

Deals That Could Close Early:
- [Company] - Incentive: [What might accelerate]
- Action: [Specific proposal to advance]

Deals to Push to Next Quarter:
- [Company] - Why: [Not real/Not ready/Low probability]
- Benefits: [Clean forecast + focus resources]

### RISK MITIGATION PLAYBOOK

If Forecast Shortfall Projected:

**Option 1: Accelerate Current Deals**
- Target: [Which deals]
- Method: [Specific incentives/concessions]
- Risk: [What we give up]

**Option 2: Expand Deal Sizes**
- Target: [Which deals could grow]
- Method: [Upsell motion]
- Probability: [Likelihood of success]

**Option 3: Aggressive New Pipeline**
- Source: [Where to find deals]
- Timeframe: [Can they close this quarter?]
- Resource: [What's needed]

**Recommended Approach:** [Which option(s) and why]

```

---

## MARKETING TEAM (2 Prompts)

### Marketing #1: Content Performance Analysis & Gap Identification

```
You are a content marketing strategist analyzing performance data to optimize content strategy.

### TASK
Analyze the content performance data below and identify strategic gaps and opportunities.

### PERFORMANCE DATA
"""
[MARKETER PASTES: Analytics data (traffic, engagement, conversions), content inventory,
keyword rankings, competitor content analysis, audience data, conversion paths]
"""

### BUSINESS CONTEXT
Industry: [Sector]
Target Audience: [Specific segments]
Content Goals: [Awareness/Consideration/Conversion focus]
Team Size: [Writers/designers/video producers]
Monthly Budget: [$X] or [Hours available]

### REQUIRED OUTPUT FORMAT

**CONTENT PORTFOLIO HEALTH OVERVIEW**

Total Content Pieces: [Number]
- Blog Posts: [#]
- Videos: [#]
- Whitepapers: [#]
- Case Studies: [#]
- Webinars: [#]
- Other: [#]

Performance Summary:
- Top 10% Content: [# pieces] driving [% of traffic/conversions]
- Middle 60% Content: [# pieces] with [performance description]
- Bottom 30% Content: [# pieces] - Status: [Underperforming/Needs optimization]

Content Production Rate:
- Current: [# pieces per month]
- Quality vs. Quantity Balance: [Assessment]

### TOP PERFORMING CONTENT ANALYSIS

For each of the top 5 performing pieces:

**[Content Title]** - Type: [Blog/Video/etc.]

Performance Metrics:
- Traffic: [Visits] - [% of total]
- Engagement: [Time on page / Video completion / Downloads]
- Conversions: [Number] - Conversion Rate: [%]
- Value: [$Revenue/leads attributed]

Success Factors:
1. [Why this performed well - topic/format/distribution]
2. [Specific element that resonated]
3. [Timing or context advantage]

Replication Opportunities:
- Similar Topics: [3-5 related content ideas]
- Format Application: [How to use this format elsewhere]
- Promotion Strategy: [What distribution worked]

### UNDERPERFORMING CONTENT AUDIT

**Content with High Potential / Low Performance:**

[Content Title] - Published: [Date]

Metrics:
- Expected Performance: [Based on topic/keyword volume]
- Actual Performance: [Current metrics]
- Gap: [% underperformance]

Diagnosis:
- Issue 1: [SEO problem/Content quality/Promotion gap]
  - Evidence: [Specific data point]
- Issue 2: [Another issue]
  - Evidence: [Specific data point]

Optimization Plan:
- Action 1: [Specific change - e.g., "Rewrite intro to address search intent"]
  - Effort: [Hours]
  - Expected Lift: [% improvement]
- Action 2: [Another action]
  - Effort: [Hours]
  - Expected Lift: [% improvement]

Decision: [Optimize / Rewrite / Retire / Redirect]

[Repeat for 5-10 high-potential underperformers]

### CONTENT GAP ANALYSIS

**Audience-Based Gaps:**

[Buyer Persona] - [Job Title/Role]

Current Coverage:
- Awareness Stage: [# pieces] - Quality: [Good/Fair/Poor]
- Consideration Stage: [# pieces] - Quality: [Good/Fair/Poor]
- Decision Stage: [# pieces] - Quality: [Good/Fair/Poor]

Critical Missing Content:
1. [Specific content type] addressing [Specific need]
   - Audience Pain Point: [What they're trying to solve]
   - Search Intent: [What they'd search for]
   - Format Recommendation: [Blog/Video/Guide/Comparison]
   - Priority: [High/Medium/Low]
   - Business Impact: [How this drives pipeline/revenue]

[Repeat for 3-5 gaps per persona]

**Keyword-Based Gaps:**

High-Value Keywords We're Missing:

| Keyword | Volume | Difficulty | Current Rank | Opportunity | Content Needed |
|---------|--------|------------|--------------|-------------|----------------|
| [Phrase] | [#/mo] | [Score] | [Position or 0] | [Why important] | [Content type] |

[List 10-15 high-opportunity keywords]

**Competitor Content Gaps:**

Competitor: [Name]

Their Top Content We Don't Have:
1. [Content topic/type]
   - Their Performance: [Estimated traffic/engagement]
   - Why It Works: [What makes it successful]
   - Our Angle: [How we'd do it differently/better]
   - Priority: [High/Medium/Low]

[Repeat for top 3 competitors]

### CONVERSION PATH ANALYSIS

**Content Journey Mapping:**

Typical Conversion Paths:
1. Entry → [Content piece] → [Content piece] → [Conversion action]
   - Volume: [# users on this path]
   - Conversion Rate: [%]
   - Drop-off Point: [Where people leave]

[Repeat for top 3-5 paths]

Missing Bridges:
- From [Topic/Stage] to [Topic/Stage]: [What content would connect these]
- Impact: [# users who could benefit]
- Content Recommendation: [Specific piece to create]

### CONTENT FORMAT PERFORMANCE

**Format Effectiveness by Goal:**

| Format | Avg. Traffic | Avg. Engagement | Conversion Rate | Cost to Produce | ROI Score |
|--------|-------------|-----------------|-----------------|-----------------|-----------|
| Blog Post | [#] | [Metric] | [%] | [$/#h] | [Score] |
| Video | [#] | [Metric] | [%] | [$/#h] | [Score] |
| Whitepaper | [#] | [Metric] | [%] | [$/#h] | [Score] |
| Case Study | [#] | [Metric] | [%] | [$/#h] | [Score] |

Insights:
- Best for Awareness: [Format] - Why: [Reason]
- Best for Engagement: [Format] - Why: [Reason]
- Best for Conversion: [Format] - Why: [Reason]
- Best ROI: [Format] - Why: [Reason]

Format Recommendations:
- Increase: [Format] - Rationale: [Why invest more]
- Decrease: [Format] - Rationale: [Why reduce]
- Experiment: [New format] - Hypothesis: [Expected benefit]

### SEASONAL & TRENDING OPPORTUNITIES

**Seasonal Patterns Identified:**

[Month/Quarter]: [Traffic/engagement pattern]
- Historical Performance: [What's worked before]
- 2025 Opportunity: [Content to prepare]
- Prep Timeline: [When to create]

**Emerging Trends:**

Trend: [Topic/keyword gaining volume]
- Growth Rate: [% increase over time period]
- Current Competition: [Low/Medium/High]
- Our Position: [Do we have content? What's its rank?]
- Action Plan: [Create new / Optimize existing / Monitor]

### DISTRIBUTION & PROMOTION ANALYSIS

**Channel Performance:**

| Channel | Content Shared | Avg. Engagement | Traffic Driven | Conversions | Best Content Type |
|---------|---------------|-----------------|----------------|-------------|-------------------|
| Organic Search | [#] | [Metric] | [#] | [#] | [Type] |
| Social Media | [#] | [Metric] | [#] | [#] | [Type] |
| Email | [#] | [Metric] | [#] | [#] | [Type] |
| Paid | [#] | [Metric] | [#] | [#] | [Type] |
| Referral | [#] | [Metric] | [#] | [#] | [Type] |

Underutilized Channels:
- [Channel]: [Why it's underused] - [Opportunity]

Distribution Gaps:
- [Content piece] performed well but only promoted via [channel]
- Opportunity: [How multi-channel distribution could amplify]

### CONTENT REFRESH STRATEGY

**High-Value Refresh Candidates:**

[Content Title] - Published: [Date] - Last Updated: [Date]

Current Performance:
- Historical Peak: [Metric at best point]
- Current State: [Metric now]
- Decline: [% drop]

Refresh Rationale:
- [ ] Information outdated (statistics, screenshots, examples)
- [ ] Search intent shifted (what people want changed)
- [ ] Competitors outranking with better content
- [ ] Missing recent developments (new features, trends)

Refresh Plan:
- Update Scope: [What sections need work]
- New Sections: [What to add]
- Effort: [Hours]
- Expected Recovery: [% of original performance or better]
- Priority: [High/Medium/Low based on potential impact]

[List 10-15 refresh candidates]

### CONTENT INVESTMENT RECOMMENDATIONS

**Recommended Content Budget Allocation:**

| Category | Current % | Recommended % | Rationale |
|----------|----------|---------------|-----------|
| New Creation | [%] | [%] | [Why adjust] |
| Optimization | [%] | [%] | [Why adjust] |
| Promotion | [%] | [%] | [Why adjust] |
| Experimentation | [%] | [%] | [Why adjust] |

### 90-DAY CONTENT ROADMAP

**Month 1: [Focus Theme]**

Week 1-2:
- Create: [2-3 high-priority new pieces]
- Optimize: [3-5 refresh candidates]
- Promote: [Specific distribution push]

Week 3-4:
[Same structure]

**Month 2: [Focus Theme]**
[Same structure]

**Month 3: [Focus Theme]**
[Same structure]

**Success Metrics by Month:**
- Month 1 Targets: [Traffic/engagement/conversion goals]
- Month 2 Targets: [Goals]
- Month 3 Targets: [Goals]

### RESOURCE ALLOCATION

**Content Team Capacity:**

Current Allocation:
- New Content Creation: [% of time]
- Content Optimization: [% of time]
- Promotion/Distribution: [% of time]
- Analysis/Planning: [% of time]

Recommended Allocation:
[Adjust based on findings]

**Skill Gaps:**
- Need: [Specific capability]
- Current State: [What's missing]
- Solution: [Hire / Train / Outsource / Tools]

### COMPETITIVE POSITIONING

**Content Advantage Areas:**
[Where we're beating competitors]
- Advantage: [Specific area]
- Maintain Strategy: [How to keep lead]

**Content Disadvantage Areas:**
[Where competitors are ahead]
- Gap: [Specific area]
- Catch-Up Strategy: [How to close gap]
- Timeline: [When we can achieve parity]

### MEASUREMENT FRAMEWORK

**Primary KPIs:**
- North Star Metric: [Main goal - leads/revenue/traffic]
- Supporting Metrics: [2-3 indicators of health]

**Leading Indicators:**
- Week 1: [What to measure early]
- Week 4: [What to check mid-month]
- Week 8: [What confirms strategy is working]

**Dashboard Requirements:**
Track these weekly:
- [ ] [Metric] - Target: [Number]
- [ ] [Metric] - Target: [Number]
- [ ] [Metric] - Target: [Number]

Alert triggers:
- If [metric] drops below [threshold] → [Action]

### EXPERIMENTATION PLAN

**Tests to Run:**

Experiment 1: [Hypothesis]
- Test: [What you'll try]
- Control: [Current approach]
- Success Metric: [How to measure]
- Duration: [Weeks]
- Decision Criteria: [Threshold to implement]

[List 3-5 experiments]

### RISK MITIGATION

**Content Strategy Risks:**
- Risk: [What could go wrong]
- Probability: [H/M/L]
- Impact: [Effect on goals]
- Mitigation: [How to reduce risk]

### NEXT STEPS & OWNERSHIP

**Immediate Actions (This Week):**
1. [Action] - Owner: [Name] - Deliverable: [Specific output]
2. [Action] - Owner: [Name] - Deliverable: [Specific output]
3. [Action] - Owner: [Name] - Deliverable: [Specific output]

**This Month:**
[5-8 priority actions with owners]

**This Quarter:**
[3-5 strategic initiatives with owners]

```

---

### Marketing #2: Campaign Brief Development from Business Goals

```
You are a campaign strategist translating business objectives into executable marketing campaigns.

### TASK
Convert the business goals below into a comprehensive campaign brief with tactics and success metrics.

### BUSINESS OBJECTIVES
"""
[MARKETER PASTES: Business goals, revenue targets, market expansion plans,
product launch details, competitive challenges, customer insights]
"""

### CAMPAIGN CONSTRAINTS
Budget: [$X] or [Not specified]
Timeline: [Start date] to [End date] = [# weeks]
Team: [Available resources]
Geography: [Markets to cover]
Must-Use Channels: [Any required platforms]
Brand Guidelines: [Link or key restrictions]

### REQUIRED OUTPUT FORMAT

**CAMPAIGN STRATEGIC FOUNDATION**

Business Goal Translation:
- Business Objective: [Stated goal from input]
- Marketing Translation: [What this means for marketing]
- Success Metric: [How we measure marketing contribution]
- Target: [Specific number to achieve]

Campaign Name: [Internal and external versions if different]

Campaign Duration: [Dates]
- Phase 1: [Dates] - Focus: [What happens]
- Phase 2: [Dates] - Focus: [What happens]
- Phase 3: [Dates] - Focus: [What happens]

### AUDIENCE DEFINITION

**Primary Audience:**

Demographics:
- Title/Role: [Specific]
- Industry: [Specific]
- Company Size: [Employees/Revenue]
- Geography: [Specific markets]

Psychographics:
- Pain Points: [Top 3 specific to this campaign]
- Goals: [What they're trying to achieve]
- Decision Criteria: [What matters in purchase]
- Media Consumption: [Where they get information]

Sizing:
- Addressable Market: [Estimated number]
- Reachable via Our Channels: [Estimated number]
- Target: [How many we aim to engage]

**Secondary Audience(s):**
[If applicable - same format as primary]

### VALUE PROPOSITION

**Core Message:**
[Single sentence - what we want audience to believe]

**Supporting Messages:**
1. [Benefit/proof point]
2. [Benefit/proof point]
3. [Benefit/proof point]

**Message Testing:**

Why This Matters to Audience:
- Problem: [What pain does this solve]
- Solution: [How we solve it uniquely]
- Proof: [Why they should believe us]

Differentiation vs. Competitors:
- Competitor A says: [Their message]
- We say: [Our contrasting/superior message]

### CAMPAIGN ARCHITECTURE

**Customer Journey Mapping:**

**Awareness Stage:**
- Audience State: [What they know/believe now]
- Our Goal: [What we want them to know/believe]
- Content Hooks: [3-5 topic angles]
- Call to Action: [Specific next step]

**Consideration Stage:**
- Audience State: [Where they are after awareness]
- Our Goal: [What we want them to do]
- Content Hooks: [3-5 topic angles]
- Call to Action: [Specific next step]

**Decision Stage:**
- Audience State: [Where they are after consideration]
- Our Goal: [Conversion action]
- Content Hooks: [3-5 topic angles]
- Call to Action: [Specific conversion CTA]

### CHANNEL STRATEGY

**Channel Mix:**

| Channel | Role | Audience % | Budget % | Content Types | Success Metric |
|---------|------|-----------|----------|---------------|----------------|
| [Channel] | [Awareness/Consideration/Conversion] | [%] | [%] | [Types] | [Metric] |

For Each Primary Channel:

**[Channel Name]**

Objective: [What this channel achieves]

Tactics:
1. [Specific tactic]
   - Format: [Ad type/content format]
   - Volume: [How many/how often]
   - Targeting: [Specific audience parameters]
   - Budget: [$X]
   - Timeline: [When this runs]

2. [Another tactic]
[Same format]

Success Metrics:
- Primary: [Main KPI] - Target: [Number]
- Secondary: [Supporting KPI] - Target: [Number]

Integration Points:
- Connects to [Other channel] via [How they work together]
- Retargeting from [Source] to [Destination]

### CONTENT PLAN

**Content Calendar:**

| Week | Asset | Format | Channel | Audience Stage | Owner | Due Date | Status |
|------|-------|--------|---------|----------------|-------|----------|--------|
| 1 | [Title] | [Type] | [Where] | [Stage] | [Name] | [Date] | [Status] |

[List all content assets needed for campaign]

**Creative Brief for Key Assets:**

Asset: [Name/Description]

Objective: [What this asset needs to achieve]

Format/Specs:
- Type: [Blog/Video/Ad/Email/Landing page]
- Length: [Word count/video duration]
- Technical: [Dimensions/file type]

Content Requirements:
- Hero Message: [Main headline/hook]
- Supporting Points: [3-5 key messages]
- Visual Elements: [Photography/graphics/data viz needs]
- Brand Elements: [Logo/colors/fonts]
- Legal/Compliance: [Disclaimers/requirements]

Call to Action:
- Primary CTA: [Button text/action]
- Secondary CTA: [If applicable]

Success Criteria:
- Awareness Asset: [Engagement rate target]
- Consideration Asset: [Click-through rate target]
- Conversion Asset: [Conversion rate target]

### LANDING PAGE STRATEGY

**[Campaign Landing Page URL]**

Purpose: [Conversion goal]

Structure:
1. Hero Section:
   - Headline: [Specific text]
   - Subhead: [Supporting text]
   - Visual: [What's shown]
   - CTA: [Button text]

2. Value Proposition:
   - [Benefit 1 with visual]
   - [Benefit 2 with visual]
   - [Benefit 3 with visual]

3. Social Proof:
   - [Testimonial/case study/logos]

4. Objection Handling:
   - FAQ or feature comparison

5. Final CTA:
   - [Strong close with CTA]

Conversion Elements:
- Form Fields: [Specific fields - keep minimal]
- Privacy/Security: [Trust signals]
- Exit Intent: [If applicable]

A/B Test Plan:
- Test 1: [Element to test] - Hypothesis: [Expected winner]
- Test 2: [Element to test] - Hypothesis: [Expected winner]

### PAID MEDIA PLAN

**Budget Allocation:**

| Channel | Budget | Goal | Expected Results | Cost Per [Goal] |
|---------|--------|------|------------------|-----------------|
| Paid Search | [$] | [Conversions] | [# of conversions] | [$X] |
| Paid Social | [$] | [Engagement/Awareness] | [Impressions/clicks] | [$X] |
| Display | [$] | [Awareness] | [Impressions] | [$X CPM] |
| Retargeting | [$] | [Conversions] | [# of conversions] | [$X] |

**Paid Search Strategy:**

Keywords:
- Tier 1 (High intent): [5-10 keywords]
  - Bid Strategy: [Target CPA/ROAS]
  - Budget: [$X/day]
- Tier 2 (Mid intent): [10-15 keywords]
  - Bid Strategy: [Target CPA/ROAS]
  - Budget: [$X/day]

Ad Copy Variants:
- Variant A: [Headline] | [Description]
- Variant B: [Headline] | [Description]
- Variant C: [Headline] | [Description]

**Paid Social Strategy:**

Platform: [LinkedIn/Facebook/Instagram/Twitter]

Audience Targeting:
- Segment 1: [Specific parameters]
  - Size: [Estimated reach]
  - Budget: [$X]
- Segment 2: [Specific parameters]
  - Size: [Estimated reach]
  - Budget: [$X]

Ad Formats:
- [Format]: [Creative concept] - Budget: [$X]
- [Format]: [Creative concept] - Budget: [$X]

### EMAIL MARKETING PLAN

**Email Sequence:**

Email 1: [Send date] - [Audience segment]
- Subject: [Text]
- Preview Text: [Text]
- Content: [Key points]
- CTA: [Action]
- Success Metric: [Open rate X% / Click rate Y%]

[Repeat for full sequence]

**Segmentation Strategy:**
- Segment: [Criteria]
- Message Variation: [How content differs]
- Volume: [# recipients]

**Nurture Path:**
- Engaged (clicked): → [Next email] → [Next email] → [Conversion offer]
- Opened only: → [Re-engagement email] → [Alternative content] → [Last attempt]
- Did not open: → [Subject line variant] → [Different send time] → [Remove from campaign]

### PARTNERSHIP & INFLUENCER STRATEGY

**Partners to Engage:**

Partner: [Company/Person]
- Audience Overlap: [Why they're relevant]
- Ask: [Specific collaboration]
- Deliverable: [What they provide]
- Compensation: [$/ Trade / Free product]
- Timeline: [When this happens]
- Success Metric: [How we measure value]

### EVENT/WEBINAR STRATEGY

**[Event Name]** - Date: [When] - Format: [In-person/Virtual/Hybrid]

Topic: [Title]
- Angle: [Why this is compelling]
- Speaker: [Who presents]

Promotion Timeline:
- T-4 weeks: [Launch promotion activities]
- T-2 weeks: [Reminder campaign]
- T-1 week: [Final push]
- T-0: [Day-of promotion]
- T+1 day: [Follow-up to attendees]
- T+3 days: [Follow-up to no-shows with recording]

Registration Target: [# registrations]
Attendance Target: [# attendees] ([% of registrations])
Pipeline Target: [# qualified leads]

### MEASUREMENT & ANALYTICS

**Campaign Dashboard:**

Track these metrics weekly:

| Metric | Week 1 | Week 2 | Week 3 | ... | Target | Status |
|--------|--------|--------|--------|-----|--------|--------|
| Impressions | | | | | [#] | |
| Clicks | | | | | [#] | |
| Leads | | | | | [#] | |
| MQLs | | | | | [#] | |
| Opportunities | | | | | [#] | |
| Pipeline $ | | | | | [$] | |

**Attribution Model:**

How we credit conversions:
- Model: [First-touch/Last-touch/Multi-touch]
- Campaign Influence: [How we measure if this campaign helped]
- Tools: [Platform for tracking]

**Success Criteria:**

Minimum Viable Success:
- [Metric]: [Minimum acceptable number]
- If below this → [Action to take]

Target Success:
- [Metric]: [Goal number]
- If hit this → [Celebration + investment decisions]

Stretch Success:
- [Metric]: [Exceptional number]
- If exceed this → [Major investment decisions]

### OPTIMIZATION PLAN

**Weekly Review Protocol:**

What to check every Monday:
- [ ] [Metric] - If below [threshold] → [Adjustment]
- [ ] [Metric] - If below [threshold] → [Adjustment]
- [ ] [Metric] - If below [threshold] → [Adjustment]

**Optimization Tactics:**

If awareness is low:
- [ ] Increase [channel] spend by [%]
- [ ] Test new creative variants
- [ ] Expand audience targeting

If engagement is low:
- [ ] Revise messaging/offer
- [ ] A/B test new content hooks
- [ ] Improve landing page experience

If conversion is low:
- [ ] Simplify form/process
- [ ] Add trust signals
- [ ] Adjust targeting to higher intent

### BUDGET MANAGEMENT

**Campaign Budget Breakdown:**

| Category | Amount | % of Total | Notes |
|----------|--------|------------|-------|
| Paid Media | [$] | [%] | [Allocation notes] |
| Content Production | [$] | [%] | [What this covers] |
| Tools/Tech | [$] | [%] | [Platforms needed] |
| Events | [$] | [%] | [If applicable] |
| Contingency | [$] | [%] | [Reserve for optimization] |
| **Total** | **[$]** | **100%** | |

**Budget Pacing:**

| Week | Planned Spend | Actual Spend | Variance | Adjustments |
|------|--------------|--------------|----------|-------------|
| 1 | [$] | | | |
| 2 | [$] | | | |
| ... | | | | |

Budget Alerts:
- If 50% spent by week [X] and results below target → [Action]
- If 75% spent by week [Y] and results at target → [Action]
- If budget remaining with 2 weeks left → [Action]

### RISK MITIGATION

**Campaign Risks:**

Risk: [What could go wrong]
- Probability: [H/M/L]
- Impact: [Effect on campaign]
- Mitigation: [How to prevent/minimize]
- Contingency: [What to do if it happens]

[List 5-7 key risks]

### TEAM ROLES & RESPONSIBILITIES

| Role | Name | Responsibilities | Deliverables | Check-ins |
|------|------|------------------|--------------|-----------|
| Campaign Manager | [Name] | [Duties] | [What they deliver] | [Frequency] |
| Content Lead | [Name] | [Duties] | [What they deliver] | [Frequency] |
| Paid Media | [Name] | [Duties] | [What they deliver] | [Frequency] |
| Design | [Name] | [Duties] | [What they deliver] | [Frequency] |

### STAKEHOLDER COMMUNICATION

**Reporting Schedule:**

Weekly:
- To: [Stakeholders]
- Format: [Email/Dashboard/Meeting]
- Content: [What's included]

Monthly:
- To: [Leadership]
- Format: [Presentation]
- Content: [Performance + insights + optimizations]

End of Campaign:
- To: [All stakeholders]
- Format: [Comprehensive report]
- Content: [Full results + learnings + recommendations]

### POST-CAMPAIGN PLAN

**Learning Capture:**

Questions to answer:
- What worked better than expected?
- What underperformed and why?
- What would we do differently?
- What should we scale?
- What should we never do again?

**Asset Repurposing:**

Content to reuse:
- [Asset]: [How to repurpose]
- [Asset]: [How to repurpose]

**Follow-Up Campaign:**

For campaign participants:
- [Nurture sequence/next offer]

For non-converters:
- [Re-engagement strategy]

### CAMPAIGN CHECKLIST

Pre-Launch (2 weeks before):
- [ ] All content created and approved
- [ ] Landing pages live and tested
- [ ] Tracking/analytics configured
- [ ] Paid campaigns set up (not live)
- [ ] Email sequences loaded
- [ ] Team trained on process
- [ ] Legal/compliance review complete

Launch Week:
- [ ] Turn on paid campaigns
- [ ] Send launch emails
- [ ] Activate social promotion
- [ ] Monitor for errors
- [ ] Respond to inquiries

Ongoing:
- [ ] Weekly optimization review
- [ ] Budget pacing check
- [ ] Creative refresh if needed
- [ ] Stakeholder updates

Post-Campaign:
- [ ] Final report compiled
- [ ] Learnings documented
- [ ] Follow-up campaigns activated
- [ ] Attribution analysis complete

```

---

## CUSTOMER SUCCESS (2 Prompts)

### Customer Success #1: Account Health Assessment & Risk Identification

```
You are a customer success strategist conducting account health reviews to prevent churn and identify expansion opportunities.

### TASK
Analyze the customer account data below and provide a comprehensive health assessment with action plans.

### ACCOUNT DATA
"""
[CSM PASTES: Usage metrics, support tickets, NPS/CSAT scores, product adoption data,
contract details, stakeholder engagement, communication history, business outcomes]
"""

### ACCOUNT CONTEXT
Account: [Company Name]
Tier: [Enterprise/Mid-Market/SMB]
ARR: [$Amount]
Contract Start: [Date]
Renewal Date: [Date] - [Days until renewal]
Seats/Licenses: [Number]
Primary Use Case: [What they use product for]

### REQUIRED OUTPUT FORMAT

**EXECUTIVE HEALTH SUMMARY**

Overall Health Score: [0-100]
- Calculation: [Show formula used]
- Trend: [↑ Improving / → Stable / ↓ Declining]
- 30-Day Change: [+/- points]

Health Status: [🟢 Healthy / 🟡 At Risk / 🔴 Critical]

One-Sentence Assessment: [Concise summary of account state]

Immediate Action Required: [Yes/No - If yes, what specifically]

### HEALTH DIMENSION ANALYSIS

**1. PRODUCT ADOPTION**

Adoption Score: [0-100]

Usage Metrics:
- Active Users: [X] of [Y] licenses = [%]
- Login Frequency: [X times per week/month]
- Feature Utilization: [X] of [Y] key features used = [%]
- Power User Count: [Number of users with >X actions/week]

Adoption Depth by Feature:

| Feature | Adoption % | Trend | Industry Benchmark | Status |
|---------|-----------|-------|-------------------|--------|
| [Feature] | [%] | [↑/→/↓] | [%] | [Above/At/Below] |

Red Flags:
- [ ] Core feature unused ([Feature] - 0 usage in [timeframe])
- [ ] Declining usage ([% drop] over [timeframe])
- [ ] License waste ([%] unused seats)
- [ ] Single user dependency ([Name] is only active power user)

Green Lights:
- [ ] Expanding usage ([% increase] over [timeframe])
- [ ] Cross-team adoption ([# departments] using product)
- [ ] Advanced feature usage ([Feature] actively used)

Recommended Actions:
1. [Specific action to improve adoption]
   - Owner: [CSM/Customer/Joint]
   - Timeline: [Days/weeks]
   - Success Metric: [How to measure improvement]

**2. BUSINESS VALUE REALIZATION**

Value Score: [0-100]

Stated Goals from Kickoff:
1. [Original goal] - Status: [Achieved/In Progress/Not Started/At Risk]
   - Target: [Specific metric]
   - Current: [Actual metric]
   - Gap: [Difference]

2. [Another goal]
[Same format]

Quantified Outcomes:
- ROI Delivered: [Calculate based on time saved, revenue increased, costs reduced]
- Payback Period: [Months] (Target was [X] months)
- Business Impact: [Specific measurable outcome]

Customer Can Articulate Value: [Yes/No/Unclear]
- Evidence: [Quote from recent conversation / Lack of clear answer]

Expansion Indicators:
- [ ] Achieving original goals (creates case for more)
- [ ] Expressed new use cases (signal of additional needs)
- [ ] Other teams inquiring about product (organic spread)
- [ ] Customer references value in exec meetings (champion strength)

Value Realization Risks:
- [ ] Goals not defined/measured (no proof of value)
- [ ] Results below expectations (not seeing ROI)
- [ ] Value not communicated to leadership (no exec visibility)

Recommended Actions:
1. [Specific action to demonstrate/increase value]
   - Owner: [Who]
   - Timeline: [When]
   - Success Metric: [How measured]

**3. ENGAGEMENT & RELATIONSHIP**

Engagement Score: [0-100]

Stakeholder Map:

| Name | Role | Influence | Champion? | Engagement Level | Last Contact | Sentiment |
|------|------|-----------|-----------|-----------------|--------------|-----------|
| [Name] | [Title] | [High/Med/Low] | [Yes/No] | [Active/Moderate/Low] | [Date] | [😊/😐/😟] |

Relationship Health:
- Executive Sponsor: [Identified/Engaged/Strong] or [Missing/Weak]
- Day-to-Day Champion: [Name] - Strength: [Strong/Moderate/Weak]
- Power User Community: [# of advocates] users who love the product
- Detractors: [# or names] users with negative sentiment

Communication Patterns:
- Initiated by Customer: [X] times in [timeframe]
- Initiated by Us: [X] times in [timeframe]
- Ratio: [Customer:Us] - Ideal is [X:Y]
- Response Time: [Avg hours for customer to reply]
- Meeting Attendance: [% of scheduled calls they attend]

Red Flags:
- [ ] Champion left company or changed roles
- [ ] Executive sponsor unresponsive
- [ ] Customer only contacts us with problems (reactive only)
- [ ] Meeting cancellations ([#] in past [timeframe])
- [ ] Slow/no responses to outreach

Green Lights:
- [ ] Multiple champions across departments
- [ ] Proactive feature requests (engaged in roadmap)
- [ ] Willing to be a reference
- [ ] Invite us to strategy meetings

Recommended Actions:
1. [Specific action to strengthen relationships]
   - Owner: [CSM or escalate to whom]
   - Timeline: [When]
   - Success Metric: [Evidence of improvement]

**4. SUPPORT & TECHNICAL HEALTH**

Support Score: [0-100]

Ticket Metrics:
- Total Tickets (past 90 days): [#]
- Avg per Month: [#]
- Trend: [Increasing/Stable/Decreasing]
- Severity Distribution: [# Critical, # High, # Medium, # Low]

Time to Resolution:
- Avg: [Hours/days]
- Compared to SLA: [Within/Exceeding]
- Customer Satisfaction: [% positive]

Issue Patterns:
- Recurring Issue: [Issue type] - [# occurrences]
  - Impact: [What this affects]
  - Root Cause: [Technical/Training/Product gap]
  - Resolution: [What needs to happen]

Red Flags:
- [ ] Escalated tickets ([#] in past [timeframe])
- [ ] Same issue repeating (not resolved at root cause)
- [ ] Critical issues ([#] severity 1-2 tickets)
- [ ] Customer frustration in tickets (tone/language indicates dissatisfaction)

Green Lights:
- [ ] Decreasing ticket volume (getting more self-sufficient)
- [ ] Only low-severity tickets (no major blockers)
- [ ] High CSAT on resolutions

Recommended Actions:
1. [Specific action to improve support experience]
   - Owner: [Support/CSM/Product]
   - Timeline: [When]
   - Success Metric: [Fewer tickets/Faster resolution/Higher CSAT]

**5. FINANCIAL & CONTRACT HEALTH**

Financial Score: [0-100]

Contract Details:
- ARR: [$X]
- Contract Term: [Length]
- Renewal Date: [Date] - Days Left: [#]
- Auto-renewal: [Yes/No]
- Notice Period: [Days before renewal]

Payment History:
- On-time Payments: [X] of [Y] = [%]
- Late Payments: [List any with dates]
- Billing Issues: [Any disputes/credits]

Pricing & Value Alignment:
- Current Price per User: [$X]
- Market Rate: [$Y]
- Discounts Applied: [%]
- Value Perception: [Expensive/Fair/Bargain based on customer feedback]

Expansion Potential:
- Unused Features: [Features they don't use but could benefit from]
- Additional Users: [Potential to add X more users based on Y]
- Upsell Products: [Other products relevant to their needs]
- Cross-sell Opportunities: [Related products they don't have]

Contraction Risk:
- [ ] Requesting to reduce seats
- [ ] Talking about budget cuts
- [ ] Comparing to cheaper alternatives
- [ ] Usage declining (don't need as much)

Red Flags:
- [ ] Price increase at renewal (may cause sticker shock)
- [ ] Customer mentioned budget review
- [ ] Late payment(s)
- [ ] Procurement investigating alternatives

Green Lights:
- [ ] Expressed interest in additional features
- [ ] Asked about adding users
- [ ] Company raised funding/growing
- [ ] Expanded to new teams organically

Recommended Actions:
1. [Specific action related to renewal/expansion]
   - Owner: [CSM/Sales/Finance]
   - Timeline: [When]
   - Success Metric: [Renewed/Expanded by $X]

### CHURN RISK ASSESSMENT

**Churn Probability: [%] - [Low/Medium/High/Critical]**

Risk Factors Present:

| Risk Factor | Severity | Evidence | Weight | Mitigation |
|-------------|----------|----------|--------|------------|
| [Factor] | [H/M/L] | [Specific data point] | [Points] | [What to do] |

Total Risk Score: [Sum of weighted factors]

Historical Churn Patterns:
[If data available, note similar accounts that churned]
- Account Profile: [Similar characteristics]
- Churn Reason: [Why they left]
- Early Warning Signs: [What we should have caught]
- Lessons Applied: [How this informs current account]

**If High/Critical Risk:**

Churn Save Plan:

Immediate Actions (This Week):
1. [Action] - Owner: [Who] - Completion: [When]
2. [Action] - Owner: [Who] - Completion: [When]

Executive Escalation:
- Escalate to: [Your exec / Their exec]
- Meeting Needed: [Yes/No] - If yes, attendees: [Who]
- Agenda: [What to discuss]

Value Reinforcement:
- Proof Points to Share: [Specific outcomes they've achieved]
- ROI Calculation: [Updated business case]
- Roadmap Preview: [Upcoming features that address their needs]

### EXPANSION OPPORTUNITY ANALYSIS

**Expansion Potential: [$X] - [Low/Medium/High]**

Expansion Pathways:

**1. Add Users**
- Current: [X] users
- Potential: [Y] additional users based on [Evidence]
- ARR Impact: [$Z]
- Timing: [Quarter to target]
- Pitch: [Why they should add users now]

**2. Upgrade Tier/Add Features**
- Current Plan: [Tier]
- Recommended: [Higher tier or add-on features]
- Additional Value: [What they get]
- ARR Impact: [$Z]
- Timing: [Quarter to target]
- Pitch: [Tie to goals they have]

**3. Cross-Sell Related Product**
- Current Products: [List]
- Recommended: [Product]
- Use Case: [How it helps them]
- ARR Impact: [$Z]
- Timing: [Quarter to target]
- Pitch: [Tie to current challenges]

Total Expansion Opportunity: [$X]

Expansion Readiness:
- [ ] High product satisfaction
- [ ] Achieving business goals
- [ ] Budget availability indicated
- [ ] Champion can advocate internally
- [ ] Executive sponsor supportive

Expansion Blockers:
- [ ] [Specific blocker] - Mitigation: [How to address]

### ACTION PLAN

**Prioritized Actions for Next 30 Days:**

**Priority 1: Critical (Do immediately)**
1. [Action]
   - Why Critical: [Risk or opportunity]
   - Owner: [Name]
   - Deadline: [Date]
   - Success Criteria: [How we know it worked]

**Priority 2: Important (Do this month)**
[Same format for 3-5 actions]

**Priority 3: Beneficial (Do if time allows)**
[Same format for 2-3 actions]

### SUCCESS PLAN UPDATE

**Quarterly Success Plan:**

This Quarter Goals:
1. [Goal] - Status: [On Track/At Risk/Off Track]
   - Owner: [Customer stakeholder]
   - Our Support: [What CSM is doing]
   - Next Milestone: [What's next] by [When]

2. [Goal]
[Same format]

Next Quarter Preview:
- Recommended Focus: [What to prioritize next]
- New Capabilities to Introduce: [Features launching]
- Business Review: [Schedule EBR if needed]

### COMMUNICATION PLAN

**Internal Communication:**

Notify:
- [ ] Account Executive (if sales implications)
- [ ] Support Team (if technical issues)
- [ ] Product Team (if feature requests/bugs)
- [ ] Leadership (if at-risk or big expansion opportunity)

Message: [Summary of account status and asks]

**Customer Communication:**

Next Touchpoint: [Date] - [Type: Check-in/Business Review/Training]

Agenda:
- Review: [What to discuss]
- Introduce: [New feature/team member]
- Plan: [Next steps/goals]

Pre-work Needed:
- [ ] [Prep item] by [Date]
- [ ] [Prep item] by [Date]

### EXECUTIVE BUSINESS REVIEW PREP

**EBR Status:** [Scheduled for [Date] / Need to schedule / Not yet appropriate]

If EBR Needed:

Recommended Timing: [When and why]
Attendees: [Their execs + our execs]
Agenda:
1. Value delivered (outcomes achieved)
2. Usage trends and insights
3. Strategic roadmap alignment
4. Success plan for next quarter
5. Partnership opportunities

Materials to Prepare:
- [ ] ROI calculations
- [ ] Usage analytics
- [ ] Success stories from their teams
- [ ] Roadmap preview
- [ ] Expansion proposal (if appropriate)

### BENCHMARKING

**How This Account Compares:**

| Metric | This Account | Peer Average | Top Quartile | Status |
|--------|-------------|--------------|--------------|--------|
| Adoption % | [%] | [%] | [%] | [Above/At/Below] |
| User Activity | [Score] | [Score] | [Score] | [Above/At/Below] |
| NPS | [Score] | [Score] | [Score] | [Above/At/Below] |
| Support Tickets | [#/month] | [#/month] | [#/month] | [Lower/Same/Higher] |
| Expansion % | [%] | [%] | [%] | [Above/At/Below] |

Insights:
- Where We're Strong: [What's working well comparatively]
- Where We're Weak: [What needs attention]
- Realistic Target: [Which benchmark to aim for and when]

### TRACKING & FOLLOW-UP

**Check-in Schedule:**

| Date | Type | Purpose | Completed | Notes |
|------|------|---------|-----------|-------|
| [Date] | [Call/Email/Review] | [What to cover] | [ ] | |

**Health Score Tracking:**

| Date | Score | Change | Key Events |
|------|-------|--------|------------|
| [Date] | [Score] | [+/-] | [What happened this period] |

Set Alert:
- If health score drops below [X] → [Trigger escalation process]
- If no customer engagement for [X days] → [Proactive outreach]

### RENEWAL STRATEGY

**Days Until Renewal: [#]**

Renewal Confidence: [%]

Renewal Timeline:

| Timeframe | Action | Owner | Status |
|-----------|--------|-------|--------|
| 90 days before | Begin renewal conversation | CSM | [ ] |
| 60 days before | Present ROI and expansion opportunity | CSM + AE | [ ] |
| 45 days before | Contract review and negotiations | AE | [ ] |
| 30 days before | Final approvals | Customer + Us | [ ] |
| 14 days before | Contract signed | Legal + Procurement | [ ] |

Renewal Playbook:
- [ ] Build business case (ROI calculations)
- [ ] Identify decision makers
- [ ] Address objections proactively
- [ ] Present expansion opportunity
- [ ] Lock in renewal before renewal date

### CONTINGENCY PLANNING

**If Things Go Wrong:**

Scenario 1: Customer raises pricing concern
- Response: [Specific talking points and value reinforcement]
- Escalation: [When to involve sales leadership]

Scenario 2: Champion leaves company
- Response: [How to quickly build new relationships]
- Escalation: [When to get executive sponsor involved]

Scenario 3: Usage drops significantly
- Response: [Intervention strategy]
- Escalation: [When to create formal save plan]

**If Things Go Right:**

Scenario 1: Strong renewal + expansion
- Capture: [Case study/reference/testimonial]
- Leverage: [For more expansions or references]

Scenario 2: Customer becomes advocate
- Activate: [Speaking opportunity/review/reference]
- Reward: [Recognition or benefits]

```

---

### Customer Success #2: Onboarding Plan & 90-Day Success Roadmap

```
You are a customer success manager designing a structured onboarding program for new customer success.

### TASK
Create a comprehensive 90-day onboarding plan that drives rapid time-to-value and strong product adoption.

### CUSTOMER PROFILE
"""
[CSM PASTES: Contract details, stated goals from sales, implementation notes,
team structure, technical environment, timeline expectations, any special requirements]
"""

### ONBOARDING CONTEXT
Company: [Name]
Industry: [Vertical]
Size: [Employees]
Product/Tier: [What they bought]
Implementation Complexity: [Low/Medium/High]
Start Date: [Date]
Success Criteria: [What defines successful onboarding]
CSM Assigned: [Name]

### REQUIRED OUTPUT FORMAT

**ONBOARDING OBJECTIVES**

Primary Goal: [Single most important outcome for 90 days]

Success Metrics:
1. [Metric] - Target: [Number] by Day [X]
2. [Metric] - Target: [Number] by Day [Y]
3. [Metric] - Target: [Number] by Day [Z]

Customer's Stated Goals:
1. [Goal from sales handoff]
   - Why It Matters: [Business impact]
   - How Product Helps: [Specific capabilities]
   - Success Measure: [How we'll know they achieved it]

2. [Another goal]
[Same format]

### PHASE-BY-PHASE PLAN

**WEEK 1: KICKOFF & FOUNDATION**

Day 1: Welcome & Kickoff Call

Agenda:
- Introductions (15 min)
  - Meet the CSM team
  - Meet customer project team
  - Establish communication norms
- Product Overview (20 min)
  - High-level tour focused on their use case
  - Key features for their goals
  - Success stories from similar customers
- Implementation Plan Review (15 min)
  - Timeline expectations
  - Customer responsibilities
  - Our responsibilities
  - Success criteria
- Q&A and Next Steps (10 min)

Pre-work Sent to Customer:
- [ ] Welcome email with kickoff details
- [ ] Onboarding checklist for their team
- [ ] Pre-kickoff questionnaire (if not completed in sales)

Deliverables:
- Recorded kickoff call
- Onboarding project plan shared
- Slack/Teams channel established (if applicable)

Day 2-3: Technical Setup

Activities:
- [ ] Account provisioned
- [ ] User accounts created
- [ ] Integrations configured
- [ ] SSO setup (if applicable)
- [ ] Permissions/roles assigned

Customer Actions Required:
- [ ] Provide user list
- [ ] Grant integration access
- [ ] Test login

Our Actions:
- [ ] Configuration completed
- [ ] Testing performed
- [ ] Documentation shared

Success Check:
- All users can log in successfully
- Core integrations connected and syncing

Day 4-5: Initial Training

Session 1: Admin Training (60 min)
- Audience: Customer admins/project lead
- Content:
  - Account settings and configuration
  - User management
  - Reporting and analytics basics
  - Best practices for rollout
- Hands-on: [Specific exercises]

Materials Provided:
- [ ] Admin guide
- [ ] Video recordings
- [ ] Quick reference cards

Success Check:
- Admin can add users independently
- Admin understands where to find key settings

Week 1 Milestone:
- [ ] Technical setup complete
- [ ] Admin trained
- [ ] Initial users activated
- [ ] First "win" achieved (one successful use of product)

### WEEK 2-3: CORE ADOPTION

Week 2 Focus: Primary Use Case

Training Session 2: End User Training (45 min)
- Audience: All initial users
- Content:
  - Core workflow for [primary use case]
  - Step-by-step tutorial
  - Common questions/mistakes
- Format: [Live/Recorded] with hands-on practice

Office Hours:
- Schedule: [Day/Time] each week
- Purpose: Answer questions, troubleshoot, provide tips
- Format: Open drop-in call

User Enablement:
- [ ] Send how-to videos daily (micro-learning approach)
- [ ] Create FAQ based on early questions
- [ ] Assign practice tasks with incentive

Success Metrics by End of Week 2:
- [X%] of users have logged in
- [Y] actions completed per user
- [Z] workflows successfully executed

Week 3 Focus: Expanding Usage

Training Session 3: Advanced Features (45 min)
- Audience: Power users/admins
- Content:
  - Advanced capabilities beyond basics
  - Automation opportunities
  - Reporting and insights
- Goal: Create internal champions

Champion Development:
- Identify 2-3 power users to become internal advocates
- Provide advanced training
- Empower them to help their peers

Customer Actions:
- [ ] Complete [specific task/workflow] at least once
- [ ] Invite additional users if needed
- [ ] Provide feedback on initial experience

Success Metrics by End of Week 3:
- [X%] of users active weekly
- [Y%] completion rate on core workflows
- Champions identified and engaged

### WEEK 4-6: DEPTH & EXPANSION

Month 1 Business Review (Week 4)

30-Day Check-In Call (45 min)

Agenda:
- Review progress against goals (15 min)
  - Adoption metrics
  - Usage patterns
  - Early wins
- Identify challenges (10 min)
  - What's not working
  - Barriers to adoption
  - Support issues
- Plan next 30 days (15 min)
  - Advanced features to introduce
  - Additional use cases
  - Training needs
- Q&A (5 min)

Materials to Prepare:
- [ ] Usage dashboard
- [ ] Adoption report (vs. benchmarks)
- [ ] Success stories from their early use
- [ ] Recommendations for improvement

Week 5-6 Focus: Second Use Case

Training Session 4: Use Case #2 (45 min)
- Build on primary use case
- Show how to extend value
- Include real examples from their data/workflows

Hands-On Support:
- Schedule 1:1 sessions with users who need extra help
- Create custom workflows for their specific needs
- Document tribal knowledge

Cross-Team Expansion:
- Identify adjacent teams who could benefit
- Facilitate intros to new stakeholders
- Provide business case for expansion

Success Metrics by End of Week 6:
- [X%] of users using 2+ features
- [Y%] week-over-week activity increase
- [Z] new teams/users onboarded

### WEEK 7-9: VALUE REALIZATION

Month 2 Business Review (Week 8)

60-Day Check-In Call (60 min)

Agenda:
- Quantify value delivered (20 min)
  - ROI calculations
  - Time saved
  - Outcomes achieved
- Deep dive on adoption (15 min)
  - Feature utilization
  - User engagement patterns
  - Benchmarking vs. similar customers
- Roadmap preview (15 min)
  - Upcoming features relevant to them
  - How to prepare
- Plan for next 30 days (10 min)

Value Calculation:

[Specific to their use case]

Goal: [Original goal]
- Baseline: [Where they started]
- Current State: [Where they are now]
- Improvement: [Quantified]
- Estimated Value: [$X saved or $Y gained]

Example Template:
- Time Saved: [X hours/week] × [Y weeks] × [$Z hourly rate] = [$Total]
- OR Revenue Impact: [Metric] improved by [%] = [$Estimated revenue impact]

Week 7-9 Activities:

- [ ] Case study development (if appropriate)
- [ ] Executive briefing (if needed to showcase value to leadership)
- [ ] Optimization review (fine-tuning configurations)
- [ ] Advanced automation setup

Success Metrics by End of Week 9:
- [X%] of target goals achieved
- [Y] measurable business outcome
- [Z%] user satisfaction score

### WEEK 10-12: OPTIMIZATION & TRANSITION TO BAU

Month 3 Business Review (Week 12)

90-Day Success Review (60 min)

Agenda:
- Celebrate wins (10 min)
  - Goals achieved
  - Adoption milestones
  - Value delivered
- Full product utilization review (20 min)
  - What's working well
  - Underutilized features
  - Optimization opportunities
- Roadmap for next quarter (20 min)
  - New goals
  - Advanced capabilities to explore
  - Expansion possibilities
- Transition to steady-state support (10 min)
  - Ongoing CSM cadence
  - Resources available
  - How to get help

Onboarding Success Scorecard:

| Success Criteria | Target | Actual | Status |
|-----------------|--------|--------|--------|
| User Adoption Rate | [%] | [%] | [✅/⚠️/❌] |
| Feature Utilization | [%] | [%] | [✅/⚠️/❌] |
| Business Goal Achievement | [Goal] | [Result] | [✅/⚠️/❌] |
| User Satisfaction (NPS/CSAT) | [Score] | [Score] | [✅/⚠️/❌] |
| Support Ticket Volume | [Max #] | [Actual #] | [✅/⚠️/❌] |
| Time to First Value | [Days] | [Days] | [✅/⚠️/❌] |

Overall Onboarding Grade: [A/B/C/D/F]

Week 10-12 Activities:

- [ ] Identify optimization opportunities
- [ ] Document custom configurations/workflows
- [ ] Create internal customer playbook
- [ ] Schedule ongoing cadence calls
- [ ] Introduce customers to peer community/resources

Transition to Business-as-Usual:

Ongoing Cadence:
- Monthly check-in calls: [Day/Time]
- Quarterly business reviews: [Schedule next one]
- Office hours: [Frequency and day/time]
- Support: [How to contact for issues]

Customer Self-Service:
- [ ] Knowledge base access
- [ ] Community forum access
- [ ] Best practice guides
- [ ] Video tutorial library

Success Metrics for Ongoing:
- Monthly Active Users: Target [%]
- Feature Adoption: Target [%]
- CSAT: Target [Score]
- Expansion Opportunity: [$X potential]

### ONBOARDING RESOURCE LIBRARY

**Training Materials:**

- [ ] Welcome Guide (PDF)
- [ ] Quick Start Checklist (PDF)
- [ ] Admin Guide (PDF/Video)
- [ ] End User Guide (PDF/Video)
- [ ] Use Case Playbooks (specific to their industry/role)
- [ ] Video Tutorial Library (organized by topic)
- [ ] FAQ Document (updated based on their questions)

**Communication Templates:**

Email #1: Welcome (Day 0)
- Subject: Welcome to [Product]! Here's What to Expect
- Content: [Key points]

Email #2: Pre-Kickoff (Day 0)
- Subject: Your Kickoff Call on [Date] - Please Prepare
- Content: [Agenda and pre-work]

Email #3: Post-Kickoff (Day 1)
- Subject: [Company] Kickoff Recap + Next Steps
- Content: [Summary and action items]

Email #4: Week 1 Recap (Day 5)
- Subject: Your First Week with [Product] - How'd It Go?
- Content: [Milestone check and encouragement]

[Continue with templates for key milestones]

**Recorded Calls:**

- [ ] Kickoff Call Recording
- [ ] Admin Training Recording
- [ ] End User Training Recording
- [ ] Advanced Features Recording
- [ ] 30-Day Business Review Recording

**Tools & Assets:**

- [ ] Onboarding Project Plan (shared doc)
- [ ] Adoption Dashboard (live link)
- [ ] ROI Calculator (template)
- [ ] Success Plan Template (for customer to fill out)

### STAKEHOLDER ENGAGEMENT PLAN

**Key Contacts:**

| Name | Role | Engagement Frequency | Communication Method | Primary Focus |
|------|------|---------------------|---------------------|---------------|
| [Name] | [Title - Executive Sponsor] | Monthly | Email + Quarterly EBR | Business value, ROI |
| [Name] | [Title - Project Lead] | Weekly | Calls + Slack | Day-to-day progress, issues |
| [Name] | [Title - Admin] | As needed | Email + Office Hours | Technical setup, user management |
| [Name] | [Title - Power User] | Weekly initially | Calls + Training | Champion development |

**Communication Cadence:**

Weekly (Weeks 1-4):
- Quick check-in call/email with project lead
- Purpose: Address blockers, answer questions, maintain momentum

Bi-weekly (Weeks 5-12):
- Progress update call
- Purpose: Review metrics, plan next steps

Monthly:
- Business review meeting
- Purpose: Showcase value, align on goals, plan future

As-Needed:
- Office hours
- Support tickets
- Slack/email for questions

### RISK MITIGATION

**Common Onboarding Risks:**

| Risk | Probability | Mitigation Strategy |
|------|-------------|-------------------|
| Low user engagement | Medium | Gamification, incentives, executive messaging |
| Technical integration issues | Medium | Pre-launch testing, dedicated tech support |
| Champion leaves/changes roles | Low | Identify multiple champions early |
| Scope creep (trying to do too much) | High | Clear phase plan, say "yes, in phase 2" to extras |
| Competing priorities (customer too busy) | High | Create sense of urgency, show quick wins |
| Poor change management | Medium | Executive sponsorship, communication plan |

**Early Warning Signs:**

- [ ] Low training attendance
- [ ] Project lead unresponsive
- [ ] No usage after Week 1
- [ ] Negative feedback in early calls
- [ ] Technical issues unresolved after 3+ days

If Any Warning Signs Appear:
1. Escalate to CSM manager
2. Schedule emergency call with customer stakeholder
3. Develop get-well plan
4. Increase touchpoint frequency

### SUCCESS CRITERIA BY PHASE

**End of Week 1:**
- [ ] All users can access product
- [ ] Admin trained and confident
- [ ] Initial "win" logged (someone successfully used product)

**End of Week 4:**
- [ ] [X%] of users active weekly
- [ ] Primary use case adopted
- [ ] Positive feedback from users

**End of Week 8:**
- [ ] [Y%] of users active weekly
- [ ] Multiple features in use
- [ ] Measurable business outcome
- [ ] Champions identified

**End of Week 12:**
- [ ] All onboarding success criteria met
- [ ] Customer can articulate ROI
- [ ] Expansion opportunity identified
- [ ] High customer satisfaction (NPS/CSAT)

### POST-ONBOARDING TRANSITION

**Handoff to Steady-State:**

CSM Responsibilities Going Forward:
- Monthly check-ins
- Quarterly business reviews
- Renewal management
- Expansion/upsell identification
- Executive relationship management

Customer Self-Sufficiency:
- Can solve common issues independently
- Knows how to access support
- Understands product roadmap
- Active in customer community (if applicable)

**Continuous Improvement:**

Onboarding Feedback:
- Survey customer at end of 90 days
- Questions:
  - What worked well?
  - What was confusing?
  - What would you have wanted more/less of?
  - How likely to recommend product? (NPS)

Internal Retrospective:
- What went smoothly?
- What challenges did we face?
- How can we improve next onboarding?
- Update playbook with learnings

### ONBOARDING METRICS DASHBOARD

**Track These Weekly:**

| Week | Active Users | Actions Completed | Features Used | Support Tickets | CSAT | Health Score |
|------|-------------|------------------|--------------|-----------------|------|--------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| ... | | | | | | |

**Benchmark Comparison:**

| Metric | This Customer | Avg for Segment | Top Quartile | Status |
|--------|--------------|----------------|--------------|--------|
| Time to First Login | [Days] | [Days] | [Days] | [✅/⚠️/❌] |
| Time to First Value | [Days] | [Days] | [Days] | [✅/⚠️/❌] |
| 30-Day Adoption % | [%] | [%] | [%] | [✅/⚠️/❌] |
| 90-Day Adoption % | [%] | [%] | [%] | [✅/⚠️/❌] |

### EXPANSION PLANNING

**Identify Expansion Early:**

During onboarding, watch for:
- [ ] Additional teams asking about product
- [ ] Use cases beyond original scope
- [ ] Customer asking "Can it also do X?"
- [ ] More users needed than originally purchased
- [ ] Interest in premium features

Document Expansion Opportunities:

Opportunity: [Specific expansion]
- Potential ARR: [$X]
- Timing: [When to present]
- Stakeholder: [Who to approach]
- Business Case: [Why they need it]

Seed the Expansion:
- Show advanced features during training
- Share success stories of customers who expanded
- Mention roadmap items relevant to other teams
- Facilitate intros to adjacent departments

### CUSTOMER SUCCESS PLAN (LIVING DOCUMENT)

**Shared with Customer:**

Goals for This Quarter:
1. [Goal] - Owner: [Customer person] - Due: [Date]
2. [Goal] - Owner: [Customer person] - Due: [Date]
3. [Goal] - Owner: [Customer person] - Due: [Date]

How We're Helping:
- [Our action] to support [their goal]
- [Our action] to support [their goal]

Risks/Blockers:
- [Issue if any]

Next Review: [Date]

**Internal CSM Notes:**

Insights:
- [What we learned about their business]
- [Key relationships and dynamics]
- [What motivates this customer]

Account Strategy:
- Renewal approach: [Strategy]
- Expansion play: [Strategy]
- Reference potential: [Yes/No/Maybe]

### CELEBRATION & RECOGNITION

**Milestones to Celebrate:**

- [ ] First successful workflow completed
- [ ] 10 active users
- [ ] 50% adoption reached
- [ ] First business goal achieved
- [ ] 90 days onboarding complete

How to Celebrate:
- Send congratulations email with specific callout
- Share success internally (with customer permission)
- Send small gift/swag
- Feature them in customer newsletter
- Request testimonial/case study

**Onboarding Success Triggers Reference Request:**

If customer achieves:
- [X%] adoption
- [Y] business outcome
- High NPS score
- Positive feedback

Then:
- Ask for testimonial
- Request to be a reference
- Invite to speak at event/webinar
- Create case study

This completes the 90-day onboarding plan. The customer is now transitioned to regular CSM cadence with a strong foundation for ongoing success.

```

---

## OPERATIONS/FINANCE (1 Prompt)

### Operations/Finance: Budget Variance Analysis & Corrective Action Plan

```
You are a financial analyst conducting budget variance analysis to understand performance and recommend corrective actions.

### TASK
Analyze the budget variance data below and provide insights with actionable recommendations.

### BUDGET DATA
"""
[ANALYST PASTES: Actual vs. budgeted spend by category, revenue vs. forecast,
departmental budgets, monthly actuals, year-to-date figures, drivers of variances]
"""

### CONTEXT
Company: [Name]
Period: [Month/Quarter/Year]
Fiscal Year End: [Date]
Department/Division: [If specific scope]
Industry: [For context on seasonality/norms]
Current Month: [Which month of fiscal year]

### REQUIRED OUTPUT FORMAT

**EXECUTIVE SUMMARY**

Overall Variance: [$ amount] or [%] [Favorable/Unfavorable]

Quick Assessment:
- Revenue vs. Plan: [% variance]
- Expenses vs. Budget: [% variance]
- Net Income vs. Budget: [% variance]
- Cash Position: [Better/Worse than planned]

Headline Findings:
1. [Most significant positive variance - what went better than expected]
2. [Most significant negative variance - what underperformed]
3. [Trend that requires attention]

Immediate Action Required: [Yes/No - If yes, what specifically]

### REVENUE ANALYSIS

**Revenue Performance:**

| Revenue Category | Budget | Actual | Variance $ | Variance % | Status |
|-----------------|--------|--------|-----------|-----------|--------|
| [Category 1] | [$] | [$] | [$] | [%] | [✅/⚠️/❌] |
| [Category 2] | [$] | [$] | [$] | [%] | [✅/⚠️/❌] |
| **Total Revenue** | **[$]** | **[$]** | **[$]** | **[%]** | |

Detailed Variance Explanations:

**[Revenue Category]** - Variance: [$X] or [Y%] [Favorable/Unfavorable]

Root Cause Analysis:
- Primary Driver: [What caused this variance - volume, price, mix, timing]
- Volume Impact: [$ variance attributable to volume difference]
- Price Impact: [$ variance attributable to pricing difference]
- Mix Impact: [$ variance attributable to product/customer mix]
- Other Factors: [One-time items, market conditions, etc.]

Supporting Data:
- Budget Assumption: [What was assumed in budget]
- Reality: [What actually happened]
- Gap: [Why assumption was wrong]

Is This Variance:
- [ ] Timing (will reverse in future periods)
- [ ] Trend (ongoing change to run rate)
- [ ] One-time (won't recur)

Forecast Impact:
- Adjust full-year forecast by: [$X] [up/down]
- Confidence Level: [High/Medium/Low]

[Repeat for each material revenue category]

**Revenue Trends:**

| Period | Budget | Actual | Variance % | YoY Growth |
|--------|--------|--------|-----------|------------|
| [Period 1] | [$] | [$] | [%] | [%] |
| [Period 2] | [$] | [$] | [%] | [%] |
| [Current Period] | [$] | [$] | [%] | [%] |

Trend Direction: [Improving/Stable/Deteriorating]
- Observation: [What the trend tells us]

### EXPENSE ANALYSIS

**Expense Performance:**

| Expense Category | Budget | Actual | Variance $ | Variance % | % of Revenue | Status |
|-----------------|--------|--------|-----------|-----------|-------------|--------|
| [Category 1] | [$] | [$] | [$] | [%] | [%] | [✅/⚠️/❌] |
| [Category 2] | [$] | [$] | [$] | [%] | [%] | [✅/⚠️/❌] |
| **Total Expenses** | **[$]** | **[$]** | **[$]** | **[%]** | | |

Detailed Variance Explanations:

**[Expense Category]** - Variance: [$X] or [Y%] [Over/Under Budget]

Root Cause Analysis:
- Primary Driver: [What caused overspend or underspend]
- Volume Driver: [Did we do more/less activity than planned?]
- Rate Driver: [Were costs higher/lower per unit than expected?]
- Scope Driver: [Did scope of work change?]
- Timing Driver: [Is this a timing difference?]

Example Breakdown:
If Payroll Expense Over Budget:
- Headcount Variance: [Planned X, Actual Y = Z difference × avg salary = $ impact]
- Compensation Variance: [Higher salaries, raises, bonuses = $ impact]
- Benefits Variance: [Higher benefits costs = $ impact]
- Overtime Variance: [Unplanned OT = $ impact]

Supporting Data:
- Budget Assumption: [What was planned]
- Reality: [What actually occurred]
- Gap: [Why different]

Is This Variance:
- [ ] Timing (will reverse)
- [ ] Trend (new run rate)
- [ ] One-time (non-recurring)

Controllable: [Yes/No/Partially]
- Explanation: [Why this variance was or wasn't controllable]

Forecast Impact:
- Adjust full-year forecast by: [$X] [up/down]

Corrective Action:
- Required: [Yes/No]
- Action: [Specific step to address]
- Owner: [Department/person]
- Timeline: [When to implement]

[Repeat for each material expense category]

### DEPARTMENTAL BUDGET REVIEW

For Each Department:

**[Department Name]**

Overall Performance: [On Budget / Over Budget / Under Budget] by [$X] or [Y%]

Budget: [$X]
Actual: [$Y]
Variance: [$Z] or [%]

Headcount:
- Budget: [FTE count]
- Actual: [FTE count]
- Variance: [+/- FTE]
- Payroll Impact: [$X]

Key Variances:
1. [Largest variance line item]
   - Amount: [$X]
   - Explanation: [Why]
   - Action: [What's being done]

2. [Second variance]
[Same format]

Department Manager Explanation:
[Quote or summarize if available]

Performance Against Deliverables:
- Delivered: [What was accomplished with the budget spent]
- Missed: [What wasn't delivered despite spending]
- ROI Assessment: [Was spend justified by outcomes?]

### CAPITAL EXPENDITURE ANALYSIS

**CapEx Performance:**

| Project/Category | Budget | Actual YTD | Remaining Budget | Forecast Total | Variance to Budget | Status |
|-----------------|--------|-----------|-----------------|----------------|-------------------|--------|
| [Project] | [$] | [$] | [$] | [$] | [$] | [On Track/Delayed/Accelerated] |

CapEx Variances:

**[Project Name]** - Budget: [$X] - Forecast: [$Y] - Variance: [$Z]

Variance Explanation:
- [ ] Scope change (explain what changed)
- [ ] Timing delay (explain why and new timeline)
- [ ] Cost overrun (explain cause: materials, labor, unexpected issues)
- [ ] Cost underrun (explain savings)

Impact on Operations:
- Expected Completion: [Original date] → [New date]
- Business Impact of Delay: [Revenue/cost impact if delayed]

Corrective Action:
- Action: [What's being done to get back on track]
- Owner: [Who's responsible]

### CASH FLOW ANALYSIS

**Cash Performance:**

Beginning Cash: [$X]

Cash Inflows:
- Collections: [$X] (Budget: [$Y], Variance: [$Z])
- Other: [$X]

Cash Outflows:
- Operating Expenses: [$X] (Budget: [$Y], Variance: [$Z])
- CapEx: [$X] (Budget: [$Y], Variance: [$Z])
- Debt Service: [$X] (Budget: [$Y], Variance: [$Z])

Ending Cash: [$X] (Budget: [$Y], Variance: [$Z])

Cash Runway: [# months at current burn rate]

Cash Concerns:
- [ ] Below minimum cash threshold
- [ ] Burn rate higher than budgeted
- [ ] Collection issues (AR aging)

Cash Opportunities:
- [ ] Excess cash (investment opportunities)
- [ ] Early payment discounts available
- [ ] Debt refinancing opportunity

### KEY PERFORMANCE INDICATORS

**Operational KPIs vs. Budget:**

| KPI | Budget | Actual | Variance % | Status |
|-----|--------|--------|-----------|--------|
| [KPI 1] | [Value] | [Value] | [%] | [✅/⚠️/❌] |
| [KPI 2] | [Value] | [Value] | [%] | [✅/⚠️/❌] |

For Each KPI:

**[KPI Name]**

Why This Matters: [Business impact of this metric]
Variance: [Actual vs. budget]
Explanation: [What drove the variance]
Correlation to Financials: [How this KPI impacts revenue/cost]

Example:
KPI: Customer Acquisition Cost (CAC)
- Budget: [$X]
- Actual: [$Y]
- Variance: [%] [Higher/Lower]
- Explanation: [Marketing spent $X but acquired Y customers instead of budgeted Z]
- Financial Impact: [This increased total acquisition cost by $X]

### PROFITABILITY ANALYSIS

**Margin Performance:**

| Metric | Budget | Actual | Variance | Status |
|--------|--------|--------|----------|--------|
| Gross Margin % | [%] | [%] | [bps] | [✅/⚠️/❌] |
| Operating Margin % | [%] | [%] | [bps] | [✅/⚠️/❌] |
| Net Margin % | [%] | [%] | [bps] | [✅/⚠️/❌] |
| EBITDA % | [%] | [%] | [bps] | [✅/⚠️/❌] |

Margin Variance Analysis:

**Gross Margin:** [Actual %] vs. Budget [%] = [X bps] [Better/Worse]

Drivers:
- Revenue Mix: [Higher/lower margin products/services mix impact = X bps]
- Pricing: [Actual prices vs. budget impact = X bps]
- COGS: [Actual costs vs. budget impact = X bps]
- Volume: [Leverage impact = X bps]

[Repeat for Operating Margin and Net Margin]

### YEAR-TO-DATE PERFORMANCE

**YTD Summary:**

| Metric | YTD Budget | YTD Actual | Variance $ | Variance % | Full Year Budget | Forecast | Variance to Budget |
|--------|-----------|-----------|-----------|-----------|----------------|---------|-------------------|
| Revenue | [$] | [$] | [$] | [%] | [$] | [$] | [$] |
| Expenses | [$] | [$] | [$] | [%] | [$] | [$] | [$] |
| Net Income | [$] | [$] | [$] | [%] | [$] | [$] | [$] |

YTD Insights:
- Trend Direction: [What YTD performance tells us about full year]
- Risk Assessment: [Likelihood of hitting full-year budget]
- Confidence Level: [High/Medium/Low] in achieving full-year plan

### FORECAST UPDATE

**Revised Full-Year Forecast:**

Based on YTD actuals and remaining year outlook:

| Line Item | Original Budget | Updated Forecast | Variance | Change Driver |
|-----------|----------------|-----------------|----------|---------------|
| Revenue | [$] | [$] | [$] | [What changed] |
| Expenses | [$] | [$] | [$] | [What changed] |
| Net Income | [$] | [$] | [$] | |

Forecast Assumptions:
- [Key assumption 1 and basis]
- [Key assumption 2 and basis]
- [Key assumption 3 and basis]

Forecast Risks:
- Upside Potential: [What could go better than forecast]
- Downside Risk: [What could go worse than forecast]
- Most Likely Scenario: [What we believe will happen]

### CORRECTIVE ACTION PLAN

**Required Actions by Priority:**

**Priority 1: Critical (Immediate Action - This Week)**

Action 1: [Specific action]
- Problem: [What variance/issue this addresses]
- Owner: [Department/person]
- Deadline: [Date]
- Financial Impact: [$X expected improvement]
- Success Metric: [How we'll know it worked]
- Status: [Not Started/In Progress/Complete]

[Repeat for 2-4 critical actions]

**Priority 2: Important (This Month)**

[Same format for 3-5 important actions]

**Priority 3: Monitor (This Quarter)**

[Same format for 2-3 monitoring items]

### EXPENSE REDUCTION OPPORTUNITIES

**If Budget Cuts Needed:**

Identify Savings Opportunities:

| Department/Category | Current Run Rate | Proposed Reduction | Annual Impact | Feasibility | Business Impact |
|-------------------|-----------------|-------------------|---------------|------------|----------------|
| [Category] | [$X/month] | [$Y/month] | [$Z] | [Easy/Medium/Hard] | [Low/Med/High] |

Prioritization:
1. Easy + Low Impact = Do immediately
2. Easy + Medium Impact = Do with caution
3. Hard + High Impact = Last resort

Recommended Cuts:
- Cut 1: [Specific action] - Saves [$X] with [Low/Med/High] business impact
- Cut 2: [Specific action] - Saves [$Y] with [Low/Med/High] business impact

Do NOT Cut:
- [Expense that seems high but is critical] - Reason: [Why this is essential]

### REVENUE ACCELERATION OPPORTUNITIES

**If Revenue Below Plan:**

Actions to Close Gap:

Opportunity 1: [Specific initiative]
- Current State: [Where we are]
- Proposed Action: [What to do]
- Revenue Impact: [$X] additional revenue
- Investment Required: [$Y]
- ROI: [X:Y ratio]
- Timeline: [How long to see results]
- Probability of Success: [High/Medium/Low]

[Repeat for 3-5 opportunities]

Recommended Priorities:
1. [Opportunity] - Highest ROI, fastest impact
2. [Opportunity] - Secondary priority
3. [Opportunity] - Consider if #1-2 insufficient

### SCENARIO PLANNING

**Best Case Scenario:**

Assumptions:
- [Optimistic but possible assumption]
- [Optimistic but possible assumption]

Financial Outcome:
- Revenue: [$X] ([Y%] above budget)
- Net Income: [$Z] ([%] above budget)

Probability: [%]

**Most Likely Scenario:**

Assumptions:
- [Realistic assumption based on trends]
- [Realistic assumption based on trends]

Financial Outcome:
- Revenue: [$X] ([Y%] vs. budget)
- Net Income: [$Z] ([%] vs. budget)

Probability: [%]

**Worst Case Scenario:**

Assumptions:
- [Pessimistic but possible assumption]
- [Pessimistic but possible assumption]

Financial Outcome:
- Revenue: [$X] ([Y%] below budget)
- Net Income: [$Z] ([%] below budget)

Probability: [%]

Contingency Plan if Worst Case:
- Action 1: [Cost cut]
- Action 2: [Revenue initiative]
- Action 3: [Cash preservation]

### BUDGET PROCESS IMPROVEMENTS

**Lessons Learned:**

Where Budget Was Accurate:
- [Category] - Variance within [X%]
- Reason: [Why budgeting process worked here]

Where Budget Was Inaccurate:
- [Category] - Variance [Y%]
- Reason: [Why we missed]
- Improvement: [How to budget this better next time]

Recommendations for Next Budget Cycle:
1. [Process improvement]
2. [Data/assumption improvement]
3. [Communication improvement]

### STAKEHOLDER COMMUNICATION

**Key Messages by Audience:**

**To Executive Team:**
- Summary: [1-2 sentence overall status]
- Biggest Concern: [What keeps you up at night]
- Biggest Opportunity: [What's going better than expected]
- Ask: [Decision or support needed]

**To Department Leaders:**
- Your Department: [Status]
- What We Need from You: [Specific action]
- Support Available: [Resources to help]

**To Board (if applicable):**
- Financial Performance: [High-level summary]
- Forecast: [Updated outlook]
- Risks: [What could go wrong]
- Opportunities: [What could go right]
- Request: [Approval/guidance needed]

### TRACKING & FOLLOW-UP

**Variance Review Cadence:**

Weekly:
- [ ] Review cash position
- [ ] Check critical expense categories
- [ ] Monitor revenue pacing

Monthly:
- [ ] Full variance analysis (this report)
- [ ] Department reviews
- [ ] Forecast update

Quarterly:
- [ ] Strategic review with leadership
- [ ] Annual forecast revision
- [ ] Budget process retrospective

**Action Item Tracker:**

| Action | Owner | Due Date | Status | Completion Date | Impact |
|--------|-------|----------|--------|----------------|--------|
| [Action] | [Name] | [Date] | [Status] | | [$X] |

### APPROVAL & SIGN-OFF

Report Prepared By: [Name] - [Date]
Reviewed By: [Name] - [Date]
Approved By: [Name] - [Date]

Next Review: [Date]

Recommendations Status:
- [ ] Accepted as proposed
- [ ] Accepted with modifications: [Note changes]
- [ ] Rejected: [Note reason]
- [ ] Deferred: [Note why and when to revisit]

---

**APPENDIX: DETAILED BACKUP DATA**

[Include supporting schedules, detailed GL reports, department-level detail, etc.]

```

---

**Techniques Used:**
- **ST-01** (Clear Objective Statement) - Each prompt begins with clear role and task definition
- **ST-02** (Structured Sequential Instructions) - Prompts use numbered steps and structured sections
- **RT-02** (Multi-Dimensional Analysis Framework) - Employs multi-dimensional tables and analysis frameworks
- **DT-01** (Hierarchical Task Breakdown) - Breaks down complex workflows into manageable components
- **DT-02** (Specific Focus Areas with Examples) - Provides concrete examples and specific categories
- **DS-06** (Prioritization and Severity Guidance) - Includes priority levels and severity classifications
- **OC-01** (Output Format Templates) - Specifies exact output formats and templates for each workflow