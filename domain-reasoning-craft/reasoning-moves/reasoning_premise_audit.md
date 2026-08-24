---
title: "Premise Audit — Surface and Test the Premises an Argument Rests On"
category: reasoning-craft/reasoning-moves
description: "Extract the explicit and implicit premises of an argument, classify each (factual / definitional / value / methodological), test each independently for support, identify which are load-bearing, and produce a one-line statement of the argument's actual fragility. Distinct from Toulmin map (structural) and from evidence-against-yourself (which targets conclusions, not premises)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - argument-analysis
  - premises
  - assumptions
  - critical-thinking
  - audit
updated: "2026-05-10"
reasoning:
  styles: [analytic, structural, dialectical]
  stakes: variable
  horizon: hours
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: premise_table_with_fragility_summary
  user_role: [analyst, writer, lawyer, researcher, executive, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md
  - domain-reasoning-craft/reasoning-moves/reasoning_claim_evidence_warrant_audit.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
---

# Premise Audit

**Objective:** Extract the premises of an argument (explicit and implicit), classify each, test each independently for support, identify which premises are load-bearing (their failure collapses the conclusion), and produce a one-line statement of the argument's actual fragility. Distinct from Toulmin mapping (which is full-structure) and from `epistemic_evidence_against_yourself.md` (which targets the conclusion); this prompt targets the premises specifically. Use this prompt when the suspect inputs are the starting claims themselves (factual / value / methodological premises), including arguments that cite no evidence at all; when the suspect link is the evidence→claim bridge in persuasive prose, use `reasoning_claim_evidence_warrant_audit.md`.

**When to use:**
- An argument's conclusion seems wrong but the structure looks valid → the premises are likely the issue.
- Auditing your own argument before publication.
- Preparing to challenge an argument: attacking premises is often more decisive than challenging the inferential structure.
- Teaching critical reading.
- Analyzing policy / strategic / scientific arguments where premises drive everything.

**When NOT to use:**
- Pure description (no argument).
- Mathematical proof (premises explicit).
- Cases where the argument's full Toulmin structure is needed (use the Toulmin prompt).

**Audience:** Analysts, writers, lawyers, researchers, executives.

---

## Inputs / Context

1. **The argument.** Passage, talk, paper section.
2. **What you're trying to do.** Audit / challenge / understand / accept-or-reject.
3. **The argument's conclusion** (what's being argued for).

---

## Constraints

### Must
- Extract **all premises** the conclusion depends on, including **implicit** ones (the ones the author didn't state but needed).
- Classify each premise: **factual** (empirical claim), **definitional** (about meaning of terms), **value** (about what should be valued), **methodological** (about what counts as evidence or what method is appropriate).
- Test each premise independently:
  - Is it true?
  - What evidence supports it?
  - What evidence challenges it?
- Identify **load-bearing** premises (failure collapses conclusion) vs **incidental** premises (failure leaves conclusion mostly intact).
- Produce a **one-line fragility statement**: "This argument rests on the truth of [load-bearing premise]; if that premise fails, the conclusion does not follow."

### Must Not
- Confuse premises with evidence. (Evidence is the *fact offered to support* a premise; the premise itself is the claim being supported, or the principle being invoked.)
- Confuse premises with the conclusion. (Conclusion is what the argument argues *for*; premises are what it argues *from*.)
- Skip implicit premises because they're not stated.
- Score premise truth based on whether you like the conclusion.
- Treat all premises as equally load-bearing.

---

## Instructions

### Step 1 — Identify the conclusion
What is the argument arguing for? One sentence.

### Step 2 — Extract premises (explicit and implicit)
List every premise the conclusion depends on. For implicit ones, write them out. Test: if you negated this premise, would the conclusion still follow?

### Step 3 — Classify each premise
| Premise | Type (factual / definitional / value / methodological) |
|---------|---------------------------------------------------------|
| [...] | factual |
| [...] | value |
| ... | ... |

### Step 4 — Test each premise
| Premise | Type | Support | Challenge | Verdict |
|---------|------|---------|-----------|---------|
| [...] | factual | [...] | [...] | [holds / contested / fails] |

### Step 5 — Identify load-bearing premises
For each premise: if false, would the conclusion collapse? Mark load-bearing or incidental.

### Step 6 — Fragility summary
One line: the argument rests on [load-bearing premise(s)]; the argument is [robust / fragile / broken] because [those premises are well-supported / contested / failed].

### Step 7 — Implications
- For audit: which premises need to be stated and defended explicitly?
- For challenge: which load-bearing premise is the most productive attack point?
- For accept-or-reject: do the load-bearing premises survive testing?

---

## False-Positive Prevention

1. **Premise-evidence confusion.** A study cited is evidence; the principle "this kind of study supports this kind of claim" is the premise.
2. **Premise-conclusion confusion.** The conclusion is what's being argued; premises are the inputs.
3. **Implicit-premise denial.** Most arguments rest on multiple implicit premises; surfacing them is the core value.
4. **Conclusion-tinted premise scoring.** Score premises by their evidential support, not by whether you like the conclusion.
5. **Equal-weight assumption.** Some premises do most of the work; identify them.
6. **Fragility-at-incidentals.** Don't declare an argument broken because an incidental premise fails.

---

## Output Format

```
# Premise audit — [argument source]

## Conclusion
> [What the argument argues for]

## Premises
| # | Premise | Type | Stated/implicit | Support | Challenge | Verdict | Load-bearing? |
|---|---------|------|-----------------|---------|-----------|---------|---------------|
| 1 | [...]   | factual | implicit | [...] | [...] | holds | yes |
| 2 | [...]   | value | stated | [...] | [...] | contested | yes |
| 3 | [...]   | methodological | implicit | [...] | [...] | fails | yes |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Load-bearing premises
- [#1]: [premise]
- [#2]: [...]
- ...

## Fragility summary
> This argument rests on [load-bearing premises]. The argument is [robust / fragile / broken] because [those premises are well-supported / contested / failed].

## Implications
- For audit: [premises needing explicit defense]
- For challenge: [most productive attack point]
- For accept-or-reject: [survives / fails / contested]
```

---

## Verification

- [ ] Conclusion stated separately.
- [ ] Premises extracted including implicit ones.
- [ ] Each premise classified (factual / definitional / value / methodological).
- [ ] Each premise tested for support and challenge.
- [ ] Load-bearing premises identified separately.
- [ ] Fragility summary explicit.
- [ ] Implications matched to user purpose.
- [ ] No premise-evidence or premise-conclusion confusion.
