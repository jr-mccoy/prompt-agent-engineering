---
title: "Diagnostic Disclosure Conversation Planner"
category: psychology/diagnostic-formulation
description: "Plan and structure the conversation in which a clinician shares a formal diagnosis with a client, balancing accuracy with the client's emotional readiness and maintaining collaborative agency"
techniques:
  - NE-07
  - CM-01
  - QA-04
  - ST-04
  - DT-02
difficulty: intermediate
intended_use: model-testing
tags:
  - diagnostic-disclosure
  - psychoeducation
  - client-communication
  - therapeutic-alliance
  - shared-decision-making
  - diagnosis-delivery
  - stigma
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_provisional_vs_rule_out_decision_aid.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Diagnostic Disclosure Conversation Planner

## Objective

Structure the clinical conversation in which a diagnosed or provisional diagnosis is shared with a client, in a manner that is accurate, alliance-preserving, non-stigmatizing, and responsive to the client's prior framework and emotional readiness. The planner generates a session arc with clinician talking points, anticipated client reactions, response scripts, and psychoeducation framing options calibrated to the specific diagnosis and client context. Producing these elements does not replace clinician judgment; the clinician adapts the script based on real-time session dynamics.

## When to Use

- Any session in which a confirmed or provisional diagnosis is being formally communicated to a client for the first time
- Re-diagnosis conversations where a prior diagnosis is being revised, added to, or clarified
- High-stakes disclosures: diagnoses with significant stigma burden (e.g., Borderline Personality Disorder, Bipolar I, Schizophrenia spectrum, Antisocial PD, major neurocognitive disorders)
- Disclosures where the client has strongly resisted the diagnostic possibility in prior sessions
- Therapeutic assessment feedback sessions where the disclosure is the planned session purpose
- Training contexts requiring scripted disclosure conversation models

Not appropriate as a substitute for an established clinical relationship. Diagnostic disclosure without sufficient therapeutic alliance is a risk event for alliance rupture, treatment dropout, and client harm.

## Inputs / Context Required

- **Diagnosis being disclosed:** DSM-5-TR name; confirmed vs. provisional `[clinician input required]`
- **Client's prior knowledge/expectation:** does the client expect this diagnosis, partially expect it, or is it likely to be surprising or unwelcome? `[clinician input required]`
- **Prior statements by the client about the diagnosis:** has the client expressed fear, resistance, or specific reactions to this diagnostic label previously? `[clinician input required]`
- **Client's cultural background and relevant identity factors:** cultural relationship to psychiatric diagnosis, stigma context, family belief frameworks `[clinician input required]`
- **Existing therapeutic alliance quality:** well-established, early-stage, or recently disrupted
- **Client's current emotional state and stability:** is the client in an acute phase, or is this a stable window for absorbing a complex disclosure?
- **Relevant support system context:** will the client be alone after the session? Is this their only support? Is a support person present or available?
- **Whether treatment is being proposed alongside disclosure:** disclosure + treatment planning in same session, or disclosure only

## Constraints

### Must
- Open with the client's own framework for their experience before introducing the diagnostic framework — validation precedes label
- Present the diagnosis as an explanatory tool that serves the client, not a fixed judgment or category the client must inhabit
- Distinguish between the diagnosis as a clinical construct and the client as a person — "you have a diagnosis of X" not "you are X"
- Anticipate the most common emotional reactions to this specific diagnosis and prepare response scripts for each: relief, devastation, rejection, numbness, over-identification
- Address the stigma burden associated with the specific diagnosis explicitly, including corrective information where public misconceptions are common
- Include a psychoeducation block that the clinician can offer in accessible language — what the diagnosis means, what it does not mean, and the evidence-based treatment outlook
- Preserve client agency: invite the client's response, question, and disagreement; the diagnostic conversation is a collaboration, not a pronouncement
- Build in a check for safety and support resources at the end: is the client stable to leave? Who will they talk to?
- Include session pacing guidance: when a disclosure is taking longer than expected because of emotional reaction, what to prioritize vs. defer

### Must Not
- Open the conversation with the label — the diagnosis lands better after the client's experience has been named and validated
- Use clinical jargon without translation — every technical term used in the disclosure requires a plain-language equivalent
- Minimize or buffer the diagnosis in a way that is technically accurate but functionally misleading (e.g., "it's just a label for what we're working on" when the diagnosis has real treatment implications)
- Project a specific emotional reaction — some clients are relieved, some are devastated; both responses are valid and neither should be pre-empted by the clinician's framing
- Treat the disclosure session as an information-delivery event — it is a relational event that requires space for the client's response
- Use stigmatizing language or descriptions of the diagnosis that reinforce harmful stereotypes (e.g., describing BPD as "manipulation"; schizophrenia as "split personality"; ADHD as a "character flaw")
- Disclose a diagnosis in a rushed or end-of-session window — disclosure requires sufficient time for the client to respond

## Instructions

1. **Confirm pre-disclosure readiness**:
   - Is the therapeutic alliance sufficiently established to support this disclosure?
   - Is the client's current state stable enough for a complex emotional conversation?
   - Is sufficient session time available (minimum 30 minutes for most disclosures; 45–50 minutes for high-stakes disclosures)?
   - Is the clinician prepared to support an acute emotional reaction if one emerges?
   - If any of the above are not met: flag the disclosure as **not yet ready** and generate a **pre-disclosure preparation plan** instead

2. **Map the diagnosis-specific disclosure landscape**:

   Identify the three most significant features of the diagnosis that will shape the disclosure conversation:
   - **Public misconception(s)** that the client has likely encountered and may need corrected
   - **Potential relief dimension(s)**: what aspects of the diagnosis name and explain experiences the client has been confused or self-blaming about
   - **Stigma burden**: what stigma does this diagnosis carry in the client's cultural and social community; what are the real-world implications (employment, relationships, insurance) the client may ask about
   - **Treatment outlook**: what does the evidence base say about treatability and prognosis for this diagnosis

   Common disclosure landscape profiles:
   - **MDD:** Relief dimension high (explains; not character failure); stigma variable; prognosis strong with treatment; common misconception: "medication will change who I am"
   - **Bipolar I/II:** High emotional impact; relief possible after long diagnostic journey; strong stigma in many communities; prognosis good with mood stabilization; critical to address "does this mean I'll be unwell forever?" and medication misconceptions
   - **PTSD:** Often relief ("there's a name for this and it's not my fault"); moderate public misconception burden; strong evidence base for treatment; address misconception that PTSD means permanent damage
   - **BPD/EUPD:** High stigma burden; common prior negative experiences with providers using this label pejoratively; disclosure requires explicit corrective framing; strong treatment evidence (DBT) should be foregrounded; distinguish from public/online misrepresentation of BPD as "manipulation disorder"
   - **ADHD (adult):** Often relief, especially for adults who struggled without explanation for years; address adult presentation misconceptions; treatment options are concrete; employment and relationship implications to name
   - **Schizophrenia spectrum:** High emotional and stigma weight; media representations are grossly inaccurate; recovery-orientation must be centered; address "dangerousness" misconception explicitly; family implications significant
   - **Personality Disorder (dimensional/AMPD):** Frame as a description of enduring patterns, not a fixed identity; emphasize that personality pathology is responsive to treatment; distinguish from character indictment
   - **Autism Spectrum (adult/late diagnosis):** Often highly meaningful, identity-reorganizing; grief for the undiagnosed years is common; frame as explanation, not diminishment; community and identity resources exist

3. **Build the disclosure session arc**:

   **Opening (5–8 minutes):**
   - Check in with the client's current state before introducing the diagnostic topic
   - Name that today's conversation will involve sharing what the assessment has found
   - Invite the client's sense of readiness: "Before I share what I'm thinking, I want to hear where you are. What's come up for you since we last met?"

   **Validation before label (3–5 minutes):**
   - Reflect and name the client's experience in the client's own language before introducing the clinical framework
   - Example: "What you've described over these weeks — the persistent exhaustion, the loss of the things you used to love, the way even small decisions feel impossible — these are real. Let me share a way of understanding what this is."

   **Diagnosis introduction (3–5 minutes):**
   - Introduce the diagnosis in accessible language, not as a label but as a named clinical picture
   - "What you're describing fits the picture of [diagnosis name] — which is a way of saying that your brain and nervous system have been in a sustained [state / pattern] that has a name, and more importantly, has well-established ways of getting better."
   - Pause after naming. Allow silence. Do not rush to the psychoeducation block.

   **Client response space (open-ended):**
   - "I want to hear what comes up for you hearing that."
   - Be prepared for silence, tears, relief, questions, rejection, or numbness — all are valid
   - Do not fill the silence. Wait.

   **Misconception correction and stigma address (as needed, not scripted — respond to what the client raises):**
   - Have corrective information ready but deliver it in response to the client's reactions, not as a prepared lecture
   - If the client raises a specific misconception or stigma concern, address it directly and factually

   **Psychoeducation block (5–8 minutes, after client response space):**
   - What this diagnosis means: the core clinical picture in plain language
   - What this diagnosis does not mean: address the most common misconceptions
   - What the evidence says about treatment and recovery: prognosis in accessible, hope-preserving language
   - "This diagnosis doesn't define who you are. It describes a pattern that has been affecting you. And there are evidence-based treatments that we know help this."

   **Treatment bridge (3–5 minutes):**
   - Connect the disclosure to next steps
   - Frame treatment as emerging from the diagnosis, not as a separate conversation
   - Invite the client's voice in the treatment direction

   **Session close — safety and support check (3–5 minutes):**
   - "Before we wrap up, I want to check in about how you're doing right now. This was a lot to take in."
   - Assess emotional state
   - Identify who the client can talk to after leaving, if they want to
   - Name that the next session can start with how this landed

4. **Generate anticipated reaction scripts**:

   For each likely client reaction, provide a clinician response scaffold:

   | Reaction | Example Client Statement | Clinician Response Frame |
   |----------|--------------------------|--------------------------|
   | Relief | "I've wondered if this was real for years. Finally having a name for it feels like a relief." | Validate the relief; affirm that the confusion is over; use the relief as an alliance moment for treatment engagement |
   | Devastation / distress | "I don't know what to do with this. This is a lot." | Slow down; no more information; full presence in the emotion; "That makes complete sense. Let's just be here for a moment." |
   | Rejection of diagnosis | "I don't think that fits me. That doesn't sound like me at all." | Curiosity, not argument; "Tell me more about what doesn't fit for you — I want to make sure we're working with something that actually matches your experience." |
   | Over-identification | "So that's why I've always been like this. It's just who I am now." | Gently distinguish diagnosis from identity; "The diagnosis names the pattern — it doesn't determine your future. People's patterns change with the right support." |
   | Stigma concern | "What does this mean for [job / relationship / insurance]?" | Validate the practical concern; provide accurate information; avoid minimizing real implications |
   | Numbness / no reaction | [Silence; minimal response] | Don't fill; offer: "It's okay if this doesn't land all at once. It sometimes takes time." |

5. **Produce session pacing guidance**:
   - If the client goes into an acute emotional crisis after the disclosure: suspend the psychoeducation plan; focus on co-regulation and safety; the disclosure work continues in the next session
   - If time runs short: psychoeducation can be provided in a written resource or deferred; the relational response to the client's reaction is always the priority
   - If the client asks about telling family members: validate the question; explore readiness; offer to support family disclosure if indicated

## Output Format

### Disclosure Readiness Assessment

```
DIAGNOSIS TO BE DISCLOSED: [clinician input required]
DISCLOSURE TYPE: [ ] Confirmed  [ ] Provisional
CLIENT READINESS INDICATORS: [alliance, state, expectations — clinician input]
READINESS ASSESSMENT: [ ] Proceed  [ ] Defer — reason: [clinician input]
SESSION TIME ALLOCATION NEEDED: [30 / 45 / 50 min]
```

---

### Diagnosis-Specific Disclosure Profile

| Feature | Content |
|---------|---------|
| Relief dimension | [what this diagnosis explains that the client may have been confused or self-blaming about] |
| Misconceptions to address | [top 2–3 public misconceptions; corrective language] |
| Stigma burden in this client's context | [cultural/community-specific; practical implications] |
| Treatment outlook | [evidence-based prognosis in accessible language] |

---

### Session Arc Outline

| Phase | Estimated Time | Clinician Talking Points | Watch For |
|-------|---------------|--------------------------|-----------|
| Opening / check-in | [x min] | [script] | [acute distress signals] |
| Validation before label | [x min] | [reflect client's language] | [ensure client feels heard before label is introduced] |
| Diagnosis introduction | [x min] | [accessible language] | [pause after naming; allow response] |
| Client response space | [open] | [hold silence; invitation] | [relief / devastation / rejection / numbness] |
| Misconception correction | [as needed] | [factual; delivered in response, not as lecture] | [stigma concerns; practical questions] |
| Psychoeducation | [x min] | [what it means; what it doesn't; treatment outlook] | [over-identification] |
| Treatment bridge | [x min] | [connect to next steps] | [client voice in treatment direction] |
| Safety and support close | [x min] | [state check; post-session support] | [acute distress; isolation risk] |

---

### Anticipated Reaction Response Scripts

| Anticipated Reaction | Clinician Response |
|---------------------|-------------------|
| Relief | [script] |
| Devastation | [script] |
| Rejection of diagnosis | [script] |
| Over-identification | [script] |
| Stigma / practical concern | [script] |
| Numbness | [script] |

---

### Session Pacing Decision Tree

```
If client enters acute emotional crisis after disclosure:
  → Suspend psychoeducation plan
  → Co-regulation focus
  → Safety check
  → Defer remaining disclosure content to next session

If session time runs short:
  → Relational response to client's reaction is the priority — always
  → Psychoeducation can be offered as written resource or deferred
  → Never rush the client response space to complete the informational agenda

If client asks about disclosure to family or employer:
  → Validate the question
  → Explore the client's readiness and intent
  → Offer to support or plan family disclosure if appropriate
```

---

### Verification Checklist

- [ ] Disclosure readiness assessed before session arc is built — proceed vs. defer decision made
- [ ] Session arc opens with client's own experience before introducing the label
- [ ] Diagnosis is introduced with accessible language, not jargon
- [ ] Sufficient response space built in after the label is named — no information overload immediately following
- [ ] Diagnosis-specific misconceptions and stigma burden identified and addressed
- [ ] Treatment outlook is included and framed with hope-preserving accuracy
- [ ] Client agency is preserved throughout — this is a conversation, not a pronouncement
- [ ] Anticipated reaction response scripts cover the full range of reactions
- [ ] Safety and support check is the session close
- [ ] Output is framed as a planning scaffold; clinician adapts in real-time to session dynamics
