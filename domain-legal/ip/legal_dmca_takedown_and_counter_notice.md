---
title: "DMCA Takedown Notice and §512(g) Counter-Notice"
category: legal/ip
description: "Draft a DMCA §512(c)(3) takedown notice or §512(g) counter-notice with every statutorily required element, perjury statements, jurisdictional consent, and §512(f) misrepresentation risk assessment under Lenz v. Universal."
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
  - ip
  - copyright
  - dmca
  - takedown
updated: "2026-05-11"
related_prompts:
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
  - domain-legal/ip/legal_open_source_license_compatibility_review.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
---

**Purpose:** Draft a fully compliant DMCA §512(c)(3) takedown notice **or** §512(g)(3) counter-notice. Output must contain every statutorily required element with no omissions, accurate identification of the work and the material, signed perjury statements, and (for counter-notices) consent to federal jurisdiction and service-of-process designation. Includes a pre-flight check against §512(f) misrepresentation exposure under *Lenz v. Universal Music Corp.*

**When to use:** Sending a takedown to an online service provider (OSP) under 17 U.S.C. §512(c); responding to a takedown with a counter-notice under §512(g); auditing a takedown program for §512(f) liability exposure; drafting standing takedown / counter-notice templates for an in-house team or platform.

---

## Your Input

- **Jurisdiction:** [US federal — DMCA is federal under 17 U.S.C. §512. Counter-notices require consent to a specific federal district court — typically (a) the federal district where the OSP's address is located if the subscriber is in the US, or (b) any judicial district in which the OSP may be found if the subscriber is outside the US, per §512(g)(3)(D)]
- **Document type:** [§512(c)(3) takedown notice / §512(g)(3) counter-notice / pre-flight §512(f) audit only]
- **Sender role:** [Copyright owner / authorized agent (with documentation) / subscriber alleged to have infringed]
- **Online service provider (OSP):** [Name, DMCA-designated agent name and contact per OSP's USCO registration, address, email — verify via the USCO DMCA Designated Agent Directory `[CITE: https://www.copyright.gov/dmca-directory/]`]
- **The copyrighted work allegedly infringed (for takedowns):** [Title, author, year, registration number (`[CITE: Reg. No. _______]`) or unregistered status, URL or location of the authoritative copy]
- **The infringing material (for takedowns):** [Specific URLs — one per item; if many items on one URL, identify each with sufficient location info to find and disable; do not use overbroad URL patterns]
- **The material taken down (for counter-notices):** [Specific URL(s) and identification before removal or disabling]
- **Subscriber identity (for counter-notices):** [Legal name, mailing address, telephone, email — must be accurate; this information will be provided to the takedown sender]
- **Fair-use / authorization / non-infringement basis (for counter-notices and for §512(f) audit on takedowns):** [The basis for good-faith belief; for counter-notices, the basis for good-faith belief the material was removed by mistake or misidentification]
- **Fair-use pre-flight analysis (for takedowns):** [Has the sender considered fair use before issuing the notice? Per *Lenz v. Universal Music Corp.*, 815 F.3d 1145 (9th Cir. 2016) [CITE: verify], copyright holders must form a subjective good-faith belief that the use is not authorized, including fair use, before sending a takedown]
- **Designated jurisdiction (for counter-notices):** [Federal district court — see jurisdiction rule above]
- **Repeat infringer policy posture (informational):** [OSP's policy under §512(i); relevant if planning a strike-based account-termination escalation]

---

## Constraints

**Must (Takedown Notice — §512(c)(3)(A)):**
- Include a **physical or electronic signature** of the copyright owner or authorized agent (§512(c)(3)(A)(i)).
- **Identify the copyrighted work** claimed to have been infringed, or — for multiple works on a single site — a representative list (§512(c)(3)(A)(ii)).
- **Identify the material that is claimed to be infringing** with information reasonably sufficient to permit the OSP to locate it (URLs are the standard) (§512(c)(3)(A)(iii)).
- Provide **contact information** for the complaining party: name, address, telephone, and email (§512(c)(3)(A)(iv)).
- Include a **good-faith belief statement**: "I have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law." (§512(c)(3)(A)(v)).
- Include an **accuracy / authority statement under penalty of perjury**: "I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed." (§512(c)(3)(A)(vi)).
- Conduct a **fair-use consideration** before sending, per *Lenz*. Document the basis.

**Must (Counter-Notice — §512(g)(3)):**
- Include a **physical or electronic signature** of the subscriber (§512(g)(3)(A)).
- **Identify the material** that has been removed or disabled and the location at which it appeared before removal (§512(g)(3)(B)).
- Include a **good-faith belief statement under penalty of perjury**: "I swear, under penalty of perjury, that I have a good faith belief that the material was removed or disabled as a result of mistake or misidentification of the material to be removed or disabled." (§512(g)(3)(C)).
- Provide the subscriber's **name, address, and telephone number** (§512(g)(3)(D)).
- Include **consent to the jurisdiction of Federal District Court** — the district where the subscriber's address is located if in the US, or any district in which the OSP may be found if outside the US (§512(g)(3)(D)).
- Include **acceptance of service of process** from the original takedown sender or their agent (§512(g)(3)(D)).

**Must Not:**
- Omit any statutorily required element. A defective notice does not impose §512(c)(1)(C) actual-knowledge on the OSP and may not trigger the takedown obligation.
- Use overbroad URL patterns ("the entire site at example.com/user/X"); identify specific URLs.
- Send a takedown without considering fair use — *Lenz* exposure under §512(f) for material misrepresentation.
- Send a takedown for material the sender does not own or have authorization to enforce — §512(f) liability for misrepresentation.
- Sign a counter-notice without an accurate subscriber address; the OSP will forward the counter-notice (with the address) to the takedown sender.
- Fabricate registration numbers; registration is not required to send a §512 notice, but if cited it must be accurate.
- Insert generic disclaimers; this is the operative legal document.
- Treat the OSP's privately drafted "DMCA form" as a substitute for the statutory elements — the form must collect each §512(c)(3) or §512(g)(3) element.

---

## Instructions

### For a Takedown Notice (§512(c)(3))

1. **To/From header.** OSP's DMCA-designated agent (verified via USCO directory) and the sender's identity / authority.
2. **Statement of authority.** "I am the copyright owner of the work identified below" OR "I am authorized to act on behalf of the copyright owner, {name}, of the work identified below." Attach authorization if agent.
3. **Identification of the copyrighted work.** Title, author, year of creation, year of publication, registration number if any (or "unregistered"), URL to the authoritative copy.
4. **Identification of the infringing material.** Each URL on its own line; brief description of the infringing element (full copy, identifiable portion, derivative).
5. **Contact information.** Full name, mailing address, telephone, email.
6. **Good-faith belief statement** — verbatim from §512(c)(3)(A)(v).
7. **Accuracy / authority statement under penalty of perjury** — verbatim from §512(c)(3)(A)(vi).
8. **Fair-use consideration documentation** (internal — preserve with the file).
9. **Signature** (physical or electronic).
10. **Date.**

### For a Counter-Notice (§512(g)(3))

1. **To/From header.** OSP's DMCA-designated agent and the subscriber's identity.
2. **Identification of the removed material and its prior location.** URL(s) where it appeared before takedown.
3. **Good-faith belief statement under penalty of perjury** — verbatim from §512(g)(3)(C).
4. **Subscriber contact information.** Full legal name, mailing address, telephone — this will be provided to the takedown sender.
5. **Consent to federal jurisdiction.** Specify the district per §512(g)(3)(D).
6. **Acceptance of service of process.** From the takedown sender or agent.
7. **Signature** (physical or electronic).
8. **Date.**

### For a §512(f) Misrepresentation Pre-Flight (Audit)

1. Does the sender own the copyright or have documented authorization?
2. Has the sender considered whether the use is fair use, licensed, or otherwise authorized?
3. Is the material identified actually a copy of the work identified, or a derivative within §106(2)?
4. Are the URLs specific and accurate?
5. Is the good-faith belief subjectively held (not merely objectively reasonable)?
6. Document the analysis for the file.

---

## Output Format

### Takedown Notice (§512(c)(3))

```markdown
{Date}

VIA EMAIL TO DMCA-DESIGNATED AGENT
{OSP DMCA-Designated Agent Name}
{OSP Legal Name}
{Address}
{Email per USCO directory}

Re: Notice of Claimed Infringement Under 17 U.S.C. §512(c)

Dear DMCA Agent:

I, {name}, write pursuant to the Digital Millennium Copyright Act, 17 U.S.C. §512(c). I am {the copyright owner of / authorized to act on behalf of the owner of, {owner name},} the copyrighted work identified below.

1. IDENTIFICATION OF COPYRIGHTED WORK
Title: {title}
Author: {author}
Year of creation / publication: {year}
Registration: {Reg. No. _______ | Unregistered}
Authoritative copy located at: {URL}

2. IDENTIFICATION OF INFRINGING MATERIAL
The following material hosted on your service infringes the foregoing copyrighted work:
- {URL 1} — {brief description}
- {URL 2} — {brief description}

3. CONTACT INFORMATION
Name: {full name}
Address: {mailing address}
Telephone: {phone}
Email: {email}

4. GOOD-FAITH BELIEF STATEMENT
I have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.

5. ACCURACY AND AUTHORITY STATEMENT UNDER PENALTY OF PERJURY
I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner or am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.

Signature: ____________________________
{Printed name}
{Title, if agent}
Date: {date}
```

### Counter-Notice (§512(g)(3))

```markdown
{Date}

VIA EMAIL TO DMCA-DESIGNATED AGENT
{OSP DMCA-Designated Agent Name}
{OSP Legal Name}
{Address}
{Email}

Re: Counter-Notice Under 17 U.S.C. §512(g)

Dear DMCA Agent:

I, {subscriber legal name}, submit this counter-notice under 17 U.S.C. §512(g) regarding material removed or disabled by {OSP} on or about {date}.

1. IDENTIFICATION OF MATERIAL AND PRIOR LOCATION
The material removed or disabled, and the location at which it appeared before removal or disabling, is:
- {URL 1} — {brief description}
- {URL 2} — {brief description}

2. GOOD-FAITH BELIEF STATEMENT UNDER PENALTY OF PERJURY
I swear, under penalty of perjury, that I have a good faith belief that the material was removed or disabled as a result of mistake or misidentification of the material to be removed or disabled.

3. SUBSCRIBER CONTACT INFORMATION
Name: {full legal name}
Address: {mailing address}
Telephone: {phone}

4. CONSENT TO JURISDICTION
I consent to the jurisdiction of the United States District Court for the {district} (the judicial district in which my address is located; or if my address is outside the United States, any judicial district in which {OSP} may be found).

5. ACCEPTANCE OF SERVICE
I will accept service of process from the person who provided notification under 17 U.S.C. §512(c)(1)(C) or an agent of such person.

Signature: ____________________________
{Printed name}
Date: {date}
```

### §512(f) Pre-Flight Checklist (Internal Document)

```markdown
# §512(f) Misrepresentation Risk Audit — {Matter}
- [ ] Sender owns the copyright or has documented authorization (attach).
- [ ] Sender has considered whether the use is fair use (document analysis, citing the four §107 factors per *Lenz*).
- [ ] Sender has considered whether the use is licensed or otherwise authorized.
- [ ] Material identified is a copy of, or a derivative within §106(2) of, the work identified.
- [ ] URLs are specific and accurate; no overbroad patterns.
- [ ] Good-faith belief is subjectively held by the signatory.
- [ ] Notice is not being used as a competitive or non-copyright pretext.

**Risk grade:** {Low / Moderate / High}
**Mitigation:** {narrow URLs / re-do fair-use analysis / seek license clearance instead / withdraw}
```

---

## Verification

- [ ] **Takedown:** Every §512(c)(3)(A) element present (signature, identification of work, identification of material, contact info, good-faith belief, perjury accuracy/authority).
- [ ] **Takedown:** Good-faith belief statement is verbatim from the statute.
- [ ] **Takedown:** Perjury statement is verbatim from the statute and signed.
- [ ] **Takedown:** Material is identified by specific URLs, not overbroad patterns.
- [ ] **Takedown:** *Lenz* fair-use consideration is documented in the file.
- [ ] **Counter-notice:** Every §512(g)(3) element present (signature, identification of material + prior location, perjury good-faith belief, contact info, consent to jurisdiction, acceptance of service).
- [ ] **Counter-notice:** Subscriber address is accurate (will be forwarded to takedown sender).
- [ ] **Counter-notice:** Federal district court designation matches the §512(g)(3)(D) rule.
- [ ] **Both:** Sent to the OSP's USCO-registered DMCA-designated agent (verified via copyright.gov directory).
- [ ] **Both:** No fabricated registration numbers, URLs, or signatures.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Sending to "support@" or "abuse@" instead of the DMCA-designated agent | Verify via the USCO DMCA Designated Agent Directory; an OSP can lose §512 safe harbor only if its registered agent receives compliant notice |
| Omitting the perjury statement or paraphrasing it | The statute specifies the substance; quote it verbatim to avoid defective notice |
| Listing "all infringing content at example.com/user/X" as the URL | §512(c)(3)(A)(iii) requires information sufficient to locate the material — list each URL |
| Skipping fair-use analysis before sending | *Lenz* requires subjective good-faith consideration of fair use; failure exposes §512(f) liability |
| Using a takedown to remove material on non-copyright grounds (defamation, trademark, competitive) | §512(f) liability — the notice swears the material is copyright-infringing |
| Counter-notice without consent to federal jurisdiction | §512(g)(3)(D) is a strict element; counter-notice is defective without it and OSP need not restore |
| Counter-notice from outside the US without designating "any district in which the OSP may be found" | §512(g)(3)(D) has a separate rule for non-US subscribers — apply correctly |
| Subscriber using a P.O. box or false address on counter-notice | The address is forwarded to the takedown sender for service; falsity exposes §512(f) and §1001 risk |
| Treating a defective takedown as a no-op | OSP may still respond if it has actual knowledge or red-flag awareness under §512(c)(1)(A); coach the OSP accordingly |
| Repeat-infringer policy mismatches | §512(i) requires a reasonably implemented repeat-infringer policy; misalignment can cost the OSP safe harbor (*BMG v. Cox*) |
| Fabricating registration numbers | Registration is not required to send a §512 notice; do not invent one |
