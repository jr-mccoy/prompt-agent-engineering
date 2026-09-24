---
title: "Brady/Giglio Request and Disclosure Tracking Framework"
category: legal/criminal
description: "Build a defense-side Brady/Giglio program for a criminal file: a specific, item-by-item disclosure request letter or motion, a tracker that logs each requested category through response, production, and follow-up, and a gap analysis that ties favorable-evidence categories to the case's contested elements and witnesses — without asserting materiality conclusions or inventing authority."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - criminal
  - brady
  - giglio
  - discovery
  - impeachment
  - hidden-evidence
updated: "2026-09-24"
related_prompts:
  - domain-legal/criminal/legal_bwc_review_protocol.md
  - domain-legal/criminal/legal_motion_to_suppress.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-legal/discovery/legal_privilege_log_generator.md
---

**Objective:** Give defense counsel a specific, case-tailored request for favorable evidence and impeachment information, plus a living tracker that records what was asked for, what the government said, what was produced, and what remains — so gaps are visible, follow-up is timely, and any later motion to compel or for relief rests on a documented record.

> **Scope guard — attorney-facing only.** For licensed counsel on the matter (defense counsel, or the prosecutor where a government posture is offered). If the person running it appears to be an unrepresented defendant or a family member, stop and route them to the public defender's office or appointed counsel, or to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`, rather than producing strategy. This guard is not a disclaimer; the ban on "consult an attorney" boilerplate below still applies.

**When to Use:** At arraignment or initial discovery; after the court issues a disclosure order (e.g., a Fed. R. Crim. P. 5(f) order in federal court `[VERIFY: current rule text]`); when new witnesses or theories emerge; before trial to confirm impeachment disclosures for each government witness; when preparing a motion to compel or for sanctions.

**Distinct from:**
- `domain-legal/discovery/legal_meet_and_confer_letter.md` — civil discovery dispute correspondence under the civil rules; criminal disclosure rests on constitutional duties, criminal rules, and statutes with different scope and timing.
- `domain-legal/discovery/legal_privilege_log_generator.md` — logs withheld civil documents; this tracker logs requested favorable-evidence categories.
- `domain-legal/criminal/legal_bwc_review_protocol.md` — surfaces favorable items from video; those items feed this tracker.

---

## Your Input

- **Jurisdiction and court:** [Required]
- **Governing disclosure sources:** [Constitutional duty; criminal discovery rule; Jencks-type statute; local rules; standing or case-specific disclosure order — supply text where available]
- **Charges and contested elements:** [What the defense disputes]
- **Government witnesses:** [Law enforcement, cooperators, informants, experts, lay witnesses — with roles]
- **Defense theory:** [Identity, self-defense, lack of intent, entrapment, reliability of forensic evidence, etc.]
- **Already produced:** [Bates ranges and descriptions]
- **Known leads:** [Items the defense believes exist — other suspects, prior inconsistent statements, lab issues, benefits to witnesses]
- **Deadlines:** [Court-ordered or rule-based, as supplied]

---

## Constraints

**Must:**
- Make every request **specific**: tie each category to a named witness, element, event, or document rather than "all Brady material."
- Cover, where the facts support it: statements inconsistent with the government's theory; other-suspect information; identification failures; forensic/lab bench notes, validation, proficiency, and error records; benefits, promises, or leniency to witnesses (including immigration or charging benefits); informant files and payments; prior false statements or adverse credibility findings for law-enforcement witnesses; witness criminal history and pending cases; mental-health or substance issues bearing on perception, where authority supports disclosure `[VERIFY]`.
- Distinguish in the tracker the source of each obligation (constitutional, rule, statute, order) as supplied by the user.
- Log each request through statuses: Requested → Responded → Produced (Bates) / Refused / Claimed none / Deferred to trial → Follow-up.
- Note timing: request that impeachment information be disclosed in time for effective use, and record the government's stated timing.
- Keep a separate list of items that may require an in-camera review request.

**Must Not:**
- State that an item "is Brady material" or "is material" as a conclusion; describe it as favorable and explain why, leaving materiality for the court `[VERIFY: standard]`.
- Invent case citations, rule subsections, disclosure deadlines, or the content of a court's order.
- Use boilerplate catch-all requests as a substitute for specific ones (a catch-all may be added at the end, not instead).
- Accuse the prosecution of suppression without a documented basis in the tracker.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Map theory to proof.** For each contested element, list what favorable evidence would look like and which witness or agency would hold it.
2. **Witness credibility grid.** For each government witness: role, possible impeachment categories, known leads, holder of the information.
3. **Draft the request.** Numbered, specific paragraphs grouped by category, each citing the supplied obligation source `[CITE]` and the case-specific reason.
4. **Build the tracker.** One row per numbered request; status, dates, Bates, government response quoted.
5. **Gap analysis.** After each production: requested-but-missing, produced-but-incomplete, newly suggested categories, and in-camera candidates.
6. **Escalation path.** For each unresolved gap: follow-up letter → motion to compel / for in-camera review → request for continuance or other relief, each with the record the motion will rely on.

---

## Output Format

```markdown
# PART A — DISCLOSURE REQUEST
[Letterhead / caption as appropriate]
Re: {Case} — Request for Favorable Evidence and Impeachment Information

Obligation sources relied on: {as supplied} [CITE]

1. {Specific request — witness/element/event — and why it bears on the defense}
2. ...
{Timing request for impeachment information}
{Catch-all, last}

# PART B — TRACKER
| Req # | Category | Tied to (element / witness) | Obligation source | Requested | Govt response (quoted) | Status | Bates | Next step / date |

# PART C — WITNESS CREDIBILITY GRID
| Witness | Role | Impeachment categories | Leads | Holder | Req # |

# PART D — GAP ANALYSIS (as of {date})
- Missing: {...}
- Incomplete: {...}
- New categories suggested by production: {...}
- In-camera candidates: {...}

# PART E — ESCALATION PLAN
| Gap | Follow-up | Motion basis (record cites) | Timing |
```

---

## Worked Example (abbreviated)

**Input:** Federal robbery case; identity contested. Government witnesses: a cooperating co-defendant, the store clerk (eyewitness), and a detective who ran a photo array. Produced: reports and the array itself (Bates 0001–0240). Leads: the clerk described a taller man in the 911 call; the cooperator has a pending state case.

**Output excerpt:**
- Request 3: "The 911 recording and CAD notes for the call placed by [clerk] at the time of the incident, and any notes of any officer's conversation with [clerk] describing the suspect's height, build, or clothing" — tied to identity; lead: 911 description.
- Request 5: "All benefits, promises, or understandings, formal or informal, offered to [cooperator], including any communication with state prosecutors concerning the pending state case" — tied to cooperator credibility `[CITE: supplied Giglio-line authority]`.
- Request 7: array administration records: instructions given, confidence statement, whether administrator was blind `[VERIFY: jurisdiction's identification-procedure rules]`.
- Tracker row 5: status "Claimed none — 2026-09-10 letter quoted"; next step: follow-up asking whether the inquiry included the state prosecutor's office.
- Gap analysis: 911 audio not produced; in-camera candidate: cooperator's proffer notes.

---

## Verification

- [ ] Jurisdiction lock; obligation sources match what the user supplied.
- [ ] Every request is specific and tied to an element or witness.
- [ ] Each government witness has a credibility-grid row.
- [ ] Tracker statuses and government responses are quoted, dated, and Bates-linked.
- [ ] No materiality conclusions; no invented rules, orders, or deadlines.
- [ ] Gap analysis and escalation plan updated after each production.
- [ ] Catch-all request appears only after the specific requests.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| A one-paragraph "all Brady material" request | Specific numbered requests tied to witnesses, elements, and events |
| Declaring items "material" in the request | Describe why the item is favorable; materiality is for the court `[VERIFY]` |
| Treating Jencks-type statement timing as the Brady timing | Track each obligation's source and timing separately as supplied |
| Forgetting law-enforcement witness credibility information | Credibility grid includes every officer who will testify |
| Accepting "none exists" without scope | Follow up on which offices, agencies, and files were searched |
| Losing track of what was produced | Tracker records Bates, dates, and quoted responses for every request |
| Citing a disclosure rule subsection from memory | Use the user-supplied text or mark `[VERIFY: rule text]` |
| Requesting cooperator information without naming benefit types | List formal and informal benefits, pending cases, immigration, and payments |
