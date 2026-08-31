# ADR-0005 — Quality and maturity are separate axes

## Status

Accepted. Not yet implemented.

## Context

The repository already has a quality vocabulary, and it is load-bearing:
`PROMPT_QUALITY_STANDARDS.md` defines Tier 1 / Tier 2 / Tier 3; several
resources are labelled Gold Standard; whole domains mark high-fabrication-risk
prompts STRONG-GUARD; `domain-psychology` sets `intended_use: model-testing`.
These describe *how well a resource is written* against the house style.

Productization needs a different question answered: *how much review and
evaluation evidence exists for this resource as a product asset?* A Tier-1
prompt can be beautifully authored and never evaluated. A structurally valid
resource is not thereby a reliable one.

Collapsing the two would silently relabel authoring craft as product assurance —
the exact overclaim the project must avoid.

## Decision

Keep two axes.

**Quality** — preserve the existing repository concepts unchanged. Tier 1/2/3,
Gold Standard, STRONG-GUARD, and domain-specific labels are not remapped into
lifecycle states.

**Maturity** — a separate PAE lifecycle field with four states:

| State | Meaning |
|---|---|
| `experimental` | Usable, still under development or lacking review/evaluation |
| `candidate` | Structurally valid and reviewed, not yet covered by behavioral evaluation |
| `stable` | Schema-valid, reviewed, relevant automated checks passing, and behaviorally evaluated where that applies |
| `deprecated` | Retained for compatibility or history, with a documented replacement or reason |

**Conservative migration default.** A resource without sufficient evidence gets
`maturity = experimental`, `review_status = unreviewed`/`unknown`,
`eval_status = untested`/`unknown`. It is *not* omitted because its frontmatter
is incomplete, and it is *not* marked stable because it passes structural
validation. The corpus is not stable by default.

## Consequences

- Both fields can be reported, filtered, and evaluated independently, and a
  claim about one never implies the other.
- Most of the corpus will begin at `experimental`, which is accurate rather than
  flattering, and gives evaluation work a visible target.
- Promotion to `stable` requires evidence that does not exist yet, so it is
  gated behind the evaluation harness on the roadmap.
