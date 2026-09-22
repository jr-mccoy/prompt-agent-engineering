---
name: corpus-inventory
description: Discover what is actually in a prompt or agent corpus, from a config rather than from hard-coded roots, and refuse to audit one that cannot be inventoried. Use this skill to "inventory our prompt library", "what resources do we actually have", "audit a client corpus", "how many prompts are there really", or when you need a counted partition of a tree into resources and recorded exclusions. Runs Gate 0, assigns a durable UID and public ID to every artifact, and records every excluded file with the reason it was excluded.
license: MIT
compatibility: Standard library only, Python 3.9+, plus the PAE checkout it ships inside for `pae_registry.identity`. `scripts/inventory.py --self-check` proves Gate 0 blocks an empty corpus, that a bare-segment exclusion is rejected, and that a misordered kind detector is rejected. No network, no writes unless `--out` is given.
metadata:
  tags: [audit, inventory, membership, governance, gate, corpus]
  updated: "2026-09-22"
---

# Corpus Inventory

## Purpose

Every governance conversation about a prompt library starts with a number
nobody can defend. "We have about four hundred prompts" turns out to mean four
hundred markdown files, of which a third are READMEs, templates, or a vendored
copy of somebody else's library.

This skill produces the defensible version: a **counted partition** of the tree
into artifacts that are resources and files that are not, where every exclusion
carries the reason it was excluded. Then it refuses to go further if the answer
is zero.

## When to Use

- At the start of any corpus audit, before anything is scored or clustered.
- When a client disputes a count and you need the partition, not the total.
- When you need durable identities for artifacts that have never had any.

## When NOT to Use

- To audit *this* repository. `scripts/generate_registry.py` already does that,
  with membership rules tuned to this tree over many phases.
- To judge quality. This skill counts and identifies; `observed-scoring` scores.

## Instructions

1. Write the corpus's membership rules into `config/audit.json` — roots,
   component directories, meta-document filenames, anchored non-resource
   prefixes, and the ordered kind detectors. Nothing is guessed from the tree.
2. Run `scripts/inventory.py <corpus> --out audit/inventory.json`.
3. Read **Gate 0** first. A block means the config matches nothing or the corpus
   is empty; both are reasons to stop, not to report a clean corpus.
4. Read the `excluded` counts next, before the resource count. A partition where
   most files are excluded is a finding about the config, the tree, or both.
5. Hand `audit/inventory.json` to `duplication-clusters` and `observed-scoring`.
   Every later stage reads this file; none of them re-walks the tree.

## The invariant that is enforced, not documented

Exclusions are **anchored path prefixes, never bare directory names**. A
bare-segment blocklist is provably wrong, and `references/membership.md` carries
the worked example: `agents/documentation/` is a category of
documentation-*writing* agents while `documentation/` is documentation *about*
resources, and a segment rule on `documentation` deletes the first while
intending to remove the second. `validate_config` rejects a prefix with no `/`
in it, so the invariant cannot be lost to a well-meaning edit.

## Bundled Resources

- `scripts/inventory.py` — discovery, classification, identity and Gate 0.
- `references/membership.md` — the precedence order, the prefix invariant and
  its worked example, and what each exclusion reason means.

## Safety

The script is read-only unless `--out` is given, and `--out` writes only the
path you name. It never writes into the corpus; that is `registry-handback`'s
job and it is gated separately.

## Troubleshooting

- Gate 0 blocks with "the config matches nothing": the roots exist but every
  file under them was excluded. Check `non_resource_prefixes` first.
- "identity cannot be derived": a path whose components normalize to nothing
  (all punctuation, or a bare extension). Rename it or exclude it deliberately.

## Verification

- [ ] Gate 0 passed, and the resource count is non-zero.
- [ ] Every exclusion reason is one you can justify to the corpus owner.
- [ ] No duplicate public IDs (Gate 0 blocks on these, because a handback
      carrying one would fail `pae validate-registry`).

## Related Skills

- `duplication-clusters` — reads this inventory and finds repeats.
- `observed-scoring` — reads this inventory and scores what it found.
- `registry-handback` — turns all of it into a registry the Engine can open.
