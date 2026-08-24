---
name: claim_evidence_mapping
description: "Run when claims in a report or draft need explicit traceability to supporting evidence."
version: "1.0.0"
category: research
tags: [claim, evidence, mapping, research]
agents_used: []
---
# Claim Evidence Mapping

## Trigger phrase
Run when claims in a report or draft need explicit traceability to supporting evidence.

## Required inputs
- Draft claims (or full document excerpt).
- Evidence corpus with citation metadata.
- Required confidence threshold and citation style.

## Output schema
- `claim_evidence_map`: table linking each claim to supporting evidence, strength rating, and citation.
- `unsupported_or_weak_claims`: claims lacking sufficient support with remediation options.
- `evidence_gaps`: prioritized data collection questions for unresolved claims.

## Validation checklist
- [ ] All material claims are represented in the mapping table.
- [ ] Evidence strength is rated consistently using a defined scale.
- [ ] Weak/unsupported claims are clearly separated from supported claims.
- [ ] Citation metadata is complete and usable for downstream writing.
