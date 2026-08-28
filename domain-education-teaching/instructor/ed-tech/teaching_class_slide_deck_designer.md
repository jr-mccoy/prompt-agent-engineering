---
title: "Instructional Slide Deck Designer"
category: education-teaching/ed-tech
description: "Design a class slide deck that supports learning rather than substituting for it: cognitive-load-aware slide structure, segmented activities, and a teacher-facing speaker-note layer."
techniques:
  - ST-02
  - CM-02
  - DS-01
  - OC-01
  - QA-01
difficulty: beginner
tags:
  - slide-deck
  - powerpoint
  - google-slides
  - presentation
  - teaching
  - cognitive-load
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/teaching_lesson_plan_generator.md
  - domain-education-teaching/ed-tech/edtech_instructional_video_script.md
  - domain-education-teaching/higher-ed-corporate/hecorp_lecture_to_active_learning_converter.md
---

# Instructional Slide Deck Designer

## Objective

Design an instructional slide deck (K–12, higher-ed, or training) that supports learning rather than substituting for it. Output is a slide-by-slide plan with content slides, activity slides, transition slides, and a teacher-facing speaker-note layer aligned to lesson objectives.

## When to Use

- Teacher or trainer building a deck for a single class period or session
- Replacing a wall-of-text deck that students aren't following
- Designing a deck that another instructor (sub, co-teacher) will use
- Department template slides for a shared course
- Online sync session where the deck is the primary visual

## When NOT to Use

- Async self-paced module — use `hecorp_async_lms_module_designer.md`
- Pure recorded video — use `edtech_instructional_video_script.md`
- Conference talk for adults / pitch deck — different convention; use presentations domain
- Choice board / hyperdoc — use `edtech_choice_board_designer.md`

---

## Inputs Needed

- **Lesson / session topic:** [...]
- **Learning band & population:** [Grade level / role]
- **Session length:** [...]
- **Learning objectives:** [2–4 measurable]
- **Modality:** [In-person / sync online / hybrid]
- **Tool:** [PowerPoint / Google Slides / Keynote / Canva / other]
- **Existing materials:** [Prior deck, textbook, handouts, problem sets]
- **Tech in room:** [Projector, smartboard, student devices, polling tool]
- **Accessibility needs:** [Captions, alt text, color contrast, reading level]

---

## Instructions

### Step 1: Outline From Objectives, Not Content

For each objective, list:

| Objective | Slides needed | Activity slides | Check-for-understanding |
|-----------|---------------|-----------------|--------------------------|
| [LO1] | 2–3 content slides | 1 activity slide | 1 CFU slide |
| [LO2] | ... | ... | ... |

Cap content slides per objective. If you "need" 8 slides for one objective, the lesson is overstuffed.

### Step 2: Apply Cognitive Load Principles

Default rules:

| Rule | Why |
|------|-----|
| One main idea per slide | Working memory limits |
| ≤ ~30 words of text per slide | Slide is signal, not script |
| Image + brief label, not image + paragraph | Avoid redundant text-narration |
| Animations advance content, not decorate | Avoid extraneous load |
| White space is content | Density blocks attention |
| Related items chunked visually | Reduce search load |

### Step 3: Design Slide Types

Use a small set of slide types, not freelance every slide:

| Type | Purpose | Layout pattern |
|------|---------|----------------|
| Title / hook | Open with a question, image, or scenario | Full-bleed image + short prompt |
| Frame | State today's objective + arc | 1 sentence + checklist |
| Activate | Retrieval / prior knowledge prompt | Question + space for student response |
| Concept | Introduce idea with model/visual | Visual primary, text minimal |
| Worked example | Walk through application | Step-by-step reveal |
| Pause / activity | Pair, individual practice, discussion | Big visible prompt + timer space |
| Check for understanding | Quick assessment | One question, response method visible |
| Transition | Mark phase change | Minimal — section header |
| Synthesize / close | What we learned + what's next | Recap + exit ticket prompt |

### Step 4: Sequence the Deck

Default arc for a single session:

```
Slide 1:  Title + hook
Slide 2:  Frame (objective + arc)
Slide 3:  Activate (retrieval)
Slide 4–6: Concept introduction (visual + text)
Slide 7:  Worked example
Slide 8:  Activity / pause
Slide 9:  Debrief / synthesize
Slide 10: Concept extension
Slide 11: Activity / pause
Slide 12: Check for understanding
Slide 13: Synthesize / close + exit ticket
```

Adjust by length and topic. Most sessions need ~10–15 slides; more usually means too much content.

### Step 5: Build Speaker Notes

Speaker notes carry the instruction the slides don't. Include per slide:

- What the teacher says (not the slide text — what the teacher *adds*)
- Question to pose (with anticipated student responses)
- Think-time / wait-time signals
- Transition cue
- Differentiation note (extension or scaffold)
- Time hint (target minute on this slide)

Speaker notes should be readable mid-teaching — short paragraphs, not essays.

### Step 6: Activity Slides Done Right

When the slide signals "now students do something":

- Big, visible prompt (so back-row students can read)
- Timer or time visible
- Response method named ("turn-and-talk" / "write in notebook" / "vote with cards")
- Transition signal (sound, visual, gesture)

A vague activity slide ("Discuss") collapses pair work.

### Step 7: Visual Standards

- Consistent fonts (one body, one display)
- Consistent color palette (3–5 colors, semantic use)
- Consistent slide template
- Images credited and at sufficient resolution
- Avoid stock photo of unrelated people pointing at laptops
- Math: render LaTeX cleanly or use clear handwritten/typed equations
- Text light/dark contrast meets WCAG AA

### Step 8: Accessibility Pass

- [ ] Alt text on every meaningful image
- [ ] Slide reading order set (not visual order)
- [ ] Color is not the sole carrier of meaning
- [ ] Captions on embedded video
- [ ] Font size ≥ 24pt for body, larger for prompts
- [ ] Text contrast verified
- [ ] Slides exportable to PDF for screen-reader users
- [ ] Animations skippable / non-essential

### Step 9: Companion Materials

Decks rarely stand alone. Pair with:

- Student handout / notes scaffold (don't make students copy slides)
- Worksheet for activity slides
- Exit ticket file
- Asynchronous version (if students may need to revisit)

### Step 10: Sub-Friendly Mode (If Needed)

If another instructor may use the deck:
- Speaker notes sufficient for cold delivery
- Materials list at front
- Time targets per slide
- Activity instructions self-contained

### Step 11: Audit Against Lesson Plan

Cross-check:

- [ ] Every objective has slides + an activity + a CFU
- [ ] Time on slides sums to session length minus transitions
- [ ] No slide is the "kitchen sink"
- [ ] Activity-to-content ratio is appropriate for grade band

---

## Output Format

1. Objective-to-slide mapping
2. Cognitive load principles applied (declared)
3. Slide-type plan
4. Slide-by-slide sequence with target time
5. Speaker notes per slide
6. Activity slide details (prompts, timers, response methods)
7. Visual standards spec
8. Accessibility audit
9. Companion materials list
10. Sub-friendly mode (if applicable)
11. Lesson-plan alignment audit

---

## False-Positive Prevention

❌ **DON'T:**
- Treat slides as the lecture script — slides should signal, not narrate
- Use 60-word bullet slides
- Skip speaker notes — instruction lives there
- Forget alt text and contrast
- Make students copy slides — design a scaffold instead
- Build 40 slides for a 50-minute class

✅ **DO:**
- Outline from objectives
- One idea per slide, ≤30 words
- Use a small set of slide types
- Build speaker notes that carry the actual teaching
- Pair the deck with student-facing materials
- Audit against the lesson plan

---

## Quality Indicators

- [ ] 10–15 slides for typical session (more justified)
- [ ] Each objective has content + activity + CFU
- [ ] Speaker notes complete
- [ ] Activity slides fully scoped
- [ ] Accessibility baseline met
- [ ] Visual consistency holds across deck

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Outline → cognitive-load rules → slide types → sequence → notes → accessibility pipeline. |
| **CM-02** | Constrains words-per-slide, slide-count, and slide-type set. |
| **DS-01** | Cognitive-load and instructional-design frame drives slide structure. |
| **OC-01** | Slide-type templates and per-slide field set produce consistent output. |
| **QA-01** | Lesson-plan alignment audit and accessibility pass close the loop. |
