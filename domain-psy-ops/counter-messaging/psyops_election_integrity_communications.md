---
title: "Election Integrity Communications — Responding to Election Falsehoods Without Becoming Part of the Contest"
category: psy-ops/counter-messaging
description: "Plan overt, attributed, nonpartisan communication about election processes when false claims are circulating — where to vote, how to vote, how counting works, why results change — under the sharper conditions elections impose: fixed deadlines that cannot be recovered, legal limits on who may say what and when, and a cost of error borne by voters and by trust in the result itself. Process-only by construction; never persuades on candidates, parties, or questions on the ballot."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - elections
  - counter-messaging
  - public-communication
  - nonpartisan
  - voting-rumors
updated: "2026-09-24"
reasoning:
  styles: [procedural, protective, evaluative]
  stakes: critical
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: phased_communication_plan
  user_role: [election_official, communications, civil_society, journalist, trust_and_safety]
  mode: [design, decide, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_prebunking_inoculation_design.md
  - domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md
  - domain-psy-ops/counter-messaging/psyops_debunk_and_correction_design.md
---

# Election Integrity Communications

**Objective:** Plan how to communicate about **election processes** when false or misleading claims about them are circulating — claims about where, when, and how to vote, who is eligible, how ballots are handled and counted, and why results change as counting proceeds. The general counter-messaging prompts apply, but elections sharpen every constraint. **Deadlines are fixed and unrecoverable**: a correction that arrives after polls close cannot give anyone their vote back. **Legal limits are real and vary by jurisdiction**: who may communicate officially, what they may say, and during which periods is often set in law. And **the cost of error is doubled**: a wrong procedural statement from a trusted source disenfranchises people directly, and a correction of it becomes evidence in the next false claim.

The prompt is **process-only by construction**. It helps communicators say true, verifiable things about how the election works. It never helps anyone persuade voters about candidates, parties, or ballot questions, and it never helps anyone discourage participation — both of which are the very behaviors this domain defends against, whoever does them. The same discipline applies to the communicator's own claims: "there was no fraud" is a statement the communicator can rarely support in full during counting, whereas "here are the safeguards, here is what is being reviewed, here is when results are certified" is true and durable.

Every procedural fact comes **from the official election authority** for the jurisdiction. This prompt does not supply dates, deadlines, eligibility rules, or procedures, and none should be supplied from memory by any AI — a confidently wrong election date is the most harmful output this prompt could produce.

**When to use:**
- You communicate for an election authority, a civil-society voter-information group, a newsroom, or a platform, and false process claims are circulating.
- You are preparing before an election and want the prebunks, holding statements, and approval paths in place.
- Results are being counted and claims about the count are spreading faster than results.
- You need to decide whether a specific election rumor warrants a response at all.

**When NOT to use:**
- The claim is not about election processes — use `psyops_rumor_response_triage.md` and `psyops_debunk_and_correction_design.md`.
- You want generic inoculation design outside an election — use `psyops_prebunking_inoculation_design.md`.
- You want to persuade voters on a candidate, party, or ballot question — outside this domain entirely.
- You need legal advice on election law — consult the election authority's counsel or a qualified election lawyer.

**Audience:** Election officials and their communications staff, civil-society voter-information organizations, journalists, and platform trust-and-safety teams.

---

## Inputs / Context

1. **Jurisdiction and phase.** Where, and whether you are before voting, during voting, during counting, or after certification.
2. **Your role and authority.** Official election authority, civil society, newsroom, or platform — each has different standing and different legal limits.
3. **The claims circulating.** Exactly what is being said, where, and at what reach, with the true procedural fact beside each — sourced from the official authority, or marked `[VERIFY]`.
4. **Official procedural facts.** Dates, deadlines, eligibility, locations, methods, counting and certification timelines — each with its official source.
5. **Legal and policy limits.** Rules on official communication, quiet periods, and neutrality for your role, as confirmed by counsel.
6. **Channels and trusted messengers.** Where affected voters actually get information, including languages and accessibility formats.
7. **Approval paths.** Who can approve what, at what hour, on election day and count nights.

---

## Constraints

### Must
- Stay **process-only**: where, when, how, who is eligible, how ballots are handled and counted, and when results are final.
- Source **every procedural fact from the official election authority**, cited in the plan; anything unsourced is `[VERIFY]` and is not published.
- Plan by **phase** — before, during voting, during counting, after certification — since timing constraints differ sharply.
- Prioritize claims that could **prevent eligible people from voting** (wrong dates, places, methods, eligibility) above all others.
- **Prebunk the known counting dynamics** before counting starts: results change as different ballot types are processed, and that is expected — where the official election authority confirms this applies in the jurisdiction.
- Speak with **attribution and on declared channels**, identifying who is speaking.
- Confirm **legal and neutrality limits with counsel** for your role before the period starts, and record what was confirmed.
- Pre-plan **self-correction**: how an error in your own procedural communication will be corrected, by whom, and how fast.

### Must Not
- Persuade on candidates, parties, or ballot questions, or characterize any of them.
- Discourage participation, or suggest voting is pointless, unsafe, or futile.
- State dates, deadlines, locations, eligibility rules, or procedures from memory.
- Declare or project outcomes ahead of the official process.
- Make blanket claims — "no fraud," "completely secure" — that the communicator cannot support; describe safeguards and reviews instead.
- Name private individuals as spreading disinformation, or attribute false claims to a campaign or foreign actor without evidence that meets `psyops_attribution_confidence_assessment.md`.
- Use undisclosed amplification, surrogates, or inauthentic accounts to spread correct information.

---

## Instructions

### Step 1 — Fix jurisdiction, phase, and role
State where, which phase, and who is speaking. Record what your role may and may not say in this phase, as confirmed by counsel.

### Step 2 — Build the official fact sheet
List every procedural fact you may need — dates, deadlines, eligibility, locations, methods, counting and certification timelines — each with its official source. Anything without a source is `[VERIFY]` and unusable until sourced.

### Step 3 — Triage claims by voter harm
Rank circulating claims: first, those that could stop eligible people voting; second, those about how ballots are handled and counted; third, those about the legitimacy of the result. Apply `psyops_rumor_response_triage.md` to decide whether each warrants a response, noting that voter-access falsehoods almost always do.

### Step 4 — Prebunk the predictable
Before voting and before counting, publish plain explanations of what will happen: how to check registration and polling place through official channels, why counts shift as ballot types are processed, when results become official. The explanation must exist before the claim it answers.

### Step 5 — Draft phase-specific holding statements
For each phase, draft a holding statement: what is known, the official source, what is being checked, and when the next update comes. Keep them process-only.

### Step 6 — Plan channels, languages, and messengers
Match each message to where affected voters actually get information, in the languages and accessible formats they use, delivered by messengers they trust — all openly attributed.

### Step 7 — Set approval paths and the self-correction plan
Name who approves what at each hour of election day and count nights, with deputies. Define how an error in your own communication is corrected within the phase that it matters.

### Step 8 — Adversarial check
Take each draft and argue that it is partisan, that it overclaims, or that a correction of it would feed the next false claim. Fix what that reveals, and confirm nothing stated is unsourced.

---

## False-Positive Prevention

1. **Procedure from memory.** A date, deadline, or rule stated without the official source — the most harmful single error available here.
2. **Overclaiming security.** "No fraud" or "completely secure" in place of specific safeguards and reviews, which then fails at the first real irregularity.
3. **Partisan drift.** Language that characterizes a side, a candidate, or a ballot question, which forfeits the trust process communication depends on.
4. **Responding to everything.** Treating every rumor as requiring a response, and amplifying low-reach claims into higher-reach ones.
5. **Late prebunking.** Explaining counting dynamics after the claim about them has spread, when the explanation now reads as an excuse.
6. **Attribution without evidence.** Blaming a campaign or foreign actor for a false claim that ordinary confusion explains.
7. **Treating confusion as malice.** Many people sharing wrong election information believe it and are trying to help others vote.
8. **Uncorrected own errors.** No pre-agreed path for correcting your own mistake inside the window where it matters.

---

## Output Format

```
# Election communications plan — [jurisdiction / election]

## Role, phase, and limits
Speaker: [...] · Phase: [before / voting / counting / after certification]
Legal and neutrality limits (confirmed by counsel on [date]): [...]

## Official fact sheet
| Fact | Official source | Status |
|---|---|---|
| [date / deadline / eligibility / location / method / timeline] | [...] | [sourced / VERIFY — not publishable] |

## Claim triage
| Claim | Reach | Voter-harm tier (1 access / 2 handling / 3 legitimacy) | Respond? | Why |
|---|---|---|---|---|

## Prebunks (published before the claim)
- Registration and polling place: [how to check via official channels]
- Counting dynamics: [why results change as ballot types are processed]
- Certification: [when results become official — sourced]

## Holding statements by phase
| Phase | Statement (process-only, attributed, with next-update time) |
|---|---|

## Channels, languages, messengers
| Audience | Channel | Language / format | Messenger (attributed) |
|---|---|---|---|

## Approval paths
| Decision | Election day | Count night | Deputy |
|---|---|---|---|

## Self-correction plan
[Who decides, how fast, which channel]

## Adversarial check
[Where drafts could read as partisan, overclaim, or feed the next claim — and what was fixed]
```

---

## Verification

- [ ] Every message is process-only.
- [ ] Every procedural fact has an official source; `[VERIFY]` items are not published.
- [ ] Legal and neutrality limits were confirmed with counsel for this role and phase.
- [ ] Claims are triaged with voter-access falsehoods first.
- [ ] Counting dynamics are prebunked before counting begins.
- [ ] Holding statements exist for each phase with a next-update time.
- [ ] Channels, languages, and accessible formats match where affected voters get information.
- [ ] Approval paths and a self-correction plan are defined.
- [ ] No persuasion on candidates, parties, or ballot questions, no discouragement of participation, and no outcome projection appears.
- [ ] No procedure stated from memory, no blanket security claim, no unsupported attribution, and no undisclosed amplification.
