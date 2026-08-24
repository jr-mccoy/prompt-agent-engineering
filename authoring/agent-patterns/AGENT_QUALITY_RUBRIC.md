# Agent Quality Rubric

**100-point quality assessment system for Claude Code agents.**

---

## Overview

This rubric provides objective criteria for evaluating agent quality across six dimensions. Use it to:

- **Validate new agents** before deployment
- **Improve existing agents** through systematic assessment
- **Maintain quality standards** across the agent library
- **Compare agents** objectively

**Target Score: 75/100** for production-ready agents

**Scoring Tiers:**
- **90-100**: Exceptional - Gold standard quality
- **75-89**: Excellent - Production-ready
- **60-74**: Good - Minor improvements needed
- **45-59**: Fair - Significant improvements required
- **Below 45**: Poor - Major rework needed

---

## Scoring Dimensions

| Dimension | Points | Weight | Focus |
|-----------|--------|--------|-------|
| [Model Appropriateness](#1-model-appropriateness-20-points) | 20 | 20% | Correct model tier selection |
| [Activation Clarity](#2-activation-clarity-20-points) | 20 | 20% | Clear triggering criteria |
| [Persona Consistency](#3-persona-consistency-20-points) | 20 | 20% | Coherent expert identity |
| [Tool Integration](#4-tool-integration-15-points) | 15 | 15% | Skills, agents, external tools |
| [Documentation Quality](#5-documentation-quality-15-points) | 15 | 15% | Comprehensive documentation |
| [Edge Cases & Safety](#6-edge-cases--safety-10-points) | 10 | 10% | Robustness and error handling |
| **Total** | **100** | **100%** | |

---

## 1. Model Appropriateness (20 points)

### Scoring Criteria

**20 points** - Perfect model tier selection
- Model tier perfectly matches task criticality
- Cost fully justified by value delivered
- Alternative tiers considered and documented
- Clear rationale for tier selection

**15 points** - Appropriate model tier
- Model tier matches task criticality
- Cost generally justified
- Reasonable choice with minor optimizations possible

**10 points** - Acceptable but suboptimal
- Model tier works but may not be optimal
- Some cost/performance trade-offs not ideal
- Better alternatives exist

**5 points** - Poor model selection
- Significant model tier mismatch
- Overpriced for value (e.g., Opus for simple tasks)
- Underpriced for criticality (e.g., Haiku for security)

**0 points** - Wrong model tier
- Completely inappropriate model selection
- Major cost inefficiency or capability mismatch

### Evaluation Questions

- [ ] Is the model tier appropriate for task criticality?
- [ ] Is the cost justified by the value delivered?
- [ ] Would a different tier be more appropriate?
- [ ] Are there clear cost optimization opportunities?

### Model Tier Guidelines

| Task Type | Correct Tier | Score | Wrong Tier | Score |
|-----------|--------------|-------|------------|-------|
| Security audit | Opus | 20 | Haiku | 0 |
| Architecture design | Opus | 20 | Sonnet/Haiku | 5-10 |
| Standard development | Sonnet | 20 | Opus (wasteful) | 10 |
| Debugging | Sonnet | 20 | Haiku | 10 |
| Diagram generation | Haiku | 20 | Opus (wasteful) | 5 |
| User preference | Inherit | 20 | Fixed tier | 10-15 |

### Examples

**20 points:** `security-auditor` using Opus for critical security work

**15 points:** `test-automator` using Sonnet for comprehensive testing

**10 points:** Agent using Opus for standard development (works but wasteful)

**5 points:** Agent using Haiku for security audits (insufficient capability)

**0 points:** Agent using Opus for simple JSON formatting

---

## 2. Activation Clarity (20 points)

### Scoring Criteria

**20 points** - Crystal clear activation
- Specific activation trigger in description ("Use PROACTIVELY for X")
- No ambiguity about when to invoke
- Use cases clearly defined
- Proactive vs passive explicitly stated

**15 points** - Clear activation
- Activation trigger present
- Generally clear when to invoke
- Minor ambiguities possible

**10 points** - Somewhat clear
- Basic activation information
- Some uncertainty about when to use
- Could be more specific

**5 points** - Vague activation
- Unclear activation criteria
- User must guess when to invoke
- Missing proactive/passive specification

**0 points** - No activation clarity
- No activation information
- Completely unclear when to use

### Evaluation Questions

- [ ] Is there a clear activation trigger in the description?
- [ ] Is it clear whether activation is proactive or passive?
- [ ] Are specific use cases documented?
- [ ] Would a user know when to invoke this agent?

### Activation Pattern Quality

| Pattern | Quality | Score Range |
|---------|---------|-------------|
| "Use PROACTIVELY for security audits, DevSecOps, or compliance" | Excellent | 18-20 |
| "Use PROACTIVELY when creating UI components" | Good | 15-17 |
| "Use when needed for Python" | Vague | 5-9 |
| No activation criteria | Poor | 0-4 |

### Examples

**20 points:**
```yaml
description: Expert security auditor... Use PROACTIVELY for security audits,
DevSecOps, or compliance implementation.
```

**15 points:**
```yaml
description: Expert debugger. Use PROACTIVELY when encountering errors or test failures.
```

**10 points:**
```yaml
description: Python expert. Use for Python development tasks.
```

**5 points:**
```yaml
description: Helps with code. Use when needed.
```

**0 points:**
```yaml
description: Expert developer.
```

---

## 3. Persona Consistency (20 points)

### Scoring Criteria

**20 points** - Excellent persona
- Clear expert identity throughout
- Domain expertise well-defined
- Consistent tone and formality
- Appropriate persona pattern (PP-01 to PP-10)
- Persona matches model tier

**15 points** - Good persona
- Clear identity
- Domain expertise defined
- Mostly consistent tone
- Minor inconsistencies

**10 points** - Acceptable persona
- Basic identity established
- Some persona elements missing
- Tone varies somewhat

**5 points** - Weak persona
- Vague identity
- Unclear expertise scope
- Inconsistent characterization

**0 points** - No persona
- Generic or missing persona
- No clear expert identity

### Evaluation Questions

- [ ] Is there a clear expert identity (role/specialization)?
- [ ] Is the domain expertise well-defined?
- [ ] Is the tone consistent throughout?
- [ ] Does the persona match the model tier?
- [ ] Is an appropriate persona pattern used?

### Persona Quality Examples

**20 points (Opus - PP-01 Expert Authority):**
```markdown
You are a security auditor specializing in DevSecOps, application security,
and comprehensive cybersecurity practices.

## Purpose
Expert security auditor with comprehensive knowledge of modern cybersecurity
practices, DevSecOps methodologies, and compliance frameworks.
```

**20 points (Haiku - PP-07 Creation Specialist):**
```markdown
You are a Mermaid diagram expert specializing in clear, professional visualizations.

## Focus Areas
- Flowcharts and decision trees
- Sequence diagrams for APIs
```

**10 points:**
```markdown
You are a developer who helps with code.
```

**5 points:**
```markdown
You help with tasks.
```

### Persona-Tier Alignment

| Tier | Expected Persona | Score Impact |
|------|------------------|--------------|
| Opus | PP-01 (Expert Authority) or PP-06 (Quality Guardian) | Aligned = 18-20, Mismatched = 5-10 |
| Sonnet | PP-02, PP-03, PP-05, PP-06 | Aligned = 15-20 |
| Haiku | PP-07 (Creation), PP-10 (Minimalist) | Aligned = 15-20 |
| Inherit | PP-03 (Tech Stack), PP-04 (Multi-Domain) | Aligned = 15-20 |

---

## 4. Tool Integration (15 points)

### Scoring Criteria

**15 points** - Excellent integration
- Related skills documented
- Related agents referenced
- External tools/APIs listed
- Integration patterns clear
- Composition strategies defined

**12 points** - Good integration
- Some integration documentation
- Key relationships captured
- External tools mentioned

**8 points** - Basic integration
- Minimal integration information
- Some tools or skills mentioned

**4 points** - Weak integration
- Little integration documentation
- Isolated agent

**0 points** - No integration
- No integration information
- Completely standalone

### Evaluation Questions

- [ ] Are related skills documented in frontmatter?
- [ ] Are related agents referenced?
- [ ] Are external tools/APIs listed in capabilities?
- [ ] Are integration patterns explained?

### Integration Pattern Quality

**Excellent (15 points):**
```yaml
---
name: security-auditor
Related skills: verification, definition
Related agents: backend-security-coder, frontend-security-coder
---

## Capabilities
### DevSecOps & Security Automation
- SAST, DAST, IAST integration in CI/CD
- Security as Code with OPA
- Container security scanning
```

**Good (12 points):**
```yaml
---
name: test-automator
Related skills: assessment, detection
---

## Capabilities
- pytest, Playwright, Selenium integration
- CI/CD pipeline integration
```

**Basic (8 points):**
```markdown
Uses external testing frameworks.
```

**None (0 points):**
No integration information.

---

## 5. Documentation Quality (15 points)

### Scoring Criteria

**15 points** - Comprehensive documentation
- Clear purpose statement
- Detailed capabilities (categorized for Opus)
- Behavioral traits defined
- Knowledge base documented
- Example interactions provided
- Response approach structured

**12 points** - Good documentation
- Purpose statement present
- Capabilities listed
- Behavioral traits included
- Examples provided

**8 points** - Adequate documentation
- Basic purpose
- Some capabilities
- Missing some sections

**4 points** - Minimal documentation
- Very brief documentation
- Major sections missing

**0 points** - No documentation
- Essentially undocumented

### Required Sections by Tier

**Opus (15 points requires ALL):**
- [x] Purpose statement
- [x] Capabilities (5-10 categories)
- [x] Behavioral Traits
- [x] Knowledge Base
- [x] Response Approach
- [x] Example Interactions

**Sonnet (15 points requires 5/6):**
- [x] Purpose statement
- [x] Capabilities (3-5 categories)
- [x] Behavioral Traits or Knowledge Base
- [x] Response Approach or Example Interactions

**Haiku (15 points requires 3/4):**
- [x] Brief focus areas
- [x] Approach steps
- [x] Output description

**Inherit (15 points requires 5/6):**
- [x] Purpose statement
- [x] Capabilities (4-6 categories)
- [x] Behavioral Traits
- [x] Knowledge Base
- [x] Example Interactions

### Evaluation Questions

- [ ] Is there a clear purpose statement?
- [ ] Are capabilities comprehensive and organized?
- [ ] Are behavioral traits defined?
- [ ] Is the knowledge base documented?
- [ ] Are example interactions provided?
- [ ] Is the response approach structured?

### Documentation Examples

**15 points (Opus - Complete):**
```markdown
## Purpose
Expert security auditor with comprehensive knowledge...

## Capabilities
### DevSecOps & Security Automation
- 10+ specific capabilities

### Modern Authentication & Authorization
- 8+ specific capabilities

[8 more categories...]

## Behavioral Traits
- Implements defense-in-depth
- Applies principle of least privilege
- Never trusts user input

## Knowledge Base
- OWASP guidelines and frameworks
- Modern authentication protocols
- DevSecOps tools and practices

## Response Approach
1. **Assess security requirements**
2. **Perform threat modeling**
[7 more steps...]

## Example Interactions
- "Conduct comprehensive security audit..."
- "Implement zero-trust authentication..."
[6 more examples...]
```

**8 points (Basic):**
```markdown
Expert in testing. Builds test automation.

## Capabilities
- Unit testing
- Integration testing
- E2E testing
```

---

## 6. Edge Cases & Safety (10 points)

### Scoring Criteria

**10 points** - Excellent safety
- Error handling explicitly mentioned
- Security considerations included
- Quality safeguards present
- Fallback strategies described
- Edge cases documented

**8 points** - Good safety
- Error handling mentioned
- Basic security considerations
- Some safeguards present

**5 points** - Basic safety
- Minimal error handling
- Limited safety considerations

**2 points** - Weak safety
- Little attention to edge cases
- Few safety measures

**0 points** - No safety
- No error handling or safety measures

### Evaluation Questions

- [ ] Is error handling mentioned in capabilities or behavioral traits?
- [ ] Are security considerations included?
- [ ] Are quality safeguards described?
- [ ] Are fallback strategies documented?
- [ ] Are edge cases or limitations mentioned?

### Safety Pattern Examples

**10 points:**
```markdown
## Behavioral Traits
- Implements defense-in-depth with multiple security layers
- Fails securely without information leakage
- Never trusts user input and validates everything
- Performs regular dependency scanning

## Capabilities
- Comprehensive error handling with custom exceptions
- Input validation and sanitization
- Rollback strategies for failed deployments
```

**5 points:**
```markdown
Handles errors appropriately.
```

**0 points:**
No mention of error handling or safety.

---

## Scoring Sheet

### Agent Information

- **Agent Name:** _________________
- **Model Tier:** Opus / Sonnet / Haiku / Inherit
- **Category:** _________________
- **Reviewer:** _________________
- **Date:** _________________

### Score Calculation

| Dimension | Max Points | Score | Notes |
|-----------|------------|-------|-------|
| 1. Model Appropriateness | 20 | _____ | |
| 2. Activation Clarity | 20 | _____ | |
| 3. Persona Consistency | 20 | _____ | |
| 4. Tool Integration | 15 | _____ | |
| 5. Documentation Quality | 15 | _____ | |
| 6. Edge Cases & Safety | 10 | _____ | |
| **TOTAL** | **100** | **_____** | |

### Quality Tier

- [ ] **90-100**: Exceptional - Gold standard
- [ ] **75-89**: Excellent - Production-ready
- [ ] **60-74**: Good - Minor improvements needed
- [ ] **45-59**: Fair - Significant improvements required
- [ ] **Below 45**: Poor - Major rework needed

### Improvement Recommendations

1. _________________________________________________
2. _________________________________________________
3. _________________________________________________
4. _________________________________________________
5. _________________________________________________

---

## Example Evaluations

### Example 1: security-auditor (Opus Agent)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Model Appropriateness | 20/20 | Opus perfect for critical security work |
| Activation Clarity | 20/20 | "Use PROACTIVELY for security audits, DevSecOps, or compliance" |
| Persona Consistency | 20/20 | Clear expert authority, consistent throughout |
| Tool Integration | 15/15 | Skills, agents, and tools well-documented |
| Documentation Quality | 15/15 | All sections present, comprehensive |
| Edge Cases & Safety | 10/10 | Defense-in-depth, error handling, security-first |
| **TOTAL** | **100/100** | **Exceptional - Gold Standard** |

---

### Example 2: debugger (Sonnet Agent)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Model Appropriateness | 18/20 | Sonnet appropriate for debugging (could argue for Inherit) |
| Activation Clarity | 18/20 | Clear proactive trigger for errors |
| Persona Consistency | 15/20 | Good procedural specialist, minimalist approach |
| Tool Integration | 10/15 | Basic integration, could document more tools |
| Documentation Quality | 10/15 | Concise but missing some sections (appropriate for Sonnet) |
| Edge Cases & Safety | 8/10 | Focuses on fixes, good error handling |
| **TOTAL** | **79/100** | **Excellent - Production-ready** |

---

### Example 3: mermaid-expert (Haiku Agent)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Model Appropriateness | 20/20 | Haiku perfect for fast diagram generation |
| Activation Clarity | 18/20 | Clear proactive trigger for visualizations |
| Persona Consistency | 18/20 | Good creation specialist, appropriate minimalism |
| Tool Integration | 12/15 | Mentions Mermaid syntax, could integrate with docs agents |
| Documentation Quality | 12/15 | Appropriate for Haiku tier, covers essentials |
| Edge Cases & Safety | 5/10 | Basic validation, could mention edge cases more |
| **TOTAL** | **85/100** | **Excellent - Production-ready** |

---

### Example 4: frontend-developer (Inherit Agent)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Model Appropriateness | 18/20 | Inherit appropriate for user choice (could argue for Sonnet) |
| Activation Clarity | 15/20 | "Use PROACTIVELY when creating UI" - good but could be more specific |
| Persona Consistency | 18/20 | Strong tech stack specialist persona |
| Tool Integration | 12/15 | Good framework integration, could reference related agents |
| Documentation Quality | 14/15 | Comprehensive, all major sections present |
| Edge Cases & Safety | 8/10 | Error boundaries, accessibility, good coverage |
| **TOTAL** | **85/100** | **Excellent - Production-ready** |

---

### Example 5: Poor Quality Agent

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Model Appropriateness | 5/20 | Using Opus for simple formatting (wasteful) |
| Activation Clarity | 5/20 | "Use when needed" - too vague |
| Persona Consistency | 8/20 | Generic developer persona |
| Tool Integration | 2/15 | No integration information |
| Documentation Quality | 4/15 | Minimal sections, brief descriptions |
| Edge Cases & Safety | 0/10 | No error handling mentioned |
| **TOTAL** | **24/100** | **Poor - Major rework needed** |

**Required Improvements:**
1. Change to Haiku tier for formatting task
2. Add specific activation trigger
3. Define clear persona (PP-07 creation specialist)
4. Document tool integration
5. Expand documentation with examples
6. Add error handling and validation

---

## Quality Improvement Workflow

### Step 1: Initial Assessment

1. Score the agent using this rubric
2. Identify dimensions below target (< 15/20, < 12/15, < 8/10)
3. Document specific issues

### Step 2: Prioritize Improvements

**High Priority (blocks production):**
- Model Appropriateness < 15
- Activation Clarity < 15
- Persona Consistency < 15

**Medium Priority (quality concerns):**
- Tool Integration < 10
- Documentation Quality < 10

**Low Priority (enhancements):**
- Edge Cases & Safety < 5

### Step 3: Implement Improvements

For each dimension:
1. Review pattern examples in [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md)
2. Study gold standard agents
3. Apply specific improvements
4. Re-score

### Step 4: Validate

- Re-run full assessment
- Verify total score ≥ 75
- Get peer review if available
- Deploy to production

---

## Continuous Improvement

### Monthly Quality Audits

1. Sample 10-20 agents randomly
2. Score using this rubric
3. Identify common issues
4. Update patterns and templates
5. Improve low-scoring agents

### Quality Metrics to Track

- **Average agent score** (target: 80+)
- **% agents ≥ 75** (target: 90%+)
- **% agents ≥ 90** (target: 20%+)
- **% agents < 60** (target: <5%)

### Common Improvement Patterns

**If average score is low:**
- Review and update templates
- Provide more examples
- Conduct training

**If specific dimension is consistently low:**
- Add more guidance for that dimension
- Update patterns
- Create dimension-specific examples

---

## Next Steps

1. **Score your agent** using this rubric
2. **Target 75+ points** for production deployment
3. **Improve low-scoring dimensions** using pattern guides
4. **Compare against gold standard** agents
5. **Iterate until production-ready**

**Related Resources:**
- [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md) - Patterns for improvement
- [AGENT_QUICK_START.md](AGENT_QUICK_START.md) - Agent creation process
- [security_auditor.md](../../domain-agentic-resources/agents/security/security_auditor.md) - Example production agent

---

**Document Version:** 1.0
**Last Updated:** 2025-12-27
**Total Possible Points:** 100
**Production Target:** 75+
