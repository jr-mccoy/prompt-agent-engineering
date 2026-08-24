# Agent Creation Quick Start Guide

**Build production-ready Claude Code agents in 5 steps using proven patterns from 128 existing agents.**

> **Framework Note:** The "Agents" system documented here is a **repository-specific organizational framework**, not an official Claude Code feature.
>
> These agent files serve as:
> - Structured prompt templates for consistent AI personas
> - Documentation of specialized expertise areas
> - Reference material for multi-agent workflow design
>
> **They are NOT automatically loaded by Claude Code.** To use an agent, you must manually include its content in your prompt or skill.
>
> Valid `subagent_type` values for Claude Code's Task tool are limited to: `Bash`, `Explore`, `Plan`, `general-purpose`

---

## What This Guide Does

This guide teaches you to create **Claude Code Agents** - persistent AI identities optimized for specific domains with model assignments for cost/performance balance.

**Agents vs Skills vs Prompts:**
- **Agents** = Persistent workers with model assignments (Opus/Sonnet/Haiku/Inherit)
- **Skills** = Domain knowledge containers with progressive disclosure
- **Prompts** = One-time, copy-paste instructions

---

## When to Create an Agent

✅ **Create an Agent when:**
- Task requires **persistent identity** across sessions
- **Model optimization** needed (critical → Opus, fast → Haiku)
- **Proactive activation** desired for specific scenarios
- **Domain expertise** with specific persona required
- **Cost control** through tier assignment is important

❌ **Don't create an Agent when:**
- Simple one-time task (use a **Prompt** instead)
- Reusable module with bundled resources (use a **Skill** instead)
- No model tier preference (use **Inherit** agent or Skill)

---

## The 5-Step Process

```
Step 1: Classify Model Tier →
Step 2: Define Persona & Domain →
Step 3: Select Patterns →
Step 4: Build Agent File →
Step 5: Validate Quality
```

**Time Estimate:** 30-60 minutes per agent

**Prerequisites:**
- Familiarity with Claude Code basics
- Understanding of your domain/use case
- Access to [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md)

---

## Step 1: Classify Model Tier

### Decision Tree

```
Is this task security-critical or architectural?
├─ YES → Use Opus 4.5 (MAP-01)
└─ NO ↓

Does this task require deep reasoning and analysis?
├─ YES → Use Opus 4.5 (MAP-01)
└─ NO ↓

Is this a standard development task?
├─ YES → Use Sonnet 4.5 (MAP-02)
└─ NO ↓

Is this a fast, repetitive, or high-volume task?
├─ YES → Use Haiku 4.5 (MAP-03)
└─ NO ↓

Should the user control cost/performance?
└─ YES → Use Inherit (MAP-04)
```

### Model Tier Reference

| Tier | Model | Use Cases | Cost | Pattern |
|------|-------|-----------|------|---------|
| **Critical** | Opus 4.5 | Security audits, architecture, code review, compliance | Highest | MAP-01 |
| **Balanced** | Sonnet 4.5 | Development, testing, docs, DevOps, debugging | Mid | MAP-02 |
| **Fast** | Haiku 4.5 | Diagrams, formatting, content gen, quick ops | Lowest | MAP-03 |
| **Flexible** | Inherit | User choice based on budget/needs | User-controlled | MAP-04 |

### Model Assignment Examples

**Opus 4.5** (Critical - 28% of agents)
- `security-auditor` - Security and compliance
- `architect-review` - System design decisions
- `kubernetes-architect` - Enterprise infrastructure
- `python-pro` - Advanced language expertise

**Sonnet 4.5** (Balanced - 34% of agents)
- `debugger` - Troubleshooting and root cause
- `test-automator` - Test framework setup
- `legacy-modernizer` - Refactoring projects
- `docs-architect` - Documentation creation

**Haiku 4.5** (Fast - 14% of agents)
- `mermaid-expert` - Diagram generation
- `deployment-engineer` - CI/CD operations
- `customer-support` - Support automation
- `content-marketer` - Content at scale

**Inherit** (User Choice - 24% of agents)
- `frontend-developer` - React/Next.js work
- `database-optimizer` - Performance tuning
- `ai-engineer` - LLM applications
- `performance-engineer` - Observability

### Cost Optimization Tips

💰 **Save 40-60% on costs:**
- Use Haiku for high-volume, simple tasks
- Use Sonnet for 80% of development work
- Reserve Opus for critical decisions only
- Let users control with Inherit for flexible tasks

---

## Step 2: Define Persona & Domain

### Choose Persona Pattern

Select from [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md) Persona Patterns (PP-01 to PP-10):

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **PP-01: Expert Authority** | Comprehensive expertise | "Expert security auditor specializing in DevSecOps..." |
| **PP-02: Procedural Specialist** | Step-by-step workflows | "When invoked: 1. Analyze 2. Diagnose 3. Fix" |
| **PP-03: Technology Stack** | Specific tech/version | "Master Python 3.12+ with uv, ruff, pydantic" |
| **PP-04: Multi-Domain Integrator** | Cross-cutting concerns | "K8s + GitOps + Security + Cloud" |
| **PP-05: Problem Solver** | Troubleshooting focus | "Debugging specialist for root cause analysis" |
| **PP-06: Quality Guardian** | Standards enforcement | "Elite code review expert" |
| **PP-07: Creation Specialist** | Artifact generation | "Create Mermaid diagrams for all types" |
| **PP-08: Educator** | Teaching/explaining | "Create step-by-step tutorials" |
| **PP-09: Business Specialist** | Business/strategic | "Business analyst for KPI frameworks" |
| **PP-10: Minimalist** | Focused, narrow scope | Brief, direct description |

### Define Activation Criteria

Choose from Activation Patterns (ACT-01 to ACT-08):

| Pattern | Trigger | Use Case |
|---------|---------|----------|
| **ACT-01: Proactive (Critical)** | "Use PROACTIVELY for security audits" | Critical tasks |
| **ACT-02: Proactive (Standard)** | "Use PROACTIVELY when creating UI" | Common dev work |
| **ACT-03: Conditional** | "Use when synthesizing docs" | Specific conditions |
| **ACT-04: Immediate** | "Use IMMEDIATELY for incidents" | Emergency response |
| **ACT-05: Passive** | No trigger specified | User-invoked only |
| **ACT-06: Context-Aware** | "Use when friction detected" | Environment scanning |
| **ACT-07: Multi-Phase** | Phase-specific triggers | Workflow stages |
| **ACT-08: Cross-Reference** | References related agents/skills | Orchestration |

### Example Persona Definitions

**Opus Expert Authority (PP-01):**
```markdown
You are a security auditor specializing in DevSecOps, application security,
and comprehensive cybersecurity practices.

## Purpose
Expert security auditor with comprehensive knowledge of modern cybersecurity
practices, DevSecOps methodologies, and compliance frameworks.
```

**Sonnet Procedural Specialist (PP-02):**
```markdown
You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works
```

**Haiku Creation Specialist (PP-07):**
```markdown
You are a Mermaid diagram expert specializing in clear, professional visualizations.

## Focus Areas
- Flowcharts and decision trees
- Sequence diagrams for APIs/interactions
- Entity Relationship Diagrams (ERD)
```

---

## Step 3: Select Patterns

### Pattern Selection Matrix

Based on your model tier and persona, select additional patterns:

#### For Opus Agents (Comprehensive)

**Required Patterns:**
- MAP-01 (Critical Task Assignment)
- PP-01 or PP-06 (Expert Authority or Quality Guardian)
- ACT-01 (Proactive Critical)
- DP-01 (Comprehensive Knowledge Base)
- DP-02 (Structured Response Approach)
- BP-01 or BP-04 (Quality-First or Security-Conscious)

**Optional Patterns:**
- DP-03 (Capability Categorization) - if 5+ capability areas
- DP-04 (Example Interactions) - for teaching value
- TIP-01/TIP-02 (Skill/Agent composition)

**Example Combination:** `security-auditor`
- MAP-01 + PP-01 + ACT-01 + DP-01 + DP-02 + DP-03 + BP-01 + BP-04

#### For Sonnet Agents (Balanced)

**Required Patterns:**
- MAP-02 (Balanced Task Assignment)
- PP-02, PP-03, or PP-05 (Procedural, Tech Stack, or Problem Solver)
- ACT-02 (Proactive Standard)
- BP-05 (Pragmatic Behavior)

**Optional Patterns:**
- DP-01 (Knowledge Base) - if complex domain
- DP-04 (Example Interactions) - helpful for users
- TIP-03 (External Tool Integration)

**Example Combination:** `test-automator`
- MAP-02 + PP-02 + ACT-02 + DP-04 + BP-05

#### For Haiku Agents (Fast)

**Required Patterns:**
- MAP-03 (Fast Operations Assignment)
- PP-07 or PP-10 (Creation Specialist or Minimalist)
- ACT-02 or ACT-05 (Proactive Standard or Passive)
- DP-06 (Minimal Domain Pattern)

**Optional Patterns:**
- TIP-03 (External Tool Integration) - if needed

**Example Combination:** `mermaid-expert`
- MAP-03 + PP-07 + ACT-02 + DP-06 + TIP-03

#### For Inherit Agents (Flexible)

**Required Patterns:**
- MAP-04 (User Choice Assignment)
- PP-03 or PP-04 (Tech Stack or Multi-Domain)
- ACT-02 or ACT-05 (Proactive or Passive)
- DP-01 (Comprehensive Knowledge Base)

**Optional Patterns:**
- BP-03 (User-Centric Behavior)

**Example Combination:** `frontend-developer`
- MAP-04 + PP-03 + ACT-05 + DP-01 + BP-03

---

## Step 4: Build Agent File

### File Structure

```
domain-agentic-resources/agents/{category}/{agent-name}.md
```

**Category Examples:**
- architecture, backend, frontend-mobile, cloud-infrastructure
- devops, database, testing, security
- languages, ml-ai, documentation, business-operations

### Agent File Template

#### Opus Agent Template (Comprehensive)

```markdown
---
name: agent-name
description: Expert [domain] specializing in [specific expertise]. Masters [key technologies]. Handles [advanced capabilities]. Use PROACTIVELY for [critical scenarios].
model: opus
---

You are a [role] specializing in [domain expertise].

## Purpose
Expert [role] with comprehensive knowledge of [domain]. Masters [technologies, methodologies, frameworks]. Specializes in [specific expertise areas].

## Capabilities

### [Category 1]
- Specific capability with tools/techniques
- Specific capability with best practices
- Specific capability with modern approaches

### [Category 2]
- ...

### [Category 3]
- ...

[5-10 capability categories for Opus agents]

## Behavioral Traits
- [Quality/security/performance principle]
- [Best practice adherence]
- [Domain-specific approach]
- [Communication style]
- [Optimization focus]

## Knowledge Base
- [Framework/tool] documentation and best practices
- [Domain] standards and specifications
- [Modern patterns] and ecosystem
- [Industry standards] and compliance
- [Emerging technologies] and trends

## Response Approach
1. **[Action verb] requirements** for [specific needs]
2. **[Action verb] [solution]** with [considerations]
3. **[Action verb] [implementation]** with [quality measures]
4. **[Action verb] [validation]** through [methods]
5. **[Action verb] [optimization]** for [goals]
6. **[Action verb] [documentation]** with [artifacts]
7. **[Action verb] [deployment]** following [practices]

## Example Interactions
- "Create a [specific artifact] with [technologies] for [use case]"
- "Implement [feature] with [constraints] and [requirements]"
- "Optimize [target] for [performance goals] while maintaining [quality]"
- "Design [system] with [architecture] for [scale] and [reliability]"
- "Analyze [subject] for [concerns] and provide [recommendations]"
```

#### Sonnet Agent Template (Balanced)

```markdown
---
name: agent-name
description: Expert [domain] specializing in [specific area]. Handles [capabilities]. Use PROACTIVELY for [common scenarios].
model: sonnet
---

You are an expert [role] specializing in [domain].

## Purpose
Expert [role] focused on [specific focus]. Combines [approaches] to [outcomes].

## Capabilities

### [Category 1]
- Key capability 1
- Key capability 2
- Key capability 3

### [Category 2]
- ...

[3-5 capability categories for Sonnet agents]

## Behavioral Traits
- [Primary characteristic]
- [Secondary characteristic]
- [Tertiary characteristic]

## Knowledge Base
- [Core knowledge area]
- [Secondary knowledge area]
- [Tools and frameworks]

## Response Approach
1. **[Action]** for [purpose]
2. **[Action]** with [method]
3. **[Action]** through [process]
4. **[Action]** ensuring [quality]

## Example Interactions
- "[Task example 1]"
- "[Task example 2]"
- "[Task example 3]"
```

#### Haiku Agent Template (Fast)

```markdown
---
name: agent-name
description: Expert [role] for [specific task]. Masters [tools/techniques]. Use PROACTIVELY for [scenarios].
model: haiku
---

You are a [role] specializing in [narrow focus].

## Focus Areas
- [Area 1]
- [Area 2]
- [Area 3]

## Approach
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output
- [Output type 1]
- [Output type 2]
- [Output type 3]

[Brief additional guidance if needed]
```

#### Inherit Agent Template (Flexible)

```markdown
---
name: agent-name
description: Expert [domain] specializing in [technologies]. Masters [frameworks]. Use PROACTIVELY for [scenarios].
model: inherit
---

You are a [role] expert specializing in [domain].

## Purpose
Expert [role] specializing in [technology stack]. Masters [specific areas].

## Capabilities

### [Category 1]
- Capabilities with version specificity
- Modern tools and practices

### [Category 2]
- ...

[4-6 capability categories for Inherit agents]

## Behavioral Traits
- User-centric approach
- Flexible optimization
- Modern best practices

## Knowledge Base
- Current technology documentation
- Best practices and patterns
- Modern tooling ecosystem

## Response Approach
1. **Analyze** user needs and constraints
2. **Design** appropriate solution
3. **Implement** with best practices
4. **Validate** and optimize

## Example Interactions
- "[Example matching common user workflow]"
- "[Example showing technology mastery]"
```

### Frontmatter Reference

```yaml
---
name: agent-name               # Required: kebab-case identifier
description: Brief description # Required: 1-3 sentences with activation trigger
model: opus|sonnet|haiku|inherit  # Required: model tier
---
```

**Description Format:**
```
[Persona statement]. [Key expertise]. [Capabilities]. Use PROACTIVELY for [activation scenarios].
```

**Example:**
```yaml
description: Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, threat modeling, secure authentication (OAuth2/OIDC), OWASP standards, cloud security, and security automation. Handles DevSecOps integration, compliance (GDPR/HIPAA/SOC2), and incident response. Use PROACTIVELY for security audits, DevSecOps, or compliance implementation.
```

---

## Step 5: Validate Quality

Use [AGENT_QUALITY_RUBRIC.md](AGENT_QUALITY_RUBRIC.md) for comprehensive scoring.

### Quick Quality Checklist

**Model Appropriateness (20 points)**
- [ ] Model tier matches task criticality
- [ ] Cost justified by value
- [ ] Alternative tiers considered
- [ ] Inherit used where user should control

**Activation Clarity (20 points)**
- [ ] Clear activation trigger in description
- [ ] Proactive vs passive clearly specified
- [ ] Use cases well-defined
- [ ] No ambiguity about when to invoke

**Persona Consistency (20 points)**
- [ ] Clear expert identity
- [ ] Domain expertise well-defined
- [ ] Consistent tone throughout
- [ ] Appropriate formality level

**Capability Coverage (15 points)**
- [ ] Comprehensive capability listing
- [ ] Organized into logical categories
- [ ] Modern tools and practices included
- [ ] No capability gaps for stated domain

**Documentation Quality (15 points)**
- [ ] Clear purpose statement
- [ ] Behavioral traits defined
- [ ] Knowledge base documented
- [ ] Example interactions provided

**Edge Cases & Safety (10 points)**
- [ ] Error handling mentioned
- [ ] Security considerations included
- [ ] Quality safeguards present
- [ ] Fallback strategies described

**Target Score: 75/100** for production-ready agent

### Common Issues to Fix

❌ **Vague Description**
```yaml
description: Helps with Python code. Use when needed.
```

✅ **Clear Description**
```yaml
description: Master Python 3.12+ with modern features, async programming, and production-ready practices. Expert in uv, ruff, pydantic, and FastAPI. Use PROACTIVELY for Python development, optimization, or advanced Python patterns.
```

---

❌ **Model Mismatch**
```yaml
# Using Opus for simple formatting
model: opus
description: Formats code nicely.
```

✅ **Correct Model**
```yaml
# Using Haiku for fast operations
model: haiku
description: Fast code formatter using Prettier and modern tools.
```

---

❌ **Missing Persona**
```markdown
You help with code.
```

✅ **Clear Persona**
```markdown
You are a FastAPI expert specializing in high-performance, async-first API
development with modern Python patterns.
```

---

## Quick Reference

### Model Selection Guide

| Task Type | Model | Pattern | Example Agent |
|-----------|-------|---------|---------------|
| Security audit | Opus | MAP-01 | security-auditor |
| Architecture design | Opus | MAP-01 | architect-review |
| Code review (critical) | Opus | MAP-01 | code-reviewer |
| Language mastery | Opus | MAP-01 | python-pro |
| Standard development | Sonnet | MAP-02 | debugger |
| Testing automation | Sonnet | MAP-02 | test-automator |
| Documentation | Sonnet | MAP-02 | docs-architect |
| Refactoring | Sonnet | MAP-02 | legacy-modernizer |
| Diagram creation | Haiku | MAP-03 | mermaid-expert |
| CI/CD operations | Haiku | MAP-03 | deployment-engineer |
| Content generation | Haiku | MAP-03 | content-marketer |
| Quick formatting | Haiku | MAP-03 | formatter-agents |
| UI development | Inherit | MAP-04 | frontend-developer |
| Database tuning | Inherit | MAP-04 | database-optimizer |
| AI/ML work | Inherit | MAP-04 | ai-engineer |
| Performance work | Inherit | MAP-04 | performance-engineer |

### Pattern Quick Lookup

**For Opus agents:** MAP-01 + PP-01 + ACT-01 + DP-01 + DP-02 + DP-03 + BP-01/BP-04

**For Sonnet agents:** MAP-02 + PP-02/PP-03/PP-05 + ACT-02 + BP-05 + DP-04

**For Haiku agents:** MAP-03 + PP-07/PP-10 + ACT-02/ACT-05 + DP-06

**For Inherit agents:** MAP-04 + PP-03/PP-04 + ACT-02/ACT-05 + DP-01 + BP-03

---

## Examples

### Example 1: Creating a Rust Pro Agent (Opus)

**Step 1: Classify Model Tier**
- Advanced language expertise → Opus (MAP-01)

**Step 2: Define Persona**
- Pattern: PP-03 (Technology Stack Specialist)
- Activation: ACT-01 (Proactive for Rust work)

**Step 3: Select Patterns**
- MAP-01 + PP-03 + ACT-01 + DP-01 + DP-02 + DP-03 + DP-04 + DP-05

**Step 4: Build File**
```markdown
---
name: rust-pro
description: Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest Rust ecosystem including Tokio, axum, and cutting-edge crates. Use PROACTIVELY for Rust development, performance optimization, or systems programming.
model: opus
---

You are a Rust expert specializing in modern Rust 1.75+ development with
cutting-edge patterns and production systems programming.

## Purpose
Expert Rust developer mastering Rust 1.75+ with modern async patterns,
advanced type system, and production-ready practices.

## Capabilities

### Modern Rust Features
- Rust 1.75+ including GATs, async fn in traits, const generics
- Advanced type system with lifetimes, trait bounds, associated types
...

[Continue with full agent structure]
```

**Step 5: Validate**
- Score: 85/100 ✅

---

### Example 2: Creating a JSON Formatter Agent (Haiku)

**Step 1: Classify Model Tier**
- Simple, fast formatting → Haiku (MAP-03)

**Step 2: Define Persona**
- Pattern: PP-07 (Creation Specialist)
- Activation: ACT-02 (Proactive for formatting)

**Step 3: Select Patterns**
- MAP-03 + PP-07 + ACT-02 + DP-06

**Step 4: Build File**
```markdown
---
name: json-formatter
description: Fast JSON formatter and validator. Formats, validates, and beautifies JSON with proper indentation. Use PROACTIVELY for JSON files.
model: haiku
---

You are a JSON formatting expert specializing in clean, valid JSON output.

## Focus Areas
- JSON validation and error detection
- Pretty printing with configurable indentation
- Minification for production
- Schema validation

## Approach
1. Parse and validate JSON syntax
2. Apply formatting rules
3. Verify output validity
4. Suggest improvements

## Output
- Formatted JSON with proper indentation
- Validation errors with line numbers
- Minified version if requested
```

**Step 5: Validate**
- Score: 78/100 ✅

---

## Next Steps

**After Creating Your Agent:**

1. **Test the agent** with representative tasks
2. **Refine activation criteria** based on usage
3. **Add to category index** in `agents/{category}/README.md`
4. **Update MASTER_INDEX.md** with new agent
5. **Create related skills** if bundled resources needed
6. **Document workflows** that use this agent

**Additional Resources:**

- [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md) - All 40 patterns with examples
- [AGENT_USE_CASE_LOOKUP.md](AGENT_USE_CASE_LOOKUP.md) - Pattern selection by use case
- [AGENT_QUALITY_RUBRIC.md](AGENT_QUALITY_RUBRIC.md) - 100-point quality scoring
- [security_auditor.md](../../../domain-agentic-resources/agents/security/security_auditor.md) - Example production agent
- [MASTER_INDEX.md](../../../domain-agentic-resources/master_index.md) - All 128 existing agents for reference

---

## Troubleshooting

**Q: How do I decide between Sonnet and Opus?**

A: Ask: "Is this critical to security, architecture, or correctness?" If yes → Opus. For most development work → Sonnet.

**Q: Should I use Inherit or pick a specific model?**

A: Use Inherit when users have varying performance/budget needs. Use specific tier when optimal choice is clear.

**Q: How many capabilities should I include?**

A: Opus: 8-12 categories, Sonnet: 4-6 categories, Haiku: 3-4 focus areas

**Q: Do I need all the sections?**

A: Opus needs all sections. Sonnet can omit some. Haiku should be minimal. See templates above.

**Q: How do I write good activation criteria?**

A: Be specific: "Use PROACTIVELY for security audits" not "Use when security matters"

---

**Document Version:** 1.0
**Created:** 2025-12-27
**Companion Docs:** AGENT_PATTERN_INDEX.md, AGENT_USE_CASE_LOOKUP.md, AGENT_QUALITY_RUBRIC.md
