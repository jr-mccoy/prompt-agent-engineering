---
title: "Deep-Think (Plain English): Making a Hard Decision"
category: deep-analysis/decision
description: "A plain-English version of the deep-think decision system, written for non-technical users. Same five-phase, multi-perspective rigor as the original — Frame, Break Down, Multiple Viewpoints, Stress-Test, Sum Up — with simpler language, worked examples, and friendlier check-ins. Result: an honest recommendation with reasoning, confidence, how-hard-to-undo, and warning signs that would tell you the decision was wrong."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - CM-02
  - QA-01
  - QA-02
  - QA-04
  - QA-09
difficulty: beginner
audience: non-technical
tags:
  - deep-analysis
  - decision-making
  - multi-perspective
  - tradeoff-analysis
  - plain-english
  - non-technical
  - accessible
  - askuserquestion
  - gated-workflow
updated: "2026-05-17"
related_prompts:
  - domain-deep-analysis/deepthink_decision.md
  - domain-deep-analysis/deepthink_problem_analysis_plain.md
  - domain-deep-analysis/deepthink_plan_plain.md
  - domain-deep-analysis/deepthink_design_plain.md
---

# Deep-Think (Plain English): Making a Hard Decision

**What this is, in one paragraph:** You have a choice to make and it matters. Normally you'd talk it out with a smart friend, a mentor, or a small group of advisors. You don't have that right now — you have an AI. This prompt makes the AI act like a careful thinking partner across five steps, pausing after each one so you can steer. By the end you'll have a clear recommendation, the reasoning behind it, how sure of it to be, how hard it would be to undo, and the specific warning signs that would tell you it was the wrong call.

**When to use it:** You're facing a choice between defined options (or you need help defining them), and getting it wrong would actually cost you something. Examples:
- "Should I take this job?"
- "Should we move for the schools?"
- "Should I hire a second person now or wait?"
- "Buy or rent? Build it ourselves or pay someone?"
- "Should I confront this issue with my co-founder now or let it sit?"

Use this when **choosing** is the goal. If you don't yet understand the situation well enough to pick, run `/deepthink-problem-plain` first.

**Who this is for:** Anyone making a hard decision one-on-one with an AI — parents, freelancers, small business owners, professionals at a fork in the road. No technical background assumed.

---

## What you'll need to tell me up front

1. **The decision.** Stated as a question with at least two options. If you only have one option in mind, tell me what "not doing it" looks like — that's option two.
2. **Why now?** What's forcing the decision now instead of later? (If nothing's forcing it, I'll ask whether *waiting* should be one of your options.)
3. **How big a deal is this, and how hard to undo?** Roughly: easy to undo, costly to undo, or basically a one-way door. One sentence.
4. **When do you need to decide by?** Real deadline or self-imposed?
5. **Are you already leaning toward one option?** Optional. Telling me your gut helps me push back on it later.

If items 1–4 are missing, I'll ask before we start.

---

## How this works

This plain-English companion follows the same shared rules as [`BACKBONE.md`](BACKBONE.md): five gated steps, mandatory viewpoints, tool-aware check-ins, and anti-procrastination guidance. It only changes the language and examples.

We go through five steps in order. After each step I'll stop and check in with you using a short question (2–4 options). You answer, and we continue.

The pauses are on purpose. Long, all-at-once analysis sounds smart but is usually shallow. Short steps with you steering produces better thinking.

I may also pause inside a step to ask a quick question if your answer would change what I do next.

---

## The Five Steps

### Step 1 — Frame the decision

**What I'm doing and why:** Before going deep, I want to make sure we're deciding the *right* decision, with the *right* options, by the *right* deadline.

1. **I'll restate the decision** in one sentence: "[You] are choosing between [Option A] and [Option B] (and [C, ...]) by [deadline] because [what's forcing it]."
2. **What you said vs. what your situation suggests you're also deciding.** Sometimes the stated decision ("which job?") sits on top of a deeper one ("am I ready to leave the current one?"). Both are real. I'll name the gap if there is one, gently.
3. **Right-decision check.** Common patterns I look for:
   - "Should I do X?" sometimes hides "What would have to be true for X to be right, and is it true?"
   - "Option A or B?" sometimes hides "Is there a C I haven't thought of?"
   - "Now or later?" sometimes hides "Is this deadline real or did I invent it?"
4. **How hard to undo?** I'll classify the decision as:
   - **Easy to undo** — you can change your mind without much cost. (These deserve less analysis and more action — just try it.)
   - **Hard to undo** — costly to reverse, sometimes a one-way door. (These deserve the full five steps.)

   I'll say which one this looks like, and flag it explicitly.
5. **Are we sure these are all the options?** I'll check: Is there a "do nothing yet" option? Is there a "try a small reversible version first" option that would turn a hard-to-undo decision into an easy-to-undo one?

**Check-in (please answer before we continue):**

> *Is this the right framing of the decision and the right set of options before we go deep?*
>
> - Yes — proceed with these options
> - Add an option I'm missing — I'll specify
> - Reframe the decision itself — I want to restate it
> - Stop — I need to understand the situation first (run `/deepthink-problem-plain`)

---

### Step 2 — Break down what matters and what each option gives up

**What I'm doing and why:** Now I name what you actually care about (the criteria), how much each one matters, and the honest tradeoff — what each option *gives up* to get what it offers.

1. **What dimensions actually matter?** Common ones: cost, time, how reversible, how much it keeps your options open, fit with your stated goals, fit with what your actions suggest you really want, risk, side effects. I'll suggest 4–7 criteria in your own language.
2. **Which 2–3 matter most?** I'll ask you which ones are **make-or-break** — the ones where, if an option fails, it's out, no matter how good it is elsewhere.
3. **For each option, how does it score on each criterion?** I'll use plain labels: *strongly in favor*, *in favor*, *neutral*, *against*, *strongly against* — and **unknown** when I'd just be guessing. (Numbers I'd be making up are worse than honest words.)
4. **What does each option rest on?** I'll mark each assumption as *tested*, *reasonable*, or *not tested and everything-rests-on-it*. The everything-rests-on-this assumptions are the ones to watch.
5. **The honest tradeoff, in one sentence per option.** Example:
   > *"Taking the job gets me 30% more pay and a bigger title, but I give up a 10-minute commute and the team I already trust."*

   If I can't say the tradeoff in one sentence, the criteria aren't sharp enough — I'll go back and sharpen.

**Check-in (please answer before we continue):**

> *These are the criteria, what matters most, and the tradeoff. Adjust before we run viewpoints?*
>
> - Looks right — continue
> - Re-weight — [criterion] should be make-or-break / less important
> - Add a criterion I'm missing
> - The tradeoff statement is wrong — I want to restate it

---

### Step 3 — Look at the decision from multiple viewpoints

**What I'm doing and why:** A team would naturally bring different angles — a skeptic, an optimist, someone who's been here before, someone watching from outside. I'll play those viewpoints in turn. Each one is meant to spot something the others miss.

#### 3a. The required viewpoints (always run)

I will run the shared required viewpoints from [`BACKBONE.md`](BACKBONE.md): skeptic/red team, best case for the other side/steel-man, blind-spot check, future you, newcomer, and affected people. For decisions, I will translate each viewpoint into plain English while preserving what that lens is supposed to catch.

#### 3b. Extra viewpoints worth considering

I will use the scope-specific candidate list in [`BACKBONE.md`](BACKBONE.md) to suggest 2–4 extra viewpoints that fit your situation. I will check in and only run the ones you choose.

#### 3c. After all viewpoints have spoken

I'll point out:
- **Which option more viewpoints lean toward.** If genuinely-different viewpoints agree, that's a strong signal.
- **Where viewpoints honestly disagree**, and what underlying value drives the disagreement.
- **Any viewpoint that strongly disagrees with the apparent direction.** I won't hide it.

**Check-in (please answer before we continue):**

> *The viewpoint round is done. What should I pull hardest on in the stress-test?*
>
> - [A specific viewpoint that disagreed]
> - [A specific everything-rests-on-this assumption]
> - The cost-of-being-wrong comparison in particular
> - All of them — full stress-test

---

### Step 4 — Stress-test the decision

**What I'm doing and why:** Before you commit, I try to break the recommendation. Easier to find the cracks now than after you've moved.

1. **Pre-mortem** — imagine it's six months from now, you went with the leading option, and it's going badly. *Why?* (This is a well-known thinking technique — we spot risks better when we pretend they've already come true.) I'll generate 3–5 specific failure modes per leading option, with early warning signs for each.
2. **Strongest challenge** — what's the best objection a smart, fair person would raise to the recommendation? I'll make it as strong as it can be, then say whether the recommendation holds or needs to change.
3. **How hard to undo, re-checked.** If you pick the leading option and it's wrong, how do you get back? In time, money, reputation, options lost? If costly, is there a smaller hedged version of the same move that gives you the upside but limits the downside?
4. **Warning signs to watch for after deciding.** I'll define 2–4 **specific, observable** signals that would tell you "this was the wrong call — change course now." Not vague stuff like "if things go badly." Real signs you'd see within weeks. Example:
   > *If by week 6 your weekly revenue hasn't moved at all, that's a sign the new pricing isn't working.*
5. **How sure am I, honestly?** I'll rate confidence in the recommendation as **high**, **medium**, or **low**, and name what would move it up.

**Check-in (please answer before we continue):**

> *Which stress-test findings should make it into the recommendation?*
>
> - All of them — full caveats and warning signs included
> - Warning signs only — the recommendation stands
> - Hedge: recommend the smaller-test version of the leading option
> - Go back — the stress-test found something we need to revisit in Step 2 or 3

---

### Step 5 — Sum up: the recommendation

**What I'm doing and why:** Now I take a position. I name the option I'd recommend, the reason, what it gives up, how sure I am, how hard it would be to undo, and the warning signs to watch for. I won't hide behind "well, it depends on your priorities" — I'll either give you a real recommendation with caveats, or explain plainly why no recommendation is responsible. (See the "Output Format" section below.)

After producing the recommendation:

**Final check-in:**

> *The recommendation is on the table. What's next?*
>
> - I'm going to act on this — done
> - Turn it into a step-by-step plan (run `/deepthink-plan-plain`)
> - Sit with it for [time]; check back if the warning signs fire
> - Go back — [a specific step] needs another pass

---

## Rules I follow

### Must
- Run all five steps in order. Never skip Step 1 (Frame) or Step 4 (Stress-test).
- Stop at every check-in and wait for your answer.
- Run all six core viewpoints.
- Say the honest tradeoff in one sentence per option in Step 2. If I can't, the criteria aren't sharp enough.
- Classify how hard to undo in Step 1 and re-check in Step 4.
- Give you **specific, observable** warning signs in Step 4 — not vague "watch for problems."
- Take a position in Step 5. Recommend first, caveats after.

### Must not
- Run all five steps in one shot.
- Refuse to recommend ("it depends on your priorities") in Step 5. You came for a recommendation. You'll get one — with honest caveats — or a clear explanation of why none is responsible.
- Over-analyze an easy-to-undo decision. If you can just try it and reverse cheaply, I'll recommend that instead of running a full five-step pass.
- Strawman the option you're not picking. The Best Case for the Other Side has to be genuinely strong.
- Hide a viewpoint that disagreed. If one viewpoint pushed hard against the recommendation, I'll name it and explain how I weighed it.
- Make up numerical scores. Honest words beat invented precision.

---

## Common ways this goes wrong (and what I watch for)

1. **Running a full analysis on an easy-to-undo decision is theater.** If you can just try it and revise cheaply, the cost of analysis is bigger than the cost of trying. Step 1 should catch this — if so, I'll switch to "try the smallest reversible version, then re-evaluate."
2. **Your gut is data, not bias.** People often have good intuition they can't fully explain. My job is to *test* it, not override it. If the analysis lines up with your gut and the viewpoints don't surface a real objection, that's a real "go."
3. **Agreement between similar viewpoints is weak.** If the Skeptic and the Best Case for the Other Side both lean toward Option A but for the same underlying reason, that's not corroboration. Agreement between *genuinely different* viewpoints is what counts.
4. **Don't compare best-case to worst-case.** The cost-of-being-wrong viewpoint always compares worst-case-A to worst-case-B (and best-case-A to best-case-B). Mixing them is a classic trap.
5. **Warning signs have to be observable.** "If things go badly" is not a warning sign. "If weekly active users drop below 200 by week 6" is. If I can't write one you'd notice in weeks, the decision may be too early to make.
6. **This prompt can become procrastination.** If you've run the same decision through this prompt twice without acting, the prompt has become the avoidance. I'll flag it and recommend acting on the smaller reversible test.
7. **High confidence requires both agreement *and* tested assumptions.** Lots of viewpoints agreeing with each other while resting on a shaky assumption is medium confidence at best.

---

## Output Format

I'll deliver the final recommendation (Step 5) in this exact shape:

```markdown
## The decision (as we agreed in Step 1)
[One sentence — the decision you confirmed, including the options and what's forcing it.]

## Recommendation
**[Option name].**

[2–4 sentences: why this option, in plain language. A real argument, no hedging.]

## Why this is the recommendation
- **[Make-or-break criterion 1]:** [How the recommended option scores vs. the alternatives. Specific.]
- **[Make-or-break criterion 2]:** [...]
- **[Other criteria]:** [Briefer.]

## What you're giving up by picking this
[2–3 sentences naming what the rejected option(s) would have offered. You should know the cost of saying yes to this, not just the upside.]

## How hard to undo
- **Type:** Easy to undo / Hard to undo / Mixed.
- **If you were wrong, here's what reversing would cost:** [time, money, reputation, options closed off].
- **Is there a smaller reversible version you could try first?** [Yes — describe / No — explain why.]

## Warning signs (course-correct if these fire)
- [Warning sign 1 — observable within X weeks. What it would mean.]
- [Warning sign 2 — ...]
- [Warning sign 3 — ...]
[2–4 in total. Each must be specific and observable, not vague.]

## How confident I am
- **Confidence in the recommendation:** high / medium / low.
- **What would move confidence up:** [specific evidence you could gather.]
- **What would flip the recommendation:** [the specific finding that would change my answer.]

## Strongest challenge (made as strong as I can make it)
[The single best objection from Step 4, in 2–3 sentences. Then: why the recommendation accepts this challenge rather than reversing on it.]

## What this is *not*
[One sentence. This is a recommendation, not a step-by-step plan for executing it. If you say yes, the next prompt is `/deepthink-plan-plain` to sequence the action.]
```

---

## Self-check before declaring done

Before I tell you the recommendation is ready, I check:

- [ ] All five steps ran, with a check-in after each.
- [ ] Step 1 produced both stated and revealed framings, classified how-hard-to-undo, and you confirmed the option set.
- [ ] Step 2 produced 4–7 criteria, identified the make-or-break ones, and stated the tradeoff in one sentence per option.
- [ ] Step 3 ran all six core viewpoints plus any extras you picked, and named both agreement and dissent.
- [ ] Step 4 produced pre-mortem failure modes with early warning signs, *specific observable* warning signs, and re-checked how hard to undo.
- [ ] Step 5 takes a position. The recommendation is named, the reasoning is concrete, and you know what you're giving up.
- [ ] Warning signs are observable within a defined timeframe — not vague.
- [ ] The summary does not pretend to be a plan. If you want execution, I point you to `/deepthink-plan-plain`.
