---
title: "Translate Vague Requirements into Testable Specifications"
category: prompt-engineering/evaluation
description: "Take a requirement phrased as a quality adjective ('more professional,' 'cleaner,' 'better reasoning,' 'more rigorous') and translate it into observable, testable behaviors with pass/fail examples drawn from the user's real outputs. Returns a spec fragment that replaces the adjective with criteria a downstream prompt, rubric, or audit can enforce."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - correctness
  - requirements
  - specification
  - testability
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
---

# Translate Vague Requirements into Testable Specifications

**Objective:** Convert a requirement phrased as a quality adjective — "more professional," "more rigorous," "cleaner," "better reasoning," "more concise" — into a set of 2–5 observable behaviors with pass / fail rules and real-output examples. The artifact is a spec fragment a downstream prompt, rubric, or audit can enforce. Vague adjectives are not rewritten into slightly less vague adjectives; they are decomposed into tests.

**When to use:**
- A stakeholder or teammate asked for "better X" and the user has to turn that into a prompt edit, rubric change, or eval criterion.
- Two reviewers are using the same adjective to describe outputs they disagree about — the adjective is doing less work than either thinks.
- The user is about to edit a prompt to "improve" an output and wants to verify the improvement is testable before spending effort.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who have received, or issued, a vague quality requirement and need to translate it into a spec fragment. Not a substitute for `correctness_discovery_prompt.md` when no spec exists at all — use this to refine or extend an existing spec with a new requirement.

---

## Inputs Required

1. **The vague requirement.** In the requester's original words. If paraphrased, the adjective may already have drifted.
2. **Who issued the requirement.** The stakeholder, reviewer, or the user themselves. The translation may depend on what this person actually wants versus the generic dictionary meaning of the adjective.
3. **2–3 real past outputs the requester called satisfactory on this dimension.** With the input.
4. **2–3 real past outputs the requester called unsatisfactory on this dimension.** With the input and a one-sentence gloss on why.
5. **The consumer of the output.** Role + decision. Adjectives mean different things for different consumers ("professional" for a legal audit vs. "professional" for a product-marketing review).

**Refuse the translation if:**
- The vague requirement has no real satisfactory + unsatisfactory examples. Without evidence from both sides, the translation will encode the user's guess about the adjective's meaning rather than the requester's actual use of it.
- The requester and the consumer are different and the user cannot say which perspective the adjective is from. "More rigorous" from the stakeholder and "more rigorous" from the end consumer may point opposite directions.
- The adjective is already a spec criterion ("output must be under 200 words"). That's not a translation job; it's a rubric entry.

---

## Instructions

### Step 1 — Interview the adjective

Ask four questions of the evidence:

- **What's present in satisfactory outputs that's absent in unsatisfactory ones?** (Positive discriminators.)
- **What's present in unsatisfactory outputs that's absent in satisfactory ones?** (Negative discriminators.)
- **What's the same in both?** (Not a discriminator; don't build the spec on this.)
- **What varies within the satisfactory outputs?** (Tolerated variation; the spec should not over-constrain this.)

The discriminators are the candidate behaviors. The non-discriminators are noise the adjective doesn't care about.

### Step 2 — Name 2–5 candidate behaviors

From the discriminators, name candidate behaviors. Each behavior should be:

- **Observable.** A grader with the output in front of them can mark it present or absent without needing to ask the requester.
- **Specific.** "Uses precise language" is not specific. "Uses domain terms from the consumer's glossary in at least 80% of technical references" is.
- **Distinct.** Two behaviors should not both be paraphrases of the same underlying discriminator.

2 behaviors is usually enough for simple adjectives ("more concise"). 5 is the ceiling; more than that, the adjective is plural and the translation should split into multiple spec fragments.

### Step 3 — Write a pass rule and a fail rule per behavior

For each behavior, write:

- **Pass rule.** A sentence starting "Output passes if…" — specific enough that two graders would agree on 9 of 10 cases.
- **Fail rule.** A sentence starting "Output fails if…" — catches the negative discriminator.

Pass and fail rules are not just negations of each other. The gap between them is the gray band where the behavior neither passes nor fails — that gap is where the tradeoff policy lives (see `correctness_tradeoff_forcer.md`).

### Step 4 — Anchor each behavior to real examples

For each behavior, cite:

- **One satisfactory output where the behavior is present.** Point to the specific span or attribute that satisfies the pass rule.
- **One unsatisfactory output where the behavior is absent.** Point to the specific span or attribute that triggers the fail rule.

If no satisfactory output exhibits a candidate behavior, the behavior is inferred, not discovered — drop it or demote it to a nice-to-have.

### Step 5 — Check for adjective residue

Re-read the candidate behaviors. If any of them still contain the original adjective or its synonyms, the translation is incomplete. "Uses professional language" is the original adjective wearing a different hat. Replace it with the underlying discriminator.

A translated spec should be understandable to a grader who has never seen the original adjective.

### Step 6 — Test the translation against a new case

Pick a real output the requester has not yet judged. Apply the translated spec. Predict whether the requester would call it satisfactory. Check with the requester if accessible, or flag for check at the next opportunity.

If the spec's prediction diverges from the requester's judgment, the translation is missing a behavior or has a wrong rule. Iterate on Steps 2–5.

### Step 7 — Write the spec fragment

Final artifact: a block that can be pasted into an existing prompt, rubric, or audit. It contains the translated behaviors, their pass/fail rules, and a one-line pointer back to the original vague requirement (for traceability if the requester revisits).

The spec fragment replaces, not supplements, the adjective in the prompt. Leaving the adjective in place alongside the translated behaviors gives the model two conflicting instructions.

---

## Constraints

### Must
- Translate into 2–5 observable, distinct behaviors per adjective.
- Provide a pass rule and a fail rule per behavior.
- Anchor each behavior to a real satisfactory and a real unsatisfactory output.
- Test the translation against a case the requester has not yet judged.
- Replace the adjective in the prompt, don't supplement.

### Must Not
- Use the original adjective or its synonyms inside the translated behaviors.
- Produce rules a grader can't apply without re-asking the requester.
- Invent behaviors from best-practice lists not evidenced in the user's outputs.
- Over-constrain variation the requester tolerates in satisfactory outputs.
- Merge translations from multiple adjectives into one spec — each adjective gets its own fragment.

---

## False-Positive Prevention

1. **Synonym-swap translations.** "Be more professional" → "use professional language" is not a translation. If the behaviors still carry the adjective or its synonyms, the translation is cosmetic.
2. **Behaviors without evidence.** A behavior that no satisfactory output exhibits is an inference. The translation must be discovered from evidence, not predicted from the adjective.
3. **Graders who need the requester.** If applying a pass/fail rule requires knowing what the requester thinks, the rule isn't a rule — it's a proxy for the requester's taste.
4. **Over-constrained tolerated variation.** Satisfactory outputs may vary widely within the adjective's bounds. The spec must not forbid variation the requester tolerates, or it will reject outputs the requester would have accepted.
5. **Plural adjectives hidden in one word.** "Rigorous" often means (a) evidence is cited, (b) counter-arguments are named, (c) claims are calibrated. Translating it as one behavior collapses three. If the adjective is genuinely plural, split the translation.
6. **Adjective-and-translation co-existing.** Leaving "be more professional" in the prompt next to the translated behaviors gives the model two instructions. Replace the adjective.
7. **Requester drift.** The same requester can use "better" to mean different things in different contexts. Re-run the translation when the context shifts; don't treat one translation as permanent.
8. **Cross-consumer transfer.** A translation for one consumer does not transfer to another. Each new consumer gets a new evidence pool and potentially different behaviors.

---

## Output Format

```markdown
## Vague requirement
"[Original words]" — from [requester].

## Consumer
[Role + decision.]

## Evidence inventory
- Satisfactory outputs: [N, labels]
- Unsatisfactory outputs: [N, labels]

## Discriminators
- Present in satisfactory, absent in unsatisfactory: [...]
- Present in unsatisfactory, absent in satisfactory: [...]
- Shared (non-discriminators, noise): [...]
- Variation tolerated within satisfactory: [...]

## Translated behaviors (2–5)

### Behavior 1 — [short name]
- **Pass rule:** Output passes if [...]
- **Fail rule:** Output fails if [...]
- **Satisfactory example:** [output #, span]
- **Unsatisfactory example:** [output #, span]

### Behavior 2 — [...]
### ...

## Unseen-case test
- Unseen output: [label]
- Spec prediction: [pass / fail on each behavior]
- Requester's actual judgment: [pass / fail or pending]
- Divergence notes (if any): [...]

## Spec fragment (paste-ready)
```
[Behaviors as pass/fail rules, stripped of the original adjective, ready to drop into a prompt or rubric.]
```

## Traceability
- Replaces requirement: "[original adjective]"
- Issued by: [requester]
- Consumer: [role + decision]
- Date: [timestamp]
```

---

## Verification

- [ ] 2–5 behaviors translated, each with pass and fail rule.
- [ ] No behavior uses the original adjective or its synonyms.
- [ ] Each behavior cites a real satisfactory and a real unsatisfactory output.
- [ ] Rules are graderable without re-consulting the requester.
- [ ] The translation has been tested against at least one unseen case.
- [ ] The spec fragment replaces the adjective, not supplements it.
- [ ] Tolerated variation in satisfactory outputs is not over-constrained.
- [ ] The fragment is dated and traced to the original requirement.
