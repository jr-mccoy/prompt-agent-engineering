---
title: "Motion to Dismiss — Rule 12(b)(6) (and State Analogs)"
category: legal/litigation
description: "Draft a motion and supporting memorandum to dismiss a complaint for failure to state a claim under Federal Rule 12(b)(6) or the controlling state analog — including standard, count-by-count plausibility analysis, and prayer."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - litigation
  - motion-to-dismiss
  - 12b6
  - twombly-iqbal
  - pleading
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/litigation/legal_motion_for_summary_judgment.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a Rule 12(b)(6) motion (or the controlling state analog — demurrer, motion to dismiss for failure to state a cause of action, etc.) attacking a complaint count-by-count under the operative pleading standard.

**When to use:** Pre-answer attack on the pleadings. For state-court analogs, replace the standard with the controlling state articulation. Output is a filable motion plus a memorandum of law.

---

## Your Input

- **Court / venue:** [Federal district / state court]
- **Operative rule:** [Fed. R. Civ. P. 12(b)(6) / state analog with citation]
- **Pleading standard articulation:** [Twombly/Iqbal plausibility / state's articulation — supply the controlling case if state]
- **Complaint to attack:** [Paste counts and the supporting factual allegations]
- **Targets:** [All counts / specific counts — list]
- **Substantive law for each targeted count:** [Elements of the claim under the controlling law]
- **Documents incorporated by reference / subject to judicial notice:** [If you intend to attach or reference]
- **Any preserved defenses to also raise:** [12(b)(1) jurisdictional, 12(b)(2) personal jurisdiction, 12(b)(3) venue, 12(b)(7) failure to join — only if intended]
- **Local rules considerations:** [Page limits, meet-and-confer, briefing schedule]
- **Tone:** [Aggressive / measured / dispassionate]

---

## Constraints

**Must:**
- State the controlling pleading standard accurately. For federal: Twombly/Iqbal — well-pleaded factual allegations are accepted as true; legal conclusions and threadbare recitations of elements are not; the claim must be plausible, not merely conceivable.
- Draft both (a) a Notice of Motion and (b) a Memorandum of Law. The motion is short; the memorandum carries the argument.
- Argue **count-by-count**. For each count, lay out the elements, identify which fail, and walk the deficient allegations through the standard.
- Distinguish between **factual deficiencies** (no plausible factual content) and **legal deficiencies** (the alleged conduct, even if true, does not state a claim).
- Address documents incorporated by reference or subject to judicial notice properly — without converting to summary judgment.
- Acknowledge but distinguish the most plausible plaintiff's-side reading; do not strawman.
- Identify whether dismissal should be **with prejudice** or **without leave to amend** based on whether amendment could plausibly cure.
- Match local rules on page limits, font, captioning, and any meet-and-confer certification.

**Must Not:**
- Argue facts outside the pleadings (other than properly noticeable / incorporated-by-reference materials). Doing so risks Rule 12(d) conversion.
- Recite Twombly/Iqbal as a magic phrase without applying the standard to specific allegations.
- Treat allegations on information and belief as automatically deficient — they can support plausibility when supported by factual content.
- Combine 12(b)(6) with 12(b)(1) jurisdictional arguments without keeping the standards separate (jurisdictional facts can be challenged on a different record).
- Move on the merits when the deficiency is curable; if curable, the typical relief is dismissal with leave to amend.
- Sneak summary-judgment-style fact arguments under the 12(b)(6) banner.

---

## Instructions

1. **Notice of Motion.** Short, names the rule, identifies the relief, sets the hearing date per local rules.
2. **Memorandum — Introduction.** Two short paragraphs: what the complaint is and why it fails count-by-count.
3. **Memorandum — Background.** Recite only the well-pleaded factual allegations relevant to the motion. Quote contract terms if attached. Identify documents subject to judicial notice / incorporated by reference.
4. **Memorandum — Legal Standard.** Twombly/Iqbal (or state articulation) in two paragraphs. Use language from the supplied authority.
5. **Memorandum — Argument, count-by-count.** For each count:
   - **Caption:** "I. Count {N} ({Claim}) Fails to State a Claim Because…"
   - **Elements** of the claim under the controlling law.
   - **Identify** which elements are deficiently pleaded.
   - **Walk** the deficient allegations through the standard, separating conclusions from factual content.
   - **Address** the most plausible reading the plaintiff will press on opposition.
6. **Memorandum — Leave to Amend.** Address whether the deficiency is curable. If incurable (e.g., the substantive law forecloses the theory; statute of limitations on the face of the complaint), argue dismissal with prejudice.
7. **Conclusion.** Crisp prayer for relief.
8. **Proposed Order.** Optional, where local rules permit.
9. **Certifications:** meet-and-confer, length, etc., per local rules.

---

## Output Format

```markdown
{COURT CAPTION}

DEFENDANT'S MOTION TO DISMISS UNDER FED. R. CIV. P. 12(b)(6)

Defendant {Name} respectfully moves this Court for an order dismissing the Complaint pursuant to Federal Rule of Civil Procedure 12(b)(6) for failure to state a claim upon which relief can be granted. This Motion is supported by the accompanying Memorandum of Law.

Dated: {date}                       /s/ {counsel}, {Bar No., firm}

---

MEMORANDUM IN SUPPORT OF DEFENDANT'S MOTION TO DISMISS

INTRODUCTION
{Two short paragraphs.}

BACKGROUND
{Well-pleaded factual allegations only; documents incorporated by reference; matters subject to judicial notice.}

LEGAL STANDARD
{Twombly/Iqbal articulation grounded in supplied authority; pinpoints required if cited.}

ARGUMENT

I. Count {N} ({Claim}) Fails to State a Claim Because {Operative Reason}.
   A. Elements. {List elements of the claim under controlling law.}
   B. The Complaint Pleads No Plausible Factual Content as to {Element}.
      {Walk the relevant allegations; separate conclusions from facts; apply the standard.}
   C. {Count-specific responses to plaintiff's likely reading.}

II. Count {N+1} ({Claim}) ...

III. ...

IV. Dismissal Should Be With Prejudice / Without Leave to Amend Because {Reason}.
   {Apply the operative incurability standard.}

CONCLUSION
For the foregoing reasons, Defendant respectfully requests that this Court dismiss Counts {…} of the Complaint {with prejudice / without leave to amend}.

Dated: {date}                       /s/ {counsel}

---

[CERTIFICATE OF COMPLIANCE / MEET-AND-CONFER CERTIFICATION per local rules]
[CERTIFICATE OF SERVICE]
[PROPOSED ORDER, if locally required]
```

---

## Verification

- [ ] Pleading standard accurately stated and grounded in supplied authority.
- [ ] Argument is count-by-count, not bundled.
- [ ] Each count has elements identified and a deficiency tied to specific allegations.
- [ ] Conclusory allegations and naked recitals of elements are flagged as such.
- [ ] No reliance on extrinsic facts beyond incorporated-by-reference / judicial-notice materials.
- [ ] Plaintiff's strongest reading is acknowledged and distinguished, not ignored.
- [ ] Leave-to-amend posture addressed with operative reason.
- [ ] Local rules (page limit, certification, captioning) accounted for.
- [ ] No invented case citations or pinpoints; missing citations flagged with placeholders.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Reciting Twombly/Iqbal without applying it | Walk specific allegations through the standard; identify which ones are conclusory and which are factual |
| Attaching exhibits not incorporated by reference | Risks Rule 12(d) conversion to summary judgment; keep to incorporated-by-reference and judicially noticeable materials |
| Treating "on information and belief" allegations as automatically deficient | Information-and-belief allegations are sufficient if supported by factual content suggesting plausibility |
| Smuggling a summary-judgment-style fact dispute into a 12(b)(6) | The motion is about pleading sufficiency; factual disputes belong elsewhere |
| Combining personal-jurisdiction and 12(b)(6) arguments under one standard | They have different standards and different records; brief separately |
| Ignoring leave to amend in federal court | Rule 15(a)(2) freely-given standard applies; argue futility, undue delay, or bad faith if seeking with-prejudice |
| Treating dicta in Twombly/Iqbal as the holding | The plausibility standard is the holding; use the operative language carefully |
| Asking for dismissal with prejudice on a curable deficiency | Match relief to incurability; over-asking weakens the motion |
| Citing pre-Twombly pleading-standard cases as if they still control | Identify any reliance on Conley v. Gibson-era standards as superseded for federal practice |
