# Portable Prompt-Authoring & Technique System

A **self-contained, drop-in prompt engine.** Copy this one folder into any project and you can author
prompts and AI resources at the same quality as the large library it was extracted from — now with the
*context of your own project*. Works with Claude Code, ChatGPT, Cursor, image models, or any AI tool,
and works standalone for a human writing prompts by hand.

It contains the **complete technique library** (≈248 formally defined techniques across 19 categories),
all the **prompt-authoring guides**, the **quality standards**, the **skill / agent / command authoring
patterns**, and a **faceless-content application layer** with ready-to-use starter prompts.

---

## Install

Copy the whole directory into your project root:

```
your-project/
└── portable-prompt-system/      ← copy this folder in
```

Then either:
- **Using Claude Code?** The bundled [`CLAUDE.md`](CLAUDE.md) orients the agent automatically when it's
  at your repo root, or `@import` it from your project's own `CLAUDE.md`:
  `See @portable-prompt-system/CLAUDE.md for how to author prompts and AI resources.`
- **Using any other tool, or working by hand?** Start at the map below.

Nothing else to set up. No build, no dependencies, no scripts required.

---

## What's inside

```
portable-prompt-system/
├── README.md            ← you are here (standalone entry point)
├── CLAUDE.md            ← Claude Code router (decision tree → techniques → guide → quality → verify)
│
├── techniques/          ← THE CORE. Self-contained technique library.
│   ├── MASTER_TECHNIQUE_INDEX.md   (the canonical catalog — every technique, with IDs like ST-01)
│   ├── USE_CASE_LOOKUP.md          (task → recommended technique combinations)
│   └── … pattern files, new-techniques/, failure modes, model quirks, security checklist, etc.
│
├── guides/              ← How to author prompts
│   ├── NON_CODING_QUICK_START.md   (content / writing / business — start here for content work)
│   ├── AI_AGENT_QUICK_START.md     (coding / technical prompts)
│   ├── PROMPT_QUALITY_STANDARDS.md (the 5-tier quality bar + false-positive prevention)
│   ├── NEW_PROMPT_TEMPLATE.md, PROMPT_STRUCTURE_GUIDE.md, TECHNIQUE_PICKER_FAST.md,
│   │   NEW_RESOURCE_CHECKLIST.md, TROUBLESHOOTING.md
│   └── image-generation/           (IMAGE_GENERATION_GUIDE.md + GPT_IMAGE_2_GUIDE.md)
│
├── resource-patterns/   ← How to author reusable Claude Code resources
│   ├── skill-patterns/ · agent-patterns/ · command-patterns/ · templates/
│   └── INTEGRATION_PATTERNS.md
│
└── content-playbook/    ← Faceless-content application layer
    ├── CONTENT_QUICK_START.md      (maps content tasks → techniques → guide → starter prompt)
    └── starter-prompts/            (6 Tier-1 prompts: scripts, hooks, thumbnails, SEO, repurpose, voice bible)
```

---

## The authoring workflow (works in any tool)

1. **Classify the task.** Creating? Analyzing? Teaching? Deciding? Drafting an image? → pick the guide:
   content/writing → `guides/NON_CODING_QUICK_START.md`; code → `guides/AI_AGENT_QUICK_START.md`;
   images → `guides/image-generation/`; faceless content → `content-playbook/CONTENT_QUICK_START.md`.
2. **Pick 3–5 techniques.** Use `techniques/USE_CASE_LOOKUP.md` (by task) or
   `guides/TECHNIQUE_PICKER_FAST.md`, then look them up in `techniques/MASTER_TECHNIQUE_INDEX.md`.
3. **Build the prompt** from `guides/NEW_PROMPT_TEMPLATE.md` (Objective → Inputs → Constraints →
   Steps → Output Format → Verification).
4. **Enforce the quality bar** with `guides/PROMPT_QUALITY_STANDARDS.md` (aim for Tier 1: explicit
   constraints, locked output format, a verification block, and false-positive prevention).
5. **Verify** using the prompt's own self-check; escalate to an adversarial stress-test (QA-02) for
   high-stakes work.

---

## The technique-ID system

Techniques are referenced by a two-letter prefix + number (e.g., `ST-01`, `NE-12`, `SV-11`). Prefixes
group them by function — `ST` structural, `RT` reasoning, `OC` output control, `QA` quality assurance,
`CM` context management, `RP` role/perspective, `NE` non-engineering, `SV` specialized visual, and more
(the full prefix table is at the top of `techniques/MASTER_TECHNIQUE_INDEX.md`).
**Always cite real IDs from the index; never invent new ones.**

---

## Provenance note (read once)

This bundle was extracted from a much larger prompt library. To keep it self-contained:

- The **technique library, guides, content playbook, and resource-patterns are fully usable on their own.**
- Some files contain **illustrative references** to the source library — paths like `domain-*/…example.md`
  (example prompts) and the `domain-agentic-resources/` **implementation** library (pre-built agents/
  skills/commands). Those referenced files are **not bundled**; treat such links as "see the source
  library." To *author* your own skills/agents/commands, use `resource-patterns/`.
- A few `**Reference:**` notes in the technique index point at source-only analysis docs. They are
  **attribution/provenance only** — not required to use any technique.
- The source library's giant prompt **catalog** (`PROMPT_INDEX.*`) is intentionally **not** copied —
  it indexes the source repo's prompts, not yours. As your project accumulates prompts, index them
  yourself (see `guides/NEW_RESOURCE_CHECKLIST.md`).

---

## Quick start for faceless content

Go straight to [`content-playbook/CONTENT_QUICK_START.md`](content-playbook/CONTENT_QUICK_START.md).
First build a voice bible (`content-playbook/starter-prompts/content_series_channel_bible.md`), then
reuse it across the script, hook, SEO, thumbnail, and repurpose prompts.

---

**Extracted:** 2026-05-27 · **Engine is tool-agnostic; the resource-patterns/ layer assumes Claude Code.**
