# Stage 0 — Engagement Config

*This kit reports structure. It does not review content, assert a quality tier,
assert a copy relationship, or determine a licence. Say so to the client before
Stage 1, not in the report.*

**Objective:** Turn what the client says about their corpus into
`config/audit.json`, so that every later stage runs on declared rules rather
than on guesses about their tree.

**When to Use:** Once, at the start of an engagement, before anything is walked.

**When NOT to use:** To audit this repository — `scripts/generate_registry.py`
already does that with membership rules tuned to this tree over many phases.

## Inputs to gather

1. **What counts as a resource.** Which directories hold artifacts people are
   meant to use? Get the list from someone who uses them, not from the tree.
2. **What is deliberately not a resource.** Vendored imports, drafts, archives,
   generated exports. Every one becomes an **anchored path prefix** ending in
   `/`. A bare directory name is rejected by config validation, and
   `references/membership.md` has the worked example explaining why.
3. **Meta documents.** Which filenames are documentation *about* the corpus
   rather than part of it. `README.md` almost always; ask about the rest.
4. **Bundled components.** Which subdirectory names belong to a parent resource
   — `references/`, `scripts/`, `assets/` and so on.
5. **Kinds, in precedence order.** How to tell a skill from an agent from a
   prompt in *their* convention. Exactly one fallback, and it must be last.
6. **The rubric.** Which authoring standard the corpus is meant to meet, and
   its version string. Gate A refuses a score that cannot name one.
7. **The scope prefix.** A short identifier for the corpus, used in every
   public ID. It becomes part of a durable identity, so agree it now.

## Method

1. Draft `config/audit.json` from the answers. Do not copy the shipped sample's
   roots — they describe the fixture corpus, not the client's.
2. Run `python3 skills/corpus-inventory/scripts/inventory.py <corpus>` and read
   the **exclusion counts before the resource count**.
3. Walk the exclusions with the client. "Two hundred files excluded as
   `non_resource_prefix`" is a conversation, not a config detail.
4. Iterate until both of you can defend the partition. The partition *is* the
   scope of the engagement; everything later inherits it.
5. Record what was agreed and what was contested. A contested exclusion belongs
   in the report's limitations.

## Output

`config/audit.json`, plus a short scope note naming:

- the roots, and who confirmed them
- every non-resource prefix, and the reason it is excluded
- the rubric and version Gate A will require
- anything the client and you did not agree on

## Verification

- [ ] `validate_config` returns no errors (the script refuses to run otherwise).
- [ ] Every non-resource prefix is anchored and ends with `/`.
- [ ] Exactly one kind detector is a fallback, and it is last.
- [ ] The exclusion counts have been read aloud to the client.
- [ ] The rubric version is a string you could resolve again in a year.

## False-Positive Prevention

1. **A clean corpus and an unmatched config look identical from the total.**
   Both report few resources. Gate 0 separates them; read its message rather
   than the count.
2. **Do not widen the roots to make the number bigger.** A larger resource count
   that includes templates and archives is a worse answer, not a better one.
3. **The client's stated conventions and their tree will disagree.** Where they
   do, the tree is the fact and the disagreement is a finding.

## Related

- `skills/corpus-inventory/SKILL.md` and its `references/membership.md`.
- Next: `stage-1-inventory-the-corpus.md`.
