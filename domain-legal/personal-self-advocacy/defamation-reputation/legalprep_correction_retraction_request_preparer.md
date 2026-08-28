---
title: "Correction / Retraction Request Preparer — Draft Your Own Plain Request to the Publisher"
category: legalprep
description: "[SELF-SUBMIT] Help a person draft their OWN plain, factual, first-person request to the person or outlet that published a statement, asking for a correction or retraction and stating factually what is inaccurate. Produces a neutral request the user sends themselves — NOT a legal cease-and-desist or demand. Does NOT make legal threats, cite statutes, claim damages, or conclude anything is defamation; any legal demand routes to an attorney. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - NE-25
  - ST-02
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - defamation
  - reputation
  - correction-request
  - retraction
  - self-submit
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_defamation_concern_documentation_organizer.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_content_removal_platform_report.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_reputation_harm_impact_log.md
  - domain-legal/ip/legal_defamation_publicity_risk_screen.md
---

**Purpose:** Help you draft your **own** plain, factual request to the person or outlet that published a statement about you, asking them to **correct or retract** it and stating, factually, what is inaccurate. The output is a neutral first-person message **you** send yourself — a normal request from one person to another, not a legal document. It states what was published, what specifically is inaccurate, the fact that supports your version, and what you are asking them to do. It does **not** make legal threats, cite statutes, claim damages, or conclude that anything "is defamation" — **any legal demand or cease-and-desist routes to an attorney**, and a legal threat sent yourself can backfire.

**When to use:** You want to ask the author, reviewer, publication, or outlet directly and reasonably to fix or take down a specific inaccurate statement, in plain language, before or instead of escalating — and you want the request to be factual and hard to dismiss.

**When NOT to use:** You want to send a cease-and-desist, threaten a lawsuit, or demand money → that is a legal demand; route to an attorney (this prompt does not draft threats). You want the platform to remove it under its rules → use `legalprep_content_removal_platform_report.md`. You want to know whether you have a legal claim → route to an attorney (`legalprep_defamation_concern_documentation_organizer.md` organizes the facts). There is a safety threat or the publisher is someone you should not contact → Safety Block first; do not contact them directly.

---

## Safety Block

Stop and use a different pathway if:
- The publisher is an abuser, stalker, or someone subject to a protective order, or contact could put you at risk → do **not** contact them directly. National Domestic Violence Hotline 1-800-799-7233 (US); emergencies 911. Route all communication through counsel or an advocate.
- The statement is part of threats or targeted harassment → preserve records, do not engage, and consider `ic3.gov` (FBI Internet Crime Complaint Center) and law enforcement; route to counsel.
- You or someone else is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own request. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **helps you draft your own plain correction/retraction request to send yourself**. It is **not legal advice, legal strategy, a legal filing, a cease-and-desist, or a substitute for an attorney or your jurisdiction's law.** It will **not** conclude that a statement "is defamation, libel, or slander," make or imply a legal threat, cite or invent statutes, standards, or cases, claim damages or a dollar figure, or set a legal deadline. **A cease-and-desist or any demand carrying legal weight or threat must come from an attorney** — sending legal threats yourself can create risk and can be used against you. Whether you have a legal claim, and whether to send a formal demand, are entirely for an attorney. *Confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **You send it yourself — as a person, not a lawyer.** This is a reasonable request from you, in your own voice. It carries no legal threat and does not pretend to.
2. **Plain, factual, and civil.** "The statement says [X]; that is inaccurate. In fact, [checkable fact]. I am asking you to correct it." Calm and specific is more persuasive than angry and vague.
3. **State the inaccuracy, not a legal conclusion.** Say what is factually wrong and what is true — never that it "is defamation" or "is illegal."
4. **Ask for a concrete action.** Name what you want: a correction, a retraction, removal of a specific line, an update note. A clear ask is easier to grant.
5. **No threats, no statutes, no damages, no deadlines-with-consequences.** Those are legal moves and belong to an attorney; including them yourself can backfire.
6. **Keep a copy and stay factual even if ignored.** Send it in a way you can document (email you keep, the outlet's correction form); if it is refused, that is a fact for your record and your attorney — not a reason to escalate the tone.
7. **You prepare and send; the attorney handles legal escalation.** This drafts your civil request. Any demand, threat, or filing is the attorney's, never this request's.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Who published it / who you are asking:** [person, reviewer, editor, outlet — and how you will reach them]
- **The exact statement (verbatim):** [quote what was published]
- **Where and when it appeared:** [platform / publication / URL / date]
- **What specifically is inaccurate:** [the specific claim that is wrong]
- **The fact that supports your version:** [the checkable fact + any document]
- **What you are asking for:** [correction / retraction / removal of a line / update note]
- **How you will send it (and keep a copy):** [email / outlet's correction form / letter]
- **Is direct contact safe and appropriate?:** [if no → Safety Block; route through counsel/advocate]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Write in the user's first-person voice, civil and factual, for the user to send themselves.
- State the specific inaccuracy and the checkable fact that supports the user's version.
- Ask for a concrete, reasonable action (correct / retract / remove a line / add an update).
- Keep the request free of legal threats, statutes, damages figures, and consequence-deadlines.
- Note the user should keep a copy of what they send.
- Label the output `MY OWN REQUEST — NOT A LEGAL DEMAND OR CEASE-AND-DESIST`.

**Must Not:**
- Conclude that the statement "is defamation, libel, or slander," or assert any legal conclusion.
- Make, imply, or hint at a legal threat ("or I will sue," "or you'll hear from my lawyer").
- Cite or invent statutes, legal standards, or case law, or claim damages / a dollar figure.
- Draft a cease-and-desist, demand letter, or any court pleading.
- Characterize or attribute motive to the publisher beyond the factual inaccuracy.
- Set a deadline tied to a legal consequence.
- Fill gaps (wording, dates, the supporting fact) with assumption — flag them instead.
- Advise contacting the publisher where it is unsafe or inadvisable — route to the Safety Block / counsel.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for whether direct contact is safe and appropriate (abuser, stalker, protective order, harassment). If not, route to the Safety Block and to counsel/advocate — do not draft a direct message. Restate the jurisdiction and the boundary: this is a **civil request the user sends themselves**, not a legal demand; legal demands are for an attorney.

### Stage 2 — Confirm the Statement and the Inaccuracy
Confirm the verbatim statement, where/when it appeared, and the specific claim that is inaccurate. Flag `[UNCERTAIN WORDING:]` or `[NEED DATE:]` if imprecise. Pull from `legalprep_defamation_concern_documentation_organizer.md` if the user has one.

### Stage 3 — State the Supporting Fact
Identify the concrete, checkable fact that supports the user's version and any document that backs it. This is what makes the request credible. Flag `[NEED DOCUMENT:]` if the supporting record is not yet in hand.

### Stage 4 — Define the Ask
Help the user name exactly what they want: a correction, a full retraction, removal of a specific line, or an update note. Keep it reasonable and specific.

### Stage 5 — Draft the Civil Request
Draft the message in the user's voice: brief, factual, civil. State what was published, what is inaccurate, the supporting fact, and the ask. Strip anything that reads as a threat, a legal claim, or a demand. No statutes, no damages, no "or else."

### Stage 6 — Assemble and Close
Assemble the request labeled as the user's own message. Remind the user to send it in a way they can keep a copy of, and to route any legal escalation — a formal demand, a cease-and-desist, a lawsuit — to an attorney.

---

## Output Format

```markdown
# MY OWN REQUEST — NOT A LEGAL DEMAND OR CEASE-AND-DESIST
From me, [name], [date], to send myself to [publisher / outlet].
This is my own plain request to correct or retract an inaccurate statement. It makes no
legal threat and asserts no legal claim. Any legal demand would come from an attorney.

To: [name / editor / outlet]
Re: A factual inaccuracy in [where it appeared], dated [date]

Hello [name],

On [date], [in/on — platform or publication] the following was published about me:

> "[Exact statement, verbatim.]" [or UNCERTAIN WORDING: confirm from source]

This is factually inaccurate. Specifically, [the specific claim] is not correct. In fact,
[the checkable fact that supports my version], which I can support with [document — or NEED DOCUMENT:].

I am asking you to [correction / retraction / removal of that line / an update note] so the
record is accurate. I would appreciate a reply letting me know whether you are able to do this.

Thank you for your time.

[My name]
[My contact — as I choose to share it]

---
Note to myself: I will send this in a way I can keep a copy of. If it is refused or ignored,
that is a fact for my records and my attorney — not a reason to escalate on my own.
For any legal demand or next step, I will consult an attorney.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal escalation routed to an attorney?
- [ ] Written in the user's first-person voice, civil and factual, for the user to send themselves?
- [ ] Labeled `MY OWN REQUEST — NOT A LEGAL DEMAND OR CEASE-AND-DESIST`?
- [ ] Specific inaccuracy stated, with the checkable supporting fact?
- [ ] A concrete, reasonable ask (correct / retract / remove / update) included?
- [ ] No conclusion that anything "is defamation," and no legal conclusion?
- [ ] No legal threat, implied or explicit ("or I'll sue," "my lawyer will contact you")?
- [ ] No statute/case citation, no damages figure, no consequence-tied deadline?
- [ ] No cease-and-desist or pleading drafted; no motive attribution?
- [ ] Note to keep a copy of what is sent included?
- [ ] Gaps flagged `[NEED ...]` / `[UNCERTAIN ...]`, not filled?
- [ ] Safety/appropriateness of direct contact screened; unsafe contact routed to counsel/advocate?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Correct this defamatory statement or I will sue" | State the inaccuracy factually and ask civilly for a correction |
| "This violates [state] libel law" | State the fact; cite nothing; legal analysis is for an attorney |
| "I am entitled to $[amount] in damages" | Make no damages claim; that is for an attorney |
| "You have 48 hours before I take legal action" | No consequence-deadline; ask for a reply, no threat |
| Write it as a cease-and-desist | Keep it a plain, civil request labeled NOT A LEGAL DEMAND |
| "You did this maliciously to ruin me" | State the inaccuracy and the fact; motive is for counsel |
| Send it to an abuser directly | Stop, Safety Block; route contact through counsel/advocate |
| Assume the supporting document exists | Flag `[NEED DOCUMENT:]` |
| Escalate the tone if ignored | Log the refusal as a fact; route escalation to an attorney |

---

## Adaptations

**By recipient:**
- **News outlet / publication:** Use the outlet's correction/ombudsman channel if it has one; keep it short and point to the specific line and the fact; editors handle these routinely.
- **Individual author / reviewer:** Keep it especially civil and low-conflict; a reasonable person-to-person request is often the fastest fix.
- **Business / review platform poster:** Ask for the specific factual correction; if they refuse, the platform's factual-error channel is a separate track (`legalprep_content_removal_platform_report.md`).

**By situation/profile:**
- **You have strong documentation:** Reference (do not over-argue) the supporting fact; offer to share the document — one clean fact is more persuasive than many.
- **Prior hostile contact / high conflict:** Consider whether direct contact is wise at all; a request from an attorney may be more appropriate — route to counsel.
- **Safety dimension / abuser:** Do not contact directly; Safety Block; all communication through counsel or an advocate.

---

## Related Prompts

- `legalprep_defamation_concern_documentation_organizer.md` — organizes the verbatim statement and inaccuracy that feed this request.
- `legalprep_content_removal_platform_report.md` — the platform-report track if the publisher refuses or is unreachable.
- `legalprep_reputation_harm_impact_log.md` — the dated harm log to keep alongside your records.
- `../../ip/legal_defamation_publicity_risk_screen.md` — the attorney-side screen for whether a formal demand or claim is warranted.
