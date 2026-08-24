---
title: "Discovery Meet-and-Confer Letter (Rule 37 Deficiency)"
category: legal/discovery
description: "Draft a meet-and-confer / Rule 37 deficiency letter that identifies specific deficiencies in the recipient's discovery responses, cites the controlling rule and authority, proposes a resolution, and creates a record sufficient to support a later motion to compel."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - discovery
  - meet-and-confer
  - rule-37
  - deficiency-letter
  - motion-to-compel
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_privilege_log_generator.md
---

**Purpose:** Produce a meet-and-confer letter that does double duty: (1) genuinely advances resolution and (2) builds the record for a motion-to-compel certification under Rule 37 (or analog) if resolution fails.

**When to use:** After receiving deficient responses; after a privilege log arrives short of standard; after a custodian production runs incomplete; before scheduling a motion to compel.

---

## Your Input

- **Court / venue and rule:** [Federal Rule 37 / state analog]
- **Discovery at issue:** [RFPs / interrogatories / RFAs / privilege log / deposition / ESI plan]
- **Specific responses being challenged:** [Quote each response or summarize the deficiency, with the request and response numbers]
- **Categories of deficiency:** [Boilerplate objections, failure to indicate withholding, inadequate privilege log entries, failure to produce on a committed schedule, scope refusal, missing custodians, missing source systems, etc.]
- **What we want:** [Production / supplemental log / specific facts / amended response — by date]
- **Prior correspondence:** [Earlier letters, emails, calls — dates and outcomes]
- **Local meet-and-confer rules:** [Telephone or in-person required? Time-frame? Certification format?]
- **Tone:** [Cooperative / firm / pre-motion]

---

## Constraints

**Must:**
- Identify each deficiency by request number and quote enough of the response to make the deficiency unmistakable.
- Cite the **specific rule provision** that the response violates (e.g., Rule 34(b)(2)(C) — failure to state whether anything is being withheld; Rule 26(b)(5) — privilege-log specificity; Rule 33(d) — business-records option requires sufficient specification).
- Cite **case authority** only if supplied; otherwise use `[CITE: ...]` placeholders.
- Propose a **specific cure**: produce by date X; supplement log by date Y; identify additional custodians.
- Propose a **meeting time** that complies with local rules (telephonic or in-person; live conference required in many districts).
- Make the letter **cite-able**: a magistrate reading it should immediately see the rule, the deficiency, the proposed cure, and the offer to confer.
- End with a clear deadline before motion practice.

**Must Not:**
- Fold in unrelated grievances. The letter should be focused on the specific discovery items.
- Be performatively aggressive. Hostility undermines the cooperative-attempt requirement.
- Demand the impossible. A 24-hour cure deadline for a custodian-list re-collection invites the responder to ignore the letter.
- Concede positions you do not need to concede.
- Reveal litigation strategy beyond what is necessary to make the discovery point.
- Use a single rolling complaint paragraph; structure for surgical responses.

---

## Instructions

1. **Header.** Date, sent via {email; certified mail; service convention}, "Re: {Matter} — Meet-and-Confer Regarding [Discovery]."
2. **Opening.** One paragraph: the discovery served and date, the responses received and date, the purpose of the letter (Rule 37 meet-and-confer), and the request for a conference.
3. **Issue-by-issue.** For each deficiency:
   - Heading: "Issue {N}: {Short title — e.g., 'RFP Nos. 7, 12, 15 — Boilerplate Objections'}"
   - Quote the relevant request and response (or summarize, but quoting is stronger).
   - Identify the rule violated with provision.
   - Identify the cure requested.
   - Set a date for cure.
4. **Privilege-log specific issues** (if any) — separate section because the analytical move is different.
5. **Custodian / source-system issues** (if any) — list of additional custodians, identification of unproduced systems.
6. **Schedule a meet-and-confer.** Propose two specific times complying with local rule.
7. **Closing.** State that if the issues are not resolved by {date}, the issuing party intends to move to compel under Rule 37.

---

## Output Format

```markdown
{LAW FIRM LETTERHEAD or EMAIL HEADER}

{date}

VIA EMAIL

{recipient counsel}
{firm}
{address}

Re: {Matter}, Case No. {…} — Meet-and-Confer Regarding Plaintiff's First Requests for Production and First Set of Interrogatories

Dear {Counsel}:

We write under Federal Rule of Civil Procedure 37(a)(1) and {Local Rule N} regarding deficiencies in {Defendant}'s {Responses dated {date}}. We propose a telephone conference to resolve these issues no later than {date}. If the issues identified below are not resolved by {date}, Plaintiff intends to seek relief from the Court.

ISSUE 1: BOILERPLATE OBJECTIONS — RFP NOS. 7, 12, 15

{Defendant}'s response to RFP No. 7, which seeks "{quoted text from RFP}," reads in full: "{quoted response, including the boilerplate objection stack}." {Defendant} has provided no specific objection grounds and has not indicated whether responsive material is being withheld.

Federal Rule 34(b)(2)(B)–(C) requires that objections "state with specificity the grounds" and that the response "state whether any responsive materials are being withheld on the basis of [the] objection." {Defendant}'s response satisfies neither requirement. {See [CITE: ... boilerplate-objection authority in this district].}

We request that {Defendant} (a) supplement its responses to RFP Nos. 7, 12, and 15 with specific objection grounds, (b) state with respect to each whether responsive materials are being withheld on the basis of the objection, and (c) produce all responsive non-privileged documents within {Defendant}'s possession, custody, or control no later than {date}.

ISSUE 2: PRIVILEGE LOG — INSUFFICIENT DESCRIPTIONS

{Defendant}'s privilege log dated {date} contains {N} entries with descriptions reading only "Communication providing legal advice" or "Work product." These descriptions do not satisfy Rule 26(b)(5)(A)(ii), which requires sufficient detail to enable assessment of the privilege claim. {See [CITE: ...].}

We request that {Defendant} supplement the privilege log to include, for each entry: (a) author and recipient roles; (b) the subject of the communication described non-privilegedly; (c) for work-product entries, the litigation anticipated and the anticipation date. Supplementation requested by {date}.

ISSUE 3: CUSTODIAN COVERAGE

{Defendant}'s production includes documents from custodians {A, B, C} but excludes {D, E, F}, who appear in {documents Bates X, Y, Z} as participants in the events at issue. We request that {Defendant} (a) confirm whether {D, E, F} were collected, (b) if not, collect and produce, and (c) confirm by {date}.

ISSUE 4: ESI SOURCES — CHAT AND MOBILE DEVICES

{Defendant}'s production does not include Slack, Microsoft Teams, or text-message data, despite the parties' ESI Protocol identifying these as collectable sources. Please confirm whether these sources have been collected and the timeline for production.

CONFERENCE

Please let us know by {date} which of the following times you are available for a telephonic meet-and-confer: {Time 1; Time 2}. If neither works, please propose two alternatives within the same week.

If we do not reach resolution by {date}, Plaintiff will move to compel under Rule 37(a)(3) and seek the available fee-shifting under Rule 37(a)(5).

Sincerely,

/s/ {counsel}
{name, bar no., firm, contact}
```

---

## Verification

- [ ] Each issue identifies the request number, quotes the deficiency, cites the rule violated, and proposes a specific cure with a date.
- [ ] Privilege-log issues addressed with the controlling specificity requirement.
- [ ] Custodian and ESI-source gaps listed concretely, not abstractly.
- [ ] Two specific conference times proposed, complying with local rule.
- [ ] Closing identifies the next-step deadline and the relief that will be sought.
- [ ] Letter is structured for surgical response, not as a rolling grievance.
- [ ] No invented case citations; missing citations flagged with placeholders.
- [ ] Tone matches the requested register without rhetorical excess.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Citing "the rules" without provision-level specificity | Cite to subsection (e.g., Rule 34(b)(2)(C); Rule 26(b)(5)(A)(ii)) |
| Demanding cure within an unreasonable window | Match the size of the cure to the timeframe |
| Bundling all deficiencies into one paragraph | One issue per heading; let the reader address each surgically |
| Performative hostility | Undermines the cooperative-attempt requirement and weakens any later 37(a)(5) fee request |
| Forgetting to indicate next-step relief | Without the specific motion threat, the letter loses leverage |
| Conceding scope by accepting a narrowed interpretation in passing | Avoid; reserve scope arguments |
| Failing to comply with local in-person/telephonic conference rules | Many districts require live conference; emails-only do not satisfy |
