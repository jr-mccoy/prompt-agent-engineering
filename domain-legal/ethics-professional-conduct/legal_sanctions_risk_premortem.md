---
title: "Sanctions Risk Pre-Mortem — Rule 11, § 1927, Inherent Power, and Fee-Shifting Exposure"
category: legal/ethics-professional-conduct
description: "Before filing or continuing a position, imagine it has drawn a sanctions motion and work backward: test each factual contention, legal contention, and purpose against the certification standards in the supplied rule text (FRCP 11 or state analog), screen for conduct that could be characterized as unreasonably multiplying proceedings (28 U.S.C. § 1927), bad faith (inherent power), or triggering statutory or contractual fee-shifting, and verify every citation exists and says what the filing claims. Produces a risk register with fixes before filing."
techniques:
  - QA-02
  - RT-02
  - NE-10
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - ethics
  - professional-responsibility
  - sanctions
  - rule-11
  - litigation-risk
  - citation-verification
  - pre-mortem
  - frivolous-filing
updated: "2026-09-24"
reasoning:
  styles: [adversarial, evaluative, prospective]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [structured, matrix]
  user_role: [attorney, litigation_partner, firm_general_counsel]
related_prompts:
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-legal/litigation/legal_motion_to_dismiss_12b6.md
  - domain-legal/research/legal_research_memo_irac.md
---

# Sanctions Risk Pre-Mortem

**Objective:** Stress-test a filing, or a continuing litigation position, before it goes out by assuming the opponent or the court has moved for sanctions and asking why the motion would succeed. The pre-mortem checks each factual contention for evidentiary support (or a properly flagged "likely to have support after discovery"), each legal contention for grounding in existing law or a nonfrivolous argument to change it, the filing's purpose, the course of conduct for unreasonable multiplication of proceedings, any indicator of bad faith, and fee-shifting exposure — and verifies that every cited authority exists and supports the proposition. Output is a risk register with specific fixes, and a go / fix-then-file / withdraw recommendation.

**When to use:**
- Before filing a complaint, counterclaim, dispositive motion, or brief that takes an aggressive factual or legal position.
- Before continuing a claim after discovery has undermined a factual contention (the continuing-duty problem).
- When an opponent has served a safe-harbor letter or draft sanctions motion.
- When any part of the filing was drafted or researched with AI assistance and citations have not been independently verified.

**Distinct from:**
- `domain-legal/litigation/legal_case_strategy_assessment.md` — merits and strategy; this prompt tests sanctionability of specific contentions and conduct.
- `domain-legal/research/legal_research_memo_irac.md` — builds the legal analysis; this prompt audits whether the filing's citations and characterizations hold up.
- `domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md` — engagement-level ethics, not filing-level exposure.

---

## Your Input

- **Court and jurisdiction:** [Federal district / state court; circuit or appellate district]
- **Rules text supplied:** [FRCP 11 or the state analog; any local rule on sanctions or AI-use certification; the fee-shifting statute or contract clause, if any. Anything not supplied is marked `[VERIFY]`.]
- **Filing or position:** [Draft text or summary of each claim, defense, or argument]
- **Factual contentions and support:** [For each: the evidence in hand, or why support is expected after discovery]
- **Legal authorities cited:** [Full list with the proposition each is cited for, plus the text of each authority or the relevant excerpt, if available]
- **Procedural history and conduct:** [Prior motions, extensions, discovery disputes, prior warnings from the court, opposing counsel's safe-harbor letters]
- **Drafting process:** [Who drafted; whether AI tools were used; verification steps taken]
- **Client-driven considerations:** [Client's objectives, any pressure to file quickly, leverage motives]

---

## Constraints

**Must:**
- Run the pre-mortem explicitly: "Assume a sanctions motion was granted. List the strongest reasons." Then test each.
- Test each factual contention against the supplied rule's factual-support standard; any contention relying on expected discovery must be specifically identified as such if the supplied rule requires it.
- Test each legal contention: existing law supports it, or it is a nonfrivolous argument for extending, modifying, or reversing law — and if the latter, whether the filing says so candidly.
- Examine purpose indicators (timing, leverage, duplicative filings, public-relations use).
- Screen course of conduct for unreasonable and vexatious multiplication (repetitive motions, pursuing claims after they became untenable) and for bad-faith indicators relevant to inherent-power sanctions.
- Verify every citation: exists, is correctly cited, supports the stated proposition, is not overruled or superseded (flag as `[NEED: citator check]` if not confirmed), and quotations are verbatim.
- Rate each risk with probability language (unlikely / possible / likely) and a reason, and give a specific fix.
- Note any safe-harbor procedure in the supplied rule and what it allows (withdraw or correct within the stated period).

**Must Not:**
- Invent, "fill in," or reconstruct any citation, pin cite, holding, or quotation. Unverifiable authorities are flagged `[NEED HOLDING: ...]` or `[NEED PIN: ...]` and treated as unsupported until verified.
- Invent sanctions standards, safe-harbor periods, local rules, or example sanctions awards. Use `[CITE: ...]`, `[VERIFY: ...]`.
- Treat a legal argument as frivolous merely because it is novel or contrary to the majority rule; assess candor and good-faith basis.
- Recommend proceeding with a contention that lacks factual support to "see what discovery shows" without the required flag.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Pre-mortem framing.** Write the three strongest paragraphs of the hypothetical sanctions motion.
2. **Citation audit.** Table of every authority: exists (verified / unverified), citation form, proposition, supports? (yes / partially / no / unknown), quote verbatim?, subsequent history checked?
3. **Factual-contention review.** Each contention → evidence → standard met? → fix (add support, recharacterize, flag as needing discovery, delete).
4. **Legal-contention review.** Each contention → existing-law support or good-faith extension argument → candor → fix.
5. **Purpose review.** Indicators and mitigations.
6. **Course-of-conduct and bad-faith screen.** Past and planned conduct; § 1927-type and inherent-power exposure.
7. **Fee-shifting exposure.** Statutory or contractual provisions (supplied text) and the triggering standard.
8. **Risk register and recommendation.** Probability, severity (monetary, non-monetary, referral, reputational, client harm), fix, owner; overall go / fix-then-file / withdraw.

---

## Output Format

```markdown
# Sanctions Risk Pre-Mortem — {Filing / Position} — {Court}
**Privileged & Confidential — Attorney Work Product**

## 1. Recommendation
{Go / Fix then file / Withdraw or narrow} — {reason}

## 2. The Hypothetical Sanctions Motion (strongest three arguments)

## 3. Citation Audit
| # | Authority (as cited) | Exists? | Proposition | Supports? | Quote verbatim? | History checked? | Action |
|---|---|---|---|---|---|---|---|

## 4. Factual Contentions
| # | Contention | Evidence | Standard met? | Fix |
|---|---|---|---|---|

## 5. Legal Contentions
| # | Contention | Basis (existing law / extension) | Candor | Fix |
|---|---|---|---|---|

## 6. Purpose and Course of Conduct

## 7. Fee-Shifting Exposure

## 8. Risk Register
| Risk | Source (rule / statute / inherent power) | Probability (reason) | Severity | Fix | Owner |
|---|---|---|---|---|---|

## 9. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** Plaintiff's counsel will file a federal complaint alleging a competitor misappropriated trade secrets and conspired with the plaintiff's former employees. Evidence: two former employees joined the competitor; the competitor launched a similar product nine months later. Draft brief section was prepared with an AI research tool; 14 authorities cited; counsel has full text for 9. FRCP 11 text supplied; no local AI-certification rule supplied.

**Output (excerpt):**
- **Hypothetical motion, argument 1:** "Plaintiff alleged that defendants 'accessed and downloaded' confidential files without any forensic or testimonial evidence of access." → Factual contention #3 lacks present support.
- **Fix:** Either obtain the forensic review of the former employees' last-30-day device activity before filing, or recharacterize and specifically identify the contention as likely to have evidentiary support after discovery, as the supplied rule text permits.
- **Citation audit:** 5 authorities without full text → **Unverified**; one of the 5 cannot be located in any reporter by the citation given → `[NEED HOLDING: authority #11 — citation not found; remove unless located]`. Treat all 5 as unsupported until pulled and read.
- **Local rules:** `[VERIFY: whether the district or assigned judge requires certification of generative-AI use]`.
- **Recommendation:** Fix then file. Risk of sanctions on citations: **likely** if filed as drafted; **unlikely** after verification and removal.

---

## Verification

- [ ] Jurisdiction lock: standards drawn from the supplied rule text of the forum court; local rules checked or `[VERIFY]`.
- [ ] Citation discipline: every authority verified as existing and supporting its proposition, or flagged and treated as unsupported; no authority invented or repaired from memory.
- [ ] Each factual contention has evidence or the required discovery flag.
- [ ] Each legal contention is grounded in existing law or candidly presented as an extension.
- [ ] Course of conduct and bad-faith indicators screened, not just the single filing.
- [ ] Fee-shifting exposure assessed against supplied provisions.
- [ ] Every risk has a probability with reason, a fix, and an owner.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Correcting" an unverifiable citation by guessing the right reporter or pin cite | Never repair from memory; flag `[NEED HOLDING]` / `[NEED PIN]` and treat as unsupported |
| Treating AI-assisted citations as verified because they look well-formed | Pull and read each authority; check subsequent history |
| Labelling a novel argument frivolous | Assess good-faith basis and whether the filing candidly argues for extension |
| Reviewing only the filing and not the course of conduct | Screen repetitive motions and positions maintained after they became untenable |
| Relying on a safe-harbor period from memory | Use the supplied rule text or `[VERIFY]` |
| Ignoring the continuing duty after discovery undermines a contention | Re-run the pre-mortem when facts change; withdraw or amend promptly |
| Quoting an authority accurately but for a proposition it does not support | Check that the holding, not dicta or a dissent, supports the stated proposition |
