---
title: "Law Issue Spotting Drill"
category: education-teaching/learner/study-by-discipline
description: "Issue-spotting practice from fact patterns: generates hypothetical scenarios, prompts the learner to identify all legal issues, then compares coverage against a model issue checklist with gap analysis and IRAC scaffold for each identified issue."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - ED-03
  - QA-12
difficulty: advanced
tags:
  - law
  - bar-exam
  - MBE
  - MEE
  - issue-spotting
  - IRAC
  - fact-pattern
  - legal-analysis
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_law_rule_application.md
  - domain-education-teaching/learner/memory-and-recall/learn_retrieval_drill_designer.md
  - domain-education-teaching/learner/exam-prep/learn_practice_test_generator.md
---

## Objective

Generate issue-spotting practice from legal fact patterns: the learner reads a hypothetical scenario, lists every legal issue they can identify, and then compares their coverage against a model issue checklist. Gaps are flagged with the missed issue and the fact-pattern trigger that should have surfaced it. The drill then provides an IRAC scaffold for each major issue, separating the task of *spotting* from the task of *analyzing* — because these are distinct exam skills.

## When to Use

- Preparing for the Multistate Essay Examination (MEE), Uniform Bar Examination (UBE), or state bar essay components
- When a learner can analyze a legal issue once identified, but misses issues during the spotting phase
- When a learner consistently over-focuses on one area of law in a fact pattern at the expense of secondary issues
- During law school exam preparation where issue spotting accounts for a significant portion of grading

**Do not use** for black-letter rule memorization — that is a separate skill covered by `learnstudy_law_rule_application.md`. Issue spotting practice assumes the learner already knows the rules; this drill tests whether they can recognize when the rules are triggered.

## Instructions

1. **Collect inputs.**
   - Ask: "Which subject area(s)? (e.g., Contracts, Torts, Constitutional Law, Criminal Law, Evidence, Property, Civil Procedure, Business Associations, Family Law, Wills & Trusts)"
   - Ask: "Which jurisdiction framework? (MBE majority rules, MEE, specific state bar)"
   - Ask: "What difficulty level? (1 = single-subject, 2–4 issues | 2 = multi-issue single subject | 3 = cross-subject, 6+ issues)"
   - Ask: "What are your known spotting weaknesses? (e.g., 'I miss affirmative defenses', 'I overlook procedural issues embedded in substantive fact patterns', 'I miss third-party claims')"
   - Ask: "How many fact patterns for this session? (1–3 recommended)"

2. **Generate the fact pattern.**
   - Write a scenario at the specified difficulty with the following properties:
     - Every fact is there for a reason — no throwaway details (but the learner does not know which facts are legally significant)
     - Include at least one embedded red herring: a fact that seems legally significant but doesn't trigger a cognizable issue
     - At difficulty 2–3: include cross-issue facts — facts that are simultaneously relevant to more than one legal issue
     - Word count: 200–400 words for difficulty 1–2; 400–700 words for difficulty 3
   - Present the fact pattern with no questions, no hints, no header labels for legal subjects.

3. **Issue-spotting task.**
   Ask the learner:
   - "List every legal issue this fact pattern raises. For each issue, note: (a) the legal claim or defense, (b) the fact that triggers it, (c) which party raises it."
   - Do not reveal how many issues exist. The learner must decide when they are done.
   - Instruct: "Organize by party — list all claims Plaintiff/Prosecution might raise, then all defenses Defendant might assert, then any third-party issues."

4. **Reveal the model issue checklist.**
   After the learner has committed to their issue list:
   - Provide a complete issue checklist, organized by party and subject
   - For each issue: the legal claim, the triggering fact(s), and a one-sentence statement of why it is cognizable
   - Flag the embedded red herring: name it and explain why it fails to raise a legal issue despite appearing significant

5. **Gap analysis.**
   Compare learner's list to the model checklist:
   - For each issue the learner **missed**: state the issue, the specific fact that should have triggered it, and the spotting rule ("When you see [fact pattern], always check for [issue]")
   - For each issue the learner **correctly spotted**: confirm
   - For each item the learner **over-spotted** (identified something that isn't an issue): briefly explain why
   - Calculate: issues spotted / total issues = spotting coverage score

6. **IRAC scaffold for major issues.**
   For the top 2–3 issues by exam importance, provide:
   - **Issue:** One sentence framing the legal question
   - **Rule:** The black-letter rule (elements or standard), stated precisely
   - **Application prompt:** "Apply each element of the rule to these specific facts: [facts listed]" — but do NOT write the application; leave that for the learner
   - **Conclusion prompt:** "Based on your analysis, who prevails on this issue and why?"

7. **Spotting pattern feedback.**
   After the gap analysis, identify the learner's spotting pattern:
   - "You consistently spotted [strong area]" — reinforce what worked
   - "You missed issues in [category]: [affirmative defenses / third-party claims / procedural issues / cross-claim issues / constitutional issues embedded in statutory fact patterns]"
   - Provide a **spotting checklist** the learner should run mentally at the end of every fact-pattern review:
     1. Have I checked for affirmative defenses for each claim?
     2. Have I checked for third-party claims (contribution, indemnification)?
     3. Have I checked procedural validity (standing, jurisdiction, venue, statute of limitations)?
     4. Have I checked for any constitutional overlay (if government actor is present)?
     5. Have I considered all parties — not just named plaintiff and defendant?

## Output Format

```
# Law Issue Spotting Drill: [Subject(s)]
Jurisdiction: [MBE/MEE/State] | Difficulty: [1/2/3] | Patterns: N

---

## Fact Pattern [#]

[Scenario text — 200–700 words depending on difficulty. No legal labels, no hints.]

---

*Before reading further — list all legal issues this fact pattern raises.*
*For each issue: (a) legal claim or defense, (b) triggering fact, (c) which party raises it.*
*Organize by party.*

[PAUSE — commit to your issue list before advancing]

---

## Model Issue Checklist

### [Plaintiff / Prosecution] Issues
1. [Claim] — Trigger: [Fact X] — Why cognizable: [one sentence]
2. ...

### [Defendant] Issues
1. [Defense] — Trigger: [Fact Y] — Why cognizable: [one sentence]
2. ...

### Third-Party / Cross-Issues
1. [Issue] — Trigger: [Fact Z]

### Embedded Red Herring
[Fact that seemed significant] — This does NOT raise a cognizable issue because: [explanation]

---

## Gap Analysis

**Issues you spotted correctly:**
- [Issue] ✓

**Issues you missed:**
- [Issue] — Trigger you should have caught: [specific fact] — Spotting rule: "When [pattern], always check [issue]"

**Issues you over-spotted (not cognizable here):**
- [Item] — Not an issue here because: [explanation]

**Spotting coverage: [X]/[Total] = [%]**

---

## IRAC Scaffold: [Major Issue #1]

**Issue:** [One-sentence legal question]

**Rule:** [Black-letter rule with elements]

**Application:** Apply each element to these facts: [relevant facts listed]
*(Write your analysis here before reading on)*

**Conclusion:** Who prevails and why? *(Write your conclusion here)*

---

## Spotting Pattern Feedback

**Your strengths:** [What you consistently caught]
**Your gap pattern:** [Category of issues you missed]
**Run this checklist at the end of every fact pattern:**
☐ Affirmative defenses checked for every claim?
☐ Third-party claims considered?
☐ Procedural issues checked (standing / SOL / jurisdiction)?
☐ Constitutional overlay (if government actor present)?
☐ All parties examined — not just named plaintiff/defendant?
```

## Example Output

---

**Input:** Contracts — MBE majority rules — Difficulty 2 — 1 fact pattern — Weakness: misses affirmative defenses

---

# Law Issue Spotting Drill: Contracts
Jurisdiction: MBE Majority | Difficulty: 2 | Patterns: 1

---

## Fact Pattern 1

On March 1, Alicia, the owner of a chain of bakeries, emails Barry, a commercial refrigeration contractor: "I need a walk-in cooler unit installed at my new bakery location by May 15. Can you do it for $18,000?" Barry immediately responds: "Yes, I can do that. Installation by May 15 for $18,000. I'll need a 25% deposit to order the equipment." Alicia reads the email and thinks to herself, "That deposit requirement is annoying, but I can work with it." She does not respond.

On March 10, Alicia emails Barry: "Let's move forward. I'll have the deposit ready." Barry, now busy with another large project, responds: "I'm not sure I can still commit to May 15. Let me get back to you." Alicia does not reply.

On March 20, Barry emails: "I've confirmed I can do May 15. I'm starting equipment orders today." Alicia responds the same day: "Perfect. Deposit check is in the mail."

Barry orders the refrigeration unit. On April 5, Alicia calls Barry to say she has found another contractor who will do the job for $14,000 and she is canceling the agreement. Barry has already paid $6,000 to his equipment supplier for the unit (non-refundable deposit under his supplier contract). He has also turned down another job worth $4,000 during the same period.

Barry sues Alicia. Alicia's attorney advises her that she may have a defense based on the March 1 exchange.

---

*Before reading further — list all legal issues this fact pattern raises.*
*For each issue: (a) legal claim or defense, (b) triggering fact, (c) which party raises it.*
*Organize by party.*

[PAUSE — commit to your issue list before advancing]

---

## Model Issue Checklist

### Barry (Plaintiff) Issues

1. **Breach of Contract** — Trigger: Alicia's April 5 cancellation after a binding agreement was formed — Why cognizable: Barry will argue a valid contract existed and Alicia's repudiation constitutes breach.

2. **Expectation Damages** — Trigger: Barry's lost profit on the job ($18,000 contract minus costs saved) — Why cognizable: Standard measure of contract damages is benefit of the bargain.

3. **Reliance Damages (alternative)** — Trigger: $6,000 non-refundable equipment deposit + $4,000 foregone opportunity — Why cognizable: If expectation damages are unavailable or uncertain, Barry can recover detrimental reliance.

### Alicia (Defendant) Issues

4. **No Contract Formed (Offer/Acceptance Defect)** — Trigger: Barry's March 1 response included a deposit condition; Alicia never expressly accepted — Why cognizable: If Barry's March 1 email was a counter-offer (adding the deposit term), Alicia's silence may not constitute acceptance under mirror-image rule.

5. **Statute of Frauds** — Trigger: Contract for services; no written signed agreement by both parties — Why cognizable: Alicia's attorney flagged a defense; learner must evaluate whether SOF applies (services contracts generally not within SOF, but worth examining if goods are involved).

6. **Revocation Before Acceptance** — Trigger: Barry's March 10 email expressing uncertainty ("not sure I can still commit") — Why cognizable: If Barry's March 1 email was an offer, Barry may have revoked it on March 10 before Alicia accepted.

### Embedded Red Herring

**Alicia thinking "the deposit is annoying but I can work with it"** — This internal thought does NOT raise a cognizable issue. Mental reservations that are not communicated do not affect contract formation under objective theory of contracts. A learner who lists "subjective intent" or "mental assent" as a separate issue has over-spotted.

---

## Gap Analysis

**Common issues spotted correctly:**
- Breach of contract ✓
- Expectation damages ✓

**Issues commonly missed:**

- **Revocation (Issue #6)** — Trigger you should have caught: Barry's March 10 message "I'm not sure I can still commit" — Spotting rule: "When an offeror expresses doubt or qualification after an offer is made, always check whether effective revocation occurred before acceptance."

- **Statute of Frauds (Issue #5)** — Trigger you should have caught: Alicia's attorney mentioned a "defense" + the contract involves a specific dollar amount over $500 — Spotting rule: "When you see a defense hinted at in the facts, examine all SOF categories (goods over $500 under UCC, contracts for real property, contracts not performable within one year, etc.) even if only to rule them out."

**Over-spotted item (if identified):**
- "Mutual assent / Alicia's subjective reluctance" — Not cognizable. Objective theory of contracts controls; unexpressed mental reservations are irrelevant.

**Spotting coverage (example):** Issues spotted 3/6 = 50%

---

## IRAC Scaffold: Contract Formation (Issue #4 — No Contract Formed)

**Issue:** Did a valid contract form between Barry and Alicia, or did Barry's deposit condition constitute a counter-offer that was never properly accepted?

**Rule:** Under the common law mirror-image rule, an acceptance that adds or modifies terms is a counter-offer, not an acceptance, and terminates the original offer. A counter-offer must itself be accepted (expressly or by conduct) to form a contract.

**Application:** Apply the mirror-image rule to these specific facts:
- Barry's March 1 email — did it constitute an offer? Was the deposit condition a term or a mere request?
- Alicia's silence on March 1 — was this acceptance, rejection, or counter-offer?
- Barry's March 10 email ("not sure I can commit") — if there was an outstanding offer, did this revoke it?
- Alicia's March 10 email ("let's move forward, deposit ready") — was this an acceptance? Of what?
- Barry's March 20 confirmation and Alicia's same-day reply — does this sequence cure any formation defect?
*(Write your analysis here before reading on)*

**Conclusion:** Did a contract form, and if so, at what moment? *(Write your conclusion here)*

---

## IRAC Scaffold: Reliance Damages (Issue #3)

**Issue:** If Barry cannot prove expectation damages with certainty, can he recover his $6,000 equipment deposit and $4,000 foregone opportunity as reliance damages?

**Rule:** A party who has relied on a contract to their detriment may recover reliance damages (out-of-pocket losses caused by the reliance) where expectation damages are speculative or cannot be proved with reasonable certainty.

**Application:** Apply to these facts:
- Is the $6,000 non-refundable supplier deposit a foreseeable reliance loss?
- Is the $4,000 foregone job recoverable as reliance, or does it require a lost profits analysis?
- Would allowing both reliance and expectation damages result in a double recovery?
*(Write your analysis here)*

**Conclusion:** What damages should Barry recover? *(Write your conclusion here)*

---

## Spotting Pattern Feedback

**Common strengths:** Most learners catch the primary breach claim and expectation damages immediately — these are front-of-mind in contracts problems.

**Common gap pattern:** Affirmative defenses (revocation, SOF, formation defects) are chronically under-spotted because learners are trained to build the plaintiff's case first. Defenses require actively "switching sides" and re-reading the fact pattern through the defendant's eyes.

**Run this checklist at the end of every fact pattern:**
☐ Have I read the facts once for plaintiff's claims AND once again for defendant's defenses?
☐ Have I checked all affirmative defenses (SOF, revocation, impossibility, failure of condition)?
☐ Have I considered third-party claims (here: Barry's supplier relationship)?
☐ Have I examined the chronology for timing issues (revocation before acceptance, lapse of offer)?
☐ Have I checked whether the attorney's hint in the facts signals a specific defense I need to analyze?

---

## False-Positive Prevention

**❌ DON'T** reveal the number of issues before the learner has attempted spotting. Knowing "there are 6 issues" is a hint that changes the task from issue spotting to issue counting.

**✅ DO** instruct learners to stop when they believe they are done, not after a specified number of entries.

**❌ DON'T** label the fact pattern by subject area ("Contracts fact pattern"). Real exam hypotheticals are unlabeled — part of the skill is recognizing which body of law applies.

**✅ DO** present the fact pattern with no subject heading. The learner must identify the applicable law area(s) as part of the spotting task.

**❌ DON'T** generate fact patterns where every fact has obvious legal significance. Real exam fact patterns contain noise — distractors, background context, and red herrings.

**✅ DO** include at least one embedded red herring per fact pattern. The gap analysis should name it and explain why it is not legally operative.

**❌ DON'T** score only on final issue count. A learner who identifies the right claims but misses all defenses has a systematic gap, even if their raw count is similar to the model.

**✅ DO** track issues separately by party (plaintiff claims vs. defendant defenses vs. third-party) to surface the systematic spotting pattern.

**❌ DON'T** skip the IRAC scaffold step. Issue spotting and legal analysis are separate skills. Learners who only practice analysis never develop the ability to spot what needs analyzing.

**✅ DO** provide the IRAC scaffold as a prompted framework (not a completed answer) so the learner practices the full exam sequence: spot → frame the legal question → analyze → conclude.

## Quality Criteria

- [ ] Fact pattern contains no legal subject labels or hints about number of issues
- [ ] At least one embedded red herring is present with explanation
- [ ] Model issue checklist is organized by party (plaintiff / defendant / third-party)
- [ ] Gap analysis identifies the specific triggering fact for each missed issue
- [ ] Gap analysis includes a "spotting rule" statement for each missed issue
- [ ] IRAC scaffold provides rule and fact list without completing the analysis
- [ ] Spotting pattern feedback identifies the category of issues missed (not just the specific miss)
- [ ] End-of-pattern checklist is provided for self-monitoring

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective explicitly separates issue spotting from legal analysis — two distinct skills requiring different training
- **ST-02 (Structured Sequential Instructions):** Seven-step process enforces the correct learning sequence: read → spot → compare → analyze → reflect
- **ED-02 (Progressive Exercise Generation):** Three difficulty levels (1–3) scale fact pattern complexity and issue count
- **ED-03 (Guided Discovery):** Learner must independently decide when spotting is complete before any model is revealed; IRAC scaffold prompts analysis without providing it
- **QA-12 (False Positives Identification):** Red herrings test selective application of rules; over-spotting is tracked and explained; learner must justify each identified issue, not just list it
