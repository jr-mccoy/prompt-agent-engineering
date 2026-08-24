---
title: "Mental Status Exam Compiler"
category: psychology/intake-assessment
description: "Compile a structured, fully descriptive Mental Status Exam from clinician interview observations, avoiding 'WNL' shorthand in favor of observed behavioral anchors."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
  - DS-04
difficulty: intermediate
intended_use: model-testing
tags:
  - mental-status-exam
  - MSE
  - intake
  - clinical-documentation
  - cpt-90791
  - cpt-90792
  - behavioral-observation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
  - domain-psychology/intake-assessment/psychology_psychiatric_history_compiler.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Mental Status Exam Compiler

## Objective

Convert a clinician's raw interview observations into a structurally complete, fully descriptive Mental Status Exam (MSE) that:

1. Covers all nine standard MSE domains in sequential order: Appearance, Behavior/Motor Activity, Attitude, Speech, Mood, Affect, Thought Process, Thought Content, and Cognition/Insight/Judgment.
2. Uses behaviorally anchored, observable language — no "WNL," no unexpanded abbreviations, no inferred internal states presented as observations.
3. Flags domains where clinical data are insufficient to complete the entry, prompting targeted follow-up.
4. Produces an MSE paragraph or structured section ready for direct insertion into a CPT 90791/90792 intake note.

## When to Use

- At intake to compile the MSE section of a biopsychosocial assessment note.
- After any clinical contact where a behavioral observation record needs to be formalized.
- In supervision to model descriptive MSE language vs. evaluative shorthand.
- When a trainee's draft MSE contains "WNL," "unremarkable," or collapsed domains that need expansion.

## Inputs / Context Required

Provide raw interview observations for as many domains as available. Mark any domain as `[not observed / not assessed]` rather than leaving blank — this distinction matters for documentation completeness.

- **Appearance:** Apparent age vs. stated age, grooming/hygiene (hair, nails, clothing cleanliness, odor), dress appropriateness to context/weather, physical condition (weight, posture, distinguishing features if clinically relevant), nutrition status.
- **Behavior / Motor Activity:** Level of cooperation with exam, psychomotor agitation or retardation (quantify if possible: e.g., "unable to remain seated," "movements slowed, 10–15 sec latency between responses"), unusual movements (tremor, tics, dystonia, tardive movements), gait if relevant, eye contact quality.
- **Attitude:** Toward examiner — cooperative, guarded, hostile, suspicious, seductive, dependent, dismissive. Toward the evaluation process.
- **Speech:** Rate (fast/slow/normal), rhythm (pressured, halting, monotone), volume, articulation, spontaneity vs. only prompted responses, latency of response.
- **Mood:** Client's own words for current emotional state (quoted if possible); duration; stability across session.
- **Affect:** Range (full / restricted / blunted / flat), intensity (within-range, heightened, blunted), quality (euthymic, dysphoric, irritable, anxious, euphoric, labile, constricted), congruence with mood and content, mobility (reactive to content changes).
- **Thought Process:** Goal-directedness, linear vs. circumstantial vs. tangential, loose associations, flight of ideas, thought blocking, perseveration, neologisms, clang associations, word salad.
- **Thought Content:** SI (endorsement, plan, intent, means — or denial), HI, NSSI, delusions (type: paranoid, grandiose, referential, somatic, erotomanic), ideas of reference, obsessions, phobias, preoccupations, magical thinking, hallucinations (AH / VH / other — content, frequency, command nature if present), depersonalization/derealization.
- **Cognition:** Orientation (person, place, date, situation), attention (sustained during interview, serial 7s or WORLD backward if administered), recent memory (recall of 3 items at 5 min if tested), remote memory (corroborated personal history recall), fund of information, abstract reasoning (proverb interpretation, similarities), concentration.
- **Insight:** Degree of awareness that symptoms are symptoms of a disorder; understanding of need for treatment; attribution of distress.
- **Judgment:** Hypothetical scenario response (e.g., finding a letter with a stamp), decision-making quality evident in recent life choices.

## Constraints

### Must

- Output all nine MSE domains in the standard sequence; never collapse or merge domains.
- Every descriptive statement must derive from a clinician observation, not an inference or projection; state what was seen or heard.
- Mood must include the client's quoted or paraphrased self-report word(s); affect must be described on four axes: range, intensity, quality, and congruence.
- Thought content must explicitly address SI and HI (even if the statement is "Client denied SI/HI/NSSI on direct questioning" — never leave thought content blank on these items).
- Flag any domain where observations were not collected with `[clinician input required: specific observation needed]`.
- If SI/HI is endorsed, cross-reference the C-SSRS or risk-crisis assessment: `[See Risk Assessment — C-SSRS / detailed risk note]`.
- Use behavioral anchors for motor observations: avoid "agitated" alone; write "unable to remain seated, stood three times during 60-min session, wrung hands continuously."

### Must Not

- Do not write "WNL," "unremarkable," "normal," or "within normal limits" for any domain — describe what was observed.
- Do not attribute thoughts, feelings, or motivations not reported by the client (e.g., "appeared sad about her divorce" when she did not report this).
- Do not omit thought content items for SI/HI under any circumstances.
- Do not use psychiatric jargon without behavioral anchor (e.g., do not write "pressured speech" alone; write "speech rate markedly elevated, talked over examiner twice, required redirection").
- Do not import information from the history section into MSE observations — MSE documents what occurred in the room during this interview.
- Do not fabricate observations; gaps are flagged.

## Instructions

1. **Review inputs domain by domain.** For each domain, confirm whether observation data were provided or whether the domain must be flagged for follow-up.

2. **Translate raw observations to descriptive clinical language.** Convert shorthand (e.g., "slow speech") to a fully anchored statement (e.g., "speech rate markedly decreased, long latency of 5–8 seconds before responding to questions, monotone quality throughout"). Retain the clinician's behavioral anchors; add clinical vocabulary that names the phenomenon.

3. **Compile the Mood domain.** Lead with client's own words in quotation marks, then add descriptive qualifier (e.g., duration, stability).

4. **Compile the Affect domain** on all four axes: range, intensity, quality, congruence.

5. **Compile Thought Process.** Use the standard taxonomy: linear/goal-directed; circumstantial (returns to topic); tangential (does not return); loose associations; flight of ideas; thought blocking; perseveration; neologisms; formal thought disorder.

6. **Compile Thought Content.** Address in order: SI (endorsed/denied with specificity), HI (endorsed/denied), NSSI (endorsed/denied), delusions, ideas of reference, obsessions, hallucinations, depersonalization/derealization, other preoccupations.

7. **Compile Cognition.** Report each sub-domain tested; note which sub-domains were not formally tested with `[not formally tested — grossly intact by history / interview performance]` or similar.

8. **Compile Insight and Judgment** as separate sub-entries within the Cognition section or as a standalone final entry per the clinician's preferred format.

9. **Assemble the complete MSE** in the output format below.

10. **Run verification.**

## Output Format

```
=== MENTAL STATUS EXAM ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
Clinician: [Name, credentials]    CPT: [90791 | 90792]

─────────────────────────────────────────
APPEARANCE
─────────────────────────────────────────
[Apparent age vs. stated age. Grooming and hygiene: describe hair, clothing, odor as observed.
Dress: appropriate/inappropriate to context and season. Distinguishing physical features
if clinically relevant. Nutritional status if observable.]

─────────────────────────────────────────
BEHAVIOR / MOTOR ACTIVITY
─────────────────────────────────────────
[Cooperation level. Psychomotor status: quantified agitation or retardation with behavioral
anchor. Unusual movements with descriptor (tremor: resting/intentional; tics: motor/vocal;
tardive-pattern if relevant). Eye contact: sustained / intermittent / avoided / overly fixed.
Gait if observed.]

─────────────────────────────────────────
ATTITUDE
─────────────────────────────────────────
[Toward examiner and evaluation: cooperative / guarded / hostile / suspicious / seductive /
dependent / dismissive. Behavioral evidence for each descriptor used.]

─────────────────────────────────────────
SPEECH
─────────────────────────────────────────
[Rate: fast / slow / normal — anchor with behavioral example. Rhythm: pressured / halting /
monotone. Volume: normal / elevated / decreased. Articulation: clear / dysarthric / slurred.
Spontaneity: freely spontaneous / only with prompting. Latency of response.]

─────────────────────────────────────────
MOOD
─────────────────────────────────────────
[Client's self-reported mood in own words: "[quoted phrase]." Duration reported by client.
Stability across session.]

─────────────────────────────────────────
AFFECT
─────────────────────────────────────────
Range: [Full / Restricted / Blunted / Flat — describe what was and was not observable].
Intensity: [Within expected range / Heightened / Blunted — anchor with example].
Quality: [Euthymic / Dysphoric / Irritable / Anxious / Euphoric / Labile / Constricted].
Congruence: [Congruent with stated mood and thought content / Incongruent — describe discrepancy].
Mobility: [Reactive to content shifts / Immobile throughout].

─────────────────────────────────────────
THOUGHT PROCESS
─────────────────────────────────────────
[Linear and goal-directed / Circumstantial (returned to topic after digressions) /
Tangential (did not return to topic) / Loose associations / Flight of ideas / Thought blocking
(paused mid-sentence, unable to continue) / Perseveration / Neologisms / Clang associations /
Formal thought disorder. Behavioral anchor for any non-linear finding.]

─────────────────────────────────────────
THOUGHT CONTENT
─────────────────────────────────────────
Suicidal Ideation: [Denied on direct questioning / Endorsed — see Risk Assessment (C-SSRS)].
Homicidal Ideation: [Denied / Endorsed — see Risk Assessment].
NSSI: [Denied / Endorsed — describe urges, recency, method].
Delusions: [None elicited / Describe: type, theme, content, fixed vs. amenable to reason].
Ideas of Reference: [Denied / Endorsed with example].
Obsessions: [None reported / Describe content and associated compulsions].
Hallucinations: [None reported / AH: describe content, frequency, command nature;
VH: describe; tactile/olfactory/other: describe].
Depersonalization / Derealization: [None reported / Describe].
Other preoccupations or notable content: [clinician input required if not addressed].

─────────────────────────────────────────
COGNITION
─────────────────────────────────────────
Orientation: [Person / Place / Date / Situation — state each].
Attention: [Sustained throughout 60-min interview / Lapses — describe / Serial 7s or WORLD
backward if administered: result].
Memory — Recent: [3-item recall at 5 min if tested: X/3 / Not formally tested — grossly intact
by interview performance].
Memory — Remote: [Personal history details consistent with record / Gaps — describe].
Fund of Information: [Commensurate with education / Below expected — example].
Abstract Reasoning: [Proverb / similarities task result if tested / Estimated from interview].
Concentration: [Sustained / Required redirection X times].
Insight: [Full: names symptoms as symptoms, understands need for treatment /
Partial: acknowledges distress but attributes to external cause /
Poor: denies mental health component / Absent — describe].
Judgment: [Intact by interview performance and recent decision history /
Impaired — describe specific evidence].

─────────────────────────────────────────
MSE SUMMARY LINE
─────────────────────────────────────────
[One to three sentence synthesis: most clinically salient MSE findings and their relevance
to diagnostic impression or risk. E.g., "MSE notable for psychomotor retardation, restricted
affect, and passive SI without plan, consistent with moderate depressive episode."]

─────────────────────────────────────────
DOMAINS REQUIRING FOLLOW-UP
─────────────────────────────────────────
[List any domain flagged [clinician input required] with the specific observation needed
and recommended timing (before end of session / next session / as clinically indicated).]
```

## Verification

- [ ] All nine MSE domains present in order: Appearance, Behavior/Motor, Attitude, Speech, Mood, Affect, Thought Process, Thought Content, Cognition (including Insight and Judgment).
- [ ] No domain reads "WNL," "unremarkable," or "within normal limits."
- [ ] Mood includes client's quoted or paraphrased self-report words.
- [ ] Affect is described on four axes: range, intensity, quality, congruence.
- [ ] Thought content explicitly addresses SI and HI — never blank on those items.
- [ ] All descriptors have at least one behavioral anchor (no bare labels like "agitated" or "pressured").
- [ ] Thought process uses standard taxonomy terms with behavioral examples for any non-linear finding.
- [ ] Cognition subsections tested vs. not-formally-tested are distinguished.
- [ ] If SI/HI endorsed, cross-reference to risk assessment is present.
- [ ] Summary line synthesizes most clinically salient findings.
- [ ] Domains missing input are flagged with `[clinician input required: ...]`, not left blank.
- [ ] No observations are imported from history — MSE reflects only what occurred during this interview.
