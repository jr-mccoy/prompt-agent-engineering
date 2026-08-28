---
title: "Journal Club Teaching Guide Designer"
category: medical-education/educator-curriculum-design
description: "Design journal club session facilitation guides with article critique framework, statistical literacy integration, discussion flow, and clinical application prompts for teaching critical appraisal skills."
techniques:
  - ST-02
  - RT-03
  - CM-02
  - ED-01
  - QA-01
difficulty: intermediate
tags:
  - journal-club
  - critical-appraisal
  - ebm
  - facilitation
  - statistics
  - clinical-education
updated: "2026-05-15"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_small_group_facilitation_guide.md
  - domain-medical-education/teaching-methods/meded_pbl_case_writer.md
  - domain-medical-education/education/medicine_literature_synthesizer.md
---

# Journal Club Teaching Guide Designer

**Objective:** Design a complete, ready-to-run journal club facilitation guide that teaches critical appraisal skills through structured article critique, statistical literacy discussion, and clinical applicability debate—not passive summary and agreement.

## When to Use
- ✅ Program directors, chief residents, or faculty designing a residency or fellowship journal club session
- ✅ Clerkship directors building evidence-based medicine (EBM) teaching into a rotation
- ✅ Medical educators who want to shift journal club from "presenter summarizes, everyone agrees" to active methodological critique
- ✅ Faculty needing a consistent facilitation structure across different article types (RCT, diagnostic study, meta-analysis, cohort, qualitative)
- ❌ Do NOT use to synthesize evidence for a clinical decision—use `medicine_literature_synthesizer.md` for that purpose; this prompt designs the pedagogical session, not the clinical summary
- ❌ Do NOT use when the goal is to brief attendings on a new guideline—journal club as designed here is a teaching format requiring active learner engagement, not a passive update mechanism

## Inputs Required
- **Learner level:** M3 / M4 / Resident PGY-X / Fellow / Faculty development
- **Article citation:** Author, journal, year, title (or PMID)
- **Article type:** RCT / Diagnostic accuracy study / Systematic review or meta-analysis / Cohort study / Qualitative study
- **Session duration:** (e.g., 60 minutes, 90 minutes)
- **Group size:** (e.g., 8-15 residents)
- **Clinical context:** Specialty and the clinical question the article addresses

## Constraints

**Must:**
- Select and apply the article-type-specific critique framework (RCT ≠ diagnostic study ≠ meta-analysis)
- Provide learners with a pre-reading guide containing 5-7 specific methods-and-results focused questions before interpretation
- Include at least one facilitation move that surfaces and corrects a common statistical misconception for the article type
- Include a "So what?" clinical applicability segment that pushes from statistical to clinical significance

**Must Not:**
- Allow the session to function as presenter-summarizes, group-agrees—the facilitation guide must require methodological critique and generate disagreement
- Treat p < 0.05 as equivalent to clinical significance—the guide must explicitly probe: "Is this difference large enough to matter for my patients?"
- Apply the same critique framework to all article types—RCT critique, diagnostic accuracy critique, and qualitative critique require different tools
- Design the session without a pre-reading guide—without focused pre-reading, session becomes passive summary-listening, not active appraisal

## Instructions

### Step 1: Collect Session Inputs
Before generating any content, confirm all six inputs above. If the article type is ambiguous, provide the following brief decision guide:
- "Is there a control group and was treatment assigned?" → RCT
- "Does the study measure sensitivity/specificity or AUC?" → Diagnostic accuracy
- "Is this a pooled analysis of multiple studies?" → Systematic review / meta-analysis
- "Are participants followed over time without randomization?" → Cohort study
- "Does the study use interviews, focus groups, or thematic analysis?" → Qualitative study

### Step 2: Apply the Article-Type-Specific Critique Framework
Select the correct framework based on article type. Present it as the structural backbone for the session.

**RCT Critique Framework:**
| Domain | Key Questions |
|---|---|
| Population (PICO-P) | Who was included/excluded? To whom does this generalize? |
| Randomization | Was allocation truly random? Concealed? |
| Blinding | Who was blinded—patients, providers, outcome assessors? What couldn't be blinded and why does it matter? |
| Allocation concealment | Could researchers predict assignment? |
| Intention-to-treat analysis | Were dropouts analyzed in their original group? |
| Primary outcome | Was it clinically meaningful or a surrogate? Pre-specified? |
| NNT / NNH | What is the number needed to treat (or harm)? Is it clinically actionable? |
| Confidence intervals | What does the CI tell us about precision? Could the true effect be negligible? |

**Diagnostic Accuracy Study Critique Framework (STARD-aligned):**
| Domain | Key Questions |
|---|---|
| Reference standard | Was it the true gold standard or a proxy? Applied to all participants? |
| Spectrum bias | Did the study include the full disease spectrum (mild to severe) or just extreme cases? |
| Sensitivity / Specificity | At what threshold? Who chose the threshold and why? |
| Likelihood ratios | LR+ and LR−—how much does a positive/negative test result shift pre-test probability? |
| Pre-test probability | What is the prevalence in your practice setting vs. the study's? |
| Indeterminate results | What happened to patients with equivocal results? |

**Systematic Review / Meta-Analysis Critique Framework (PRISMA-aligned):**
| Domain | Key Questions |
|---|---|
| Search strategy | Were all relevant databases searched? Was grey literature included? |
| Study selection | Were inclusion/exclusion criteria pre-specified? Any language bias? |
| Heterogeneity | What is I²? Is it acceptable to pool these studies? |
| Publication bias | Was a funnel plot assessed? Egger's test? |
| GRADE evidence quality | What is the overall quality of evidence—high, moderate, low, very low? |
| Direction of effect | Is the summary estimate consistent across subgroups? |

**Cohort Study Critique Framework:**
| Domain | Key Questions |
|---|---|
| Comparability | Were groups comparable at baseline? What confounders were measured? |
| Selection bias | How were participants selected? Who was excluded? |
| Loss to follow-up | What percentage were lost? Could this bias the result? |
| Confounding | Was multivariable adjustment used? What residual confounders might remain? |
| Bradford-Hill criteria | Does the association satisfy temporality, dose-response, biological plausibility? |
| Causation vs. association | Does this design allow causal inference? Why or why not? |

**Qualitative Study Critique Framework:**
| Domain | Key Questions |
|---|---|
| Transferability | To what populations and contexts can findings transfer? |
| Reflexivity | Did the authors acknowledge their own positionality? |
| Member checking | Were findings returned to participants for validation? |
| Saturation | Was data collection continued until no new themes emerged? |
| Trustworthiness | What strategies (triangulation, audit trail, peer debriefing) were used? |
| Clinical relevance | What does this tell us about patient experience that changes how we practice? |

### Step 3: Design the Pre-Reading Guide for Learners
Generate 5-7 questions learners must answer in writing before the session. Questions must focus on methods and results—not conclusions or clinical implications. The goal is to make the presenter's summary redundant before they deliver it.

**Design principle:** If a learner can answer the pre-reading questions without reading the methods section carefully, the questions are too easy. Revise them.

Example pre-reading questions for an RCT on heart failure pharmacotherapy:
1. "What was the primary outcome and how was it defined? Is this outcome clinically meaningful or a surrogate?"
2. "What percentage of participants were lost to follow-up in each group? How were they handled in the analysis?"
3. "Was the study blinded? Who was blinded and who was not? Does this matter for the primary outcome?"
4. "What is the absolute risk reduction for the primary outcome? Calculate the NNT."
5. "What patient populations were explicitly excluded from the trial? Do any of your patients resemble those exclusions?"

### Step 4: Design the Session Facilitation Flow
Structure the session with explicit time allocations. Enforce the time limits.

**Recommended 60-minute structure:**

| Segment | Content | Time |
|---|---|---|
| 1. Presenter summary | Methods + results only. No interpretation. Presenter reads from structured summary, not slides. | 10 min |
| 2. Methods critique | Structured group critique using the article-type framework from Step 2 | 15-20 min |
| 3. Results discussion | Statistical results + statistical literacy discussion prompts (Step 5) | 10-15 min |
| 4. Clinical applicability debate | "Would this change your practice? For whom? With what caveats?" | 10-15 min |
| 5. Synthesis close | One synthesis question + exit ticket | 5 min |

**Presenter briefing:** Tell the presenter explicitly—"Your job is to summarize methods and results, not to tell us what the study means. Stop after results. The group does the interpretation."

**90-minute adaptation:** Add 20 minutes to the methods critique segment and add a 10-minute breakout for small-group critique of one specific methods domain before whole-group discussion.

### Step 5: Generate Statistical Literacy Discussion Prompts
For the article type selected, generate 4-6 pre-written statistical literacy discussion questions. These should surface and correct the most common statistical misconceptions for that study type.

**For RCTs:**
- "The p-value for the primary outcome was 0.03. What does that actually tell us—and what doesn't it tell us?"
- "The relative risk reduction is 25%. What is the absolute risk reduction? Calculate the NNT. Now does it feel the same size?"
- "Look at the confidence interval for the primary outcome. What is the lower bound? Could the true effect be clinically trivial?"
- "The study was stopped early for benefit. How does that affect our estimate of the true effect size?"

**For Diagnostic Accuracy:**
- "The sensitivity is 85%. Does that mean 15% of patients with the disease will be missed? What does this mean in your practice?"
- "The LR+ is 6.5. If your pre-test probability for this condition is 20%, what is your post-test probability after a positive result? (Use Fagan nomogram or Bayes' theorem.)"
- "The study used a threshold of [X]. At a different threshold, sensitivity and specificity would change inversely. Who decided this threshold and why should you care?"

**For Meta-Analysis:**
- "I² is 68%. What does that mean for whether you should trust the pooled estimate?"
- "The funnel plot is asymmetric. What does that suggest and how should it change your interpretation of the summary effect?"
- "The GRADE quality of evidence is 'moderate.' What would push it to 'high' and what would push it to 'low'?"

Include the specific statistical misconception each question is designed to surface, so the facilitator knows what to listen for and how to correct it.

### Step 6: Build the Clinical Applicability Debate Segment
Generate 4 discussion questions that push the group from statistical findings to clinical decision-making. These questions require judgment, values, and local context—not just data reading.

Standard clinical applicability questions (adapt to article content):
1. "Given what we know about the study population, does this result apply to [specific patient type in your practice]? Why or why not?"
2. "The NNT is [X]. What is the number needed to harm for the primary adverse outcome? Given both, how do you counsel a patient?"
3. "Would implementing this intervention change your practice tomorrow? What would need to be true first?"
4. "If your evidence quality is moderate, what would a reasonable clinician do while waiting for better evidence?"

Facilitator note for this segment: This is where the session must generate genuine disagreement. If everyone agrees immediately, the facilitator must introduce a counter-case: "What if your patient is elderly, has renal impairment, and can't afford the medication? Does your answer change?"

### Step 7: Build the Synthesis Close and Exit Activity
**Synthesis question (facilitator-delivered, learner-generated response):**
"In one sentence: what is the one thing from today's critique that will change how you read a [RCT / diagnostic study / meta-analysis] next month?"

**Exit ticket (anonymous, 2 minutes):**
"Write down: (1) the strongest limitation of this study that the presenter didn't mention, and (2) one clinical question you'd need answered before changing your practice based on this article."

Use exit ticket data to open the next journal club session: "Last time, three people mentioned [limitation X]—let's start there today."

### Step 8: Assemble the Complete Facilitation Guide
Compile Steps 1-7 into a single ready-to-use document with:
- Timing master table (facilitator-facing)
- Presenter briefing script (what to say to the presenter before the session)
- Pre-reading guide (learner-facing, distributable separately)
- Session facilitation flow with scripted facilitator language
- Statistical literacy prompts with misconception flags
- Clinical applicability debate questions
- Synthesis close and exit ticket

---

## Worked Example

**Inputs:** PGY2-3 internal medicine residents / RCT: EMPEROR-Reduced (empagliflozin in HFrEF) / 60 minutes / 10 residents

**Presenter Briefing:** "Your summary should cover: study design, primary outcome definition, randomization and blinding, and primary results (absolute numbers, not just relative risk). Stop before interpretation. 10 minutes maximum."

**Pre-Reading Guide (excerpt):**
1. "What was the primary composite endpoint? Is each component individually clinically meaningful or is one a surrogate?"
2. "What was the absolute risk reduction for the primary endpoint? Calculate the NNT for cardiovascular death or HF hospitalization."
3. "Were patients with eGFR < 20 included? How does this affect applying the results to your CKD stage 4 patients with HFrEF?"

**Methods Critique Focus (RCT Framework):**
- Facilitator opens: "Let's start with the primary outcome. Was it pre-specified? How was HF hospitalization defined—and does that definition match how your hospital would capture it?"
- Statistical literacy prompt: "The HR was 0.75 with p < 0.001. What's the ARR? What's the NNT? Now compare those numbers to a statin trial. Does empagliflozin feel bigger or smaller than a statin?"
- Misconception to surface: Relative risk reduction (25%) vs. absolute risk reduction (~5% per year): these are radically different numbers. Which one do you use when counseling a patient?

**Clinical Applicability Debate Trigger:**
"The trial excluded patients with eGFR < 20. If your next HFrEF patient has an eGFR of 18, what do you do?"

**Exit Ticket:** "Name one patient type from your practice this week that would or would not have been enrolled in EMPEROR-Reduced."

---

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Journal club as "presenter summarizes, everyone agrees" | The facilitation guide must require methodological critique before interpretation. If the session can end without anyone naming a limitation, it has failed |
| Treating p < 0.05 as clinical significance | Every facilitation guide for an RCT must include a prompt that explicitly surfaces the relative vs. absolute risk reduction distinction and asks: "Is this difference large enough to matter for my patients?" |
| Same critique framework for all article types | RCT critique requires allocation concealment and ITT analysis; diagnostic accuracy critique requires spectrum bias and likelihood ratios; qualitative critique requires reflexivity and saturation. Using the wrong framework produces superficial critique |
| No pre-reading guide | Without focused pre-reading questions, session time is spent on passive summary listening. Pre-reading makes the presenter's summary confirmatory, not educational—that is the correct goal |
| Facilitator fills silence with their own interpretation | When the facilitator pre-empts the group's critique with their own, the session becomes a lecture with discussion decoration. Hold silence. Use the Socratic probing moves |

## Output Format

**Section 1 — Session Overview**
- Article citation, article type, learner level, group size, duration, clinical context

**Section 2 — Critique Framework**
- Article-type-specific framework table with key questions per domain

**Section 3 — Pre-Reading Guide (Learner-Facing)**
- 5-7 methods-and-results focused questions; distributable as a separate handout

**Section 4 — Presenter Briefing**
- Scripted instructions for the presenting resident (what to cover, what to stop before)

**Section 5 — Session Facilitation Flow**
- Timing table with facilitator scripts for each segment

**Section 6 — Statistical Literacy Discussion Prompts**
- 4-6 pre-written questions with misconception flags for each

**Section 7 — Clinical Applicability Debate Questions**
- 4 discussion questions requiring judgment and local context

**Section 8 — Synthesis Close and Exit Ticket**
- Synthesis question and exit ticket format with instructions for using data next session

## Verification Checklist
- [ ] Article type confirmed and correct critique framework applied (not generic)
- [ ] Pre-reading guide contains 5-7 methods-focused questions (not conclusions-focused)
- [ ] Session facilitation flow explicitly separates presenter summary from group critique
- [ ] At least one statistical literacy prompt addresses relative vs. absolute risk (or equivalent for non-RCT types)
- [ ] Clinical applicability segment contains at least one question that will generate genuine disagreement
- [ ] Facilitator guide contains explicit note: "p < 0.05 ≠ clinical significance—this must be surfaced"
- [ ] Exit ticket is anonymous and brief (< 2 minutes)
