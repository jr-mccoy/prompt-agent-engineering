# /source-my-draft

**Full pipeline (Stages 0–6).** Take the author's uncited material and produce the fact→source matrix, cited manuscript, and risk report.

## Usage
`/source-my-draft` then paste the braindump / outline / draft (wrap in `<material>...</material>`).

## What it runs
Invokes `agents/sourcing-orchestrator` to run `orchestrator_sourced_nonfiction.md` end to end:
Stage 0 intake → 1 extract/type → 2 live source discovery (fan-out workers) → 3 match/weight → 4 disposition → 5 legal-risk + Gate A/B → 6 assembly (only if Gate A PASS).

## Guarantees
- Every kept factual claim traces to a REAL source found this run, or it is softened/reframed/cut.
- No fabricated citations. Legal exposure flagged and routed to counsel (never "cleared").
- Author sees all REFRAMED / UNVERIFIED / counsel-routed residue.

## Preconditions to gather
Field (→ profile), citation style, jurisdiction if real people/orgs are named, stakes level.
