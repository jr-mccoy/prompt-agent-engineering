---
title: "PACU Educator Toolkit — Shared Safety Preamble"
category: healthcare-clinical/perianesthesia
description: "The shared safety preamble for every perianesthesia artifact: what the toolkit is and is not, the non-negotiable content rules (no invented doses, thresholds, protocols, sources or scope), and the verification checklist before use."
techniques:
  - OC-10
  - CM-02
  - OC-09
  - CM-09
  - QA-01
difficulty: intermediate
tags:
  - pacu
  - safety
  - patient-safety
  - nursing
updated: "2026-10-06"
---

# PACU Educator Toolkit — Shared Safety Preamble

> **Medical disclaimer — read before use.** This prompt is an educational aid for
> **licensed perianesthesia clinicians and their educators** — not clinical decision
> support; the toolkit's `SAFETY_PREAMBLE.md` governs. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

**Scope:** This preamble applies to every skill, prompt, image meta-prompt, and orchestrator
artifact in `domain-healthcare-clinical/prompts/perianesthesia/`. Individual artifacts carry a one-line safety reminder that
points here; this file is the full version. Inline it into any generated artifact when you want
stronger coverage than the one-line reminder gives.

---

## 1. What this toolkit is — and is not

Everything produced by this toolkit is an **educational aid for licensed perianesthesia clinicians
and their educators**. It is not:

- a clinical decision-support system;
- a dosing calculator or drip-rate calculator;
- a substitute for provider orders, facility protocol, or the bedside nurse's own judgment;
- a source of medical advice for patients or the public;
- an authority on any facility's scope of practice.

Nothing generated here should reach a patient, a chart, or a policy document without review by a
qualified clinician and reconciliation against current institutional policy.

## 2. Non-negotiable content rules

These bind every artifact the toolkit produces.

1. **No invented doses.** Never state a dose, concentration, dilution, infusion rate, bolus volume,
   or administration interval. Where a number would appear, write `per provider order`.
2. **No invented thresholds.** Never state a vital-sign cut-off, lab threshold, discharge score,
   temperature target, or device setting. Write `per facility protocol`.
3. **No invented facility protocols.** Escalation chains, activation criteria, rapid-response
   triggers, and staffing rules vary by institution. Describe the *category* of action and route the
   specific value to local policy.
4. **No invented sources.** Cite real reference works by chapter title inline (for example,
   "*Drain's*, Ch. 32: Gynecologic Surgery"). Never fabricate a citation, page number, guideline
   number, or URL. If the source is not known, say so rather than approximating it.
5. **No scope inflation.** Do not imply that a PACU nurse may independently initiate therapy that
   requires a provider order, nor assume a scope that a given unit's competency validation does not
   grant.

## 3. Required safety posture in generated material

Every generated artifact should:

- open with a visible safety reminder line;
- name the **reversible/physiologic causes first** for any symptom-based topic, so learners hunt the
  cause rather than treating the number;
- state **who to escalate to and when**, by role rather than by name;
- distinguish **recognition and escalation** (nursing priority) from **treatment** (provider order);
- flag high-risk populations explicitly where relevant (obesity/OSA, pediatric, geriatric, obstetric,
  ambulatory/day-surgery, cardiac).

## 4. Reversal, rescue, and high-alert topics

Artifacts covering reversal agents, rescue drugs, or time-critical emergencies carry two additional
obligations:

- state that **duration mismatch and re-sedation/recurarization are expected risks**, so surveillance
  does not stop at the first good response; and
- state that the nurse's role is **early recognition, calling for help, and retrieving resources**,
  with all pharmacology per provider order and the applicable protocol or checklist.

## 5. Images and visual artifacts

Image meta-prompts produce **layout-and-rendering** instructions, not sources of clinical truth.
Image models are not anatomically or numerically reliable. Every clinical structure, label, value,
and relationship in a generated image must be supplied by the user from an expert-verified source
and checked by a qualified reviewer before any instructional use.

## False-Positive Prevention

When applying this document, the failure is an artifact that *looks* compliant with §2 and §6 while breaking them:

❌ **DON'T:**
- Count `per provider order` or `per facility protocol` in the body as compliance when the same artifact fills the slot elsewhere — a worked example, quiz answer key, rationale, image label, table footnote or "typical value" aside that supplies the number.
- Accept a citation because it has the right shape ("*Drain's*, Ch. N: Title"). A chapter title or number that does not exist in the named edition passes a skim of §2 rule 4 on form alone.
- Tick "safety reminder line present" when it appears only at the end, inside a collapsed section, or in the generator prompt but not in the generated artifact.
- Let passive voice hide who acts ("naloxone is given", "the airway is secured", "the infusion is titrated") — scope inflation that never names the nurse still fails rule 5.
- Treat escalation as "by role" when the role comes attached to an invented pager number, response time or activation criterion.

✅ **DO:**
- Run §6 as a search, not a read-through: scan the whole artifact — examples, answer keys, image prompts, tables, alt text — for digits and units (mg, mcg, mL, /min, /h, %, °, mmHg, score values) and account for every hit (a chapter or stage number is allowed; a dose, rate or cut-off is not).
- Check each cited chapter against the table of contents of the named edition; if it cannot be checked, replace it with "source not verified" rather than keeping the closest-sounding title.
- For each clinical action verb, name the actor; any action that needs a provider order must say `per provider order` beside it.

## 6. Verification checklist before use

- [ ] No dose, rate, concentration, or interval appears anywhere in the artifact.
- [ ] No vital-sign, lab, score, or device-setting threshold is stated as fact.
- [ ] Every citation names a real reference work and chapter; none were invented.
- [ ] Escalation is described by role and routed to facility policy.
- [ ] The scope described matches what a PACU nurse may actually do.
- [ ] A safety reminder line is present near the top of the artifact.
- [ ] A qualified clinician has reviewed the artifact against current local protocol.
