# Dry Run

Every transcript below is a real run against the tracked fixtures in
`samples/`, captured by running the commands shown. Most of the fixtures are
**negative**: a gate proved only against the case it passes has not been
proved.

`SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE.` Everything here
is fixture output. It is not a measurement of any real corpus, and no figure
below generalises past `samples/`.

---

## Gate 0 — inventoriable

`samples/corpus-good` passes. `samples/corpus-empty` holds only meta documents
under the configured roots, so discovery finds nothing and the gate blocks
rather than reporting a clean corpus — the one outcome an audit must never
produce by accident.

The last two checks prove the config invariants: a bare-segment exclusion and a
misordered fallback detector are both refused before anything is walked.

```text
$ python3 skills/corpus-inventory/scripts/inventory.py --self-check
inventory --self-check:
PASS  Gate 0 (inventoriable) — corpus-good
        resources: 6 {'prompt': 4, 'skill': 2}
        excluded:  {'non_resource_prefix': 2, 'meta_document': 1, 'bundled_component': 2}
   -> corpus-good: expected PASS, got PASS [ok]
BLOCK  Gate 0 (inventoriable) — corpus-empty
        resources: 0 {}
        excluded:  {'meta_document': 2}
        - 2 markdown file(s) sit under the configured roots and every one was excluded — the config matches nothing, which is not the same as a clean corpus
   -> corpus-empty: expected BLOCK, got BLOCK [ok]
   -> bare-segment exclusion rejected: ok
   -> misordered fallback rejected: ok
SELF-CHECK PASS
(exit 0)
```

---

## Clustering — exact, candidate, and what is deliberately not clustered

The byte-identical pair is reported as `exact` from the content hash. The
reworded pair is a `candidate` at 0.67. `analysis_incident_timeline.md`, which
shares the corpus but not the subject, is not clustered with either — and the
exact pair is not double-reported as a candidate.

No cluster names a canonical, and no `copy_of` edge appears anywhere in the
output.

```text
$ python3 skills/duplication-clusters/scripts/cluster.py --self-check
cluster --self-check:
clusters — corpus-good (6 artifacts analysed)
  exact:     1
    [exact]     prompts/analysis_dependency_review.md == prompts/analysis_dependency_review_copy.md
  candidate: 2
    [candidate] 0.67  prompts/analysis_dependency_audit.md ~ prompts/analysis_dependency_review.md
    [candidate] 0.64  prompts/analysis_dependency_audit.md ~ prompts/analysis_dependency_review_copy.md
  canonical: never inferred — see the disclosure in the JSON output
   -> the byte-identical pair is reported as exact: ok
   -> no exact cluster names a canonical: ok
   -> the reworded near-duplicate is reported as a candidate: ok
   -> the exact pair is not double-reported as a candidate: ok
   -> an unrelated artifact is not clustered with the dependency set: ok
   -> no cluster asserts a copy_of edge: ok
SELF-CHECK PASS
(exit 0)
```

---

## Gate A — scoreable

`deploy-helper` scores 54 of the 54 mechanically observable points. Note the
denominator: **of 100 rubric points, and tier not asserted**, on every line.

`release-notes` is the defective fixture. Its three blocking security findings —
a credential-shaped assignment, an absolute user path, a contact address — cap
the verdict at `blocked` regardless of the total, and each names its file and
line.

The four Gate A negatives are tracked score records, not inline dictionaries:
one with no rubric version, one with no provenance, one asserting a tier, and
one whose category exceeds its observable maximum.

```text
$ python3 skills/observed-scoring/scripts/observed_score.py --self-check
observed_score --self-check:
PASS  samples/corpus-good/skills/deploy-helper: 54/54 observable (of 100 rubric points; tier not asserted) — clean
   -> deploy-helper: expected PASS, got PASS [ok]
FAIL  samples/corpus-good/skills/release-notes: 26/54 observable (of 100 rubric points; tier not asserted) — blocked
       - name_lowercase: name 'Release_Notes' is not lowercase
       - name_charset: name 'Release_Notes' is not alphanumeric-and-single-hyphens
       - name_matches_directory: name 'Release_Notes' does not match bundle directory 'release-notes'
       - description_length_band: description is 21 characters, outside the 50-500 band
       - description_states_trigger: description names no trigger condition (no "use when" / "activates when" / "when the user")
       - explicit_bundled_references: no bundled resource is referenced explicitly from the body
       - when_to_use_section: no "When to Use" section
       - when_not_to_use_section: no "When NOT to Use" section
       - related_section: no Related section
       - numbered_instruction_steps: fewer than three numbered instruction steps
       - verification_section: no Verification or Validation section
      !! no_hardcoded_secret: credential-shaped assignment at release-notes/SKILL.md:22
      !! no_absolute_user_path: absolute user path '/Users/jdoe/' at release-notes/SKILL.md:23
      !! no_personal_contact: contact detail 'jane.doe@example-corp.test' at release-notes/SKILL.md:24
       - safety_section: no Safety or Warnings section
       - failure_handling_section: no Troubleshooting or failure-handling section
   -> release-notes: expected FAIL, got FAIL [ok]
   -> blocking security finding caps the verdict: ok
   -> no tier is asserted for either fixture: ok
   -> Gate A score_observed_valid.json: expected PASS, got PASS [ok]
   -> Gate A score_no_rubric_version.json: expected BLOCK, got BLOCK (rubric.version is missing; a score that cannot be tied to a rubric version cannot be re-run or disputed) [ok]
   -> Gate A score_no_provenance.json: expected BLOCK, got BLOCK (provenance None is not one of ('observed', 'self_reported'); an undisclosed score cannot be told apart from the author's own) [ok]
   -> Gate A score_tier_asserted.json: expected BLOCK, got BLOCK (tier 'Tier 3' is asserted; this kit may report structural findings and disclosed scores, never a quality tier as a fact) [ok]
   -> Gate A score_over_cap.json: expected BLOCK, got BLOCK (cat5_safety=20 exceeds its observable maximum 13) [ok]
SELF-CHECK PASS
(exit 0)
```

---

## Gate B — claim-safe

Six rules, six negative fixtures, one clean report, and one anti-gaming case.

The last fixture is the one that matters most for whether the gate survives
contact with real work: it contains **every forbidden sentence**, fenced as the
counter-examples they are, and it passes. Without that, this kit's own
`references/forbidden-claims.md` could not be written.

```text
$ python3 skills/claim-safety/scripts/claim_guard.py --self-check
claim_guard --self-check:
PASS  Gate B (claim-safe) — samples/reports/report_clean.md
   -> report_clean.md: expected PASS, got PASS [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_unlicensed_claim.md
        - [unlicensed_direction]:13 'reduces' sits beside the quantity '40%' with no interval licensing it: Consolidating the candidate clusters reduces prompt sprawl by 40% across the corpus.
   -> report_unlicensed_claim.md: expected BLOCK, got BLOCK [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_tier_asserted.md
        - [undisclosed_tier]:13 'is Tier 3' asserts a quality tier as a fact: The bundle at  is Tier 3 and needs no further work before wide distribution.
   -> report_tier_asserted.md: expected BLOCK, got BLOCK [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_missing_stamp.md
        - [fixture_figure_unstamped] the report quotes figures against a fixture corpus without the stamp 'SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE'; sample output must not be readable as a result
   -> report_missing_stamp.md: expected BLOCK, got BLOCK [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_no_limitations.md
        - [missing_limitations] the report carries quantities and no Limitations section; ADR-0040 requires limitations to be generated, not remembered
   -> report_no_limitations.md: expected BLOCK, got BLOCK [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_roi_claim.md
        - [roi_or_money_claim]:1 'ROI' is a performance claim in financial clothing: # Governance audit — ROI claim
        - [roi_or_money_claim]:5 'payback' is a performance claim in financial clothing: Negative fixture: a payback figure, which is a performance claim in financial clothing.
        - [roi_or_money_claim]:13 'pays for itself' is a performance claim in financial clothing: The remediation pays for itself within two quarters at an ROI of 3.
   -> report_roi_claim.md: expected BLOCK, got BLOCK [ok]
BLOCK  Gate B (claim-safe) — samples/reports/report_forbidden_sentence.md
        - [forbidden_sentence] ADR-0040 forbids this claim by name: 'pae has 90% accuracy'
   -> report_forbidden_sentence.md: expected BLOCK, got BLOCK [ok]
PASS  Gate B (claim-safe) — samples/reports/report_fenced_counterexamples.md
   -> report_fenced_counterexamples.md: expected PASS, got PASS [ok]
SELF-CHECK PASS
(exit 0)
```

---

## Gate C — handback complete

The dry run stages a copy of the corpus, builds the registry there, validates
it, and discards the copy — so a failed build can never leave a partial
registry in a client tree. `corpus-empty` is refused before a registry is
built at all.

The tampered-checksum case is the one that makes the gate mean something: the
verdict is the Engine's own `validate_registry`, so corrupting one record's
hash is caught rather than passed through.

```text
$ python3 skills/registry-handback/scripts/handback.py --self-check
handback --self-check:
PASS  Gate C (handback complete) — 6 record(s), staged from /home/user/prompt-agent-engineering/ai-governance-audit-kit/samples/corpus-good
        engine: 6 records, 6 unique UIDs, summary schema pae-registry-summary/1
   -> corpus-good stages and validates: ok
BLOCK  Gate C (handback complete) — Gate 0 blocked this corpus
        - 2 markdown file(s) sit under the configured roots and every one was excluded — the config matches nothing, which is not the same as a clean corpus
   -> corpus-empty is refused before a registry is built: ok
   -> the unmodified Engine opens the handback: ok
   -> a tampered checksum is caught by Gate C: ok
   -> no record asserts a copy edge, review status or tier: ok
   -> cluster findings ride as diagnostics, not edges: ok (6 diagnostic(s))
SELF-CHECK PASS
(exit 0)
```

---

## The handback, written and then proven

```text
$ python3 skills/registry-handback/scripts/handback.py /path/to/their/corpus --write
PASS  Gate C (handback complete) — 6 record(s), written into /path/to/their/corpus
        engine: 6 records, 6 unique UIDs, summary schema pae-registry-summary/1
(exit 0)
```

Now the part the whole kit exists for. These commands run **the unmodified
Engine** against a corpus it has never seen, using nothing but the two marker
files the kit wrote:

```text
$ pae stats
repository: /path/to/their/corpus
schema:     pae-registry-summary/1
records:    6 (live 6, tombstone 0)
recounted:  no

by kind (live / total)
  prompt            4 / 4
  skill             2 / 2

by maturity
  experimental                6

by serving policy
  standard                    6

by metadata completeness
  full                        6
(exit 0)

$ pae search "incident timeline"
1 result(s); showing 1
terms: incident timeline

 1. prompt:client/prompts/analysis-incident-timeline
    prompt · client · score 2.446
    Incident Timeline
    title: incident timeline
    pid: incident timeline
    desc: incident timeline
    tags: timeline
    path: incident timeline
(exit 0)

$ pae route "review third-party dependencies"
status:   matched
scope:    client
kind:     prompt
coverage: 1.00   margin: 1.00

candidate scopes
  client                                1.976  (3 hit(s))

candidate kinds
  prompt                                1.976  (3 hit(s))

start from
  prompt:client/prompts/analysis-dependency-review
      Dependency Review
  prompt:client/prompts/analysis-dependency-review-copy
      Dependency Review
  prompt:client/prompts/analysis-dependency-audit
      Dependency Audit

why
  - top hit prompt:client/prompts/analysis-dependency-review matched title[dependency review], pid[dependency review], desc[dependency party review third], tags[review], path[dependency review]
  - coverage 1.00 (threshold 0.34)
  - scope margin 1.00 (threshold 0.25)
(exit 0)

$ pae validate-registry --verify-checksums
aliases:            0
lines:              6
records:            6
relationship_edges: 0
repository:         /path/to/their/corpus
summary_schema:     pae-registry-summary/1
unique_public_ids:  6
unique_uids:        6
checksums:          verified
result:             ok — no problems found
(exit 0)
```

`pae search` returns the client's own artifact under the client's own scope.
`pae route` resolves to it. `pae validate-registry` verifies every checksum. If
this worked, the handback is an asset; if it had not, the kit would be a report
generator.

---

## The full suite

```text
$ python3 -m unittest discover -s tests 2>&1 | tail -4
----------------------------------------------------------------------
Ran 55 tests in 0.144s

OK
(exit 0)
```

55 tests, loading the same scripts the pipeline runs. There is no test-only
implementation of any gate.
