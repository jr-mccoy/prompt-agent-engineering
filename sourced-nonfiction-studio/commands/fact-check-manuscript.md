# /fact-check-manuscript

**Reconcile a finished draft against its sources.** For an already-cited draft, confirm every factual claim is actually supported by its citation — catching orphans, overreach, and misattribution.

## Usage
`/fact-check-manuscript` then paste the draft (`<manuscript>...</manuscript>`) and the source set with each source's actual content (`<sources>...</sources>`).

## What it runs
`domain-research-academic/research_manuscript_fact_check_reconciler.md`. If a claim turns out to be an ORPHAN, routes it to `domain-professional-writing/writing/writing_unsourced_claim_disposition.md`.

## Output
Reconciliation table (per claim: SUPPORTED / PARTIAL / OVERREACH / MISATTRIBUTED / ORPHAN / UNVERIFIABLE) + a prioritized fix list + publish-blocker summary.

## Use when
You have a cited draft (yours or a contributor's) and need a final check that the text and its citations actually agree before publishing. This is the studio's back-end gate applied to an existing manuscript.
