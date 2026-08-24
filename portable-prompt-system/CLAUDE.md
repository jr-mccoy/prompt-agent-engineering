# Prompt-Authoring Engine — Agent Router

You are working in a project that bundles a **portable prompt-authoring & technique system** under
`portable-prompt-system/`. When the user asks you to **write a prompt, design an AI workflow, craft an
image-generation brief, or build a reusable skill/agent/command**, use this engine instead of improvising.
It encodes ~248 named techniques and a Tier-1 quality bar.

> If this file lives at the project root, treat the paths below as relative to it. If it's imported
> from a parent `CLAUDE.md`, prefix paths with `portable-prompt-system/`.

---

## Decision tree

```
User request
│
├─ Write / improve a PROMPT?
│   ├─ Content / writing / business / education / research?  → guides/NON_CODING_QUICK_START.md
│   ├─ Coding / technical / DevOps / analysis?               → guides/AI_AGENT_QUICK_START.md
│   └─ Faceless content (scripts, hooks, thumbnails, SEO,
│      repurposing, channel voice)?                          → content-playbook/CONTENT_QUICK_START.md
│
├─ Generate an IMAGE (thumbnail, cover, infographic, logo)?  → guides/image-generation/
│   └─ Targeting OpenAI gpt-image-2 specifically?            → guides/image-generation/GPT_IMAGE_2_GUIDE.md
│
└─ Build a reusable SKILL / AGENT / COMMAND for Claude Code? → resource-patterns/
    (skill-patterns/ · agent-patterns/ · command-patterns/ · INTEGRATION_PATTERNS.md)
```

---

## The 5-step authoring loop (follow every time you write a prompt)

1. **Classify** the task and pick the guide from the decision tree above.
2. **Select 3–5 techniques.** Look up the task in `techniques/USE_CASE_LOOKUP.md` (or the fast picker
   `guides/TECHNIQUE_PICKER_FAST.md`), then read the chosen techniques in
   `techniques/MASTER_TECHNIQUE_INDEX.md`. Use only **real IDs** from the index — never invent one.
3. **Build** the prompt on the structure in `guides/NEW_PROMPT_TEMPLATE.md`:
   **Objective (ST-01) → Inputs/Context (CM-01) → Constraints, Must/Must-Not (CM-02) →
   Steps (ST-02) → Output Format (ST-03) → Verification (QA-01).**
   When the prompt consumes pasted material, wrap it in named XML-style tags
   (see `guides/PROMPT_STRUCTURE_GUIDE.md`).
4. **Meet the quality bar** in `guides/PROMPT_QUALITY_STANDARDS.md` — Tier 1 means explicit
   constraints, a locked output format, a verification block, and **false-positive prevention**
   (the model must not invent facts, fabricate authority, or pass off uncertain claims as certain).
5. **Verify.** Include a self-check; for high-stakes/monetized output, add an adversarial
   stress-test (QA-02: "list 3 ways this could be wrong or misleading").

---

## Operating rules

- **Cite techniques by ID** as you design (e.g., "using CM-02 for the no-fabrication constraint") so
  choices are auditable.
- **Default to the full structured format** when delivering a reusable prompt: YAML frontmatter
  (`title`, `category`, `techniques`, `difficulty`, `tags`, `updated`) + the sectioned body above.
  For a one-off ad-hoc prompt, the body alone is fine.
- **Never invent data, statistics, citations, or expertise** in prompts you write or in content you
  generate. Bake an explicit no-fabrication constraint into content prompts and flag uncertain items.
- **Match scope to the request.** A quick prompt doesn't need the resource-patterns machinery; reserve
  skills/agents/commands for genuinely reusable, multi-step capabilities.
- **Save good prompts** into the project using the convention `{function}.md` and validate against
  `guides/NEW_RESOURCE_CHECKLIST.md`.

---

## Note on bundled scope

The `resource-patterns/` layer assumes the Claude Code ecosystem (Task tool, `subagent_type`,
`.claude/`). References inside the bundle to a `domain-agentic-resources/` implementation library or
`domain-*` example prompts point at the **source** library and are **not** included here — they're
illustrative. The techniques, guides, content playbook, and authoring patterns are fully self-contained.
