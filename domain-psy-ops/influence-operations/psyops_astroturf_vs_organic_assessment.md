---
title: "Astroturf vs Organic — Is the Grassroots Support Real"
category: psy-ops/influence-operations
description: "Assess whether a movement, campaign, or wave of public comment reflects genuine constituency or manufactured appearance, using funding transparency, participation depth, local specificity, and cost-to-participate rather than message uniformity. Built to protect real grassroots movements from dismissal, since accusing an authentic movement of astroturfing is the more common and more damaging error."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - astroturfing
  - civil-society
  - advocacy
  - analysis
updated: "2026-07-28"
reasoning:
  styles: [analytic, evidential, adversarial]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: authenticity_assessment
  user_role: [analyst, journalist, policy, researcher]
  mode: [assess, audit, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
  - domain-policy/policy_stakeholder_coalition_map.md
---

# Astroturf vs Organic Assessment

**Objective:** Assess whether an apparent groundswell — a campaign, a movement, a flood of public comments, a wave of local opposition — reflects a genuine constituency or a manufactured appearance of one. The discriminating evidence is **funding transparency, participation depth, local specificity, and cost-to-participate**, not message uniformity, which real movements produce abundantly because they distribute talking points on purpose.

This prompt is built with a deliberate asymmetry. Calling a real grassroots movement astroturf is the more common error and by far the more damaging one: it is the standard move for dismissing inconvenient public opposition, it strips ordinary people of standing, and it is nearly impossible for them to disprove. Meanwhile genuine astroturf usually leaves documentary traces — funding, contracts, coordinating vendors — that are findable if you look. **The burden therefore sits on the astroturf finding**, and "authentic, professionally supported" is a common and legitimate middle result: most effective movements have both real constituents and paid staff, and that combination is not astroturf.

**When to use:**
- A campaign has appeared quickly and you need to assess whether it represents real people.
- A regulatory docket or consultation has received a large volume of similar comments.
- Someone has dismissed a movement as astroturf and you want to check the claim.
- You are reporting on advocacy and need to characterize its base accurately.

**When NOT to use:**
- You are assessing account-level coordination on a platform — use `psyops_coordinated_inauthentic_behavior_indicators.md`.
- You want to map who is aligned with whom on a policy question — use `domain-policy/policy_stakeholder_coalition_map.md`.
- The question is whether the movement's claims are correct. That is separate and this prompt does not address it.

**Audience:** Journalists, policy analysts, regulators, researchers, and communications staff assessing an advocacy campaign.

---

## Inputs / Context

1. **The campaign.** What it advocates, when it appeared, and how it presents itself.
2. **The visible participants.** Who is publicly involved, and at what level of engagement.
3. **Funding and organizational evidence.** Registrations, filings, disclosures, vendor relationships, staff — and whether you have checked or are assuming.
4. **The affected constituency.** Who would plausibly care about this issue, how many there are, and where they are.
5. **The volume and channel.** How much activity, through what mechanism — a comment portal, a petition tool, in-person turnout, sustained local organizing.
6. **Who benefits.** Which commercial or political interests align with the campaign's position — a hypothesis generator only.

---

## Constraints

### Must
- Weight **documentary evidence** — funding, contracts, vendor relationships, employment — above behavioral inference.
- Assess **participation depth**: does involvement extend beyond the cheapest possible action into meetings, time, money, or personal risk?
- Check **local specificity**: do participants demonstrate situated knowledge that outsiders would not have?
- Measure **cost-to-participate**. High-cost participation is very difficult to manufacture at scale; low-cost participation proves little either way.
- Treat **"authentic but professionally supported"** as a first-class outcome and check for it explicitly.
- Assess whether a **plausible constituency exists** at all — an issue with no affected population producing mass local turnout is the real anomaly.
- State the **cost of a false astroturf finding** for the people involved.

### Must Not
- Infer astroturf from message uniformity. Real campaigns distribute talking points, form letters, and templates, and instruct supporters to use them.
- Treat professional staff, funding, or communications support as astroturf. Nearly every effective movement has all three.
- Use "who benefits" as a finding. It generates hypotheses and cannot establish manufacture.
- Name individual participants as paid shills. Where documentary evidence establishes paid participation, that attaches to the organization and its disclosures.
- Fabricate funding relationships, filings, vendor names, or organizational links. Unverified is `[VERIFY]`.
- Dismiss a movement because its position aligns with a wealthy interest. Sometimes the public and an industry genuinely agree.
- Let the analyst's view of the underlying issue drive the authenticity finding.

---

## Instructions

### Step 1 — Record your own position on the issue
State whether you agree with the campaign. This predicts the direction of your error more strongly than any other input.

### Step 2 — Establish whether a constituency plausibly exists
Who would care about this, how many, and where? A campaign with a large real constituency behaving normally is the baseline expectation, not something to be explained.

### Step 3 — Pursue the documentary layer first
Registrations, filings, disclosures, employment, vendor and agency relationships, domain registrations, PR retainers. This is where genuine astroturf is actually caught. Record what you checked and what you could not access.

### Step 4 — Assess participation depth
Sort participation by cost: form-letter signature, personal comment, meeting attendance, sustained volunteering, donation, public identification, travel, risk. A campaign that is entirely low-cost is undetermined; one with substantial high-cost participation is very hard to fake.

### Step 5 — Test local specificity
Do participants show knowledge only locals would have — the road, the schedule, the history, the specific harm? Generic testimony is weak evidence either way; specific testimony is strong evidence of authenticity.

### Step 6 — Examine the mechanism
For comment floods: is there a submission tool, is the tool disclosed, do comments show any personalization, and — importantly — can the named submitters be shown to be real people who consented? Undisclosed tooling and non-consenting submitters is documented astroturf; a disclosed tool with real consenting users is ordinary advocacy.

### Step 7 — Check for the professional-support middle
Explicitly ask whether the evidence fits "real constituency, professionally organized." Most cases land here, and it is the answer most likely to be skipped.

### Step 8 — Adversarial check and finding
Argue that this is a genuine movement and you are pattern-matching normal organizing to manufacture. Then state the finding with confidence, and state what a wrong astroturf call would cost these people.

---

## False-Positive Prevention

1. **Uniformity as proof.** Form letters, shared talking points, and templates are standard organizing practice, distributed deliberately and used willingly.
2. **Professionalism as proof.** Staff, funding, branding, and media training indicate an effective movement, not a fake one.
3. **Beneficiary reasoning.** Concluding manufacture because a corporation or party benefits. Publics and interests align on real issues constantly.
4. **Position-driven findings.** Scrutinizing campaigns you disagree with. If your astroturf findings correlate with your politics, the method is broken.
5. **Speed as suspicion.** Treating rapid mobilization as unnatural. Existing networks, group chats, and acute triggers mobilize real people in hours.
6. **Missing the middle.** Forcing a binary when "authentic but professionally supported" fits the evidence, which it usually does.
7. **Individual shill naming.** Attaching paid-participation findings to named individuals rather than to organizations and their disclosure obligations.
8. **Asymmetric burden.** Requiring a movement to prove authenticity. Astroturf is the positive claim and carries the burden of proof.

---

## Output Format

```
# Authenticity assessment — [campaign]

## My position on the underlying issue
[Agree / disagree / neutral — recorded to correct for it]

## Plausible constituency
[Who would care, how many, where — is a real base expected here?]

## Documentary layer (weighted highest)
| Item | Checked? | Finding |
|---|---|---|
| Registrations / filings | yes | [...] |
| Funding disclosure | no — [VERIFY] | |
| Vendor / agency / PR relationships | | |
| Staff vs volunteer composition | | |

## Participation depth
| Cost tier | Evidence of participation | Volume |
|---|---|---|
| Low (signature, form letter) | | |
| Medium (personal comment, meeting) | | |
| High (time, money, travel, public identification, risk) | | |

## Local specificity
[Situated knowledge present? Examples — or generic throughout]

## Mechanism (for comment/petition floods)
[Tool used? Disclosed? Personalization? Submitters real and consenting?]

## The professional-support middle
[Does "real constituency, professionally organized" fit the evidence? Explicitly answered.]

## Finding
[Organic / organic with professional support / mixed / manufactured / undetermined]
**Confidence:** [low / moderate / high] — documentary basis: [what, if any]

## Cost of a wrong astroturf call
[What being wrong would do to the people involved]

## Adversarial check
[The case that this is a genuine movement and I am pattern-matching normal organizing]

## Unknowns
[All [VERIFY] items]
```

---

## Verification

- [ ] The analyst's own position on the issue is recorded up front.
- [ ] Documentary evidence was pursued before behavioral inference, and gaps are marked `[VERIFY]`.
- [ ] Message uniformity contributed nothing to the finding.
- [ ] Professional staffing, funding, and communications support were not treated as evidence of manufacture.
- [ ] Participation depth is sorted by cost, and high-cost participation is weighted accordingly.
- [ ] The "authentic but professionally supported" outcome was explicitly considered.
- [ ] Beneficiary reasoning is used only to generate hypotheses, never as a finding.
- [ ] No individual participant is named as a paid shill.
- [ ] The burden of proof sits on the astroturf claim, not on the movement.
- [ ] The cost of a wrong astroturf finding is stated.
