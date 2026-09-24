---
title: "Household Paperwork System — Where Every Important Document Lives, How Long to Keep It, and How Someone Else Finds It"
category: productivity/home-life
description: "Design a household's paper-and-digital document system — a small set of categories, one physical and one digital home for each, a keep/shred rule per document type marked for verification, an inbox-to-filed routine that fits a weekly slot, and a 'where things are' sheet a partner or executor could use if you were unavailable; distinct from `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md`, which reviews what estate documents say, and `domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md`, which designs task capture rather than document storage."
techniques:
  - ST-05
  - DS-26
  - ST-02
  - QA-01
difficulty: beginner
tags:
  - household
  - paperwork
  - filing-system
  - documents
  - organization
  - emergency-preparedness
updated: "2026-09-24"
related_prompts:
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-productivity/home-life/home_seasonal_maintenance_calendar.md
---

# Household Paperwork System

**Objective:** Produce a household document system small enough to maintain — categories,
locations, retention rules, a weekly routine and a findability sheet — so that any important
document can be found in under five minutes by you, and by the person who would need it if
you could not be asked.

**When to Use:**
- Papers live in several drawers, an email inbox and a phone's camera roll, and finding the
  car title took an afternoon.
- You are about to need documents in bulk: a mortgage, a move, a tax year-end, a new baby,
  caring for a parent.
- Only one person in the household knows where anything is.
- `domain-personal-development/major-decisions/personal_estate_wishes_attorney_prep.md` or the estate beneficiary review has produced
  documents that need a safe, findable home.

**Not this prompt if:**
- You want to know whether your will, beneficiary designations and titling are consistent —
  `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md`.
- Your problem is tasks and to-dos piling up, not documents — `domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md`.
- Someone has died and you need the admin sequence — `home_after_death_admin_checklist.md`
  (it uses this system's "where things are" sheet if it exists).

**Audience:** Any adult running a household, alone or with a partner. Works with paper-only,
digital-only or mixed.

## Inputs Required

1. **Household members** and who handles which paperwork today.
2. **Where documents currently live:** drawers, boxes, email folders, cloud drives, phone photos.
3. **Document types you have** (list what comes to mind; the prompt fills gaps): identity,
   property, vehicles, insurance, tax, banking, pensions/retirement, medical, children's
   school, pets, warranties, estate documents.
4. **Space and tools:** a drawer or box available; a cloud storage account; a scanner or phone.
5. **Time you can give weekly** (realistic: 10–20 minutes).
6. **Your country or region** — retention periods differ; they will be marked for verification.

## Instructions

### Step 1 — Fix a small category set (ST-05)
Use 8–12 top-level categories with at most one level of sub-folders. Default set (DS-26),
adjusted to the household: Identity & vital records · Home · Vehicles · Insurance · Money &
banking · Tax · Retirement & investments · Health · Children · Estate & legal · Warranties &
manuals · Pets. The same names are used on paper and in the digital folders.

### Step 2 — Assign one home per category, per format
For each category: the physical location (labelled file, fire-resistant box for originals that
cannot be replaced easily) and the digital folder path. Originals that are hard to replace —
birth, marriage and death certificates, property titles, signed estate documents — go in the
secure place; note where any are held by an attorney or bank instead.

### Step 3 — Set keep/shred rules, marked for verification
Per document type, a default: *keep permanently*, *keep while current + [period]*, *keep
[period]*, *shred on receipt of next*. Mark tax, legal and financial retention periods
"[VERIFY with tax authority guidance / your accountant]" — do not state them as fact. When
unsure, the safe default is keep and scan.

### Step 4 — Design the weekly routine (ST-02)
One physical inbox tray and one digital "to file" folder. Weekly, in the stated slot: open,
act or diary anything with a deadline, scan what is needed digitally, file, shred per rule.
Annually: purge per retention rules and update the "where things are" sheet.

### Step 5 — Write the "where things are" sheet
One page: each category, where the originals are, where the digital folder is, how to get
into it (the *location* of access details — e.g. "password manager, emergency access set up for
[person]" — never the passwords themselves), key contacts (accountant, attorney, insurer,
bank). Tell the person who would need it where the sheet is.

### Step 6 — Test it (QA-01)
Ask the other household member (or a trusted person) to find three named documents using
only the sheet. Time it. Fix anything that took more than five minutes.

## Constraints

### Must
- Use the same category names on paper and digitally.
- Give every category exactly one physical home and one digital home.
- Mark every legal/tax retention period for verification.
- Keep the findability sheet free of passwords and account numbers.

### Must Not
- Create more than 12 top-level categories or more than one level of nesting.
- Recommend destroying originals of vital records, titles or signed legal documents.
- Assume a scan replaces an original where an original may be legally required.

## Output Format

```
## Household paperwork system — [household], [date]
Weekly slot: [day, time, who] · Annual purge: [month]

### Categories and homes
| Category | Paper location | Digital folder | Originals held elsewhere |

### Keep / shred rules
| Document type | Rule | Verified? |

### Weekly routine (numbered)
### "Where things are" sheet (one page; location of sheet: ...; told to: ...)
### Findability test | Document | Found by | Time | Fix |
```

## Verification

- [ ] 8–12 categories, identical on paper and digital.
- [ ] Every category has one physical and one digital home.
- [ ] Every legal/tax retention period marked "[VERIFY]".
- [ ] The routine fits the stated weekly time.
- [ ] The findability sheet names locations and contacts, not credentials.
- [ ] Someone other than the author found three documents using only the sheet.

## False-Positive Prevention

1. **Over-engineered taxonomy.** Forty folders feel organised on day one and are abandoned by
   week six. Cap categories.
2. **Two homes for one thing.** "Insurance is in the drawer, or maybe the cloud" means nobody
   knows. One home per format.
3. **Retention from memory.** "Keep tax records seven years" may be wrong for your jurisdiction
   or situation. Mark and verify.
4. **Passwords on the sheet.** A findability sheet that holds credentials is a security risk;
   point to where access is managed instead.
5. **Only the organiser can find things.** The test with a second person is the point of the system.
6. **Shredding originals after scanning.** Some originals cannot be replaced or are required as
   originals; keep them.

## Example Output

```
## Household paperwork system — the Okafor household, 2026-09-24
Weekly slot: Sunday 19:00, 15 min, Ada (Chidi covers when away) · Annual purge: January

### Categories and homes
| Identity & vital records | Fire box, shelf A | /Home Docs/01 Identity | Passports: fire box |
| Home | Drawer 1 "Home" | /Home Docs/02 Home | Deed: held by mortgage lender [confirm] |
| Insurance | Drawer 1 "Insurance" | /Home Docs/04 Insurance | — |
| Estate & legal | Fire box, shelf B | /Home Docs/10 Estate | Signed wills: attorney's office + copy in fire box |
| Children | Drawer 2 | /Home Docs/09 Children | Birth certificates: fire box |

### Keep / shred rules
| Tax returns + supporting docs | Keep [period — VERIFY with tax authority] | No |
| Utility bills | Shred on receipt of next unless used for tax | Yes |
| Appliance manuals | Keep while owned; digital copy OK | Yes |

### Weekly routine
1. Empty tray + "to file" folder. 2. Anything with a date → calendar. 3. Scan what we'd need away from home.
4. File per table. 5. Shred per rules.

### "Where things are" sheet — kept in fire box lid + shared with Chidi's sister (emergency contact)
Accountant: T. Mensah · Attorney: holds wills · Password manager: emergency access set for Chidi

### Findability test
| Car title | Chidi | 2 min | — |
| Home insurance policy | Chidi | 9 min | Was in email only → saved to /04 Insurance |
| Kids' vaccination records | Chidi | 3 min | — |
```

## Techniques Used

- **ST-05 Hierarchical Organization** — a capped, one-level category tree.
- **DS-26 Safe Defaults Pattern** — a default category set and "keep and scan" when unsure.
- **ST-02 Structured Sequential Instructions** — the weekly inbox-to-filed routine.
- **QA-01 Self-Verification** — the second-person findability test.

## Related Prompts

- `../../domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — reviewing what the estate documents say.
- `home_seasonal_maintenance_calendar.md` — the annual purge fits alongside seasonal tasks.
- `home_after_death_admin_checklist.md` — relies on the "where things are" sheet.
