# Stage 6 — Registry Handback (Gate C)

*The deliverable is a corpus that works, not a document about one.*

**Objective:** Write a conformant PAE registry into the client's tree so the
unmodified Engine — search, routing, context bundling, validation, MCP — runs
on their corpus, and prove it in their own shell.

**When to Use:** At the end of the engagement, and once mid-engagement to prove
the pipeline end to end before the report is written.

**When NOT to use:** Before Gate 0 passes. A registry built from an empty
inventory is a confident, empty, wrong answer, and `produce()` refuses.

## Method

1. **Dry run first:** `python3 skills/registry-handback/scripts/handback.py <corpus>`.
   The registry is built and validated in a staged copy; the corpus is
   untouched.
2. Read Gate C. The verdict is the Engine's own `validate_registry` result with
   checksums verified — not an inspection of whether the files look right.
3. Fix findings **at their source**. A `duplicate_public_id` is a corpus
   problem; fixing it in the registry would hide it.
4. `python3 skills/registry-handback/scripts/handback.py <corpus> --write`
5. **Prove it in the client's shell**, not yours:

   ```bash
   PAE_REPO=/path/to/their/corpus pae stats
   PAE_REPO=/path/to/their/corpus pae search "<something they know is there>"
   PAE_REPO=/path/to/their/corpus pae validate-registry
   ```

   Pick the search term with them, from a problem they actually have.

## Gate C — HANDBACK COMPLETE

Blocks unless both marker files exist, the Engine can open the tree, and
validation returns no issues with checksums verified. It additionally fails if
`assert_nothing_invented()` finds a copy edge, a review status, or a
tier-shaped quality scheme in any record, or if any score would fail Gate A.

## What the handback deliberately does not say

| Field | Written | Why not more |
|---|---|---|
| `governance.review_status` | `unknown` | nothing was recorded; inventing one fabricates a rubric score |
| `relationships.copy_of` | `null` | copies come from explicit edges, never hashes or filenames |
| `license.status` | `unresolved` | guessing a client's licensing is the most expensive possible error |
| `quality[].scheme` | `structural-coverage-observed` | the name says what the number is and how it was obtained |

Cluster findings ride as `diagnostics` with their evidence, so the client can
adjudicate and then assert the edges themselves.

## Output

`meta/registry/registry.jsonl` and `meta/registry/registry-summary.json` inside
the client's corpus, plus the transcript of the three `PAE_REPO` commands run
in front of them.

## Verification

- [ ] Gate C passes with checksums verified.
- [ ] The three `PAE_REPO` commands ran in the client's environment.
- [ ] `assert_nothing_invented()` returned empty.
- [ ] The client knows the registry is generated and how to regenerate it.

## False-Positive Prevention

1. **Files that look right are not a handback.** The only proof is the Engine
   opening the tree. That is why Gate C calls the validator rather than
   checking shapes.
2. **Do not hand-edit either marker file.** They are generated together and
   `summary_drift` will catch the disagreement — after the client has it.
3. **A registry outside the corpus fails every record.** `source.path` resolves
   against the repository root.
4. **Checksums drift the moment the corpus changes.** If anything moved during
   the engagement, re-run from Stage 1 rather than patching.

## Related

- `skills/registry-handback/SKILL.md`; `references/contract.md` for the exact
  field-by-field contract.
- Next: `stage-7-closeout-and-remediation-plan.md`.
