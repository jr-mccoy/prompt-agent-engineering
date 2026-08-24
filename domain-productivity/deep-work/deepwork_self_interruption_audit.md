---
title: "Audit Self-Interruption Patterns"
category: productivity/deep-work
description: "Distinguish external interruptions from self-interruptions in a week of focus-block logs and classify each self-interruption into a function (anxiety check, decision avoidance, stimulation, context loss, legitimate capture) so the user sees which pattern dominates and can treat it directly."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - self-interruption
  - focus
  - diagnostics
  - attention
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/deep-work/deepwork_lost_focus_day_troubleshoot.md
  - domain-productivity/deep-work/deepwork_message_triage_system.md
---

# Audit Self-Interruption Patterns

**Objective:** Given a log of interruptions during focus blocks, separate external from self-initiated, then classify every self-interruption into one of five functions. Produce a dominant-pattern finding and one targeted countermove per pattern — not general "stay focused" advice.

**When to use:** When the user suspects they're the main threat to their own focus, when focus parameters (span, recovery) are poor despite a clean calendar, or as follow-up to a calendar audit that ruled out external causes.

**Audience:** An individual auditing themselves. Not a manager studying team behavior.

---

## Inputs Required

1. **A log of ≥ 20 interruptions during focus blocks**, across at least 5 sessions. For each: timestamp, block topic, interruption target (what they switched to), whether triggered by an external cue (notification, person, phone), and one-line "what I was thinking when I switched."
2. **Self-rating per session** on whether the work "wanted to be avoided" — simple 1–5 (5 = I was actively avoiding it).
3. **A note on ambient conditions** for each session: alone/co-located, hungry/fed, rested/tired, any medication or caffeine baseline.
4. **One recent self-interruption the user remembers vividly** — 3 sentences on what pulled them away.

If fewer than 20 interruptions are logged, say so and refuse to classify — the distribution will be noise.

---

## Instructions

1. **Split external vs self-initiated** using the external-cue flag. Report the ratio. If > 50% are external, note this and recommend the user run a triage-system prompt first — self-interruption audit is secondary.

2. **Classify each self-interruption into exactly one function:**
   - **Anxiety check** — opening email/Slack/news without expecting anything specific
   - **Decision avoidance** — switching away when hitting a hard sub-problem
   - **Stimulation-seeking** — tab, video, message for variety (usually in a long block)
   - **Context loss** — forgot what they were doing, went looking for the thread
   - **Legitimate capture** — had a real thought to save elsewhere, meant to return in <60 sec

   Classification evidence must cite the "what I was thinking" field. Do not infer.

3. **Report the distribution and name the dominant function.** If two functions tie, name both.

4. **Cross-check against ambient conditions.** Flag any pattern: "Stimulation-seeking concentrates in tired-late-afternoon sessions" — only if the data supports it.

5. **Provide one targeted countermove per observed function**, not per theoretical function:
   - Anxiety check → a named pre-block action that discharges the anxiety (e.g., 2-min scan of one specific inbox, then close)
   - Decision avoidance → a "name the hard sub-problem out loud before you switch" rule
   - Stimulation-seeking → shorter blocks aligned to attention span
   - Context loss → an end-of-block context note (link to reload-ritual prompt)
   - Legitimate capture → a capture tool inside the work context, not a general inbox

6. **Identify at most one false pattern to unlearn.** Often the user believes their interruptions are "legitimate capture" when they are mostly anxiety check. Name this honestly if the data shows it.

---

## Output Format

```
## Interruption Split
- External: N (N%)
- Self-initiated: N (N%)

## Self-Interruption Distribution
| Function | Count | % of self-initiated |
|---|---|---|
| Anxiety check | ... | ... |
| Decision avoidance | ... | ... |
| Stimulation-seeking | ... | ... |
| Context loss | ... | ... |
| Legitimate capture | ... | ... |

## Dominant Pattern
[function(s)] — N% of self-initiated interruptions
Evidence: [cite 2–3 entries from the log]

## Ambient Correlations (if any)
- [correlation only if data supports it]

## Countermoves (one per observed function)
1. For [function]: [specific countermove]
2. ...

## False Pattern to Unlearn (if any)
- [one specific belief vs. data]

## What Not to Change
- Do not touch patterns below 10% of the distribution. They are noise.
```

---

## Constraints

**Must:**
- Use only the user's supplied log.
- Classify every self-interruption into exactly one function.
- Cite the "what I was thinking" field as evidence for classification.
- Recommend at most one countermove per observed function.

**Must not:**
- Recommend willpower, discipline, or motivation fixes.
- Recommend apps, blockers, or timers (different prompt).
- Tell the user their work is "too hard" or "not engaging enough."
- Pathologize self-interruption. It's a system output, not a character trait.

---

## False-Positive Prevention

- **Legitimate-capture inflation:** The user will self-report many interruptions as legitimate. Check the "what I was thinking" field — if it says "checking" or is vague, it is anxiety check, not capture.
- **Decision-avoidance mislabeling:** A switch during a hard moment is decision avoidance only if the user can name the hard sub-problem they were dodging. If they can't, it's more likely stimulation-seeking.
- **Ambient overclaim:** Correlations between tiredness and interruption need ≥ 3 datapoints at each condition. Do not claim correlation from two sessions.
- **Over-countering:** Five countermoves stack into a new system that itself becomes focus-destructive. Limit to observed functions only.

---

## Self-Verification (before finalizing)

- [ ] External vs self split is computed.
- [ ] Every self-interruption has exactly one function label.
- [ ] Each label cites the log's thought field as evidence.
- [ ] Dominant pattern is named with a percentage.
- [ ] Countermoves exist only for observed (not theoretical) functions.
- [ ] Ambient correlations, if claimed, cite ≥ 3 datapoints per side.
- [ ] No willpower, app, or character-based advice appears.
