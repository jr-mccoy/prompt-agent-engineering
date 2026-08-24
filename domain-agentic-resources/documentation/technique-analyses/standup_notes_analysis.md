# Technique Analysis: standup-notes

**Resource Type:** Command
**Path:** claude-code-resources/commands/orchestration/standup-notes.md
**Date Analyzed:** 2025-12-22

---

## Identified Techniques

### Technique 1: Multi-Source Data Orchestration
- **Category:** AG (Agentic) + DS (Domain-Specific)
- **Pattern:** Coordinating multiple data sources (Git, Jira, Obsidian, Calendar) into single coherent output
- **Example:** "Primary Sources: Git commit history, Jira tickets, Obsidian vault, Calendar events"
- **Maps to existing:** AG-07 (Pipeline Orchestration) applied to data gathering
- **Effectiveness:** Comprehensive view from fragmented information sources

### Technique 2: AI-Assisted Commit Summarization
- **Category:** NEW (Natural language synthesis)
- **Pattern:** Converting technical git commits into business value statements
- **Example:** "Transform 'feat: commits into 'Implemented X to enable Y', Group related commits into single accomplishments"
- **Maps to existing:** NEW - translation from technical to business language
- **Effectiveness:** Makes updates accessible to non-technical stakeholders

### Technique 3: Structured Output Templates with Time Metadata
- **Category:** OT (Output) + NE (Non-Engineering)
- **Pattern:** Consistent format with Yesterday/Today/Blockers structure plus time estimates
- **Example:**
```markdown
## Yesterday / Last Update
• [task] - [link] - [timestamp]
## Today / Next
• [task] - [ticket] - [Expected completion: end of day]
```
- **Maps to existing:** OC-01 (Output Format Templates) + NE-02 (Phased Workflow)
- **Effectiveness:** Scannable, actionable format with clear expectations

### Technique 4: Blocker Escalation Framework
- **Category:** DS (Domain-Specific) + NEW
- **Pattern:** Structured blocker reporting with Impact/Need/From/Tried/Next-Step fields
- **Example:**
```markdown
**[CRITICAL]** [Description]
- **Impact:** [What's stopped]
- **Need:** [Specific request]
- **From:** [@person]
- **Tried:** [Attempted solutions]
```
- **Maps to existing:** NEW - systematic blocker communication
- **Effectiveness:** Makes blockers actionable with clear ownership

### Technique 5: Async-First Communication Principles
- **Category:** NE (Non-Engineering) + NEW
- **Pattern:** Design for asynchronous consumption with enough context for distributed timezones
- **Example:** "Post at consistent time, Include context for different timezones, Make blockers actionable without synchronous discussion"
- **Maps to existing:** NE-01 (Single-Question Pacing) extended to async workflows
- **Effectiveness:** Enables global teams without synchronous meetings

### Technique 6: Pattern Recognition in Commits
- **Category:** NEW (Data analysis technique)
- **Pattern:** Extracting accomplishments by recognizing patterns in commit messages (conventional commits, ticket references)
- **Example:**
```markdown
For each commit:
1. Extract commit type (feat, fix, refactor)
2. Parse ticket references (JIRA-123, #456)
3. Group by feature area or epic
4. Summarize into accomplishment statements
```
- **Maps to existing:** NEW - automated narrative generation from structured data
- **Effectiveness:** Reduces manual work, ensures consistency

### Technique 7: Capacity-Aware Planning
- **Category:** DS (Domain-Specific) + NE (Non-Engineering)
- **Pattern:** Calculating available time and flagging overcommitment
- **Example:** "Calculate available hours (8h - meetings - interruptions), Flag overcommitment if planned work exceeds capacity"
- **Maps to existing:** NE-09 (Scope Reduction Pressure) applied to daily planning
- **Effectiveness:** Prevents unrealistic commitments

### Technique 8: Follow-Up Action Extraction
- **Category:** NEW (Task derivation)
- **Pattern:** Automatically extracting actionable tasks from standup content
- **Example:**
```markdown
From standup notes, extract:
1. Blockers → reminder tasks
2. Deliverables → todo with deadline
3. Dependencies → "Waiting On" list
```
- **Maps to existing:** NEW - derivative task generation
- **Effectiveness:** Ensures standup commitments translate to action items

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Technical-to-Business Translation
- **Description:** AI-powered conversion of technical commit messages into business value statements
- **Implementation:** Parse conventional commits, extract ticket context, reframe as user-facing accomplishments
- **Use case:** Team communication across technical and non-technical stakeholders
- **Proposed category:** NE (Non-Engineering)
- **Proposed code:** NE-13

### Pattern 2: Multi-Source Narrative Synthesis
- **Description:** Combining structured data from multiple tools (Git, Jira, Calendar, Notes) into coherent narrative
- **Implementation:** Correlate data across sources, resolve conflicts, generate unified update
- **Use case:** Status reporting from fragmented tool landscape
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-19

### Pattern 3: Structured Blocker Escalation
- **Description:** Formalized blocker communication with Impact/Need/From/Tried/Next fields
- **Implementation:** Template requiring specific information for each blocker
- **Use case:** Distributed teams needing clear, actionable blocker communication
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-20

### Pattern 4: Async-First Communication Design
- **Description:** Designing communication artifacts for asynchronous consumption across timezones
- **Implementation:** Consistent timing, complete context, actionable blockers, threaded discussions
- **Use case:** Global distributed teams
- **Proposed category:** NE (Non-Engineering)
- **Proposed code:** NE-14

### Pattern 5: Automated Task Derivation
- **Description:** Extracting actionable tasks from narrative content (standup notes, meeting notes)
- **Implementation:** Parse for commitments, blockers, dependencies; generate task list
- **Use case:** Converting communication into trackable work items
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-21

---

## Multi-Technique Combinations

**Technique Stack:** Multi-Source Orchestration + Commit Summarization + Structured Templates + Blocker Escalation + Async-First Design + Capacity Planning + Task Derivation

**Combination Purpose:** Create comprehensive, automated standup note generation for distributed teams

**Synergies:**
- Multi-source orchestration + Commit summarization = Complete work picture
- Structured templates + Async-first = Scannable across timezones
- Blocker escalation + Task derivation = Blockers become trackable work
- Capacity planning + Structured output = Realistic commitments

---

## Notes for Integration

**Add to MASTER_TECHNIQUE_INDEX:**
- NE-13: Technical-to-Business Translation
- DS-19: Multi-Source Narrative Synthesis
- DS-20: Structured Blocker Escalation
- NE-14: Async-First Communication Design
- DS-21: Automated Task Derivation

**Cross-reference with prompts:**
- Related to: `domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md` (project planning)
- Related to: `domain-personal-development/prompts/work_better_*.md` (productivity prompts)
- Complements: `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`

**Best practices:**
- Always synthesize from multiple sources
- Translate technical to business language
- Design for async consumption
- Make blockers actionable with ownership
- Derive tasks from commitments

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 implementation)
**Analysis Duration:** 14 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** High - Critical for remote team coordination
