---
title: "Disagreement Diagnosis — Empirical, Definitional, or Normative?"
category: reasoning-craft/epistemic
description: "Take a stuck disagreement between two parties (or two positions in your own head) and diagnose its layers: empirical (about facts), definitional (about what words mean), normative (about what should be valued), and reference-class (about which comparable cases should anchor judgment). Most stuck disagreements have multiple layers; surfacing them ends false-deadlocks."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - disagreement
  - diagnosis
  - definitional
  - normative
updated: "2026-05-10"
reasoning:
  styles: [dialectical, structural, taxonomic]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: pair_or_team
  output_format: layered_diagnosis
  user_role: [analyst, executive, founder, policy, mediator, individual]
  mode: [diagnose, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
---

# Disagreement Diagnosis

**Objective:** Take a stuck disagreement and diagnose its layers. Most disagreements that feel intractable are stuck because the parties are arguing across layers without realizing it: one is making an empirical claim, the other a normative claim. Surfacing the layers does not necessarily resolve the disagreement, but it does end *false* deadlocks (where the parties would actually agree if they were arguing on the same layer) and clarifies what kind of evidence or argument could plausibly close the remaining gap.

The four layers:
- **Empirical** — disagreement about what is true in the world. Resolvable in principle by evidence.
- **Definitional** — disagreement about what a word, category, or concept means. Resolvable by stipulating a definition.
- **Normative** — disagreement about what should be valued, prioritized, or done. Not resolvable by evidence alone; requires a values argument.
- **Reference-class** — disagreement about which comparable cases should anchor judgment. Resolvable by negotiating the inclusion criteria.

**When to use:**
- Two parties (or two views you hold) keep talking past each other.
- A team meeting keeps re-litigating the same conflict without progress.
- A public debate seems to have parties shouting at each other from different premises.
- A personal argument with a partner / colleague / family member that re-surfaces in different forms.
- Drafting a position paper that needs to address opposing views and you want to know where the actual disagreement lives.

**When NOT to use:**
- One party's bad faith is clearly established and severe (e.g., openly using "definition disputes" purely as a stalling tactic) — at that point diagnosis is pointless. Partial or merely suspected bad faith stays in scope: run the diagnosis and surface the risk.
- The disagreement is genuinely about preferences with no shared decision context. Some preferences just differ.
- Time pressure is severe.

**Audience:** Mediators, team leads, executives, policy people, anyone in a stuck argument worth understanding rather than just winning.

---

## Inputs / Context

1. **The disagreement.** State it as a question or as the two competing claims.
2. **The two parties.** Their actual positions in their own words (best effort). Internal disagreements: name the two voices.
3. **What's already been tried.** What evidence has been exchanged, what arguments made.
4. **The decision context.** Is this disagreement attached to a decision that needs to be made? If yes, what decision and by when?
5. **Each party's stake.** What does each lose if they're wrong, and what does each lose if they concede?

---

## Constraints

### Must
- Diagnose all four layers, even if some return "no disagreement here." The mapping itself is informative.
- Quote or paraphrase actual claims from both parties when assessing each layer. Don't generalize ("Party A thinks X is good, Party B thinks X is bad" — that's not a diagnosis, that's a restatement).
- Identify which layer is **load-bearing** — the one whose resolution would actually close the disagreement.
- Distinguish between layers where the parties disagree and layers where they agree but don't realize it.
- For empirical layers, name what evidence would settle it. For definitional, propose a stipulation. For normative, name the values in tension. For reference-class, name the criteria for inclusion both parties would accept.
- End with a concrete next step matched to the load-bearing layer.

### Must Not
- Reduce a normative disagreement to an empirical one because empirical disagreements feel more tractable.
- Treat a definitional disagreement as substantive when it's actually just a word choice.
- Pretend a values disagreement can be "resolved by data." Sometimes the disagreement is about values, and the next step is values negotiation, not more research.
- Take sides during the diagnosis. The diagnosis is descriptive; advocacy comes later if at all.
- Dismiss any layer's disagreement as "not the real issue" without examining it.

---

## Instructions

### Step 1 — Restate
Write the disagreement as a question or as two competing claims. Try to use language both parties would accept.

### Step 2 — Restate each party's view
In their own words (best effort), 2–4 sentences each. Both should be recognizable to the party who holds the view.

### Step 3 — Empirical layer audit
Identify any factual claims either party makes. For each:
- Do the parties actually disagree about the fact?
- What evidence could settle it?
- Is the evidence available, expensive, or impossible to obtain?

If parties agree on facts, mark this layer "no disagreement" and move on.

### Step 4 — Definitional layer audit
Identify the key terms each party uses. For each:
- Are they using the same word for different concepts?
- Are they using different words for the same concept?
- If a definition were stipulated, would the disagreement shrink or disappear?

Common definitional traps: "fairness", "good", "scalable", "successful", "harm", "responsible", "freedom", "necessary."

### Step 5 — Normative layer audit
Identify the values, priorities, or principles each party brings. For each:
- What do they prioritize that the other party deprioritizes?
- Is the priority disagreement absolute (one party doesn't value the other's priority at all) or relative (both value both, but weight them differently)?
- Are the underlying values articulated, or smuggled inside empirical claims?

### Step 6 — Reference-class layer audit
Identify which past cases or analogies each party draws on. For each:
- Are they reasoning from different reference classes?
- If they used the same reference class, would they reach similar conclusions?
- What would the inclusion criteria for a shared reference class be?

### Step 7 — Load-bearing layer
Identify which layer, if resolved, would actually end the disagreement. Often it's the layer the parties have spent the *least* time on. Weigh each party's stake (Input 5): what a party loses by being wrong or by conceding predicts how sticky each layer will be, and informs the bad-faith-risk note in the output.

### Step 8 — Hidden agreements
Identify any layer where the parties agree but don't realize it. Surfacing hidden agreements often defuses heat by establishing what's actually shared.

### Step 9 — Resolution path
Matched to the load-bearing layer:
- **Empirical:** specify the evidence to seek.
- **Definitional:** propose a stipulation both parties could accept (or note that they cannot).
- **Normative:** acknowledge the values gap and ask whether a decision rule (vote, defer, escalate, parallel paths) can be agreed.
- **Reference-class:** propose inclusion criteria; if both parties accept, redo the analysis on the agreed class.

### Step 10 — Next step
- A concrete action matched to the resolution path
- Who does it
- By when
- What signal of progress would look like

---

## False-Positive Prevention

1. **Empirical reduction of values.** "Once the data is in, we'll know who's right." Often false. If the disagreement is normative, more data won't resolve it; it will just give each side new ammunition.
2. **Word-game dismissal.** "It's just a definitional dispute" used to dismiss a substantive disagreement. Definitional disputes are sometimes substantive (the choice of definition determines what gets measured, valued, regulated).
3. **One-layer tunneling.** Diagnosing only the layer the user prefers (often empirical, because it feels tractable) and ignoring the layer that's actually load-bearing.
4. **Hidden agreement blindness.** Missing layers where the parties agree. Surfacing agreement is half the value of the diagnosis.
5. **Diagnosis-as-advocacy.** Using the diagnosis to side with one party. The diagnosis is descriptive.
6. **False solvability claim.** Marking a normative disagreement as "resolvable" because there's a procedure. The procedure resolves the *decision*, not the disagreement.
7. **Bad-faith ignored.** If one party is using definitional moves as a stalling tactic, the diagnosis applies but the resolution is different (escalate, change the table, accept the disagreement won't resolve). Surface bad faith if it's likely.
8. **Both-sides-ism.** Forced symmetry when one party is empirically wrong. Symmetry is for layers; on a layer, sometimes one side is correct.

---

## Output Format

```
# Disagreement diagnosis — [topic]

## The disagreement
[As a question or as two competing claims, in language both parties would accept]

## Party positions (in their own words)
- **Party A:** [2–4 sentences]
- **Party B:** [2–4 sentences]

## Layer-by-layer

### Empirical
- Disagreement present? [yes / no / partial]
- Specific factual claims in dispute: [list]
- Evidence that would settle it: [specific]
- Evidence currently available? [yes / no / costly]

### Definitional
- Disagreement present? [yes / no / partial]
- Key terms used differently: [list]
- Proposed stipulations: [if any]
- If stipulated, would disagreement shrink? [yes / no / partially]

### Normative
- Disagreement present? [yes / no / partial]
- Values in tension: [list]
- Type: [absolute / relative / smuggled inside empirical claims]
- Articulated by either party? [yes / no / one-sided]

### Reference-class
- Disagreement present? [yes / no / partial]
- Reference class used by Party A: [...]
- Reference class used by Party B: [...]
- Shared inclusion criteria possible? [yes / no]

## Load-bearing layer
- Layer: [empirical / definitional / normative / reference-class]
- Why: [the layer whose resolution would actually close the disagreement]

## Hidden agreements
- [Where do A and B actually agree, possibly without realizing it]

## Resolution path
- Matched to load-bearing layer: [path]
- Concrete next step: [action]
- Owner: [name]
- Deadline: [date]
- Progress signal: [observable]

## Notes
- Bad-faith risk: [low / moderate / high]
- If disagreement is genuinely irreducible (e.g., values gap with no shared decision rule), what does each party do? [proceed in parallel / one defers / escalation / accept]
```

---

## Verification

- [ ] All four layers diagnosed (with "no disagreement" allowed).
- [ ] Each party's view restated in their own words and recognizable to them.
- [ ] Empirical-evidence pointer is specific.
- [ ] Definitional stipulations are proposed (or impossibility noted).
- [ ] Normative values are named, not smuggled.
- [ ] Reference-class criteria proposed if relevant.
- [ ] Load-bearing layer identified and named.
- [ ] Hidden agreements (if any) surfaced.
- [ ] Resolution path matches the load-bearing layer.
- [ ] No empirical reduction of normative disagreements.
- [ ] No diagnosis-as-advocacy.
