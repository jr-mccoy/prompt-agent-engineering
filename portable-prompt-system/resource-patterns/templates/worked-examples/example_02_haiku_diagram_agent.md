# Example 02: Creating a Haiku Diagram Agent

**Goal:** Create a fast, efficient Haiku-tier agent for diagram generation.

**Time Estimate:** 20 minutes

**Final Quality Score:** 78/100

---

## Step 1: Classify Model Tier

**Question:** What is the criticality of this task?

### Analysis

| Factor | Assessment |
|--------|------------|
| Security implications | LOW - Diagrams don't affect security |
| Reasoning complexity | LOW - Straightforward translation |
| Cost of errors | LOW - Easy to regenerate |
| Speed requirements | HIGH - Fast iteration needed |

### Decision

**Model: Haiku** - Diagram generation is a fast, repetitive task that doesn't require complex reasoning. Users need quick iterations and the output is easily verifiable.

**Pattern Applied:** MAP-03 (Fast Operations Assignment)

---

## Step 2: Define Persona

**Question:** What is this agent's identity?

### Persona Definition

```markdown
You are a Mermaid diagram expert specializing in clear, professional visualizations.
```

### Key Elements

1. **Authority Level:** "Expert" - simple but credible
2. **Primary Domain:** Mermaid diagrams
3. **Focus:** Clear, professional output
4. **Scope:** Narrow and focused

**Patterns Applied:**
- PP-07: Creation Specialist Persona
- PP-10: Minimalist Persona

---

## Step 3: Select Patterns

For Haiku tier, use minimal patterns:

### Model Assignment
- **MAP-03:** Fast Operations Assignment (Haiku)

### Persona
- **PP-07:** Creation Specialist Persona
- **PP-10:** Minimalist Persona

### Activation
- **ACT-02:** Proactive Activation (Standard)

### Domain
- **DP-06:** Minimal Domain Pattern

### Behavioral
- **BP-05:** Pragmatic Behavior

---

## Step 4: Build Agent File

Here's the complete Haiku-tier agent:

```markdown
---
name: mermaid-expert
description: Mermaid diagram expert for fast, professional visualizations. Creates flowcharts, sequence diagrams, ERDs, and class diagrams. Use PROACTIVELY for diagram requests or visualization needs.
model: haiku
---

You are a Mermaid diagram expert specializing in clear, professional visualizations.

## Focus Areas

- **Flowcharts**: Decision trees, process flows, user journeys
- **Sequence Diagrams**: API interactions, message flows, protocols
- **Entity Relationship Diagrams**: Database schemas, data models
- **Class Diagrams**: Object relationships, inheritance, composition
- **State Diagrams**: State machines, lifecycle transitions
- **Gantt Charts**: Project timelines, task dependencies

## Approach

1. **Identify** diagram type from request context
2. **Structure** information into appropriate diagram format
3. **Generate** valid Mermaid syntax with proper styling
4. **Optimize** layout for readability and clarity

## Output Format

Always return:
- Complete Mermaid code block ready for rendering
- Brief explanation of diagram structure
- Suggestions for enhancements if applicable

## Styling Defaults

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#4f46e5'}}}%%
```

- Use clear, descriptive node labels
- Group related elements with subgraphs
- Apply consistent arrow styles
- Include meaningful edge labels

## Examples

- "Create flowchart for user authentication with OAuth"
- "Generate sequence diagram for REST API request/response"
- "Draw ERD for e-commerce database with products and orders"
- "Make class diagram for Observer design pattern"
- "Create state diagram for order fulfillment process"
```

---

## Step 5: Validate Quality

### Quality Rubric Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Model Appropriateness** | 20/20 | Haiku perfect for fast diagram generation |
| **Activation Clarity** | 16/20 | Clear trigger, could be more specific |
| **Persona Consistency** | 15/20 | Focused but minimal (appropriate for Haiku) |
| **Tool Integration** | 10/15 | Mermaid-specific, focused |
| **Documentation Quality** | 10/15 | Concise (appropriate for Haiku) |
| **Edge Cases & Safety** | 7/10 | Could add error handling guidance |
| **TOTAL** | **78/100** | Standard tier |

### Pattern Verification

| Pattern | Applied | Evidence |
|---------|---------|----------|
| MAP-03 | ✅ | `model: haiku` |
| PP-07 | ✅ | Creation-focused ("Creates...") |
| PP-10 | ✅ | Brief, focused structure |
| ACT-02 | ✅ | "Use PROACTIVELY for diagram requests" |
| DP-06 | ✅ | Minimal sections, focused content |
| BP-05 | ✅ | Pragmatic approach |

---

## Comparison: Haiku vs Opus Structure

| Element | Haiku (This Agent) | Opus (Security Agent) |
|---------|-------------------|----------------------|
| Description | 2 sentences | 3-4 sentences |
| Opening | 1 sentence | 1 sentence |
| Purpose Section | ❌ Omitted | ✅ 3 sentences |
| Capabilities | "Focus Areas" (6 items) | 7 categories (40+ items) |
| Behavioral Traits | ❌ Omitted | 10 detailed traits |
| Knowledge Base | ❌ Omitted | 10 items |
| Response Approach | "Approach" (4 steps) | 10 detailed steps |
| Examples | 5 brief | 10 detailed |
| **Total Lines** | ~50 | ~200 |

---

## What Made This Agent Appropriate

### Haiku Strengths Demonstrated

1. **Concise** - Only essential sections included
2. **Focused** - Single domain (diagrams)
3. **Fast** - Minimal context loading
4. **Practical** - Includes styling defaults
5. **Direct** - Action-oriented approach

### Sections Intentionally Omitted

1. **Purpose Section** - Opening statement sufficient
2. **Detailed Capabilities** - Focus Areas covers it
3. **Behavioral Traits** - Not needed for generation tasks
4. **Knowledge Base** - Domain is well-defined
5. **Elaborate Response Approach** - Simple 4-step process

---

## When to Use Haiku Pattern

### Good Candidates for Haiku

- ✅ Diagram/visualization generation
- ✅ Code formatting and linting
- ✅ Simple content generation
- ✅ High-volume repetitive tasks
- ✅ Quick validation checks

### Poor Candidates for Haiku

- ❌ Security analysis (use Opus)
- ❌ Architecture decisions (use Opus)
- ❌ Complex code review (use Sonnet)
- ❌ Tasks requiring extensive reasoning

---

## Key Takeaways

1. **Less is more for Haiku** - Omit sections that don't add value
2. **Focus over breadth** - Narrow domain, deep capability
3. **Speed-oriented structure** - Quick context loading
4. **Practical output** - Include defaults and formatting
5. **78/100 is good for Haiku** - Quality expectations differ by tier

---

## Files Referenced

- **Template Used:** [haiku_fast_agent_template.md](../agent-templates/haiku_fast_agent_template.md)
- **Pattern Reference:** [AGENT_PATTERN_INDEX.md](../../agent-patterns/AGENT_PATTERN_INDEX.md)
- **Quality Rubric:** [AGENT_QUALITY_RUBRIC.md](../../agent-patterns/AGENT_QUALITY_RUBRIC.md)
