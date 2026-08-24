---
title: "Parsing & Morphology Helper (Greek / Hebrew / Aramaic) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Structure and VERIFY the parsing/morphology of an original-language form the user supplies. The model lays out the checking procedure, explains what each parsing slot means, names real tools, and treats any parse it offers as candidate / verify-required — never asserting morphology, lemmas, or Strong's numbers from memory as authoritative."
techniques:
  - ST-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - parsing
  - morphology
  - greek
  - hebrew
  - aramaic
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
---

# Parsing & Morphology Helper (Greek / Hebrew / Aramaic)

**Objective:** Help the user structure and **verify** the parsing/morphology of one original-language form they supply — explaining what each parsing slot means, laying out a disciplined checking procedure, and routing every parse to a real morphological tool — **without asserting any morphology from memory as authoritative.** The output is a verification scaffold, not a parsing oracle.

> **STRONG-GUARD prompt.** This is among the highest-fabrication-risk prompts in the domain. Language models routinely invent lemmas, parsing codes, Strong's numbers, and frequency counts that look authoritative and are wrong. Every parse this prompt offers is **candidate / verify-required**; nothing is presented as settled unless the user supplied it.

**When to use:**
- You have a Greek, Hebrew, or Aramaic form and want to understand and confirm its parse.
- You want to learn what each parsing category means before trusting a tool's output.
- You want to cross-check a parse you already have against a disciplined procedure.

**When NOT to use:**
- You need an authoritative parse with no way to verify it — go to a tagged morphological database (Accordance, Logos, a reverse interlinear, the morphology in a critical text). This prompt scaffolds and cross-examines; it does not replace those tools.
- Your question is the *function* of the syntax (case use, tense-aspect, clause type) rather than the form's parse — use `biblical_language_greek_syntax_analysis.md` or `biblical_language_hebrew_syntax_analysis.md`.

**Audience:** Seminary/academic (A) and pastors (P) who can access a real morphological tool.

---

## Inputs / Context

1. **The form.** The exact word as it appears (script and/or transliteration) and the verse reference where it occurs.
2. **Surrounding text (optional but recommended).** The clause/verse in a named translation and, if available, the original-language line — pasted by the user; the model references by address and does not quote from memory.
3. **Known data (optional).** Any lemma, parse, or Strong's number the user already has — supplied so the model can organize and cross-check, not invent, it.
4. **Language & corpus.** Greek (NT/LXX), Biblical Hebrew, Biblical/Targumic Aramaic — sets the right morphological system.
5. **Purpose.** Learning the categories / confirming a parse / preparing exegesis — sets depth.

---

## Constraints

### Must
- Treat every morphological datum (lemma, root, parsing of each slot, Strong's number, frequency) as **candidate / verify-required** unless the user supplied it. Label each: **supplied-by-user**, **candidate (verify)**, or **uncertain / ambiguous**.
- Explain what each parsing slot *means* (e.g., for Greek verbs: person, number, tense-form, voice, mood; for Greek nominals: case, number, gender; for Hebrew verbs: stem/binyan, conjugation, person, gender, number) so the user can evaluate a tool's output, not just copy it.
- For any candidate parse, name the *kind* of tool that confirms it (tagged morphological database, reverse interlinear, the morphology line of a critical edition) and instruct the user to verify there.
- Flag genuine **morphological ambiguity** (homographic/defective forms, forms parseable more than one way) rather than forcing a single parse.
- State confidence on any candidate parse and the single most important verification step.

### Must Not
- Assert a lemma, parse, root, Strong's number, or frequency from memory as if authoritative; never invent a Strong's number to fill a gap.
- Quote a lexicon, grammar, or morphological reference verbatim from memory.
- Present a tagged-database-style parse as finished when the user has supplied no data and cannot verify.
- Resolve a genuinely ambiguous form by guessing; surface the options instead.
- Misquote the text; reference by address and use the user's supplied forms.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where a parse bears on a contested reading (e.g., a form that could be parsed two ways with different theological payoff), present both parses and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the parse that favors any tradition's preferred conclusion, or let a morphological choice smuggle in a doctrinal verdict.

---

## Instructions

### Step 1 — Fix the form and its location
Restate the form (script/transliteration) and the exact reference. Echo any user-supplied lemma/parse/Strong's number as **supplied-by-user**. If none supplied, mark "lemma / parse / Strong's #: not supplied — look up in a morphological tool"; do not generate them.

### Step 2 — Name the parsing slots for this language
List the morphological categories that *must* be filled for this part of speech in this language (verb vs. noun vs. participle vs. particle), and explain each slot in one line so the user knows what to confirm.

### Step 3 — Offer a candidate parse (clearly flagged)
If helpful, propose a candidate value for each slot, each labeled **candidate (verify)** or **uncertain / ambiguous**. Immediately instruct: "Confirm each slot against a tagged morphological database / reverse interlinear before relying on it." Never present the candidate parse as definitive.

### Step 4 — Flag ambiguity and alternatives
Identify whether the form is morphologically ambiguous (could be parsed more than one way). List the competing parses and what would disambiguate them (context, accents/pointing, the critical text's tagging).

### Step 5 — Verification procedure
Spell out the concrete checking steps: locate the form in a tagged database; confirm the lemma; confirm each slot; check frequency in a concordance; cross-check parsing against the morphology line of a named critical edition. Treat all recalled frequencies/lemmas as verify-required.

### Step 6 — Confidence + contested-reading note
State confidence on the candidate parse (low/moderate/high) and the one verification step that matters most. If the parse choice affects a contested interpretation, describe the competing readings and attribute them to streams — without ruling.

---

## Output Format

```
# Parsing/Morphology — [form] in [reference]

## Form
- Script / transliteration: [as supplied, else "not supplied"]
- Language / corpus: [Greek NT/LXX | Biblical Hebrew | Aramaic]
- Lemma: [supplied-by-user | not supplied — look up]
- Strong's #: [supplied-by-user | not supplied — look up]
- Reference & text used: [address] ([translation/original], supplied by user)

## Parsing slots for this part of speech (what each means)
- [slot]: [one-line explanation]
- [slot]: [one-line explanation]

## Candidate parse (VERIFY each slot in a tagged morphological tool)
| Slot | Candidate value | Confidence | Verify in |
|------|-----------------|-----------|-----------|
| [..] | candidate (verify) | low/mod/high | [tool] |

## Ambiguity / alternative parses
- Could also be: [alt parse] — disambiguated by [context/pointing/accents/critical text]

## Verification procedure
- [ ] Locate form in a tagged morphological database
- [ ] Confirm lemma
- [ ] Confirm each parsing slot
- [ ] Check frequency in a concordance (verify count)
- [ ] Cross-check parse against a named critical edition's morphology line

## Confidence & contested-reading note
- Candidate-parse confidence: low / moderate / high
- Most important verification step: [..]
- If parse affects interpretation: [Stream A reading] | [Stream B reading] — described, not adjudicated
```

---

## Verification

- [ ] No lemma, parse, root, Strong's number, or frequency asserted as fact unless user-supplied; all else labeled candidate/verify-required.
- [ ] No lexicon, grammar, or morphology reference quoted from memory.
- [ ] Each parsing slot explained, not just filled.
- [ ] Genuine morphological ambiguity surfaced rather than resolved by guess.
- [ ] A concrete verification procedure routes every datum to a named real tool.
- [ ] Candidate parse carries a confidence label and a named next verification step.
- [ ] Parse-dependent interpretive divergence (if any) described, not adjudicated.

---

## False-Positive Prevention

❌ **DON'T:**
- Output a clean, tagged-database-style parse that readers will trust as authoritative.
- Generate a plausible lemma, Strong's number, or frequency to fill a gap.
- Force a single parse onto a genuinely ambiguous form.
- Recall a frequency count or lemma and state it as fact.
- Let the parse that favors a doctrinal conclusion win without flagging the alternative.

✅ **DO:**
- Label every datum supplied-by-user / candidate (verify) / uncertain, and name where to confirm it.
- Leave gaps as gaps ("not supplied — look up") rather than inventing data.
- Explain each parsing slot so the user can evaluate, not just copy.
- Surface ambiguity and say what would disambiguate it.
- State a confidence level and the one verification step that matters most.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step procedure (Fix form → Name slots → Candidate parse → Ambiguity → Verification procedure → Confidence) imposes a disciplined sequence that prevents jumping from a recalled parse to a settled conclusion.
- **RT-05 (Evidence-Based Reasoning):** Every morphological datum is grounded in a named tool or flagged unverified; recalled lemmas, parses, Strong's numbers, and frequencies are treated as candidate data, never authoritative claims.
- **QA-04 (Uncertainty Acknowledgment):** Each slot is labeled supplied-by-user / candidate (verify) / uncertain; morphological ambiguity is surfaced explicitly; the candidate parse carries a low/moderate/high confidence rating with a named next step.
- **QA-05 (Citation Requirements):** Requires naming the tool type (tagged morphological database, reverse interlinear, critical-edition morphology line) that would confirm each slot, so the output is a verification roadmap rather than a finished parse.
- **OC-12 (External Reference Catalog):** The output format embeds a structured verification procedure cataloging the specific real tools needed to validate the lemma, each parsing slot, and the frequency.
