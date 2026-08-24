# DRY_RUN — Worked pass over `samples/braindump-sample.md`

A worked mini-run of the full pipeline on the career-coach braindump. It shows
the behavior the studio guarantees: real sources or none, tacit knowledge
reframed (not asserted), a named-party defamation flag, and Gate A blocking
assembly until every KEEP claim resolves.

**One citation below is REAL and was fetched live during this run** (the BLS
duration-of-unemployment data). Where live search did not return an at-tier
source, the claim is honestly SOFTENED, REFRAMED, or CUT — no source is
invented to fill a slot. That is the point of the exercise.

---

## Stage 0 — Scope Record
- Field / profile: `general` (career/labor content; min anchor tier 3; recency caution 10y)
- Citation style: `inline_numbered`
- Names real living parties? **YES** → "Jane Doe at Acme Corp" → jurisdiction: `US-common-law-default; CONFIRM state` → **Stage 5 defamation screen REQUIRED**
- Stakes: general (one item — "never take a counteroffer" — is career-advice high-ish)
- Deliverables: matrix + manuscript + risk report

## Stage 1 — Claim Ledger (abridged)
| # | Claim | Type | Load-bearing | 
|---|-------|------|--------------|
| 1 | Avg job search ~5 months | verifiable-fact | yes |
| 2 | Most roles filled before posted | verifiable-fact | yes |
| 3 | Recruiters spend ~6s on a résumé | verifiable-fact | yes |
| 4 | Same-day thank-you note → more offers | experiential-opinion | yes |
| 5 | Networking most effective **for everyone** | professional-judgment | yes |
| 6 | Never take a counteroffer — always ends badly | experiential-opinion | yes |
| 7 | Small teams hire faster (fewer approvers) | experiential-opinion (labeled) | no |
| 8 | Jane Doe at Acme inflated the numbers | claim-about-named-person | yes |
| 9 | Two-week career break → higher long-term earnings | verifiable-fact | yes |

## Stage 2 — Source Discovery (LIVE)
- **Claim 1:** REAL search (BLS). Mean duration of unemployment was **23.4 weeks in Q4 2024** (≈ 5.4 months), up from 21.1 weeks a year earlier. [S1]
  - Supporting passage (fetched): "the average (mean) duration of unemployment rose to 23.4 weeks in the fourth quarter of 2024."
  - Caveat captured: this is *mean unemployment duration*, a proxy for "job search length," not a direct measure. → drives a SOFTEN, not a naked KEEP.
- **Claim 2:** mixed/'hidden job market' estimates vary widely; no single at-tier anchor → PARTIAL.
- **Claim 3:** the "6 seconds" figure traces to a single recruiting-vendor eye-tracking study; no independent at-tier confirmation found → attribute, don't state as law. (Specific study left as `[verify original]` — not fabricated here.)
- **Claims 4, 6, 7, 9:** NO SOURCE FOUND at an acceptable tier.

## Stage 3 — Verdicts
| # | Verdict | Anchor | Licensed certainty |
|---|---------|--------|--------------------|
| 1 | SUPPORTED (as mean unemployment duration) | [S1] | "about five months, by one common measure" |
| 2 | PARTIAL | — | "a meaningful share, estimates vary" |
| 3 | CONTESTED/weak | single vendor study | "one study put it at ~6s" |
| 4,6,7,9 | UNVERIFIED | — | — |
| 5 | UNVERIFIED (universal form) | — | — |

## Stage 4 — Dispositions
| # | Disposition | Rewrite |
|---|-------------|---------|
| 1 | **SOFTEN/KEEP** | "By one common measure — the average duration of unemployment — a job search runs roughly five months (about 23 weeks in late 2024). [S1]" |
| 2 | **SOFTEN** | "A meaningful share of roles are filled through referrals and internal moves before any public posting, though estimates vary widely." |
| 3 | **SOFTEN/attribute** | "One widely-cited recruiter eye-tracking study put initial résumé review at roughly six seconds; treat it as indicative, not precise." |
| 4 | **REFRAME** | "In my coaching practice, candidates who send a prompt, specific thank-you note tend to fare better — a pattern I've seen, not a proven rule." |
| 5 | **REFRAME + narrow** | "In my experience, networking is the highest-leverage tactic for most mid-career candidates — less so for some early-career or credential-gated roles." |
| 6 | **CUT** | (removed — no basis, high-stakes, contested even as opinion) |
| 7 | **REFRAME (keep as labeled)** | already "In my experience…"; kept as judgment |
| 8 | → Stage 5 (defamation) | — |
| 9 | **CUT** | (removed — UNVERIFIED, presented as fact; no basis found) |

## Stage 5 — Risk & Integrity + Gates
- **Defamation (jurisdiction: CONFIRM):** `[HIGH] Jane Doe` — "routinely inflated the numbers" is a harmful factual assertion about an identifiable private living person, unsupported → route to counsel. Options (reduce, not clear): document with contemporaneous evidence; narrow to a specific witnessed incident you can substantiate; anonymize/composite; or cut. **Not cleared.**
- **Copyright:** no long quotes; the 6-second study is paraphrased + attributed. OK.
- **Integrity / citation shape:** ran `scripts/check_citations.py` on the draft matrix → after CUT of 6 and 9 and REFRAME of the rest, the only KEEP/SOFTEN facts (1, 2, 3) carry resolvable references or attribution.
- **Gate A: PASS** (no orphan KEEP claims; no UNVERIFIED claim kept as fact; [S1] resolves).
- **Gate B:** 1 HIGH defamation flag routed to counsel (publish-blocker until resolved); jurisdiction to confirm.

## Stage 6 — Assembly (Gate A PASS → proceed)
**Fact→Source Matrix** (excerpt):
| # | Claim | Disposition | Source | Reference | Marker |
|---|-------|-------------|--------|-----------|--------|
| 1 | Job search ~5 months | SOFTEN/KEEP | [S1] | U.S. BLS, duration of unemployment, Q4 2024. https://www.bls.gov/charts/employment-situation/duration-of-unemployment.htm | — |
| 4 | Thank-you notes help | REFRAME | — | — | [author's professional judgment] |
| 8 | Jane Doe inflated numbers | HELD | — | — | counsel-review (defamation) |

### References
- [S1] U.S. Bureau of Labor Statistics. "Long-term unemployed accounted for 23.7 percent of total unemployed in September 2024" / duration-of-unemployment data, 2024. https://www.bls.gov/opub/ted/2024/long-term-unemployed-accounted-for-23-7-percent-of-total-unemployed-in-september-2024.htm

**Author Disclosure & Residue**
- Reframed as judgment (not fact): 4, 5, 7
- Cut: 6 (never-take-a-counteroffer — no basis, high-stakes), 9 (career-break earnings — unverified, asserted as fact)
- Counsel-review (blocks publish until resolved): 8 (Jane Doe)
- Note: sourcing was AI-assisted; verify [S1] and the 6-second study against the originals before publishing; confirm jurisdiction for the defamation review.

---

## What this run demonstrates
1. **Real sources or none** — claim 1 got a genuine, resolvable BLS citation fetched live; claims 4/6/7/9 got no source and were reframed or cut, not backfilled with an invented cite.
2. **Tacit expertise preserved honestly** — the coach's real insights (4, 5, 7) survive as clearly-labeled judgment, not as fake facts.
3. **Overreach corrected** — "6 seconds" and "for everyone" were softened/narrowed to what evidence supports.
4. **Named-party risk caught** — the Jane Doe claim is flagged HIGH and routed to counsel, never cleared.
5. **Gate A is real** — the citation-shape script + semantic critique block assembly until every KEEP claim resolves; CUT/REFRAME are how unsourceable claims exit without faking a source.

_Sources: [U.S. BLS — long-term unemployed, Sept 2024](https://www.bls.gov/opub/ted/2024/long-term-unemployed-accounted-for-23-7-percent-of-total-unemployed-in-september-2024.htm), [U.S. BLS — duration of unemployment](https://www.bls.gov/charts/employment-situation/duration-of-unemployment.htm)._
