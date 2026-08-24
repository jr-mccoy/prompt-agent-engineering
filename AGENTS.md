# AGENTS.md — Working Guide for Prompting-Guides

This file adapts key instructions from `CLAUDE.md` for agents working in this repository.

## Purpose
Use this repository as a **prompt + agentic resource library first**, and only create new assets when needed.

## Core Routing Logic
When a user asks for work, route by intent:

1. **"Create a new prompt"**
   - **Image generation prompt** → use `domain-image-generation/IMAGE_GENERATION_GUIDE.md`
   - **Coding/technical prompt** → use `AI_AGENT_QUICK_START.md`
   - **Non-coding prompt** → use `NON_CODING_QUICK_START.md`

2. **"Create a new skill"**
   - Use `authoring/skill-patterns/README.md`

3. **"Help me with X" (task execution)**
   - Prefer existing resources:
     - `domain-agentic-resources/skills/`
     - then domain prompt libraries in `domain-*/`

4. **"How do I / what’s best practice"**
   - Reference documentation/guides (`README.md`, techniques index, quick starts, authoring guides)

## Repository Mental Model
- `authoring/` = how to build skills/agents/commands
- `domain-agentic-resources/` = implemented skills, agents, commands, personas
- `domain-*/` = prompt libraries by subject area
- `techniques/` = prompt engineering reference system

## Skill vs Prompt Decision
Create a **skill** when the capability is reusable, multi-step, resource-backed, tool-integrated, or benefits from progressive disclosure.

Create a **prompt** when it’s one-off, simple, and task-specific without external resources.

## Priority Resource Map (Quick)
- Software engineering help → `domain-software-engineering/`
- Frontend help → `domain-frontend-development/`
- Workflows/project planning → `domain-engineering-workflows/`
- Business analysis → `domain-business-strategy/`
- Productivity/focus → `domain-productivity/`
- Image generation → `domain-image-generation/`
- Prompt improvement/meta work → `domain-prompt-engineering/`
- Parenting → `domain-parenting/`
- Professional communication → `domain-professional-communication/`

## Operating Rules (Token & Workflow Efficiency)
1. Don’t re-read files already read unless changed or a new section is required.
2. Don’t re-verify facts already established in-session.
3. Prefer targeted search (`rg`) over broad file reads.
4. Read large files in slices when possible.
5. Batch independent checks/reads.
6. Trust successful tool outputs; avoid redundant confirmations.
7. Stop once the user’s task is complete.

## Practical Defaults
- Reuse existing repository assets before drafting from scratch.
- Match the user’s task to the narrowest applicable domain/path.
- Keep outputs structured, concrete, and ready to use.

---
Source basis: `CLAUDE.md` (root).
