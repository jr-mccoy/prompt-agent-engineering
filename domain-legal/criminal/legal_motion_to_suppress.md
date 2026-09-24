---
title: "Motion to Suppress — Fourth, Fifth, and Sixth Amendment Grounds"
category: legal/criminal
description: "Draft a defense motion to suppress evidence or statements on Fourth Amendment (search/seizure), Fifth Amendment (Miranda/voluntariness), or Sixth Amendment (right to counsel) grounds — with standing, a record-cited factual basis, ground-by-ground argument, anticipated government exceptions, and an evidentiary-hearing request — using only authority the user supplies."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - criminal
  - motion-to-suppress
  - fourth-amendment
  - miranda
  - exclusionary-rule
  - illegal-search
updated: "2026-09-24"
related_prompts:
  - domain-legal/criminal/legal_bwc_review_protocol.md
  - domain-legal/criminal/legal_brady_giglio_review_request.md
  - domain-legal/litigation/legal_motion_in_limine_set.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Objective:** Produce a filing-ready motion to suppress (with supporting memorandum and hearing request) for defense counsel, in which every factual assertion is anchored to a discovery source, every legal proposition carries user-supplied authority or a placeholder, and each constitutional ground is argued separately with its own standing, violation, causation, and remedy analysis.

> **Scope guard — attorney-facing only.** For licensed counsel on the matter (defense counsel, or the prosecutor where a government posture is offered). If the person running it appears to be an unrepresented defendant or a family member, stop and route them to the public defender's office or appointed counsel, or to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`, rather than producing strategy. This guard is not a disclaimer; the ban on "consult an attorney" boilerplate below still applies.

**When to Use:** After initial discovery (reports, warrants and affidavits, BWC/dash-cam, interrogation recordings) is in hand and counsel has identified a search, seizure, statement, or identification that may be unlawful; before the pretrial-motion deadline; when preparing for a suppression hearing.

**Distinct from:**
- `domain-legal/litigation/legal_motion_in_limine_set.md` — evidentiary-rule exclusion (FRE 403/404/702) at trial; this prompt is constitutional exclusion before trial.
- `domain-legal/research/legal_research_memo_irac.md` — an internal research memo; this prompt drafts the court filing.
- `domain-legal/criminal/legal_bwc_review_protocol.md` — mines the footage for suppression hooks; this prompt turns those hooks into a motion.
- `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_police_report_account_preparer.md` — a layperson reporting a crime; this prompt is practitioner-only defense work, never advice to a defendant acting without counsel.

---

## Your Input

- **Jurisdiction and court:** [Federal district / state court + county — required]
- **Controlling constitutional and state provisions:** [U.S. Const. amends. IV / V / VI and any state constitutional analog the user wants argued separately]
- **Charges:** [Counts and statutes]
- **Evidence to suppress (one row per item):** [Physical item / statement / identification / digital data — with where and when obtained]
- **Factual sources:** [Police reports, warrant + affidavit, CAD logs, BWC timestamps, interrogation transcript, witness statements — with Bates or exhibit numbers]
- **Client's connection to the place/item searched:** [Ownership, residence, overnight guest, driver/passenger, account holder — for standing]
- **Authority supplied:** [Cases, statutes, rules the user has pulled and verified]
- **Local rules:** [Motion deadline, page limits, whether a hearing must be requested in the motion, affidavit requirements]
- **Posture notes:** [Anything already conceded, prior rulings, co-defendant motions]

---

## Constraints

**Must:**
- Argue each ground (e.g., warrantless entry; stop exceeded scope; Miranda violation; involuntariness; post-charge interrogation without counsel) in its **own section** with its own standing, violation, and fruit analysis.
- Cite a discovery source for every factual sentence: `(Rpt. of Ofc. X at 3)`, `(BWC-1 at 00:14:22)`, `(Bates DEF-0042)`.
- Address **standing / reasonable expectation of privacy** before merits for every Fourth Amendment ground.
- Anticipate the government's likely exceptions (consent, exigency, search incident to arrest, automobile, plain view, inventory, good faith, inevitable discovery, independent source, attenuation, public safety) and respond only to those the facts make plausible.
- Identify the **burden allocation** for each ground as a `[VERIFY: burden and standard in {jurisdiction}]` item unless the user supplies authority.
- Request an evidentiary hearing and state the specific disputed facts that require one.
- Treat state constitutional grounds as separate arguments when the user supplies them; never assume a state provision is co-extensive with the federal one.

**Must Not:**
- Invent case names, holdings, pin cites, statutory text, burdens, or deadlines. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[NEED HOLDING: ...]`, `[VERIFY: ...]`.
- Assert facts not in the supplied sources, or characterize officer credibility without a documented inconsistency.
- Draft the motion for, or give strategy to, a defendant proceeding without counsel; the output is for defense counsel.
- Bundle unrelated violations into one argument or seek suppression of evidence not causally linked to the alleged illegality.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Build the suppression inventory.** Table: item → how obtained → constitutional ground(s) → standing basis → causal link → likely government exception.
2. **Fix the timeline.** Order events by timestamp from the sources; mark conflicts between sources (report says 22:10, BWC shows 22:14) as `CONFLICT` rows — these become hearing issues.
3. **Standing screen.** For each Fourth Amendment item, state the client's interest and the source that proves it. Drop items with no supportable standing and say why.
4. **Ground-by-ground argument.** For each ground: rule `[CITE]` → facts (cited) → application → why the likely exception fails on these facts.
   - **Warrant-affidavit branch (Franks-type challenge), only if the evidence was seized under a warrant.** If the sources show a statement in the affidavit was false, or a material fact was omitted, identify each one, the source showing it, and why the affiant knew or recklessly disregarded it; then test whether probable cause survives with the false statement excised (or the omission added). A hearing on this ground requires a substantial preliminary showing, usually supported by offers of proof or affidavits — list what the defense can attach `[VERIFY: standard and offer-of-proof requirements in {jurisdiction}]`. Negligence or innocent mistake is not enough; do not plead this branch on a bare inconsistency.
5. **Fruit analysis.** Trace derivative evidence from each primary illegality; address attenuation factors only as the user's authority frames them.
6. **Remedy and hearing request.** Specify exactly what is to be suppressed and the disputed facts requiring testimony.
7. **Risk note (internal, not filed).** What the motion discloses about defense theory; any testimony the client would need to give on standing and its use-limits `[VERIFY: use-immunity rule for suppression testimony in {jurisdiction}]`.

---

## Output Format

```markdown
# SUPPRESSION INVENTORY (internal)
| # | Evidence | Obtained (when/how, source) | Ground | Standing basis | Causal link | Likely exception |
|---|---|---|---|---|---|---|

# TIMELINE (internal)
| Time | Event | Source | Conflict? |

---
[CAPTION]
DEFENDANT'S MOTION TO SUPPRESS {EVIDENCE / STATEMENTS} AND REQUEST FOR EVIDENTIARY HEARING

## Introduction
{Relief sought, grounds, one paragraph.}

## Statement of Facts
{Chronological, every sentence cited to a source.}

## Argument
### I. {Ground 1 — e.g., The warrantless entry into the residence violated the Fourth Amendment}
A. Standing — {...}
B. The {search/seizure} was unlawful — {rule [CITE]; application}
C. No exception applies — {each plausible exception, answered}
D. Fruits — {derivative evidence}
### II. {Ground 2}
{...}

## Request for Evidentiary Hearing
{Numbered disputed facts requiring testimony.}

## Conclusion
{Itemized suppression order requested.}

---
# INTERNAL RISK NOTE
- Theory disclosure: {...}
- Standing testimony: {...} [VERIFY: ...]
- Open placeholders: {list every [CITE]/[VERIFY]}
```

---

## Worked Example (abbreviated)

**Input:** State court; possession with intent charge. Officer stopped a car for a lane violation at 01:12 (report). BWC shows the citation was printed at 01:19; the officer then asked for consent, was refused, and held the driver (client, registered owner) for a K-9 that arrived 01:41. The dog alerted; cocaine found in the trunk. Client later said "it's mine" in the cruiser without warnings. User supplies authority on stop-prolongation and custodial interrogation.

**Output excerpt:**
- Inventory row 1: Cocaine (trunk) → Fourth Amendment, prolonged detention → standing: registered owner and driver (DMV record, Bates 0007) → causal: found only after K-9 sniff during extension → likely exception: independent reasonable suspicion.
- Timeline conflict: report says "K-9 arrived shortly"; BWC-1 00:29:10 shows 22-minute wait after citation was complete → hearing issue #1.
- Argument I.C answers reasonable suspicion: the report lists "nervousness" only; no other articulable fact appears in any source `[CITE: user-supplied authority on nervousness alone]`.
- Argument II (statement): in-cruiser, handcuffed per BWC-1 00:31:02, no warnings in any recording → custody is well supported, but interrogation is not yet shown: no source records what preceded "it's mine" `[NEED: whether the statement responded to questioning or its functional equivalent]`. Argue custodial interrogation only if the BWC audio or reports show a question or its functional equivalent `[CITE]`; if the statement was volunteered, rely on the fruit-of-Ground-I argument alone.
- Internal note: `[VERIFY: whether state constitution provides broader protection against prolonged stops in {state}]` — user did not supply authority, so it is flagged, not argued.

---

## Verification

- [ ] Jurisdiction lock: court, constitutional provisions, and any state analog match the user's input.
- [ ] Every factual sentence carries a source cite; conflicts between sources are surfaced, not smoothed.
- [ ] Standing addressed first for each Fourth Amendment ground.
- [ ] Each ground argued separately with its own fruit analysis.
- [ ] Only plausible exceptions addressed, each answered with cited facts.
- [ ] No invented authority, burdens, or deadlines; all gaps are placeholders listed in the risk note.
- [ ] Relief is itemized and matches the inventory.
- [ ] Audience is defense counsel; no advice to an unrepresented defendant.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Arguing a Fourth Amendment violation without establishing the client's standing | Standing section first; drop items where no source supports an interest |
| Treating Miranda and voluntariness as one claim | They are distinct grounds with distinct remedies and impeachment consequences; argue separately |
| Invoking the Sixth Amendment for pre-charge questioning | Flag the attachment question as `[VERIFY: attachment point]` rather than assuming the right had attached |
| Smoothing a report/BWC timing conflict into one narrative | Record both versions with sources and make the conflict a hearing issue |
| Addressing every textbook exception at length | Answer only the exceptions the facts make plausible; long boilerplate buries the strong ground |
| Asserting the officer "lied" | Describe the documented inconsistency; credibility is for the hearing |
| Seeking suppression of evidence with no causal link to the illegality | Tie each item to the violation or drop it; overreach costs credibility |
| Filling a missing burden or good-faith rule from memory | Use `[VERIFY]`/`[CITE]` and list it in the risk note |
