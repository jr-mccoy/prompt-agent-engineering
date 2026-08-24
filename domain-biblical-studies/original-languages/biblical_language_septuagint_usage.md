---
title: "Septuagint (LXX) Usage & Masoretic Text Divergences — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Structure a disciplined analysis of where the Septuagint diverges from the Masoretic Text for a user-specified passage — classifying each divergence type (translation technique, Vorlage difference, theological interpretation, scribal), assessing interpretive significance, and noting NT citations — treating every textual claim as candidate / verify-required, requiring the user to supply BOTH texts, and attributing scholarly approaches to streams without ruling."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - septuagint
  - lxx
  - masoretic-text
  - textual-divergence
  - translation-technique
  - old-testament
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_ot_in_nt_usage.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_canon_versification_differences.md
  - domain-biblical-studies/original-languages/biblical_language_textual_criticism_primer.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
---

# Septuagint (LXX) Usage & Masoretic Text Divergences

**Objective:** Take a passage the user supplies — with both the Masoretic Text (MT) and Septuagint (LXX) readings pasted in — and structure a disciplined analysis of where and how the two diverge, what type of divergence each represents, and what the divergences mean for interpretation. **The model never asserts MT or LXX readings from memory.** The output is a classified divergence scaffold the user verifies against critical editions and specialist literature.

> **STRONG-GUARD prompt.** This is among the highest-fabrication-risk prompts in the domain. Models routinely fabricate LXX readings, misremember MT-LXX divergences, invent translation techniques, assert which divergences reflect a different Vorlage without evidence, and confidently produce Greek or Hebrew text from memory that does not match any real edition. **The user must supply both texts.** Every divergence classification, every Vorlage hypothesis, and every translation-technique label is **candidate / verify-required** — never asserted from memory.

**When to use:**
- You have both the MT and LXX text of a passage in front of you and want to understand where and why they differ.
- You are studying a passage where the LXX reading is theologically significant (e.g., messianic readings, divine-name usage, legal differences).
- You are preparing the text-critical or translation-history layer of an exegesis, thesis, or paper.
- You are investigating whether a NT author followed the LXX, the MT, or neither.

**When NOT to use:**
- You do not have both texts in front of you — this prompt requires user-supplied texts and will not reconstruct them from memory.
- Your question is the syntax of the Greek text itself — use `biblical_language_greek_syntax_analysis.md`.
- Your question is how a NT passage uses an OT text — use `biblical_language_ot_in_nt_usage.md` (though the two prompts complement each other).
- Your question is a broad comparison across modern English translations — use `biblical_translation_comparison.md`.

**Audience:** Seminary/academic (A) with access to critical editions (BHS/BHQ, Rahlfs/Goettingen LXX).

---

## Inputs / Context

1. **The passage reference.** Book, chapter, verse(s) — with any versification differences between MT and LXX noted by the user.
2. **The MT text.** Hebrew text pasted by the user from a named edition (BHS, BHQ, or equivalent); the model references by address and does not supply Hebrew text from memory.
3. **The LXX text.** Greek text pasted by the user from a named edition (Rahlfs, Goettingen, or equivalent); the model references by address and does not supply Greek text from memory.
4. **A translation of each (optional but recommended).** Named translations for orientation — helps confirm the user's texts are correctly aligned.
5. **The question (optional).** A specific divergence or pattern the user wants to focus on (e.g., "Why does the LXX add a clause here?" "Does this reflect a different Vorlage?").
6. **Purpose.** Exegesis / text-critical paper / NT-usage study / learning — sets depth.

---

## Constraints

### Must
- Require the user to supply both texts; do not reconstruct, quote, or assert MT or LXX readings from memory.
- Treat every divergence classification (translation technique, Vorlage difference, theological interpretation, scribal error/harmonization) as **candidate / verify-required**.
- Distinguish clearly between (a) what the texts say (supplied by the user) and (b) how the model classifies and interprets the divergence (candidate analysis).
- Where a divergence's cause is debated among text critics, present the competing explanations descriptively and attribute them to identifiable scholarly approaches.
- For any classification, name the *kind* of resource that adjudicates it (a critical edition's apparatus, a specialist LXX commentary, a Vorlage study) and **flag specific citations as verify-required.**
- When noting Dead Sea Scrolls (DSS/Qumran) witnesses, flag all DSS readings as **verify-required** — models are especially unreliable on DSS data.
- Present both the MT and LXX as transmitted textual traditions with their own histories — neither is automatically "original."

### Must Not
- Assert or fabricate any Hebrew or Greek reading from memory; all textual data comes from the user.
- Claim a divergence "definitely reflects a different Vorlage" or "is clearly a translation technique" without flagging the classification as candidate and naming what would adjudicate it.
- Fabricate or assert specific scholarly citations (author, page, section) from memory; name the resource *type* and flag verify-required.
- Invent Dead Sea Scrolls readings or assert Qumran support for a Vorlage hypothesis from memory.
- Use a textual divergence to smuggle in a contested doctrinal conclusion; present tradition-dependent readings as options.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where a divergence bears on a contested theological question (e.g., messianic readings, divine sovereignty vs. human agency, monotheism/angelology), lay out the interpretive options and attribute them to identifiable traditions or scholarly positions descriptively.
- **Must Not:** privilege the reading (MT or LXX) that favors any tradition's doctrinal conclusion, or treat either text as inherently "more original" without argument and evidence.

---

## Instructions

### Step 1 — Confirm passage and user-supplied texts
Restate the passage reference. Confirm that the user has supplied both the MT text (from a named edition) and the LXX text (from a named edition). If either is missing, request it before proceeding — "Supply the [MT/LXX] text from a critical edition before proceeding; I cannot supply original-language wording from memory." Echo user-supplied texts as **supplied-by-user**. Note any versification differences between MT and LXX for the passage (flag as verify-required; cross-reference `biblical_language_canon_versification_differences.md`).

### Step 2 — Map divergences between MT and LXX
Working from the user-supplied texts, identify each point where the LXX diverges from the MT. For each divergence, state precisely what the MT reads (as supplied) and what the LXX reads (as supplied). Number each divergence for reference. Describe the nature of the difference observationally (addition, omission, substitution, transposition, expansion, different syntax) without yet classifying the *cause*. Flag any ambiguity in alignment as **candidate alignment (verify)**.

### Step 3 — Classify each divergence type (candidate)
For each numbered divergence, offer a candidate classification from the standard typology, each flagged **candidate (verify)**:
- **Translation technique:** The translator rendered the Hebrew into Greek using a recognizable method (dynamic equivalence, harmonization to context, lexical substitution, simplification, expansion for clarity). Note that translation technique varies by LXX book and even by section — verify against translation-technique studies for this specific book.
- **Vorlage difference:** The LXX translator may have been working from a Hebrew text that differed from the MT at this point. Explain the test: Can a plausible Hebrew Vorlage be reconstructed? Do any DSS manuscripts support it? Do other ancient versions agree with the LXX or the MT? Flag all DSS and versional data as **verify-required**.
- **Theological interpretation:** The translator added or modified material reflecting theological commitments or interpretive tradition. Explain what would support this classification.
- **Scribal:** Copying error, dittography, haplography, metathesis, or later harmonization in the transmission of either text.

Where multiple classifications are viable, present them as competing hypotheses and explain what evidence would disambiguate them.

### Step 4 — Assess interpretive significance
For each significant divergence, state what interpretive difference it makes. Tag each interpretive payoff as **text-supported (verify)** or **inference (stream)**. Where the divergence affects a theologically loaded question, present the tradition-dependent readings without adjudicating. State what each reading communicates and how it has been received in its tradition (Jewish reading of MT, early Christian reception of LXX).

### Step 5 — Note NT usage if the passage is cited in the NT
If the passage (or any portion of it) is cited or alluded to in the NT, note the NT reference and whether the NT author appears to follow the LXX, the MT, or neither — working from user-supplied texts only. Flag all NT-citation alignments as **candidate (verify)**. Do not assert "the NT author used the LXX here" from memory — this conclusion requires wording comparison across all three texts. Route to `biblical_language_ot_in_nt_usage.md` for deeper triangulation.

### Step 6 — Tradition-neutral presentation of scholarly approaches
Where the divergence is debated, present how different scholarly approaches handle it:
- **Vorlage-priority approaches:** Scholars who argue the divergence reflects a different Hebrew source text.
- **Translation-technique approaches:** Scholars who argue the divergence reflects the translator's rendering strategy.
- **Theological-Tendenz approaches:** Scholars who argue the divergence reflects interpretive expansion or theological adjustment.
- Attribute each approach to its scholarly stream without ruling; name the resource *types* that adjudicate (flagged verify-required).

Give confidence on the central divergence classification(s) and the one verification step that matters most. List the resource *types* to consult (critical edition apparatus, specialist LXX commentary, Vorlage study, DSS edition), with specific citations flagged verify-required.

---

## Output Format

```
# LXX / MT Divergence Analysis — [reference]

## Orientation
- Passage: [reference] (MT versification: [..] | LXX versification: [..] — VERIFY)
- MT text: [supplied-by-user from named edition]
- LXX text: [supplied-by-user from named edition]
- Question: [..]

## Divergence map (from user-supplied texts)
| # | MT reads (supplied) | LXX reads (supplied) | Type of difference |
|---|---------------------|----------------------|--------------------|
| 1 | [..] | [..] | [addition / omission / substitution / transposition / expansion] |
| 2 | [..] | [..] | [..] |

## Divergence classification (candidate — VERIFY against critical editions & specialist literature)
| # | Candidate classification | Alt classification(s) | Evidence that would disambiguate | Verify in |
|---|-------------------------|----------------------|----------------------------------|-----------|
| 1 | candidate (verify) | [..] | [..] | [resource type] (citation flagged verify) |

## Interpretive significance
- Divergence #[n]: [interpretive payoff] — text-supported (verify) / inference ([stream])
- MT reading communicates: [..] | LXX reading communicates: [..]
- Tradition-dependent readings: [Option A — stream] | [Option B — stream]

## NT citation check (if applicable)
- [NT ref] appears to follow: [LXX / MT / neither / mixed] — candidate (verify)
- Full triangulation: route to biblical_language_ot_in_nt_usage.md

## Scholarly approaches (attributed, not adjudicated)
- Vorlage-priority: [..] — [resource type, citation verify-required]
- Translation-technique: [..] — [resource type, citation verify-required]
- Theological-Tendenz: [..] — [resource type, citation verify-required]

## Confidence & verification map
- Central classification: [..] (confidence: low/mod/high; would change if ..)
- Most important verification step: [..]
- Consult (specific citations verify-required): [critical edition apparatus], [specialist LXX commentary], [Vorlage study], [DSS edition if relevant]
```

---

## Verification

- [ ] User supplied both MT and LXX texts; no readings invented or asserted from memory.
- [ ] Every divergence classification flagged candidate/verify-required; none asserted as settled fact.
- [ ] Vorlage hypotheses flagged as candidate with disambiguating evidence named; no DSS readings asserted from memory.
- [ ] No specific scholarly citation (author/page/section) asserted from memory — resource types named, citations flagged verify.
- [ ] Tradition-dependent interpretive significance attributed to streams, not adjudicated.
- [ ] NT citation alignment flagged candidate (verify) and routed to the OT-in-NT prompt for depth.
- [ ] Neither MT nor LXX privileged as the "original" text; both presented as transmitted traditions.
- [ ] Central conclusion carries confidence + a change condition.

---

## False-Positive Prevention

❌ **DON'T:**
- Supply or "fill in" MT or LXX readings from memory — models routinely fabricate Greek and Hebrew text.
- Confidently assert "this reflects a different Vorlage" without flagging the claim as candidate and naming what evidence would confirm or refute it.
- Cite Dead Sea Scrolls readings from memory — DSS data is among the most frequently fabricated content.
- Cite "Tov, p. ___" or "Jobes & Silva, ch. ___" from memory — these are routinely misremembered or invented.
- Let the reading (MT or LXX) that supports a doctrinal conclusion win without naming the alternative and the tradition that holds it.

✅ **DO:**
- Require the user to paste both texts from named critical editions before beginning analysis.
- Flag every classification as candidate (verify) and route it to critical editions and specialist resources.
- Present debated divergences as competing hypotheses attributed to scholarly positions.
- Flag all DSS/Qumran evidence as verify-required with special emphasis.
- State confidence and the single most decisive verification step.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Confirm texts → Map divergences → Classify → Interpretive significance → NT citation check → Scholarly approaches + confidence) prevents leaping from a recalled divergence to a theological conclusion.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across distinct dimensions — textual divergence type, classification cause, interpretive significance, NT usage, scholarly approach — so no single layer is mistaken for the whole.
- **RT-05 (Evidence-Based Reasoning):** Every classification is grounded in a named resource type or flagged unverified; Vorlage hypotheses require disambiguating evidence; DSS data is double-flagged as verify-required.
- **QA-04 (Uncertainty Acknowledgment):** Classifications are flagged candidate (verify); competing scholarly explanations are surfaced; the central conclusion carries a low/moderate/high confidence with a change condition.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for each classification and explicitly flags specific citations (author/section/page) as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (critical edition apparatus, specialist LXX commentary, Vorlage study, DSS edition) needed to validate each textual claim.
