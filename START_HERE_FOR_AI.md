# AI Assistant Start Here

**Purpose:** Fast orientation for AI assistants (Claude, ChatGPT, Codex, Cursor, etc.) to navigate this repository efficiently.

---

## What This Repo Contains

This is a collection of **~1,800 AI prompts** and coding agent resources organized into 20 domain directories. It provides:

- **Prompts** for coding, business, productivity, education, healthcare, and 15+ other domains
- **Skills** (186) - Reusable capabilities with bundled resources
- **Agents** (99) - Task-specific agents with model recommendations
- **Commands** (~96) - Multi-agent orchestration workflows
- **Personas** (52) - Pipeline identities for complex workflows
- **Techniques** (327 active) - Formally defined prompt engineering techniques across 18 categories

The canonical technique reference is [`techniques/MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md).

---

## If You Only Read 3 Files, Read These

| Priority | File | Why |
|----------|------|-----|
| 1 | [`techniques/MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md) | Canonical technique catalog (327 active techniques). All IDs are authoritative here. |
| 2 | [`AI_AGENT_QUICK_START.md`](AI_AGENT_QUICK_START.md) | 5-step process for building coding/technical prompts |
| 3 | [`NON_CODING_QUICK_START.md`](NON_CODING_QUICK_START.md) | Task patterns for education, healthcare, writing, business prompts |

---

## Routing Table: What Do You Need?

| Task | Go To |
|------|-------|
| **Build a coding/technical prompt** | [`AI_AGENT_QUICK_START.md`](AI_AGENT_QUICK_START.md) |
| **Build a non-coding prompt** (education, writing, healthcare, business) | [`NON_CODING_QUICK_START.md`](NON_CODING_QUICK_START.md) |
| **Build an image generation prompt** | [`domain-image-generation/IMAGE_GENERATION_GUIDE.md`](domain-image-generation/IMAGE_GENERATION_GUIDE.md) |
| **Find techniques by use case** | [`techniques/USE_CASE_LOOKUP.md`](techniques/USE_CASE_LOOKUP.md) |
| **Look up technique definitions** | [`techniques/MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md) |
| **Create a reusable skill** | [`authoring/skill-patterns/README.md`](authoring/skill-patterns/README.md) |
| **Find existing skills/agents/commands** | [`domain-agentic-resources/`](domain-agentic-resources/) |
| **Find existing prompts by domain** | See [Folder Quick Reference](#folder-quick-reference) below |
| **Understand full repo structure** | [`REPO_MAP.md`](REPO_MAP.md) |

---

## Folder Quick Reference

| Folder | Contains |
|--------|----------|
| `domain-software-engineering/` | Code analysis, testing, DevOps, cloud, API, mobile (~483) |
| `domain-frontend-development/` | React, Vue, accessibility, performance, testing (~33) |
| `domain-agentic-resources/` | Skills, agents, commands, personas for Claude Code (~821) |
| `domain-business-strategy/` | SWOT, competitive analysis, startup, research (~124) |
| `domain-productivity/` | Validation, career, automation, prototyping (~84) |
| `domain-image-generation/` | Branding, coloring-book, healthcare images (~15) |
| `domain-engineering-workflows/` | Sprint planning, tasks, workflows (~58) |
| `domain-presentations/` | Executive and board presentations (~24) |
| `domain-professional-writing/` | Domain-specific professional guides (~46) |
| `domain-professional-communication/` | PRDs, product management (~30) |
| `domain-personal-development/` | Goals, habits, career (~43) |
| `domain-prompt-engineering/` | Meta-prompts for prompt improvement (~22) |
| `domain-decision-making/` | Decision frameworks (~28) |
| `domain-healthcare-clinical/` | Clinical decision support (~55) |
| `domain-learning-coding/` | Coding education (~17) |
| `domain-research-academic/` | Literature review, methodology (~15) |
| `techniques/` | MASTER_TECHNIQUE_INDEX.md + USE_CASE_LOOKUP.md |
| `authoring/` | Skill, agent, command creation guides |

---

## How to Ask the Repo for Help

**Example queries an AI can follow:**

### Example 1: "Help me review this code for security issues"
1. Check `domain-software-engineering/analysis/security/` for existing prompts
2. Find `security_vulnerability_analysis.md`
3. Execute that prompt against the user's code

### Example 2: "Create a new prompt for database migration review"
1. This is a NEW prompt request (not using an existing one)
2. Open `AI_AGENT_QUICK_START.md`
3. Follow the 5-step process to build a custom prompt
4. Reference `techniques/MASTER_TECHNIQUE_INDEX.md` for technique IDs

### Example 3: "What technique should I use for step-by-step analysis?"
1. Open `techniques/USE_CASE_LOOKUP.md`
2. Look for reasoning/analysis patterns
3. Find `RT-01: Chain-of-Thought` or similar

---

## Warning: Technique IDs May Change

Technique IDs can merge or be renamed as the repository evolves. **The Master Technique Index is canonical.**

- Always reference [`techniques/MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md) for current IDs
- If you find a deprecated ID, check the Master Index for the current equivalent
- The Master Index includes merge documentation when techniques are consolidated

---

## Full Documentation

For comprehensive guidance, see:
- [`CLAUDE.md`](CLAUDE.md) - Complete agent instructions (detailed decision trees, category mappings)
- [`README.md`](README.md) - Full repository documentation
- [`REPO_MAP.md`](REPO_MAP.md) - Visual folder structure

---

**Last Updated:** 2026-04-20
