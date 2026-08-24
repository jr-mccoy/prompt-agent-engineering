# Technique Contribution Guide

How to propose, validate, and register a new prompt-engineering **technique** in this repository.

> **Techniques vs prompts.** A *prompt* is a concrete, reusable instruction set for a task. A *technique* is a reusable, named building block (an ID like `ST-01`, `RT-02`, `QA-01`) that many prompts cite in their frontmatter. The canonical catalog is [`../techniques/MASTER_TECHNIQUE_INDEX.md`](../techniques/MASTER_TECHNIQUE_INDEX.md). This guide is the (previously missing) path for adding to it.

---

## When is something a technique?

Propose a new technique only when **all** of these hold. If it fails any, it's probably a prompt variant or a tip — not a catalog entry.

| Criterion | Bar |
|-----------|-----|
| **Reusable** | It plausibly applies to **≥3 prompts across ≥2 domains** — not a one-off trick for a single prompt. |
| **Demonstrated** | You can show it working in **≥2 concrete prompts** (existing or new), with before/after or example output. |
| **Definable** | You can describe what it does and when to use it in **≤3 sentences**. |
| **Distinct** | It does **not** substantially overlap an existing technique. Search the index first; if it's a specialization, prefer a *variant* of the existing base technique over a brand-new ID. |
| **Categorizable** | It fits one of the 16 existing categories (ST, RT, OC, QA, CM, RP, DT, ED, MP, DS, AG, NE, IT, SV, DD, DP). A genuinely new category is a much bigger proposal — raise it as an issue first. |

When in doubt: **prefer extending an existing technique** (as a documented variant) over minting a new ID. The catalog's value comes from being curated, not exhaustive.

---

## The category prefixes

| Prefix | Category | Prefix | Category |
|--------|----------|--------|----------|
| `ST` | Structural | `MP` | Meta-Prompting |
| `RT` | Reasoning | `DS` | Domain-Specific |
| `OC` | Output Control | `AG` | Agentic |
| `QA` | Quality Assurance | `NE` | Non-Engineering |
| `CM` | Context Management | `IT` | Interaction |
| `RP` | Role & Perspective | `SV` | Specialized Visual |
| `DT` | Decomposition | `DD` | Done Definition |
| `ED` | Educational | `DP` | Delegation & Productivity |

---

## Proposal template

Open an issue (or PR) titled `technique: <short name>` containing:

```markdown
## Proposed technique
**Name:** [Short, descriptive name]
**Category:** [ST | RT | OC | QA | CM | RP | DT | ED | MP | DS | AG | NE | IT | SV | DD | DP]
**Definition (≤3 sentences):** [What it does and when to use it]

## Why it's distinct
[Which existing techniques are closest, and why this isn't just one of them.
If it's a specialization, say which base technique it extends.]

## Evidence it generalizes
- Prompt 1: [path or proposed path] — how the technique is used
- Prompt 2: [path or proposed path] — how the technique is used
- (More if available)

## Example (before / after or sample output)
[Concrete demonstration of the effect]

## Suggested ID
[e.g. QA-XX — maintainers assign the final number]
```

---

## Review & acceptance

1. **Discussion.** Maintainers review against the criteria above. Expect questions about overlap and generalization — this keeps the catalog clean.
2. **ID assignment.** If accepted, a maintainer assigns the next free number in the category (don't hard-assign one yourself; propose, and let review finalize it).
3. **Catalog entry.** Add the technique to [`../techniques/MASTER_TECHNIQUE_INDEX.md`](../techniques/MASTER_TECHNIQUE_INDEX.md) following the existing entry format (name, description, when to use, relationship to neighboring techniques, example). If relevant, add it to [`../techniques/USE_CASE_LOOKUP.md`](../techniques/USE_CASE_LOOKUP.md).
4. **Backfill.** Reference the new ID in the `techniques:` frontmatter of the prompts that demonstrate it, and re-run `python3 ../scripts/generate_prompt_index.py`. Run `python3 ../scripts/validate_technique_catalog.py` to confirm every reference resolves.

---

## Deprecating or merging a technique

The catalog already supports retirement: deprecated/merged IDs remain as **stubs** that point to their replacement (the index header tracks these). To deprecate or merge:

- Don't delete the ID — convert its entry to a short stub noting what replaced it and why.
- Update prompts that cited the old ID to the surviving one, then regenerate the index.
- Note the change in [`../CHANGELOG.md`](../CHANGELOG.md).

This keeps historical references valid and the catalog honest about its own evolution.

---

## Attribution

If your technique is based on published work (a paper, a well-known method, your own research), cite the source in the catalog entry. External contributors are credited; if you're formalizing a technique you published independently, say so in the proposal so the attribution can be recorded.

---

**See also:** [`NEW_PROMPT_TEMPLATE.md`](NEW_PROMPT_TEMPLATE.md) · [`../PROMPT_QUALITY_STANDARDS.md`](../PROMPT_QUALITY_STANDARDS.md) · [`../EXTERNAL_CONTRIBUTOR_GUIDE.md`](../EXTERNAL_CONTRIBUTOR_GUIDE.md)
