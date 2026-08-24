---
title: "Map Performed-Role Versus Acting-From-Self, and Close One Gap"
category: personal-development/identity
description: "Across the user's real contexts, classify each as aligned self, chosen adaptation, or costly performance; score the cost of each performance; distinguish healthy code-switching from identity-eroding suppression; and produce one bounded, safe move to close the single most expensive gap."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - identity
  - authenticity
  - performance
  - code-switching
  - self-alignment
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
  - domain-personal-development/prompts/identity/identity_life_audit_reckoning.md
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/resilience/resilience_self_discipline_system.md
---

# Map Performed-Role Versus Acting-From-Self, and Close One Gap

**Objective:** Map where the user is performing a role versus acting from self across their real contexts, separate legitimate adaptation from costly performance, score what each performance costs, and produce one bounded, safe move to close the single most expensive gap.

**When to use:** The user feels they're "wearing a mask" in some part of life; is drained by keeping up an act; or suspects the version of themselves at work / online / with family isn't the real one. Not for auditing whether someone else is authentic, and not a mandate to be radically transparent everywhere.

**Audience:** An individual examining their own contexts. Not clinical. If the sense of having "no real self" is persistent and distressing, or tied to depersonalization, that points past this prompt — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Arena list.** 6–10 specific contexts the user moves through: e.g., team meetings, one-on-ones with a manager, with parents, with a partner, with old friends, with new acquaintances, online/social, alone.
2. **Version-per-arena.** For each arena, a short descriptor of the version of themselves that shows up ("cheerful and agreeable," "guarded and precise," "the fixer," "quiet").
3. **Self-baseline.** How the user acts and speaks when fully at ease — with someone who has seen the real them and it went fine. Concrete: tone, topics, how much they say, what they let show.
4. **Cost signals per arena.** For each arena: drain level after (low/med/high), dread before (Y/N), relief when it ends (Y/N), and who — if anyone — the user can't be honest with there.
5. **Most-expensive arena.** The one arena where the gap between the performed version and the self-baseline feels most costly.
6. **Safety note.** For any arena, whether being more openly oneself would be genuinely unsafe (retaliation, discrimination, a hostile or abusive person). Honest, plain.

If the arena list has fewer than 5 arenas, or input 3 is missing, ask for more — the audit needs a baseline to measure gaps against.

---

## Instructions

### Step 1 — Classify each arena's performance type

Compare each arena's version (input 2) to the self-baseline (input 3) and label it with exactly one type. Not all performance is a problem — the taxonomy exists to separate the legitimate from the costly.

| # | Type | Signature | Reading |
|---|---|---|---|
| 1 | **Aligned** | Version ≈ baseline; low drain, no dread. | Not a gap. Leave it. |
| 2 | **Adaptive code** | Context-appropriate adjustment, freely chosen, low cost (professional register, tact, formality). | Legitimate. Code-switching is not inauthenticity. |
| 3 | **Armor** | Hiding a specific vulnerability for protection; moderate cost. | May be warranted; check safety before touching. |
| 4 | **Audition** | Performing to earn approval, status, or being liked; high cost. | A gap worth closing. |
| 5 | **Assimilation** | Suppressing a core trait to belong; highest cost, erodes self over time. | The most expensive gap; safety-gate before any move. |

Cite the specific version and cost signals that justify each label.

### Step 2 — Cost-score the performances

For Types 3–5 only, score cost = drain (input 4) × frequency of the arena × who gets excluded (the people the user can't be honest with). Aligned and adaptive-code arenas (Types 1–2) are not scored — they aren't costing anything to fix.

### Step 3 — Separate legitimate adaptation from costly performance

State explicitly which arenas are Types 1–2 (fine — do not pathologize them) and which are Types 3–5 (candidates for closing). This step protects the user from the trap of deciding that every adjustment is fakeness.

### Step 4 — Locate the single most expensive gap

Cross the cost scores (Step 2) with the user's own nomination (input 5). Name one arena. If input 5 disagrees with the scores, say so and go with the evidence, noting the discrepancy.

### Step 5 — Safety gate, then one gap-closing move

Before proposing anything, check input 6 for the chosen arena. **If being more openly oneself there is genuinely unsafe, do not prescribe disclosure** — name the constraint plainly, and the move becomes reducing the arena's frequency or cost, or routing the real self to a safe arena instead.

If safe, produce **one** bounded move: show one true thing, once, in that one arena — a real opinion voiced, a boundary stated, a fact about oneself let through, a performed behavior dropped for one interaction. Small and reversible. Not "be your authentic self everywhere."

---

## Constraints

### Must
- Classify every arena into exactly one type with cited cost signals.
- Score cost only for Types 3–5.
- Explicitly protect Types 1–2 as legitimate, not gaps.
- Run the safety gate (input 6) before proposing any move.
- Output exactly one bounded, reversible gap-closing move.

### Must Not
- Treat all role-playing, formality, or code-switching as inauthenticity.
- Prescribe radical honesty or full disclosure, especially where input 6 flags risk.
- Moralize about "living your truth" or "being your authentic self."
- Frame professional or contextual adaptation as a moral failing.
- Output a plan to close every gap — pick one.

---

## False-Positive Prevention

1. **Code-switching is not inauthenticity.** Adjusting register for a context (Type 2) is a competence, not a betrayal of self; do not flag it as a gap.
2. **Some armor is warranted.** Guardedness with an untrustworthy or hostile person is protection, not performance-to-fix. Check safety (input 6) before touching any Type-3 arena.
3. **Never prescribe unsafe disclosure.** If openness invites retaliation, discrimination, or harm, the move is cost-reduction or safe-arena routing — the prompt must not push the user to expose themselves into danger.
4. **A professional role is not a fake self.** Playing a defined role at work isn't inauthentic unless it requires suppressing a core trait (Type 5); distinguish role from suppression.
5. **Privacy and introversion aren't performance.** Choosing not to share, or being quiet by nature, is a self-baseline, not a mask. Measure against the user's real baseline (input 3), not an extroverted default.
6. **Don't reify a single fixed "true self."** The output is closing one costly gap in one arena, not discovering a permanent essence the user must display everywhere.

---

## Output Format

```
## Arena classification
| Arena | Version shown | Baseline gap | Type | Cost signals |
|---|---|---|---|---|
| ... | ... | ... | #N | [drain/dread/relief/excluded] |

## Cost scores (Types 3–5 only)
| Arena | Type | Drain × Frequency × Excluded | Score |
|---|---|---|---|
| ... | ... | ... | ... |

## Legitimate vs costly
- **Leave alone (Types 1–2):** [arenas] — chosen adaptation, not gaps.
- **Candidates (Types 3–5):** [arenas].

## Most expensive gap
[One arena], because [cost score + input 5].

## Safety gate
[Safe to close / Unsafe — constraint named.]

## Gap-closing move (this week)
[If safe: one true thing shown once in that arena, by when. If unsafe: reduce frequency/cost or route real self to a safe arena.]

Predicted check: after this move, [observable drop in drain/dread, or one honest exchange that lands].
```

---

## Verification

- [ ] Every arena classified into one type with cited cost signals.
- [ ] Cost scored only for Types 3–5; Types 1–2 explicitly protected.
- [ ] Legitimate adaptation separated from costly performance.
- [ ] One most-expensive gap named from evidence.
- [ ] Safety gate (input 6) run before any move; no unsafe disclosure prescribed.
- [ ] Exactly one bounded, reversible gap-closing move.
- [ ] No moralizing about authenticity, no radical-honesty mandate.
