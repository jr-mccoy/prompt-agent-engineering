---
name: external-prompt-kit-ingestor
description: "Use this skill whenever an external prompt kit, prompt collection, or article-with-embedded-prompts is dropped into this repository (any markdown/PDF/text file containing one or more pasteable prompts that didn't originate here). Splits the source into individually structured Tier-1 prompt files, registers any net-new techniques in the master technique index, organizes outputs into the correct domain directory (creating new ones when justified), updates PROMPT_INDEX.json and PROMPT_INDEX.md, leaves a back-pointer in the source, and reports implications. Trigger phrases: \"process this kit\", \"ingest this prompt collection\", \"we got a new prompt pack\", \"import these external prompts\", \"extract prompts from this article\"."
license: Repository internal
metadata:
  tags:
    - meta
    - ingestion
    - curation
    - prompt-engineering
    - repo-maintenance
  updated: "2026-04-19"
---

# External Prompt Kit Ingestor

Standard procedure for absorbing an outside prompt kit into this repository so it becomes first-class, indexed, technique-tagged content rather than an orphaned file.

## When to Use

Trigger this skill when any of the following lands in the repo:
- A markdown/text/PDF "prompt kit" or "prompt pack" from an external author
- An article that embeds one or more reusable prompts in code/quote blocks
- A team-shared `.md` containing prompts the user wants made permanent
- A copied-in conversation transcript whose prompts deserve preservation

Do **not** use this skill for:
- Authoring a new prompt from scratch (use `AI_AGENT_QUICK_START.md` or `NON_CODING_QUICK_START.md`)
- One-off prompt improvement (use `domain-prompt-engineering/prompt-improvement/`)
- Already-structured prompts that just need a home (skip to step 4)

## Operating Principles

1. **One source of truth per prompt.** Every extracted prompt becomes its own Tier-1 file with full YAML frontmatter. The original kit file stays in place as the narrative source and gets a top-of-file note pointing at the structured versions.
2. **Reuse techniques before inventing them.** Most kits map to existing IDs in `techniques/MASTER_TECHNIQUE_INDEX.md`. Only register a new technique when the pattern is genuinely novel and reusable across domains.
3. **Place by intent, not by surface form.** A prompt about agent loops belongs in `domain-engineering-workflows/ai-patterns/`, not wherever it's syntactically convenient. Use the Category Mapping in the root `CLAUDE.md`.
4. **Indexes are not optional.** A prompt that isn't in `PROMPT_INDEX.json` and `PROMPT_INDEX.md` is invisible to discovery tooling. Update both.
5. **Report implications.** Every ingestion ends with a written analysis of how the new prompts relate to existing patterns, what gaps they expose, and what follow-up work they suggest.

## Procedure

Follow `workflows/ingest.md` end-to-end. Do not skip steps. The workflow is gated — each phase produces an artifact the next phase consumes.

Phases:
1. **Inventory** — Identify every distinct prompt in the source.
2. **Classify** — Assign domain, category, and difficulty per prompt.
3. **Map techniques** — Match each prompt against the master technique index; flag novel patterns for promotion.
4. **Structure** — Generate Tier-1 markdown files (frontmatter + body) per prompt.
5. **Place** — Write files to the correct domain directory, creating new subdirectories when justified.
6. **Index** — Update `PROMPT_INDEX.json` and `PROMPT_INDEX.md`.
7. **Back-reference** — Add a repository note to the top of the source file linking to the new structured files.
8. **Report** — Deliver an implications memo to the user.

## Bundled Resources

- `workflows/ingest.md` — The full step-by-step procedure with gate checks.
- `references/frontmatter-template.md` — Canonical YAML frontmatter and body skeleton for extracted prompts.
- `references/technique-promotion-criteria.md` — Decision rules for "is this technique novel enough to register in the master index?"
- `references/ingestion-checklist.md` — Pre-delivery validation checklist (run before declaring done).

## Quality Gate

Before reporting completion, every extracted prompt must:
- Have valid YAML frontmatter with title, category, description, techniques, difficulty, tags, updated, related_prompts
- Reference at least 3 valid technique IDs from `techniques/MASTER_TECHNIQUE_INDEX.md`
- Live in a domain directory consistent with the root `CLAUDE.md` Category Mapping
- Appear in both `PROMPT_INDEX.json` and `PROMPT_INDEX.md`
- Carry a `Source:` line in the body pointing back to the original kit file

The source file must:
- Begin with a `> **Repository note:**` block listing the structured files
- Remain unchanged below that note (preserve the author's narrative)

## Done Criteria

Done = (a) all prompts extracted and placed, (b) techniques registered or matched, (c) both indexes updated, (d) source back-referenced, (e) implications memo delivered to user covering: pattern family this kit introduces, cross-references to existing prompts/skills, gaps it exposes, suggested follow-ups.

## Related Resources

- Skill: `domain-agentic-resources/skills/developer-tools/skill-creator` — for promoting recurring kit patterns into reusable skills
- Agent: `domain-agentic-resources/agents/orchestration/prompt-kit-ingestor.md` — the parallel-worker wrapper around this skill
- Authoring: `authoring/skill-patterns/AGENT_SKILL_QUICK_START.md` — when an ingested kit clearly wants to become a skill rather than a prompt set
- Reference: root `CLAUDE.md` Category Mapping section — authoritative domain placement rules
