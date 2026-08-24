# `domain-science/ethics-integrity/`

The research-ethics-and-integrity layer: resolving authorship and credit, disclosing conflicts, screening for dual-use concern, auditing AI use, self-checking for fabrication / falsification / plagiarism and image manipulation, and walking the correction-vs-retraction decision. Runs alongside the methods and statistics layers throughout the project, and especially before submission.

**Load-bearing convention for this directory:** these prompts **structure, disclose, screen, and self-audit — they never adjudicate**. They do not assign guilt, issue a biosecurity or legal determination, or substitute for the institution's research-integrity office, IBC / DURC committee, journal editor, ORI, or a COPE flowchart. Formal allegations and final decisions route to those bodies. Nothing is invented: every contribution, financial relationship, image, and policy is `[user-supplied]`.

## Map (Phase 2H — 8 prompts)

### Credit & disclosure

| File | Coverage |
|---|---|
| [`science_authorship_and_credit_resolver.md`](science_authorship_and_credit_resolver.md) | CRediT 14-role × contributor matrix + ICMJE four-criteria authorship determination; guest/ghost-authorship and order |
| [`science_conflict_of_interest_disclosure_drafter.md`](science_conflict_of_interest_disclosure_drafter.md) | Financial + non-financial COI elicitation; ICMJE-form-aligned per-author statements; over-disclose-when-in-doubt |

### Self-audit before submission

| File | Coverage |
|---|---|
| [`science_misconduct_self_audit.md`](science_misconduct_self_audit.md) | Pre-submission FFP + QRP risk register (neutral, non-accusatory); "reproduce every number from raw data" |
| [`science_image_integrity_self_check.md`](science_image_integrity_self_check.md) | Blot/gel/micrograph allowed-vs-forbidden adjustments, raw-image retention, duplication self-scan |
| [`science_responsible_ai_use_in_research_audit.md`](science_responsible_ai_use_in_research_audit.md) | AI-use inventory → acceptable-with-disclosure vs unacceptable (ICMJE/COPE); disclosure-statement draft |
| [`science_open_science_practices_self_audit.md`](science_open_science_practices_self_audit.md) | FAIR / CARE / TRUST + preregistration/open-materials scored audit at submission and study close |

### Governance & post-publication

| File | Coverage |
|---|---|
| [`science_dual_use_research_assessment.md`](science_dual_use_research_assessment.md) | **Defensive, governance-level** DURC self-screen → routing + mitigation; no operational detail |
| [`science_retraction_or_correction_decision_walkthrough.md`](science_retraction_or_correction_decision_walkthrough.md) | Correction (erratum/corrigendum) vs expression of concern vs retraction per COPE; honest notice skeleton |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study/manuscript context; invents nothing (`[user-supplied]` gaps); locks the output format; names the relevant standard (CRediT, ICMJE, COPE, ORI FFP, FAIR/CARE/TRUST, US DURC/P3CO at governance level); uses neutral, non-accusatory language; routes formal processes to the proper body; and ends with a verification checklist + false-positive matrix. The dual-use prompt explicitly balances Open Science against biosecurity and names responsible-disclosure / restricted-sharing as the considered exception.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
