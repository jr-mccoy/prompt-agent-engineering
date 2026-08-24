---
title: "Preprint Release Plan"
category: science/writing-communication
description: "Plan a preprint release: select the discipline-matched server, choose a Creative Commons license, verify the target journal allows preprinting, and lock versioning, DOI, data/code, consent, and post-print update path — with preprinting as the default."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - QA-02
  - NE-10
difficulty: advanced
tags:
  - preprint
  - biorxiv
  - arxiv
  - chemrxiv
  - creative-commons
  - journal-policy
  - versioning-doi
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_conference_abstract_drafter.md
  - domain-science/writing-communication/science_poster_designer.md
---

# Preprint Release Plan

**Objective:** Produce a concrete release plan for posting a preprint: select the server that matches the discipline, choose a Creative Commons license with its reuse tradeoffs surfaced, verify the target journal permits preprinting, and lock versioning/DOI, a data and code availability statement, an author-consent and competing-interests check, and a post-publication update path. Preprinting is the default; opting out requires a reasoned branch. Server scopes and license terms are cited, but all policies are verify-on-site.

**When to use:** You have a manuscript (or near-final draft) and need to decide whether, where, and how to preprint it before or alongside journal submission.

**Required inputs:**
- **Discipline.** Field and subfield (drives server selection; clinical/health work routes to a screened server).
- **Finding / work context.** What the manuscript reports, its status (draft / submitted / in revision), and whether it involves human-subjects, clinical, or otherwise sensitive content. Never invented.
- **Target venue or audience.** The journal(s) you intend to submit to (needed for the preprint-policy check) and the readership you want the preprint to reach.
- **Authorship & consent status.** `[user-supplied]` — are all co-authors informed and consenting to preprint; any institutional/funder posting requirements.

**Optional inputs:**
- Existing data/code repositories and their DOIs; data sensitivity or embargo constraints.
- Funder open-access mandates (e.g., zero-embargo CC-BY requirements).
- Reuse goals (do you want commercial reuse, derivatives, text/data mining permitted).
- Whether a press release or journal embargo is planned.
- Preferred timing relative to journal submission (before, concurrent, after acceptance).

**Constraints — Must:**
- Open with discipline, finding context, target journal(s), and consent status before planning.
- Make preprinting the default recommendation; provide a reasoned opt-out branch only when a concrete blocker exists (e.g., a target journal that forbids preprints, an unresolved data-sensitivity or consent issue, or a patent/IP timing concern).
- Select the server by matching discipline to scope: bioRxiv (biology), medRxiv (clinical/health — note its screening for clinical content), arXiv (physics/math/CS/quant), ChemRxiv (chemistry), EarthArXiv (earth/planetary/environmental), SSRN (social sciences/economics/law), OSF Preprints (multidisciplinary / discipline-specific overlays). State the match and the runner-up.
- Recommend a license with tradeoffs: CC-BY as the default for maximum reuse and citation; surface CC-BY-NC (blocks commercial reuse — can limit downstream use) and CC0 (public-domain dedication — maximal reuse, no attribution requirement) as alternatives. Tie the choice to funder mandates if supplied.
- Require the user to verify the target journal's preprint policy via Sherpa Romeo / Transpose; do not assert a journal's policy from memory.
- Plan versioning + DOI: how versions are numbered, when to post an updated version, and how the preprint DOI relates to the eventual published DOI.
- Include a data/code availability statement and a competing-interests/consent check.
- Define the post-print update path (link the published version, post the accepted version if permitted, retract/withdraw conditions).

**Constraints — Must Not:**
- Do not invent results, citations, DOIs, conference requirements, or server policies. Draft only from user-supplied content; mark gaps `[user-supplied]` / "verify on the venue/server site".
- Do not assert that a specific journal allows or forbids preprints from memory — route to Sherpa Romeo / Transpose for the user to verify.
- Do not state a server's current scope, screening, or license options as fixed fact without a verify-on-site flag.
- Do not recommend posting without confirming all co-authors consent.
- Do not use "novel", "groundbreaking", or "first-ever" in any drafted summary text.

**Instructions:**

1. **Confirm the frame.** Restate discipline, finding context, target journal(s), data/consent status, and funder mandates (flag `[user-supplied]`).
2. **Default to preprinting; test for blockers.** State preprinting as the default. Probe for opt-out triggers: a target journal that forbids preprints, unresolved consent, data sensitivity, clinical-screening needs, or IP/patent timing. Use a probability-weighted read of the blockers to decide default vs opt-out, and present the branch honestly.
3. **Select the server.** Match discipline to server scope; name the primary choice and a runner-up, with a one-line rationale each. For clinical/health work, route to medRxiv and note its screening step. Flag all scope claims verify-on-site.
4. **Choose the license.** Recommend CC-BY as default; lay out CC-BY-NC and CC0 tradeoffs; reconcile with any funder open-access mandate. Note that the chosen server may constrain license options (verify on the server).
5. **Verify the journal preprint policy.** Instruct the user to check the target journal(s) on Sherpa Romeo and/or Transpose for: whether preprints are allowed, which version may be posted, citation/DOI requirements, and any media/embargo rules. Do not pre-judge the answer.
6. **Plan versioning, DOI, and data/code.** Define version numbering, when to post v2+ (major revisions, post-acceptance), how the preprint DOI links to the published DOI, and write a data/code availability statement (with repository DOIs or `[user-supplied]`).
7. **Run consent and competing-interests checks.** Confirm all co-authors consent to preprint; capture competing interests and funding disclosures; note institutional posting requirements.
8. **Define the post-print update path.** Specify linking the published version to the preprint, posting the accepted manuscript if the journal permits, and the conditions/process for withdrawal or correction.
9. **Emit the release checklist + decision table.** Produce a server/license/journal-policy decision table and a sequential release checklist with each verify-on-site item flagged.

**Output format (locked):**

```
## Frame
- Discipline | Finding context | Target journal(s) | Consent status [user-supplied] | Funder mandate [user-supplied]

## Default recommendation
- Preprint: YES (default) / opt-out — with reason
- Opt-out branch (if any): trigger + rationale

## Server selection
| Choice | Server | Scope match | Notes (screening / verify-on-site) |
|---|---|---|---|
| Primary | ... | ... | ... |
| Runner-up | ... | ... | ... |

## License recommendation
- Recommended: CC-BY (default) — rationale
- Alternatives: CC-BY-NC (tradeoff) | CC0 (tradeoff)
- Funder-mandate reconciliation: [user-supplied]
- Server license constraints: [verify on the server site]

## Journal preprint-policy check
- Action: verify target journal(s) on Sherpa Romeo / Transpose
- What to confirm: preprints allowed? which version? citation/DOI rules? media/embargo?
- Status: [user to verify — do not assume]

## Versioning, DOI & data/code
- Version plan: v1 ... v2+ triggers ...
- DOI: preprint DOI ↔ published DOI linkage
- Data availability: [user-supplied] | Code availability: [user-supplied]

## Consent & disclosures
- Co-author consent: [user-supplied] | Competing interests: [user-supplied] | Funding: [user-supplied]

## Post-print update path
- Link published version | Post accepted manuscript (if permitted) | Withdrawal/correction conditions

## Release checklist
- [ ] sequential steps, each verify-on-site item flagged

## Flags & gaps
- [items marked user-supplied or verify-on-site]
```

**Reporting-standard / convention alignment:** Preprint server scopes (bioRxiv, medRxiv, arXiv, ChemRxiv, EarthArXiv, SSRN, OSF Preprints — verify on site); Creative Commons licensing (CC-BY / CC-BY-NC / CC0); preprint↔journal policy verification via Sherpa Romeo and Transpose; DOI and versioning conventions; open-science data/code availability statements.

**Verification checklist (before delivering):**
- [ ] Discipline, finding context, target journal(s), and consent status were captured first.
- [ ] Preprinting is the stated default; any opt-out has a concrete, reasoned trigger.
- [ ] Server selection matches discipline; clinical/health work routes to medRxiv with screening noted.
- [ ] License recommendation includes CC-BY default plus CC-BY-NC / CC0 tradeoffs and funder reconciliation.
- [ ] Journal preprint policy is routed to Sherpa Romeo / Transpose for the user to verify — not asserted.
- [ ] Versioning, DOI linkage, and a data/code availability statement are planned.
- [ ] Co-author consent and competing-interests checks are present.
- [ ] A post-print update path and a flagged release checklist are produced.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Asserted journal policy | "Journal X allows preprints" stated confidently | Route to Sherpa Romeo / Transpose; never assert from memory |
| Wrong server | A clinical study planned for bioRxiv | Match discipline to scope; clinical → medRxiv with screening note |
| License mismatch | CC-BY-NC chosen where a funder mandates CC-BY | Reconcile license with funder mandate; surface NC/CC0 tradeoffs |
| Stale scope claim | A server's scope/screening stated as current fact | Flag all server scope/policy claims verify-on-site |
| Consent skipped | A plan that posts before co-authors agree | Require explicit co-author consent before recommending posting |
| Version drift | Preprint left unlinked to the published version | Plan DOI linkage and a post-print update path |
| Default-off bias | Treating preprinting as optional by habit | Make preprinting the default; require a concrete blocker to opt out |
