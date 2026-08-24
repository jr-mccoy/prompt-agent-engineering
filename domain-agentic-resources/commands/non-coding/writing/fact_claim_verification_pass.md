---
name: fact_claim_verification_pass
description: "Run before publication when factual assertions must be checked and confidence-labeled."
version: "1.0.0"
category: writing
tags: [claim, fact, verification, writing]
agents_used: []
---
# Fact Claim Verification Pass

## Trigger phrase
Run before publication when factual assertions must be checked and confidence-labeled.

## Required inputs
- Draft content with factual claims.
- Trusted references or source corpus.
- Verification policy (required certainty, citation format, redline rules).

## Output schema
- `verification_table`: claim-by-claim status (Verified/Uncertain/Unsupported), evidence, and citation.
- `annotated_draft_actions`: exact edits, caveats, or removals needed before publish.
- `verification_summary`: overall publication readiness and outstanding blockers.

## Validation checklist
- [ ] All factual claims are assessed individually.
- [ ] Uncertain and unsupported claims include concrete next actions.
- [ ] Citations are attached for verified claims per required format.
- [ ] Readiness summary clearly states whether publication criteria are met.
