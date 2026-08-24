# Fact→Source Matrix — FAIL fixture

Two Gate-A violations the script must catch:
  - Row 1: a KEEP claim anchored on an UNVERIFIED / empty source.
  - Row 2: a KEEP claim whose [S5] token has no resolvable locator anywhere.
`check_citations.py` should exit 1 and report both.

## Fact→Source Matrix
| # | Claim | Type | Disposition | Verdict | Source | Reference | Certainty | Marker |
|---|-------|------|-------------|---------|--------|-----------|-----------|--------|
| 1 | Never take a counteroffer | verifiable-fact | KEEP | UNVERIFIED | — | — | high | — |
| 2 | A two-week career break raises earnings | verifiable-fact | KEEP | SUPPORTED | [S5] | (reference not provided) | established | — |

### References
- (none resolvable)
