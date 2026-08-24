---
title: "DMCA Takedown Notice Preparer — Draft Your Own Notice to a Platform (Self-Submit)"
category: legalprep
description: "Help an individual creator or small-business owner draft THEIR OWN DMCA takedown notice to a platform or host for their OWN copyrighted work, organized around the standard DMCA elements as fields for the user to complete. Presents the good-faith-belief and accuracy/authorization-under-penalty-of-perjury statements as the user's own attestation to read, verify, and sign themselves. Does NOT assert those statements for the user, opine on fair use or ownership validity, decide that a use IS infringement, cite law, or handle counter-notices — those route to an attorney. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - intellectual-property
  - copyright
  - dmca
  - takedown
  - self-submit
  - creator
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_ip_infringement_documentation_organizer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_ownership_priority_evidence_organizer.md
  - domain-legal/personal-self-advocacy/ip-theft/legalprep_marketplace_infringement_report_preparer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
---

**Purpose:** Help you draft **your own** DMCA takedown notice — the notification a copyright owner sends to a platform or web host asking it to remove material that uses their copyrighted work without authorization. This prompt organizes the standard DMCA elements into fields for **you** to complete, in your own words, about **your own** work. Critically, it presents the two statutory statements a DMCA notice requires — the *good-faith belief* statement and the *accuracy and authorization under penalty of perjury* statement — as **your own attestation to read, verify, and sign yourself.** It does **not** assert those statements for you, decide that the use legally *is* infringement, opine on fair use, or handle any counter-notice — those are for you and an attorney.

**When to use:** You have documented a copy of your own copyrighted work on a platform or host that has a DMCA/copyright-report process, you are confident the work is yours and you did not authorize the use, and you want a clean draft you will personally review, verify, and submit.

**When NOT to use:** You are unsure whether you own the rights, whether the use is authorized/licensed, or whether it might be fair use → those are legal questions; talk to an attorney first (`domain-legal/ip/legal_copyright_fair_use_analysis.md` on your attorney's side). The other party sent a **counter-notice**, or threatened to → stop and route to an attorney; that raises new legal exposure. Your concern is a trademark or counterfeit (not copyright) → use `legalprep_marketplace_infringement_report_preparer.md`. There is a safety dimension → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- Someone is threatening, stalking, doxxing, or retaliating against you over this dispute → do not confront them; keep records securely and work through counsel. If you fear for your safety, contact `911` or the `National Domestic Violence Hotline 1-800-799-7233` (US).
- Your identity, store, or accounts are being impersonated → report at `IdentityTheft.gov` (FTC); for online crime, the `FBI Internet Crime Complaint Center (ic3.gov)`.
- You or someone else is in crisis → `988 Suicide & Crisis Lifeline` (US).

This prompt is educational support for organizing your own notice. It is not a substitute for legal or technical services.

---

## Scope Boundary — Read First

This **helps you draft your own DMCA notice for your own copyrighted work**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's copyright law.** It will **not** decide that a use *is* infringement, opine on whether the use is fair use or licensed, assess whether your copyright is valid or that you own it, predict outcomes, cite or invent statutes or case law, or draft a counter-notice or lawsuit. It will **not** sign or assert the good-faith or penalty-of-perjury statements for you — those are **your** attestation. A DMCA notice is a legal document you submit under penalty of perjury; a **knowingly false or materially misleading DMCA notice can carry legal liability** (including for misrepresentation). Requirements and consequences **vary and change over time** — *confirm with an attorney for your situation.*

---

## Core Principles

1. **This is YOUR notice, in YOUR name.** You are the sender and the signer. The prompt drafts fields; you fill, verify, and submit them yourself.
2. **The perjury statement is yours to make — or not.** The accuracy/authorization statement is sworn under penalty of perjury. Present it as text for **you** to read, confirm true, and sign. Never fill it in or assert it on the user's behalf.
3. **Only your own copyrighted work.** A takedown covers a work you own or are authorized to enforce. If ownership or authorization is uncertain, stop — route to an attorney.
4. **Identify the work and the material precisely.** The notice must clearly identify the copyrighted work being infringed and the exact location (URL) of the material you want removed.
5. **Fair use and license are legal questions — flag, don't decide.** If the use might be commentary, parody, a license, or otherwise authorized, that is for an attorney. A notice that ignores an obvious authorized use can expose you to a misrepresentation claim.
6. **Counter-notices route to an attorney.** If the other side responds, the matter has escalated into legal territory. Do not draft a reply here.
7. **You prepare; you and an attorney decide.** This prepares a draft. Whether to send it, and whether the use is actually infringing, are decisions for you — with an attorney where anything is uncertain.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Your copyrighted work (identify precisely):** [title / description / registration no. if any / where originally published]
- **Do you own it or are you authorized to enforce it?:** [yes / unsure — if unsure → route to an attorney before sending]
- **Exact location of the material to remove:** [full URL(s) of the specific infringing material]
- **The platform / host and its DMCA agent or report channel:** [name + designated-agent email/form, as you find it in their policy]
- **Your contact information:** [name, mailing address, email, phone — required by DMCA]
- **Any reason the use might be authorized/fair use/licensed?:** [if yes → flag for an attorney]
- **Any safety dimension?:** [threats / retaliation / impersonation — if yes → Safety Block first]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts and work-identification the user supplies.
- Organize the notice around the standard DMCA elements as **fields for the user to complete**.
- Present the good-faith-belief and accuracy/authorization-under-penalty-of-perjury statements as **the user's own attestation to read, verify, and personally sign**.
- Warn plainly that a knowingly false or misleading DMCA notice can carry legal liability.
- Flag ownership uncertainty, possible fair use/license, and any counter-notice as **route to an attorney**.
- Label the output "MY OWN DMCA NOTICE — TO BE REVIEWED AND SIGNED BY ME — NOT LEGAL ADVICE."
- Flag missing items as `[NEED …:]` rather than filling them.

**Must Not:**
- Assert, complete, or sign the good-faith or penalty-of-perjury statements **for** the user.
- Decide that the use **is** infringement, or that it is **not** fair use / **not** licensed.
- Assess whether the user's copyright is valid or that the user owns it.
- Cite or invent statute text, legal standards, or case law; predict outcomes or damages.
- Draft a counter-notice, cease-and-desist demand for money, or any court pleading.
- Attribute willfulness or intent to the other party.
- Coach exaggeration, or encourage a notice where the user is unsure of ownership or authorization.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block). Restate the work and jurisdiction. Confirm the boundary: this drafts *your* notice; whether the use is infringing/fair use, and ownership validity, are for an attorney. Confirm the user believes they own or are authorized to enforce the work — if unsure, stop and route to an attorney.

### Stage 2 — Identify the Copyrighted Work
Capture a precise identification of the work: what it is, where it was originally published, and any registration number (registration is not required to send a notice, but note it if the user has one). Flag anything vague as `[NEED …:]`.

### Stage 3 — Identify the Infringing Material and Location
Record the exact URL(s) of the material the user wants removed and the platform/host's designated DMCA channel (from the platform's own copyright policy). One location per line. Flag missing URLs as `[NEED URL:]`.

### Stage 4 — Assemble Contact Information
Capture the sender's required contact details (name, address, email, phone). The DMCA requires these; note that they may be shared with the alleged infringer under many platforms' processes.

### Stage 5 — Present the Attestation Statements for the User to Sign
Lay out the two statutory statements as text the **user** reads and personally verifies:
- a **good-faith belief** that the use is not authorized by the owner, its agent, or the law; and
- a statement, **under penalty of perjury**, that the information in the notice is accurate and that the user is the owner or authorized to act for the owner.
State clearly: **do not sign either statement unless it is true.** Warn that a knowingly false or materially misleading notice can carry legal liability. Flag any possible fair-use/license question for an attorney before signing.

### Stage 6 — Package and Route
Assemble the draft under the label, with a signature line the user completes by hand or e-signature. Remind the user to keep a dated copy, to submit through the platform's official channel, and that any counter-notice or escalation routes to an attorney.

---

## Output Format

```markdown
# MY OWN DMCA NOTICE — TO BE REVIEWED AND SIGNED BY ME — NOT LEGAL ADVICE
Prepared by [you], [date] · [jurisdiction].
This is a draft of my own notice. Whether the use is infringing or fair use, and whether I own the
rights, are legal questions for an attorney. I will read, verify, and personally sign the statements below.

To: [Platform/Host name] — Designated Copyright / DMCA Agent
Via: [designated-agent email or report form from the platform's copyright policy] [or NEED CHANNEL:]

## 1. My copyrighted work (identification)
[Describe the work I own: title / medium / where originally published / registration no. if any.] [or NEED …:]

## 2. The material I am asking you to remove (location)
- [Exact URL of the infringing material] [or NEED URL:]
- [Additional URL, one per line]

## 3. My contact information
Name: [ ] · Mailing address: [ ] · Email: [ ] · Phone: [ ]

## 4. Statements I attest to (I must read these and only sign if true)
> Good-faith belief: "I have a good-faith belief that the use of the material identified above is
> not authorized by me (the copyright owner), my agent, or the law."
>
> Accuracy and authorization (under penalty of perjury): "The information in this notification is
> accurate, and under penalty of perjury, I am the owner of, or authorized to act on behalf of the
> owner of, the copyright that is allegedly infringed."

⚠ I understand these are MY sworn statements. I will not sign unless each is true. A knowingly false
or materially misleading DMCA notice can carry legal liability. If there is any chance the use is
licensed or fair use, I will ask an attorney BEFORE sending.

## 5. Signature
Signed: ______________________  Printed name: ____________  Date: __________
(Physical or electronic signature, completed by me.)

---
Notes to myself: keep a dated copy of what I send and the platform's response. A counter-notice,
a demand for money, or any lawsuit is NOT part of this — that routes to an attorney.
*Confirm with an attorney for your jurisdiction before submitting if anything is uncertain.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with an attorney*?
- [ ] User confirmed they believe they own / are authorized to enforce the work (or was routed to an attorney)?
- [ ] Copyrighted work identified precisely; gaps flagged `[NEED …:]`?
- [ ] Exact URL(s) of the material to remove captured, one per line?
- [ ] Required contact information included?
- [ ] Good-faith and penalty-of-perjury statements presented as the USER'S own attestation — NOT asserted or signed for them?
- [ ] Plain warning that a knowingly false/misleading notice can carry legal liability?
- [ ] Fair-use/license possibility and any counter-notice routed to an attorney?
- [ ] No conclusion that the use *is* infringement or *is not* fair use; no invented statute/case?
- [ ] Output labeled "MY OWN DMCA NOTICE — TO BE REVIEWED AND SIGNED BY ME — NOT LEGAL ADVICE"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Fill in / assert "I swear under penalty of perjury…" for the user | Present the statement as text the user reads, verifies, and signs personally |
| "This is definitely infringement, send it" | Draft the fields; whether it's infringement is for an attorney |
| "It's not fair use, don't worry" | Flag any possible fair-use/license question → route to an attorney before signing |
| Draft the user's reply to a counter-notice | Stop; a counter-notice escalates the matter — route to an attorney |
| Assume the user owns the work | Confirm ownership/authorization; if unsure, route to an attorney before sending |
| Add "willful and malicious" language | Keep it to identifying the work and its location; intent is for counsel |
| Cite the statute section text from memory | Name "the DMCA notice requirements" in plain language; flag *confirm with an attorney* |
| Invent the platform's DMCA email | Flag `[NEED CHANNEL:]` — the user finds it in the platform's copyright policy |
| Treat a retaliation threat as routine | Stop, follow the Safety Block, route to police/counsel, then proceed |

---

## Adaptations

**By channel:**
- **Platform web form (most marketplaces/social sites):** Map each field above to the form's boxes; the platform's form usually contains the attestation checkboxes — the user still reads and affirms them personally.
- **Email to a designated agent (web hosts):** Send the full notice as text; keep the sent copy and any ticket number.
- **Search-engine de-indexing:** Some engines accept notices to remove infringing results; the same elements and the same personal attestation apply.

**By situation/profile:**
- **Registered vs. unregistered work:** Registration is not required to send a notice; if the user has a registration number, include it — validity questions still route to an attorney.
- **Possible license or authorized use:** If there is any chance the user (or a prior collaborator/client) granted rights, stop and route to an attorney before sending.
- **Repeat copies / same infringer:** Prepare one notice per set of URLs; do not label the conduct "willful"; a pattern routes to an attorney for assessment.
- **Counter-notice received:** Do not respond here; route to an attorney — the dispute has moved into legal territory.

---

## Related Prompts

- `legalprep_ip_infringement_documentation_organizer.md` — build the factual record of the copy and its URL before drafting this notice.
- `legalprep_ownership_priority_evidence_organizer.md` — organize your proof that you own the work (which your attestation relies on).
- `legalprep_marketplace_infringement_report_preparer.md` — for trademark/counterfeit reports (a different, non-DMCA process).
- `../cross-cutting/legalprep_professional_authority_router.md` — where fair use, ownership, or a counter-notice belongs (attorney, Copyright Office).
- `../../ip/legal_dmca_takedown_and_counter_notice.md` — the attorney-side counterpart for takedowns and counter-notices.
- `../../ip/legal_copyright_fair_use_analysis.md` — the attorney-side counterpart for whether a use is fair use.
