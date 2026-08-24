# Stage 4 — Claim Disposition

**Role in pipeline:** The honesty gate's decision stage. For every claim, decide how it may appear in the manuscript. This is where unsourceable tacit expertise is truthfully reframed rather than asserted as fact.

**Objective:** Assign each claim exactly one disposition — KEEP / SOFTEN / REFRAME / QUOTE / CUT — so nothing experiential ships as established fact and nothing valuable is needlessly lost.

**Orchestrates:** `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` (primary), `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` (certainty calibration).

---

## Inputs
- Claim Ledger (Stage 1) + Claim Verdicts (Stage 3).
- Scope Record (stakes flag, profile bar).

## Instructions
1. **Map verdict → disposition** for verifiable-fact claims:
   - `SUPPORTED` → **KEEP** (record anchor source).
   - `PARTIAL` → **SOFTEN** to the sourced (narrower/weaker) version.
   - `CONTESTED` → **SOFTEN/QUOTE** presenting the disagreement with attribution.
   - `UNVERIFIED` → go to step 2 (do NOT keep as fact).
2. **For UNVERIFIED facts and for judgment/opinion/analysis claims, test the basis:**
   - Strong experiential basis / defensible professional judgment → **REFRAME** as explicitly labeled judgment ("In my experience…", "In my professional judgment…"), certainty matched to basis.
   - Genuine common knowledge → **KEEP** unmarked (sanity-check it isn't folklore).
   - Best as exact words → **QUOTE** + attribute.
   - Thin/no basis → **CUT**.
3. **Apply the stakes multiplier.** Health/legal/financial/safety claims: KEEP requires a real at-tier source; otherwise SOFTEN/REFRAME with an explicit "not established — verify with [professional]" note, or CUT.
4. **Write honest rewrites** for SOFTEN/REFRAME/QUOTE.
5. **Produce the residue report** — every REFRAMED and CUT claim, so the author sees exactly what could not be stated as fact and why.

## Output Format
```
## Dispositions
| Claim # | Verdict | Disposition | Anchor / basis | Rewrite (if any) |
|---------|---------|-------------|----------------|------------------|
| 1 | SUPPORTED | KEEP | S1 | — |
| 2 | PARTIAL | SOFTEN | S5 | "One study suggests…" |
| 6 | UNVERIFIED | REFRAME | strong pattern basis | "In my experience…" |
| 8 | UNVERIFIED | CUT | no basis, high-stakes | — |

## Residue Report
- Reframed as judgment: [#s]
- Cut: [#s + why]
- High-stakes needing professional-verification note: [#s]
```

## Verification
- [ ] No UNVERIFIED claim is KEPT as fact.
- [ ] REFRAME wording is explicitly attributive (reader can tell judgment from fact).
- [ ] No baseless guess reframed into false "in my experience" authority (those are CUT).
- [ ] SOFTEN changed certainty, not meaning.
- [ ] Stakes multiplier applied; residue report complete.
