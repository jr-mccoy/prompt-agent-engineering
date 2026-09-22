# Stage 5 — Report and Claim Safety (Gate B)

*This is the gate that protects you, not the client.*

**Objective:** Write the report, then refuse to ship it if it claims more than
the evidence supports.

**When to Use:** After Stage 4, on every deliverable that leaves the building —
report, summary, slide, case study.

**When NOT to use:** On working notes. Running it over prose that is not a
claim-bearing deliverable produces noise and trains you to ignore it.

## Method

1. Draft the report from `audit/findings.md`. Keep findings and recommendations
   in separate sections, as Stage 4 produced them.
2. Write `## Limitations` **from this run**, not from the last one. At minimum:
   what is specific to this corpus, config and commit; what fraction of the
   rubric was observable; that lexical clustering cannot see a paraphrase; how
   scores were obtained; and that author is not reviewer.
3. Stamp every figure drawn from a fixture or sample run with
   `SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE`.
4. `python3 skills/claim-safety/scripts/claim_guard.py <report.md>`
5. Fix each finding by **removing the claim or adding the evidence**. Moving a
   sentence into a code fence is legitimate only when it genuinely is a quoted
   counter-example.
6. Re-run until Gate B passes. Any finding blocks; there is no advisory tier.

## Gate B — CLAIM-SAFE

| Rule | Blocks |
|---|---|
| `forbidden_sentence` | the claims ADR-0040 forbids by name |
| `unlicensed_direction` | a directional word beside a quantity with no interval |
| `roi_or_money_claim` | payback, ROI, "pays for itself", a currency figure |
| `undisclosed_tier` | "is Tier N" stated as a fact |
| `fixture_figure_unstamped` | fixture figures with no synthetic stamp |
| `missing_limitations` | quantities with no Limitations section, or too thin a one |

## Output

A report that passes Gate B, plus the gate's clean output attached to the
engagement record. The clean run is itself worth keeping: it is the evidence
that the claims were checked.

## Verification

- [ ] Gate B passes with zero findings.
- [ ] Limitations were written from this run.
- [ ] Every fixture-derived figure carries the stamp.
- [ ] No sentence claims a direction the evidence cannot license.
- [ ] Findings and recommendations are still separate after editing.

## False-Positive Prevention

1. **A number the client wants is still a number you cannot support.** "Roughly
   what would consolidation save us?" is answered with what you measured — the
   cluster count — and an explicit statement that usage was not measured.
2. **Do not fence a claim to get past the gate.** The fence exists for quoted
   counter-examples. Using it to smuggle a claim defeats the only mechanism
   protecting you from that claim later.
3. **Limitations copied from a previous engagement are worse than none.** They
   read as boilerplate and they will be wrong about this corpus.
4. **Gate B cannot tell you a number is true.** A false figure, correctly
   hedged, passes. This is the last check before shipping and never the only
   one.

## Related

- `skills/claim-safety/SKILL.md`; `references/forbidden-claims.md` for a
  rewrite of every blocked pattern.
- Next: `stage-6-registry-handback.md`.
