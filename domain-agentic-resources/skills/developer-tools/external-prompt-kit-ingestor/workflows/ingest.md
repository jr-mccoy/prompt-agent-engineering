# Ingest Workflow

End-to-end procedure for absorbing an external prompt kit. Each phase has a gate check — do not proceed until the gate passes.

## Phase 1: Inventory

**Goal:** Produce a numbered list of every distinct prompt in the source.

Steps:
1. Read the source file fully.
2. Identify prompt boundaries. Signals: code/quote blocks, `<role>`/`<instructions>` XML tags, "Prompt N:" headings, "Copy this prompt" call-outs, fenced markdown.
3. For each prompt, capture: working title, one-sentence purpose, approximate length, whether it includes role/instructions/output/guardrails sections.
4. Note any prompts that are partial fragments, code samples, or examples — these are NOT ingestion candidates.

**Gate check:** You can list every prompt by number, name, and purpose. If the source is ambiguous about boundaries, ask the user before proceeding.

## Phase 2: Classify

**Goal:** Assign each prompt to a domain, category, and difficulty.

Steps:
1. For each prompt, consult the "Category Mapping" section of `meta/ROUTING_REFERENCE.md`.
2. Assign:
   - **Domain directory** (e.g., `domain-engineering-workflows/ai-patterns/`)
   - **Category slug** for frontmatter (e.g., `ai-patterns`, `analysis/security`)
   - **Difficulty** — beginner | intermediate | advanced
3. If no existing subdirectory fits and the kit introduces 2+ prompts of a coherent new pattern family, propose a new subdirectory and justify it in writing before creating.
4. Avoid sprawl: do not create new top-level domains. Add subdirectories only.

**Gate check:** Every prompt has a target path. Any new subdirectory has a written justification.

## Phase 3: Map Techniques

**Goal:** Tag each prompt with 3–7 valid technique IDs from `techniques/MASTER_TECHNIQUE_INDEX.md`.

Steps:
1. Open `techniques/MASTER_TECHNIQUE_INDEX.md` (read once; do not re-read per prompt).
2. For each prompt, identify the dominant patterns it uses. Common matches:
   - Gated multi-phase flow → `NE-02` (Phased Workflow Architecture)
   - Adversarial check / red-team → `RT-07` (Cascade Effect Analysis), `QA-21` (Metric Gaming Vector Enumeration)
   - Constraint blocks (`<guardrails>`) → `CM-02` (Constraint Specification)
   - Verification step / self-audit → `QA-08` (Gate-Based Verification)
   - Conditional output (verdict A vs B) → `OC-04` (Conditional Output Logic)
   - Metric definition → `DS-02` (Metric Specification)
3. Apply the rules in `references/technique-promotion-criteria.md` to decide whether any pattern in the kit is genuinely novel.
4. If novel: draft a new technique entry (ID, name, description, when-to-use, example, see-also) and append it to `techniques/MASTER_TECHNIQUE_INDEX.md`. Use the next sequential ID in the appropriate category (AG, QA, DS, etc.).
5. Update `techniques/USE_CASE_LOOKUP.md` if the new technique fits a documented use case.

**Gate check:** Every prompt has 3+ valid IDs. Any new IDs are appended to the master index with full definitions, not just IDs in frontmatter.

## Phase 4: Structure

**Goal:** Generate one Tier-1 markdown file per prompt.

Use `references/frontmatter-template.md` as the canonical skeleton. For each prompt:

1. Filename: `{category-slug}_{specific_function}.md` (lowercase, underscores). For agentic patterns prefer `workflow_agent_{topic}.md` to match the existing convention in `domain-engineering-workflows/ai-patterns/`.
2. Frontmatter fields (all required):
   - `title` — descriptive, title case, no quotes around hyphens
   - `category` — matches the directory the file lives in
   - `description` — one sentence describing what the prompt does
   - `techniques` — list of valid IDs from Phase 3
   - `tags` — 3–6 lowercase keyword tags for search
   - `difficulty` — beginner | intermediate | advanced
   - `updated` — today's date in `YYYY-MM-DD`
   - `related_prompts` — at least one cross-reference (other prompts in the same kit count)
3. Body sections (in order):
   - `# {Title}`
   - `**Purpose:**` one-sentence
   - `**When to use:**` one-sentence
   - `**What you'll get:**` one-sentence
   - `**Source:**` `{original-kit-filename}.md`
   - A fenced ```markdown block containing the verbatim prompt as-given by the source author (do not paraphrase the prompt itself — that's the deliverable)
   - Optional: `## Notes` for repo-specific guidance

**Gate check:** Each file passes the validation checklist in `references/ingestion-checklist.md`.

## Phase 5: Place

**Goal:** Write files to disk in the correct location.

Steps:
1. Confirm target directory exists; create if a Phase-2 justification exists.
2. Write each file. Do not overwrite existing prompts without user confirmation — if a target filename collides, append `_v2` or rename.
3. Verify file count matches Phase 1 inventory.

**Gate check:** Filesystem state matches the plan.

## Phase 6: Index

**Goal:** Both repo indexes know about the new prompts.

Steps:
1. Open `PROMPT_INDEX.json`. Append one entry per new prompt at the appropriate location (preserve sort order if any). Required fields: `path`, `title`, `domain`, `category`, `description`, `techniques`, `tags`, `difficulty`, `keywords`.
2. Open `PROMPT_INDEX.md`. Append one row per new prompt to the appropriate domain section table.
3. If the repo has an `update-index` script (check `scripts/`), prefer running it over manual edits.

**Gate check:** Grep for each new filename in both index files returns a hit.

## Phase 7: Back-Reference

**Goal:** Source file points at its structured derivatives.

Edit the top of the source kit file to add (above any existing content):

```
> **Repository note:** Structured prompt versions from this kit are now available in `{target-directory}/` as:
> - `{file_1}.md`
> - `{file_2}.md`
> - `{file_3}.md`

```

Do not modify any other content in the source file. Preserve the author's narrative verbatim.

**Gate check:** Source file opens with the repository note. No other lines changed.

## Phase 8: Implications Memo

**Goal:** A short written analysis delivered to the user, not committed to a file unless requested.

Cover, in this order:
1. **Pattern family** — What category of work does this kit address? Is it new to the repo or reinforcing an existing pattern?
2. **Cross-references** — Which existing prompts, skills, or agents now share lineage with these? Suggest concrete cross-link edits.
3. **Technique impact** — Did this kit introduce new technique IDs? If so, name them and describe the broader use cases they unlock beyond this kit.
4. **Gaps exposed** — What's missing from the repo that this kit makes obvious? (e.g., the kit covers "audit before doing X" but the repo has no prompt for "doing X itself".)
5. **Follow-up suggestions** — 1–3 concrete next prompts, skills, or agents worth building.

Keep the memo to ~200–400 words. Direct prose, no fluff.

## When to Stop

Stop after the implications memo. Do **not**:
- Re-read files you already wrote
- Re-verify indexes after a successful Edit
- Commit changes unless the user asks
- Build the follow-up resources you suggested unless the user requests them
