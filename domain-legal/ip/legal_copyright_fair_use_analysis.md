---
title: "Copyright Fair Use Analysis (17 U.S.C. §107 Four-Factor Test)"
category: legal/ip
description: "Four-factor fair use analysis under 17 U.S.C. §107, grounded in supplied authority and applied to a specific use, with transformativeness analysis under Warhol v. Goldsmith, market-substitution analysis, and posture statement for AI training-data uses."
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
  - copyright
  - fair-use
  - transformative
updated: "2026-05-11"
related_prompts:
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-legal/research/legal_precedent_comparison_table.md
---

**Purpose:** Produce a defensible fair-use opinion under 17 U.S.C. §107 applied to a specific use, weighing all four statutory factors (and not just transformativeness), grounded in supplied case authority for the controlling circuit. Output is suitable for risk counseling, litigation contention, DMCA counter-notice support, or pre-publication clearance.

**When to use:** Pre-publication clearance for criticism / commentary / news reporting / teaching / scholarship / research / parody / sampling / quotation / appropriation art; defending an infringement claim; supporting a DMCA §512(g) counter-notice on fair-use grounds; AI-training-data risk analysis; documentary filmmaking; database / search / indexing services.

---

## Your Input

- **Jurisdiction:** [US federal — copyright is exclusively federal under 17 U.S.C.; specify circuit (1st–11th, DC, Fed Cir) for controlling fair-use precedent; *Warhol v. Goldsmith* (2023) is binding everywhere]
- **The work allegedly infringed:** [Title, author, year of creation, year of publication (or unpublished), medium, registration status — quote registration `[CITE: Reg. No. _______]` if known or `[NEED: ...]`; nature (factual / creative / functional)]
- **The accused use:** [Verbatim description of what is taken, how it is used, in what medium, for what purpose, to what audience, with what commercial posture]
- **Quantitative amount taken:** [Words / seconds / frames / lines / pixels / database rows — both absolute and as percentage of the work]
- **Qualitative amount taken:** [Whether what was taken is the "heart" of the work, the most expressive elements, or peripheral material]
- **Transformativeness theory:** [New expression, meaning, or message — articulate specifically; or new purpose distinct from the original; *Warhol*-style "purpose-and-character" analysis comparing the original use case to the secondary use case]
- **Commercial posture:** [Commercial / nonprofit / educational / news reporting / mixed]
- **Market for the original work:** [Primary market, derivative-works market, licensing market, any actual licensing of the type of use at issue]
- **Licensing market evidence:** [Whether the type of use is customarily licensed — supplied evidence of licensing markets or absence thereof]
- **Statutory favored category alignment:** [Criticism / comment / news reporting / teaching / scholarship / research / parody — §107 preamble]
- **AI / training-data posture (if applicable):** [Whether the use involves machine learning training, retrieval-augmented generation, output generation; outputs' substantial similarity to inputs; whether the model can regurgitate training data — flag as `[CITE: relevant authority]` and treat as an unsettled area]

---

## Constraints

**Must:**
- Apply all four §107 factors. Fair use is a holistic balancing — no single factor is dispositive ([CITE: Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994)]).
- Treat **transformativeness** under *Warhol Foundation v. Goldsmith*, 598 U.S. 508 (2023): factor one asks whether the secondary use has a "further purpose or different character" from the original, and the inquiry compares **specific uses** of the works at issue — not just the works in the abstract. A high degree of transformation does not override factor four if the secondary use serves as a market substitute.
- Distinguish **transformative use** (factor one) from **derivative work** (17 U.S.C. §106(2)) — many derivative works are not fair use even if they add new expression.
- Analyze the **nature of the copyrighted work** (factor two): factual works receive thinner protection than creative works; unpublished works weigh against fair use ([CITE: Harper & Row Publishers, Inc. v. Nation Enters., 471 U.S. 539 (1985)]).
- Analyze **amount and substantiality** (factor three) both **quantitatively** and **qualitatively** — taking the "heart" of a work weighs heavily against fair use even if small in absolute amount.
- Analyze **market effect** (factor four): (a) substitution in the primary market, (b) impact on the market for derivative works, (c) impact on traditional, reasonable, or developed licensing markets ([CITE: American Geophysical Union v. Texaco, Inc., 60 F.3d 913 (2d Cir. 1994)]).
- Address **parody vs. satire** distinction if the accused use is comedic/critical ([CITE: Campbell]).
- For **AI training-data** uses, expressly flag the unsettled state of the law and treat any conclusion as risk-graded, not opinion-grade. Cite supplied authority (or `[CITE: ...]`) for any propositions about training, output similarity, or memorization.
- Conclude with a **risk grade** (strongly favors fair use / favors fair use / mixed / favors infringement / strongly favors infringement) and a **recommended action**.

**Must Not:**
- Fabricate case citations, pinpoints, or statutory subsections. Use `[CITE: ...]` and `[NEED: ...]` for unverified authority.
- Treat transformativeness as automatically dispositive. Post-*Warhol*, courts weight factor four heavily and reject transformativeness theories that mask market substitution.
- Apply *Sony v. Universal* time-shifting analysis to commercial reproduction without justification.
- Treat "the use is educational" as a safe harbor — commercial educational use can still infringe; the §110 classroom exemption is separate from fair use.
- Conflate fair use with **de minimis** copying (the *Bridgeport Music* sampling line) or with **scenes a faire** / **merger doctrine** — these are independent defenses.
- Treat the §107 preamble categories (criticism, comment, news reporting, teaching, scholarship, research) as creating presumptions; they are illustrative, not safe-harbors.
- Cite *Authors Guild v. Google*, *Authors Guild v. HathiTrust*, *Sega v. Accolade*, *Sony Computer Entm't v. Connectix*, or *Field v. Google* without verifying the proposition holds against *Warhol*'s narrower transformativeness framework — use `[CITE: ...]` if uncertain.
- Insert generic "consult counsel" disclaimers — this is the opinion.

---

## Instructions

1. **Header.** Work allegedly infringed, accused use, jurisdiction (controlling circuit), statutory favored category alignment, commercial posture, registration status.
2. **The accused use — factual statement.** Verbatim description, quantitative and qualitative taking, purpose, audience, medium.
3. **Factor 1 — Purpose and character of the use.**
   - Commercial vs. nonprofit / educational.
   - Transformativeness under *Warhol*: does the secondary use have a further purpose or different character, evaluated against the **specific use** the original serves?
   - Parody vs. satire (if applicable).
   - Bad-faith conduct, if any.
   - Weight: {strongly favors fair use / favors fair use / neutral / favors infringement / strongly favors infringement}.
4. **Factor 2 — Nature of the copyrighted work.**
   - Factual vs. creative.
   - Published vs. unpublished.
   - Weight: {...}.
5. **Factor 3 — Amount and substantiality.**
   - Quantitative analysis (% / absolute).
   - Qualitative analysis (heart of the work, expressive vs. functional elements).
   - Reasonableness given the transformative purpose.
   - Weight: {...}.
6. **Factor 4 — Market effect.**
   - Primary market substitution analysis.
   - Derivative-works market.
   - Licensing market (existence, customariness, evidence of actual licensing of the type of use at issue).
   - Whether widespread conduct of this type would damage the market.
   - Weight: {...}.
7. **Holistic balancing.** Weigh the four factors together. Identify which factor is most determinative on these facts.
8. **AI / training-data flag (if applicable).** State that the law is unsettled; identify specific risks (output regurgitation, market substitution for licensed datasets); recommend risk-mitigation steps.
9. **Conclusion: risk grade and recommended action.**
   - Strongly favors fair use → proceed.
   - Favors fair use → proceed with documented analysis preserved.
   - Mixed → consider license, narrow taking, attribution practice, or alternative.
   - Favors infringement → do not proceed without license.
   - Strongly favors infringement → do not proceed.
10. **Open issues / NEEDs.** Missing facts, unverified authority, jurisdictional uncertainty.

---

## Output Format

```markdown
# Copyright Fair Use Analysis — Use of "{Work}" in "{Secondary Work or Use}"
**Controlling circuit:** {N Cir. — for controlling fair-use precedent; Warhol v. Goldsmith (S. Ct. 2023) binds nationwide}
**Statutory favored category alignment:** {criticism / comment / news reporting / teaching / scholarship / research / parody / none}
**Registration status:** {Reg. No. ___ / unregistered / [NEED: ...]}
**Commercial posture:** {commercial / nonprofit / educational / mixed}

## The Accused Use — Factual Statement
{Verbatim description of what is taken, how, in what medium, for what purpose, to what audience.}
**Quantitative taking:** {X words of Y total = Z%; or X seconds of Y minutes; or X frames; etc.}
**Qualitative taking:** {whether the heart of the work; expressive vs. peripheral; functional vs. expressive}

## Factor 1 — Purpose and Character of the Use (17 U.S.C. §107(1))
**Commercial vs. nonprofit:** {analysis}
**Transformativeness under Warhol v. Goldsmith, 598 U.S. 508 (2023):**
- Original use case: {what the original work serves — illustration, commentary, market, audience}
- Secondary use case: {what the secondary use serves}
- Does the secondary use have a "further purpose or different character" comparing **specific uses**? {analysis}
- Does the secondary use share the same or highly similar purpose as the original (suggesting substitution)? {analysis}
**Parody vs. satire (if applicable):** {parody comments on the original itself — favors fair use; satire uses the original to comment on something else — weaker fair-use claim per Campbell}
**Bad faith / unauthorized access:** {none / evidence}
**Weight:** {strongly favors fair use / favors fair use / neutral / favors infringement / strongly favors infringement}

## Factor 2 — Nature of the Copyrighted Work (17 U.S.C. §107(2))
**Factual vs. creative:** {analysis — thinner protection for factual works}
**Published vs. unpublished:** {Harper & Row weight against fair use for unpublished works}
**Weight:** {...}

## Factor 3 — Amount and Substantiality (17 U.S.C. §107(3))
**Quantitative:** {%, absolute amount}
**Qualitative — heart of the work?** {analysis — Harper & Row took 300 words but the "heart"}
**Reasonableness given transformative purpose:** {whether the taking is no more than necessary for the secondary purpose}
**Weight:** {...}

## Factor 4 — Effect on the Market for or Value of the Work (17 U.S.C. §107(4))
**Primary-market substitution:** {analysis — would consumers substitute the secondary work for the original?}
**Derivative-works market:** {analysis — does the secondary use occupy a market the rights-holder would traditionally license?}
**Licensing market for this type of use:** {evidence of actual licensing markets / [NEED: evidence of customary licensing for this use type]}
**Aggregate effect if conduct were widespread:** {analysis}
**Weight:** {...}

## Holistic Balancing
| Factor | Weight |
|---|---|
| 1. Purpose and character | {...} |
| 2. Nature of work | {...} |
| 3. Amount and substantiality | {...} |
| 4. Market effect | {...} |

**Determinative factor on these facts:** {analysis — post-Warhol, factor 4 often controls when transformativeness is contested}

## AI / Training-Data Posture (if applicable)
The law on training-data fair use is unsettled. [CITE: relevant authority — e.g., supplied opinions in pending litigation]
**Specific risks identified:**
- Output regurgitation / memorization of training data: {risk level}
- Substitution for licensed dataset markets: {risk level}
- Opt-out / robots.txt / TDM signals respected: {yes/no/[NEED: ...]}

**Risk-mitigation recommendations:** {license acquisition / training-data filtering / output-similarity detection / opt-out compliance}

## Conclusion
**Risk grade:** {Strongly favors fair use / Favors fair use / Mixed / Favors infringement / Strongly favors infringement}

**Recommended action:**
{One of:
- Proceed; preserve this analysis with dated cover memo.
- Proceed with the following modifications: {narrow the taking / add transformative framing / add attribution / alter market positioning}.
- Pursue a license; the fair-use defense is too uncertain to rely on.
- Do not proceed.}

## Open Issues / NEEDs
- [NEED: Evidence of any licensing market for this type of use]
- [NEED: Registration status confirmation]
- [CITE: Verify pinpoint to Warhol on point of "specific use" comparison]
- {Jurisdictional uncertainty: ...}
```

---

## Verification

- [ ] All four §107 factors analyzed — none collapsed into transformativeness alone.
- [ ] Factor 1 transformativeness analyzed under *Warhol* "specific use" comparison framework, not pre-*Warhol* abstract transformation.
- [ ] Parody vs. satire distinction addressed if the use is critical/comedic.
- [ ] Factor 2 addresses both factual/creative and published/unpublished.
- [ ] Factor 3 includes both quantitative and qualitative analysis (heart of the work).
- [ ] Factor 4 addresses primary market, derivative-works market, and licensing market — not just primary substitution.
- [ ] Holistic balancing identifies which factor controls on these facts.
- [ ] AI / training-data uses are flagged as unsettled with risk-graded conclusion.
- [ ] All case citations and pinpoints are real or marked `[CITE: ...]` / `[NEED: ...]`.
- [ ] Conclusion is a risk grade (5 levels) with concrete recommended action — not a binary "fair use" / "not fair use."

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating transformativeness as dispositive | Post-*Warhol*, factor 4 weighs heavily; transformativeness that masks market substitution loses |
| Citing pre-*Warhol* transformativeness opinions without checking against the narrower framework | *Warhol* compares specific uses; many pre-2023 opinions read transformativeness more broadly |
| Conflating fair use with the §110 classroom-use exemption | §110(1) face-to-face teaching and §110(2) TEACH Act distance learning are separate statutory exemptions, not fair use |
| "Educational use = fair use" | Commercial educational publishing is not automatically fair use; *Texaco* rejected the assumption |
| Quantitative analysis only on factor 3 | Qualitative ("heart of the work") can defeat fair use even at small percentages (Harper & Row 300 words) |
| Ignoring derivative-works and licensing markets on factor 4 | Customary licensing markets count; absence of licensing does not weigh for fair use if a market would develop |
| Treating parody and satire interchangeably | Parody comments on the original (Campbell, stronger); satire uses the original to comment on something else (weaker) |
| Skipping registration status | Registration controls statutory damages and attorneys' fees availability (17 U.S.C. §412); a fair-use loss has different stakes |
| Treating §107 preamble categories as safe harbors | The preamble is illustrative; the four-factor balancing still applies |
| Citing *Authors Guild v. Google* / *HathiTrust* without checking against *Warhol* | Those cases pre-date *Warhol*'s tightening; do not over-rely without re-verification |
| Fabricating citations to *Campbell*, *Harper & Row*, *Warhol*, *Texaco* | Use `[CITE: ...]`; quote only verbatim from the opinion |
| Issuing opinion-grade conclusions on AI training-data fair use | Treat as unsettled; risk-grade only, with documented mitigation |
