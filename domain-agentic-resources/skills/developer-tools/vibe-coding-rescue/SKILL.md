---
name: vibe-coding-rescue
description: Diagnose and recover an AI-assisted ("vibe-coded") project that has hit a wall — confused codebase, AI agent looping on the same task, security debt from auto-generated code, or a handoff with no documentation. Use when an AI coding session has produced more code than the team understands, when progress has stalled despite many edits, or when bringing a human engineer onto a previously AI-led project.
metadata:
  tags:
    - ai-coding
    - recovery
    - refactoring
    - handoff
    - diagnosis
  updated: "2026-05-05"
---

# Vibe-Coding Rescue

AI coding sessions can produce a working prototype fast and a maintenance disaster slowly. This skill is for projects that started in AI flow and have now hit a wall — the codebase is wide, the architecture is implicit, the AI keeps editing the same files without making progress, and nobody can confidently explain how the system works. The skill bundles five workflows for diagnosing, scaffolding, and recovering.

## When to Use This Skill

- A previously fast-moving AI-coded project has stalled on a specific task
- The AI agent keeps "fixing" the same area without converging
- A founder/PM needs to hand off an AI-built prototype to a human engineering team
- Security and quality concerns have accumulated in AI-generated code
- The project lacks the rules/context document needed for AI to be productive going forward

## Workflows

This skill routes to five workflows in `domain-software-engineering/vibe-coding-rescue/`. Pick the one that matches the symptom.

### 1. Wall Diagnosis (`viberescue_wall_diagnosis.md`)

**Trigger:** "I don't know why we're stuck."

Diagnoses the type of wall: context wall (codebase outgrew the AI's working memory), architecture wall (implicit decisions colliding), capability wall (task is outside the model's ability), or process wall (no clear acceptance criteria, no rollback strategy).

Output: a labeled diagnosis with a specific next-step playbook.

### 2. Rules File Design (`viberescue_rules_file_design.md`)

**Trigger:** "The AI keeps making the same mistakes."

Builds a `CLAUDE.md` / `.cursorrules` / equivalent rules file specific to the codebase: directory conventions, library choices that must be respected, test patterns, and forbidden moves. This is the single highest-leverage artifact for getting AI productivity back.

Output: a complete rules file scaffold tailored to the actual codebase.

### 3. Decompose Stuck Task (`viberescue_decompose_stuck_task.md`)

**Trigger:** "The AI has tried to implement this 8 times and it's still broken."

Breaks a task that's beyond the AI's one-shot capability into smaller subtasks each within reach. Identifies what scaffolding (types, tests, mock data) needs to exist before the AI attempts the next subtask. Names the specific signal that each subtask is complete.

Output: a sequenced subtask list with acceptance criteria for each.

### 4. Security Audit (`viberescue_security_audit.md`)

**Trigger:** "We're considering shipping this to real users."

Audits AI-generated code for the failure modes specific to AI coding: hallucinated package names, unsafe deserialization, missing input validation, secrets in code, leaked PII in logs, copy-pasted vulnerable patterns, dependency confusion. Distinct from a generic security review because it knows what AI tools tend to get wrong.

Output: a prioritized list of security findings with remediation steps.

### 5. Engineer Handoff Briefing (`viberescue_engineer_handoff_briefing.md`)

**Trigger:** "We're hiring a real engineer to take this over."

Produces a briefing document that lets a human engineer load the project into their head: what was built, why these architectural choices were made (or admit they were emergent), what works, what doesn't, what tests exist, where the risks are, what the AI-coding session left undone.

Output: a 3-5 page briefing that converts implicit context into explicit handoff material.

## Routing Decision Tree

```
What's the symptom?
│
├── "We don't know why we're stuck" → Workflow 1: Wall Diagnosis
│
├── "AI keeps making the same mistakes / ignoring conventions"
│   → Workflow 2: Rules File Design
│
├── "AI can't complete this specific task no matter how I prompt"
│   → Workflow 3: Decompose Stuck Task
│
├── "Considering shipping to users / shipping to production"
│   → Workflow 4: Security Audit (always run before launch)
│
└── "Bringing a human engineer onto the project"
    → Workflow 5: Engineer Handoff Briefing
```

## Recommended Sequence for a Full Rescue

When taking over a project that's hit multiple problems at once:

1. **Wall Diagnosis** — name the type of wall first
2. **Security Audit** — find the things that block shipping at all
3. **Rules File Design** — stabilize AI behavior going forward
4. **Decompose Stuck Task** — apply to whatever the AI is currently failing at
5. **Engineer Handoff Briefing** — only when steps 1-4 produce stable ground

## Companion Skills

- `dataset-validation` (skills/ml-ai/) — if the project includes any data pipelines
- `model-evaluation-harness` (skills/ml-ai/) — if AI features are part of the product
- `core-web-vitals-audit` (skills/seo-marketing/) — if it's a customer-facing web app

## Related Resources

The source prompts live at:
- ../../../domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
- ../../../domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
- ../../../domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md
- ../../../domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md
- ../../../domain-software-engineering/vibe-coding-rescue/viberescue_engineer_handoff_briefing.md

These prompts are the executable workflows; this SKILL.md is the routing layer that picks the right one given the symptom.

## Anti-Patterns to Avoid

- **Running all five workflows in parallel** — the order matters; results from one inform the next
- **Skipping Wall Diagnosis** — without naming the type of wall, you treat the wrong root cause
- **Treating the rules file as one-and-done** — it should be revised every time the AI gets confused in a recurring way
- **Decomposing without scaffolding** — small subtasks still need types, tests, and clear interfaces in place
- **Handoff briefing without security audit first** — you'll hand over latent risks the new engineer can't surface
