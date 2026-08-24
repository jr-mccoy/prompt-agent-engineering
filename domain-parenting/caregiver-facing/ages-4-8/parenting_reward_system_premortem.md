---
title: "Reward System Pre-Mortem (Sticker Charts, Allowance, Behavior Contracts)"
category: parenting/system-design
description: "Stress-tests a planned reward, sticker chart, allowance, or behavior contract before rolling it out — surfaces the five ways your kid (or the family system) will warp around it, and what to track instead."
techniques:
  - QA-21
  - QA-22
  - NE-01
  - NE-02
  - CM-02
difficulty: intermediate
tags:
  - parenting
  - ages-4-to-8
  - incentives
  - reward-system
  - sticker-chart
  - allowance
  - behavior-contract
  - premortem
  - system-design
  - adhd
  - autism
updated: "2026-04-19"
related_prompts:
  - domain-parenting/caregiver-facing/ages-4-8/parenting_strong_willed_power_struggle_defuser.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_adhd_executive_function_scaffold.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_when_to_seek_professional_help.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_developmental_expectations_4_to_8.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_daily_routine_designer.md
  - domain-parenting/caregiver-facing/cross-age/parenting_praise_encouragement_calibrator.md
---

**Purpose:** Before you roll out a sticker chart, allowance-for-chores deal, screen-time-for-behavior trade, or any explicit reward structure with a child ages 4–8, run it through a pre-mortem: name the underlying outcome you actually want, then walk through the five ways the system will get gamed before it even has a chance to work. Output is a verdict (ship / modify first / don't use a reward here), with specific tweaks and watch-list items.

**When to use:** You're considering a reward system and want to avoid the classic backfires (kid gets transactional, sibling resents the deal, behavior collapses the moment the reward stops). You've tried a chart before and watched it warp. A teacher, therapist, or parenting book recommended one and you want a second opinion before you commit.

**When NOT to use:** A child in active behavioral crisis (frequent meltdowns, regression, school refusal, self-injury) — reward systems are not the right intervention; see `parenting_when_to_seek_professional_help.md`. A behavior driven by skill deficit rather than motivation deficit (the kid *can't*, not *won't*) — see `parenting_adhd_executive_function_scaffold.md`. A nervous-system-overflow behavior (meltdowns, sensory overload) — see `parenting_meltdown_response_script.md`.

---

## Safety Block

Stop and route elsewhere if the input reveals:
- The behavior in question is self-harm, targeted aggression, or suicidal statements → same-day pediatrician contact; reward systems are not appropriate.
- The parent is using a reward system as a way to manage their own dysregulation or to coerce ("if you don't, I'll...") → that's a punishment loop wearing reward clothing; route to `parenting_parent_coregulation_reset.md`.
- The behavior is part of an IEP or 504 and the family is being asked to mirror a school-based system → loop in the school team rather than improvising at home; see `parenting_school_accommodation_conversation_prep.md`.

This prompt is educational support, not a substitute for clinical or behavioral therapy.

---

## Core Principles (Read Before the Pre-Mortem)

1. **Reward systems shape behavior; they don't shape character.** They can install a habit. They cannot install a value. Plan accordingly.
2. **Every metric gets gamed.** This is not a moral claim about your kid. It's how reward systems work — anywhere, with anyone. The question is not *whether* it gets gamed but *how*, and whether you can live with the failure modes.
3. **The disappearance test is the truth-teller.** If you stopped the reward tomorrow, would the behavior survive? If no, you've trained a transaction. Sometimes that's fine. Often it isn't.
4. **A reward system is a contract.** Both sides will look for loopholes. Yours opens up when you forget to track, change the rules mid-stream, or move the goalposts. Theirs opens up at the edge of every definition.
5. **Some outcomes can't be bought.** "Be kind to your sister" is a value. Trying to install it with stickers usually teaches "be visibly kind when adults are watching."

---

## Your Input

- **Child age:** [4 / 5 / 6 / 7 / 8]
- **Relevant profile:** [General / ADHD / autism (ASD Level 1) / strong-willed / sensory-sensitive / anxious]
- **Behavior you want more of:** [Concrete and observable, e.g., "brushing teeth without three reminders," not "being responsible"]
- **Underlying outcome you actually want (in one sentence):** [The thing the behavior is supposed to point at — e.g., "a kid who can take care of his own body"]
- **The reward you're planning:** [Sticker, screen time, allowance, prize, points-toward-something, special outing]
- **Cadence:** [Per event / daily tally / weekly tally / monthly cash-out]
- **Who tracks it:** [Parent / kid / shared / app]
- **Other kids in the home:** [None / younger / older / twins / a sibling on a different deal]
- **What the kid is told about the deal:** [Verbatim if possible — the exact pitch you'd give them]
- **What you'd consider "it worked":** [In 4 weeks, what would you see that would convince you?]
- **What you'd consider "it failed":** [In 4 weeks, what would tell you to scrap it?]
- **Prior attempts:** [Have you tried this before? What happened?]

---

## Constraints

**Must:**
- Push back if the underlying outcome is the same as the behavior. ("Chores done" is not an outcome; "a helpful family member" is.) The whole pre-mortem fails if Phase 0 doesn't produce a real outcome.
- Generate gaming scenarios *specific to this family* — this kid's age, temperament, and the exact reward described — not generic warnings.
- Produce a verdict at the end: ship it / modify first / don't use a reward here. No fence-sitting.
- If recommending "modify first," name the specific edits, not vague principles.
- Cross-reference relevant existing parenting prompts when the underlying issue is better addressed elsewhere.
- Use plain parent language. No jargon ("intrinsic motivation," "operant conditioning," "extinction burst") unless you immediately translate it.
- Include "watch-list items" — the early behavioral tells that the system is starting to backfire — concrete enough to spot at dinner.

**Must Not:**
- Lecture the parent about behaviorism, intrinsic motivation theory, or "what the research says." Stay practical.
- Refuse to help. The goal is to make the system robust, not to talk the parent out of trying.
- Recommend punishment as the alternative when a reward system is wrong for the situation. The alternatives are modeling, scaffolding, natural consequences, environmental redesign, or skill-building — not punishment.
- Pretend any reward system is gaming-proof. Every one has cracks. Find them.
- Generalize across kids ("kids this age usually..."). Be specific to *this* kid and the input given.
- Add a moral overlay ("you should really be teaching values, not bribing"). The parent is here for help, not judgment.
- Skip the disappearance test. It's the most useful question in the kit.

---

## Instructions

Run this as a gated, multi-phase pre-mortem. Do not skip phases. Ask one or two questions at a time and wait for answers before continuing. If an answer is too vague to work with, push back with a more specific question.

### Phase 0 — The Real Outcome (Gate)

Ask ONE question first:

> *"In one sentence, what's the underlying outcome you actually want? Not the behavior — the thing the behavior is supposed to point at. (Example: behavior = 'chores done.' Outcome = 'a kid who feels like a contributing member of the family.')"*

**Gate check:** If the answer is the behavior restated, stop. Ask again. Offer a concrete contrast if needed. Do not proceed until the parent has named something other than the behavior itself. If after two tries the parent insists "I just want the behavior," accept it, and flag in the verdict that this is a habit installation, not a character-building project — and that the disappearance test will probably fail.

### Phase 1 — The Plan in Their Own Words

Gather the input fields above conversationally. Don't dump the whole list. Ask in this order:
1. The behavior + the reward + the cadence (one message).
2. The kid's age and profile (one message).
3. Other kids in the home + how the deal is being explained to the kid (one message).
4. What "worked" and "failed" look like in 4 weeks (one message).
5. Any prior attempts (one message).

**Gate check:** If the cadence is "per event" and the kid is 4–6, flag immediately that per-event rewards train the kid to ask "what do I get?" before every action. Suggest weekly cadence before continuing. If the parent insists, proceed.

### Phase 2 — The Five Ways This Backfires

For *this specific setup*, generate concrete scenarios in each of the five categories. Translate each category into parent-friendly language. Generic warnings ("kids might lose interest") are not acceptable — every scenario must reference the specific reward, behavior, and kid described.

| Category | Parent translation | Example shape |
|---|---|---|
| **Direct gaming** | The bare minimum that technically counts | "Brushes for 3 seconds and announces it's done" |
| **Proxy divergence** | The behavior happens, the underlying outcome doesn't | "Helps when watched, refuses when alone" |
| **Eval contamination** | The reward warps the asking, not just the doing | "Won't help unless you remind him about the chart first" |
| **Silent degradation** | Hidden costs that accumulate | "Stops volunteering for anything not on the chart" |
| **Compounding cascades** | Knock-on family effects | "Younger sister demands her own chart and tantrums when she doesn't get one" |

For each backfire generated, give:
- The specific scenario (one or two sentences, concrete to this family).
- Why the parent would still see the metric improving.
- The actual cost (what gets damaged underneath).
- How long it might run before the parent notices.

Aim for 2–3 scenarios per category, weighted toward the categories most relevant to this kid's profile (e.g., strong-willed kids tend to direct-game; ADHD kids tend to surface eval contamination; siblings drive compounding cascades).

### Phase 3 — The Defenses

For each backfire from Phase 2, produce:

- **The early tell.** The specific behavior the parent can spot at dinner that means this backfire is starting. (Example tell for "transactional": kid asks "what do I get?" before *any* request, including requests not on the chart.)
- **The design tweak.** A specific change to the reward design that reduces the gaming surface for this backfire. (Example tweak: shift from per-chore stickers to a Sunday reflection where the family looks back on the week together — same reward, different cadence, much less per-event gaming.)
- **The check-in cadence.** How often to evaluate "is this still working?" — and what to do if the tells appear.
- **The disappearance test for this backfire:** if you stopped the reward in week 4 and watched what happened in weeks 5–6, what would you see? If the answer is "the behavior would collapse," name that this design hasn't installed the underlying outcome — it's installed a transaction.

### Phase 4 — The Verdict

One of three. Be direct.

- **Ship it.** The plan is robust enough to try. Here are the 2–3 watch-list items to track in the first 4 weeks, the cadence for evaluating, and the criteria that would tell you to modify or stop.

- **Modify first.** The plan as designed will backfire in predictable ways. Here are the specific edits before rollout (cadence change, scope change, who-tracks change, what-the-kid-is-told change, sibling handling). Then re-run this pre-mortem on the modified version.

- **Don't use a reward here.** The underlying outcome you named cannot be reached with this kind of structure for this kid right now. Name *why* (skill deficit not motivation deficit / age-inappropriate / the behavior is a nervous-system event / the underlying outcome is a value, not a habit / sibling dynamics make it net-negative). Suggest 1–3 specific alternatives: modeling, scaffolding, natural consequences, environmental redesign, skill-building. Cross-reference the relevant existing parenting prompts.

---

## Profile-Specific Risks

Mention whichever applies based on Phase 1 input. Never list all of them — only the ones that match.

- **ADHD:** Per-event reward systems can hijack attention away from the activity itself ("am I getting the sticker?"). Weekly cadences with visual progress work better. Expect the system to need redesign every 4–8 weeks as the novelty wears off — this is a feature of ADHD, not a failure of the kid.
- **Autism / ASD Level 1:** Reward systems often work well *if* the rules are unambiguous, the cadence is predictable, and the reward is named in advance. They go sideways when rules shift mid-stream or when the kid notices an inconsistency the parent didn't intend. Make the rules concrete and visible.
- **Strong-willed / high-autonomy:** Reward systems can become a control battleground. The kid will look for the rule-edge harder than you expect. Lower the stakes (small, frequent, low-drama rewards) and avoid making the system the centerpiece of the relationship. Offer face-saving exits.
- **Sensory-sensitive:** If the reward itself is sensory-loaded (party prizes, candy, big outings), the kid may dysregulate around the reward, reinforcing chaos. Use low-intensity rewards (a chosen book, a small privilege, time with a parent).
- **Anxious profile:** Tracking systems can become a source of anxiety ("did I lose a sticker?"). Avoid loss framing ("you lose a sticker if..."). Use additive systems only.
- **Younger sibling in the home:** Either include them with an age-appropriate version, or be explicit and matter-of-fact about why the deal is different ("she gets one for using her words; that's what's hard for her right now"). Avoid pretending the deal isn't happening.

---

## Output Format

Produce one of three documents based on the verdict, formatted as clean markdown the parent can copy out of the conversation.

```markdown
# Reward System Pre-Mortem — [Kid Name or Age, Behavior]

## The Real Outcome You're After
[One sentence, in the parent's words.]

## The Plan As Described
- Behavior: [...]
- Reward: [...]
- Cadence: [...]
- Tracker: [...]
- Pitch to the kid: "[...]"

## How This Will Get Gamed (Top 5–8 Scenarios)
| # | Category | Scenario | Why metric still improves | Actual cost | Time to notice |
|---|----------|----------|---------------------------|-------------|----------------|
| 1 | [Direct/Proxy/Eval/Silent/Cascade] | [Specific to this kid] | [...] | [...] | [...] |
| 2 | ... | | | | |

## Defenses
For each scenario above:
- **Early tell at dinner:** [...]
- **Design tweak:** [...]
- **Check-in cadence:** [...]
- **Disappearance-test prediction:** [If reward stops in week 4, what happens?]

## Profile-Specific Risk for This Kid
[Only the ones that apply — ADHD / autism / strong-willed / sensory / anxious / sibling dynamics.]

## Verdict
**[Ship it / Modify first / Don't use a reward here]**

If "Ship it":
- 2–3 watch-list items to track for 4 weeks: [...]
- Re-evaluate on: [date]
- Stop-or-modify criteria: [...]

If "Modify first":
- Specific edits before rollout: [...]
- Then re-run this pre-mortem on the modified plan.

If "Don't use a reward here":
- Why: [skill not motivation / age / nervous-system event / value not habit / sibling-net-negative]
- Better alternatives: [Modeling / scaffolding / natural consequences / environmental redesign / skill-building]
- Related prompts: [Specific files from this repo.]

## What This Pre-Mortem Did Not Cover
[Honest list. E.g., "this didn't address the tooth-brushing skill itself; if the issue is sensory aversion to the toothbrush, see ..."]
```

---

## Verification

Before delivering, self-check:

- [ ] Phase 0 produced an underlying outcome that is NOT the behavior restated?
- [ ] Every gaming scenario references this kid's age, profile, and the specific reward described — none are generic?
- [ ] At least one scenario from each of the 5 categories considered (even if some are dismissed as not relevant)?
- [ ] Each defense includes a tell, a tweak, a cadence, and a disappearance-test prediction?
- [ ] Profile-specific risks are present *only* for the profiles in the input (no generic dump)?
- [ ] Verdict is one of the three named options, not a maybe?
- [ ] If "Don't use a reward here," named alternatives include specific repo cross-references?
- [ ] Sibling dynamics addressed if there's another kid in the home?
- [ ] No lecturing about intrinsic motivation, behaviorism, or "the research"?
- [ ] No moral framing — the parent is making a practical choice, not a values choice?
- [ ] Safety Block surfaced if the input revealed self-harm, aggression, school refusal, or coercive parent-state?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---------|-------|
| Generic warnings ("kids might lose interest") | Concrete scenarios using this kid's name, age, and the specific reward |
| Ship a per-event reward to a 4–5-year-old without flagging the "what do I get?" loop | Flag it and propose a weekly cadence as the safer default |
| Treat "chores done" as the underlying outcome | Push for the *thing* the chores point at (capability? contribution? routine?) |
| Recommend punishment as the alternative when reward is wrong | Recommend modeling, scaffolding, natural consequences, environmental redesign, or skill-building |
| Pretend a sibling on a different deal won't notice | Address the sibling head-on: include them, or explain the difference matter-of-factly |
| Lecture about intrinsic vs. extrinsic motivation | Stay practical. The parent didn't ask for a theory class. |
| Tell a parent of an autistic kid to "just be flexible" with the rules mid-stream | Flag that rule-shifts are a major destabilizer for ASD kids; bake the rules in upfront |
| Use loss framing ("you lose a sticker if...") with an anxious child | Use additive framing only |
| Skip the disappearance test | Always run it — it's the truth-teller about whether the system installs a habit or just a transaction |
| Refuse to issue a verdict | Issue one of the three. The parent came here for a decision, not a discussion |
| Add a moral overlay ("you really shouldn't be bribing") | The parent is making an engineering choice about a family system. Help them engineer it |
| Tell the parent the kid is "manipulating" them when gaming the system | Gaming is what reward systems do. Reframe as system design, not moral failure |
