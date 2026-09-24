---
title: "Behavioral Interview Story Bank — Eight True Stories Mapped to the Competencies You Will Be Asked About"
category: personal-development/job-search
description: "Build a reusable bank of eight to twelve true work stories for behavioral interviews in any field: each drafted in situation–task–action–result form with the candidate's own part isolated, mapped to the competencies the target postings screen for, stress-tested against the follow-up questions interviewers actually ask, and checked for coverage gaps — so answers are prepared from real episodes rather than improvised or embellished."
techniques:
  - ST-02
  - ST-46
  - RT-05
  - QA-02
  - DD-02
difficulty: intermediate
tags:
  - job-search
  - interview-prep
  - behavioral-interview
  - star-method
  - competencies
  - candidate
  - interview-coming-up
  - answer-interview-questions
  - past-work-examples
updated: "2026-09-24"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_ml_interview_prep.md
  - domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md
  - domain-personal-development/job-search/jobsearch_pipeline_tracker_and_cadence.md
---

# Behavioral Interview Story Bank

**Objective:** Produce a bank of eight to twelve true stories, each in a
tight situation–task–action–result shape with the candidate's own actions
isolated, mapped to the competencies the target role screens for, with
prepared answers to the likely follow-ups and a coverage table showing which
competencies still lack a story.

**When to Use:**
- You have interviews coming and freeze on "tell me about a time when…".
- Your answers run long, drift into "we", or end without a result.
- You keep telling the same two stories for every question.
- **Not this prompt if** you are preparing for an ML technical interview —
  `domain-AI-ML/learning-ai-ml/mllearn_ml_interview_prep.md` coaches concepts,
  coding and statistics for ML roles only. This prompt covers the behavioral
  round for any role family and does no technical quizzing.
- **Not this prompt if** you are designing an interview loop as the employer;
  that is `domain-hr-management/hiring/hr_interview_loop_design.md`.

## Inputs / Context

**Required:**
1. **Two or three target postings** (or the fit decoder output) — the source
   of the competencies.
2. **Raw episodes**: 12–20 moments from the last five years, one or two lines
   each — a conflict, a failure, a deadline, a decision with thin data, a time
   you changed someone's mind, a time you were wrong. Rough is fine.
3. **Interview format if known**: panel, one-to-one, recorded video, and
   typical answer length expected.

**Optional:**
- The company's published values or leadership principles, if they interview
  against them.
- Feedback from past interviews.

## Method

1. **Extract the competency list (ST-02).** From the postings, list the six to
   ten competencies the role will screen for, in the postings' own words
   (e.g. "influence without authority", "prioritise under ambiguity"). Always
   add the four near-universal prompts: a failure, a conflict, a
   disagreement with a manager, and "why are you leaving".

2. **Select episodes.** For each raw episode, note which competencies it
   could evidence. Keep the eight to twelve that together cover the list with
   the least overlap and the most recent, relevant scope. Drop episodes where
   the candidate's role was marginal.

3. **Draft each story in STAR, result-weighted (ST-46).**
   - **Situation** — one or two sentences; just enough to make the stakes
     clear.
   - **Task** — what the candidate specifically was responsible for.
   - **Action** — three to five concrete steps *the candidate* took, in "I",
     including one judgment call and why.
   - **Result** — what changed, with a figure where one is known, and what the
     candidate learned or would do differently.
   Target: 90–120 seconds spoken, about 200–250 words. Action should be the
   longest part.

4. **Isolate the candidate's part (DD-02, RT-05).** Every "we" is rewritten as
   what the candidate did, or flagged as a team action the candidate should
   say plainly was a team action. Every figure in a result is marked
   **checked** (the candidate can source it) or **approximate** (say
   "roughly" when telling it). No figure is supplied that the candidate did
   not give.

5. **Stress-test each story (QA-02).** Write the three follow-ups a skeptical
   interviewer would ask: "What would you do differently?", "What did your
   manager think?", "What was the hardest trade-off?", "How do you know it
   was your action that caused the result?". Draft a one-to-two-sentence true
   answer to each. A story that cannot survive its follow-ups is demoted.

6. **Build the coverage table.** Competencies down, stories across. Mark the
   primary story and a backup for each competency. Any competency with no
   story is a gap: either find a new episode or prepare an honest shorter
   answer.

7. **Prepare the failure and the "why leaving" answers with care.** The
   failure story must be a real failure with a real consequence, owned
   without blaming others. "Why leaving" is forward-looking and does not
   criticise the current employer.

## Output Format

```
# Story bank — [candidate], for [target family]

## Competencies screened
1. [competency — source posting]

## Stories
### S1 — [short memorable label]
Competencies: [primary], [secondary]
S: [...]
T: [...]
A: 1. [...] 2. [...] 3. [...]
R: [...] {checked / approximate}
Follow-ups:
- Q: [...] → A: [...]
Spoken length: ~[n] sec

## Coverage
| Competency | Primary story | Backup | Gap? |

## Gaps and plan
- [competency] — [find episode / prepared short answer]
```

## Verification

- [ ] Every competency comes from a posting or from the four universal prompts.
- [ ] Every Action section is in "I", with team actions labelled as such.
- [ ] Every figure is marked checked or approximate, and none was invented.
- [ ] Every story has three follow-ups with true answers.
- [ ] Every competency has a primary and a backup story, or is listed as a gap.
- [ ] Each story fits 90–120 seconds spoken.
- [ ] The failure story names a real consequence and the candidate's ownership.

## False-Positive Prevention

1. **A well-structured story can still be the team's story.** STAR shape with
   "we" throughout tells the interviewer nothing about the candidate. The
   Action section must survive "and what did *you* do?".
2. **A failure that is a disguised strength is not a failure.** "I work too
   hard" or a failure that was someone else's fault fails the question, and
   interviewers recognise it.
3. **A dramatic story is not a relevant one.** The most exciting episode may
   evidence a competency the role does not screen for. Map to the list.
4. **More stories is not more coverage.** Twelve stories that all show
   "delivered under deadline" leave conflict and influence uncovered. Use the
   coverage table.
5. **A rehearsed answer that ignores the question fails.** Stories are raw
   material; the candidate must be able to lead with the part the question
   asks about, not recite from the top.
6. **Precision you cannot back is a liability.** "Increased retention 23.4%"
   invites "how was that measured?". Say "roughly a quarter" if that is what
   is known.
7. **Embellishment compounds under follow-up.** A story improved beyond what
   happened will fail at the second follow-up; the prompt drafts only what the
   candidate confirms.

## Example Output

```
# Story bank — Leo M., for Program / project management (construction tech)

## Competencies screened
1. Keeps cross-functional work on schedule — posting A
2. Influence without authority — posting A, B
3. Prioritise under ambiguity — posting B
4. Communicates risk early — posting B
5–8. Failure; conflict; disagreeing with a manager; why leaving (universal)

## Stories
### S3 — "The permit slip"
Competencies: communicates risk early (primary), influence without authority (secondary)
S: A 40-unit residential job; the city permit review was running three weeks behind, and framing crews were booked.
T: I was the project coordinator responsible for the schedule and the weekly owner update.
A: 1. I rebuilt the look-ahead to show which trades could start without the permit (site utilities, off-site prefabrication). 2. I told the owner's rep in the Monday update, before the superintendent had agreed, because the booking deadline was Wednesday. 3. I set up a 15-minute call with the super and the framing sub to move their start by two weeks instead of cancelling. 4. I called the permit office twice a week and logged each answer in the update.
R: The framing sub held the crew for the new date; the job lost about 8 working days instead of 15 {approximate — from the revised schedule}. I'd now raise permit risk at the 60% design stage, not after submission.
Follow-ups:
- Q: What did the superintendent think of you going to the owner first? → A: He was annoyed; I apologised for the order, not the content, and we agreed I'd give him 24 hours' notice next time.
- Q: How do you know the re-sequencing saved the days? → A: The original schedule and the revised one both exist; the difference is the trades that started early.
- Q: What was the hardest trade-off? → A: Telling the owner before I had a fix, versus waiting and missing the booking deadline.
Spoken length: ~110 sec

## Coverage
| Competency | Primary | Backup | Gap? |
|---|---|---|---|
| On schedule | S1 | S3 | — |
| Influence | S5 | S3 | — |
| Ambiguity | S2 | — | backup missing |
| Risk early | S3 | S6 | — |
| Failure | S7 | — | backup missing |
| Conflict | S4 | S3 (follow-up) | — |
| Disagree with manager | S8 | — | backup missing |
| Why leaving | prepared answer | — | — |

## Gaps and plan
- Ambiguity backup — candidate recalls a scope change on the clinic fit-out; draft as S9.
- Failure backup — prepare one; do not reuse S7 in the same loop.
```

## Techniques Used

- **ST-02 Structured Sequential Instructions** — competencies, selection, drafting, testing, coverage in order.
- **ST-46 Assertion-Evidence Structure** — result-weighted STAR with the action as the evidence.
- **RT-05 Evidence-Based Reasoning** — figures marked checked or approximate.
- **QA-02 Adversarial Stress-Test** — each story attacked with the follow-ups interviewers ask.
- **DD-02 Vague-to-Concrete Translation** — "we" and adjectives become the candidate's specific actions.

## Related Prompts

- `domain-AI-ML/learning-ai-ml/mllearn_ml_interview_prep.md` — technical prep for ML roles; pair with this for the behavioral round.
- `domain-personal-development/job-search/jobsearch_job_posting_fit_decoder.md` — the competency source.
- `domain-personal-development/job-search/jobsearch_pipeline_tracker_and_cadence.md` — log which stories were used in which loop.
