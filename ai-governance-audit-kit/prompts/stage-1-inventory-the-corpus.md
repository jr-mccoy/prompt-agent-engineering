# Stage 1 — Inventory the Corpus (Gate 0)

*This kit reports structure. It does not review content.*

**Objective:** Produce a counted partition of the corpus into resources and
recorded exclusions, assign a durable identity to every resource, and refuse to
continue if the answer is zero.

**When to Use:** Immediately after Stage 0, and again whenever the config
changes.

**When NOT to use:** As a quality judgement. This stage counts and identifies.

## Method

1. `python3 skills/corpus-inventory/scripts/inventory.py <corpus> --out audit/inventory.json`
2. Read **Gate 0** first, then the exclusions, then the resource count. That
   order is deliberate: the count is the least informative of the three.
3. For each kind, spot-check three artifacts by hand against the detector that
   classified them. A detector that is subtly wrong produces a confident,
   entirely wrong inventory.
4. Record anything Gate 0 blocked on and what you changed to clear it. A
   duplicate public ID cleared by renaming a client file is a change to their
   corpus and belongs in the report.

## Gate 0 — INVENTORIABLE

The gate blocks when:

- a configured root does not exist in the corpus;
- markdown sits under the roots and **every** file was excluded, meaning the
  config matches nothing;
- nothing at all was found;
- an artifact's path yields no derivable identity;
- two artifacts normalise to the same public ID.

It fails closed rather than reporting an empty clean bill of health. That
outcome — a confident, empty, wrong answer — is the one an audit must never
produce by accident, and it is the most likely failure of a misconfigured run.

## Output

`audit/inventory.json`, containing per resource: `uid`, `id`, `path`, `kind`,
`scope`, `title`, `description`, `tags`, `techniques`, `has_frontmatter`,
`bytes`, `lines`, `content_sha256`. Plus `by_kind`, `excluded` with reasons,
`missing_roots`, and the Gate 0 verdict.

Every later stage reads this file. None of them re-walks the tree, so a
correction here propagates and a correction anywhere else does not.

## Verification

- [ ] Gate 0 passed.
- [ ] Every exclusion reason is one you can justify to the corpus owner.
- [ ] Three artifacts per kind were spot-checked against their detector.
- [ ] The resource count was reported *with* the exclusion counts, never alone.

## False-Positive Prevention

1. **A high `outside_root` count is not noise.** It means the roots are
   narrower than the corpus. Confirm that with the owner before proceeding.
2. **`has_frontmatter: false` is not a finding by itself.** Plenty of corpora
   keep metadata elsewhere. It becomes a finding only against a rubric that
   requires frontmatter, which is Stage 3's job.
3. **Do not quote the resource count as a headline.** "We found 412 prompts" is
   the sentence this whole stage exists to replace with a partition.

## Related

- `skills/corpus-inventory/SKILL.md`; `references/membership.md` for precedence.
- Next: `stage-2-duplication-clusters.md`.
