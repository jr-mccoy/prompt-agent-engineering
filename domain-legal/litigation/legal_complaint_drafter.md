---
title: "Civil Complaint Drafter"
category: legal/litigation
description: "Draft a federal or state civil complaint with caption, jurisdictional allegations, parties, factual allegations, claims (with elements), demand for relief, and signature block — sized to the pleading standard of the controlling jurisdiction."
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
  - litigation
  - complaint
  - pleading
  - drafting
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_answer_with_affirmative_defenses.md
  - domain-legal/litigation/legal_motion_to_dismiss_12b6.md
  - domain-legal/research/legal_issue_spotter_from_facts.md
---

**Purpose:** Draft a complaint to file. Output sized to the controlling pleading standard — Twombly/Iqbal plausibility for federal court, the user's state's standard for state court (notice pleading, code pleading, fact pleading).

**When to use:** Initiating litigation, drafting amended complaints after a granted motion to dismiss, training/evaluation tasks where the goal is producing a filable pleading.

---

## Your Input

- **Court / venue:** [Federal district + division, or state court + county]
- **Pleading standard:** [Federal plausibility / state notice / state code / state fact-pleading]
- **Parties:** [Plaintiff(s) and defendant(s) with addresses or "to be redacted" placeholders, business form, citizenship for diversity]
- **Subject-matter jurisdiction theory:** [Federal question with statute / diversity with amount in controversy / supplemental / state court of general jurisdiction]
- **Personal jurisdiction theory:** [General / specific with contacts / consent / long-arm + due process]
- **Venue theory:** [Statutory provision]
- **Claims to plead:** [List — with the substantive law (federal statute, state common law, etc.) controlling each]
- **Operative facts:** [Chronology — events, communications, transactions, harm, damages]
- **Documents to attach or quote:** [Contracts, policies, communications]
- **Damages / relief sought:** [Compensatory, statutory, punitive, injunctive, declaratory, fees, costs]
- **Jury demand:** [Yes / no]
- **Pre-suit notice or exhaustion completed:** [If any required]

---

## Constraints

**Must:**
- Open with caption matching the court's local rules format.
- Plead jurisdiction, venue, and parties in numbered paragraphs before factual allegations.
- Use **numbered paragraphs** throughout; one fact per paragraph as a default.
- For each claim, plead the elements in the order required by controlling law and tie supplied facts to each element.
- Match the pleading standard:
  - **Federal plausibility (Twombly/Iqbal):** factual allegations sufficient to render the claim plausible, not conclusory recitations of elements.
  - **State notice pleading:** short and plain statement of facts and claim.
  - **State code/fact pleading:** ultimate facts pleaded for each element.
- Include a separate count for each claim, captioned (e.g., "Count I — Breach of Contract").
- Include a demand for relief that matches the claims.
- Include jury demand if requested.
- Include the signature block, court bar number placeholder, and certification placeholders required by local rules.

**Must Not:**
- Plead legal conclusions in lieu of facts (e.g., "Defendant breached the contract" without facts showing the breach).
- Plead claims not supported by supplied facts.
- Cite cases inside the complaint absent a specific local-rule allowance — complaints generally do not cite case law in the body.
- Invent parties, dates, contract terms, or harm.
- Combine multiple claims into a single count.
- Demand relief not available for the claim pleaded (e.g., punitive damages where the substantive law forecloses them).
- Insert generic "consult counsel" disclaimers — this is a filable pleading.

---

## Instructions

1. **Caption.** Court, parties, case number placeholder, document title, jury demand designation.
2. **Introduction (optional, often used in federal court).** One short paragraph summarizing the dispute. Avoid argument.
3. **Parties.** One numbered paragraph per party with citizenship/residence and business form.
4. **Jurisdiction.** Numbered paragraphs identifying subject-matter jurisdiction, personal jurisdiction, and (where appropriate for the form) Article III standing facts.
5. **Venue.** Statutory basis with facts.
6. **Factual Allegations.** Numbered, chronological where possible. One fact per paragraph as a default. Quote contract or policy language verbatim where relied on.
7. **Claims (Counts).** Each count includes:
   - Caption ("Count I — {Claim} (Against Defendant {X})")
   - Incorporation of prior paragraphs by reference.
   - Numbered paragraphs walking through each element with supplied facts.
   - Allegation of damages or entitlement to relief specific to the count.
8. **Demand for Relief.** Itemized: compensatory damages, statutory damages, punitive (if available and pleaded), injunctive, declaratory, attorneys' fees and costs (only if a fee-shifting basis exists), pre- and post-judgment interest.
9. **Jury Demand.** If requested.
10. **Signature block, certification placeholders (e.g., Rule 11), exhibit list.**

---

## Output Format

Use the court's standard format. Default federal template below; adapt to state court if specified.

```markdown
UNITED STATES DISTRICT COURT
{DISTRICT} OF {STATE}
{DIVISION}

{PLAINTIFF},
                                        Plaintiff,
v.                                                  Case No. ____________
{DEFENDANT},
                                        Defendant.

COMPLAINT
JURY TRIAL DEMANDED

Plaintiff {Name}, by and through undersigned counsel, alleges as follows:

I. INTRODUCTION
1. {short paragraph}

II. PARTIES
2. Plaintiff is ...
3. Defendant is ...

III. JURISDICTION AND VENUE
4. This Court has subject-matter jurisdiction under {28 U.S.C. § ____} because ...
5. This Court has personal jurisdiction over Defendant because ...
6. Venue is proper in this District under {28 U.S.C. § 1391(b)(__)} because ...

IV. FACTUAL ALLEGATIONS
7. ...
8. ...
{numbered chronologically}

V. CLAIMS FOR RELIEF

COUNT I — {Claim} (Against {Defendant})
{N}. Plaintiff incorporates paragraphs 1 through {N-1} as if fully set forth herein.
{N+1}. {Element 1 with supporting facts}
{N+2}. {Element 2 with supporting facts}
...
{N+k}. As a direct and proximate result, Plaintiff suffered {damages}.

COUNT II — {Claim} (Against {Defendant})
{...}

VI. DEMAND FOR RELIEF
WHEREFORE, Plaintiff respectfully requests that this Court enter judgment as follows:
A. {Compensatory damages in an amount to be proven at trial};
B. {Statutory damages under {statute}};
C. {Injunctive relief: ...};
D. {Declaratory relief: ...};
E. {Pre- and post-judgment interest};
F. {Reasonable attorneys' fees and costs under {fee-shifting authority}};
G. Such further relief as the Court deems just and proper.

VII. JURY DEMAND
Plaintiff demands trial by jury on all issues so triable.

Dated: {date}                       Respectfully submitted,

                                    /s/ {attorney name}
                                    {Bar No.}
                                    {Firm}
                                    {Address, phone, email}
                                    Counsel for Plaintiff
```

---

## Verification

- [ ] Pleading standard correctly applied (federal plausibility / state notice / state code).
- [ ] Subject-matter jurisdiction, personal jurisdiction, and venue separately pleaded with statutory bases.
- [ ] Each count separately captioned with the claim and the defendant(s).
- [ ] Each count walks through the claim's elements with supplied facts.
- [ ] No case citations in the body of the complaint absent a local-rule reason.
- [ ] No invented parties, dates, terms, or harm.
- [ ] Damages and relief match what is available for each pleaded claim.
- [ ] Jury demand and signature block present where applicable.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Pleading "Defendant breached the contract" without the operative term and the alleged breach | Quote the operative term, allege the conduct that breached it, and tie to damages |
| Treating notice pleading as license to plead conclusions | Even notice-pleading jurisdictions require facts sufficient to give notice of the claim |
| Citing cases inside the complaint | Most jurisdictions disfavor this in the body; legal authority is for briefs, not pleadings |
| Combining counts | Each claim gets its own count; alternative theories are separately captioned |
| Demanding punitive damages without a substantive-law basis | Many claims foreclose punitives — verify against the controlling law |
| Pleading diversity without amount-in-controversy facts | $75,000+ for federal diversity must be pleaded with facts, not asserted |
| Skipping pre-suit notice or exhaustion | Plead compliance facts where the claim has a notice/exhaustion prerequisite |
| Demanding fees without a fee-shifting basis | Identify the statute, contract provision, or common-fund theory; American rule otherwise |
| Inventing contract language | Quote verbatim or attach as exhibit |
