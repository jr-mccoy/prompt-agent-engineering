---
title: "Original-Language Word Study (Greek / Hebrew / Aramaic) — Structured, Anti-Fabrication"
category: biblical-studies/exegesis-interpretation
description: "Structure a rigorous word study on a Greek, Hebrew, or Aramaic term while refusing to invent lexical data. Presents candidate glosses and semantic range as verify-required, routes the user to named real lexicons and interlinears, labels every claim by confidence, and guards against the etymological and illegitimate-totality-transfer fallacies."
techniques:
  - ST-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - word-study
  - greek
  - hebrew
  - lexicon
  - anti-fabrication
  - exegesis
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
---

# Original-Language Word Study (Greek / Hebrew / Aramaic)

**Objective:** Produce a disciplined word study on a single original-language term as it functions in a specific passage — its candidate glosses, semantic range, usage pattern, and contribution to meaning — **without inventing any lexical data.** The output is a structured study scaffold the user completes and verifies against real reference works, not an authoritative lexicon entry.

> **STRONG-GUARD prompt.** This is the highest-fabrication-risk prompt in the domain. Language models routinely invent roots, etymologies, glosses, semantic ranges, Strong's numbers, parsing, and frequency counts that sound authoritative and are wrong. This prompt treats all such data as **verify-required** and never presents it as settled.

**When to use:**
- Studying how a key term functions in a specific verse or passage.
- Checking whether a popular claim about a word's "real meaning" holds up.
- Preparing the lexical layer of an exegesis, sermon, or paper.

**When NOT to use:**
- You need an authoritative lexicon entry — go to BDAG, HALOT, LSJ, DCH, TDNT, or NIDNTTE directly. This prompt scaffolds and cross-examines; it does not replace them.
- You have no way to verify against a real lexicon/interlinear. Without verification this study is unreliable; say so and stop.

**Audience:** Seminary/academic (A), pastors (P), and equipped group leaders (G) who can access real reference works.

---

## Inputs / Context

1. **The term.** The word as the user has it (transliteration, lemma, and/or the script form), with the verse reference where it occurs.
2. **The passage text.** The user should paste the verse(s) in a named translation; the model references by address and does not quote from memory.
3. **Known reference data (optional).** Any lexicon glosses, Strong's number, or parsing the user already has — supplied so the model can organize, not invent, it.
4. **Declared tradition (optional).** If supplied, the model may note resources/terminology familiar to that tradition, but still labels lexical data as verify-required and notes alternatives.
5. **Purpose.** Exegesis paper / sermon prep / claim-checking — sets depth.

---

## Constraints

### Must
- Treat every lexical datum (gloss, semantic range, root, etymology, Strong's number, parsing, frequency) as **candidate / verify-required** unless the user supplied it. Mark each with a confidence label: **supplied-by-user**, **commonly-reported (verify)**, or **uncertain**.
- For any gloss or semantic claim, name the *kind* of resource that would confirm it (e.g., "confirm in BDAG/HALOT," "check a concordance for usage," "parse with a real interlinear") — and instruct the user to verify there.
- Distinguish **meaning in this context** from the word's **broader semantic range**. Context, not the full range, determines the sense here.
- Apply the discipline of usage: how the *same author / same corpus* uses the word matters more than gloss lists.
- State confidence on the final "sense in this passage" judgment (low / moderate / high) and what would raise it.

### Must Not
- Invent or assert any root, etymology, gloss, semantic range, Strong's number, parsing, or frequency count from memory as if authoritative.
- Quote a lexicon, TDNT/NIDNTTE article, or any reference work verbatim from memory.
- Commit the **etymological fallacy** (deriving present meaning from word origin/roots) or **illegitimate totality transfer** (importing the word's whole range into one occurrence).
- Privilege a tradition's preferred gloss as the "true" meaning, or use the word study to smuggle in a contested doctrinal conclusion.
- Misquote the passage; reference by address and use the user's supplied translation text.

---

## Instructions

### Step 1 — Fix the term and its location
Restate the lemma/transliteration and the exact reference. If the user supplied a Strong's number or parsing, echo it as **supplied-by-user**. If not, do **not** generate one; mark "Strong's number: not supplied — look up in a concordance."

### Step 2 — Candidate glosses (verify-required)
List the glosses you would *expect* to see, each labeled **commonly-reported (verify)** or **uncertain**. Immediately instruct: "Confirm these against [BDAG / HALOT / LSJ / DCH] before relying on them." Never present the list as definitive.

### Step 3 — Semantic range vs. contextual sense
- Sketch the plausible semantic range (verify-required).
- Then narrow: given the genre, syntax, and argument of *this* passage, which part of the range is in play? This contextual narrowing is the heart of the study.

### Step 4 — Usage evidence
Identify how to check usage: same author, same book, same Testament/corpus, LXX (for Hebrew→Greek), etc. If you can name *candidate* parallel passages, mark them **verify the reference and wording**. Tell the user to run a concordance/morphology search rather than trusting recalled lists.

### Step 5 — Test popular claims
If the user (or common teaching) attaches a special meaning to the word ("this Greek word *really* means…"), test it against Steps 3–4 and the two fallacies above. State whether the claim is supportable, overstated, or a fallacy — flagging that the verdict itself needs verification.

### Step 6 — Sense in this passage + confidence
State the best-supported sense in context, with a confidence label and the single most important verification step that would change or confirm it.

### Step 7 — Tradition note (only if relevant)
If interpretive traditions read the word differently (e.g., a term with disputed theological weight), describe the differing readings descriptively and attribute them to streams — without ruling.

---

## Output Format

```
# Word Study — [transliteration / lemma] in [reference]

## Term
- Lemma / transliteration: [..]
- Script form: [as supplied, else "not supplied"]
- Strong's #: [supplied-by-user | not supplied — look up]
- Parsing: [supplied-by-user | not supplied — parse with a real interlinear]
- Reference & translation used: [address] ([translation], text supplied by user)

## Candidate glosses (VERIFY against BDAG/HALOT/LSJ/DCH)
| Gloss | Confidence | Verify in |
|-------|-----------|-----------|
| [..]  | commonly-reported (verify) | [resource] |

## Semantic range vs. contextual sense
- Plausible range (verify-required): [..]
- Narrowing factors in this passage (genre/syntax/argument): [..]
- Sense in play here: [..]

## Usage evidence (run a real concordance/morphology search)
- Where to check: [author/book/corpus/LXX]
- Candidate parallels (verify reference + wording): [..]

## Popular-claim check
- Claim: [..]  → Verdict: supportable / overstated / fallacy ([etymological | totality-transfer]) (verify)

## Sense in this passage
- Best-supported sense: [..]
- Confidence: low / moderate / high
- Most important verification step: [..]

## Tradition note (if applicable)
- [Stream A] reads it as [..]; [Stream B] as [..] — described, not adjudicated.

## Verification required before use
- [ ] Glosses confirmed in a named lexicon
- [ ] Parsing/Strong's confirmed in a real tool
- [ ] Parallel references checked for existence and wording
```

---

## Verification

- [ ] No gloss, root, etymology, Strong's number, parsing, or frequency asserted as fact unless user-supplied; all else labeled verify-required.
- [ ] No lexicon/TDNT/NIDNTTE text quoted from memory.
- [ ] Contextual sense distinguished from full semantic range.
- [ ] Etymological fallacy and illegitimate totality transfer checked.
- [ ] Passage referenced by address; user's translation used, not a recalled quote.
- [ ] Final sense carries a confidence label and a named next verification step.
- [ ] Tradition differences (if any) described, not adjudicated.

---

## False-Positive Prevention

❌ **DON'T:**
- Output a confident gloss list that looks like a lexicon entry — readers will trust it as authoritative.
- Generate a plausible Strong's number, parsing, or frequency count to fill a gap.
- Argue "the Greek/Hebrew *literally* means X, therefore the verse means X" (etymological fallacy).
- Pour the word's entire semantic range into a single occurrence (illegitimate totality transfer).
- Recall "parallel verses" and present them without flagging that references and wording must be checked.

✅ **DO:**
- Label every lexical datum supplied-by-user / commonly-reported (verify) / uncertain, and name where to confirm it.
- Leave gaps as gaps ("not supplied — look up") rather than inventing data.
- Let context, syntax, and same-corpus usage drive the contextual sense.
- State a confidence level and the one verification step that matters most.
- Describe tradition-specific readings without ruling between them.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 7-step workflow (Fix term → Candidate glosses → Semantic range vs. sense → Usage evidence → Test popular claims → Confidence judgment → Tradition note) imposes a disciplined sequence that prevents jumping from a gloss list to a doctrinal conclusion.
- **RT-05 (Evidence-Based Reasoning):** Every lexical datum is grounded in a named source or flagged unverified; recalled glosses, Strong's numbers, and etymologies are treated as candidate data rather than authoritative claims.
- **QA-04 (Uncertainty Acknowledgment):** Every gloss and semantic claim is labeled supplied-by-user / commonly-reported (verify) / uncertain; the final sense in context carries a low/moderate/high confidence rating with a named next verification step.
- **QA-05 (Citation Requirements):** Requires naming the resource type (BDAG, HALOT, LSJ, DCH) that would confirm each claim, so the output is a verification roadmap rather than a finished reference.
- **OC-12 (External Reference Catalog):** The output format embeds a structured Verification Required block listing specific lexicons, tools, and search types needed to validate each layer of the study.
