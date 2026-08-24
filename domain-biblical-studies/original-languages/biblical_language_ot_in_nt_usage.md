---
title: "OT-in-NT Usage Analysis (MT / LXX / NT Citation) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Analyze how a New Testament text uses an Old Testament quotation or allusion: compare the wording across the Masoretic Text, the Septuagint, and the NT citation (all supplied by the user), classify the kind of use, and attribute interpretive approaches to identifiable streams — while NEVER fabricating textual apparatus, versification, or which-textual-tradition claims, and routing every wording and variant question to named real resources."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - ot-in-nt
  - septuagint
  - masoretic-text
  - quotation
  - intertextuality
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
---

# OT-in-NT Usage Analysis (MT / LXX / NT Citation)

**Objective:** Take a New Testament text that quotes or alludes to the Old Testament and structure a disciplined comparison — how the wording differs across the Masoretic Text, the Septuagint, and the NT citation (all **supplied by the user**), what kind of use the NT author is making, and how interpretive streams account for the differences — **without fabricating textual apparatus, versification, or claims about which textual tradition a citation follows.** The output is a comparison and method scaffold the user verifies against named real resources.

> **STRONG-GUARD prompt.** This is among the highest-fabrication-risk prompts in the domain. Models routinely invent which manuscripts read what, assert that "the NT follows the LXX here," fabricate apparatus and variant data, and misremember chapter/verse numbering (which differs between MT, LXX, and English). Here, **every wording, versification, variant, and which-tradition claim is verify-required**; the user supplies all three texts, and nothing about manuscripts or numbering is asserted from memory.

**When to use:**
- A NT passage quotes/alludes to the OT and you want to compare the wording across MT, LXX, and NT.
- You want to classify the kind of use (quotation, allusion, echo) and how the NT author handles the source.
- You're examining why the NT wording matches/differs from the Hebrew or the Greek OT.

**When NOT to use:**
- You want a general canonical/intertextual trace across Scripture (not the MT/LXX/NT triangulation) — use `biblical_canonical_intertextual_reading.md`.
- Your question is purely why translations differ in one verse — use `biblical_translation_comparison.md`.
- You cannot supply or verify the three texts (MT, LXX, NT) — without them this analysis is unreliable; say so and stop.

**Audience:** Seminary/academic (A) and pastors (P) able to access the MT, a critical LXX, and a critical NT.

---

## Inputs / Context

1. **The NT citation.** The NT verse(s) and text in a named edition/translation, plus the OT reference the user believes is being used — pasted by the user.
2. **The OT source texts.** The corresponding OT passage as the user has it from the **MT** (Hebrew) and the **LXX** (Greek), each in a named edition/translation — pasted by the user. The model references by address and does not supply these from memory.
3. **Known textual data (optional).** Any apparatus/variant notes or versification mappings the user already has — supplied so the model organizes, not invents, them.
4. **Declared tradition (optional).** If supplied, the model may foreground that stream's approach to OT-in-NT use but still notes alternatives.
5. **The question.** Classify the use / explain the wording differences / weigh interpretive significance — sets focus.

---

## Constraints

### Must
- Work only from the three texts the user supplies (MT, LXX, NT); compare wording among them by address.
- Treat every textual-history claim — which manuscript reads what, whether the NT "follows" MT or LXX, variant readings, apparatus, and versification mapping — as **verify-required**, routed to a critical edition's apparatus and a Septuagint study resource. Never assert these from memory.
- Flag **versification differences** explicitly (MT vs. LXX vs. English numbering can differ) and tell the user to confirm the mapping, rather than asserting a verse number.
- Classify the *kind* of use descriptively (quotation / allusion / echo / composite citation) with the criteria you are applying, and note classification is interpretive.
- Present **competing interpretive approaches** to OT-in-NT use (e.g., readings that emphasize original OT context vs. those that emphasize the NT author's christological/typological reframing) and attribute them to streams without ruling.
- State confidence on the central claim (especially any claim about source tradition) and what would confirm it.

### Must Not
- Assert which textual tradition a NT citation follows, or invent/assert variant readings, apparatus, or manuscript sigla from memory.
- State a verse number for MT/LXX/NT from memory as if certain; flag versification as verify-required.
- Supply the MT, LXX, or NT wording from memory in place of the user's texts, or quote a critical edition's apparatus verbatim from memory.
- Privilege the interpretive approach that favors any tradition's conclusion as the correct one; smuggle a doctrinal verdict through the "which text" question.
- Treat a perceived allusion as a certain quotation without flagging the classification as interpretive.

### Tradition-neutral stance (Must / Must Not)
- **Must:** present the wording comparison and the range of interpretive approaches to OT-in-NT use, attributing each to identifiable streams (e.g., grammatical-historical-priority readings, typological/christological readings, intertextual/"metalepsis" readings) descriptively.
- **Must Not:** endorse one approach as correct, or present a contested classification or christological reading as the plain sense.

---

## Instructions

### Step 1 — Fix the three texts and references
Restate the NT citation reference and the proposed OT source reference. Confirm the user has supplied the **NT text, the MT text, and the LXX text**. If any is missing, mark "not supplied — provide before analysis" and do not fill it from memory. Flag that MT/LXX/English versification may differ and the mapping must be verified.

### Step 2 — Align and compare the wording
Lay the three texts side by side (user-supplied) and note, by observation, where the NT wording agrees with the MT, agrees with the LXX, agrees with neither, or differs from both. Describe the differences; do **not** conclude "the NT follows X" — mark that conclusion as verify-required against critical editions.

### Step 3 — Classify the kind of use
Apply explicit criteria to classify the use (formal quotation with introductory formula / unmarked quotation / allusion / echo / composite or conflated citation). State the criteria and flag the classification as interpretive.

### Step 4 — Account for the differences (candidate explanations, verify)
List candidate explanations for the wording differences (translation from Hebrew, use of a Greek OT form, paraphrase/adaptation, a different Vorlage, textual variants) — each flagged **verify-required** and routed to a critical NT apparatus, a critical LXX, and Septuagint scholarship. Do not assert which explanation is correct from memory.

### Step 5 — Interpretive approaches (attributed, not ruled)
Present the main interpretive approaches to how the NT author uses the OT here, attributing each to identifiable streams, and note how each handles any context shift between the OT setting and the NT use — without adjudicating.

### Step 6 — Significance + confidence
State what is at stake interpretively, each claim tagged **text-supported (verify)** or **inference (stream)**. Give confidence on any source-tradition claim (which will usually be low without apparatus verification) and the single most important verification step.

---

## Output Format

```
# OT-in-NT Usage — [NT ref] using [OT ref]

## Texts (all user-supplied; versification VERIFY — MT/LXX/English may differ)
- NT: [ref] ([edition], supplied)
- MT: [ref] ([edition], supplied)  | versification mapping: verify
- LXX: [ref] ([edition], supplied) | versification mapping: verify

## Wording comparison (observation only)
| Element | NT | MT | LXX | Agrees with (observed) |
|---------|----|----|-----|------------------------|
| [..] | [..] | [..] | [..] | MT / LXX / neither / both (observed, not a source-claim) |
- "Which tradition the NT follows": NOT asserted — verify against critical editions

## Classification of use (interpretive)
- Type: quotation / allusion / echo / composite (criteria applied: ..) — interpretive

## Candidate explanations for differences (VERIFY)
- [explanation] — verify in [critical NT apparatus / critical LXX / Septuagint scholarship]

## Interpretive approaches (attributed, not ruled)
- [Stream A approach]: [..] | [Stream B approach]: [..]
- Handling of OT→NT context shift per approach: [..]

## Significance & confidence
- [claim] — text-supported (verify) / inference ([stream])
- Source-tradition claim confidence: low / moderate / high (low without apparatus check)
- Most important verification step: [..]
```

---

## Verification

- [ ] All three texts (NT, MT, LXX) used as user-supplied; none filled from memory.
- [ ] No claim about which textual tradition the NT follows asserted from memory; flagged verify against critical editions.
- [ ] No variant readings, apparatus, or manuscript sigla invented or asserted from memory.
- [ ] Versification differences (MT/LXX/English) flagged and routed to verification, not asserted.
- [ ] Use-classification stated with criteria and marked interpretive.
- [ ] Competing interpretive approaches attributed to streams, not adjudicated.
- [ ] Central source-tradition claim carries confidence + a named verification step.

---

## False-Positive Prevention

❌ **DON'T:**
- Declare "the NT here quotes the LXX, not the Hebrew" from memory — this is exactly the claim that requires apparatus verification.
- Invent variant readings, apparatus notes, or manuscript names to explain a difference.
- Assert MT/LXX/NT verse numbers from memory when numbering systems diverge.
- Supply the OT or NT wording yourself instead of using the user's texts.
- Present a typological/christological reading (or a strict original-context reading) as the obviously correct approach.

✅ **DO:**
- Compare only the user-supplied texts and describe observed agreement, not source-conclusions.
- Flag every textual-history, variant, and versification claim as verify-required and name the resource.
- State classification criteria and mark the classification interpretive.
- Attribute competing OT-in-NT approaches to streams without ruling.
- Keep source-tradition confidence low until the user checks a critical apparatus.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix texts → Compare wording → Classify use → Explain differences → Interpretive approaches → Significance) keeps observation (wording comparison) prior to any source-tradition or interpretive conclusion.
- **RT-02 (Multi-Dimensional Analysis Framework):** Triangulates across three textual witnesses (MT, LXX, NT) and across interpretive dimensions (textual, classificational, interpretive-stream) so no single axis carries the verdict.
- **RT-05 (Evidence-Based Reasoning):** Wording claims rest only on user-supplied texts; every textual-history, variant, and source claim is grounded in a named critical resource or flagged unverified.
- **QA-04 (Uncertainty Acknowledgment):** Use-classification is marked interpretive; source-tradition claims default to low confidence without apparatus verification; each significance claim is tagged text-supported (verify) vs. inference (stream).
- **QA-05 (Citation Requirements):** Requires routing every variant, apparatus, versification, and source question to named real resources (critical NT, critical LXX, Septuagint scholarship), with nothing recalled from memory presented as authoritative.
- **OC-12 (External Reference Catalog):** The output embeds a structured catalog of the critical editions and scholarship needed to verify the wording comparison, the explanations for differences, and any source-tradition claim.
