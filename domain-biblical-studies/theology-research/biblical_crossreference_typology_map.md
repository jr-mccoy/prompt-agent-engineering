---
title: "Cross-Reference & Typology Mapper — Verified Links vs. Interpretive Typology"
category: biblical-studies/theology-research
description: "Map cross-references and typological connections for a passage or figure, sharply distinguishing explicit textual links (quotations the text itself makes) from probable allusions and from interpretive typology that traditions construct — referencing everything by address, refusing to fabricate references, and noting where a typological reading is contested."
techniques:
  - RT-02
  - RT-05
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - typology
  - cross-reference
  - intertextuality
  - anti-fabrication
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md
  - domain-biblical-studies/theology-research/biblical_theme_canonical_trajectory.md
  - domain-biblical-studies/theology-research/biblical_topical_theology_synthesis.md
---

# Cross-Reference & Typology Mapper

**Objective:** Build a map of how a passage or figure connects to the rest of Scripture — explicit textual links, probable allusions, and typological readings — keeping crisp the difference between what the text demonstrably connects and what an interpretive tradition constructs.

> **STRONG-GUARD prompt.** Fabricated cross-references and over-confident typology are major risks. Reference by address, mark verify-required, and distinguish explicit links from interpretive typology.

**When to use:**
- Tracing a type/antitype or a network of cross-references responsibly.
- You want to know which connections the text makes vs. which a tradition reads in.

**When NOT to use:**
- You want straightforward canonical/intertextual reading of one passage — use `biblical_canonical_intertextual_reading.md`.
- You want a theme's development across the canon — use `biblical_theme_canonical_trajectory.md`.

**Audience:** Pastors (P), seminary/academic (A).

---

## Inputs / Context

1. **The passage or figure.** Reference and text (user-supplied) or the figure/type of interest.
2. **Connections in hand (optional).** Links the user already has.
3. **Declared tradition (optional).** May foreground that tradition's typology; alternatives and contested status still noted.

---

## Constraints

### Must
- Classify each connection: **explicit textual link** (the text quotes/cites), **probable allusion**, or **interpretive typology** (a reading a tradition constructs).
- Reference every connection **by address** and mark verify-required (existence + wording + that it bears the claimed link).
- For typology, state whose reading it is (stream) and how widely accepted/contested it is; do not present it as the text's explicit claim.
- Note the interpretive payoff of strong links; caution against over-reading weak/typological ones.

### Must Not
- Invent references, quotations, or typological "patterns" not grounded in the text.
- Present interpretive typology as an explicit textual link.
- Assert a contested typology as the settled meaning.

### Tradition-neutral stance (Must / Must Not)
- **Must:** attribute typological readings to streams; note contested status.
- **Must Not:** present one tradition's typology as the established reading.

---

## Instructions

### Step 1 — Identify candidate connections
List candidates by address with the basis for each.

### Step 2 — Classify
Label each explicit link / probable allusion / interpretive typology; rate strength.

### Step 3 — Verify routing
Mark all verify-required; for quotations, flag wording/source-version for checking.

### Step 4 — Typology handling
For typological readings, attribute to streams and state acceptance/contested status; keep them separate from explicit links.

### Step 5 — Payoff & caution
State what strong links contribute; caution against building doctrine on weak or contested typology.

---

## Output Format

```
# Cross-Reference & Typology Map — [passage/figure]

## Connections
| Other text (address) | Type | Strength | Held by | Verify |
|----------------------|------|----------|---------|--------|
| [addr] | explicit/allusion/typology | strong/moderate/thin | [stream if typology] | yes |

## Typology notes (attributed, contested status)
- [type→antitype]: [stream]; acceptance: [broad/contested]

## Payoff & cautions
- Strong links contribute: [..] | Don't over-read: [..]
```

---

## Verification

- [ ] Each connection classified explicit / allusion / typology and strength-rated.
- [ ] Every reference by address and verify-required.
- [ ] Typology attributed to streams with contested status noted.
- [ ] Interpretive typology kept distinct from explicit links.
- [ ] No invented references or patterns; no contested typology asserted as settled.

---

## False-Positive Prevention

❌ **DON'T:**
- Generate a web of cross-references from memory as established.
- Present a tradition's typology as something the text explicitly states.
- Build doctrine on a single contested type.

✅ **DO:**
- Classify explicit link > allusion > interpretive typology, by address, verify-required.
- Attribute typology to streams and flag contested status.
- Reserve interpretive weight for demonstrable links.
