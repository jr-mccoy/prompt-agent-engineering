---
title: "Personnel Targeting Exposure Review — Reducing What Can Be Used Against Your People"
category: psy-ops/organizational-red-team
description: "Assess how exposed key staff are to pretexting, impersonation, and targeted harassment, using only what is already publicly available, and produce reduction actions plus organizational protections. Consent-first and dignity-first: staff are participants rather than subjects, findings go to the individual, and the review never investigates private lives or produces a dossier."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - security-awareness
  - harassment
  - organizational-resilience
  - privacy
updated: "2026-07-28"
reasoning:
  styles: [analytic, protective, procedural]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: exposure_review_with_reductions
  user_role: [security, communications, hr, executive]
  mode: [assess, design, act]
related_prompts:
  - domain-psy-ops/personal-defense/psyops_social_engineering_pretext_recognition.md
  - domain-psy-ops/organizational-red-team/psyops_org_influence_threat_model.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
---

# Personnel Targeting Exposure Review

**Objective:** Assess how exposed specific roles are to **pretexting, impersonation, and targeted harassment**, and reduce that exposure. The review works only from information that is **already publicly available** — the point is to see what an attacker would trivially assemble, not to discover anything new about anyone. It then produces two sets of outputs: **reduction actions** the individual can take if they choose, and **organizational protections** that do not depend on individual behavior at all.

The prompt is built consent-first for a reason: a review like this is one procedural step away from surveillance of employees, and organizations that get this wrong cause more harm than the threat did. Staff are **participants, not subjects**. Findings about a person go to that person. Nothing here investigates private life, associations, finances, or opinions, and the output must never be assemblable into a dossier — which is precisely what an attacker wants and precisely what a badly run review produces and stores.

The second design principle is that **the organizational layer matters more than the individual layer**. Telling people to reduce their digital footprint puts the burden on the target and works poorly. Verification procedures, payment controls, and a real harassment response protect people regardless of how visible they are — and visibility is often a job requirement.

**When to use:**
- Staff are exposed by role: finance approvals, executive authority, public-facing work, moderation, research on contested topics.
- Following a pretexting attempt, an impersonation incident, or harassment of a colleague.
- Before a period of heightened attention — a launch, a controversy, litigation, a campaign.
- Building a security-awareness program that is about the organization rather than about blaming staff.

**When NOT to use:**
- Someone is being harassed right now — support them and use your incident process; this is a preparation tool.
- You want individual guidance on handling an approach — use `../personal-defense/psyops_social_engineering_pretext_recognition.md`.
- You want the organizational threat picture — use `psyops_org_influence_threat_model.md`.
- The exposure is technical rather than social — use `domain-software-engineering/analysis/security/`.

**Audience:** Security, HR, and communications teams, with the participation of the staff concerned.

---

## Inputs / Context

1. **Roles in scope**, and why each is exposed — authority, access, visibility, or subject matter.
2. **Consent status.** Whether the individuals know about and agreed to this review. If not, stop.
3. **Public surface.** What is discoverable about the role and its holder without any special access: company site, professional networks, conference material, publications, press.
4. **What an attacker would want.** Payment authority, credential access, credibility to impersonate, or the ability to distress the person.
5. **Existing controls.** Verification procedures, payment authorization, out-of-band confirmation requirements, harassment response.
6. **Incident history.** Prior impersonation, pretexting, or harassment against this organization.

---

## Constraints

### Must
- Obtain **consent first**, and stop the review if it is absent.
- Work **only from already-public information**, and record where each item was found.
- Send **findings about a person to that person**, and let them decide what to change.
- Weight **organizational controls above individual footprint reduction**, since the burden should not sit on the target.
- Distinguish **exposure that is a job requirement** — public-facing roles, published researchers, spokespeople — and protect it organizationally rather than asking people to disappear.
- Include **harassment response**, not only impersonation and fraud, and include the family-contact dimension where relevant.
- Define **retention and destruction** for whatever the review produces, since the artifact is itself a risk.
- Include the **verification procedure** that defeats impersonation regardless of exposure.

### Must Not
- Investigate anyone's private life, associations, political views, finances, or family beyond what a public-facing role has itself published.
- Compile a dossier, or produce an output that concentrates scattered public information into one convenient document about a person. Structure the output so it cannot function as a targeting package.
- Proceed without consent, or use the review to assess staff loyalty, conduct, or opinions.
- Use non-public data sources, purchased data brokers, or credentials to look anything up.
- Fabricate exposure findings or attacker capabilities.
- Recommend that staff delete their professional presence as a default. For many roles, visibility is the job.
- Retain the compiled findings indefinitely, or store them anywhere less protected than the information they concern.

---

## Instructions

### Step 1 — Confirm consent and scope
Confirm each individual knows, has agreed, and understands they will receive their own findings. Without consent, stop. Then define narrowly what is in scope by **role function** rather than by person.

### Step 2 — Identify what an attacker actually wants from each role
Payment authority, system access, credibility to impersonate to others, or the ability to distress the person into a mistake or out of a job. This determines what matters and keeps the review from drifting into general curiosity.

### Step 3 — Survey the public surface, minimally
Only what is trivially discoverable and only what is relevant to the attacker goals identified. Record where each item was found. Do not go looking beyond that boundary — the review's value is in what is easy to find, not in what is possible to find.

### Step 4 — Map pretext material
Which public facts would make an approach credible: reporting lines, project names, vendors, travel and conference attendance, internal vocabulary. Note that most of this is legitimately public and cannot be removed, which is why the fix is procedural.

### Step 5 — Assess impersonation exposure
How easily could someone impersonate this person to colleagues or partners? Public voice and writing samples, photographs, and known relationships all enable this — and again, none of it should be removed for a public-facing role.

### Step 6 — Assess harassment exposure
Contact routes, location inference, family visibility, and whether the person's subject matter attracts hostility. Note what organizational support exists and, honestly, whether it works.

### Step 7 — Build the two layers
Organizational controls first: out-of-band verification for payment and credential requests, dual authorization, a stated policy that no one will be penalized for delaying to verify, a harassment response with a named owner, and a communications position that supports targeted staff publicly. Then individual reductions, offered as options.

### Step 8 — Set retention, deliver findings, and run the adversarial check
Define how long anything is kept, where, and when it is destroyed. Deliver each person's findings to them. Then argue that this review has itself created a targeting document, and fix the output until it has not.

---

## False-Positive Prevention

1. **Review becomes surveillance.** Drifting from role exposure into a person's life, associations, or views. Consent and a narrow role-based scope are the only real controls.
2. **Output becomes a dossier.** Concentrating scattered public facts into one convenient document — exactly the artifact an attacker would want, now stored on your systems.
3. **Burden on the target.** Recommending footprint reduction as the primary fix. Organizational controls protect people who cannot and should not disappear.
4. **Visibility treated as a flaw.** Advising spokespeople, researchers, and public-facing staff to reduce presence, which asks them to stop doing their jobs.
5. **Consent skipped for expedience.** Running the review quietly "to avoid alarming people." It is discoverable, it destroys trust, and it converts a security exercise into an HR incident.
6. **Harassment omitted.** Assessing only fraud and impersonation while the actual harm to staff is abuse and intimidation.
7. **Non-public sources used.** Data brokers, purchased datasets, or credentialed lookups, which changes the review's legal and ethical character entirely.
8. **No retention limit.** Keeping the compiled findings indefinitely, so the review's artifact outlives its usefulness and becomes the exposure.

---

## Output Format

```
# Personnel exposure review — [role function, not name where avoidable]

## Consent
[Confirmed for all individuals in scope — yes/no. If no: **stop.**]

## Scope
[Defined by role function; what is explicitly out of scope: private life, associations, views, finances, family]

## What an attacker wants from this role
[Payment authority / access / impersonation credibility / ability to distress]

## Public surface relevant to those goals
| Item | Where found | Relevant to | Removable? |
|---|---|---|---|
| [reporting line] | company site | pretexting | no — legitimately public |

## Pretext material available
[Public facts that would make an approach credible — most will be unremovable, which is the point]

## Impersonation exposure
[How easily this person could be impersonated to colleagues and partners]

## Harassment exposure
[Contact routes, location inference, subject-matter hostility — and whether current support actually works]

## Layer 1 — Organizational controls (primary)
| Control | Detail | Owner |
|---|---|---|
| Out-of-band verification for payment/credential requests | | |
| Dual authorization above [threshold] | | |
| Stated policy: no penalty for delaying to verify | | |
| Harassment response protocol | | |
| Public support position for targeted staff | | |

## Layer 2 — Individual options (offered, not required)
[Delivered to the individual, for them to choose from]

## Retention
[What is kept, where, who can access it, and destruction date]

## Adversarial check
[The case that this review has created a targeting document — and what was changed so it has not]
```

---

## Verification

- [ ] Consent was confirmed before the review, and absence of consent stops it.
- [ ] Only already-public information was used; no data broker, purchased dataset, or credentialed lookup.
- [ ] Nothing about private life, associations, views, finances, or family was investigated.
- [ ] The output is structured so it cannot function as a targeting dossier, and this was explicitly tested.
- [ ] Organizational controls are the primary layer; individual reductions are offered as options.
- [ ] Job-required visibility is protected organizationally rather than treated as a flaw to remove.
- [ ] Harassment exposure is assessed alongside fraud and impersonation.
- [ ] Findings about a person are delivered to that person.
- [ ] Retention, storage, access, and destruction are defined.
- [ ] The review was not used to assess loyalty, conduct, or opinions.
