# PACU Educator Toolkit — Shared Safety Preamble

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

## 6. Verification checklist before use

- [ ] No dose, rate, concentration, or interval appears anywhere in the artifact.
- [ ] No vital-sign, lab, score, or device-setting threshold is stated as fact.
- [ ] Every citation names a real reference work and chapter; none were invented.
- [ ] Escalation is described by role and routed to facility policy.
- [ ] The scope described matches what a PACU nurse may actually do.
- [ ] A safety reminder line is present near the top of the artifact.
- [ ] A qualified clinician has reviewed the artifact against current local protocol.
