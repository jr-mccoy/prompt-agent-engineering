# Repository Review & Reflection Prompt

## Purpose
A comprehensive self-reflective analysis prompt for AI agents to evaluate the **Prompting-Guides** repository. Use this prompt to identify improvements, gaps, inconsistencies, and opportunities across the repository's 1200+ prompts and extensive coding agent resources.

## Target Audience
- **AI coding agents** (Claude Code, Cursor, GitHub Copilot) performing repository maintenance
- **Repository maintainers** seeking systematic improvement analysis
- **Contributors** wanting to understand where help is most needed

---

## Repository Context

### Current Scale (2026)
| Resource Type | Count | Location |
|---------------|-------|----------|
| Total Prompts | 1200+ | `domain-*/` directories |
| Prompt Engineering Techniques | 242 | `techniques/` |
| Agent Skills | 138 | `domain-agentic-resources/skills/` |
| Task-Specific Agents | 134 | `domain-agentic-resources/agents/` |
| Multi-Agent Commands | 73 | `domain-agentic-resources/commands/` |
| Pipeline Personas | 53 | `domain-agentic-resources/personas/` |
| Skill-Building Patterns | 41 | `authoring/skill-patterns/` |
| Domain Directories | 20 | Root level |

### Directory Structure Overview
```
prompting-guides/
├── domain-software-engineering/    # Code analysis, testing, DevOps, cloud, API, mobile (~206)
├── domain-agentic-resources/       # Skills, agents, commands, personas (~575)
├── domain-business-strategy/       # Business analysis & strategy (~109)
├── domain-engineering-workflows/   # Project management & workflows (~77)
├── domain-productivity/            # Productivity & validation (~98)
├── domain-image-generation/        # Image generation prompts (~110)
├── domain-presentations/           # Board decks & presentations (~48)
├── domain-prompt-engineering/      # Meta-prompts about prompts (~22)
├── domain-decision-making/         # Decision frameworks (~19)
├── domain-advertising/             # Industry-specific advertising (~18)
├── domain-professional-writing/    # Professional domain guides (~44)
├── domain-professional-communication/ # PRDs, stakeholder updates (~29)
├── domain-personal-development/    # Goals, habits, career (~26)
├── domain-healthcare-clinical/     # Clinical decision support (~17)
├── domain-learning-coding/         # Coding education (~17)
├── domain-research-academic/       # Literature review, methodology (~14)
├── domain-conversation-practice/   # Language conversation practice (~9)
├── domain-creative-writing/        # Fiction, essays, narrative
├── domain-education-teaching/      # Lesson plans, worksheets, assessments
├── domain-specialized-fields/      # Legal, finance, trades, real estate
├── techniques/                     # Prompt engineering reference (242 techniques)
├── authoring/                      # Resource creation guides (skills, agents, commands)
└── _archive/                       # Deprecated content
```

### Key Reference Files
| File | Purpose |
|------|---------|
| `CLAUDE.md` | Primary AI agent guide with decision trees and mappings |
| `AI_AGENT_QUICK_START.md` | 5-step process for building coding prompts |
| `NON_CODING_QUICK_START.md` | Guide for non-coding prompts (education, healthcare, etc.) |
| `PROMPT_QUALITY_STANDARDS.md` | Quality tiers and false-positive prevention patterns |
| `domain-image-generation/IMAGE_GENERATION_GUIDE.md` | 8 core techniques for image generation |
| `techniques/MASTER_TECHNIQUE_INDEX.md` | Complete catalog of 242 techniques |
| `techniques/USE_CASE_LOOKUP.md` | Task-to-technique mapping |
| `authoring/skill-patterns/SKILL_PATTERN_INDEX.md` | Skill authoring system |
| `authoring/agent-patterns/AGENT_QUICK_START.md` | Agent authoring patterns |
| `authoring/command-patterns/COMMAND_QUICK_START.md` | Command authoring patterns |

---

## Analysis Framework

### Phase 1: Structural Integrity Analysis

#### 1.1 Directory Organization
Evaluate the `domain-*` structure:

- **Consistency**: Do all domain directories follow the same organizational patterns?
- **Completeness**: Are there logical domains missing from the structure?
- **Balance**: Are some domains over/under-represented relative to their importance?
- **Depth**: Is subdirectory nesting appropriate and consistent?
- **Orphans**: Are there prompts that don't fit well in their current location?

**Check specifically:**
```
- Does each domain-* directory have a README.md?
- Are subdirectory structures parallel across similar domains?
- Is the _archive/ being used appropriately for deprecated content?
```

#### 1.2 Naming Convention Audit
Assess file naming across all directories:

- **Pattern adherence**: Do files follow `{category}_{specific_function}.md` convention?
- **Predictability**: Can users guess file names based on content?
- **Collision avoidance**: Are names unique enough to prevent confusion?
- **Searchability**: Do names contain keywords users would search for?

**Sample audit approach:**
```
1. List 20 random files from different domains
2. Assess naming consistency
3. Identify outliers or inconsistencies
4. Propose standardization where needed
```

#### 1.3 Cross-Reference Integrity
Verify internal linking:

- **Broken links**: Check for references to moved/deleted files
- **Missing links**: Identify prompts that should reference related content but don't
- **Circular references**: Detect unhelpful circular linking patterns
- **Index accuracy**: Verify README files accurately list their contents

---

### Phase 2: Content Quality Assessment

#### 2.1 Prompt Quality Tier Analysis
Using `PROMPT_QUALITY_STANDARDS.md`, evaluate prompt distribution:

| Tier | Characteristics | Target % |
|------|-----------------|----------|
| Tier 1 (Gold) | Full structure, false-positive prevention, verification | 30%+ |
| Tier 2 (Silver) | Good structure, some verification | 40% |
| Tier 3 (Bronze) | Basic structure, minimal verification | 20% |
| Tier 4 (Draft) | Incomplete, needs significant work | <10% |

**Assessment tasks:**
1. Sample 30 prompts across domains (stratified sampling)
2. Score each against quality rubric
3. Calculate tier distribution
4. Identify patterns in lower-tier prompts
5. Prioritize upgrade candidates

#### 2.2 Technique Application Audit
Verify technique documentation alignment:

- **Technique tagging**: Do prompts reference their underlying techniques (ST-01, RT-02, etc.)?
- **Technique coverage**: Are all 242 documented techniques used somewhere?
- **Technique accuracy**: When techniques are referenced, are they applied correctly?
- **Technique gaps**: Are there prompts using undocumented techniques?

#### 2.3 False-Positive Prevention Review
Critical quality differentiator - assess implementation:

- **Boundary conditions**: Do prompts specify what NOT to do?
- **Edge case handling**: Are common failure modes addressed?
- **Validation checkpoints**: Do complex prompts include self-verification?
- **Output constraints**: Are outputs bounded to prevent hallucination?

---

### Phase 3: Agentic Resources Deep Dive

#### 3.1 Skills Assessment (138 skills)
Location: `domain-agentic-resources/skills/`

**Evaluate:**
- **Coverage**: Do skills cover all major development workflows?
- **Quality**: Do skills follow patterns from `authoring/skill-patterns/`?
- **Documentation**: Does each skill have complete SKILL.md metadata?
- **Resources**: Are bundled resources (scripts, templates) up-to-date?
- **Dependencies**: Are inter-skill dependencies clear and valid?

**Gap analysis questions:**
- What common developer tasks lack skill support?
- Which technology stacks are underrepresented?
- Are there redundant skills that should be merged?

#### 3.2 Agents Assessment (134 agents)
Location: `domain-agentic-resources/agents/`

**Evaluate:**
- **Task coverage**: Do agents cover the full development lifecycle?
- **Specialization**: Is each agent focused enough to be useful?
- **Orchestration**: Can agents work together effectively?
- **Documentation**: Are agent capabilities and limitations clear?

#### 3.3 Commands Assessment (73 commands)
Location: `domain-agentic-resources/commands/`

**Evaluate:**
- **Workflow coverage**: Do commands support common multi-step workflows?
- **Agent coordination**: Do commands properly orchestrate multiple agents?
- **Error handling**: Do commands handle failure gracefully?
- **Documentation**: Are command interfaces well-documented?

#### 3.4 Personas Assessment (53 personas)
Location: `domain-agentic-resources/personas/`

**Evaluate:**
- **Role clarity**: Is each persona's purpose distinct and clear?
- **Pipeline fit**: Do personas integrate well into development pipelines?
- **Consistency**: Do personas maintain consistent behavior?
- **Documentation**: Are persona capabilities and limitations documented?

---

### Phase 4: Authoring System Review

#### 4.1 Skill Authoring System
Location: `authoring/skill-patterns/`

**Evaluate:**
- **Pattern completeness**: Do the 41 patterns cover all skill types?
- **Template quality**: Is `GOLD_STANDARD_SKILL.md` a good example?
- **Quick start effectiveness**: Can new contributors follow `SKILL_PATTERN_INDEX.md`?
- **Quality rubric accuracy**: Does the 100-point rubric correctly assess skill quality?

#### 4.2 Agent Authoring System
Location: `authoring/agent-patterns/`

**Evaluate:**
- **Pattern coverage**: Are all agent types documented?
- **Examples**: Are there enough examples for each pattern?
- **Integration guidance**: Is agent-to-agent communication documented?

#### 4.3 Command Authoring System
Location: `authoring/command-patterns/`

**Evaluate:**
- **Workflow patterns**: Are multi-agent workflow patterns documented?
- **Error handling patterns**: Is failure recovery documented?
- **Testing guidance**: Can authors validate their commands?

---

### Phase 5: Domain-Specific Analysis

#### 5.1 Software Engineering Domain (~206 prompts)
Location: `domain-software-engineering/`

**Coverage check:**
- Security analysis (14 prompts) - Is OWASP Top 10 covered?
- Testing (14 prompts) - Unit, integration, E2E, accessibility?
- DevOps (20 prompts) - CI/CD, containers, IaC?
- Cloud (8 prompts) - AWS, GCP, Azure, serverless?
- Mobile (83 prompts) - iOS, Android, cross-platform?

**Gap identification:**
- Modern frameworks (Next.js, Remix, SvelteKit)?
- AI/ML development workflows?
- Edge computing and serverless patterns?

#### 5.2 Image Generation Domain (~110 prompts)
Location: `domain-image-generation/`

**Technique validation against `IMAGE_GENERATION_GUIDE.md`:**
- Terminology Steering - avoiding UI triggers
- Grid Forcing + Enumerated Slots - explicit layouts
- Constraint Redundancy - repeated negative constraints
- Negative Space Control - background/shadow banning
- Allowed vs Forbidden - clear boundaries
- Physical Context Anchoring - real-world usage
- Deliverables Locking - exact specifications
- Validation Checklist - self-audit blocks

**Coverage check:**
- Worksheet generators - educational use cases?
- Visualizations - data and concept diagrams?
- Branding - logos, icons, illustrations?
- Model-specific notes - DALL-E, Midjourney, Stable Diffusion?

#### 5.3 Business & Strategy Domain (~109 prompts)
Location: `domain-business-strategy/`

**Coverage check:**
- Strategic frameworks (SWOT, Porter's, BCG)?
- Financial analysis tools?
- Startup/launch resources?
- Research and competitive analysis?

#### 5.4 Non-Coding Domains
Assess against `NON_CODING_QUICK_START.md` patterns:

| Domain | Location | Key Check |
|--------|----------|-----------|
| Education | `domain-education-teaching/` | CREATE pattern compliance |
| Healthcare | `domain-healthcare-clinical/` | Safety and clinical accuracy |
| Research | `domain-research-academic/` | Methodology rigor |
| Personal Development | `domain-personal-development/` | IMPROVE pattern compliance |
| Creative Writing | `domain-creative-writing/` | CREATE pattern compliance |

---

### Phase 6: Documentation & Navigation

#### 6.1 CLAUDE.md Effectiveness
The primary AI agent guide - critical assessment:

- **Accuracy**: Do all file paths and counts match reality?
- **Decision tree**: Is the routing logic correct and complete?
- **Category mapping**: Are all domains properly mapped?
- **Quick reference**: Is the task-to-resource table accurate?

#### 6.2 README Completeness
Every directory should have navigation:

- **Root README.md**: Complete overview with accurate counts?
- **Domain READMEs**: Each `domain-*/README.md` accurate and helpful?
- **Subdirectory READMEs**: Nested directories documented?

#### 6.3 Technique Documentation
Location: `techniques/`

- **MASTER_TECHNIQUE_INDEX.md**: All 242 techniques documented?
- **USE_CASE_LOOKUP.md**: Task-to-technique mappings accurate?
- **Examples**: Are technique examples current and useful?

---

### Phase 7: Community & Maintenance

#### 7.1 Contribution Infrastructure
- **CONTRIBUTING.md**: Does it exist and is it current?
- **Issue templates**: Are they defined and useful?
- **PR templates**: Do they guide quality contributions?
- **Code owners**: Is ownership defined for different areas?

#### 7.2 Quality Automation
- **Linting**: Are markdown files validated?
- **Link checking**: Are broken links detected?
- **Format validation**: Is prompt structure enforced?
- **CI/CD**: What automation exists?

#### 7.3 Versioning & Changelog
- **Version tracking**: How are changes tracked?
- **Migration guides**: Are breaking changes documented?
- **Deprecation policy**: Is the `_archive/` strategy documented?

---

### Phase 8: Future-Proofing

#### 8.1 Emerging Technology Gaps
Identify missing coverage for:

- **AI/ML development**: Model training, evaluation, deployment prompts?
- **LLM operations**: Prompt versioning, A/B testing, monitoring?
- **Edge/IoT**: Embedded systems, edge computing?
- **Web3/Blockchain**: Smart contracts, decentralized apps?
- **AR/VR/XR**: Spatial computing development?

#### 8.2 Workflow Integration Opportunities
- **IDE plugins**: VSCode, JetBrains integration potential?
- **CLI tools**: Command-line access to prompts?
- **API access**: Programmatic prompt retrieval?
- **Package managers**: npm/pip distribution?

#### 8.3 Measurement & Feedback
- **Usage analytics**: How to measure prompt effectiveness?
- **User feedback**: Mechanisms for improvement suggestions?
- **A/B testing**: How to compare prompt versions?
- **Quality metrics**: Automated quality scoring?

---

## Output Format

Structure your analysis as follows:

### Executive Summary
```markdown
## Executive Summary

### Repository Health Score: [X/100]

### Top 5 Strengths
1. [Strength with specific evidence]
2. ...

### Top 5 Critical Issues
1. [Issue with impact assessment]
2. ...

### Recommended Priority Actions
1. [Action] - Impact: [High/Med/Low], Effort: [High/Med/Low]
2. ...
```

### Detailed Findings by Phase

For each finding, use this format:
```markdown
#### [Finding Title]

**Phase:** [1-8]
**Category:** [Structural/Content/Agentic/Authoring/Domain/Docs/Community/Future]
**Severity:** [Critical/High/Medium/Low]

**Observation:**
[Specific, evidence-based observation]

**Impact:**
[Why this matters - user experience, maintainability, completeness]

**Recommendation:**
[Specific, actionable steps to address]

**Effort Estimate:** [Small: <1 day / Medium: 1-5 days / Large: 1+ weeks]

**Success Criteria:**
[How to verify the fix is complete]
```

### Quick Wins (High Impact, Low Effort)
```markdown
## Quick Wins

| # | Action | Impact | Effort | Owner |
|---|--------|--------|--------|-------|
| 1 | [Specific action] | [Benefit] | [Hours] | [Area] |
| 2 | ... | ... | ... | ... |
```

### Strategic Initiatives (High Impact, Higher Effort)
```markdown
## Strategic Initiatives

### Initiative 1: [Title]

**Objective:** [What this achieves]

**Rationale:** [Why this matters]

**Scope:**
- [Component 1]
- [Component 2]

**Implementation Plan:**
1. [Step 1]
2. [Step 2]

**Success Metrics:**
- [Metric 1]
- [Metric 2]

**Estimated Effort:** [Time/resources]
```

### New Content Recommendations
```markdown
## Recommended New Content

### High Priority Additions

| Title | Domain | Purpose | Target User |
|-------|--------|---------|-------------|
| [Prompt name] | [domain-*] | [Problem solved] | [User type] |

### Skill Gaps to Fill

| Skill Name | Category | Capability | Priority |
|------------|----------|------------|----------|
| [Name] | [Category] | [What it does] | [H/M/L] |

### Documentation Needs

| Document | Location | Purpose |
|----------|----------|---------|
| [Name] | [Path] | [Why needed] |
```

### Conclusion
```markdown
## Conclusion

### Overall Assessment
[2-3 paragraph summary of repository health]

### Recommended Roadmap

**Immediate (This Week):**
- [ ] [Action 1]
- [ ] [Action 2]

**Short-term (This Month):**
- [ ] [Action 1]
- [ ] [Action 2]

**Medium-term (This Quarter):**
- [ ] [Action 1]
- [ ] [Action 2]

### Long-term Vision
[Where should this repository be in 1 year?]
```

---

## Execution Guidelines

### Sampling Strategy
For large-scale assessment, use stratified sampling:

```
Total prompts to sample: 50-100
Distribution:
- domain-software-engineering: 15 (largest domain)
- domain-agentic-resources: 15 (most complex)
- domain-business-strategy: 8
- domain-image-generation: 8
- Other domains: 2-3 each
```

### Severity Classification

| Severity | Definition | Response Time |
|----------|------------|---------------|
| Critical | Breaks functionality, incorrect information, security issue | Immediate |
| High | Significant usability or quality issue | This week |
| Medium | Noticeable issue affecting experience | This month |
| Low | Minor improvement opportunity | When convenient |

### Evidence Requirements
All findings must include:
- Specific file paths or examples
- Quantified impact where possible
- Reproducible observation method
- Clear before/after comparison for recommendations

### Anti-Patterns to Avoid
- Generic advice without specific examples
- Recommendations that increase maintenance burden disproportionately
- Changes that break existing workflows without migration path
- Scope creep beyond repository's core mission
- Perfectionism over pragmatism

---

## Success Criteria

A complete analysis will:

1. **Coverage**: Address all 8 phases with evidence from each
2. **Specificity**: Include 30+ specific, actionable findings
3. **Prioritization**: Clear distinction between quick wins and strategic initiatives
4. **Balance**: Mix of content, structural, and process improvements
5. **Measurability**: Success criteria for each major recommendation
6. **Pragmatism**: Recommendations proportional to available resources

---

## Begin Analysis

Start by reading `CLAUDE.md` to understand current repository guidance, then systematically work through each phase. Use file search, content analysis, and sampling to gather evidence. Prioritize findings by impact and effort, and structure output according to the format above.

**Remember:** The goal is actionable improvement, not exhaustive cataloging. Focus on changes that meaningfully improve the repository for its dual audience of AI coding agents and human developers.

---

**Version:** 2.0
**Last Updated:** 2026-01-28
**Supersedes:** `_archive/REPOSITORY_IMPROVEMENT_ANALYSIS.md`
