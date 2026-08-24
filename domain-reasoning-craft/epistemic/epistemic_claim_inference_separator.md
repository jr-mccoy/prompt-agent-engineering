---
title: "Claim / Inference Separator — Untangle Observation, Claim, and Inference"
category: reasoning-craft/epistemic
description: "Walk a passage sentence by sentence and tag each unit as pure observation (directly seen/measured), claim (an assertion the author makes), or inference (a conclusion drawn from observations and claims), surfacing where inferences are dressed as observations and where claims are smuggled inside what reads like neutral description. Counters the failure mode of accepting a confident narrative whole because the inferential leaps are hidden inside descriptive prose."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - claim-inference
  - text-analysis
  - critical-reading
  - audit
updated: "2026-05-21"
reasoning:
  styles: [analytical, diagnostic, structural]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: annotated_passage_plus_summary
  user_role: [analyst, researcher, editor, journalist, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_logical_fallacy_scan.md
  - domain-reasoning-craft/reasoning-moves/reasoning_claim_evidence_warrant_audit.md
  - domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md
---

# Claim / Inference Separator

**Objective:** Take a passage and walk it sentence by sentence, tagging each unit as **observation** (something directly seen, measured, or reported as raw fact), **claim** (an assertion the author advances), or **inference** (a conclusion the author draws from observations plus claims). Then surface the two key pathologies: inferences presented as if they were observations, and claims smuggled into sentences that read like neutral description. Output an annotated passage plus a summary of where the load-bearing inferential moves happen. Especially useful for auditing journalism, expert witness statements, incident reports, and persuasive writing where the persuasion lives in the framing.

**When to use:**
- A report or article reads as objective but you suspect its conclusions are baked into the description.
- Auditing testimony, an incident write-up, or a news piece for where fact ends and interpretation begins.
- Reviewing your own writing to check you haven't presented your conclusions as if they were observations.
- Before relying on a source, to separate what it actually witnessed from what it concluded.

**When NOT to use:**
- You need the full argument structure with warrants — use `reasoning_claim_evidence_warrant_audit.md`.
- You're scanning for named logical fallacies — use `epistemic_logical_fallacy_scan.md`.
- The text is explicitly an argument with clearly labeled premises and conclusion; the separation is already done.

**Audience:** Analysts, editors, journalists, researchers, and careful readers who need to know where description stops and interpretation starts.

---

## Inputs / Context

1. **The passage.** Provided verbatim so each sentence can be tagged and quoted.
2. **The author's apparent conclusion.** What the passage seems to be establishing — needed to locate the load-bearing inferences.
3. **Context of production.** Who wrote it, for whom, with what purpose (journalism, testimony, report) — affects where smuggling is likely.
4. **What counts as observation here (optional).** In some domains, instrument readings or recorded data are the only true observations; the user can set the bar.

---

## Definitions

- **Observation:** a directly perceived or measured fact, reported without interpretation ("the meeting started at 9:14"; "the sensor read 412 ppm"). Reproducible by another observer.
- **Claim:** an assertion the author advances that goes beyond raw observation ("the team was unprepared"; "the policy is effective"). Could be true or false; requires support.
- **Inference:** a conclusion derived by reasoning from observations and/or claims ("because attendance dropped, morale must be falling"). The inferential link is the move under audit.

---

## Constraints

### Must
- Tag **each sentence or clause** as observation, claim, or inference (a sentence may contain more than one unit; split it).
- Quote the text being tagged so the reader can check the call.
- Flag **inference-as-observation**: places where a conclusion is written in the grammatical form of a fact ("the obviously rushed rollout" embeds the inference "it was rushed" as description).
- Flag **smuggled claims**: evaluative or interpretive content riding inside apparently neutral description (loaded adjectives, selective detail, presupposition).
- Identify the **load-bearing inferential moves**: the few inferences the conclusion actually depends on.
- Stay **descriptive, not evaluative-of-truth**: the job is to separate the types, not to rule on whether the claims are true.

### Must Not
- Rewrite the passage; annotate it.
- Tag everything as inference because all language involves some interpretation. Reserve "observation" for genuinely raw, reproducible facts and tag the rest honestly.
- Judge whether claims/inferences are *correct* — that's a separate step. Here you separate types and locate the leaps.
- Miss presupposition — content asserted by being assumed ("when did the cover-up start?" presupposes a cover-up).
- Overwhelm with trivial tags; foreground the units that carry the argument.

---

## Instructions

### Step 1 — Restate the apparent conclusion
One sentence. The load-bearing inferences are the ones that support *this*.

### Step 2 — Segment the passage
Break the text into taggable units (sentences or clauses). A sentence mixing fact and interpretation gets split.

### Step 3 — Tag each unit
Assign observation / claim / inference, with a quote. When unsure between claim and inference, ask: is the author *asserting* this (claim) or *deriving* it from something else stated (inference)?

### Step 4 — Flag inference-as-observation
Find units written as description that actually encode a conclusion (loaded modifiers, causal language presented as fact). Mark each and state the embedded inference.

### Step 5 — Flag smuggled claims and presuppositions
Find evaluative content inside neutral-looking prose and anything asserted by presupposition. Quote and name what's being slipped in.

### Step 6 — Trace the load-bearing inferences
List the few inferences the conclusion depends on. For each, name the observations/claims it rests on and whether those are present in the text or assumed.

### Step 7 — Summary
State where the passage is doing its real persuasive work: which inferential leaps carry the conclusion, and how visible they are to a casual reader.

---

## False-Positive Prevention

1. **Everything-is-inference nihilism.** Tagging all language as interpretation because no description is perfectly neutral. Keep a usable bar for observation, or the tool loses its edge.
2. **Truth-judging drift.** Sliding from "this is an inference" into "this inference is wrong." Separation first; correctness is a different prompt.
3. **Missing presupposition.** Only catching explicit claims and missing what's asserted by assumption. Check questions and subordinate clauses for smuggled content.
4. **Loaded-modifier blindness.** Letting "obviously," "rushed," "so-called," "predictably" pass as description. These embed inferences in adjective/adverb form.
5. **Over-tagging trivia.** Annotating every mundane sentence equally. Foreground the units that bear on the conclusion.
6. **Claim/inference confusion.** Tagging a derived conclusion as a bare claim (or vice versa). The test: is it asserted outright, or built from other stated content?
7. **Rewriting instead of annotating.** Producing a "cleaned up" version rather than exposing the structure of the original.
8. **Source-observation overtrust.** Treating a source's report of an event as observation when it's actually the source's inference about the event. Tag what the *text* gives you, noting second-hand reports.

---

## Output Format

```
# Claim / inference separation — [source]

## Apparent conclusion
[One sentence]

## Annotated passage
| # | Quoted unit | Tag (Obs / Claim / Inf) | Note |
|---|-------------|--------------------------|------|
| 1 | "[verbatim]"| Obs                      |      |
| 2 | "[verbatim]"| Inf (as observation)     | embeds: [the hidden inference] |
| 3 | "[verbatim]"| Claim (smuggled)         | loaded term: "[word]" asserts [what] |
| … |             |                          |      |

## Inference-as-observation flags
[List units written as fact that encode a conclusion, with the embedded inference each]

## Smuggled claims / presuppositions
[Evaluative or presupposed content inside neutral-looking prose]

## Load-bearing inferences
| Inference | Rests on (obs/claims) | Present in text or assumed? |
|-----------|------------------------|-----------------------------|
| [the leap]| [what it stands on]    | assumed                     |

## Where the persuasion lives
[Which inferential leaps carry the conclusion and how visible they are to a casual reader]
```

---

## Verification

- [ ] Each unit tagged observation / claim / inference, with a quote.
- [ ] A workable bar for "observation" maintained (not everything tagged inference).
- [ ] Inference-as-observation instances flagged with the embedded inference named.
- [ ] Smuggled claims and presuppositions surfaced with the loaded content quoted.
- [ ] Load-bearing inferences listed with what they rest on and whether it's present or assumed.
- [ ] Analysis separates types without ruling on truth.
- [ ] Annotation, not rewrite.
- [ ] Summary names where the real persuasive work happens.
