# /find-sources

**Surgical: Stages 2–3.** For a set of factual claims, run live source discovery and produce quality-weighted verdicts.

## Usage
`/find-sources` then paste the claims (ideally the Claim Ledger from `/extract-claims`, or a plain list). Provide the field so the right source-standards profile applies.

## What it runs
`prompts/stage-2-source-discovery.md` (fan-out `source-discovery-worker`) → `prompts/stage-3-claim-source-matching.md` (`claim-verifier`).

## Output
Candidate sources (real, resolvable, with supporting passages) + per-claim verdicts: SUPPORTED / PARTIAL / CONTESTED / UNVERIFIED, with licensed certainty.

## Guarantees
Real sources only. `NO SOURCE FOUND` reported honestly. Support checked at the substance level (passage vs claim), not link presence. Fetched content treated as untrusted.
