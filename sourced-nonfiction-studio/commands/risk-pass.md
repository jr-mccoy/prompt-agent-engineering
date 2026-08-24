# /risk-pass

**Surgical: Stage 5.** Run the legal-risk and integrity pass on a draft: copyright/fair-use, defamation/publicity, plagiarism, and no-fabrication.

## Usage
`/risk-pass` then paste the draft. Provide jurisdiction (country + US state) if any real living people or organizations are named — this is required for the defamation/publicity screen.

## What it runs
`prompts/stage-5-legal-risk-integrity.md` via `agents/risk-reviewer`, orchestrating the fair-use, defamation/publicity, original-expression, and integrity prompts + `scripts/check_citations.py`.

## Output
A severity-ranked risk report (copyright / defamation / privacy-publicity / plagiarism / fabrication) with reduce-not-clear options per flag, plus Gate A (sourcing integrity) and Gate B (legal safety) status.

## Boundary
Flags and routes risk to counsel. **Does not give legal advice and clears nothing for publication.** US-common-law default; confirm jurisdiction.
