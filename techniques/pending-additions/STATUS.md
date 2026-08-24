# Pending Technique Additions — Status

Durable capture of technique material mined from a strong model in isolated (no-repo-context)
sessions, then dedup-gated against the live index by a repo-side reviewer. This folder holds
material **not yet woven into `MASTER_TECHNIQUE_INDEX.md`**, deliberately sequenced *behind* the
index-integrity cleanup (you don't build a new wing on a cracked foundation).

## Applied in this commit (already live)
- **`audit_technique_index.py`** — index-integrity validator (pre-commit/CI gate).
- **Index integrity pass** — removed 12 dead `new-techniques/` links; removed 6 Quick-Reference
  entries citing undefined QS-01..04 / MA-01..08; fixed mislabels AG-30→AG-32, AG-31→AG-33,
  QA-11→QA-01, MP-04 name; reconciled the header count to the mechanical entry count (264).
- **House-style block** → `PROMPT_QUALITY_STANDARDS.md` (Tier 1+ patterns, with the
  insufficiency-verdict and proportionality-precedence corrections folded in).
- **Copy-or-Mark + fenced-example + Category-line + verdict-rule guidance** → `authoring/NEW_PROMPT_TEMPLATE.md`.
- **`/review-prompt` skill** → `domain-agentic-resources/skills/review-prompt/SKILL.md`.

## INTEGRATED into the index (2026-07-08)
The docs in this folder are now **provenance/archive** — the techniques are live in
`MASTER_TECHNIQUE_INDEX.md` (active count 293 → 327; validator passes all hard checks).

| Source doc | Integrated as |
|---|---|
| `TECHNIQUE_INDEX_ADDITIONS.md` (Session 0 + 1) | QA-23 (Question tier), QA-24 (Dismissed-candidates table), QA-25 (Two-executor divergence), QA-26 (First-invented-fact), QA-27 (Pressure-minus-counterweight), QA-28 (Findings-vs-presentation triage), OC-13 (Two-axis verdict), RT-23 (Input provenance + sensitivity/Overrides variants), DD-12 (Sweep-with-budget) |
| `TECHNIQUE_FAMILY_inter_prompt_contracts.md` | new **IPC** family, IPC-01..IPC-14 |
| `TECHNIQUE_CLUSTER_action_gating.md` | new **GT** family, GT-01..GT-11 (friction ceiling = GT-08) |
| adjacent-prompt fencing | **merged into AG-38** as a variant (not a new ID) |
| `CANDIDATE_LEDGER.md` / `INGESTION_CHANGESET.md` | provenance + the Session-0 prompt-batch plan (prompts still to be authored/relocated) |

The "negative-space accounting" umbrella term was **not** minted as an ID (avoids the SV-14
"Negative Space Control" clash); it lives as the framing note in `PROMPT_QUALITY_STANDARDS.md`.

## Session-0 prompt files — LANDED (2026-07-08)
All five are now in the repo with changeset fixes applied and every cross-reference verified:
- `domain-software-engineering/analysis/quality/quality_pull_request_diff_review.md` (category → `code-analysis/quality`)
- `domain-software-engineering/analysis/quality/quality_concurrency_race_condition_audit.md` (category fixed; Example Output fenced)
- `domain-decision-making/decisioning_prioritization_framework_selector.md`
- `domain-decision-making/decisioning_opportunity_sunk_cost_audit.md` (numeric-recount step added; example units reconciled)
- `domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` (relocated from decision-making; category → `engineering-workflows/planning`)

## Still open
- **A2 — error-handling & resilience audit** (`code-analysis/quality`): not yet authored. The PR-review
  and concurrency prompts originally cross-referenced it; those links were repointed to the existing
  `quality_error_analysis.md` so nothing dangles. Author A2 as a future item, then optionally restore the links.
- **PROMPT_INDEX.json / PROMPT_INDEX.md**: regenerate to include the 5 new prompts (+ the 34 index techniques).
- **Mining backlog**: one open new-shape tension remains (T18 resumable state).

## Prerequisite before integration: CLEARED — index passes all hard checks
The earlier report of "43 undefined refs + 2 duplicate headings" was largely a **validator
artifact**, not a document defect: the first-pass validator only recognized `### ID:` headings and
did not skip fenced code blocks, so it (a) missed the ~38 techniques legitimately defined in
`**ID: Name**` bold form under *High-Priority Techniques – Phase 1 Integration*, and (b) counted the
merge/deprecation **demos** (ST-03, SV-04) that are already inside ```` ```markdown ```` fences.

The validator was rewritten to be **fence-aware** and to recognize every real definition form
(`###`/`####` headings, `**bold**` entries, multi-ID groups `A/B/C:`, `*(Merged from …)*`,
`→ Merged into`, and `(also ID)` aliases), and to ignore ID-shaped strings whose prefix is not a
real technique namespace (e.g. external `AP-*` anti-patterns). After the genuine fixes from the
prior commit, the index now reports:

- **Referenced-but-undefined IDs: 0** · **Duplicate structural definitions: 0** · **Dead links: 0** → **PASS**
- Header corrected to the honest count: **293 active technique definitions** (264 with full `###`
  entries + 29 bold-catalogued) plus 10 deprecated/merged stubs. *(The intermediate "264" figure
  was itself a naive `###`-only miscount; the original "293 active" was correct.)*
- 5 remaining **soft** mislabel warnings are legitimate shorthand/range descriptors in comparison
  prose (advisory only; they do not gate).

The ID namespace is therefore clean and the technique-content additions below can be integrated.

## Decisions recorded
- **DoD/AC builder** → relocate to `domain-engineering-workflows/workflows/` (category `engineering-workflows/planning`).
- **A2 error-handling resilience audit** → author (resolves two dangling cross-refs in the Session-0 batch).

## Provenance
Mined across 5 sessions; each mechanism dedup-checked against the live index before promotion.
Full audit trail in `CANDIDATE_LEDGER.md`.
