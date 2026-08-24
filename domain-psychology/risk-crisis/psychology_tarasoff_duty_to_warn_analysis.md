---
title: "Tarasoff / Duty-to-Protect Analysis"
category: psychology/risk-crisis
description: "Walk through an identifiable-victim duty-to-protect analysis using a state-by-state aware framework: foreseeability, options (warn, hospitalize, treat differently, notify law enforcement), and documentation standards."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - RT-03
  - RT-05
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - tarasoff
  - duty-to-warn
  - duty-to-protect
  - identifiable-victim
  - foreseeable-harm
  - state-statute
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_homicidal_ideation_triage.md
  - domain-psychology/risk-crisis/psychology_civil_commitment_narrative.md
---

# Tarasoff / Duty-to-Protect Analysis

## Objective

Produce a structured analysis when an identifiable-victim duty-to-protect question arises. The output must:

1. Identify the **state's specific framework**: mandatory duty-to-warn, mandatory duty-to-protect (warn, hospitalize, or take other reasonable steps), permissive duty (no duty but immunity if discharge in good faith), or no statutory duty (with common-law obligation).
2. Apply the canonical four-element test: (a) **identifiable victim**, (b) **serious threat of physical violence**, (c) **foreseeability** of the threat (clinician knew or should have known), (d) **professional standard of care** for action.
3. Generate the **option set** the clinician must consider: warn the victim, warn law enforcement, hospitalize the patient (voluntary or involuntary), intensify outpatient treatment with documentation, contact identified family / supports, combinations.
4. Document the **chosen action**, the **rationale**, the **time of decision**, and the **execution** (calls, warnings, transport).
5. Generate the **client conversation** about the disclosure and the action taken.
6. Anticipate **post-decision risk management**: ongoing risk to victim and to client, repair of alliance if continuing care, coordination with supervisor and risk management, documentation review.

This is decision support, not legal advice; statutes vary materially by state, and the clinician must consult their state statute, licensing board, and risk-management resources.

## When to Use

- During or immediately after a homicidal-ideation triage flagged duty-to-protect criteria.
- After a credible third-party report of threat by client toward an identifiable target.
- After client makes a statement during or between sessions that meets the threshold.
- Pre-emptive walkthrough at supervision when the clinician is uncertain whether prior content triggered duty.

## Inputs / Context

- Linked homicidal-ideation triage: target identifiability, plan, means, intent, history of violence.
- Client's specific statements (verbatim where possible): when, in what context, what was said.
- Identifiable victim: name, relationship, accessibility, prior contact between client and victim, any pattern of approach.
- Means access: firearms, vehicle, weapons, prior violence with similar means.
- Imminence indicators: agitation, intoxication, plan specificity, timeline, recent stressor (loss of relationship, custody, employment, eviction).
- State-of-licensure framework: Tarasoff progeny in this state — duty-to-warn / duty-to-protect / permissive / common law / case law specifics. Clinician must verify current state law.
- Agency policy on duty-to-protect actions and risk-management contact requirements.
- Prior consultation: supervisor, risk management, on-call psychiatry, agency attorney.
- Client's awareness of the framework (from intake informed consent).

## Constraints

### Must

- Output the following labeled sections in order: **Encounter Metadata**, **Source / Statement Documentation**, **State Framework**, **Four-Element Test**, **Option Set Considered**, **Action Selected**, **Execution**, **Client Conversation**, **Post-Decision Risk Management**, **Documentation**, **Supervisor / Risk-Management Consultation**, **Limits and Disclaimer**, **Signatures**.
- Verbatim quotes of the client's statement(s) preserved.
- Four-element test answered explicitly with evidence per element; if any element is unmet, the analysis explains how that affects the duty trigger.
- Option set considered must include at least: warn the victim, notify law enforcement, hospitalize the client (voluntary or involuntary), intensify outpatient treatment with monitored conditions, notify identified supports — plus any state-specific options. Document why each option was selected, modified, or rejected.
- Action selected may be a combination (e.g., warn victim by phone + notify local PD + initiate civil commitment).
- Execution captures time-stamped calls and contacts with content of each communication.
- Client conversation: when (before / after / both / never depending on safety), trauma-informed yet honest framing, transparency about what was disclosed and to whom.
- Post-decision risk management: ongoing victim-safety considerations, retaliation risk against client, alliance repair if continuing care, supervisor coordination, documentation review.
- Disclaimer that statutes vary by state and the clinician must verify current law.

### Must Not

- Do not warn or breach confidentiality without applying the four-element test in writing.
- Do not refuse to act when criteria are met because of fear of confidentiality breach; the duty-to-protect statute or common-law obligation supersedes confidentiality in most jurisdictions when criteria are met.
- Do not delay action when imminence indicators are present.
- Do not warn beyond what is necessary to meet duty (e.g., do not disclose unrelated clinical content to law enforcement).
- Do not assume one state's framework applies in another; the analysis must be state-specific.
- Do not promise the client that no warning will be made when criteria are met.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile encounter metadata.
2. Document source and statement(s), with verbatim quotes and context.
3. State the state framework: mandatory duty-to-warn / mandatory duty-to-protect / permissive / common-law; cite statutory or case-law reference; disclaimer that clinician must verify.
4. Apply the four-element test, evidence per element.
5. Enumerate the option set considered with rationale per option.
6. Select action (single or combination); document rationale tied to the option set.
7. Execute and time-stamp each contact (victim, law enforcement, supports, hospital).
8. Generate client conversation script and document timing.
9. Document post-decision risk management.
10. Document supervisor / risk-management consultation.
11. Append disclaimer.
12. Run verification.

## Output Format

```
=== TARASOFF / DUTY-TO-PROTECT ANALYSIS ===

ENCOUNTER METADATA
Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date: [YYYY-MM-DD]    Time of analysis: [HH:MM]
Setting: [Outpatient / ED / Inpatient / Telehealth]
Clinician: [Name, credentials, license #]
Supervisor / on-call: [Name, credentials]
Agency / risk management contacted: [Name, role, time]

SOURCE / STATEMENT DOCUMENTATION
Source: [Direct in-session statement / between-session communication / collateral report]
Verbatim statement(s): "[exact words; preserve language]"
Context: [What was happening in session; preceding content; affect; intoxication status]
Repetition / specificity: [First time / repeated / increasing specificity]

STATE FRAMEWORK
State of licensure: [...]
Framework: [Mandatory duty-to-warn / Mandatory duty-to-protect / Permissive (immunity if disclose) / No statutory duty (common law)]
Statutory / case-law reference: [...]
Disclaimer: This analysis is decision support; statutes vary and case law evolves. Clinician verifies current state law and agency policy.

FOUR-ELEMENT TEST

(a) Identifiable victim
- Element met: [Yes / No / Class identifiable]
- Evidence: [Named individual / "anyone in my office" identifiable as the office workforce / not identifiable]

(b) Serious threat of physical violence
- Element met: [Yes / No]
- Evidence: [Verbatim threat content; specificity; lethality of stated method]

(c) Foreseeability (clinician knew or should have known)
- Element met: [Yes / No]
- Evidence: [Statement made directly; clinical impression at time; preceding history of violence; means access; intoxication; imminence indicators]

(d) Professional standard of care for action
- Element met: [Yes / No]
- Evidence: [Reasonable clinician standard given the data; consultation reflects standard]

Conclusion: [Duty triggered / Duty not triggered / Uncertain — escalate to supervisor and risk management]

OPTION SET CONSIDERED
1. Warn the identifiable victim directly: [Selected / Modified / Rejected — rationale]
2. Notify law enforcement (with sufficient information to enable protective action): [Selected / Modified / Rejected — rationale]
3. Hospitalize the client voluntarily: [Selected / Modified / Rejected — rationale]
4. Initiate involuntary hold: [Selected / Modified / Rejected — see civil-commitment narrative if selected]
5. Intensify outpatient treatment with monitored conditions (means restriction, increased contact, identified support involvement): [Selected / Modified / Rejected — rationale]
6. Notify identified supports / family with consent: [Selected / Modified / Rejected — rationale]
7. State-specific options: [...]

ACTION SELECTED
[Selected action(s) — single or combination]
Rationale: [Why this combination satisfies the duty while limiting unnecessary disclosure; rejected options rationale]
Decision time: [HH:MM]

EXECUTION
| Time | Action | Recipient | Content (concise, factual) | Outcome |
|------|--------|-----------|----------------------------|---------|
| HH:MM | Phone | [Victim — name] | "[content of warning]" | [Reached / VM / Unreachable] |
| HH:MM | Phone | [Law enforcement agency] | "[content]" | [Officer name; report number] |
| HH:MM | Phone | [On-call psychiatry / ED] | "[content]" | [Outcome] |
| HH:MM | Phone | [Supervisor] | "[content]" | [Documented] |
| HH:MM | Other | [...] | [...] | [...] |

CLIENT CONVERSATION
Timing: [Before / Concurrent with / After action — rationale tied to safety]
Script: "Today you told me [verbatim]. Given what you said, I'm required by [state law / professional standard] to take steps to protect [the named target]. I'm going to / I have [specific actions]. I'm telling you this because I want you to hear it from me. Here's what's going to happen next: [what unfolds]. I want to keep working with you through this — this changes what we focus on for a while, but it doesn't end our work."
Client response: [Affect / agreement / refusal / escalation — observed]

POST-DECISION RISK MANAGEMENT
- Ongoing victim safety: [Specific further actions if any]
- Retaliation risk against client: [Considered; mitigations if applicable]
- Client psychiatric stabilization: [If outpatient continues, density of contact; if hospitalized, coordination plan]
- Alliance repair if continuing care: [Specific repair plan]
- Supervisor follow-up: [Date / time]
- Risk-management debrief: [Date / time]
- Documentation review: [Within 24 h]

DOCUMENTATION
- Linked: homicidal-ideation triage (date), civil-commitment narrative (if applicable, date), progress note (this date).
- Time of decision logged.
- Verbatim statement preserved.
- Each contact with time / recipient / content / outcome captured.
- Action rationale documented.

SUPERVISOR / RISK-MANAGEMENT CONSULTATION
- Pre-action consultation (when time permits): [Yes / No — name, time, content]
- Post-action consultation: [Date / time / content]
- Risk-management or licensing-board guidance: [...]

LIMITS AND DISCLAIMER
This is decision support, not legal advice. Statutory and case-law frameworks vary by state and evolve. The clinician must verify current state law, agency policy, and licensing-board guidance, and consult risk management or legal counsel when uncertain.

SIGNATURES
Clinician: __________________  Date/Time: ___________
Supervisor: ________________  Date/Time: ___________
```

## Verification

- [ ] All labeled sections present and in order.
- [ ] Verbatim client statement preserved.
- [ ] State framework named with statutory / case-law reference and disclaimer.
- [ ] Four-element test answered explicitly with evidence per element.
- [ ] Option set considered includes ≥ 6 options with selection / modification / rejection rationale.
- [ ] Action selected may be a combination; rationale explicit.
- [ ] Execution table time-stamped per contact.
- [ ] Client-conversation script and timing documented.
- [ ] Post-decision risk management addresses victim, retaliation, alliance, supervisor.
- [ ] Documentation block links to homicidal-ideation triage and civil-commitment narrative if applicable.
- [ ] Supervisor / risk-management consultation captured.
- [ ] Disclaimer present.
- [ ] No breach of confidentiality before four-element test applied; no failure to act when criteria met.
- [ ] Gaps flagged; nothing fabricated.
