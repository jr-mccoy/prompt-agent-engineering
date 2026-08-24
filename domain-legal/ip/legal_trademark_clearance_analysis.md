---
title: "Trademark Clearance Analysis (Knockout + Full)"
category: legal/ip
description: "Two-stage trademark clearance: (1) knockout search against USPTO and state registers, (2) full clearance with likelihood-of-confusion analysis under the controlling circuit's multi-factor test (DuPont / Sleekcraft / Polaroid / Pizzeria Uno), distinctiveness placement on the Abercrombie spectrum, and Section 2(d) bar assessment."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - ip
  - trademark
  - clearance
  - likelihood-of-confusion
updated: "2026-05-11"
related_prompts:
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-legal/research/legal_precedent_comparison_table.md
---

**Purpose:** Deliver an actionable clearance opinion on a proposed mark: knockout against federal and state registers + common-law uses, full likelihood-of-confusion analysis against the closest cited references under the controlling multi-factor test, distinctiveness placement, and a recommendation (clear / clear with conditions / do not adopt / pivot to coexistence).

**When to use:** Before adoption of a new brand, product, service, or campaign mark; before filing a §1(a) or §1(b) application; before responding to a §2(d) refusal; pre-investment IP diligence; rebranding after cease-and-desist exposure.

---

## Your Input

- **Jurisdiction:** [US — federal registration + state common-law uses / TTAB if opposition or cancellation posture / specific circuit for litigation risk (1st–11th, DC, Fed Cir for appeals from TTAB); flag if foreign registration also needed (Madrid Protocol / national filings)]
- **Proposed mark:** [Exact spelling, capitalization, design elements if any — quote verbatim]
- **Mark format:** [Standard character / stylized + design / sound mark / trade dress / certification mark / collective mark]
- **Goods / services:** [Verbatim recitation if drafted, or proposed scope — identify Nice Classes]
- **Applicant entity:** [Name, type, state of formation, address]
- **Use posture:** [In-use §1(a) with first-use dates / intent-to-use §1(b) / foreign basis §44(d)/(e) / Madrid §66(a)]
- **Channels of trade:** [Online direct-to-consumer / retail / B2B / regulated channels]
- **Target consumer:** [Sophistication level, price point, purchase frequency]
- **Knockout search results supplied:** [USPTO TESS hits, state register hits, common-law hits (Secretary of State business names, domain registrations, social handles, app stores) — with each cited entry]
- **Closest cited references:** [Each reference: registration number or common-law identifier, mark, owner, goods/services, registration date, status (live/dead/cancelled), first-use date — use `[CITE: Reg. No. _______]` or `[NEED: ...]` for missing data]
- **Distinctiveness theory:** [Generic / descriptive (with or without acquired distinctiveness under §2(f)) / suggestive / arbitrary / fanciful]
- **Coexistence or consent posture:** [Existing consent agreements, related-party use, prior co-pending applications]

---

## Constraints

**Must:**
- Conduct knockout against **federal (USPTO)**, **state registers**, and **common-law** sources (Secretary of State entity names, domain WHOIS, social handles, app marketplaces, industry directories).
- Place the proposed mark on the **Abercrombie spectrum** with reasoning (generic / descriptive / suggestive / arbitrary / fanciful). Note that descriptive marks are unregistrable on the Principal Register absent §2(f) acquired distinctiveness.
- Apply the **controlling multi-factor likelihood-of-confusion test** for the forum:
  - **TTAB / USPTO §2(d) refusals:** *In re E.I. du Pont de Nemours & Co.*, 476 F.2d 1357 (CCPA 1973) — 13 DuPont factors [CITE: verify pinpoint].
  - **Ninth Circuit:** *AMF Inc. v. Sleekcraft Boats*, 599 F.2d 341 (9th Cir. 1979) — 8 Sleekcraft factors [CITE: verify].
  - **Second Circuit:** *Polaroid Corp. v. Polarad Elecs. Corp.*, 287 F.2d 492 (2d Cir. 1961) — 8 Polaroid factors [CITE: verify].
  - **Third Circuit:** *Interpace Corp. v. Lapp, Inc.* — 10 Lapp factors [CITE: verify].
  - **Fifth Circuit:** *Digit. Eng'g* / "digits of confusion" [CITE: verify].
  - **Other circuits:** apply the circuit's stated test (Frisch's, Pizzeria Uno, etc.) [CITE: verify per circuit].
- For each cited reference, analyze each applicable factor on the record (similarity in sight/sound/meaning/commercial impression; relatedness of goods/services; channels of trade; sophistication of buyers; strength of senior mark — conceptual + commercial; actual confusion evidence; intent; bridging the gap; quality of junior's goods; length of concurrent use).
- Identify any **Section 2(d) refusal risk** (likelihood of confusion with a registered or prior-pending mark) and **Section 2(e) refusal risks** (descriptiveness, deceptive misdescriptiveness, primarily merely surname, geographic descriptiveness, functional).
- Identify **Section 2(a)** issues (false connection, disparagement / scandalous — note *Matal v. Tam* and *Iancu v. Brunetti* limits) and **Section 2(c)** consent-of-living-person issues.
- Flag **dilution exposure** (15 U.S.C. §1125(c)) where a famous senior mark is implicated, with the eight factors for fame.
- Recommend one of: **clear / clear with conditions** (e.g., narrow ID, design element, disclaimer) / **coexistence agreement opportunity** / **do not adopt — pivot**.
- Use `[CITE: ...]` and `[NEED: ...]` for unverified citations and missing search data.

**Must Not:**
- Fabricate registration numbers, serial numbers, filing dates, first-use dates, owner names, or pinpoint citations to TMEP, DuPont, Sleekcraft, or any opinion.
- Treat a "no exact hits" knockout result as clearance — sound-alike, translation, and phonetic equivalents must be evaluated.
- Skip common-law search — federal registration does not eliminate prior senior common-law users in their geographic territory (*Tea Rose-Rectanus* doctrine).
- Apply the DuPont factors to a district-court infringement opinion or apply Sleekcraft to a TTAB matter — match the test to the forum.
- Recommend "register on the Supplemental Register" without explaining the consequences (no §1052(d) protection, no presumption, eligible after 5 years to claim §2(f)).
- Insert generic "consult counsel" disclaimers — this is the counsel opinion.

---

## Instructions

1. **Header.** Proposed mark, format, goods/services + classes, applicant, jurisdiction, controlling LOC test.
2. **Distinctiveness placement.** Abercrombie spectrum with reasoning. If descriptive, evaluate §2(f) acquired-distinctiveness posture (5+ years substantially exclusive use, advertising, sales, declarations, survey).
3. **Knockout summary.** Table of all hits found, with status (live/dead), owner, goods, similarity. Identify "knockouts" (clear barring uses) vs. "investigate further."
4. **Closest cited references — detailed analysis.** For each top reference (typically 3–5):
   - Identification block: mark, reg. no. / common-law identifier, owner, goods/services, status, first-use date, channels.
   - Multi-factor analysis applying the **controlling test** — one row per factor, evidence/inference for each.
   - Conclusion: high / moderate / low LOC risk.
5. **Section 2(d) bar assessment.** Cumulative across cited references — is the application likely to face a §2(d) refusal? Is a registration achievable with ID narrowing or design distinction?
6. **Section 2(e) and other absolute-bar assessments.** Descriptiveness, surname, geographic, functional, deceptive misdescriptiveness, disparagement-adjacent.
7. **Dilution exposure (if applicable).** Famous-mark fact pattern + eight fame factors.
8. **Common-law / geographic exposure.** Tea Rose-Rectanus zones, prior users with potential injunction rights in specific regions.
9. **Coexistence opportunity.** Where LOC is borderline, identify candidates for consent / coexistence agreements (channel separation, geographic carve-out, class restriction).
10. **Recommendation block.** Clear / clear with conditions / coexistence / do not adopt — with action steps (ID amendment, design lock-up, §1(b) ITU vs. §1(a), state common-law use plan, foreign filing strategy).

---

## Output Format

```markdown
# Trademark Clearance Analysis — "{Proposed Mark}"
**Mark format:** {standard character / stylized + design / ...}
**Goods/services:** {verbatim recitation} — Class(es) {Nice}
**Applicant:** {name, entity type, state}
**Jurisdiction / controlling LOC test:** {US federal — TTAB DuPont / 9th Cir. Sleekcraft / 2d Cir. Polaroid / ...}

## 1. Distinctiveness (Abercrombie)
**Placement:** {Generic / Descriptive / Suggestive / Arbitrary / Fanciful}
**Reasoning:** {analysis}
**§2(f) posture (if descriptive):** {acquired-distinctiveness facts / [NEED: evidence of 5+ years substantially exclusive use, advertising spend, sales, survey]}

## 2. Knockout Summary
| Mark | Reg./Source | Owner | Goods/Class | Status | First Use | Similarity |
|---|---|---|---|---|---|---|
| {hit} | {Reg. No. / TESS / state / common-law source} | {owner} | {goods} | {live/dead/pending} | {date} | {high/mod/low — sight/sound/meaning} |
| ... | ... | ... | ... | ... | ... | ... |

**Knockouts identified:** {list of disqualifying hits}
**Further investigation:** {list}

## 3. Closest Cited References — Likelihood-of-Confusion Analysis

### Reference A: "{Senior Mark}" — [CITE: Reg. No. _______]
**Owner:** {name} | **Goods/Class:** {recitation} | **Status:** {live} | **First use:** {date} | **Channels:** {...}

| Factor (per {DuPont / Sleekcraft / Polaroid}) | Analysis | Weight |
|---|---|---|
| Similarity of marks (sight/sound/meaning/commercial impression) | {analysis} | {favors senior / junior / neutral} |
| Similarity / relatedness of goods or services | {analysis — In re Coors Brewing standard for TTAB} | {...} |
| Similarity of trade channels | {analysis} | {...} |
| Conditions of purchase / buyer sophistication | {analysis — price point, purchase frequency} | {...} |
| Strength of senior mark (conceptual + commercial) | {Abercrombie placement of senior + market evidence} | {...} |
| Actual confusion | {evidence / none of record / [NEED: ...]} | {...} |
| Intent of junior user | {good-faith adoption / [NEED: ...]} | {...} |
| Bridging the gap (likelihood senior expands) | {...} | {...} |
| {additional factors per controlling test} | {...} | {...} |

**LOC conclusion vs. Reference A:** {high / moderate / low}

### Reference B: "{Senior Mark}" — [CITE: Reg. No. _______]
{same structure}

## 4. Section 2(d) Bar Assessment
**Cumulative §2(d) refusal risk:** {high / moderate / low}
**Bases:** {summary citing closest references}
**Mitigation:** {ID narrowing / design distinction / disclaimer / channel restriction}

## 5. Section 2(e) and Other Absolute-Bar Risks
- §2(e)(1) Descriptiveness: {...}
- §2(e)(2) Geographic descriptiveness: {...}
- §2(e)(3) Primarily geographically deceptively misdescriptive: {...}
- §2(e)(4) Primarily merely a surname: {...}
- §2(e)(5) Functional (trade dress): {...}
- §2(a) False connection / deceptive: {...}
- §2(c) Consent of living person: {...}

## 6. Dilution Exposure (15 U.S.C. §1125(c))
**Famous-mark fact pattern present?** {Yes / No — analysis}
**Fame factors (if applicable):** {duration / extent of advertising / geographic reach / degree of recognition / use by third parties / federal registration — [CITE: 15 U.S.C. §1125(c)(2)(A)]}

## 7. Common-Law / Geographic Exposure
**Prior senior common-law users:** {list with territory under Tea Rose-Rectanus}
**Risk:** {nationwide registration achievable subject to concurrent-use carve-out / geographic injunction risk}

## 8. Coexistence Opportunity
{Identification of candidates for consent agreements with channel/class/geographic separation}

## 9. Recommendation
**Disposition:** {Clear / Clear with conditions / Pursue coexistence / Do not adopt — pivot}
**Action steps:**
1. {e.g., Amend ID to "{narrowed recitation}" to avoid §2(d) overlap with Reference A}
2. {e.g., File §1(b) ITU; convert to §1(a) upon use in commerce}
3. {e.g., Approach Reference B owner for consent agreement with channel separation}
4. {e.g., Register state common-law use in {jurisdiction} to establish priority}
5. {e.g., Foreign filing via Madrid in {countries} within 6-month Paris Convention priority}

## Open Issues / NEEDs
- [NEED: Verified TESS search export with date]
- [NEED: State register search for {states}]
- [NEED: Common-law search (domain WHOIS, social handles, app stores) — supplied search did not cover]
- [CITE: pinpoint to DuPont factor citation if used in record]
```

---

## Verification

- [ ] Knockout covered federal (USPTO), state registers, and common-law sources (entity names, domains, social, app stores).
- [ ] Mark placed on Abercrombie spectrum with reasoning.
- [ ] §2(f) acquired-distinctiveness posture addressed if mark is descriptive.
- [ ] Controlling multi-factor LOC test matched to the forum (DuPont for TTAB; circuit-specific test for litigation).
- [ ] Every cited reference analyzed factor-by-factor, not in summary.
- [ ] §2(d) bar assessment is cumulative across references, not just per-reference.
- [ ] §2(e), §2(a), §2(c) absolute-bar issues evaluated.
- [ ] Dilution exposure addressed where a famous-mark fact pattern exists.
- [ ] Tea Rose-Rectanus / common-law geographic exposure addressed.
- [ ] Recommendation is one of: clear / clear with conditions / coexistence / do not adopt — with concrete action steps.
- [ ] All registration numbers, dates, and citations are real or marked `[CITE: ...]` / `[NEED: ...]`.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "No exact hits — mark is clear" | Sound-alike, translation, phonetic equivalents, and design elements must be searched; clearance requires LOC analysis, not just identity check |
| Applying DuPont in a 9th Cir. infringement opinion | DuPont is the TTAB/USPTO test; Sleekcraft is the 9th Cir. infringement test — match to forum |
| Treating descriptive marks as registrable on the Principal Register without §2(f) | Descriptive marks require §2(f) acquired distinctiveness (typically 5+ years substantially exclusive use); Supplemental Register is the alternative |
| Ignoring common-law users because federal register is clear | Tea Rose-Rectanus preserves prior common-law users in their geographic territory; senior common-law use can defeat federal registration nationwide |
| Equating "live registration" with "active use" | A registration can be live but vulnerable to non-use cancellation after 3 years (§14) — file a USPTO status check; consider TTAB cancellation as offensive option |
| Conflating dilution with confusion | Dilution requires fame under §1125(c) — most marks do not qualify; do not assert dilution against non-famous senior marks |
| Recommending coexistence without channel/class/geographic separation | Consent agreements are not auto-accepted; the USPTO weighs them as one DuPont factor and may still refuse |
| Skipping the foreign filing window | Paris Convention 6-month priority runs from first US filing; Madrid extension requires basic US application; flag if foreign filing matters |
| Applying *Matal v. Tam* / *Iancu v. Brunetti* to all §2(a) issues | Those decisions invalidated disparagement and scandalous bars only; false connection and deceptive bars remain enforceable |
| Fabricating Reg. Nos. or first-use dates | Use `[CITE: Reg. No. _______]` or `[NEED: TESS export]`; never invent |
