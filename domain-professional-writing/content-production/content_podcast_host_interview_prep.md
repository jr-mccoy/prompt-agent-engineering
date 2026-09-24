---
title: "Podcast Host Interview Prep — The Question Plan, Follow-Ups, and What You Must Not Get Wrong About the Guest"
category: professional-writing/content-production
description: "Prepare the host side of a podcast or video interview: the episode's goal for this guest, a sourced guest brief built from supplied research, a question plan ordered from warm-up to the hard question with follow-ups for thin answers, facts to confirm with the guest before recording, and a pre-interview checklist — distinct from guest-side media prep (which prepares the person being interviewed) and from person background research (which produces the sourced briefing this prompt consumes)."
techniques:
  - CM-01
  - ST-02
  - RT-05
  - QA-02
  - QA-04
difficulty: intermediate
tags:
  - podcast
  - interviewing
  - question-plan
  - guest-research
  - host-prep
  - content-production
  - what-to-ask
  - interviewing-an-expert
  - fact-check-bio
updated: "2026-09-24"
related_prompts:
  - domain-science/public-engagement/science_media_interview_prep.md
  - domain-business-strategy/go-to-market/research_person_background.md
  - domain-professional-writing/content-production/content_podcast_episode_outline.md
---

# Podcast Host Interview Prep

**Objective:** Walk into the interview knowing what this conversation is for,
what you can say about the guest without being corrected on air, and which
questions will get past the answers they have given everywhere else.

**When to Use:**
- A guest is booked and recording is within days.
- The guest has done many interviews and you want something they haven't said.
- The topic is sensitive or contested and the hard question has to be asked well.

**Not this prompt if:**
- *You* are the guest preparing to be interviewed →
  `domain-science/public-engagement/science_media_interview_prep.md` (message
  map and bridge phrases for the interviewee).
- You need the sourced professional background first →
  `domain-business-strategy/go-to-market/research_person_background.md`. Run it
  first and feed its output in; this prompt does not do open-ended research on
  a person and does not go beyond professional public information.
- You need the whole episode's rundown and show notes →
  `domain-professional-writing/content-production/content_podcast_episode_outline.md`.
- You are designing a qualitative research interview →
  `domain-research-academic/research_interview_guide_designer.md`.

## Inputs

1. **Show and audience**: who listens, what they already know.
2. **Why this guest, now**: the book, launch, news, or story.
3. **Guest research**: the background brief, their recent interviews, their
   own writing — with sources.
4. **Episode length** and how much of it is the interview.
5. **Agreements**: topics the guest asked to avoid, embargoes, approval terms.
6. **The host's own view**, if the show is opinionated.

## Method

1. **Set the interview's job (CM-01).** One sentence: what the listener should
   understand or feel by the end that they couldn't get from the guest's
   last five interviews.
2. **Build the guest brief from sources only (RT-05).** Name, current role,
   the relevant work, 3–5 facts the host will say aloud — each with its source.
   Anything the host will say that is not sourced goes into *Confirm with
   guest* (pronunciation, title, dates, numbers).
3. **Map what they always say.** From their recent interviews, list the stock
   stories and lines. Plan to acknowledge or skip them, not re-elicit them.
4. **Write the question plan (ST-02)** in four movements:
   | Movement | Purpose | Style |
   |---|---|---|
   | Warm-up | Relax, establish voice | Specific, easy, not "tell us about yourself" |
   | Story | Get scenes and turning points | "Take me to the moment when…" |
   | Substance | The ideas, with specifics | "What would someone get wrong about…?" |
   | The hard question | What the audience most wants asked | Direct, fair, sourced; asked once, then a follow-up |
   Each main question gets one follow-up for a thin answer and one for a
   rehearsed answer.
5. **Stress-test the hard question (QA-02).** Is it accurate, fair, and sourced?
   Would the guest recognise the premise? Write the question the guest's
   critics would ask and the one their supporters would ask; ask the one the
   evidence supports.
6. **Mark uncertainty (QA-04).** Where the research conflicts or is thin, the
   question becomes open rather than presumptive.
7. **Pre-interview checklist.** Pronunciations, title, plugs, topics off
   limits, recording setup, consent to record, approval terms.

## Output Format

```
# Interview prep — [guest] on [show], recording [date]
Job of this interview: [one sentence]

## Guest brief (sourced)
| Fact to say aloud | Source |
## Confirm with guest before recording
## What they always say (skip or acknowledge)
## Question plan
| # | Movement | Question | Follow-up if thin | Follow-up if rehearsed |
## The hard question — stress test
Premise · source · critic's version · supporter's version · chosen wording
## Pre-interview checklist
```

## Verification

- [ ] Every fact the host will say aloud has a source or is in *Confirm with guest*.
- [ ] No question re-asks the guest's stock story without a new angle.
- [ ] The hard question's premise is sourced and phrased so the guest can answer it.
- [ ] Topics the guest asked to avoid are respected or the disagreement is flagged to the host.
- [ ] The plan fits the interview time (≈ 3–4 min per main question).
- [ ] Nothing in the brief comes from private or non-professional information.

## False-Positive Prevention

1. **"Tell us about yourself" is not a warm-up; it is a monologue invitation.**
2. **A long preamble is not a question.** Keep each question to one sentence
   the guest can hold in mind.
3. **Double-barrelled questions get the easier half answered.** One ask per question.
4. **Gotcha is not rigour.** A hard question with a premise the host can't
   source damages the show, not the guest.
5. **Do not invent biography.** A wrong title or date said on air is the most
   common host error; confirm instead.
6. **Twenty questions for a 30-minute interview is a list, not a plan.**
   Plan fewer and follow up more.
7. **Don't script the guest's answers.** Anticipate, don't presume.

## Example Output

```
# Interview prep — Dr. Amara Okafor on "Built Environment", recording 2026-10-03
Job: listeners leave understanding why her city's heat-map project changed
where trees were planted — and what it didn't fix.

## Guest brief (sourced)
| Fact to say aloud | Source |
|---|---|
| Urban climate researcher, [university] | Background brief (research_person_background output, 2026-09-20) |
| Led the 2024 street-temperature mapping project | Project report, supplied |
| New book, "Shade" (Oct 2026) | Publisher page, supplied |

## Confirm with guest
Pronunciation of "Okafor" · preferred title (Dr./Professor) · book's exact release date.

## What they always say
The "bus stop at 52°C" story (in 4 of 5 recent interviews) — acknowledge in one line, don't re-elicit.

## Question plan
| # | Movement | Question | If thin | If rehearsed |
|---|---|---|---|---|
| 1 | Warm-up | What were you measuring the first time you carried a sensor down a street? | "What surprised you that day?" | "Not the bus stop — what else?" |
| 2 | Story | Take me to the council meeting where the map was first shown. | "Who spoke first?" | "What did you expect them to say?" |
| 3 | Substance | What would a city planner get wrong reading your map? | "Give me one street." | "Where has that actually happened?" |
| 4 | Substance | Why trees rather than cool roofs in the first round? | "Who made that call?" | "What would you do differently?" |
| 5 | Hard | Residents in two mapped neighbourhoods say planting raised rents. What does your data say about that? | "Is that something the project measured?" | "What would it take to measure it?" |

## Hard question — stress test
Premise: rent concerns raised at a public meeting (minutes supplied, 2025-11).
Critic's version: "Did your project gentrify these streets?" — premise not
supported; causation not shown. Supporter's version: "Isn't rent a separate
issue?" — dodges it. Chosen: #5 as written — sourced, answerable, open.

## Pre-interview checklist
Book plug at close (agreed) · no questions on her current grant bid (asked
to avoid) · remote recording, backup local track · verbal consent on tape.
```

## Techniques Used

- **CM-01 Explicit Context Framing** — the interview's job for this show and audience.
- **ST-02 Structured Sequential Instructions** — warm-up → story → substance → hard question.
- **RT-05 Evidence-Based Reasoning** — every on-air fact sourced or confirmed.
- **QA-02 Adversarial Stress-Test** — critic's and supporter's versions of the hard question.
- **QA-04 Uncertainty Acknowledgment** — open questions where research is thin.

## Related Prompts

- `domain-science/public-engagement/science_media_interview_prep.md` — the guest's side.
- `domain-business-strategy/go-to-market/research_person_background.md` — the sourced background brief.
- `content_podcast_episode_outline.md` — placing the interview in the episode rundown.
