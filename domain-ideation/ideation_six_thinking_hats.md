---
title: "Six Thinking Hats — Parallel Thinking on One Proposal"
category: ideation/parallel-thinking
description: "Run a proposal, plan, or idea through de Bono's six thinking modes — facts (white), feelings (red), caution (black), benefits (yellow), alternatives (green), process (blue) — one mode at a time, so the whole group (or a solo thinker) explores the same angle together instead of arguing across angles. Chooses a hat sequence to fit the purpose, keeps each mode pure, and ends with a blue-hat summary of what changed. Distinct from ideation_persona_what_would_x_do.md, which generates new ideas from other people's viewpoints; hats examine one proposal through modes of thinking everyone adopts at once."
techniques:
  - NE-12
  - ST-02
  - CM-02
  - OC-03
  - QA-01
difficulty: beginner
tags:
  - ideation
  - six-thinking-hats
  - parallel-thinking
  - group-discussion
  - proposal-review
  - facilitation
  - meetings-become-debates
  - constant-naysayer
  - review-my-idea
updated: "2026-09-24"
reasoning:
  styles: [parallel, divergent, evaluative]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, founder, facilitator, strategist, individual]
  mode: [diverge, converge]
related_prompts:
  - domain-ideation/ideation_persona_what_would_x_do.md
  - domain-ideation/ideation_idea_convergence_dot_voting.md
  - domain-decision-making/decisioning_fresh_perspective_generator.md
---

# Six Thinking Hats — Parallel Thinking on One Proposal

**Objective:** Examine a single proposal, plan, or idea through six distinct modes of thinking, one at a time, so that everyone involved is looking in the same direction at the same moment. The method (Edward de Bono, 1985) exists to stop the most common meeting failure: one person defending benefits while another attacks risks and a third states feelings as facts, so no angle is ever explored fully. The prompt picks a hat sequence suited to the purpose, runs each hat with its rules enforced, and closes with a blue-hat summary of what the session changed.

| Hat | Mode | Rule |
|-----|------|------|
| **Blue** | Process | Sets the focus, sequence, and time; summarises at the end |
| **White** | Facts and information | What we know, what we do not, what we would need — no interpretation |
| **Red** | Feelings and intuition | Gut reactions, stated without justification, kept short |
| **Black** | Caution | Risks, weaknesses, why it might not work — each with a reason |
| **Yellow** | Benefits | Value and why it could work — each with a reason |
| **Green** | Creativity | Alternatives, modifications, new possibilities; no judgement |

---

## When to Use

- A proposal is on the table and discussion keeps collapsing into advocate versus critic.
- A group has a dominant pessimist or optimist and you want both views given their turn and their limit.
- You want a structured solo review of your own idea that does not skip the angle you dislike.
- An idea from a divergence sprint needs a fuller look before it enters scoring.

**Distinct from:**
- `domain-ideation/ideation_persona_what_would_x_do.md` — generates new ideas from five external viewpoints (contrarian, regulator, child…). Hats examine *one existing proposal*, and the modes are thinking styles everyone wears together, not characters.
- `domain-ideation/ideation_idea_convergence_dot_voting.md` — narrows a long list. Hats go deep on one item.
- `domain-decision-making/decisioning_fresh_perspective_generator.md` — offers new perspectives on a framed decision; it does not sequence a group through modes.

**When NOT to use:**
- You have fifty ideas and need five — converge first.
- The decision is purely quantitative and the data settles it; a white-hat pass alone is enough.

---

## Inputs / Context

1. **The proposal.** Stated in two or three sentences.
2. **Purpose of the session.** Evaluate, improve, decide, or explore — this sets the sequence.
3. **Participants.** Solo, or the group and any known dominant voices.
4. **Available facts.** Data the white hat can draw on; gaps are fine.
5. **Time available.** Used to allocate minutes per hat.

---

## Method

### Step 1 — Blue hat: set the focus and sequence
State the question in one sentence. Choose a sequence to fit the purpose:
- **Evaluate a proposal:** Blue → White → Green → Yellow → Black → Red → Blue
- **Improve an idea:** Blue → White → Yellow → Black → Green → Blue
- **Quick gut check:** Blue → Red → Yellow → Black → Red → Blue

Allocate time; red hat gets the least (under a minute per person).

### Step 2 — Run each hat in order
For each hat, generate only content of that mode. In group mode, everyone contributes to the same hat; in solo mode, the model produces the hat's content and flags any line that belongs to another hat.

### Step 3 — Enforce the purity rules
- White: facts and named unknowns only; opinions go to a "parked" list.
- Red: no justifications. "I feel uneasy about the pricing" is complete.
- Black and yellow: every point carries a *because*. Unreasoned pessimism is red-hat content.
- Green: no evaluation; black-hat reactions to green ideas are parked for later.

### Step 4 — Second black hat on green output (optional)
If green produced alternatives worth keeping, run a short black hat on the top one or two only.

### Step 5 — Blue hat: summarise and decide next action
List what changed: new facts needed, risks with mitigations, strongest benefits, alternatives worth pursuing, and the collective red-hat reading at close versus open. Name the next action and owner.

---

## Output Format

```
# Six Hats — [proposal]

## Blue (open): question, purpose, sequence, time per hat

## White — facts
| Known | Unknown | How we'd find out |

## Red — feelings (open)
- ...

## Yellow — benefits (each with because)
## Black — cautions (each with because)
## Green — alternatives / modifications

## Parked (content that arrived under the wrong hat)
| Line | Belongs under |

## Red — feelings (close)   [if in sequence]

## Blue (close): summary
- Facts to obtain:
- Top risks and mitigations:
- Strongest benefits:
- Alternatives to pursue:
- Shift in red-hat reading:
- Next action / owner:
```

---

## Verification

- [ ] Sequence chosen and justified by the stated purpose.
- [ ] Every black- and yellow-hat point carries a reason.
- [ ] Red-hat entries carry no justification and are brief.
- [ ] White-hat section contains no interpretation; unknowns are listed.
- [ ] Off-mode content is parked, not deleted.
- [ ] Closing blue hat names a next action and owner.

---

## False-Positive Prevention

1. **Hats as roles.** Assigning "Sam is always black hat" recreates the debate the method removes. Everyone wears the same hat at the same time.
2. **Black hat as the verdict.** A long black-hat list does not mean the idea is bad; it means cautions were explored. Weigh them against yellow and mitigations.
3. **Opinion in a white hat.** "Customers will hate this" is not a fact. Move it to red or black, with its reason.
4. **Yellow-hat cheerleading.** "It's exciting" is red. Yellow requires a reason the benefit is real.
5. **Skipping red because it feels soft.** Unspoken feelings leak into black-hat arguments. Giving them sixty seconds keeps the other hats honest.
6. **Green ideas judged on arrival.** Evaluating during green kills the alternatives before they are finished. Park the reactions.
7. **No closing blue.** Six sections without a summary is a transcript. The session ends with what changed and who acts.

---

## Example

**Proposal:** "Move our 12-person agency to a four-day week (32 hours) from next quarter at the same pay." Purpose: evaluate.

- **Blue:** Should we pilot a four-day week next quarter? Sequence: evaluate. 45 minutes.
- **White:** Known — 80% of revenue is retainers with response-time clauses; utilisation averaged 71% last year. Unknown — whether clients' contracts define "business days"; how many hours currently go to internal meetings. Find out: contract review; one-week calendar audit.
- **Red (open):** excited; anxious about the retainer clients; sceptical it survives a busy month.
- **Green:** staggered days so every weekday is covered; pilot with one team only; 32 hours as flex-time rather than a fixed Friday.
- **Yellow:** retention — two resignations last year cited burnout, *because* replacing a designer costs roughly a quarter's billing; recruiting edge *because* few local agencies offer it.
- **Black:** retainer response-time breaches *because* clients expect Friday coverage; unbilled overtime creep *because* scope does not shrink with hours.
- **Parked:** "Clients won't notice" (arrived under white; belongs under yellow and needs a reason).
- **Red (close):** anxiety now attached to one specific thing — Friday coverage — rather than general.
- **Blue (close):** obtain contract terms and meeting-hours audit; mitigate coverage with staggered days; pilot with one team for eight weeks; owner: operations lead, decision date in three weeks.

---

## Techniques Used

- **NE-12 Cognitive Mode Framing** — each hat is an explicit mode directive set before content is produced.
- **ST-02 Structured Sequential Instructions** — purpose-dependent hat sequences.
- **CM-02 Constraint Specification** — per-hat purity rules (reasons required, no justification for red).
- **OC-03 Markdown Table Specification** — white-hat known/unknown table and parked-content table.
- **QA-01 Self-Verification** — parked-content audit and closing checklist.

---

## Related Prompts

- `domain-ideation/ideation_persona_what_would_x_do.md` — generate ideas from outside viewpoints.
- `domain-ideation/ideation_idea_convergence_dot_voting.md` — narrow a long list before going deep on one.
- `domain-decision-making/decisioning_fresh_perspective_generator.md` — new perspectives on an already-framed decision.
