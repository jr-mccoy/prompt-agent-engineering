---
title: "Online Content Report Preparer — Draft Your Own Factual Report of Content to a Platform"
category: legalprep
description: "[SELF-SUBMIT] Help a person draft their OWN factual report or flag of online content to a platform or search engine under that platform's policies (harassment, impersonation, privacy, factual-error/removal). Produces a neutral, first-person report the user submits themselves. Does NOT decide whether content is defamatory, assert legal conclusions, cite law, or draft a legal demand — platform-policy removal is separate from any legal remedy, and legal remedies route to an attorney. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - NE-25
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - defamation
  - reputation
  - platform-report
  - content-removal
  - self-submit
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_defamation_concern_documentation_organizer.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_correction_retraction_request_preparer.md
  - domain-legal/personal-self-advocacy/defamation-reputation/legalprep_reputation_harm_impact_log.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
---

**Purpose:** Help you draft your **own** clear, factual report to a platform or search engine — flagging content about you under the platform's **own policies** (harassment, impersonation, non-consensual private information, or a factual-error/removal channel). The output is a first-person report **you** submit through the platform's reporting tool; it is not written or sent by anyone else on your behalf. It organizes your report neutrally so it maps to the policy category you are using. It does **not** decide whether the content is defamatory, assert any legal conclusion, or serve as a legal demand — a platform removing content under its policy is **separate from any legal remedy**, and legal remedies route to an attorney.

**When to use:** You have identified content about you online and want to report it through the platform's built-in reporting/flagging tool, and you want your report to be factual, specific, and matched to the right policy category so it is easy for the platform to act on.

**When NOT to use:** You want to know whether the content is legally defamatory or whether to sue → that is legal analysis; route to an attorney (`legalprep_defamation_concern_documentation_organizer.md` organizes the underlying facts). You want to send the author a correction request → use `legalprep_correction_retraction_request_preparer.md`. You are filing a copyright takedown for your own work that was copied → that is a distinct DMCA process (`../../ip/legal_dmca_takedown_and_counter_notice.md`). There is a safety threat → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- The content is part of threats, stalking, doxxing, or targeted harassment → National Domestic Violence Hotline 1-800-799-7233 (US); emergencies 911. Report to the platform's safety/emergency channel and to law enforcement; consider `ic3.gov` (FBI Internet Crime Complaint Center) for a criminal dimension. Preserve records; do not confront the poster.
- The content exposes your home address, financial, or other sensitive private information → use the platform's privacy/personal-information removal channel and, for identity misuse, `IdentityTheft.gov` (FTC).
- You or someone else is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own report. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **helps you draft your own factual report to a platform under that platform's policies**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** conclude that content "is defamation, libel, or slander," assert any legal conclusion, cite or invent statutes or cases, or draft a legal demand or cease-and-desist. **A platform's decision to remove content under its own rules is separate from, and does not determine, any legal right or remedy** — platforms apply their policies, not the law of your jurisdiction, and outcomes vary and change over time. Whether you have a legal claim is entirely for an attorney. *Confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **You submit it yourself.** This is your own report, entered through the platform's reporting tool with your own account or contact details. No one is drafting a demand on your behalf.
2. **Match the platform's policy category, don't invent a legal one.** Report under the platform's actual category — harassment, impersonation, privacy/personal-information, or its factual-error/removal channel — not under a "defamation" legal label.
3. **Factual and specific beats angry and broad.** "This account uses my name and photo and claims to be me" is actionable by a reviewer; "this is disgusting and illegal" is not.
4. **Point to the exact content.** Give the URL, handle, post ID, or screenshot the platform needs to locate it. A report a reviewer cannot locate cannot be acted on.
5. **Say plainly why it violates the policy — in the platform's terms.** State which policy and how the content fits it, factually, without asserting a legal conclusion.
6. **Platform removal is not a legal ruling.** Removal (or refusal) says nothing about whether you have a legal claim. Keep the two tracks separate.
7. **You prepare and submit; the attorney handles legal remedies.** This organizes your policy report. Any legal claim, demand, or filing is the attorney's, never this report's.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Platform / search engine:** [where the content is]
- **Exact location of the content:** [URL / handle / post ID — and a saved screenshot]
- **Which platform policy applies:** [harassment / impersonation / privacy-personal-info / factual-error or removal channel — as the platform defines it]
- **What the content is:** [factual description of what it shows or claims]
- **Why it violates that policy (factually):** [how it fits the platform's category, in plain terms]
- **Your relationship to it:** [it names/depicts me; it impersonates me; it exposes my private info]
- **What you have preserved:** [screenshots, URLs, dates — before reporting, in case it changes]
- **Any safety dimension (threats, doxxing)?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Write the report in the user's first-person voice, for the user to submit themselves.
- Match the report to a real platform policy category, in the platform's own terms.
- Point to the exact content (URL/handle/post ID) and note preserved copies.
- Keep the report factual, specific, and neutral in tone.
- Note that platform-policy removal is separate from any legal remedy, and route legal remedies to an attorney.
- Label the output `MY OWN REPORT — [platform] — NOT A LEGAL FILING`.

**Must Not:**
- Conclude that content "is defamation, libel, or slander," or assert any legal conclusion.
- Cite or invent statutes, legal standards, or case law.
- Draft a legal demand, cease-and-desist, or court pleading.
- Characterize or attribute motive to the poster beyond the factual content.
- Present the report as guaranteed to result in removal.
- Fill gaps (URL, dates, policy category) with assumption — flag them instead.
- Coach the user to submit a false or exaggerated report, or to gather evidence unlawfully.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for threats, doxxing, or targeted harassment and route to the Safety Block if present. Restate the jurisdiction. State the boundary: this drafts **your own** policy report; platform removal is **separate from any legal remedy**, and the legal question is for an attorney.

### Stage 2 — Preserve Before Reporting
Confirm the user has saved dated screenshots and the URL before submitting — content can be edited or deleted once reported. Flag `[NEED DOCUMENT: capture and date before reporting]` if not.

### Stage 3 — Identify the Right Policy Channel
Help the user match the content to the platform's **own** policy category (harassment, impersonation, privacy/personal-information, factual-error/removal). Use the platform's terms, not a legal label. If the user is unsure which channel exists, flag `[CONFIRM: check the platform's current reporting categories]`.

### Stage 4 — Locate the Content Precisely
Record the exact URL, handle, and/or post ID the platform reviewer needs. A report must point to a locatable item. Flag `[NEED URL:]` / `[NEED POST ID:]` if missing.

### Stage 5 — State the Violation Factually
Draft, in the user's voice, a factual statement of what the content is and how it fits the chosen policy — no legal conclusions, no motive, no legal labels. Keep it specific and brief.

### Stage 6 — Assemble the Report and Note the Attestation
Assemble the first-person report labeled as the user's own submission. If the platform's form includes a certification (e.g., "I confirm this report is accurate" or a good-faith statement), present it as **the user's own statement to read, verify, and affirm themselves** — do not assert it for them. Close by noting platform removal ≠ legal remedy; route legal remedies to an attorney.

---

## Output Format

```markdown
# MY OWN REPORT — [platform] — NOT A LEGAL FILING
Prepared by me, [name], [date], to submit through [platform]'s reporting tool.
This is my own factual report under [platform]'s policy. It does NOT allege defamation
or any legal claim; platform removal is separate from any legal remedy.

## Policy Category I Am Reporting Under
[Platform's own category — e.g., Impersonation / Harassment / Privacy — personal information / Factual-error channel]
[CONFIRM: this matches a current [platform] reporting category]

## The Content
- Location: [exact URL / handle / post ID]
- What it is: [factual description of what the content shows or claims]
- Date I observed / captured it: [YYYY-MM-DD]
- Preserved copy: [screenshot/archive stored at — location]

## Why It Violates [platform]'s Policy (factual)
[In my own words: what the content does and how it fits the chosen policy category —
factual and specific, no legal conclusions. E.g., "This account uses my legal name and
my photograph and presents itself as me; I did not create it and it is not authorized by me."]

## What I Am Requesting
[The platform's available action under this policy — e.g., removal of the impersonating
account / removal of the post / de-indexing under the removal channel.]

## My Own Attestation (for me to read, verify, and affirm before submitting)
[If [platform]'s form asks me to confirm accuracy or good faith, I will read that statement,
confirm it is true to the best of my knowledge, and affirm it myself. I do not assert it here
on anyone else's behalf.]

---
Note to myself: A platform removing (or declining to remove) this content decides nothing
about any legal claim I may have. For legal remedies, I will consult an attorney.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal remedies routed to an attorney?
- [ ] Report written in the user's first-person voice, for the user to submit themselves?
- [ ] Labeled `MY OWN REPORT — [platform] — NOT A LEGAL FILING`?
- [ ] Matched to a real platform policy category in the platform's own terms (not a legal label)?
- [ ] Exact content location (URL/handle/post ID) included; preserved copy noted?
- [ ] Violation stated factually — no "this is defamation," no legal conclusion, no statute/case citation?
- [ ] No legal demand, cease-and-desist, or pleading drafted?
- [ ] No motive attribution beyond the factual content?
- [ ] Any platform certification presented as the user's own statement to affirm, not asserted for them?
- [ ] Note that platform removal is separate from any legal remedy included?
- [ ] Gaps flagged `[NEED ...]` / `[CONFIRM:]`, not filled?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Report this as defamation — it's illegal" | Report under the platform's actual policy (harassment/impersonation/privacy), factually |
| "This will get it removed, guaranteed" | Note the platform decides under its own rules; outcomes vary |
| Assert a legal conclusion in the report | State the facts and how they fit the platform's policy |
| Cite a statute to the platform | Cite nothing; keep it to the platform's terms |
| Write the report as if from a lawyer | Keep it first-person; it is the user's own submission |
| Sign a good-faith/accuracy certification for the user | Present it for the user to read, verify, and affirm themselves |
| Fill in a URL or post ID you don't have | Flag `[NEED URL:]` / `[NEED POST ID:]` |
| Treat platform removal as a legal win | Keep the policy track and the legal track separate |
| Treat threats/doxxing as a routine report | Stop, follow the Safety Block, use the safety channel + law enforcement |

---

## Adaptations

**By policy channel:**
- **Impersonation:** Focus on identity — your real name/photo used, you did not create the account, it is presented as you; platforms usually ask you to verify your identity.
- **Harassment / abuse:** Describe the targeting factually (repeated posts, tags, coordinated activity); pair with the Safety Block if there are threats.
- **Privacy / personal information (doxxing):** Point to the specific private data exposed (home address, financial, ID numbers); this channel is often faster than a factual-error channel.
- **Factual-error / removal channel (e.g., a search engine's removal or a review platform's process):** State the specific factual error and what supports your version; note this channel varies widely by platform — `[CONFIRM: current process]`.

**By situation/profile:**
- **Content keeps reappearing:** Report each instance, keep dated records, and note the pattern in the harm log — but do not characterize it as a "campaign" in the report.
- **Copyrighted work of yours was copied:** That is a separate DMCA process, not a policy report → `../../ip/legal_dmca_takedown_and_counter_notice.md`.
- **Safety dimension:** Safety Block first; use the platform's safety/emergency channel; preserve and route to law enforcement and counsel.

---

## Related Prompts

- `legalprep_defamation_concern_documentation_organizer.md` — organizes the underlying facts of the statement before you report it.
- `legalprep_correction_retraction_request_preparer.md` — to ask the author/outlet directly for a correction, a separate track from a platform report.
- `legalprep_reputation_harm_impact_log.md` — the dated harm log to accompany your records.
- `../../ip/legal_dmca_takedown_and_counter_notice.md` — the distinct copyright takedown process when your own work was copied (attorney-side reference).
