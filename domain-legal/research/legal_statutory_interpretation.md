---
title: "Statutory Interpretation Analysis"
category: legal/research
description: "Apply standard statutory interpretation methodology — text, structure, canons, legislative history, agency construction, and constitutional avoidance — to a discrete interpretive question."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - research
  - statutory-interpretation
  - regulatory
  - canons-of-construction
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Walk a single statutory or regulatory text through a structured interpretive analysis to answer a specific applied question. Designed for matters where the dispute is "what does this provision mean as applied to these facts."

**When to use:** Tax, regulatory compliance, criminal-law mens rea questions, employment statutes, environmental rules, securities provisions, ERISA, immigration, any matter where the operative dispute is the meaning of a statutory or regulatory phrase.

---

## Your Input

- **Statutory or regulatory text (verbatim):** [Paste the operative provision, plus surrounding subsections if cross-references matter]
- **Citation:** [e.g., 18 U.S.C. § 1962(c); 17 C.F.R. § 240.10b-5; Cal. Lab. Code § 2802]
- **Jurisdiction:** [Federal circuit, state, or both]
- **Interpretive question:** [Concretely: "Does the term 'employee' in subsection (b) include a worker who…?"]
- **Facts to be applied:** [The fact pattern triggering the question]
- **Agency interpretation, if any:** [Final rule preamble, guidance, no-action letter, opinion letter — supply the text]
- **Legislative history, if relied on:** [Committee reports, floor statements, prior versions — supply the text]
- **Cases interpreting this provision the user has identified:** [Full citations + relevant text]
- **Interpretive philosophy preference:** [Textualist / purposivist / pragmatic / no preference — affects emphasis, not the analysis steps]

---

## Constraints

**Must:**
- Run the analysis in a fixed order: (1) text, (2) structure, (3) canons, (4) agency interpretation, (5) legislative history, (6) constitutional avoidance, (7) policy/purpose.
- For text: identify ordinary meaning, term-of-art meaning, and any statutory definition. Note any defined terms incorporated by cross-reference.
- For structure: examine surrounding subsections, the section's place in the chapter, and definitions sections.
- For canons: identify which substantive and linguistic canons plausibly apply (e.g., *expressio unius*, *ejusdem generis*, *noscitur a sociis*, rule of lenity, constitutional avoidance, federalism canons, anti-superfluity, whole-act, in pari materia). Note canons that cut against the proposed reading.
- For agency interpretation: identify the level of deference the controlling jurisdiction currently affords (the user supplies the controlling deference framework if it has shifted recently).
- Identify reasonable interpretations on both sides — at least two — and explain which is stronger and why.
- Conclude with a probability-tiered answer (likely / probably / could go either way / unlikely) with the operative reason.

**Must Not:**
- Treat ordinary meaning as dispositive without checking statutory definitions and cross-references.
- Cite cases or canons not in the user's authority list. Use `[NEED CITE: {kind of authority}]` placeholders for gaps.
- Confuse the deference framework's current state for what it was in older opinions; if the user has not specified the current deference standard, ask.
- Default to legislative history when the text is unambiguous in the controlling jurisdiction's textualism baseline.
- Apply the rule of lenity outside criminal or quasi-criminal contexts.
- Generate "the legislature intended" claims without grounding in supplied legislative-history text.

---

## Instructions

1. **Quote and parse the operative phrase.** Break it into its grammatical pieces. Identify modifiers and antecedents.
2. **Statutory definitions sweep.** Search the supplied text for definitions sections and incorporated definitions; note which terms in the operative phrase are defined.
3. **Structural reading.** Examine surrounding provisions: are the user's facts handled elsewhere? Does another subsection's phrasing suggest the operative phrase means something narrower or broader (whole-act canon, anti-superfluity)?
4. **Canon screen.** For each plausibly applicable canon, state the canon, why it applies, what it implies here, and any counter-canon that pulls the other direction.
5. **Agency interpretation.** If the user supplied agency text: summarize the agency's reading, locate the controlling deference rule, apply it.
6. **Legislative history (if applicable in the jurisdiction's interpretive method).** Use only supplied text. Distinguish committee reports (highest weight in most courts that consider history) from floor statements (lower weight).
7. **Constitutional avoidance.** If a reading raises a serious constitutional question, identify it and note whether avoidance applies.
8. **Synthesize.** State both readings, identify the stronger, give the operative reason, and assign a probability tier.
9. **Apply to the user's facts.** Walk the facts through the chosen reading and identify any fact-driven uncertainty.

---

## Output Format

```markdown
## Operative Provision

> {verbatim text}

**Citation:** {full citation}

## The Question

{One sentence.}

## Analysis

### 1. Text
- Operative phrase: "{phrase}"
- Grammatical structure: {subject, verb, modifiers, antecedents}
- Ordinary meaning: {...}
- Term-of-art meaning, if any: {...}
- Statutory definitions that apply: {... or "none in supplied text"}
- Cross-referenced terms: {...}

### 2. Structure
- Surrounding subsections: {...}
- Whole-act / anti-superfluity observations: {...}
- Definitions section interactions: {...}

### 3. Canons
| Canon | Why it applies | What it implies | Counter-canon |
|-------|----------------|-----------------|---------------|
| {e.g., ejusdem generis} | {...} | {...} | {...} |

### 4. Agency Interpretation
- Agency reading: {...}
- Controlling deference framework (as supplied): {...}
- Application: {...}

### 5. Legislative History (if relied on)
- Source and weight: {...}
- What it shows: {...}
- Limits: {...}

### 6. Constitutional Avoidance
- Constitutional question raised by reading X: {... or "none"}
- Application of avoidance canon: {...}

### 7. Purpose / Policy
- Stated purpose in the statute: {...}
- Reading consistent with purpose: {...}

## Two Reasonable Readings

**Reading A — {short label}.** {Statement of the reading, the strongest support, and which interpretive moves it relies on.}

**Reading B — {short label}.** {Same.}

## Stronger Reading

{Identify, with operative reason — usually the interpretive move that does the most work.}

## Probability Tier

{Likely / Probably / Could go either way / Unlikely} that {operative phrase} {means / does not mean} {X} as applied to the facts because {reason}.

## Application to Facts

{Fact-by-fact application of the chosen reading. Flag fact-driven uncertainties.}

## Open Items
- Authority needed: {...}
- Facts to develop: {...}
- Live deference question: {...}
```

---

## Verification

- [ ] Operative phrase quoted verbatim, not paraphrased.
- [ ] Statutory definitions checked before reaching for ordinary meaning.
- [ ] Each canon comes with a counter-canon or a statement that none cuts the other way.
- [ ] Agency interpretation analyzed under the controlling deference framework, not a stale one.
- [ ] Legislative history weighted by source and used only when interpretive method permits.
- [ ] Both reasonable readings stated; one identified as stronger with operative reason.
- [ ] Probability tier given.
- [ ] Application to facts identifies fact-driven uncertainty rather than burying it.
- [ ] No invented cases, agency guidance, or legislative history.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Plain meaning controls" without checking statutory definitions | Definitions section overrides ordinary meaning |
| Citing a canon as if it's dispositive | Canons are presumptions; identify the counter-canon |
| Treating committee reports and floor statements as equivalent | Reports carry more weight than individual statements in most jurisdictions that consider history |
| Defaulting to old deference doctrine | Use the current deference framework as supplied; flag if unstated |
| Conflating purpose with intent | Purpose is statutory; intent attribution to a multi-member legislature is contestable |
| Applying rule of lenity to civil statutes | Lenity is criminal/quasi-criminal only |
| Reading a single subsection in isolation | Whole-act canon and structure usually inform meaning |
| Ignoring the constitutional avoidance canon when a reading raises a real constitutional question | Identify the question; do not duck it |
| Saying "the legislature intended X" without supplied legislative-history text | Tie any intent claim to specific supplied text |
