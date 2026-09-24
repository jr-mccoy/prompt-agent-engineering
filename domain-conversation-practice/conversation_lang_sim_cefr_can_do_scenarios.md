---
title: "Language Sim — CEFR Can-Do Scenarios With Pass / Not Yet / Not Elicited Verdicts"
category: conversation-practice
description: "Pick 2–4 specific CEFR can-do descriptors at a target level, build a role-play scenario for each in which that descriptor is necessary to succeed, write observable pass criteria before the scene, and return a per-descriptor verdict of Pass / Not yet / Not elicited quoting transcript evidence; a self-check against named descriptors and not a certification, distinct from learn_daily_conversation_drill.md (practice with no verdict) and learn_adaptive_input_output_loop.md (teaching cycles)."
techniques:
  - QA-11
  - RT-05
  - CM-03
  - QA-04
difficulty: intermediate
tags:
  - language-learning
  - CEFR
  - can-do-statements
  - speaking-assessment
  - role-play
  - self-assessment
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_lang_sim_master_template.md
  - domain-education-teaching/learner/language/learn_daily_conversation_drill.md
  - domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md
---

# Language Sim — CEFR Can-Do Scenarios

**Objective:** Answer "am I really B1 at speaking?" with evidence rather than a feeling. The learner picks a few specific can-do descriptors. Each one gets a scenario in which the descriptor is *required*, and pass criteria are written *before* the scene. After the scene, each descriptor gets a verdict that quotes what the learner actually said.

**When to Use:**
- You self-assess at a CEFR level and want to test specific claims ("I can deal with most travel situations") rather than the whole level.
- You are preparing for a speaking exam and want to know which functions are secure.
- You finished a course unit and want to check that its can-do goals transfer to unscripted talk.

**Not this prompt if… / distinct from**
- You want relaxed practice with no verdict. Use `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`.
- You want to be taught the missing function. Use `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`, starting from this prompt's *Not yet* lines.
- You need an official level for a job or visa. Take an accredited exam. This is a self-check against paraphrased descriptors, and it says so in its output.
- You want a general scenario with a correction mode and no verdict. Use `conversation_lang_sim_master_template.md` directly.

## Inputs

1. **Target language and variety, L1, target level.**
2. **Descriptors to test (2–4).** Paste them from your course or the CEFR Companion Volume (Council of Europe, 2020), or ask for candidates. Candidates are offered as **paraphrases**, labelled as such, with a note to check the official wording.
3. **Correction mode.** The default is **off** for the scene itself, because assessment works best without interruption. The debrief handles form.
4. **Topics you know well**, so topic knowledge does not mask language ability.

## Method

1. **Scope the test (CM-03).** Confirm the level and 2–4 descriptors. Reject a descriptor that cannot be elicited in text role-play, such as one about following a live TV broadcast, and say why.

2. **Write the pass criteria first (QA-11).** For each descriptor, write 2–3 **observable** behaviours that must appear in the transcript, and one **fail signal**. Show these to the learner *before* the scene. The criteria are fixed once the scene starts.
   - Example: *B1 (paraphrased) — can handle most situations likely to arise when travelling.* Pass: states the problem so the partner can act on it; asks at least one follow-up question; confirms the outcome. Fail signal: switches to L1 to get the problem across.

3. **Build one scenario per descriptor.** Engineer the scenario so the descriptor is **necessary**: the learner cannot finish without the function. Plant one complication that forces it. Paste each scenario into the master template's `[SCENARIO BLOCK]`, with the partner calibrated to the target level.

4. **Run the scenes.** Keep the partner in role, at level. Do not steer the learner toward the criteria. If the scene ends without the function being required, that is the model's fault, and the verdict is *Not elicited*, not *Not yet*.

5. **Judge against the criteria (RT-05).** For each descriptor, give a verdict:
   - **Pass**: every criterion was observed. Quote the line for each one.
   - **Not yet**: the function was required and the learner did not perform it, or needed L1 or HINT to do it. Quote the moment.
   - **Not elicited**: the scene never required it. Re-run with a sharper complication.
   Also give a **confidence** level (QA-04): *High* if each criterion was observed more than once, *Medium* if once, and *Low* if the evidence is borderline.

6. **Form notes, briefly.** Up to 3 form patterns, only where they affected a criterion. Say which pattern cost which verdict.

7. **Next step.** For each *Not yet*, name the one function to practise, and whether to use the adaptive loop or a scenario re-run.

## Output Format

```
# CEFR can-do check — [language], target [level]
Note: descriptors are paraphrased; check them against the official CEFR Companion Volume wording.

## Pass criteria (fixed before the scenes)
| # | Descriptor (paraphrased / as supplied) | Pass criteria | Fail signal |

## Scenes
### Descriptor 1 — scenario: … | planted complication: …
[transcript]

## Verdicts
| # | Verdict | Evidence (quoted) | Confidence |

## Form notes affecting verdicts
- [pattern] → cost [criterion] in descriptor [#]

## Next
- Descriptor [#]: practise [function] via [prompt]
```

## Verification

- [ ] Pass criteria were written and shown before any scene started, and not edited afterwards.
- [ ] Each scenario made its descriptor necessary, with a planted complication.
- [ ] Every Pass cites a quoted line for each criterion.
- [ ] *Not elicited* is used when the scene failed to require the function, and is never counted as a fail.
- [ ] Descriptors are labelled as paraphrased or supplied, with no claim to official wording.
- [ ] The output never states "you are B1". It reports only on the descriptors tested.

## False-Positive Prevention

1. **Level inflation from a friendly partner.** A partner who fills gaps makes every descriptor pass. Hold the partner at level and let misunderstandings happen.
2. **Moving goalposts.** Writing or softening criteria after seeing the transcript. They are fixed before the scene.
3. **Confusing *Not elicited* with *Not yet*.** If the scenario never forced the function, the learner has not failed it.
4. **Quoting CEFR from memory as official.** Wording drifts. Label paraphrases as paraphrases.
5. **Form errors as fails.** A descriptor about handling a situation is passed by handling it. Accuracy counts only where the descriptor names it.
6. **Whole-level verdicts.** Three descriptors do not make a level. Report the descriptors.
7. **Topic masking.** A learner who knows the topic well can pass on content. Choose familiar topics so the language is what is being tested.

## Example Output

```
# CEFR can-do check — German, target B1
Note: descriptors are paraphrased; check them against the official CEFR Companion Volume wording.

## Pass criteria
| # | Descriptor (paraphrased) | Pass criteria | Fail signal |
| 1 | Can handle most travel situations | states the problem actionably; asks ≥1 follow-up; confirms the outcome | switches to English |
| 2 | Can give reasons and explanations for opinions briefly | gives an opinion + ≥2 reasons with "weil/denn"; responds to one challenge | opinion with no reason |

## Scenes
### Descriptor 1 — train cancelled at Köln Hbf; complication: the replacement bus leaves from another exit
### Descriptor 2 — a colleague asks whether the office should move to a four-day week

## Verdicts
| # | Verdict | Evidence | Confidence |
| 1 | Pass | "Mein Zug nach Bonn fällt aus, was kann ich machen?"; "Wo genau ist der Ausgang?"; "Also, Bus um 14:10, Ausgang Nord?" | High |
| 2 | Not yet | Gave opinion + one reason ("weil ich mehr Zeit habe"); when challenged, replied "ja, vielleicht" | Medium |

## Form notes affecting verdicts
- Verb-final after "weil" held; the second reason was abandoned mid-clause → cost criterion 2b

## Next
- Descriptor 2: practise responding to a counter-argument; adaptive loop, then re-run this scene
```

## Techniques Used

- **QA-11 (Pass/Fail Test Harness):** observable criteria fixed before the scene, with three verdict states.
- **RT-05 (Evidence-Based Reasoning):** every verdict quotes the transcript.
- **CM-03 (Scope Definition):** the test is limited to 2–4 named descriptors, and uncheckable ones are rejected.
- **QA-04 (Uncertainty Acknowledgment):** confidence per verdict, paraphrase labels, and no whole-level claims.

## Related Prompts

- `domain-conversation-practice/conversation_lang_sim_master_template.md`: the slots, calibration and commands these scenes run in.
- `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`: low-stakes practice between checks.
- `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`: teach the functions marked *Not yet*.
