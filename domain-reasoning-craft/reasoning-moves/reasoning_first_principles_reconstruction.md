---
title: "First-Principles Reconstruction — Tear a Belief Down to Atoms and Rebuild"
category: reasoning-craft/reasoning-moves
description: "Take a working belief or design, decompose it into the smallest claims that the rest depends on, audit each atomic claim independently for evidence and necessity, then rebuild the structure from the surviving atoms. Surfaces inherited assumptions that survived only by being repeated, not by being earned."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - reasoning
  - first-principles
  - decomposition
  - assumption-audit
  - rebuild
updated: "2026-05-10"
reasoning:
  styles: [reductive, deductive, constructive]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: atomic_claims_then_reconstruction
  user_role: [founder, engineer, strategist, scientist, designer, analyst]
  mode: [audit, synthesize]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md
  - domain-reasoning-craft/reasoning-moves/reasoning_inversion.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
---

# First-Principles Reconstruction

**Objective:** Take a working belief, design, plan, or process — and tear it down to the smallest atomic claims it rests on. Audit each claim independently: is it true, is it necessary, and what is the evidence for it? Then rebuild the structure using only the surviving atoms. The diagnostic value is identifying inherited assumptions that survived because nobody questioned them, not because they were earned.

**When to use:**
- A practice or belief is doing real work in a system, but its origin is "this is how it's done."
- A design is over-complicated and you suspect components are vestigial.
- You're entering a domain whose conventional wisdom looks like consensus but might be inheritance.
- A founder/strategist is deciding whether to copy or rebuild a category.
- A scientist or engineer is reviewing a method whose assumptions have not been recently re-audited.

**When NOT to use:**
- The belief in question is well-evidenced and recently re-validated. First-principles is expensive; spend it where there's reason to suspect rot.
- The system is so complex that atomic decomposition would take longer than the decision warrants.
- Speed matters more than correctness (early prototype, throwaway code, low-stakes choice).
- You're using "first principles" as rhetoric to discard a well-supported view because it's inconvenient.

**Audience:** Founders, engineers, scientists, designers, strategists, analysts — anyone whose work depends on assumptions they didn't personally validate.

---

## Inputs / Context

1. **The belief, design, or practice under examination.** State it as a single claim or a brief description of the system.
2. **The domain.** What field's conventions apply (engineering, biology, finance, product design)?
3. **Why now.** What triggered the audit — failure, a new constraint, a competitive move, a personal doubt?
4. **Stakes of being wrong.** Low / medium / high. High-stakes audits warrant deeper atom-level investigation.
5. **What you'd accept as evidence per atom.** Empirical, theoretical, expert consensus, internal data. Mismatch between expected and available evidence is itself a finding.

---

## Constraints

### Must
- Decompose to atoms — claims that themselves cannot be reduced further within the domain. If an atom decomposes further, it isn't an atom.
- For each atom, evaluate three properties: **truth** (is the claim correct?), **necessity** (is the claim required for the larger structure to hold?), and **evidence** (what supports it?).
- Mark each atom with a status: **load-bearing & supported**, **load-bearing & unsupported**, **redundant**, or **false / outdated**.
- Rebuild from atoms that survived. The reconstruction may differ from the original; document the differences.
- Distinguish between atoms that are *physically necessary* (can't be otherwise without violating physics, math, or hard constraints) and *contingently necessary* (only necessary because of a choice made earlier in the chain). Contingent necessity is where most opportunities for redesign live.

### Must Not
- Confuse decomposition with skepticism. The goal is rebuild, not destroy.
- Use first-principles as a license to ignore evidence ("just because everyone says X doesn't mean…"). Some inherited beliefs are inherited because they're correct; the audit should find that.
- Stop at one level of decomposition. "We use TLS because it's secure" is not an atom; "TLS provides confidentiality / integrity / authentication via [specific mechanisms]" is closer.
- Assume atoms are independent when they have shared dependencies. Map the dependencies before evaluating individually.
- Reconstruct without comparing to the original. The diff is part of the deliverable.

---

## Instructions

### Step 1 — Restate the structure
Write the belief / design / practice in one paragraph. Include what it does, what it rests on, and what would happen if it were absent.

### Step 2 — Decompose to atoms
List the atomic claims the structure depends on. Aim for 5–15. Each should be:
- A single declarative sentence
- Specific enough to be evaluated independently
- Not further reducible within the domain

If an "atom" is a compound claim ("X because Y and Z"), split it.

### Step 3 — Map dependencies
Briefly note which atoms depend on other atoms. A dependency graph isn't always necessary, but knowing which atoms are upstream of others matters for rebuild.

### Step 4 — Evaluate each atom
For each atom, assess:
- **Truth:** Is it correct? Evidence: [what supports it; if nothing, mark `[no evidence found]`].
- **Necessity:** If this atom were false / removed, would the larger structure fail? (Yes / partial / no.)
- **Type of necessity:** physically / mathematically necessary, OR contingently necessary (because of a prior design choice).
- **Status:** load-bearing & supported / load-bearing & unsupported / redundant / false / outdated.

### Step 5 — Surface the inherited atoms
Atoms whose only evidence is "this is how it's done" or "everyone does it this way" are inherited. Inherited is not the same as wrong, but it is the same as un-audited. List inherited atoms separately.

### Step 6 — Reconstruct
Using only the atoms that survived (load-bearing & supported, plus any atoms whose support you can find or generate), rebuild the structure. The reconstruction:
- May be smaller than the original (if redundant atoms existed).
- May be different in shape (if contingent necessity opened alternative paths).
- May be the same (if every atom was earned).

### Step 7 — Diff
Write the differences between original and reconstruction. For each difference:
- What changed
- Why (which atom failed, was redundant, or was contingently replaceable)
- What the change costs / unlocks

### Step 8 — Action
- If the reconstruction is identical: the structure was earned. Trust it more.
- If the reconstruction is smaller: identify what to drop and the smallest reversible test that would confirm it can be dropped safely.
- If the reconstruction is differently shaped: design a transition path or a parallel-track experiment.
- If the reconstruction is meaningfully larger: the original was missing necessary atoms; you've found a gap.

---

## False-Positive Prevention

1. **Pseudo-decomposition.** Decomposing into bullet points without actually atomizing. Test: each atom should be evaluable on its own without referring to others.
2. **First-principles as rhetoric.** Using the move to dismiss what you don't want to be true. The audit must be willing to find that inherited atoms were inherited *because they're correct*.
3. **Skipping evidence step.** Marking an atom "true" because it feels true. If no evidence is available, mark `[no evidence found]` and treat as load-bearing-and-unsupported.
4. **Over-reduction.** Decomposing past the point where atoms are operationally meaningful. Stop when further decomposition no longer changes the rebuild.
5. **Independence assumption.** Treating atoms as independent when they share dependencies. The dependency map prevents this.
6. **Reconstruction without diff.** Producing a rebuild that looks identical to the original without explaining why every atom survived. The diff is the diagnostic.
7. **Domain-naïve atomization.** Decomposing outside your domain expertise can produce atoms that look reasonable but miss what experts know. If atomizing in an unfamiliar domain, mark atoms `[low confidence in atomicity]`.
8. **Survivorship bias in evidence.** "It's been working for years" is evidence of survival, not always evidence of correctness. Distinguish "no harm has been observed" from "the mechanism is sound."

---

## Output Format

```
# First-principles reconstruction — [structure]

## Original structure
[One-paragraph statement of the belief / design / practice]

## Atomic claims
| # | Claim                       | Depends on | Evidence                  | Necessity (Y/P/N) | Necessity type | Status                   |
|---|-----------------------------|------------|---------------------------|-------------------|----------------|--------------------------|
| 1 | [atom]                      | —          | [evidence]                | Y                 | physical       | load-bearing & supported |
| 2 | [atom]                      | 1          | [evidence or `[none]`]    | Y                 | contingent     | load-bearing & unsupported |
| 3 | [atom]                      | 1, 2       | [evidence]                | N                 | —              | redundant                |
| … |                             |            |                           |                   |                |                          |

## Inherited atoms (un-audited)
- [List atoms whose only support is convention / inheritance]

## Reconstruction
[Rebuild the structure using surviving + earned atoms]

## Diff
| Original element | Status in reconstruction | Why                          | Cost / unlock |
|------------------|--------------------------|------------------------------|---------------|
| [element]        | dropped                  | atom #3 was redundant        | [savings]     |
| [element]        | replaced                 | atom #2 contingently necessary; alternative now in place | [tradeoff] |
| [element]        | preserved                | all atoms earned             | —             |

## Verdict
- Reconstruction is [identical / smaller / differently shaped / larger]
- Confidence: [low / moderate / high]
- Recommended action: [trust / drop element X with test Y / transition to new shape / fill gap with atom Z]
```

---

## Verification

- [ ] Atoms are individual declarative sentences, not compound.
- [ ] Each atom has truth, necessity, evidence, and status.
- [ ] Necessity is typed (physical vs contingent).
- [ ] Inherited atoms are surfaced separately.
- [ ] Dependency relations between atoms are recorded.
- [ ] Reconstruction is built only from surviving atoms.
- [ ] Diff between original and reconstruction is documented and explained.
- [ ] Verdict and action are matched to the diff.
- [ ] No atom marked "true" without evidence noted (or `[no evidence found]`).
- [ ] First-principles framing not used to ignore well-supported inherited claims.
