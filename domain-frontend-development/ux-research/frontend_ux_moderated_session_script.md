---
title: "Moderated Usability Session Script — The Moderator's Words, Neutral Probes, and What Not to Say"
category: frontend-development/ux-research
description: "Write the word-for-word moderator script for a moderated usability session — welcome and consent, think-aloud instruction with a warm-up, task hand-offs read verbatim, a bank of neutral probes and rescue lines, and a debrief — with every leading, confirming, or teaching phrase replaced; distinct from the study plan (which chooses tasks and metrics) and from qualitative interview guides (which have no tasks)."
techniques:
  - ST-02
  - CM-02
  - NE-04
  - OC-07
  - QA-01
difficulty: intermediate
tags:
  - ux-research
  - usability-testing
  - moderation
  - think-aloud
  - interview-technique
  - session-script
updated: "2026-09-24"
related_prompts:
  - domain-frontend-development/ux-research/frontend_ux_usability_test_plan.md
  - domain-research-academic/research_interview_guide_designer.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
---

# Moderated Usability Session Script

**Objective:** Give the moderator a script they can read aloud that elicits
behaviour and reasoning without steering either — so that a participant's
success or failure is caused by the interface, not by what the moderator said.

**When to Use:**
- A usability test plan exists and sessions are about to be booked.
- More than one person will moderate and sessions must be comparable.
- A previous round was criticised for leading participants ("so you'd click
  Save here, right?").

**Not this prompt if:**
- Tasks, sample, and metrics are not decided yet → `frontend_ux_usability_test_plan.md`.
  This prompt takes the plan's tasks as given and never adds or reorders them.
- You are running open discovery interviews without tasks → `domain-research-academic/research_interview_guide_designer.md`.
- The sessions are unmoderated: write on-screen task text in the plan instead.

## Inputs

1. The approved **task list** with scenarios and success criteria (from the plan).
2. **Session length**, remote or in person, recording tool.
3. **Consent terms**: what is recorded, who sees it, retention.
4. **Prototype limits** and dead ends the moderator must steer around.
5. Any **post-task / post-session questionnaire** (SEQ, SUS, UMUX-Lite).

## Method

1. **Declare the moderator's operating principles (OC-07).** Put these at the
   top of the script, where the moderator re-reads them before every session:
   - Answer questions with a question; the interface must answer, not you.
   - Never name a UI element before the participant does.
   - Silence is data. Count to five before probing.
   - You are testing the design; say so, and mean it.
2. **Write the sequence (ST-02):** welcome → consent → background (2–3
   behavioural questions only) → think-aloud instruction → warm-up task →
   test tasks → post-session questions → debrief → thanks.
3. **Think-aloud instruction plus warm-up.** Instruct, then practise on
   something unrelated to the product (e.g. "find tomorrow's weather on this
   phone") so the habit forms before it matters.
4. **Task hand-offs verbatim.** Read the plan's scenario exactly; give it on a
   card or chat message too; state how the participant signals "done".
5. **Build the neutral probe bank (CM-02).** Each probe must be answerable
   without the moderator's opinion. Constraint: no probe may contain a UI
   label, an adjective of judgement ("confusing", "easy"), or a yes/no frame.
6. **Calibrate with bad/good pairs (NE-04).** For every risky moment
   (participant asks for help; participant is stuck; participant succeeds and
   looks for approval), write what a moderator instinctively says and the
   neutral replacement.
7. **Write the rescue ladder.** Stuck → wait → "What are you looking for?" →
   "Where would you expect to find it?" → declare assist, record as
   *assisted*, move on. Never let a participant fail for more than the time
   limit the plan states.
8. **Self-check (QA-01)** against the Verification list.

## Output Format

```
# Session script — [study]
Moderator principles: [4 lines]

## 1. Welcome & consent (≈3 min) — read aloud
## 2. Background (≈3 min) — questions
## 3. Think-aloud instruction + warm-up (≈3 min)
## 4. Tasks — for each: hand-off text · done signal · time limit · watch-fors
## 5. Probe bank — neutral probes by situation
## 6. Bad → good calibration table
## 7. Rescue ladder
## 8. Post-session questions + questionnaire
## 9. Debrief & thanks
```

## Verification

- [ ] No sentence the moderator reads contains a label shown on the screen under test.
- [ ] Every probe is open-ended (no yes/no, no "would you…?").
- [ ] Task hand-offs match the test plan word for word.
- [ ] A warm-up task precedes the first real task.
- [ ] The rescue ladder ends in a declared, recorded assist.
- [ ] Timings sum to less than the session length, with 5 minutes slack.

## False-Positive Prevention

1. **"Is that what you expected?" is leading.** It supplies the frame of
   expectation. Use "What did you expect to happen?"
2. **Praise is a probe.** "Great!" after success teaches the participant which
   answers you want; use a neutral "Thank you, let's continue."
3. **Explaining the design is scoring your own test.** If the moderator
   explains, the task becomes *assisted*, whatever the participant did next.
4. **Background questions are not a discovery interview.** Keep them to what
   helps interpret behaviour; more belongs in a separate study.
5. **Asking "why" repeatedly produces rationalisation.** Ask about what they
   were looking for or expected, not why they did it.
6. **Do not script reactions to success criteria.** The moderator must not
   reveal the criterion (e.g. "yes, that's the right page").
7. **Silence is not a problem to fix.** Probing within two seconds interrupts
   the very reasoning you want to hear.

## Example Output

Scenario: team-plan checkout study (tasks from the matching test plan).

```
# Session script — Team-plan checkout, prototype v4
Moderator principles: answer with a question · never name a UI element first ·
count to five before probing · we are testing the design, not you.

## 1. Welcome & consent (3 min)
"Thanks for joining. We're testing a design for buying extra seats, and we
want to see where it works and where it doesn't. Nothing you do today can be
wrong — if something is hard, that's the design's problem, and exactly what we
need to know. With your permission I'll record the screen and audio; only the
research team sees it, and it's deleted after 90 days. Is that OK?"

## 2. Background (3 min)
- "Tell me about the last time you changed the number of paid seats on a tool."
- "Who else was involved in paying for it?"

## 3. Think-aloud + warm-up (3 min)
"As you work, please say what you're looking at, what you're trying to do, and
what you expect to happen — like narrating to someone who can't see your screen.
Let's practise: open a weather site and find tomorrow's forecast for your city."

## 4. Tasks
T1 hand-off (read verbatim, also pasted in chat): "Your team has grown to 12
people. Get everyone access this month." Done signal: "Tell me when you think
you're finished." Limit: 6 min. Watch-for: does the seat control get noticed
before scrolling?
T2 hand-off: "Before you pay, tell me what you'll be charged today and why."
Limit: 4 min. Watch-for: reading of the proration line.
T3 hand-off: "Your finance team needs a bill they can pay by transfer."
Limit: 4 min.

## 5. Probe bank
Hesitation: "What are you looking for right now?"
After a click: "What did you expect to happen?"
Reads silently: "What's going through your mind?"
Says "done": "What tells you that you're finished?"

## 6. Calibration
| Instinct (bad) | Neutral (good) |
|---|---|
| "Try the seat dropdown." | "Where would you expect to change that?" |
| "Great, that's right!" | "Thank you. Let's move on." |
| "Does the proration make sense?" | "In your own words, what is this charge?" |
| "Why did you click that?" | "What were you hoping that would do?" |

## 7. Rescue ladder
Wait 5 s → "What are you looking for?" → "Where would you expect to find it?"
→ at 6 min: "Let's say we found it — I'll show you" — log T1 as ASSISTED.

## 8. Post-session
UMUX-Lite (2 items, read as written). Then: "What, if anything, would you want
to change before using this for real?"

## 9. Debrief
"That's everything. You helped us see two places the design needs work. Your
$75 incentive arrives by email within 3 days. Any questions for me?"
```

## Techniques Used

- **ST-02 Structured Sequential Instructions** — a fixed session order every moderator follows.
- **CM-02 Constraint Specification** — rules that every probe must satisfy.
- **NE-04 Good vs Bad Example Calibration** — instinctive vs neutral phrasing pairs.
- **OC-07 Operating Principles Declaration** — the moderator's four principles up front.
- **QA-01 Self-Verification** — leading-language and timing checks before use.

## Related Prompts

- `frontend_ux_usability_test_plan.md` — where the tasks and metrics come from.
- `domain-research-academic/research_interview_guide_designer.md` — task-free qualitative interviews.
- `frontend_ux_usability_findings_severity_log.md` — logging what the sessions reveal.
