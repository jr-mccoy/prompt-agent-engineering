---
title: "Mandated Reporter Decision Walkthrough (CPS / APS)"
category: psychology/risk-crisis
description: "Walk through a mandated-reporter decision for suspected child abuse or neglect or vulnerable-adult abuse: reasonable-suspicion threshold, jurisdictional rules, what triggers a report vs document-and-monitor, how to make the report, client conversation, and post-report therapy continuity."
techniques:
  - ST-04
  - DT-02
  - RT-05
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - mandated-reporting
  - cps
  - aps
  - reasonable-suspicion
  - duty-to-report
  - post-report-engagement
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
---

# Mandated Reporter Decision Walkthrough (CPS / APS)

## Objective

Produce a structured decision-and-documentation walkthrough for a mandated-reporter decision regarding suspected:

- Child abuse or neglect (physical, sexual, emotional, neglect, exposure to violence) — **CPS**.
- Abuse, neglect, or exploitation of a vulnerable / dependent adult (elder, disabled adult) — **APS**.

The output must:

1. Apply the **reasonable suspicion** threshold (not "proof," not "certainty") used in most U.S. jurisdictions.
2. Walk the clinician through which categories of mandated reporters exist, what counts as suspicion, and what the jurisdiction's rules are (with explicit acknowledgment that statutes vary by state and the clinician must consult their own state's statute or licensing board).
3. Distinguish **must-report** scenarios from **document-and-monitor** scenarios.
4. Give the clinician a script for **how to make the report** — what to gather first, who to call, what to say, what gets documented.
5. Provide a **client-conversation** script for telling the client (when permitted), including timing relative to the report and trauma-informed framing.
6. Build a **post-report therapy continuation plan** focused on the rupture-and-repair work the report often triggers.

This is decision support, not legal advice; the prompt explicitly directs the clinician to consult their state statute, agency policy, and supervisor.

## When to Use

- Suspected child abuse or neglect emerges in session (disclosure by client, observation of injury, third-party allegation, sibling disclosure).
- Suspected abuse, neglect, or exploitation of a vulnerable adult (elder, dependent adult).
- Re-evaluation of a prior decision when new information emerges.
- Pre-emptive walkthrough at supervision when a clinician is uncertain whether a past situation warranted a report.

## Inputs / Context

- Clinician's jurisdiction (state, sometimes county for specifics) and license type; mandated-reporter status confirmed.
- The information that raised concern: who said what, what was observed, when, where; direct disclosure vs third-party report vs observation.
- Identifying information about the alleged victim and alleged perpetrator (when known): age, relationship, current location, current safety.
- Prior reports made (by clinician or others) about this situation, when known.
- Client's status: is the client the alleged victim, alleged perpetrator, parent of alleged victim, or third party?
- Imminence of harm: ongoing exposure, access to the victim, severity, history.
- Agency / employer policy on coordinated reports (some agencies require notification of supervisor and risk management before report; others do not).
- Confidentiality framework explained at intake (informed consent on file).
- Linguistic / cultural context relevant to interpretation (e.g., culturally-bound discipline practices that nonetheless meet legal threshold).

## Constraints

### Must

- Output the following labeled sections in order: **Trigger / Source**, **Jurisdictional Frame**, **Reasonable-Suspicion Threshold Analysis**, **Categorization** (must-report / document-and-monitor / consult-and-decide), **Pre-Report Preparation**, **How to Make the Report**, **Client Conversation Script**, **Post-Report Therapy Continuation Plan**, **Documentation**, **Supervision / Consultation**, **Signatures**.
- Reasonable-suspicion analysis names the specific facts that support or undercut the threshold; does not require certainty or corroboration.
- Categorization identifies must-report situations explicitly (e.g., a child's first-person disclosure of recent sexual abuse with an identified perpetrator typically meets must-report regardless of corroboration).
- Pre-report preparation includes: gather identifying details available, do not delay the report to investigate, document time of decision, notify supervisor / agency per policy.
- How-to-make-the-report includes: hotline number lookup steps (state CPS hotline / APS hotline), what intake will ask (alleged victim, alleged perpetrator, address, relationship, what was observed/heard, prior reports, mandated reporter info), follow-up written report timeline (typically 24–48 h), case number capture.
- Client conversation: when to tell the client (before vs after the call depends on safety), trauma-informed framing, validation, transparency about what was reported and why, what happens next.
- Post-report plan: rupture-and-repair, alliance preservation, therapeutic processing, coordination with CPS/APS worker (with consent), risk management for retaliation.
- Documentation: time of decision, basis (facts supporting reasonable suspicion), report agency, report time, person spoken to, case number, supervisor notification, client conversation timing and content.
- Limits: explicit note that the prompt is decision support, not legal advice, and that the clinician should consult their state statute and licensing board.

### Must Not

- Do not require certainty before reporting; reasonable suspicion is the threshold.
- Do not investigate the alleged abuse beyond what is needed to meet reporting requirements; investigation is the agency's role.
- Do not delay reporting to seek client consent; reporting is mandated regardless of consent.
- Do not promise confidentiality you do not have; the informed consent on file should already make clear that mandated reporting is an exception.
- Do not over-report situations that don't meet threshold (false positives have costs); document the document-and-monitor decision when threshold not met.
- Do not retaliate against client for triggering the report; rupture-and-repair is the therapeutic task.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile trigger / source: who said what, what was observed.
2. State jurisdictional frame: clinician's state, mandated-reporter status, statutes referenced (with disclaimer that statutes vary and clinician should verify).
3. Apply reasonable-suspicion analysis: list facts supporting and undercutting threshold; conclude met / not met.
4. Categorize: must-report / document-and-monitor / consult-and-decide; if consult-and-decide, identify whom (supervisor, agency risk management, state hotline pre-call consultation in some states).
5. Pre-report preparation: gather identifying details available, document time of decision, notify supervisor per policy, do not delay to investigate further.
6. How to make the report: hotline number, intake questions to expect, key facts to communicate, written-report deadline, capture case number.
7. Client conversation script: when to tell, trauma-informed framing, transparency, what happens next.
8. Post-report therapy plan: alliance preservation, processing, coordination with worker, retaliation risk management.
9. Documentation block.
10. Supervision / consultation block.
11. Run verification.

## Output Format

```
=== MANDATED REPORTER DECISION WALKTHROUGH ===

TRIGGER / SOURCE
Date: [YYYY-MM-DD]    Time: [HH:MM]
Source: [Direct client disclosure / clinician observation / third-party report / sibling disclosure / collateral information]
Specifics: [What was said / observed, in client's words where available: "..."]
Alleged victim: [Name, age, relationship to client, current location, current safety]
Alleged perpetrator: [Name, age, relationship, current access to victim]
Prior reports: [Known prior reports — when, by whom, outcome]

JURISDICTIONAL FRAME
State: [...]    County (if relevant): [...]
Clinician licensure: [License type] — mandated reporter status: [Confirmed]
Statute referenced: [State CPS / APS statute citation]
Disclaimer: This walkthrough is decision support; statutes vary by state and the clinician must verify current statute, agency policy, and licensing-board guidance.
Agency policy on pre-report supervisor notification: [Yes / No / Not applicable]

REASONABLE-SUSPICION THRESHOLD ANALYSIS
Facts supporting reasonable suspicion:
- [Fact #1]
- [Fact #2]
- [...]
Facts undercutting reasonable suspicion:
- [Fact #1]
- [...]
Threshold conclusion: [Met / Not met / Uncertain — proceed to consult]

CATEGORIZATION
- [Must-report — specific facts triggering the must-report category]
- [Document-and-monitor — basis for not reporting; specific monitoring plan: what to watch for, when to revisit]
- [Consult-and-decide — supervisor / agency risk management / state hotline pre-call consultation; document consultation and outcome]

PRE-REPORT PREPARATION (if reporting)
- Identifying details available: [Alleged victim full name / age / address / school / parent or guardian; alleged perpetrator full name / address / relationship to victim; current access to victim]
- Notify supervisor / agency: [Per policy — done at HH:MM, by whom]
- Time of decision logged: [HH:MM]
- Investigation: limited to what is needed for the report (do not investigate further)

HOW TO MAKE THE REPORT
- Hotline: [State CPS / APS hotline number — clinician to verify current number]
- Intake will likely ask: alleged victim, alleged perpetrator, addresses, relationship, what was observed/heard, when, where, prior reports, mandated reporter identifying info.
- Key facts to communicate (concise, factual, do not embellish): [...]
- Time of call: [HH:MM]    Person spoken to (intake worker): [Name, ID]
- Case number / report ID: [Capture]
- Written follow-up report: [Required within N hours per state — deadline date/time]

CLIENT CONVERSATION SCRIPT
Timing decision: [Before report (safety-permitting) / immediately after call / at next session — rationale]
Opening: "I have something I have to tell you about today's session that I want you to hear from me directly. I'm a mandated reporter. What you described meets the threshold the state requires me to report, and I have made / am about to make that call to [agency]. I want to be transparent with you about exactly what I reported and what happens next, and I want to keep working with you through this."
Validation: [Specific to client — fear, anger, betrayal, relief; honor whichever]
Transparency: [What was reported; what was not; what the agency does next; that the agency may contact the client / family / school]
Continuity: "We will keep meeting. This doesn't end our work — it changes what we work on for a while."

POST-REPORT THERAPY CONTINUATION PLAN
- Alliance preservation: [Specific repair work; honor anger; don't defend]
- Processing: [Make space for client's reaction across multiple sessions]
- Coordination with CPS/APS worker (with ROI): [Plan for collateral contact]
- Risk management for retaliation: [If alleged perpetrator has access to client; safety planning if applicable]
- Family work: [If client is parent of alleged victim; complex alliance considerations]
- Documentation in chart: [Each post-report session documents the therapeutic work and any coordination]

DOCUMENTATION
- Time of decision: [HH:MM YYYY-MM-DD]
- Facts supporting reasonable suspicion (verbatim where possible)
- Categorization (must-report / document-and-monitor / consulted)
- Report agency: [...]    Hotline number called: [...]    Time of call: [...]    Intake worker: [...]    Case number: [...]
- Supervisor / agency notification: [Time, person]
- Client conversation: [Time, content, response]
- Written follow-up report submission: [Date / Method]
- Subsequent contacts with agency: [Date, person, content]

SUPERVISION / CONSULTATION
- Supervisor consulted: [Name, time]
- Agency risk management: [Name, time]
- Personal liability insurance carrier / licensing board (when uncertain): [If consulted, capture]
- Outcome of consultation: [...]

LIMITS OF THIS WALKTHROUGH
This is decision support. The clinician must verify their current state's statute, agency policy, and licensing-board guidance. Statutes change. When uncertain, the clinician should consult supervisor, agency risk management, or in some states the CPS/APS hotline itself for pre-report consultation.

Clinician: __________________  Date/Time: ___________
Supervisor / consultant: ______  Date/Time: ___________
```

## Verification

- [ ] Trigger / Source documents what was said / observed and source type.
- [ ] Jurisdictional Frame names state, license, statute, disclaimer.
- [ ] Reasonable-suspicion analysis lists supporting and undercutting facts.
- [ ] Categorization explicit (must-report / document-and-monitor / consult-and-decide).
- [ ] Pre-report prep includes supervisor notification per policy and time-of-decision logging.
- [ ] How-to-make-the-report includes hotline, intake questions, written-report deadline, case-number capture.
- [ ] Client conversation script includes timing decision and trauma-informed framing.
- [ ] Post-report therapy plan addresses alliance preservation and retaliation risk if applicable.
- [ ] Documentation block captures all decision and report particulars.
- [ ] Supervision / consultation block present.
- [ ] Limits-of-walkthrough disclaimer present.
- [ ] No demand for certainty; reasonable-suspicion threshold honored.
- [ ] No promise of confidentiality not in scope.
- [ ] Gaps flagged; nothing fabricated.
