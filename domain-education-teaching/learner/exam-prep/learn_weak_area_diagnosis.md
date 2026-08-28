---
title: "Weak Area Diagnosis and Drill Plan"
category: education-teaching/learner-study-skills
description: "Systematically diagnoses knowledge gaps from quiz scores, self-ratings, or error logs and outputs a ranked weakness map with a targeted drill plan for each gap."
techniques:
  - ST-01
  - ST-03
  - RT-05
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - weakness-diagnosis
  - knowledge-gaps
  - targeted-review
  - exam-prep
  - metacognition
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-study-skills/learnstudy_mistake_log_reviewer.md
  - domain-education-teaching/learner-study-skills/learnstudy_error_correction_cycle.md
  - domain-education-teaching/learner-study-skills/learnstudy_study_next_advisor.md
  - domain-education-teaching/learner-study-skills/learnstudy_confidence_calibration.md
---

## Objective

Turn raw performance data — quiz results, self-ratings, or error logs — into a ranked weakness map with specific, actionable drill plans for each identified gap.

## When to Use

- After a practice test or quiz where score breakdowns are available
- When the learner can self-rate confidence on individual topics
- Before deciding what to study next, when unsure where time will be best spent
- After a real exam to diagnose what to fix before the retake or next exam

**Do not use** as a replacement for actually studying the content — this prompt diagnoses, it does not teach. Follow up with the appropriate drill prompts for each weakness identified.

## Instructions

1. **Collect performance data.**
   Accept any of these input forms:
   - Quiz/test results: topic name + % correct or raw score
   - Self-ratings: topic list with learner-rated confidence (1–5 scale or Low/Medium/High)
   - Error log: list of questions or problems the learner got wrong, with the topic each belongs to
   - Mixed: any combination of the above

   Also ask:
   - "What is the total list of topics covered in this course or exam?" (to detect topics not yet tested — a hidden gap)
   - "When is your exam?"
   - "Which topics are worth the most marks or appear most frequently on exams?"

2. **Classify every topic on three dimensions.**

   **Dimension 1 — Mastery score:** % correct, self-rating mapped to %, or proportion of errors
   - 90–100%: Strong
   - 70–89%: Adequate
   - 50–69%: Shaky
   - 0–49%: Weak

   **Dimension 2 — Exam-weight:** High / Medium / Low (from learner's input or reasonable default)

   **Dimension 3 — Time-sensitivity:** How many days until exam, vs. estimated hours to fix this gap

3. **Compute a priority score for each weak topic.**
   Priority score = (4 − mastery level) × exam-weight multiplier × (1 + time-pressure factor)

   Use these multipliers:
   - Exam-weight: High = 3, Medium = 2, Low = 1
   - Time-pressure factor: ≥14 days = 0 (no urgency), 7–13 days = 0.3, 3–6 days = 0.7, ≤2 days = 1.5

   The formula ensures high-weight, low-mastery, close-deadline topics rank highest.

4. **Output a ranked weakness table.**
   Sort all topics by priority score, highest first.
   Include: Topic | Mastery | Exam Weight | Priority Score | Recommended Action

5. **For the top 3–5 weaknesses, generate a targeted drill plan.**
   Each plan specifies:
   - Root cause hypothesis: why is this topic weak? (conceptual gap, procedural gap, exposure gap, or confusion with similar concept)
   - Recommended resources or approach (e.g., "re-read textbook section X, then do problem set Y")
   - 3–5 specific practice questions or tasks to address the gap directly
   - Success criterion: what does "fixed" look like?
   - Estimated time to reach adequacy (hours)

6. **Flag untested topics.**
   List any topics from the full course topic list that do not appear in the performance data — these are invisible gaps.

7. **State confidence in the diagnosis.**
   Rate confidence: High (if multiple data points per topic), Medium (if self-ratings only), Low (if sparse data).
   Recommend additional data collection if confidence is Low.

## Output Format

```
# Weakness Diagnosis: [Course / Exam Name]
Date: [today] | Exam: [date or days out]

## Data Sources Used
[Brief description of what data was provided]

## Ranked Weakness Map
| Rank | Topic | Mastery | Exam Weight | Priority Score | Action |
|---|---|---|---|---|---|
| 1 | ... | Weak | High | 18 | Drill immediately |
| 2 | ... | Shaky | High | 12 | Drill this week |
| ... | | | | | |

## Untested Topics (Hidden Gaps)
- [Topic X] — never appeared in performance data

## Targeted Drill Plans

### Gap #1: [Topic]
**Root cause hypothesis:** ...
**Approach:** ...
**Practice tasks:**
1. ...
2. ...
3. ...
**Success criterion:** ...
**Estimated time to adequacy:** N hours

[Repeat for top 3–5 gaps]

## Diagnostic Confidence
**Confidence:** [High / Medium / Low]
**Reason:** ...
**If Low:** Recommend [specific data collection step]
```

## Example Output

---

**Input:** Statistics 201 — Practice exam results + learner self-ratings. Exam in 8 days.

Topics + Data:
- Descriptive Statistics: 88% correct (quiz), Medium weight
- Probability Fundamentals: 52% correct (quiz), High weight
- Sampling Distributions: 45% correct (quiz), High weight
- Hypothesis Testing (t-tests): 61% correct (quiz), High weight
- Chi-Square Tests: Self-rated 2/5 confidence, Medium weight
- Regression: Self-rated 4/5, High weight
- ANOVA: Not yet tested (not in practice exam data)

---

# Weakness Diagnosis: Statistics 201
Date: 2026-05-15 | Exam: 2026-05-23 (8 days)

## Data Sources Used
Practice exam quiz results (% correct) for 5 topics and self-ratings (1–5) for 2 topics. ANOVA was identified from the course topic list but did not appear in performance data.

---

## Ranked Weakness Map

| Rank | Topic | Mastery | Exam Weight | Priority Score | Action |
|---|---|---|---|---|---|
| 1 | Sampling Distributions | Weak (45%) | High | 17.0 | **Drill immediately** |
| 2 | Probability Fundamentals | Weak (52%) | High | 15.6 | **Drill immediately** |
| 3 | Hypothesis Testing (t-tests) | Shaky (61%) | High | 10.4 | Drill this week |
| 4 | Chi-Square Tests | Shaky (2/5 ~ 40%) | Medium | 6.8 | Drill after #1–3 |
| 5 | Descriptive Statistics | Adequate (88%) | Medium | 1.2 | Maintenance only |
| 6 | Regression | Adequate (4/5 ~ 80%) | High | 2.6 | Light review |

## Untested Topics (Hidden Gaps)
- **ANOVA** — This topic appeared on the course outline but not in the practice exam. You have no performance data for it. If ANOVA is on the real exam, this is a zero-data blind spot.
  - **Recommended action:** Self-test on ANOVA immediately. Rate your confidence and add it to the priority map.

---

## Targeted Drill Plans

### Gap #1: Sampling Distributions (Mastery: Weak — 45%)

**Root cause hypothesis:** Exposure gap combined with conceptual gap. Students who struggle here typically conflate the population distribution, the sample distribution, and the sampling distribution — three related but distinct concepts. Low score suggests exposure was insufficient (not just a calculation error).

**Approach:**
1. Re-read the sampling distribution concept from the textbook before attempting problems (15 min)
2. Draw the three-distribution diagram by hand for a concrete example
3. Then do problems — starting with identification questions before calculation questions

**Practice tasks:**
1. "Given a population with μ=50, σ=10, and n=25 samples, describe the sampling distribution of the mean: shape, mean, standard error." (Identification + calculation)
2. "A study takes samples of n=100 from a highly skewed population. What does the Central Limit Theorem say about the sampling distribution? What if n=4?" (Conceptual)
3. "A researcher reports SE = 2.0 for samples of size 16. What is the population SD?" (Back-calculate)
4. "Why is the sampling distribution narrower than the population distribution? Explain to someone who has never taken statistics." (Explain-to-teach)
5. "A population is bimodal. What happens to the sampling distribution of the mean as n increases?" (Transfer)

**Success criterion:** Able to explain sampling distributions to a classmate without notes AND correctly solve 4/5 calculation problems with correct SE formula.

**Estimated time to adequacy:** 3–4 hours (1 hour concept review, 2–3 hours problem practice)

---

### Gap #2: Probability Fundamentals (Mastery: Weak — 52%)

**Root cause hypothesis:** Likely procedural gap in applying rules (addition rule, multiplication rule, conditional probability, Bayes) plus confusion between independent and dependent events.

**Approach:** Drill with increasingly complex probability trees. Visual representations help — draw every problem before solving.

**Practice tasks:**
1. "A bag has 3 red, 5 blue balls. You draw two without replacement. What is P(both red)?" (Multiplication, dependent events)
2. "P(A) = 0.4, P(B) = 0.3, P(A∩B) = 0.12. Are A and B independent? Are they mutually exclusive?" (Test both properties)
3. "In a population, 1% have a disease. A test is 95% sensitive and 90% specific. A patient tests positive — what is the probability they actually have the disease?" (Bayes' theorem)
4. "Explain the difference between P(A|B) and P(B|A) using a concrete example." (Conditional probability direction)
5. "Roll two fair dice. What is P(sum > 9 | first die shows 4)?" (Conditional probability calculation)

**Success criterion:** Correctly solve 4/5 conditional probability problems and accurately compute Bayes problems without formula lookup.

**Estimated time to adequacy:** 2–3 hours

---

### Gap #3: Hypothesis Testing — t-tests (Mastery: Shaky — 61%)

**Root cause hypothesis:** Partial understanding — likely knows the procedure but makes errors in test selection (one-sample vs. two-sample vs. paired) or interpretation (especially p-value meaning and what rejecting H₀ actually implies).

**Practice tasks:**
1. "A one-sample t-test yields t=2.35, df=24. Is this significant at α=0.05 (two-tailed)?" (Calculation + table reading)
2. "A researcher claims p=0.03 means there is a 97% chance the alternative hypothesis is true. Is this correct? Explain." (Interpretation error correction)
3. "You have pre-test and post-test scores from the same students. Which t-test do you use and why?" (Test selection)
4. "Two independent groups (n₁=20, n₂=18). What test do you run? State H₀ and H₁ explicitly." (Design identification)
5. "A study fails to reject H₀ with p=0.18. A classmate says 'the null hypothesis is true.' Correct them." (Common misconception)

**Success criterion:** Correctly select test type and interpret results for any scenario without hesitation. Able to articulate what a p-value does and does not mean.

**Estimated time to adequacy:** 2 hours

---

## Diagnostic Confidence

**Confidence:** Medium

**Reason:** Quiz data provides reasonable signal for 5 topics, but self-ratings (Chi-Square, Regression) are less reliable than objective performance data — learners systematically overestimate mastery of topics they have reviewed recently. ANOVA has zero data.

**Recommended next step:** Take a 5-question mini-quiz on Chi-Square and ANOVA before committing to this priority ranking. This will take 20 minutes and significantly improve diagnosis accuracy.

---

## False-Positive Prevention

**❌ DON'T** diagnose a topic as "weak" based on a single question's data — small sample sizes produce unreliable estimates.

**✅ DO** note confidence level in the diagnosis and flag when data is sparse (fewer than 3 questions per topic).

**❌ DON'T** assume all topics in the course have equal exam weight — a "weak" topic that counts for 3% of the exam is less urgent than a "shaky" topic worth 25%.

**✅ DO** always collect or estimate exam weights before ranking priorities.

**❌ DON'T** ignore untested topics just because there is no performance data — absence of data is not evidence of competence.

**✅ DO** explicitly flag topics from the course list that are not represented in the performance data.

**❌ DON'T** generate a generic "study more" recommendation — the drill plan must be specific (exact question types, success criteria, time estimate).

**✅ DO** provide 3–5 targeted practice tasks per gap with a clear success criterion.

## Quality Criteria

- [ ] All provided performance data is used to classify mastery level
- [ ] Priority score accounts for mastery, exam weight, and time to exam
- [ ] Ranked table is complete and sorted
- [ ] Untested topics are flagged separately from ranked topics
- [ ] Drill plans cover the top 3–5 gaps with root cause hypotheses, tasks, success criteria, and time estimates
- [ ] Diagnostic confidence is stated with reasoning
- [ ] Recommendations are specific, not generic

## Techniques Used

- **ST-01 (Clear Objective Statement):** Single-sentence objective distinguishes diagnosis from teaching
- **ST-03 (Output Format Specification):** Ranked table + drill plan format makes output immediately actionable
- **RT-05 (Evidence-Based Reasoning):** Priority scoring is formula-based and grounded in learner-provided performance data
- **QA-01 (Self-Verification):** Verifies that all topics from the course list are accounted for (including untested ones)
- **QA-04 (Uncertainty Acknowledgment):** Diagnostic confidence section explicitly states data quality and its limitations
