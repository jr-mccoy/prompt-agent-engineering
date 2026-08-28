---
title: "Math Drill Sequencer"
category: education-teaching/learner/study-by-discipline
description: "Designs a spaced, interleaved math problem sequence from a skill list: maps prerequisite dependencies, assigns problem difficulty tiers, schedules spacing based on recent performance, flags prerequisite gaps before drilling dependent skills, and generates the complete problem set."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - CM-01
  - QA-04
difficulty: intermediate
tags:
  - mathematics
  - problem-sequencing
  - interleaving
  - spaced-practice
  - prerequisite-mapping
  - drill
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_math_proof_practice.md
  - domain-education-teaching/learner/study-by-discipline/learn_science_problem_interleaver.md
  - domain-education-teaching/learner/memory-and-recall/learn_retrieval_drill_designer.md
  - domain-education-teaching/learner/exam-prep/learn_weak_area_diagnosis.md
---

## Objective

Design a math drill sequence that is spaced (matching review intervals to retention needs), interleaved (mixing skill types to prevent false fluency), and prerequisite-aware (blocking drills on dependent skills when foundational gaps exist). The output is a ready-to-practice problem set with difficulty progressions, not just a list of topics.

## When to Use

- When a learner has multiple math skills to maintain simultaneously and needs to know what to practice in what order
- When preparation for a cumulative exam requires practicing both new and previously learned skills
- When a learner's study plan consists of "practice more problems" without a principled sequencing system
- When prerequisite gaps are suspected — certain problems keep failing even though the learner has studied them

**Do not use** to learn a new concept from scratch — this is a review and reinforcement tool. For initial encoding, use a worked-examples approach first. Do not use `learnstudy_math_proof_practice.md` instead — that prompt specializes in proof construction; this one generates computational/applied problem sequences.

## Instructions

1. **Collect inputs.**
   - Ask: "List the math skills you need to practice. (Be specific — e.g., 'integration by parts,' not just 'integration')"
   - Ask: "For each skill, rate your current fluency: Weak / Developing / Solid"
   - Ask: "How many days until your exam?"
   - Ask: "How long is your practice session today? (in minutes)"
   - Ask: "Have you practiced any of these skills in the last 1–7 days? If yes, which ones?"

2. **Map prerequisite dependencies.**
   Before sequencing, identify which skills have prerequisites:
   - If Skill B requires Skill A, and Skill A is rated Weak → flag Skill A as a prerequisite blocker
   - Display a dependency tree: `Skill A → Skill B → Skill C`
   - For any skill with a Weak-rated prerequisite, move the prerequisite to top priority regardless of exam date

3. **Assign priority and spacing tier to each skill.**

   **Priority rules:**
   - P1 — Weak fluency + foundational/prerequisite + high exam weight → Practice daily
   - P2 — Developing fluency + appears frequently on exam → Practice every 2–3 days
   - P3 — Solid fluency + standalone skill → Practice every 5–7 days (maintenance only)

   **Spacing rules for today's session:**
   - Skills practiced 1–2 days ago: include in today's session (short interval — reinforce before forgetting)
   - Skills practiced 3–5 days ago: include (medium interval — near optimal recall point)
   - Skills practiced 6–7+ days ago: include (long interval — verify retention hasn't decayed)
   - Skills never practiced or last practiced more than 7 days ago: include at Level 1 difficulty first

4. **Build the interleaved problem sequence.**
   - Select problems for each skill at the appropriate difficulty tier (see below)
   - Interleave: no more than 2 consecutive problems from the same skill
   - Place prerequisite skills before the dependent skills within the session
   - Total problems per session: 1 min/problem for routine fluency + 3–5 min/problem for complex problems

   **Difficulty tiers:**
   - **Tier 1 (Routine):** Standard application of the algorithm/formula — confirms the procedure is intact
   - **Tier 2 (Non-routine):** Problem requires one extra step of reasoning — recognizing which form to use, handling a special case, or reformulating the problem
   - **Tier 3 (Integration):** Problem requires combining 2+ skills or applying the skill in an unfamiliar context

   Assign tier based on fluency rating:
   - Weak → Tier 1 first, then 2 if Tier 1 is correct
   - Developing → Tier 2 primarily, with one Tier 3 at the end
   - Solid → Tier 2–3, skip Tier 1 unless the skill hasn't been touched in 7+ days

5. **Generate the complete problem set.**
   Write out every problem fully (no "generate your own" placeholders). Include:
   - The problem statement with all given information
   - Parenthetical notation: `(Skill: [name] | Tier: [1/2/3])`
   - Full worked solution below a separator line

6. **Include session-end performance check.**
   After the set, ask: "Which problems took more than 2× the expected time? Which did you need to peek at the solution for?" These are the skills to move to P1 for the next session.

## Output Format

```
# Math Drill Sequence
Skills: [N] | Session length: N min | Exam: N days away

## Prerequisite Map
[Skill A] → [Skill B] → [Skill C]
⚠ Prerequisite blocker: [Skill A is Weak — drill this before B and C]

## Today's Skill Schedule

| Skill | Fluency | Priority | Last practiced | Today's tier | # Problems |
|---|---|---|---|---|---|
| [Skill name] | Weak | P1 | Never | Tier 1 | 4 |

---

## Problem Set
*(Attempt each without looking at solutions. Time yourself.)*

### Problem 1 — (Skill: [name] | Tier: 1)
[Problem statement]

---
*[Solution below — cover until attempted]*

**Solution:**
[Worked solution]
**Answer:** [Final answer with units if applicable]

---

[Repeat for all problems]

## Session Performance Check
After the set:
- Problems that took 2× expected time: ___
- Problems where I peeked: ___
- Skills to move to P1 next session: ___
```

## Example Output

---

**Input:** 5 skills from a Calculus II course — Integration by parts, Trig substitution, Partial fractions, Sequences and series convergence (ratio test), Taylor series — Fluency: IBP = Developing, Trig sub = Weak, PF = Solid, Ratio test = Developing, Taylor series = Weak — 10 days until final — 45 min session — Last practiced: IBP 2 days ago, PF 5 days ago, nothing else

---

# Math Drill Sequence
Skills: 5 | Session length: 45 min | Exam: 10 days away

## Prerequisite Map

Integration by parts → (standalone)
Trig substitution → (standalone, but requires trig identity recall — flag if trig identities are weak)
Partial fractions → Integration by parts and polynomial long division as prerequisites
Sequences/Series → (standalone)
Taylor series → Derivatives, integration as prerequisites

⚠ **Prerequisite check:**
- Trig substitution: Weak — confirm trig identities (sin²x + cos²x = 1, tan²x + 1 = sec²x, etc.) before drilling
- Taylor series: Weak — confirm derivative fluency before drilling higher-order expansions

---

## Today's Skill Schedule

| Skill | Fluency | Priority | Last practiced | Today's tier | # Problems |
|---|---|---|---|---|---|
| Trig substitution | Weak | P1 | Never | Tier 1 | 3 |
| Integration by parts | Developing | P2 | 2 days ago | Tier 2 | 3 |
| Taylor series | Weak | P1 | Never | Tier 1 | 2 |
| Partial fractions | Solid | P3 | 5 days ago | Tier 2 | 2 |
| Ratio test | Developing | P2 | Never | Tier 2 | 2 |

Total: 12 problems × avg 3.5 min = ~42 min

---

## Problem Set

*(Do not look at solutions. Time each problem. Mark with ⏱ if it takes longer than expected.)*

---

### Problem 1 — (Skill: Trig substitution | Tier 1)

Evaluate: ∫ √(9 − x²) dx

**Hint if needed:** What substitution removes the square root of a difference of squares?

---
**Solution:**
Let x = 3 sin θ → dx = 3 cos θ dθ

√(9 − x²) = √(9 − 9sin²θ) = √(9cos²θ) = 3|cos θ| = 3cos θ (assuming cos θ ≥ 0)

∫ 3cos θ · 3cos θ dθ = 9∫ cos²θ dθ

Using identity: cos²θ = (1 + cos 2θ)/2:
= 9 · [θ/2 + sin 2θ/4] + C
= 9θ/2 + 9sin 2θ/4 + C

Back-substitute: θ = arcsin(x/3), sin 2θ = 2 sin θ cos θ = 2(x/3)(√(9−x²)/3)

**Answer:** (9/2)arcsin(x/3) + (x/2)√(9−x²) + C

---

### Problem 2 — (Skill: Integration by parts | Tier 2)

Evaluate: ∫ x² ln(x) dx

*(Non-routine: requires choosing u and dv correctly — the standard "LIATE" priority does not immediately apply if misremembered)*

---
**Solution:**
Let u = ln x → du = (1/x)dx
Let dv = x² dx → v = x³/3

IBP formula: ∫ u dv = uv − ∫ v du

= (x³/3)ln(x) − ∫ (x³/3)(1/x) dx
= (x³/3)ln(x) − (1/3)∫ x² dx
= (x³/3)ln(x) − (1/3)(x³/3) + C

**Answer:** (x³/3)ln(x) − x³/9 + C

*Why IBP not just a u-substitution? Because the integrand is a product of two fundamentally different function types (algebraic and logarithmic) with no obvious substitution.*

---

### Problem 3 — (Skill: Taylor series | Tier 1)

Write the Taylor series for f(x) = eˣ centered at x = 0, up to and including the x⁴ term.

---
**Solution:**
Taylor series: f(x) = Σ f⁽ⁿ⁾(0)/n! · xⁿ

For eˣ: f⁽ⁿ⁾(x) = eˣ for all n → f⁽ⁿ⁾(0) = 1

eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! + ...

**Answer:** eˣ ≈ 1 + x + x²/2 + x³/6 + x⁴/24 (+ higher order terms)

---

### Problem 4 — (Skill: Trig substitution | Tier 1)

Evaluate: ∫ x/√(x² + 4) dx

*(Note: this looks like trig sub but is actually simpler — test if the learner recognizes when to use u-substitution instead)*

---
**Solution:**
⚠ This is NOT a trig substitution problem despite the square root.

Let u = x² + 4 → du = 2x dx → x dx = du/2

∫ x/√(x² + 4) dx = ∫ (1/√u)(du/2) = (1/2)∫ u^(−1/2) du = (1/2)(2u^(1/2)) + C

**Answer:** √(x² + 4) + C

*The key insight: when the numerator is (close to) the derivative of the expression under the radical, u-substitution is simpler than trig substitution. Trig sub is needed when there is no such relationship.*

---

### Problem 5 — (Skill: Integration by parts | Tier 2)

Evaluate: ∫ eˣ cos(x) dx

*(This requires IBP twice, with a system-of-equations trick at the end)*

---
**Solution:**
Let u = cos x, dv = eˣ dx → du = −sin x dx, v = eˣ

∫ eˣ cos x dx = eˣ cos x + ∫ eˣ sin x dx

Apply IBP again to ∫ eˣ sin x dx:
Let u = sin x, dv = eˣ dx → du = cos x dx, v = eˣ

= eˣ sin x − ∫ eˣ cos x dx

Now: ∫ eˣ cos x dx = eˣ cos x + eˣ sin x − ∫ eˣ cos x dx

2∫ eˣ cos x dx = eˣ cos x + eˣ sin x

**Answer:** ∫ eˣ cos x dx = eˣ(cos x + sin x)/2 + C

---

### Problem 6 — (Skill: Partial fractions | Tier 2)

Evaluate: ∫ (3x + 5)/(x² − x − 2) dx

---
**Solution:**
Factor denominator: x² − x − 2 = (x − 2)(x + 1)

Partial fractions: (3x + 5)/[(x−2)(x+1)] = A/(x−2) + B/(x+1)

3x + 5 = A(x+1) + B(x−2)

x = 2: 11 = 3A → A = 11/3
x = −1: 2 = −3B → B = −2/3

∫ [11/(3(x−2)) − 2/(3(x+1))] dx

**Answer:** (11/3)ln|x−2| − (2/3)ln|x+1| + C

---

### Problem 7 — (Skill: Ratio test | Tier 2)

Determine if the series Σ (n! × 3ⁿ) / nⁿ converges or diverges.

---
**Solution:**
Apply ratio test: L = lim(n→∞) |a_{n+1}/a_n|

a_n = n! × 3ⁿ / nⁿ
a_{n+1} = (n+1)! × 3^(n+1) / (n+1)^(n+1)

|a_{n+1}/a_n| = [(n+1)! × 3^(n+1) / (n+1)^(n+1)] × [nⁿ / (n! × 3ⁿ)]
= (n+1) × 3 × nⁿ / (n+1)^(n+1)
= 3nⁿ / (n+1)ⁿ
= 3 × [n/(n+1)]ⁿ
= 3 × [1/(1 + 1/n)]ⁿ

As n→∞: [1/(1+1/n)]ⁿ → 1/e

L = 3/e ≈ 3/2.718 ≈ 1.10 > 1

**Conclusion:** Series **diverges** (ratio test L > 1)

---

### Problems 8–12

[Additional problems: one Trig substitution Tier 2, one Taylor series Tier 1 for sin(x) centered at 0, one Integration by parts Tier 3 combining with substitution, one Ratio test for a factorial-free series, one Partial fractions with repeated roots at Tier 2]

---

## Session Performance Check

After completing all 12 problems:

1. **Problems that took 2× expected time (>7 min for Tier 2 problems):**
   Write: ___

2. **Problems where I needed to look at the solution before finishing:**
   Write: ___

3. **Skills to move to P1 for tomorrow's session:**
   Write: ___

4. **Key insight from this session:**
   (What did the interleaving reveal about your classification skill? E.g., "I kept confusing u-sub with trig sub")

---

## False-Positive Prevention

**❌ DON'T** sequence all problems from the same skill together, even if "it's more efficient." Blocked practice feels efficient because the previous problem primes the next one — but it does not transfer to exams.

**✅ DO** interleave, even when the learner resists, and explain that the difficulty of interleaving is the training signal — it means the sequencing is working.

**❌ DON'T** drill Tier 3 problems on a Weak-rated skill. Getting complex problems wrong on a skill that isn't consolidated yet causes discouragement and false negative assessments.

**✅ DO** require correct Tier 1 fluency before moving to Tier 2, and Tier 2 fluency before Tier 3.

**❌ DON'T** skip the prerequisite map. A learner who has forgotten partial fraction decomposition will fail integration-by-partial-fractions problems and attribute the failure to integration rather than algebra.

**✅ DO** check prerequisite fluency explicitly before including dependent skills in the drill.

**❌ DON'T** omit the session performance check — this is how spacing intervals get adjusted. Without it, every skill stays at the same interval regardless of performance.

**✅ DO** use time-per-problem and peek-count as objective performance signals, and use them to re-tier skills for the next session.

## Quality Criteria

- [ ] Prerequisite map is shown before the problem set
- [ ] Skills are tiered by fluency rating (Weak = Tier 1 first, Solid = Tier 2–3)
- [ ] No more than 2 consecutive problems from the same skill
- [ ] Prerequisite-blocking skills appear before dependent skills in sequence
- [ ] Every problem is written out in full (no placeholder instructions to "generate a problem")
- [ ] Session performance check is included with specific prompts for re-tiering decisions
- [ ] Total problem count is feasible for the stated session length

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies spaced + interleaved + prerequisite-aware as the three structural constraints — all three must hold, not just one
- **ST-02 (Structured Sequential Instructions):** Six-step process ensures prerequisite map is completed before sequencing
- **ED-02 (Progressive Exercise Generation):** Difficulty tiers (Routine → Non-routine → Integration) are calibrated to fluency rating
- **CM-01 (Explicit Context Framing):** Spacing decisions are grounded in when each skill was last practiced, not arbitrary intervals
- **QA-04 (Uncertainty Acknowledgment):** Session performance check makes the next-session adjustment an explicit decision, not an assumption
