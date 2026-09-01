# ADR-0004 — The registry normalizes source schemas instead of rewriting the corpus

## Status

Accepted. Not yet implemented.

## Context

Resource metadata in this repository is heterogeneous, and each shape is
heterogeneous *for a reason*:

- domain prompts carry `title`, `category`, `description`, `techniques`, `tags`,
  `difficulty`, `updated`, `related_prompts`;
- skills follow the Claude Agent Skills spec — `name`, `description`, and a
  `metadata` block;
- agents carry `name`, `description`, `model`;
- commands carry their own shape, validated by their own script;
- roughly a sixth of indexed files carry no frontmatter at all.

Eight vendored Google `android/skills` and Anthropic's `skill-creator` are
byte-identical to pinned upstream commits and are kept that way by a re-sync
procedure and a CI drift check. Editing them to add project metadata would break
that guarantee and the Apache-2.0 provenance recorded in
[`../../THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).

Forcing one frontmatter schema across the corpus would mean thousands of edits,
would break the skills' compatibility with the tools that consume them, and is
explicitly a non-goal of productization.

## Decision

Source files keep their native format. The registry is a **generated output**,
not a new format imposed on the corpus.

Per-kind adapters (`PromptAdapter`, `SkillAdapter`, `AgentAdapter`,
`CommandAdapter`, `PersonaAdapter`, `TechniqueAdapter`) read each native shape
and emit one common registry record. The registry schema is the adapters' output
contract.

Project-owned metadata that cannot safely or consistently live in a source file
goes in sidecar records under `meta/registry/`: stable ID, maturity, review
status, evaluation status, license, attribution, provenance, canonical/copy
relations, serving policy, aliases, compatibility.

Vendored resources get their project metadata **only** in the sidecar.

## Consequences

- Adding a resource kind means adding an adapter, not migrating files.
- The registry can be regenerated and its schema versioned independently of the
  corpus.
- Sidecar and source can drift; the generator must treat the source as
  authoritative for fields the source owns, and CI must verify the sidecar still
  refers to resources that exist.
- Byte-identical vendored files stay byte-identical.
