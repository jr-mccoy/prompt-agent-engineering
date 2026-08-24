---
title: "Steelman Construction — Build the Strongest Version of the Position You Disagree With"
category: reasoning-craft/reasoning-moves
description: "Construct the strongest defensible version of an opposing position before responding to it. Force the reasoner to articulate the position in language its proponents would accept, surface the strongest empirical and normative arguments for it, and only then identify the actual remaining disagreement. Counters strawmanning and motivated reasoning."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - steelman
  - argument-analysis
  - intellectual-empathy
  - disagreement
updated: "2026-05-10"
reasoning:
  styles: [dialectical, adversarial-empathy]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured_argument
  user_role: [analyst, writer, strategist, founder, executive, policy]
  mode: [audit, synthesize]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
  - domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md
---

# Steelman Construction

**Objective:** Build the strongest defensible version of a position the user disagrees with. Articulate the position in language its proponents would accept, surface the best empirical and normative arguments in its favor, name the conditions under which it would be correct, and only then identify what the user's actual remaining disagreement is. The deliverable is not "I now agree" — it is "I now know exactly what we disagree about."

**When to use:**
- The user is preparing to argue against a position publicly (op-ed, memo, debate, RFC response) and wants to avoid strawmanning.
- The user is making a high-stakes decision against a position held by smart people they respect, and wants to verify the disagreement is real.
- A team is polarized; surfacing the steelman of each side defuses motivated dismissal.
- The user keeps "winning" the argument in their head — a sign they're arguing against a weaker version than exists in the wild.

**When NOT to use:**
- The position is genuinely indefensible (factual hoax, fringe pseudoscience). Steelmanning a flat-earth claim wastes effort and can mislead by suggesting a serious version exists when it does not.
- The user already understands the strongest version and needs to act, not deliberate further.
- Time pressure is acute. Steelmanning is a slow, careful move.

**Audience:** Writers, strategists, executives, founders, policy analysts, anyone whose argument quality is bounded by their willingness to confront strong opposition.

---

## Inputs / Context

1. **The position the user disagrees with.** One sentence, in the user's words.
2. **The user's position.** One sentence, also in the user's words.
3. **What proponents of the opposing position actually believe.** As best as the user can articulate. (We will improve this in step 1.)
4. **The user's stake.** Why does this disagreement matter (decision, publication, relationship, policy)?
5. **The strongest opposing voices the user has encountered.** Names, articles, arguments — so the steelman is grounded in real interlocutors, not the user's caricature.

---

## Constraints

### Must
- Restate the opposing position in language a thoughtful proponent would accept and sign. If you cannot, the steelman has not been constructed yet.
- Surface at least three distinct arguments for the opposing position: one empirical, one normative/values-based, one structural/incentive-based. Each must be stated as if you believed it.
- Identify the conditions under which the opposing position would be correct — what would have to be true about the world.
- Name the strongest empirical evidence for the opposing position and the strongest empirical evidence against the user's position. (These are often different.)
- Distinguish between disagreements that are **empirical** (about facts), **definitional** (about what words mean), and **normative** (about what we should value).
- End with a one-sentence statement of the *remaining* disagreement after the steelman is constructed.

### Must Not
- Use scare quotes, hedges, or qualifiers ("they claim", "they would argue") that distance the steelman from the user. Write it as if you held the view.
- Build a steelman that no actual proponent would recognize — that is still strawmanning, just dressed up.
- End with "but they're still wrong because…" without first stating the remaining disagreement cleanly.
- Smuggle the user's view into the steelman by including its weaknesses ("a defender might argue X, but obviously…"). Write the cleanest version, then critique separately.
- Assume the disagreement is purely empirical when it is in fact about values. Most stuck disagreements are values masquerading as facts.

---

## Instructions

### Step 1 — Restate
Write the opposing position in one sentence using language a proponent would accept. Test by asking: would [named proponent] sign this? If no, revise.

### Step 2 — Three argument tracks
Build the strongest argument on each track:

- **Empirical:** "Here is what the data / evidence / track record actually shows that supports this position." Cite or paraphrase real evidence.
- **Normative:** "Here is what is at stake morally, ethically, or in terms of values. Even if the empirical case were weaker, this is why the position deserves weight." Avoid weak-form virtue claims; engage the actual values.
- **Structural / incentive-based:** "Here is the structural / institutional / second-order reason this position is defensible regardless of individual cases. Look at incentives, equilibria, what happens if everyone acts on the alternative."

Each argument is 2–4 sentences and stated in first person as if held.

### Step 3 — Conditions for correctness
Name 2–4 things that, if true about the world, would make the opposing position the right one. The more specific, the better. ("If interest rates stay above 5% for 24+ months", not "if economic conditions are bad enough".)

### Step 4 — Strongest evidence in both directions
- Strongest evidence *for* the opposing position: cite the most credible single piece of evidence proponents would point to.
- Strongest evidence *against* the user's position: this is sometimes the same evidence, sometimes different. Surface it explicitly.

### Step 5 — Disagreement classification
Diagnose the disagreement type:
- **Empirical:** disagreement about what is true. Resolvable in principle by evidence.
- **Definitional:** disagreement about what a word or category means. Resolvable by stipulation.
- **Normative:** disagreement about what should be valued or prioritized. Not resolvable by evidence alone; requires an argument about values.

Most stuck disagreements have all three layers. Name them in the order of load-bearing-ness.

### Step 6 — Remaining disagreement
After the steelman is built, write one sentence: "Even granting the strongest version of the opposing position, my remaining disagreement is [X]." If the user cannot complete this sentence, the disagreement may be weaker than they thought.

### Step 7 — Updated stance
- Did anything in the steelman update the user's position? If yes, what?
- If nothing updated, why not? (Possible answers: the steelman was already known and weighed; the empirical situation is too clear; the values gap is too wide; the steelman, while strong, doesn't address the load-bearing layer of your own position.) Each is a different kind of "no update."

---

## False-Positive Prevention

1. **Performative steelmanning.** Going through the motions while signaling that the opposing position is contemptible. Test: would a thoughtful proponent feel fairly represented?
2. **The composite proponent.** Building a steelman from the most extreme proponents and then attributing it to all who hold the position. Steelman the strongest version, then note that not all proponents hold that strongest version.
3. **Hidden weasels.** "A defender *might* argue", "*they would say*". Drop the distancing language. Write in first person.
4. **Empirical reduction.** Reducing a normative disagreement to an empirical one because empirical disagreements feel more tractable. Don't.
5. **Steelman-then-dismiss.** "I built the steelman, now let me show why it's wrong." That's fine — but the steelman section must stand on its own first, before the rebuttal section.
6. **Conditions impossibly specific.** "If consumer behavior fully reverses by Q3 2026 *and* regulation passes *and*…" — this is rhetoric, not analysis. Conditions should be plausible enough that a reasonable observer might believe them.
7. **Silent values-smuggling.** The normative argument should engage the proponents' actual values, not your own values applied to their position.

---

## Output Format

```
# Steelman of [position]

## Restated position
> [One sentence in language a proponent would sign.]

## Strongest arguments

### Empirical
[2–4 sentences, first person, with the strongest evidence.]

### Normative / values-based
[2–4 sentences, first person, engaging the actual values at stake.]

### Structural / incentive-based
[2–4 sentences, first person, on second-order or institutional reasons.]

## Conditions under which this position would be correct
1. [Specific, plausible condition]
2. [Specific, plausible condition]
3. [Optional]
4. [Optional]

## Evidence
- Strongest evidence *for* the opposing position: [citation / description]
- Strongest evidence *against* my position: [citation / description]

## Disagreement classification
- Empirical layer: [yes/no — what fact is contested?]
- Definitional layer: [yes/no — what term is contested?]
- Normative layer: [yes/no — what value is contested?]
- Load-bearing layer: [which of the above is doing most of the work in this disagreement]

## Remaining disagreement
> Even granting the strongest version of the opposing position, my remaining disagreement is [X].

## Update
- Did the steelman move my position? [yes / partially / no]
- If yes: [what specifically updated]
- If no: [which of the four reasons applies, and why]
```

---

## Verification

- [ ] Restated position is one a thoughtful proponent would sign.
- [ ] Three argument tracks (empirical, normative, structural) are present and stated in first person.
- [ ] Each argument cites real evidence or engages real values, not strawmanned versions.
- [ ] Conditions for correctness are specific and plausible.
- [ ] Strongest evidence for the opposing position and against the user's position are both surfaced.
- [ ] Disagreement is classified across empirical / definitional / normative layers.
- [ ] Remaining-disagreement sentence is concrete, not "they're just wrong."
- [ ] Update statement is honest — either named what moved, or named why nothing did.
- [ ] No distancing language ("they claim", scare quotes) inside the steelman section.
