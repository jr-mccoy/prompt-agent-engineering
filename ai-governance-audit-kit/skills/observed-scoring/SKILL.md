---
name: observed-scoring
description: Score an artifact from what is in it rather than from what its author claims about it, and disclose which of the two you did. Use this skill to "score our skills against a rubric", "audit skill quality", "which bundles have security problems", "check our prompts against the authoring standard", or when a score has to survive someone asking where it came from. Runs Gate A, reports an observable subset with the subset's own maximum, and never asserts a quality tier.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/observed_score.py --self-check` proves the clean fixture scores 54/54, the defective fixture is capped by its blocking security findings, no tier is emitted for either, and Gate A refuses four separately-defective score records. No network, no writes.
metadata:
  tags: [audit, scoring, rubric, security, governance, gate, provenance]
  updated: "2026-09-22"
---

# Observed Scoring

## Purpose

`agentic-system-factory/scripts/score_rubric.py` scores a `<!-- RUBRIC -->`
block the author wrote about their own bundle, and says so in its own honesty
caveat. That is the right design for a curator scoring their own work, and it
is unusable in an audit, because the thing under audit *is* the author's
account of their work.

This skill keeps that scorer's caps, its load-bearing minimum, its capping
behaviour, its CLI and its exit-code contract, and replaces the parser with
**detectors that read the artifact**. Every detector is pure regex or a
filesystem fact. Nothing here needs a model.

## The denominator is the honest part

Most of the 100-point authoring rubric is not mechanically observable.
"Describes WHAT the skill does", "logical section ordering" and "content is
accurate" are judgements. Scoring them with a regex and printing 100 as the
denominator would fabricate a rubric score — precisely what
`pae_registry/governance.py` refuses when it declines to infer a tier from
document structure.

So the report is an **observable subset with its own maximum stated beside every
figure**: 54 of the rubric's 100 points, and `tier: null`.

| Category | Rubric points | Observable here |
|---|---|---|
| Metadata | 20 | 11 |
| Structure | 20 | 14 |
| Content | 25 | 7 |
| Resources | 15 | 9 |
| Safety | 20 | 13 |
| **Total** | **100** | **54** |

## When to Use

- You need a score a client can challenge and you can defend line by line.
- You need the security findings — a credential, an absolute user path, a
  contact detail — located to a file and a line.
- You need to compare what an author claimed with what is there. The gap
  between the observed score and a self-reported block is itself a finding.

## When NOT to Use

- To decide whether an artifact is *good*. The 46 unobservable points are where
  most of that lives, and `authoring/skill-patterns/SKILL_QUALITY_RUBRIC.md`
  expects a human.
- To score this repository's own resources for governance. Nothing here
  promotes anything: `pae_registry/governance.py` owns that refusal.

## Instructions

1. Run `scripts/observed_score.py <bundle>` for each skill bundle, or
   `--json` to capture the record.
2. Read **blocking findings** first. The rubric's own "Must Pass" security
   checks cap the verdict regardless of the total, the same way the factory's
   `SECURITY_MIN` caps a tier regardless of the total.
3. Read the coverage as `observed / observable_max`, never as a percentage of
   100. Quoting `54/100` would be the misreport this design exists to prevent.
4. Check **Gate A** on every score you intend to publish: a rubric name, a
   rubric version and a stated provenance, or it is not a finding.
5. Where `self_reported` is populated, report it **beside** the observed score.
   Merging them destroys the comparison.

## Bundled Resources

- `scripts/observed_score.py` — the detectors, the scoring, and Gate A.
- `references/detectors.md` — every detector, what it matches, what it
  deliberately does not, and the false positive each narrow pattern prevents.

## Safety

Read-only. Security detectors run on the **unstripped** text and across the
whole bundle, because a credential inside a code fence is still a credential in
the file and a bundled script is the likelier place to find one. Prose
detectors run on text with fences removed, so a documented example never scores
as the real thing.

## Troubleshooting

- A date is reported as a contact detail: the phone pattern is too loose. The
  shipped one is deliberately narrow for exactly this reason — see
  `references/detectors.md`.
- A good bundle scores low on `cat3_content`: only 7 of 25 content points are
  observable. That is the denominator working, not a defect.

## Verification

- [ ] Gate A passes for every published score.
- [ ] Every figure is quoted against `observable_max`, never against 100.
- [ ] `tier` is null in every record.
- [ ] Every blocking finding names a file and a line.

## Related Skills

- `corpus-inventory` — tells this skill what to score.
- `claim-safety` — stops the report quoting these numbers as performance.
