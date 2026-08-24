---
title: "Defamation & Right-of-Publicity Risk Screen — Flag Liability Exposure in Nonfiction Naming Living People or Organizations"
category: legal/ip
description: "Screen a nonfiction draft that names living people or identifiable organizations for defamation and right-of-publicity/privacy exposure: locate factual assertions that could harm reputation, test each against truth/opinion/privilege structure, flag unsupported or risky statements, and route genuine exposure to counsel. Organizes and flags risk — it does not give legal advice or clear anything for publication."
techniques:
  - ST-01
  - ST-02
  - QA-05
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - defamation
  - right-of-publicity
  - nonfiction
  - risk-screen
  - pre-publication
  - privacy
updated: "2026-07-06"
related_prompts:
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
  - domain-research-academic/research_manuscript_fact_check_reconciler.md
  - domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md
---

# Defamation & Right-of-Publicity Risk Screen

**Objective:** Screen a nonfiction draft that names or identifies living people or organizations, locate the statements that could create defamation, false-light, privacy, or right-of-publicity exposure, test each against the standard structure (is it a statement of fact or opinion; is it provably true and sourced; is a privilege or a public-figure/actual-malice consideration in play), and flag the risky ones for the author and their counsel to resolve.

**This is a risk-organizing tool, not legal advice.** It does not determine liability, does not "clear" anything for publication, and cannot substitute for a media/publishing attorney. Its job is to make sure nothing risky ships *unseen* — it surfaces exposure and routes it, using the correct analytical structure so counsel review is efficient. Defamation and publicity law is **jurisdiction-specific** (and varies sharply by country); the screen defaults to US common-law framing and flags jurisdiction as a required input.

**When to Use:**
- A nonfiction piece (article, book, exposé, memoir, report, review) names or clearly identifies real living people or organizations and makes factual assertions about them.
- Pre-publication risk pass, especially where claims are critical, negative, or reveal private facts.
- Memoir or reporting drawing on the author's own experience of real people.

**When NOT to use:**
- Nothing in the piece identifies a real person/organization (fully general or anonymized) — minimal exposure; skip.
- You need an actual legal opinion or a decision to publish — that's counsel's call; this only organizes the risk.
- Pure copyright/plagiarism questions — use the fair-use and original-expression prompts.

**Audience:** Nonfiction authors, editors, and publishers doing pre-publication risk triage before counsel review.

---

## Inputs / Context

1. **The draft** (wrap in `<draft>...</draft>`).
2. **Jurisdiction** (REQUIRED): country and, in the US, state — governs the standards. If unknown, state that the screen is US-common-law-default and jurisdiction must be confirmed.
3. **Who is named:** for each identifiable person/entity, note whether they are a **public figure/official** or a **private individual** (affects the fault standard), and whether living (defamation generally protects the living).
4. **Support for each claim:** what source/evidence backs each factual assertion about a named party (ties to the fact-check reconciler).
5. **Intent:** is a statement offered as verifiable fact or as the author's opinion/experience?

---

## Constraints

### Must
- Identify **every identifiable living person/organization** and every factual assertion about them.
- For each such assertion, classify: **fact vs. opinion**, **reputation-harmful or not**, **supported vs. unsupported**, and note **public-figure vs. private** status and any **privilege** (e.g., fair report of official proceedings).
- Flag the high-risk pattern: a **statement of fact**, that is **harmful to reputation**, that is **not provably true / not well-sourced**, about an **identifiable living party**. That combination is the core defamation exposure.
- Separately flag **privacy / right-of-publicity / false-light** issues: disclosure of private facts, or commercial use of a person's name/likeness, even when the statement is true.
- Route every flag to counsel with the specific concern named; propose risk-reducing options (source it, soften to opinion, attribute, anonymize, cut) **without** claiming any option makes it "safe."

### Must Not
- Declare any statement legally safe, non-defamatory, or cleared to publish — that is counsel's determination.
- Give a legal opinion, predict case outcomes, or cite specific statutes/cases as advice (name the *type* of standard, not a fabricated authority).
- Treat "it's true" as automatically clearing risk (truth is a defense to defamation but not to privacy/publicity/false-light, and provability matters).
- Fabricate the public-figure status, the facts, or the jurisdiction's standard — flag unknowns as inputs to confirm.
- Assume opinion labeling immunizes a statement — an "opinion" implying undisclosed defamatory facts can still carry risk; flag it.

---

## Instructions

1. **Identify the named parties.**
   - List every identifiable living person and organization (including those identifiable by description, not just name). Note public-figure vs. private, if known.

2. **Extract assertions about each.**
   - For each party, pull every statement made about them. Tag each as fact or opinion, and harmful-to-reputation or neutral.

3. **Run the defamation structure (CRITICAL) on harmful factual assertions.**
   - For each harmful statement of fact about an identifiable living party, ask:
     - Is it **provably true and well-sourced**? (If yes → lower risk, but confirm the source in hand.)
     - If not clearly true/sourced → **HIGH-RISK FLAG**.
     - Is it really **opinion**, and if so does it imply undisclosed defamatory facts? (Implied-fact opinion still flags.)
     - Public figure/official? Note that a higher fault standard (actual malice) typically applies — but do not treat that as clearance.

4. **Run the privacy/publicity pass.**
   - Flag: disclosure of private, non-newsworthy facts; use of name/likeness for commercial advantage; portrayals that place someone in a false light — **even if true**.

5. **Propose risk-reducing options (not clearances).**
   - Per flag: strengthen the source, attribute ("according to…"), convert to clearly-disclosed opinion, anonymize/de-identify, add the subject's response, or cut. State that these *reduce* exposure and still require counsel sign-off.

6. **Assemble the counsel packet.**
   - Group flags by severity; for each, give the statement, the concern, the party's status, current support, and the options. Mark jurisdiction assumptions.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T** say anything is "safe," "not defamatory," or "cleared" — flag and route; never clear.
❌ **DON'T** treat truth as a universal shield — it doesn't cover privacy, publicity, or false-light, and it must be *provable*.
❌ **DON'T** assume calling something "opinion" removes risk — implied-fact opinion still flags.
❌ **DON'T** invent a party's public-figure status, the governing standard, or a case citation — mark unknowns for confirmation.
❌ **DON'T** over-flag neutral or clearly-true, well-sourced statements into noise — reserve HIGH-RISK for the harmful-fact-unsupported-identifiable pattern.
✅ **DO** require jurisdiction and treat it as load-bearing.
✅ **DO** separate defamation exposure from privacy/publicity exposure — they have different rules.
✅ **DO** tie each factual flag to whether a real source supports it (link to the fact-check reconciler).
✅ **DO** route every genuine flag to counsel with a specific, structured concern.

## Dual-Failure Prevention (QA-20)
- **Harmful failure:** missing a real exposure (an unsupported reputation-damaging factual claim about a named person ships unseen).
- **Unhelpful failure:** flagging every mention of a real person so the author drowns in noise and ignores the screen. Calibrate: HIGH-RISK = harmful + factual + unsupported + identifiable; everything else is lower or informational.

## Confidence Levels
- **High:** clear harmful-fact-unsupported pattern, or clearly neutral/true-sourced statement.
- **Medium:** fact/opinion line is genuinely arguable, or public-figure status/jurisdiction affects it.
- **Low:** can't tell without facts the author must supply (party status, whether the claim is true, jurisdiction) — flag as an input to resolve.

---

## Expected Output

### Output Format

```
## Named Parties
| Party | Identifiable how | Public/Private (if known) | # assertions |

## Risk Flags (high severity first)
### [HIGH] Statement about [Party]
- Statement: "..."
- Type: fact / opinion(implying fact)
- Reputation-harmful: yes
- Current support: [source or NONE]
- Concern: unsupported harmful factual assertion about an identifiable living [private/public] party → defamation exposure
- Options (reduce, not clear): [source it / attribute / soften to disclosed opinion / anonymize / add response / cut]
- Jurisdiction note: [US-default; confirm state / country]

### [PRIVACY] ...
### [MEDIUM] ...

## Counsel Packet Summary
- High-risk flags: n | Privacy/publicity flags: n | Medium: n
- Required inputs to resolve: [jurisdiction, party status, source confirmations]
- Reminder: this screen organizes and routes risk; it is not legal advice and clears nothing.
```

---

## Example Output

## Named Parties
| Party | Identifiable how | Public/Private | # assertions |
| Jane Doe (former manager) | named + described | private (likely) | 3 |
| Acme Corp | named | organization | 2 |

## Risk Flags (high severity first)
### [HIGH] Statement about Jane Doe
- Statement: "Jane routinely falsified the quarterly numbers."
- Type: fact
- Reputation-harmful: yes (imputes dishonesty/possible crime)
- Current support: NONE (author's recollection only)
- Concern: unsupported harmful factual assertion about an identifiable private living person → core defamation exposure.
- Options (reduce, not clear): document with contemporaneous evidence; attribute to a specific incident you witnessed and can substantiate; narrow to what you directly observed; or cut. None of these "clears" it — counsel must review.
- Jurisdiction note: US-default; confirm state (some states differ on private-figure fault and damages).

### [PRIVACY] Statement about Jane Doe
- Statement: discloses her medical leave and diagnosis.
- Concern: disclosure of private, likely non-newsworthy facts → privacy exposure even if true.
- Options: remove the diagnosis; keep only what's necessary and non-private; get consent; counsel review.

### [MEDIUM] Statement about Acme Corp
- Statement: "Acme's product is the worst on the market."
- Type: opinion (hyperbole) — but verify it doesn't imply undisclosed factual defects.
- Concern: likely protected opinion; flag only if it implies specific false facts.
- Options: keep as clearly-subjective opinion; avoid implying undisclosed test data you don't have.

## Counsel Packet Summary
- High-risk flags: 1 | Privacy/publicity flags: 1 | Medium: 1
- Required inputs to resolve: jurisdiction (state), whether the falsification claim is documentable, Jane's consent status.
- Reminder: this screen organizes and routes risk; it is not legal advice and clears nothing.

---

## Customization Guide
- **Memoir mode:** emphasize private-facts/false-light and composite-character options; personal recollection is not, by itself, provable truth.
- **Investigative mode:** emphasize documentation trails, fair-report privilege for official proceedings, and offering subjects a right of response.
- **Non-US:** flag that many jurisdictions are far more claimant-friendly (e.g., truth alone may not suffice, or the burden shifts) — counsel in the relevant country is essential.

## Techniques Used
- **ST-01 (Clear Objective):** locate and route liability exposure; explicitly not a clearance.
- **ST-02 (Structured Sequential Instructions):** identify parties → extract assertions → defamation structure → privacy pass → options → packet.
- **QA-05 (Citation Requirements):** ties each factual flag to whether a real source supports it.
- **QA-04 (Uncertainty Acknowledgment):** confidence levels + explicit "not legal advice / clears nothing."
- **CM-02 (Constraint Specification):** hard boundaries — no clearance, no fabricated authority, jurisdiction required.

## Related Prompts
- `domain-legal/ip/legal_copyright_fair_use_analysis.md` — the copyright half of the risk pass.
- `domain-research-academic/research_manuscript_fact_check_reconciler.md` — confirm whether harmful factual claims are actually supported.
- `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` — calibrate fact-vs-opinion framing.
