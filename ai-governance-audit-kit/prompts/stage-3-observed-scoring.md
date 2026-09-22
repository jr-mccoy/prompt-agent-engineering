# Stage 3 — Observed Scoring (Gate A)

*A score without a named rubric version and a stated provenance is not a
finding.*

**Objective:** Score each artifact from what is in it, disclose that the score
was observed rather than self-reported, and report it against the observable
maximum rather than against the rubric's 100.

**When to Use:** After Stage 1, on every artifact the engagement covers.

**When NOT to use:** To decide whether an artifact is *good*. Most of that
lives in the 46 points no regex can read.

## Method

1. For each bundle: `python3 skills/observed-scoring/scripts/observed_score.py <bundle> --json`
2. Read **blocking findings** first. A credential, an absolute user path or a
   contact detail caps the verdict regardless of the total, and each is
   reported with a file and a line.
3. Read the coverage as `observed / observable_max`. Never as a percentage of
   100 — see False-Positive Prevention.
4. Where `self_reported` is populated, put it **beside** the observed figure in
   the report. The gap is one of the more useful findings an audit produces.
5. Check Gate A on every record you intend to publish.

## Gate A — SCOREABLE

A score record must carry:

- `rubric.name` — the standard it was scored against;
- `rubric.version` — a string resolvable again in a year;
- `provenance` — `observed` or `self_reported`, never absent;
- `tier: null` — a tier asserted as a fact is refused;
- no category above its stated observable maximum.

`python3 skills/observed-scoring/scripts/observed_score.py --gate-a <score.json>`
checks an existing record.

## The denominator

| Category | Rubric points | Observable |
|---|---|---|
| Metadata | 20 | 11 |
| Structure | 20 | 14 |
| Content | 25 | 7 |
| Resources | 15 | 9 |
| Safety | 20 | 13 |
| **Total** | **100** | **54** |

## Output

One score record per artifact, plus a findings list where every entry names a
check, a path, and what was seen.

## Verification

- [ ] Gate A passes for every published score.
- [ ] Every figure is quoted against `observable_max`.
- [ ] `tier` is null everywhere.
- [ ] Every blocking finding names a file and a line.
- [ ] Self-reported blocks are reported separately, never merged.

## False-Positive Prevention

1. **`54/100` is the misreport this design exists to prevent.** The figure is
   54 of 54 *observable* points. Writing it against 100 implies the artifact
   failed 46 checks that were never run.
2. **A low `cat3_content` is not evidence of bad content.** Seven of 25 points
   are observable there. It means three structures are absent.
3. **A high observable score is not a recommendation.** It says the structure
   is present. Whether the content is right is a human's call, and
   `meta/adr/0041-author-reviewer-separation.md` says it should not be the
   author's.
4. **Do not aggregate scores into a corpus average.** An average over an
   observable subset, presented as corpus quality, is a claim Gate B will
   block and should.

## Related

- `skills/observed-scoring/SKILL.md`; `references/detectors.md` for every
  detector and the false positive each narrow pattern prevents.
- Next: `stage-4-governance-findings.md`.
