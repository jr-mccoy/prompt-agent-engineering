---
title: "Motion to Compel Discovery Drafter"
category: legal/discovery
description: "Draft a motion to compel discovery responses or production — request-by-request deficiency log, meet-and-confer record, relevance and proportionality showing, and an expense-shifting request with a fee declaration — the filing that follows the Rule 37 deficiency letter rather than the letter itself."
techniques:
  - DT-05
  - RT-05
  - QA-08
  - ST-03
difficulty: advanced
tags:
  - legal
  - discovery
  - motion-to-compel
  - rule-37
  - deficiency-log
  - other-side-wont-answer-discovery
  - incomplete-document-production
updated: "2026-09-24"
related_prompts:
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-legal/discovery/legal_privilege_log_generator.md
  - domain-legal/depositions/legal_deposition_outline_30b6.md
---

# Motion to Compel Discovery Drafter

**Objective:** Convert a failed meet-and-confer into a motion the court can decide request by request: each disputed request quoted with the response and the specific deficiency, the relevance of the withheld material tied to a claim or defense, the proportionality showing, a conferral record that satisfies the certification requirement, and a supported request for the expenses the rule makes available.

> **Scope guard — attorney-facing.** For counsel of the requesting party. It assumes discovery was properly served and a good-faith conferral occurred. A self-represented litigant should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- Responses are late, evasive, incomplete, or rest on boilerplate objections, and the deficiency letter did not cure them.
- A privilege log is missing or inadequate after a documented request.
- A corporate designee appeared unprepared on noticed topics and you seek a further deposition.
- A nonparty has not complied with a subpoena (motion in the compliance court `[VERIFY]`).

**Not this prompt if:**
- You have not yet sent a deficiency letter — use `domain-legal/discovery/legal_meet_and_confer_letter.md` first; most forums require it.
- You are resisting discovery — use `domain-legal/discovery/legal_motion_for_protective_order_drafter.md`.
- You are seeking sanctions for lost ESI or violation of a prior order — that is a different standard; flag and stop.

## Inputs

- **Jurisdiction and court (required):** Court, judge, operative rules (FRCP 37(a) or state analog), and local procedure for discovery disputes — pre-motion conference, joint statement or stipulation format, page limits, and any deadline relative to the discovery cutoff `[VERIFY]`.
- **Requests and responses:** Verbatim text of each disputed request, the response, and objections; service dates.
- **Conferral record:** The deficiency letter(s), responses, call dates and attendees, and any partial agreements.
- **Relevance theory:** For each request, the claim or defense it bears on and what you expect it to show.
- **Production facts:** What has been produced (Bates ranges), gaps observed (date gaps, missing custodians, missing attachments), privilege log status.
- **Expense data:** Time spent on the conferral and motion, by timekeeper, with rates.

## Method

**Ground rules:** No invented case names, holdings, or quotations — `[CITE: proposition]` / `[NEED PIN: …]`. Do not state deadlines, page limits, or joint-statement requirements not supplied — `[VERIFY: …]`. Quote requests and responses verbatim; never paraphrase the other side's response in a way that changes it.

1. **Gate: is the motion ripe?** Confirm (a) the requests were served and responses were due, (b) a deficiency letter identified each item now in dispute, (c) a live conferral occurred if the forum requires one `[VERIFY]`, and (d) the motion is timely relative to the discovery cutoff `[VERIFY]`. If any gate fails, stop and list what to do first.
2. **Build the deficiency log.** One row per disputed request: request text, response/objection, deficiency category (no response; boilerplate objection; objection without stating whether material is withheld; evasive or incomplete answer; improper privilege assertion; production gap), what you asked for in conferral, the other side's last position, and the specific order you want.
3. **Narrow before you file.** Drop requests where the dispute is minor or you already have the material; narrow requests you offered to narrow in conferral, and say so. Courts notice when a motion seeks more than was discussed.
4. **Relevance and proportionality.** For each request (or group of related requests), connect the material to a claim or defense and address the proportionality factors that the responding party put at issue `[VERIFY: operative rule]`. Burden arguments the other side did not support with facts are noted as unsupported.
5. **Objection-specific responses.** Boilerplate objections: show they lack the required specificity. Privilege: show the log is missing or insufficient and ask for a compliant log by a date. "Will produce" with no date: ask for a date certain.
6. **Draft the conferral certification.** Dates, participants, items resolved, items unresolved, and a neutral description of the impasse.
7. **Expenses.** Request the reasonable expenses, including attorney's fees, that the operative rule provides for when a motion is granted or discovery is provided after filing `[VERIFY: FRCP 37(a)(5) or analog, and its exceptions]`; attach a fee declaration with entries limited to the conferral and motion.
8. **Proposed order.** Request-by-request, with a compliance date and the form of production.
9. **If the forum requires a joint statement,** restructure the output so each request is followed by the moving party's and responding party's positions, leaving the latter for opposing counsel.

## Output Format

```markdown
# Motion to Compel Package — {Caption}

## 1. Ripeness Gate
| Check | Status | Source |
(served / due / deficiency letter covers item / live conferral / timeliness [VERIFY])

## 2. Deficiency Log
| Req. # | Request (verbatim) | Response/objection (verbatim) | Deficiency category | Conferral ask | Their last position | Order sought |

## 3. Notice of Motion
## 4. Memorandum
I. Introduction — what is sought, in one paragraph
II. Background — discovery served; conferral history
III. Legal Standard [CITE placeholders]
IV. Argument
   A. {Group 1: requests __–__} — relevance → deficiency → proportionality
   B. {Group 2} ...
   C. Expenses Should Be Awarded
V. Conclusion
## 5. Conferral Certification
## 6. Fee Declaration (conferral + motion time only)
| Date | Timekeeper | Hours | Task | Rate |
## 7. [Proposed] Order — request by request, with compliance date
## 8. Verification Items
```

## Verification

- [ ] Jurisdiction lock: rule, local dispute procedure, and format (motion vs. joint statement) tied to the stated forum.
- [ ] Citation discipline: no invented authority; placeholders where not supplied.
- [ ] Scope discipline: only items raised in the deficiency letter and conferral are in the motion.
- [ ] Ripeness gate passed or failures reported.
- [ ] Every row quotes the request and response verbatim.
- [ ] Each request group has a relevance tie to a named claim or defense.
- [ ] Expense request supported by a fee declaration limited to recoverable tasks.
- [ ] Proposed order specifies a date and form of production per request.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Moving on items never raised in conferral | Scope to the deficiency letter; add new items only after conferring |
| Paraphrasing the other side's responses | Quote verbatim in the log |
| Arguing "relevant" without tying to a claim or defense | Name the element or defense for each group |
| Omitting the expense request or its support | Include the request and a fee declaration |
| Ignoring a joint-statement or pre-motion-conference rule | Check local procedure in the ripeness gate |
| Seeking more than was requested | Proposed order mirrors the (narrowed) requests |

## Example

**Input sketch:** Federal employment case. Plaintiff (fictional) Dana Oyelaran served RFP 4 (her personnel file) and RFP 9 (communications among three named managers about her termination, 2025). Defendant Corvid Health Systems responded to RFP 9: "Objection, overbroad, unduly burdensome, seeks privileged information. Subject to and without waiving, Defendant will produce responsive non-privileged documents." Nothing produced after 60 days; no privilege log. Deficiency letter 2026-08-12; call 2026-08-20.

**Output (abridged):**

> **Deficiency log, RFP 9.** Deficiency category: boilerplate objections; does not state whether material is withheld; no production; no privilege log. Conferral ask: production and log within 14 days. Their last position: "working on it." Order sought: produce within 14 days of the order; serve a compliant privilege log for any withheld item.
>
> **Argument IV.A (excerpt).** RFP 9 is limited to three custodians and a single year. It seeks the decision-makers' communications about the termination, which bear directly on whether the stated reason was pretextual. Corvid's objection does not identify any burden with facts and does not state whether documents are being withheld on the basis of its objections `[VERIFY: FRCP 34(b)(2)(C)]`.
>
> **Expenses.** Plaintiff requests her reasonable expenses in making this motion `[VERIFY: FRCP 37(a)(5)(A)]`, supported by the attached declaration (6.4 hours).
