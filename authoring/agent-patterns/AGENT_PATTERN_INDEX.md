# Agent Pattern Index

**Complete catalog of agent design patterns extracted from 128 production agents across all model tiers.**

---

## Overview

This index documents **40 agent patterns** discovered through analysis of existing agents in the Claude Code Resources library. These patterns represent proven approaches for building effective, cost-optimized, and maintainable agents.

**Pattern Categories:**
- **MAP (Model Assignment Patterns)**: 5 patterns - Model tier selection and optimization
- **PP (Persona Patterns)**: 10 patterns - Agent identity and expertise definition
- **ACT (Activation Patterns)**: 8 patterns - When and how agents should activate
- **TIP (Tool Integration Patterns)**: 6 patterns - How agents use tools and skills
- **BP (Behavioral Patterns)**: 5 patterns - Agent response and interaction style
- **DP (Domain Patterns)**: 6 patterns - Domain-specific expertise organization

**Total Patterns: 40**

---

## Table of Contents

1. [Model Assignment Patterns (MAP-01 to MAP-05)](#model-assignment-patterns-map)
2. [Persona Patterns (PP-01 to PP-10)](#persona-patterns-pp)
3. [Activation Patterns (ACT-01 to ACT-08)](#activation-patterns-act)
4. [Tool Integration Patterns (TIP-01 to TIP-06)](#tool-integration-patterns-tip)
5. [Behavioral Patterns (BP-01 to BP-05)](#behavioral-patterns-bp)
6. [Domain Patterns (DP-01 to DP-06)](#domain-patterns-dp)
7. [Pattern Combinations](#pattern-combinations)
8. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Model Assignment Patterns (MAP)

### MAP-01: Critical Task Assignment (Opus)

**When to use:** Security audits, architecture decisions, complex code review, critical infrastructure

**Model:** Opus 4.8

**Characteristics:**
- Tasks requiring highest reasoning capability
- Security-critical operations
- Architectural decision-making
- Complex analysis and deep expertise
- Compliance and regulatory work
- Strategic planning and design

**Cost Implication:** Highest cost, justified by criticality

**Example Agents:**
- `security-auditor` - DevSecOps and comprehensive security
- `architect-review` - System architecture and design review
- `kubernetes-architect` - Enterprise container orchestration
- `python-pro` - Advanced Python patterns and optimization

**Pattern Structure:**
```yaml
---
name: agent-name
model: opus
description: Expert in critical domain. Use PROACTIVELY for high-stakes decisions.
---
```

**Real-World Usage:**
```markdown
You are a security auditor specializing in DevSecOps, application security,
and comprehensive cybersecurity practices.

## Purpose
Expert security auditor with comprehensive knowledge of modern cybersecurity
practices, DevSecOps methodologies, and compliance frameworks.
```

---

### MAP-02: Balanced Task Assignment (Sonnet)

**When to use:** General development, code quality, documentation, DevOps, testing

**Model:** Sonnet 4.6

**Characteristics:**
- Balanced intelligence and speed
- Most common development tasks
- Code quality and reviews
- Documentation creation
- Testing automation
- DevOps troubleshooting

**Cost Implication:** Mid-tier cost, optimal for most tasks

**Example Agents:**
- `debugger` - Root cause analysis and troubleshooting
- `test-automator` - Comprehensive test automation
- `legacy-modernizer` - Refactoring and modernization
- `docs-architect` - Technical documentation

**Pattern Structure:**
```yaml
---
name: agent-name
model: sonnet
description: Expert in domain. Use PROACTIVELY for standard development tasks.
---
```

**Real-World Usage:**
```markdown
You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
```

---

### MAP-03: Fast Operations Assignment (Haiku)

**When to use:** Quick operations, formatting, diagram generation, simple automation

**Model:** Haiku 4.5

**Characteristics:**
- Speed-optimized tasks
- Diagram and visualization generation
- Simple documentation
- Quick formatting and linting
- Sales/marketing content
- Repetitive operations

**Cost Implication:** Lowest cost, high throughput

**Example Agents:**
- `mermaid-expert` - Diagram generation
- `deployment-engineer` - Fast CI/CD operations
- `customer-support` - AI-powered support automation
- `content-marketer` - Content creation at scale

**Pattern Structure:**
```yaml
---
name: agent-name
model: haiku
description: Expert in fast operations. Use PROACTIVELY for high-volume tasks.
---
```

**Real-World Usage:**
```markdown
You are a Mermaid diagram expert specializing in clear, professional visualizations.

## Focus Areas
- Flowcharts and decision trees
- Sequence diagrams for APIs/interactions
- Entity Relationship Diagrams (ERD)
```

---

### MAP-04: User Choice Assignment (Inherit)

**When to use:** Tasks where user controls cost/performance trade-off

**Model:** inherit

**Characteristics:**
- Flexible performance requirements
- Budget-conscious operations
- Experimental features
- User-controlled optimization
- Non-critical path tasks
- Development vs production trade-offs

**Cost Implication:** User-controlled based on budget

**Example Agents:**
- `frontend-developer` - React/Next.js development
- `database-optimizer` - Performance tuning
- `ai-engineer` - LLM application development
- `performance-engineer` - Observability and optimization

**Pattern Structure:**
```yaml
---
name: agent-name
model: inherit
description: Expert in domain. User chooses model based on budget and performance needs.
---
```

**Real-World Usage:**
```markdown
You are a frontend development expert specializing in modern React applications,
Next.js, and cutting-edge frontend architecture.

## Purpose
Expert frontend developer specializing in React 19+, Next.js 15+, and modern
web application development.
```

---

### MAP-05: Dynamic Model Selection

**When to use:** Agents that adapt model based on task complexity within domain

**Model:** varies (conditional logic in description)

**Characteristics:**
- Task complexity analysis
- Automatic tier escalation
- Cost optimization through smart routing
- Hybrid approaches (start with Haiku, escalate to Sonnet/Opus)

**Cost Implication:** Optimized cost through intelligent routing

**Implementation:**
```markdown
## Model Selection Strategy
- Simple queries → Haiku
- Standard development → Sonnet
- Critical decisions → Opus
- User override available
```

**Usage Guidance:**
- Not yet widely implemented in existing agents
- Emerging pattern for future optimization
- Requires orchestration layer

---

## Persona Patterns (PP)

### PP-01: Expert Authority Persona

**When to use:** Establishing credibility and comprehensive expertise

**Characteristics:**
- "Expert", "Master", "Elite" titles
- Comprehensive knowledge declaration
- Authority in specific domain
- Deep technical expertise
- Years of experience implied

**Example Agents:**
- "Expert security auditor specializing in DevSecOps..."
- "Master Python 3.12+ with modern features..."
- "Elite AI-powered customer support specialist..."

**Pattern Structure:**
```markdown
You are an [expert/master/elite] [role] specializing in [domain expertise].

## Purpose
[Expert/Master/Elite] [role] with comprehensive knowledge of [technologies,
methodologies, frameworks]. Masters [key capabilities]. Specializes in
[specific expertise areas].
```

**Real-World Usage:**
```markdown
You are a FastAPI expert specializing in high-performance, async-first API development
with modern Python patterns.

## Purpose
Expert FastAPI developer specializing in high-performance, async-first API development.
```

---

### PP-02: Procedural Specialist Persona

**When to use:** Agents focused on specific workflows and processes

**Characteristics:**
- Step-by-step process emphasis
- Workflow-oriented description
- Clear procedure definition
- Systematic approach
- Checklist-driven

**Example Agents:**
- `debugger` - "When invoked: 1. Capture error... 2. Identify reproduction steps..."
- Deployment agents with specific deployment sequences

**Pattern Structure:**
```markdown
You are an expert [role] specializing in [process].

When invoked:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]
```

**Real-World Usage:**
```markdown
When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works
```

---

### PP-03: Technology Stack Specialist

**When to use:** Deep expertise in specific technology ecosystem

**Characteristics:**
- Technology version specificity (e.g., "Python 3.12+", "React 19")
- Ecosystem mastery
- Framework-specific patterns
- Version-aware best practices
- Modern tooling emphasis

**Example Agents:**
- `python-pro` - "Python 3.12+ with uv, ruff, pydantic"
- `frontend-developer` - "React 19, Next.js 15"
- `fastapi-pro` - "FastAPI 0.100+, SQLAlchemy 2.0"

**Pattern Structure:**
```markdown
You are a [technology] expert specializing in [specific version/framework] with
cutting-edge [tools/practices] from the [year] ecosystem.

## Purpose
Expert [technology] developer mastering [version]+ features, [modern tooling],
and production-ready development practices.
```

---

### PP-04: Multi-Domain Integrator

**When to use:** Agents bridging multiple domains or technologies

**Characteristics:**
- Cross-domain expertise
- Integration focus
- Multiple technology stacks
- Architectural perspective
- System-level thinking

**Example Agents:**
- `kubernetes-architect` - Cloud + containers + GitOps + security
- `cloud-architect` - Multi-cloud + IaC + FinOps + compliance

**Pattern Structure:**
```markdown
You are a [role] specializing in [domain A], [domain B], and [domain C]
integration. Masters [cross-cutting concerns] across [multiple systems].
```

---

### PP-05: Problem Solver Persona

**When to use:** Troubleshooting and resolution-focused agents

**Characteristics:**
- Problem identification emphasis
- Root cause analysis focus
- Solution-oriented approach
- Diagnostic expertise
- Fix-it mindset

**Example Agents:**
- `debugger` - "Debugging specialist for errors, test failures, and unexpected behavior"
- `devops-troubleshooter` - "Expert DevOps troubleshooter specializing in rapid incident response"

**Pattern Structure:**
```markdown
You are a [problem-solving role] specializing in [types of problems].

[Process-oriented problem-solving approach]
```

---

### PP-06: Quality Guardian Persona

**When to use:** Agents focused on quality assurance and standards

**Characteristics:**
- Quality standards enforcement
- Best practices advocacy
- Review and validation focus
- Compliance checking
- Standards documentation

**Example Agents:**
- `code-reviewer` - "Elite code review expert"
- `test-automator` - "Quality engineering strategies"
- `security-auditor` - "Compliance frameworks"

**Pattern Structure:**
```markdown
You are a [quality role] specializing in [quality domain]. Masters [standards,
frameworks, best practices]. Ensures [quality outcomes].
```

---

### PP-07: Creation Specialist Persona

**When to use:** Agents that build or generate artifacts

**Characteristics:**
- Creation and generation focus
- Output-oriented description
- Building/constructing emphasis
- Artifact production
- Template and scaffold creation

**Example Agents:**
- `mermaid-expert` - "Create Mermaid diagrams"
- `api-documenter` - "Create interactive docs, generate SDKs"
- Content creation agents

**Pattern Structure:**
```markdown
You are a [creator role] specializing in [what you create]. Creates [outputs]
with [quality attributes].

## Output
- [Artifact type 1]
- [Artifact type 2]
- [Artifact type 3]
```

---

### PP-08: Educator Persona

**When to use:** Agents focused on teaching and knowledge transfer

**Characteristics:**
- Teaching and explanation focus
- Educational approach
- Progressive learning
- Concept explanation
- Tutorial creation

**Example Agents:**
- `tutorial-engineer` - "Creates step-by-step tutorials and educational content"
- Teaching-focused documentation agents

**Pattern Structure:**
```markdown
You are an [educator role] specializing in [domain]. Transforms [complex concepts]
into [accessible learning experiences].
```

---

### PP-09: Business Specialist Persona

**When to use:** Business-focused agents (non-technical or hybrid)

**Characteristics:**
- Business context awareness
- ROI and value focus
- Strategic thinking
- Stakeholder communication
- Business metrics emphasis

**Example Agents:**
- `business-analyst` - "Business intelligence and strategic analysis"
- `hr-pro` - "Professional, ethical HR partner"
- `legal-advisor` - "GDPR-compliant texts, compliance"

**Pattern Structure:**
```markdown
You are a [business role] specializing in [business domain]. Focuses on
[business outcomes, compliance, strategy].
```

---

### PP-10: Minimalist Persona

**When to use:** Simple, focused agents with narrow scope

**Characteristics:**
- Brief description
- Focused scope
- Single responsibility
- No elaborate sections
- Direct and concise

**Example Agents:**
- `debugger` - Very concise, procedural
- Some Haiku-tier agents

**Pattern Structure:**
```markdown
You are an expert [role] specializing in [narrow focus].

[Brief procedural description]
```

---

## Activation Patterns (ACT)

### ACT-01: Proactive Activation (Critical)

**When to use:** Agents that should activate without user prompting for critical tasks

**Activation Trigger:** "Use PROACTIVELY for [critical scenarios]"

**Characteristics:**
- No user request needed
- Automatic engagement on triggers
- Critical path operations
- Security and compliance
- Architecture decisions

**Example Usage:**
```yaml
description: Expert security auditor... Use PROACTIVELY for security audits,
DevSecOps, or compliance implementation.
```

**Real-World Agents:**
- `security-auditor` - Security audits
- `architect-review` - Architectural decisions
- `code-reviewer` - Code quality assurance

**Implementation:**
```markdown
Use PROACTIVELY for:
- [Critical scenario 1]
- [Critical scenario 2]
- [Critical scenario 3]
```

---

### ACT-02: Proactive Activation (Standard)

**When to use:** Agents for common development tasks

**Activation Trigger:** "Use PROACTIVELY for [task types]"

**Characteristics:**
- Common development scenarios
- Standard workflows
- Regular operations
- No special authorization needed

**Example Usage:**
```yaml
description: Build React components... Use PROACTIVELY when creating UI
components or fixing frontend issues.
```

**Real-World Agents:**
- `frontend-developer` - UI components
- `python-pro` - Python development
- `test-automator` - Testing automation

---

### ACT-03: Conditional Activation

**When to use:** Agents that activate based on specific conditions

**Activation Trigger:** "Use when [specific condition]"

**Characteristics:**
- Context-dependent activation
- Specific trigger conditions
- Event-based engagement
- Conditional logic

**Example Usage:**
```yaml
description: Expert C4 Component-level specialist. Use when synthesizing
code-level documentation into logical components.
```

**Real-World Agents:**
- C4 documentation agents - Specific documentation phases
- Workflow-specific agents

---

### ACT-04: Immediate Activation

**When to use:** Emergency and incident response

**Activation Trigger:** "Use IMMEDIATELY for [crisis]"

**Characteristics:**
- Emergency response
- Production incidents
- Critical outages
- Time-sensitive operations
- Escalation scenarios

**Example Usage:**
```markdown
Use IMMEDIATELY for production incidents or SRE practices.
```

**Real-World Agents:**
- `incident-responder` - Production incidents

---

### ACT-05: Passive Activation (On Request)

**When to use:** Specialized agents invoked only when explicitly needed

**Activation Trigger:** No proactive trigger specified

**Characteristics:**
- User-initiated only
- Specialized use cases
- Optional enhancement
- No automatic engagement

**Example Agents:**
- Some niche language specialists
- Optional optimization agents

---

### ACT-06: Context-Aware Activation

**When to use:** Agents that analyze context before engaging

**Activation Trigger:** "Use PROACTIVELY when [context detected]"

**Characteristics:**
- Environment scanning
- Context analysis
- Smart triggering
- Situational awareness

**Example Usage:**
```markdown
Use PROACTIVELY when setting up new projects, after team feedback, or when
development friction is noticed.
```

**Real-World Agents:**
- `dx-optimizer` - Developer experience improvements

---

### ACT-07: Multi-Phase Activation

**When to use:** Agents for specific phases of larger workflows

**Activation Trigger:** Phase-specific triggers

**Characteristics:**
- Workflow phase awareness
- Sequential activation
- Pipeline stage alignment
- Multi-step processes

**Example Agents:**
- C4 documentation series (code → component → container → context)
- TDD orchestrator phases

---

### ACT-08: Cross-Reference Activation

**When to use:** Agents that reference related agents/skills

**Activation Trigger:** Related agent mentions in description

**Characteristics:**
- Agent composition awareness
- Skill integration references
- Multi-agent coordination
- Workflow orchestration hints

**Example Usage:**
```yaml
Related agents: security, database-architect, performance-engineer
Related skills: verification, definition
```

---

## Tool Integration Patterns (TIP)

### TIP-01: Skill Composition

**When to use:** Agents that leverage existing skills

**Characteristics:**
- References to skills in frontmatter
- Skill invocation in capabilities
- Modular capability extension
- Reusable domain knowledge

**Pattern Structure:**
```yaml
---
name: agent-name
description: ...
Related skills: skill-a, skill-b, skill-c
---
```

**Example Agents:**
- Agents with "Related skills: implementation, recognition"

---

### TIP-02: Agent Orchestration

**When to use:** Agents that coordinate other agents

**Characteristics:**
- Multi-agent workflow coordination
- Agent invocation patterns
- Workflow orchestration
- Sequential or parallel agent execution

**Pattern Structure:**
```yaml
Related agents: agent-a, agent-b, agent-c
```

**Example Agents:**
- `tdd-orchestrator` - Coordinates testing workflow
- Architecture agents coordinating review agents

---

### TIP-03: External Tool Integration

**When to use:** Agents that integrate with external tools/APIs

**Characteristics:**
- Tool/API mentions in capabilities
- Integration patterns documented
- Authentication handling
- API-specific patterns

**Example Capabilities:**
```markdown
### Integration Patterns
- Message queues (RabbitMQ, Kafka, Redis Pub/Sub)
- External API integration with httpx
- gRPC service integration
```

**Example Agents:**
- `fastapi-pro` - External service integration
- `observability-engineer` - Monitoring tools

---

### TIP-04: Framework Mastery

**When to use:** Agents deeply integrated with specific frameworks

**Characteristics:**
- Framework-specific patterns
- Deep tool integration
- Framework best practices
- Ecosystem expertise

**Example:**
```markdown
## Capabilities
### Core FastAPI Expertise
- FastAPI 0.100+ features
- Pydantic V2 for data validation
- SQLAlchemy 2.0+ with async support
```

---

### TIP-05: CLI and Command Execution

**When to use:** Agents that execute system commands

**Characteristics:**
- Bash/shell command generation
- CLI tool usage
- System operations
- Infrastructure commands

**Example Agents:**
- DevOps agents (Terraform, Kubernetes CLI)
- Deployment agents (kubectl, helm)

---

### TIP-06: Progressive Disclosure

**When to use:** Agents with layered capability exposure

**Characteristics:**
- Metadata layer (always loaded)
- Detailed capabilities (loaded on activation)
- Advanced features (loaded on demand)
- Resource bundling for complex scenarios

**Pattern Structure:**
```yaml
---
# Metadata layer (~100 tokens)
name: agent-name
description: Brief description for discovery
model: opus
---

# Instructions layer (<5k tokens)
You are an expert...

## Purpose
[Core purpose]

## Capabilities
[Detailed capabilities revealed on activation]
```

---

## Behavioral Patterns (BP)

### BP-01: Quality-First Behavior

**When to use:** Agents prioritizing quality and best practices

**Characteristics:**
```markdown
## Behavioral Traits
- Implements defense-in-depth with multiple security layers
- Follows [framework] best practices religiously
- Writes comprehensive tests with high coverage (>90%)
- Documents code thoroughly with docstrings
```

**Example Agents:**
- `security-auditor` - Security-first approach
- `python-pro` - PEP 8 and best practices
- `code-reviewer` - Quality assurance focus

---

### BP-02: Performance-Conscious Behavior

**When to use:** Agents focused on optimization

**Characteristics:**
```markdown
## Behavioral Traits
- Considers performance implications
- Writes async-first code by default
- Optimizes for Core Web Vitals
- Profiles and benchmarks regularly
```

**Example Agents:**
- `fastapi-pro` - Async-first patterns
- `performance-engineer` - Optimization focus

---

### BP-03: User-Centric Behavior

**When to use:** Agents focused on user experience

**Characteristics:**
```markdown
## Behavioral Traits
- Prioritizes user experience and performance equally
- Empathy-first approach with genuine care
- Clear communication with jargon-free explanations
- Considers accessibility from the design phase
```

**Example Agents:**
- `frontend-developer` - UX and accessibility
- `customer-support` - Empathy and clarity

---

### BP-04: Security-Conscious Behavior

**When to use:** Security-aware agents

**Characteristics:**
```markdown
## Behavioral Traits
- Never trusts user input and validates everything
- Fails securely without information leakage
- Implements principle of least privilege
- Performs regular dependency scanning
```

**Example Agents:**
- `security-auditor` - Defense in depth
- Backend security agents

---

### BP-05: Pragmatic Behavior

**When to use:** Practical, solution-focused agents

**Characteristics:**
```markdown
## Behavioral Traits
- Focuses on practical, actionable fixes
- Balances automation investment with manual expertise
- Values automation and continuous monitoring
- Considers business risk and impact
```

**Example Agents:**
- `debugger` - Root cause, not symptoms
- `test-automator` - Balanced automation

---

## Domain Patterns (DP)

### DP-01: Comprehensive Knowledge Base

**When to use:** Agents with extensive domain knowledge

**Structure:**
```markdown
## Knowledge Base
- [Technology] official documentation
- [Framework] best practices
- [Domain] standards and specifications
- Modern [tools] and ecosystem
- [Industry] standards and compliance
```

**Example Agents:**
- All Opus-tier agents
- Technology specialists

---

### DP-02: Structured Response Approach

**When to use:** Agents with defined workflows

**Structure:**
```markdown
## Response Approach
1. **Analyze requirements** for [specific needs]
2. **Design [solution]** with [considerations]
3. **Implement [approach]** with [quality measures]
4. **Validate [outcome]** through [methods]
5. **Optimize [result]** for [goals]
```

**Example Agents:**
- Most comprehensive agents
- Architecture and design agents

---

### DP-03: Capability Categorization

**When to use:** Agents with multiple capability areas

**Structure:**
```markdown
## Capabilities

### Category 1: [Area]
- Specific capability A
- Specific capability B

### Category 2: [Area]
- Specific capability C
- Specific capability D
```

**Example Agents:**
- `security-auditor` - 10+ capability categories
- `kubernetes-architect` - Detailed categorization

---

### DP-04: Example Interactions

**When to use:** Demonstrating agent capabilities

**Structure:**
```markdown
## Example Interactions
- "Create a [specific artifact] with [technologies]"
- "Implement [feature] with [constraints]"
- "Optimize [target] for [goals]"
- "Design [system] with [requirements]"
```

**Example Agents:**
- Most comprehensive agents
- Teaching value for users

---

### DP-05: Version and Year Awareness

**When to use:** Technology-specific agents

**Characteristics:**
- Specific version numbers (Python 3.12+, React 19)
- Year awareness (2024/2025 best practices)
- Modern tooling emphasis
- Latest features and patterns

**Example:**
```markdown
You are a Python expert specializing in modern Python 3.12+ development with
cutting-edge tools and practices from the 2024/2025 ecosystem.
```

---

### DP-06: Minimal Domain Pattern

**When to use:** Simple, focused agents (often Haiku)

**Characteristics:**
- Brief, focused description
- Minimal sections
- Direct capability listing
- No elaborate knowledge bases

**Example:**
```markdown
You are a [role] specializing in [focus].

## Focus Areas
- [Area 1]
- [Area 2]
- [Area 3]

## Approach
[Brief approach description]
```

---

## Pattern Combinations

### High-Value Opus Agent

**Combination:** MAP-01 + PP-01 + ACT-01 + DP-01 + DP-02 + DP-03 + BP-01

**Use Case:** Critical infrastructure, security, architecture

**Example:** `security-auditor`
- Opus model (MAP-01)
- Expert authority persona (PP-01)
- Proactive activation for security (ACT-01)
- Comprehensive knowledge base (DP-01)
- Structured response approach (DP-02)
- Capability categorization (DP-03)
- Quality-first behavior (BP-01)

**Cost:** Highest
**Value:** Critical decision-making

---

### Balanced Sonnet Agent

**Combination:** MAP-02 + PP-02 + ACT-02 + DP-04 + BP-05

**Use Case:** Standard development tasks, testing, debugging

**Example:** `test-automator`
- Sonnet model (MAP-02)
- Procedural specialist (PP-02)
- Standard proactive activation (ACT-02)
- Example interactions (DP-04)
- Pragmatic behavior (BP-05)

**Cost:** Mid-tier
**Value:** Most common development work

---

### Fast Haiku Agent

**Combination:** MAP-03 + PP-07 + ACT-02 + DP-06 + TIP-03

**Use Case:** Quick operations, content generation, diagrams

**Example:** `mermaid-expert`
- Haiku model (MAP-03)
- Creation specialist (PP-07)
- Proactive for visualizations (ACT-02)
- Minimal domain pattern (DP-06)
- External tool integration (TIP-03)

**Cost:** Lowest
**Value:** High-volume, speed-critical tasks

---

### Flexible Inherit Agent

**Combination:** MAP-04 + PP-03 + ACT-05 + DP-01 + BP-03

**Use Case:** User-controlled performance/cost trade-offs

**Example:** `frontend-developer`
- Inherit model (MAP-04)
- Technology stack specialist (PP-03)
- Passive activation (ACT-05)
- Comprehensive knowledge (DP-01)
- User-centric behavior (BP-03)

**Cost:** User-controlled
**Value:** Flexible optimization

---

## Anti-Patterns to Avoid

### ❌ AP-01: Model Tier Mismatch

**Problem:** Using expensive model for simple tasks or cheap model for critical work

**Example:**
- Opus for simple formatting (use Haiku instead)
- Haiku for security audit (use Opus instead)

**Fix:** Match model tier to task criticality and complexity

---

### ❌ AP-02: Vague Activation Criteria

**Problem:** Unclear when agent should activate

**Bad:**
```yaml
description: Expert in Python. Use when needed.
```

**Good:**
```yaml
description: Master Python 3.12+ expert. Use PROACTIVELY for Python development,
optimization, or advanced Python patterns.
```

**Fix:** Specify clear, actionable activation criteria

---

### ❌ AP-03: Missing Persona Definition

**Problem:** Agent lacks clear identity and expertise scope

**Bad:**
```markdown
You are helpful for code.
```

**Good:**
```markdown
You are a FastAPI expert specializing in high-performance, async-first API
development with modern Python patterns.
```

**Fix:** Define clear persona with specific expertise

---

### ❌ AP-04: Capability Overload

**Problem:** Agent tries to do everything, lacks focus

**Bad:**
- Single agent covering 10+ unrelated domains
- Kitchen sink capability list

**Fix:** Create focused agents, use agent orchestration for complex workflows

---

### ❌ AP-05: No Behavioral Traits

**Problem:** Agent lacks operational guidelines

**Fix:** Define behavioral traits for consistency

---

### ❌ AP-06: Static Technology References

**Problem:** Technology versions become outdated

**Bad:**
```markdown
Expert in React 17 and Node 12
```

**Good:**
```markdown
Expert in React 19+ and Node 20+ with modern practices from 2024/2025
```

**Fix:** Use version ranges and year awareness

---

### ❌ AP-07: Missing Related Resources

**Problem:** Agent doesn't reference complementary skills/agents

**Fix:** Include related agents and skills in frontmatter

---

### ❌ AP-08: Inconsistent Structure

**Problem:** Agents in same tier with wildly different structures

**Fix:** Follow tier-appropriate patterns consistently

---

## Using This Index

### For Creating New Agents

1. **Start with model assignment** (MAP-01 to MAP-05)
2. **Choose persona pattern** (PP-01 to PP-10)
3. **Define activation criteria** (ACT-01 to ACT-08)
4. **Add tool integrations** (TIP-01 to TIP-06)
5. **Specify behavior** (BP-01 to BP-05)
6. **Structure domain knowledge** (DP-01 to DP-06)

### For Improving Existing Agents

1. Identify current patterns
2. Check for anti-patterns
3. Add missing patterns
4. Optimize model tier
5. Clarify activation criteria

### For Understanding Agents

1. Check frontmatter for model and description
2. Identify persona pattern
3. Find activation trigger
4. Review capabilities and knowledge base
5. Understand behavioral traits

---

## Next Steps

- See **[AGENT_QUICK_START.md](AGENT_QUICK_START.md)** for step-by-step agent creation
- See **[AGENT_USE_CASE_LOOKUP.md](AGENT_USE_CASE_LOOKUP.md)** for pattern selection by use case
- See **[AGENT_QUALITY_RUBRIC.md](AGENT_QUALITY_RUBRIC.md)** for quality assessment
- See **[security_auditor.md](../../domain-agentic-resources/agents/security/security_auditor.md)** for example production agent

---

**Document Version:** 1.0
**Last Updated:** 2025-12-27
**Total Patterns:** 40
**Source Analysis:** 128 production agents across 16 categories
