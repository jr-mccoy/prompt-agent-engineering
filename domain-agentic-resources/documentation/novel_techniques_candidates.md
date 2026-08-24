# Novel Technique Candidates

---
**⚠️ IMPORTANT UPDATE (2025-12-23):**

**This file contains only Priority 1 techniques (28 of 451 total).**

**For the complete consolidation of ALL 451 novel techniques across all 7 priorities, see:**
**[NOVEL_TECHNIQUES_COMPREHENSIVE_CANDIDATES.md](novel_techniques_comprehensive_candidates.md)**

This includes:
- Priority 1: 28 techniques (Orchestration Commands) - **THIS FILE**
- Priority 2: 186 techniques (Skills with Bundled Resources)
- Priority 3: 37 techniques (Opus Agents)
- Priority 4: 69 techniques (SONNET Agents)
- Priority 5: 42 techniques (HAIKU Agents)
- Priority 6: 51 techniques (INHERIT Agents)
- Priority 7: 38 techniques (Skills without Bundled Resources)

---

# Priority 1 Only: Orchestration Commands (28 techniques)

**Date Created:** 2025-12-22
**Source Analysis:** Task 2.2 - Analysis of 7 orchestration commands
**Total Novel Techniques Identified:** 28
**Status:** Partial - See comprehensive document for all 451 techniques

---

## Executive Summary

Analysis of 7 orchestration commands from Claude Code resources revealed **28 novel prompting techniques** not documented in the existing MASTER_TECHNIQUE_INDEX.md (84 techniques). These techniques represent a significant expansion of prompting knowledge, particularly in areas of:

- **Context Management:** 6 new techniques for intelligent context handling in long-running workflows
- **Domain-Specific Development:** 11 new techniques for software development orchestration
- **Agentic Orchestration:** 4 new techniques for multi-agent coordination
- **Production AI Systems:** Techniques for staged rollout, A/B testing, and quality gates

**Key Insight:** These techniques operate at the **system-level** (coordinating agents, managing sessions, ensuring production safety) rather than the **prompt-level** (optimizing individual requests). This represents an entirely new dimension of prompting patterns.

---

## High Priority (Recommend Adding to MASTER_TECHNIQUE_INDEX)

These techniques appear frequently, solve clear problems, are generalizable beyond Claude Code, and are genuinely novel.

---

### MP-05: Extended Thinking Documentation

**Category:** Meta-Prompting (MP)

**Discovered in:** 6 of 7 orchestration commands (86% usage)

**Description:** System-level reasoning blocks that explain WHY a workflow is structured a certain way, documenting design rationale for complex multi-agent orchestrations.

**Pattern:**
```markdown
[Extended thinking: This workflow coordinates multiple specialized agents to deliver
a complete full-stack feature from architecture through deployment. It follows
API-first development principles, ensuring contract-driven development where the API
specification drives both backend implementation and frontend consumption. The
architecture-first approach prevents integration issues and enables parallel development...]
```

**Use Cases:**
- Complex multi-agent orchestration commands
- Workflows with non-obvious sequencing rationale
- Systems where understanding "why" prevents breaking "how"
- Maintainable AI workflows requiring future modifications

**Effectiveness:** Makes complex orchestration maintainable by preserving design rationale. Without this, future modifications risk breaking carefully-designed workflows.

**Generalizability:** High - applicable to any complex workflow requiring long-term maintenance

**Frequency:** 86% of analyzed orchestration commands (6 of 7)

**Novelty:** NEW - Similar to RT-01 (Chain of Thought) but for workflow design rationale, not task execution

**Proposed Code:** MP-05

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Meta-Prompting Techniques

---

### CM-05: Progressive Context Accumulation

**Category:** Context Management (CM)

**Discovered in:** 5 of 7 orchestration commands (71% usage)

**Description:** Explicit chaining of context where each workflow step's output feeds the next step's context, with transparent dependency tracking.

**Pattern:**
```markdown
### Step 1: Database Architecture Design
- Context: Initial requirements and business domain model
- Expected output: Entity relationship diagrams, table schemas

### Step 2: Backend Service Architecture
- Context: Database schema from step 1, non-functional requirements
- Expected output: API specifications, authentication flows

### Step 3: Frontend Implementation
- Context: API specifications from step 2, UI/UX requirements
- Expected output: Component architecture, routing structure
```

**Use Cases:**
- Multi-step workflows where context must build progressively without loss
- Long-running projects requiring clear information handoffs
- Orchestration with explicit dependencies between phases

**Effectiveness:** Prevents context loss in long workflows. Each agent knows exactly what information to consume from previous agents.

**Generalizability:** Very high - applicable to any multi-phase workflow

**Frequency:** 71% of orchestration commands (5 of 7)

**Novelty:** Extends CM-04 (Summary-Expand Loop) with explicit dependency tracking

**Proposed Code:** CM-05

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Context Management Techniques

---

### CM-06: Semantic Vector-Based Context Management

**Category:** Context Management (CM)

**Discovered in:** context-save-restore, context-restore commands (specialized pattern)

**Description:** Using vector embeddings and similarity search for intelligent context storage and retrieval instead of traditional key-value approaches.

**Pattern:**
```markdown
## Context Storage Strategy
1. Semantic Compression
   - Generate embeddings for context segments
   - Store in vector database (Pinecone/Weaviate/Qdrant)
   - Enable similarity-based retrieval

2. Intelligent Retrieval
   - Query with semantic similarity (not keyword matching)
   - Rank by relevance score
   - Load within token budget
```

**Implementation Example:**
```python
# Store context with semantic vectors
context_embedding = embed_text(context_segment)
vector_db.upsert(id=context_id, vector=context_embedding, metadata=context_metadata)

# Retrieve by semantic similarity
query_embedding = embed_text(current_task)
relevant_contexts = vector_db.query(query_embedding, top_k=10)
```

**Use Cases:**
- Projects with massive context (years of development history)
- Cross-project knowledge transfer
- Intelligent context recommendations based on current task
- Long-running AI workflows with selective context loading

**Effectiveness:** Enables intelligent context retrieval based on semantic relevance, not just recency or keyword matching. Critical for managing large-scale contexts.

**Generalizability:** Very high - applicable to any RAG system, long-running AI workflow, or knowledge management

**Frequency:** Specialized but critical (2 commands focused on context management)

**Novelty:** NEW - fundamentally different approach to context storage/retrieval

**Proposed Code:** CM-06

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Context Management Techniques

---

### CM-07: Token-Budget-Aware Progressive Loading

**Category:** Context Management (CM)

**Discovered in:** context-save-restore, context-restore commands

**Description:** Dynamically loading context components in priority order until token budget is exhausted, maximizing utility within API constraints.

**Pattern:**
```markdown
## Context Rehydration Strategy

1. Prioritize Components
   - Critical: Current task context, recent decisions
   - Important: Related architectural decisions, active issues
   - Useful: Historical context, related projects

2. Progressive Loading
   - Load highest priority first
   - Track token consumption
   - Stop when budget reached
   - Log what was included/excluded

3. Budget Management
   - Default: 8,192 tokens for context
   - Reserve: 50% for user conversation
   - Monitor: Token usage per component
```

**Implementation Example:**
```python
def rehydrate_context(project_context, token_budget=8192):
    prioritized_components = prioritize_components(context_components)
    restored_context = {}
    current_tokens = 0

    for component in prioritized_components:
        component_tokens = estimate_tokens(component)
        if current_tokens + component_tokens <= token_budget:
            restored_context[component] = load_component(component)
            current_tokens += component_tokens
        else:
            break  # Budget exhausted

    return restored_context, current_tokens
```

**Use Cases:**
- Long-running projects resuming from saved state
- Working with large codebases within context limits
- RAG systems with limited context windows
- Production AI systems with strict token budgets

**Effectiveness:** Directly addresses the most common production constraint - API token limits. Ensures maximum value from available context.

**Generalizability:** Very high - critical for any production AI system with token constraints

**Frequency:** Specialized but universally applicable (2 commands, but solves universal problem)

**Novelty:** NEW - practical implementation of token budget management

**Proposed Code:** CM-07

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Context Management Techniques

---

### DS-13: Architecture-First Enforcement

**Category:** Domain-Specific (DS)

**Discovered in:** full-stack-feature command

**Description:** Workflow design that enforces architectural decisions before implementation by sequencing phases and requiring specific outputs as dependencies.

**Pattern:**
```markdown
## Phase 1: Architecture & Design Foundation
### 1. Database Architecture Design
- Expected output: Entity relationship diagrams, table schemas, migration scripts

### 2. Backend Service Architecture
- Context: Database schema from step 1
- Expected output: API contracts (OpenAPI/GraphQL), authentication flows

### 3. Frontend Architecture
- Context: API contracts from step 2
- Expected output: Component architecture, routing structure

## Phase 2: Implementation (Cannot start until Phase 1 complete)
### 4. Backend Service Implementation
- Context: API specifications from Phase 1
```

**Use Cases:**
- Large features where ad-hoc development leads to integration problems
- Projects requiring API-first or contract-driven development
- Teams needing to enforce architectural discipline
- Preventing frontend-backend integration issues

**Effectiveness:** Prevents integration issues by establishing clear contracts first. Enables parallel development with clear interfaces. Forces architectural thinking upfront.

**Generalizability:** High - applicable to any complex software development project

**Frequency:** 1 command, but represents critical best practice

**Novelty:** NEW - architectural pattern enforced through workflow ordering

**Proposed Code:** DS-13

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Domain-Specific Techniques

---

### DS-19: Multi-Source Narrative Synthesis

**Category:** Domain-Specific (DS)

**Discovered in:** standup-notes command

**Description:** Combining structured data from multiple fragmented tools (Git, Jira, Calendar, Obsidian) into coherent narrative for status reporting.

**Pattern:**
```markdown
## Data Source Integration

### Primary Sources
1. **Git Commit History**
   - Extract: Commit messages, timestamps, files changed
   - Parse: Conventional commits (feat/fix/refactor)
   - Group: By feature area or epic

2. **Jira Tickets**
   - Extract: Ticket status, assignee, comments
   - Correlate: With Git commits via ticket references
   - Track: Progress and blockers

3. **Calendar Events**
   - Extract: Meetings attended, time consumed
   - Calculate: Available development time
   - Flag: Overcommitment risks

4. **Obsidian Notes / Documentation**
   - Extract: Design decisions, technical notes
   - Context: Why certain approaches taken

### Synthesis Strategy
- Correlate data across sources (commits → tickets → calendar)
- Resolve conflicts (Git says done, Jira says in progress)
- Generate unified narrative (Yesterday/Today/Blockers format)
```

**Use Cases:**
- Status reporting from fragmented tool landscape
- Team communication across technical and non-technical stakeholders
- Async team updates for distributed teams
- Standup automation

**Effectiveness:** Eliminates manual work of synthesizing information from multiple sources. Ensures comprehensive updates without missing context.

**Generalizability:** Very high - modern development uses fragmented tools everywhere

**Frequency:** 1 command, but solves universal problem

**Novelty:** NEW - systematic multi-source orchestration for narrative generation

**Proposed Code:** DS-19

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Domain-Specific Techniques

---

### AG-13: Parallel-Converge Orchestration

**Category:** Agentic (AG)

**Discovered in:** full-stack-feature command

**Description:** Explicit support for parallel agent execution with defined convergence points for synchronization and integration.

**Pattern:**
```markdown
## Phase 2: Parallel Implementation
The following tasks can run simultaneously:

### 4. Backend Service Implementation (Parallel Track A)
- Agent: python-pro / nodejs-expert / golang-pro
- Duration: Estimated 40% of total development time

### 5. Frontend Implementation (Parallel Track B)
- Agent: frontend-developer
- Duration: Estimated 40% of total development time

### 6. Database Implementation (Parallel Track C)
- Agent: database-architect
- Duration: Estimated 20% of total development time

## Coordination Notes
- Parallel tasks in Phase 2 can run simultaneously
- Must converge for Phase 3 (Integration & Testing)
- Integration point: All implementations complete with unit tests passing

## Phase 3: Integration & Testing (Convergence Required)
- All parallel tracks must complete before starting
- Integration testing validates convergence
```

**Use Cases:**
- Maximizing development velocity while maintaining integration quality
- Multi-agent systems with independent work streams
- Complex features requiring specialized expertise in parallel
- Time-sensitive projects needing concurrent development

**Effectiveness:** Maximizes development velocity while maintaining integration quality. Explicit convergence points ensure coordination.

**Generalizability:** High - applicable to any multi-agent workflow with parallelizable tasks

**Frequency:** 1 command, but fundamental orchestration pattern

**Novelty:** Extends AG-07 (Pipeline Orchestration) with parallelization

**Proposed Code:** AG-13

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Agentic Techniques

---

### AG-14: Cost-Aware Agent Orchestration

**Category:** Agentic (AG)

**Discovered in:** multi-agent-optimize command

**Description:** Strategic assignment of LLM models (Opus/Sonnet/Haiku) based on task criticality, treating cost as an explicit optimization parameter.

**Pattern:**
```markdown
## Model Assignment Strategy

### Tier 1: Opus 4.5 (Critical Decisions)
- Architecture design decisions
- Security vulnerability assessment
- Code review for production systems
- Cost: ~$15 per 1M input tokens
- Use when: Mistakes are expensive

### Tier 2: Sonnet 4.5 (Balanced Tasks)
- Complex implementation work
- Integration testing
- Documentation generation
- Cost: ~$3 per 1M input tokens
- Use when: Complexity requires reasoning but not critical

### Tier 3: Haiku 4.5 (Fast Operations)
- Syntax checking
- Code formatting
- Simple transformations
- Cost: ~$0.25 per 1M input tokens
- Use when: Speed and cost matter more than depth

### Cost Optimization Rules
- Never use Opus for tasks Haiku can handle
- Monitor cost per task, flag anomalies (>20% increase)
- Batch similar low-priority tasks for Haiku
- Use Sonnet as default, upgrade/downgrade based on results
```

**Use Cases:**
- Multi-agent systems requiring cost/performance optimization
- Production AI systems with budget constraints
- Teams needing to balance quality and cost
- High-volume AI workflows

**Effectiveness:** Optimizes cost without sacrificing quality on critical tasks. Makes cost a first-class concern in orchestration design.

**Generalizability:** High - applicable to any multi-model AI system

**Frequency:** 1 command, but critical for production systems

**Novelty:** NEW - explicit cost optimization in orchestration

**Proposed Code:** AG-14

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Agentic Techniques

---

### AG-15: Staged Rollout with Automatic Rollback

**Category:** Agentic (AG)

**Discovered in:** improve-agent command

**Description:** Progressive deployment of improved agents (Alpha 5% → Beta 20% → Canary 50% → Full 100%) with automated rollback triggers for production safety.

**Pattern:**
```markdown
## Rollout Strategy

### Stage 1: Alpha (5% of traffic)
- Duration: 24 hours
- Success criteria:
  - Success rate ≥ 95% (baseline)
  - Error rate < 2%
  - Latency < 3 seconds p95

### Stage 2: Beta (20% of traffic)
- Duration: 48 hours
- Success criteria:
  - Success rate ≥ 95%
  - Cost per task < baseline + 10%
  - User complaints < 5

### Stage 3: Canary (50% of traffic)
- Duration: 72 hours
- Success criteria:
  - Sustained performance at Beta levels
  - A/B testing shows improvement

### Stage 4: Full Rollout (100% of traffic)
- Condition: All previous stages passed
- Monitor: Continue monitoring for 7 days

## Automatic Rollback Triggers
- Success rate drops >10% from baseline → IMMEDIATE ROLLBACK
- Critical errors increase >5% → IMMEDIATE ROLLBACK
- User complaints spike (>3x baseline) → ROLLBACK WITHIN 1 HOUR
- Cost per task increases >20% → ROLLBACK WITHIN 4 HOURS
- Manual trigger → ROLLBACK IMMEDIATELY
```

**Use Cases:**
- Production AI agents serving live traffic
- High-stakes applications (healthcare, finance, legal)
- Systems where downtime is expensive
- Continuous improvement of AI systems

**Effectiveness:** Prevents catastrophic failures when deploying improved agents to production. Balances innovation with safety.

**Generalizability:** Very high - critical for any production AI system

**Frequency:** 1 command, but represents production best practice

**Novelty:** NEW - adapting software deployment patterns to AI agent improvement

**Proposed Code:** AG-15

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Agentic Techniques

---

### QA-06: Constitutional AI for Prompts

**Category:** Quality Assurance (QA)

**Discovered in:** improve-agent command

**Description:** Self-correction principles with critique-revise loops to improve prompt quality through iterative refinement.

**Pattern:**
```markdown
## Constitutional AI Improvement Loop

### Phase 1: Generate Initial Version
- Create prompt based on requirements
- Document design decisions

### Phase 2: Critique Against Principles
Evaluate against constitutional principles:
1. **Clarity**: Is every instruction unambiguous?
2. **Completeness**: Are all edge cases addressed?
3. **Consistency**: Do instructions contradict?
4. **Conciseness**: Can we remove redundancy?
5. **Correctness**: Will this achieve the goal?

For each principle:
- Rate: 1-5 scale
- Identify: Specific violations
- Explain: Why it's a problem

### Phase 3: Revise Based on Critique
- Address each identified issue
- Maintain working parts
- Generate improved version

### Phase 4: Verify Improvement
- Compare new version to old
- Confirm issues resolved
- Check for new issues introduced

### Iteration: Repeat 2-3 times minimum
```

**Use Cases:**
- Hardening prompts before production deployment
- Systematic prompt improvement
- Quality assurance for critical prompts
- Training prompt engineers

**Effectiveness:** Forces explicit quality verification and iterative refinement. Catches issues that single-pass review misses.

**Generalizability:** Very high - applicable to any prompt engineering workflow

**Frequency:** 1 command, but fundamental QA practice

**Novelty:** Extends QA-01 (Chain-of-Verification) with constitutional principles

**Proposed Code:** QA-06

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Quality Assurance Techniques

---

### QA-07: Statistical A/B Testing for Prompts

**Category:** Quality Assurance (QA)

**Discovered in:** improve-agent command

**Description:** Systematic comparison of prompt variations with statistical validation to measure improvement objectively.

**Pattern:**
```markdown
## A/B Testing Framework

### Test Design
- **Variant A (Control)**: Current prompt version
- **Variant B (Treatment)**: Improved prompt version
- **Sample Size**: Minimum 100 tasks per variant (p < 0.05 significance)
- **Randomization**: 50/50 split, randomized assignment
- **Duration**: Until statistical significance achieved

### Success Metrics
1. **Primary Metric**: Task success rate
   - Definition: Task completed correctly without errors
   - Baseline: Current success rate
   - Goal: >5% improvement (absolute)

2. **Secondary Metrics**:
   - Response quality (1-5 rating by human evaluator)
   - Time to completion
   - Cost per task
   - User satisfaction (if applicable)

### Statistical Analysis
- Calculate: Mean, standard deviation, confidence intervals
- Test: Two-proportion z-test for success rate
- Require: p < 0.05 for significance
- Effect size: Cohen's h ≥ 0.2 (small effect)

### Decision Rules
- IF p < 0.05 AND improvement ≥ 5% → DEPLOY
- IF p < 0.05 AND improvement < 5% → NEEDS WORK
- IF p ≥ 0.05 → NO SIGNIFICANT DIFFERENCE, continue testing or abandon

### Guardrails
- Stop if success rate drops >10% (safety check)
- Stop if cost increases >20% without success improvement
- Minimum 100 samples per variant (avoid false positives)
```

**Use Cases:**
- Validating prompt improvements objectively
- Comparing multiple prompt strategies
- Production AI systems requiring data-driven decisions
- Continuous improvement workflows

**Effectiveness:** Provides objective, statistical validation of improvements. Prevents subjective bias and overconfidence.

**Generalizability:** Very high - applicable to any AI system optimization

**Frequency:** 1 command, but critical for data-driven improvement

**Novelty:** NEW - applying rigorous statistical testing to prompt engineering

**Proposed Code:** QA-07

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Quality Assurance Techniques

---

### NE-13: Technical-to-Business Translation

**Category:** Non-Engineering (NE)

**Discovered in:** standup-notes command

**Description:** AI-powered conversion of technical commit messages and implementation details into business value statements for non-technical stakeholders.

**Pattern:**
```markdown
## Translation Strategy

### Step 1: Extract Technical Information
- Commit messages (conventional commits format)
- Code changes (files modified, lines changed)
- Ticket references (JIRA-123, GitHub #456)
- Technical details (API endpoints, database changes)

### Step 2: Identify Business Context
- Which feature or epic does this support?
- What user problem does this solve?
- What business capability does this enable?
- What risk does this mitigate?

### Step 3: Transform to Business Language

**Technical:**
```
feat: Add OAuth2 authentication flow
- Implemented token refresh endpoint
- Added JWT validation middleware
- Updated user schema with refresh_token column
```

**Business Translation:**
```
✅ Implemented secure user authentication
- Users can now safely sign in and stay logged in across sessions
- Reduces security risk and improves user experience
- Enables upcoming social media integration features
```

### Translation Principles
- Focus on user value, not implementation details
- Explain "what" and "why", minimize "how"
- Use business metrics (user experience, revenue, risk) not technical metrics
- Make blockers actionable for non-technical decision makers
```

**Use Cases:**
- Team communication across technical and non-technical stakeholders
- Executive status reporting
- Product management updates
- Client-facing progress reports

**Effectiveness:** Makes technical work accessible to non-technical stakeholders. Builds shared understanding across teams.

**Generalizability:** Very high - every organization needs technical-business translation

**Frequency:** 1 command, but addresses universal communication challenge

**Novelty:** NEW - systematic AI-powered domain translation

**Proposed Code:** NE-13

**Integration:** Add to MASTER_TECHNIQUE_INDEX under Non-Engineering Techniques

---

## Medium Priority (Consider Adding)

These techniques are valuable but either less frequent, more specialized, or overlapping with existing techniques.

---

### CM-08: Context Fingerprinting and Drift Detection

**Category:** Context Management (CM)

**Discovered in:** context-save-restore command

**Description:** Generating unique identifiers for context versions and detecting when context has drifted from expected state.

**Pattern:**
```markdown
## Context Versioning Strategy

### Fingerprint Generation
- Hash all context components (SHA-256)
- Include: Code state, decisions, dependencies, configuration
- Generate: Unique fingerprint per save
- Store: Fingerprint with timestamp and metadata

### Drift Detection
- Compare: Current state vs. last saved fingerprint
- Identify: Changed components (added, modified, deleted)
- Assess: Severity (breaking vs. non-breaking changes)
- Alert: If drift exceeds threshold

### Semantic Diff
- Beyond file changes: Understand semantic meaning
- Detect: API contract changes, dependency updates, config changes
- Classify: Compatible vs. incompatible drift
```

**Use Cases:**
- Multi-session projects where context consistency is critical
- Team collaboration on shared AI contexts
- Detecting unexpected changes to project state

**Effectiveness:** Tracks context evolution and detects inconsistencies. Critical for long-running collaborative projects.

**Generalizability:** Medium-High - useful for any persistent context system

**Frequency:** 1 command (specialized context management)

**Novelty:** NEW - version control applied to AI context

**Proposed Code:** CM-08

**Rationale for Medium Priority:** Specialized for advanced context management scenarios

---

### CM-09: Knowledge Graph Context Representation

**Category:** Context Management (CM)

**Discovered in:** context-save-restore command

**Description:** Representing context as knowledge graph with ontological relationships instead of flat structures.

**Pattern:**
```markdown
## Knowledge Graph Structure

### Entities
- **Concepts**: Classes, functions, modules, services
- **Decisions**: Architectural choices, trade-offs
- **Dependencies**: Libraries, APIs, services
- **People**: Authors, reviewers, stakeholders

### Relationships
- **depends_on**: Component A depends on Component B
- **implements**: Code implements Architecture Decision
- **replaces**: New approach replaces old approach
- **conflicts_with**: Decision conflicts with constraint

### Graph Operations
- **Traversal**: Find all dependencies of component X
- **Inference**: If A depends on B, and B deprecated, then A at risk
- **Query**: "Show all architectural decisions affecting authentication"
```

**Use Cases:**
- Complex domains with rich entity relationships
- Projects requiring impact analysis
- Systems needing inference capabilities

**Effectiveness:** Enables inference and relationship discovery. More powerful than flat context for complex domains.

**Generalizability:** Medium - requires sophisticated context management needs

**Frequency:** 1 command (specialized approach)

**Novelty:** NEW - graph-based context representation

**Proposed Code:** CM-09

**Rationale for Medium Priority:** Advanced technique requiring specialized infrastructure

---

### CM-10: Composite Relevance Scoring

**Category:** Context Management (CM)

**Discovered in:** context-restore command

**Description:** Multi-dimensional ranking using semantic similarity, temporal relevance, and historical impact for intelligent context prioritization.

**Pattern:**
```python
def calculate_relevance_score(context_item, current_task):
    # Semantic relevance (40% weight)
    semantic_score = cosine_similarity(
        embed(context_item.content),
        embed(current_task.description)
    ) * 0.4

    # Temporal relevance (30% weight)
    age_days = (now - context_item.timestamp).days
    temporal_score = exp(-age_days / 30) * 0.3  # Decay over 30 days

    # Historical impact (30% weight)
    impact_score = context_item.reference_count * 0.3

    # Composite score
    total_score = semantic_score + temporal_score + impact_score
    return total_score
```

**Use Cases:**
- Intelligent context retrieval with multiple factors
- Balancing recency with relevance
- Long-running projects with large context stores

**Effectiveness:** More sophisticated than single-dimension ranking (recency only or similarity only).

**Generalizability:** High - applicable to any context retrieval system

**Frequency:** 1 command (but represents best practice)

**Novelty:** NEW - multi-factor context ranking

**Proposed Code:** CM-10

**Rationale for Medium Priority:** Advanced optimization over simpler approaches

---

### DS-14: Layer-Specific Agent Specialization

**Category:** Domain-Specific (DS)

**Discovered in:** multi-agent-optimize command

**Description:** Assigning specialized agents by architectural layer (Database, Application, Frontend) rather than by technology or feature.

**Pattern:**
```markdown
## Layer-Based Agent Assignment

### Database Layer
- Agent: database-architect
- Responsibilities: Schema design, query optimization, indexing, migrations
- Optimizes: Data access patterns, join performance, storage efficiency

### Application Layer
- Agent: backend-architect, python-pro, nodejs-expert
- Responsibilities: Business logic, API design, service architecture
- Optimizes: Code structure, algorithm efficiency, resource usage

### Frontend Layer
- Agent: frontend-developer, react-specialist
- Responsibilities: UI components, state management, rendering
- Optimizes: Bundle size, rendering performance, user experience
```

**Use Cases:**
- Full-stack optimization requiring layer-specific expertise
- Performance tuning across architectural boundaries
- Systems with clear separation of concerns

**Effectiveness:** Ensures right expert handles each layer. Prevents frontend developer optimizing database or vice versa.

**Generalizability:** Medium-High - applicable to layered architectures

**Frequency:** 1 command

**Novelty:** NEW - layer-based vs. technology-based specialization

**Proposed Code:** DS-14

**Rationale for Medium Priority:** Specialized application to specific architecture patterns

---

### DS-15: Code Archaeology as Investigation

**Category:** Domain-Specific (DS)

**Discovered in:** issue (GitHub) command

**Description:** Using git history analysis (git bisect, git blame, commit history) as systematic debugging and root cause analysis technique.

**Pattern:**
```markdown
## Code Archaeology Process

### Phase 1: Identify Affected Code
- Use git blame to find when code was last modified
- Identify: Author, timestamp, commit message

### Phase 2: Bisect to Find Introduction
- Use git bisect to find commit that introduced bug
- Binary search through commits
- Test each commit: good vs. bad

### Phase 3: Analyze Context
- Review commit: What was being changed and why?
- Check ticket references: What feature/fix was this?
- Read commit message: What was the intent?

### Phase 4: Trace Dependencies
- Find related commits (same files, same author, same timeframe)
- Identify patterns (was this rushed? incomplete?)
- Assess impact (what else might be affected?)
```

**Use Cases:**
- Debugging issues with unclear root cause
- Understanding "how did we get here"
- Learning from past mistakes
- Code review with historical context

**Effectiveness:** Systematic approach to debugging using version control. More rigorous than ad-hoc investigation.

**Generalizability:** High - applicable to any Git-based project

**Frequency:** 1 command (but represents fundamental debugging practice)

**Novelty:** NEW - formal technique for git-based investigation

**Proposed Code:** DS-15

**Rationale for Medium Priority:** Valuable but overlaps with existing debugging practices

---

### DS-16: Issue-to-PR Complete Lifecycle

**Category:** Domain-Specific (DS)

**Discovered in:** issue (GitHub) command

**Description:** End-to-end workflow orchestration from GitHub issue creation through implementation, testing, review, and deployment with full traceability.

**Pattern:**
```markdown
## Complete Lifecycle Workflow

### Stage 1: Issue Analysis
- Parse issue description
- Identify requirements
- Ask clarifying questions
- Document acceptance criteria

### Stage 2: Planning
- Create implementation plan
- Identify affected files
- Estimate complexity
- Create branch (feat/ISSUE-123-description)

### Stage 3: Implementation
- Write code following plan
- Include issue reference in commits (Fixes #123)
- Write tests
- Update documentation

### Stage 4: Quality Gates
- Run tests (all must pass)
- Security scan (no critical issues)
- Code review (approval required)

### Stage 5: Pull Request
- Create PR with issue link
- Include: Description, test plan, screenshots
- Request review from relevant stakeholders

### Stage 6: Deployment
- Merge PR
- Deploy to staging
- Verify fix in production
- Close issue with resolution comment

### Traceability
- Issue → Branch → Commits → PR → Deployment
- Every code change links back to business requirement
```

**Use Cases:**
- Teams requiring audit trails
- Enterprise development with compliance requirements
- Open source projects needing contribution tracking

**Effectiveness:** Provides complete traceability from requirement to deployment. Ensures accountability and compliance.

**Generalizability:** High - applicable to any GitHub-based workflow

**Frequency:** 1 command

**Novelty:** NEW - complete lifecycle orchestration with traceability

**Proposed Code:** DS-16

**Rationale for Medium Priority:** Valuable workflow but process-specific

---

### DS-17: Embedded Tool Integration Patterns

**Category:** Domain-Specific (DS)

**Discovered in:** issue (GitHub) command

**Description:** Including exact CLI commands and tool invocations within workflow steps for repeatable execution.

**Pattern:**
```markdown
### Step 3: Run Security Scan
Execute the following command:
```bash
npm audit --audit-level=high
```

Expected output: No high or critical vulnerabilities

If vulnerabilities found:
```bash
npm audit fix
# Review changes
git diff package-lock.json
```

### Step 5: Create Pull Request
Execute the following command:
```bash
gh pr create \
  --title "Fix: Security vulnerabilities in dependencies" \
  --body "$(cat <<'EOF'
## Summary
Fixed 3 high-severity vulnerabilities in dependencies

## Changes
- Updated lodash to 4.17.21
- Updated axios to 1.6.0

## Testing
- All unit tests passing
- Security scan clean
EOF
)"
```
```

**Use Cases:**
- Repeatable workflows requiring exact tool usage
- Documentation that doubles as executable instructions
- Teams standardizing on specific tools and parameters

**Effectiveness:** Eliminates ambiguity about tool usage. Ensures consistency across executions.

**Generalizability:** High - applicable to any tool-based workflow

**Frequency:** 1 command

**Novelty:** Extends DS-03 (Tool Suggestions) with exact invocations

**Proposed Code:** DS-17

**Rationale for Medium Priority:** Useful enhancement but incremental improvement

---

### DS-18: Branch Naming Convention Enforcement

**Category:** Domain-Specific (DS)

**Discovered in:** issue (GitHub) command

**Description:** Enforcing standardized git branch naming patterns through workflow instructions.

**Pattern:**
```markdown
## Branch Naming Convention

### Format: `{type}/{issue-number}-{short-description}`

### Types:
- `feat/` - New feature
- `fix/` - Bug fix
- `refactor/` - Code refactoring
- `docs/` - Documentation changes
- `test/` - Test additions or changes
- `chore/` - Build/tooling changes

### Examples:
- `feat/123-user-authentication`
- `fix/456-memory-leak-in-upload`
- `refactor/789-extract-payment-service`

### Validation:
- Issue number required (except chore)
- Description: lowercase, hyphen-separated, max 50 chars
- Type must match commit type
```

**Use Cases:**
- Teams needing Git workflow standardization
- Projects with many contributors
- Automation relying on branch naming patterns

**Effectiveness:** Improves organization and enables automation based on branch names.

**Generalizability:** High - applicable to any Git-based team

**Frequency:** 1 command

**Novelty:** NEW - systematic branch naming enforcement

**Proposed Code:** DS-18

**Rationale for Medium Priority:** Organizational practice, not prompting innovation

---

### DS-20: Structured Blocker Escalation

**Category:** Domain-Specific (DS)

**Discovered in:** standup-notes command

**Description:** Formalized blocker communication with Impact/Need/From/Tried/Next fields for actionable escalation.

**Pattern:**
```markdown
## Blocker Report Format

**[SEVERITY]** [Brief Description]

- **Impact:** What is stopped or at risk?
- **Need:** What specific help or decision is required?
- **From:** Who can unblock this? (@person or @team)
- **Tried:** What solutions have been attempted?
- **Next Step:** What happens if not resolved by [date]?

### Example:

**[CRITICAL]** API authentication failing in production

- **Impact:** 100% of API requests failing, revenue stopped
- **Need:** Production database credentials for new auth service
- **From:** @platform-team or @security-team
- **Tried:** Used staging credentials (rejected), contacted on-call (no response)
- **Next Step:** Rollback to old auth if not resolved by 3pm EST

### Severity Levels:
- **[CRITICAL]** - Immediate impact, blocks all progress
- **[HIGH]** - Blocks primary work, workaround possible
- **[MEDIUM]** - Blocks secondary work, can work around
- **[LOW]** - Informational, no immediate block
```

**Use Cases:**
- Distributed teams needing clear blocker communication
- Async workflows requiring actionable escalation
- Teams with multiple stakeholders

**Effectiveness:** Makes blockers actionable with clear ownership. Enables async decision-making.

**Generalizability:** Very high - universal team communication challenge

**Frequency:** 1 command

**Novelty:** NEW - systematic blocker communication framework

**Proposed Code:** DS-20

**Rationale for Medium Priority:** Valuable communication pattern, but process-oriented

---

### DS-21: Automated Task Derivation

**Category:** Domain-Specific (DS)

**Discovered in:** standup-notes command

**Description:** Extracting actionable tasks from narrative content (standup notes, meeting notes, commit messages).

**Pattern:**
```markdown
## Task Extraction Process

### Step 1: Parse Narrative
- Standup notes, meeting notes, commit messages
- Identify: Commitments, blockers, dependencies, deliverables

### Step 2: Extract Tasks

**From Commitments:**
"Today: Complete user authentication"
→ Task: "Implement user authentication" (Due: end of day)

**From Blockers:**
"Blocked: Need API credentials from @platform-team"
→ Task: "Request API credentials from @platform-team" (High priority)

**From Dependencies:**
"Waiting on: Design mockups from @design-team"
→ Task: "Follow up with @design-team on mockups" (Check-in task)

### Step 3: Structure Tasks
- **Title:** Action-oriented (verb + object)
- **Assignee:** Extracted from context
- **Due Date:** Derived from commitments
- **Priority:** Based on blocker severity
- **Type:** Action, Reminder, Waiting On

### Step 4: Create Tracking Items
- Add to task management system (Jira, Linear, etc.)
- Link to source (standup note, meeting)
- Set reminders based on due dates
```

**Use Cases:**
- Converting communication into trackable work items
- Ensuring standup commitments become tracked tasks
- Reducing manual task creation overhead

**Effectiveness:** Ensures commitments translate to action items. Reduces manual overhead.

**Generalizability:** High - applicable to any team communication

**Frequency:** 1 command

**Novelty:** NEW - automated task generation from narrative

**Proposed Code:** DS-21

**Rationale for Medium Priority:** Automation enhancement, depends on tool integration

---

### DS-22: Cross-Project Knowledge Transfer

**Category:** Domain-Specific (DS)

**Discovered in:** context-restore command

**Description:** Extracting learned patterns from one project and adapting them to another via semantic vector mapping.

**Pattern:**
```markdown
## Knowledge Transfer Process

### Phase 1: Extract Patterns from Source Project
- Identify: Successful patterns, lessons learned, anti-patterns avoided
- Encode: As semantic vectors (patterns, contexts, outcomes)
- Store: In knowledge base with metadata

### Phase 2: Analyze Target Project
- Identify: Current challenges, architecture, constraints
- Encode: As semantic vectors
- Map: Target needs to source patterns

### Phase 3: Find Relevant Patterns
- Semantic search: Query target project needs against source patterns
- Rank: By relevance score (semantic + domain similarity)
- Filter: By applicability (compatible architectures, languages)

### Phase 4: Adapt and Apply
- Translate: Source pattern to target context
- Adapt: For technology stack, scale, constraints
- Validate: Compatibility with target project

### Example:
**Source Project:** E-commerce platform (Node.js, MongoDB)
**Learned Pattern:** "Rate limiting with Redis prevents API abuse"

**Target Project:** SaaS analytics platform (Python, PostgreSQL)
**Adapted Pattern:** "Rate limiting with Redis + PostgreSQL (user tier limits)"
**Adjustments:** Added tier-based limits, integrated with PostgreSQL for persistence
```

**Use Cases:**
- Organizations with multiple projects
- Teams learning from past experiences
- Consultants applying patterns across clients

**Effectiveness:** Systematizes organizational learning. Prevents reinventing solutions.

**Generalizability:** Medium-High - requires mature tooling and processes

**Frequency:** 1 command (specialized knowledge management)

**Novelty:** NEW - semantic vector-based knowledge transfer

**Proposed Code:** DS-22

**Rationale for Medium Priority:** Advanced technique requiring organizational maturity

---

### AG-16: Continuous Improvement Cycle

**Category:** Agentic (AG)

**Discovered in:** improve-agent command

**Description:** Formalized cadence for ongoing agent optimization with feedback collection, analysis, and iteration.

**Pattern:**
```markdown
## Continuous Improvement Framework

### Phase 1: Baseline Measurement (Week 1)
- Collect: Success rate, quality scores, cost per task
- Establish: Current performance baseline
- Identify: Top 3 improvement opportunities

### Phase 2: Hypothesis Generation (Week 2)
- Propose: Specific improvements (prompt changes, model upgrades)
- Predict: Expected impact on metrics
- Plan: A/B test design

### Phase 3: Experimentation (Weeks 3-4)
- Run: A/B tests with statistical rigor
- Collect: Data on treatment vs. control
- Monitor: For regressions or issues

### Phase 4: Analysis and Decision (Week 5)
- Analyze: Statistical significance of results
- Decide: Deploy, iterate, or abandon
- Document: Learnings for future iterations

### Phase 5: Deployment (Week 6)
- Deploy: Using staged rollout (AG-15)
- Monitor: Production performance
- Update: Baseline for next cycle

### Cycle: Repeat every 6 weeks
```

**Use Cases:**
- Production AI systems requiring ongoing improvement
- Teams committed to data-driven optimization
- Long-running AI agents needing evolution

**Effectiveness:** Prevents stagnation. Ensures systematic improvement over time.

**Generalizability:** High - applicable to any production AI system

**Frequency:** 1 command

**Novelty:** NEW - formalized improvement cadence for AI agents

**Proposed Code:** AG-16

**Rationale for Medium Priority:** Process framework, not prompting technique per se

---

### IT-14: Configuration-Driven Orchestration

**Category:** Interaction Techniques (IT)

**Discovered in:** full-stack-feature command

**Description:** Single workflow with configuration parameters for variations, avoiding duplication.

**Pattern:**
```markdown
## Configuration Options

### Required Configuration
**stack**: Technology stack selection
- Options: "React/FastAPI/PostgreSQL", "Vue/Django/MySQL", "Angular/NestJS/MongoDB"
- Effect: Determines which specialized agents to use

**deployment_target**: Cloud platform
- Options: "AWS", "GCP", "Azure"
- Effect: Tailors infrastructure and deployment agents

### Optional Configuration
**testing_depth**: Testing thoroughness
- Options: "comprehensive" (unit + integration + e2e), "essential" (unit + smoke)
- Default: "comprehensive"

**compliance**: Regulatory requirements
- Options: "GDPR", "HIPAA", "SOC2", "none"
- Effect: Adds compliance validation steps

### Configuration Usage
```markdown
User provides:
- stack: "React/FastAPI/PostgreSQL"
- deployment_target: "AWS"
- testing_depth: "comprehensive"
- compliance: "HIPAA"

Workflow automatically:
- Uses: react-specialist, python-pro, database-architect (PostgreSQL)
- Configures: AWS-specific deployment agent
- Includes: Comprehensive test suite
- Adds: HIPAA compliance validation phase
```
```

**Use Cases:**
- Workflows applicable to multiple tech stacks
- Reducing maintenance burden (one workflow, many configurations)
- Standardizing processes across variations

**Effectiveness:** Single workflow handles multiple scenarios without duplication. Reduces maintenance burden.

**Generalizability:** High - applicable to any parameterizable workflow

**Frequency:** 1 command

**Novelty:** NEW - DRY principle applied to orchestration workflows

**Proposed Code:** IT-14

**Rationale for Medium Priority:** Engineering best practice, incremental innovation

---

### IT-15: Dynamic Context Expansion with Lazy Loading

**Category:** Interaction Techniques (IT)

**Discovered in:** context-restore command

**Description:** Starting with minimal context and progressively expanding based on runtime requests and needs.

**Pattern:**
```markdown
## Lazy Loading Strategy

### Initial Load (Minimal Context)
- Project name and type
- Current task description
- Essential dependencies (20% of full context)

### Progressive Expansion Triggers

**User asks about architecture:**
→ Load: Architectural decision records, system diagrams

**User asks about specific module:**
→ Load: Module code, related tests, recent changes

**Error occurs:**
→ Load: Error logs, related debugging history

### Context Priority Tiers

**Tier 1 (Always Loaded):**
- Current task and goals
- Active issues and blockers
- Recent critical decisions

**Tier 2 (Load on Request):**
- Historical context
- Full codebase documentation
- Detailed architectural decisions

**Tier 3 (Load on Demand):**
- Git history
- Old design documents
- Archived discussions

### Memory Management
- Track: What context is currently loaded
- Evict: Least recently used when approaching limits
- Reload: On-demand when needed again
```

**Use Cases:**
- Working within token budgets
- Large projects with extensive context
- Interactive sessions where needs evolve

**Effectiveness:** Optimizes token usage by loading only what's needed. Adapts to user's current focus.

**Generalizability:** High - applicable to any large-context scenario

**Frequency:** 1 command

**Novelty:** Extends CM-07 (Token Budget) with runtime adaptability

**Proposed Code:** IT-15

**Rationale for Medium Priority:** Advanced optimization technique

---

### NE-14: Async-First Communication Design

**Category:** Non-Engineering (NE)

**Discovered in:** standup-notes command

**Description:** Designing communication artifacts specifically for asynchronous consumption across timezones.

**Pattern:**
```markdown
## Async-First Principles

### 1. Complete Context in Every Message
- No references to "we discussed earlier"
- Include all relevant links and context
- Assume reader wasn't in real-time discussion

### 2. Explicit Next Steps
- Clear action items with owners
- Deadlines in multiple timezones (EST/PST/UTC/etc.)
- What happens if no response by deadline

### 3. Scannable Structure
- Use: Clear headers, bullet points, bold for key info
- Avoid: Long paragraphs, buried action items
- Highlight: Blockers, deadlines, decisions needed

### 4. Threaded Discussions
- Use: Comment threads for discussions
- Avoid: Email chains that exclude people
- Enable: People to catch up asynchronously

### 5. Consistent Timing
- Post: At same time each day/week
- Across: Multiple timezones (rotating if needed)
- Predictable: Team knows when to check

### Example: Async Standup
**Posted:** Every day at 9am EST / 2pm UTC / 9:30pm IST

## Yesterday (2024-01-15)
• [COMPLETED] Implemented OAuth2 authentication - [PR #123](link)
• [COMPLETED] Fixed memory leak in upload service - [PR #124](link)

## Today (2024-01-16)
• [IN PROGRESS] Integration testing for auth flow - Expect completion by EOD EST
• [STARTING] Performance optimization for search API

## Blockers
**[HIGH]** Need production database credentials for auth service
- **Impact:** Can't deploy auth to production
- **Need:** Credentials from @platform-team
- **Deadline:** Jan 17, 9am EST (if not resolved, will rollback)

**Questions?** Reply in thread below (will check at 3pm EST and 9am EST next day)
```

**Use Cases:**
- Global distributed teams across timezones
- Remote-first organizations
- Teams with flexible schedules

**Effectiveness:** Enables effective collaboration without requiring synchronous meetings.

**Generalizability:** Very high - increasingly important for distributed work

**Frequency:** 1 command

**Novelty:** NEW - systematic async communication principles

**Proposed Code:** NE-14

**Rationale for Medium Priority:** Communication best practice, process-oriented

---

## Low Priority (Document but Don't Add Yet)

These techniques are valuable in specific contexts but too specialized, overlapping, or implementation-specific for general technique index.

---

### OT-06: Multi-Format Context Serialization

**Category:** Output Techniques (OT)

**Discovered in:** context-save-restore command

**Description:** Supporting multiple serialization formats (JSON, Markdown, Protocol Buffers, YAML, MessagePack) for different use cases.

**Rationale for Low Priority:** Implementation detail rather than prompting technique. Storage format choice doesn't change prompting approach.

---

## Summary Statistics

### By Priority
- **High Priority:** 13 techniques (recommended for immediate integration)
- **Medium Priority:** 14 techniques (valuable but specialized)
- **Low Priority:** 1 technique (document but don't add to index)

### By Category
- **Context Management (CM):** 6 techniques (CM-05 through CM-10)
- **Domain-Specific (DS):** 11 techniques (DS-13 through DS-22, with gaps for future)
- **Agentic (AG):** 4 techniques (AG-13 through AG-16)
- **Meta-Prompting (MP):** 1 technique (MP-05)
- **Interaction Techniques (IT):** 2 techniques (IT-14, IT-15)
- **Quality Assurance (QA):** 2 techniques (QA-06, QA-07)
- **Non-Engineering (NE):** 2 techniques (NE-13, NE-14)
- **Output Techniques (OT):** 1 technique (OT-06)

### By Generalizability
- **Very High:** 10 techniques (applicable to most AI systems)
- **High:** 13 techniques (applicable to many scenarios)
- **Medium-High:** 4 techniques (applicable to specific domains)
- **Medium:** 1 technique (specialized applications)

---

## Integration Recommendations

### Immediate Actions (High Priority)

1. **Add 13 high-priority techniques to MASTER_TECHNIQUE_INDEX.md**
   - MP-05: Extended Thinking Documentation
   - CM-05: Progressive Context Accumulation
   - CM-06: Semantic Vector-Based Context Management
   - CM-07: Token-Budget-Aware Progressive Loading
   - DS-13: Architecture-First Enforcement
   - DS-19: Multi-Source Narrative Synthesis
   - AG-13: Parallel-Converge Orchestration
   - AG-14: Cost-Aware Agent Orchestration
   - AG-15: Staged Rollout with Automatic Rollback
   - QA-06: Constitutional AI for Prompts
   - QA-07: Statistical A/B Testing for Prompts
   - NE-13: Technical-to-Business Translation

2. **Update technique count**
   - Current: 84 techniques
   - After integration: 97 techniques (13 high-priority additions)

3. **Create new section or expand existing**
   - Option A: Create "Orchestration Techniques" category
   - Option B: Significantly expand AG (Agentic) category
   - Recommendation: Expand AG category, as most orchestration techniques fit there

### Future Actions (Medium Priority)

4. **Consider adding 14 medium-priority techniques** after validating with more resource analysis
   - Wait for Priority 2 analysis (skills with bundled resources)
   - Wait for Priority 3 analysis (Opus 4.5 agents)
   - Validate frequency and applicability before adding

### Documentation Updates

5. **Update AI_AGENT_QUICK_START.md**
   - Add section on orchestration commands as advanced pattern
   - Reference new techniques when appropriate

6. **Update USE_CASE_LOOKUP.md**
   - Add use cases: Multi-agent orchestration, Production AI deployment, Context management for long workflows
   - Reference new techniques in relevant use case sections

7. **Create specialized guides**
   - "Building Multi-Agent Orchestration Commands" (using MP-05, AG-13, CM-05)
   - "Production AI Deployment Patterns" (using AG-15, QA-07, AG-14)

---

## Next Steps for Task 3.2

**Task 3.2:** Write detailed technique documentation for each high-priority novel technique

For each of the 13 high-priority techniques, create comprehensive documentation:

**File:** `prompt-techniques/new-techniques/[TECHNIQUE-CODE].md`

**Required Sections:**
1. Technique Name & Code
2. Category
3. Description (2-3 sentences)
4. When to Use (specific scenarios)
5. Pattern (structural template)
6. Example (complete, working example)
7. Variations (different applications)
8. Combination Patterns (works well with...)
9. Pitfalls (common mistakes)
10. Real-World Usage (references to Claude Code resources using it)

**Estimated Time:** 10-15 hours (1 hour per technique × 13 techniques)

---

**End of Novel Techniques Candidates Document**
