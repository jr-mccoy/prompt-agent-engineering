# Forbidden claims, and what to write instead

Every example below sits inside a fence, which is how this page can exist: Gate
B strips fenced blocks and inline code spans before its prose detectors run, the
same anti-gaming rule as `agentic-system-factory/scripts/check_gate.py`.

## Forbidden by name

`meta/adr/0040-public-performance-claim-governance.md` forbids these outright:

```text
PAE makes AI 20% smarter
PAE has 90% accuracy
proven to improve every model
```

...along with any number derived from the Phase 4/5 internal sets. Matching is
on normalized text, so casing and whitespace cannot smuggle one through.

## The licensing rule for a directional word

The ADR's own formulation: *"There is no code path that writes 'improved'
without a number requiring it."*

Blocked — a direction beside a quantity, with nothing licensing it:

```text
Consolidating the candidate clusters reduces prompt sprawl by 40%.
The remediation improves retrieval accuracy by 12 points.
```

Not blocked — the same direction with no number attached. It carries nothing to
mislead with, and a gate that blocks ordinary prose gets switched off:

```text
This gate reduces the chance that an unbacked claim reaches a client.
```

Allowed — the quantity is licensed by an interval:

```text
Condition A completed 61% of tasks versus 48% under condition B
(+13 pp; paired 95% CI 4 to 22).
```

The claim-ready sentence ADR-0040 specifies names benchmark and version, task
count, commit, model, conditions, effect, 95% CI and repeat design. There is
deliberately no generic accuracy field for a later reader to extract.

## ROI and money

Blocked, because a payback figure is a performance claim in financial clothing:

```text
The remediation pays for itself within two quarters.
An ROI of 3.2x on the engagement fee.
Saves $40,000 a year in duplicated authoring effort.
```

Write instead what you actually measured:

```text
Nine artifacts were found in three exact-duplicate clusters. What
consolidating them is worth depends on how often each is used, which this
audit did not measure.
```

If a report genuinely needs to *discuss* an ROI figure — a client's own, say —
put it in backticks. That is the same escape hatch the forbidden sentences get,
and it forces the mention to be visibly a quotation.

## Asserted tiers

Blocked:

```text
The bundle at skills/deploy-helper is Tier 3.
This is a Tier 2 prompt.
```

Allowed, because the provenance is disclosed in the same sentence:

```text
skills/deploy-helper scores 54 of the 54 mechanically observable points.
The author's self-reported block claims 92 of 100; the two are reported
separately and the gap is a finding.
```

## Fixture figures

Every figure drawn from a fixture or a sample run carries, verbatim:

```text
SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE
```

Gate B blocks a report that cites a configured fixture path marker alongside a
quantity without the stamp. Sample output must not be readable as a result by
someone who was not there.

## Limitations

Limitations are **generated, not remembered**. A report carrying quantities and
no `## Limitations` section is blocked, as is one whose section is thinner than
the configured minimum.

They should be written from *this* run. The ones worth stating almost always
include: that every figure is specific to this corpus, config and commit; what
fraction of the rubric was observable; that lexical clustering cannot see a
paraphrase; how scores were obtained; and that the author of an artifact is not
its reviewer (`meta/adr/0041-author-reviewer-separation.md`).

## What Gate B cannot do

It checks a claim against the shape of its support. It cannot tell you whether
the underlying number is true. A false number, correctly hedged, passes — which
is why the gate is the last check before a report ships and never the only one.
