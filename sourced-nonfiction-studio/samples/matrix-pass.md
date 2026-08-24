# Fact→Source Matrix — PASS fixture

Every KEEP/SOFTEN claim has a resolvable [S#] token; the unsourceable claim is
REFRAMED (not kept as fact). `check_citations.py` should exit 0.

## Fact→Source Matrix
| # | Claim | Type | Disposition | Verdict | Source | Reference | Certainty | Marker |
|---|-------|------|-------------|---------|--------|-----------|-----------|--------|
| 1 | Average job search ~5 months | verifiable-fact | KEEP | SUPPORTED | [S1] | U.S. BLS, "Job Search Duration," 2024, https://www.bls.gov/ | established | — |
| 2 | A large share of roles filled via referrals before posting | verifiable-fact | SOFTEN | PARTIAL | [S2] | Smith & Lee, 2021, doi:10.1000/exampledoi | some evidence | — |
| 3 | Prompt, specific thank-you notes help | experiential-opinion | REFRAME | UNVERIFIED | — | — | author judgment | [author's professional judgment] |
| 4 | Never take a counteroffer | experiential-opinion | CUT | UNVERIFIED | — | — | — | cut: no basis, high-stakes |

### References
- [S1] U.S. Bureau of Labor Statistics, 2024. https://www.bls.gov/
- [S2] Smith, J. & Lee, K. (2021). Referral hiring patterns. doi:10.1000/exampledoi
