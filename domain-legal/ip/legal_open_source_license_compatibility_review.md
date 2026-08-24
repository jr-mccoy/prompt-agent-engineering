---
title: "Open Source License Compatibility Review"
category: legal/ip
description: "Compatibility analysis for a dependency tree against a project's outbound license: classify each license by copyleft tier, evaluate static/dynamic linking and SaaS/network-use implications, surface patent grants, attribution duties, CLA/DCO posture, and produce a pass/fail-with-remediation report."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - ip
  - open-source
  - copyleft
  - license-compatibility
updated: "2026-05-11"
related_prompts:
  - domain-legal/ip/legal_copyright_fair_use_analysis.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-legal/ip/legal_dmca_takedown_and_counter_notice.md
---

**Purpose:** Audit a software project's dependency tree against its outbound license. Identify every license, classify it by copyleft tier, evaluate the linking and distribution facts, surface attribution and patent obligations, and produce a pass / pass-with-remediation / fail report. Output supports diligence, release sign-off, M&A IP schedules, and shipping decisions.

**When to use:** Pre-release license audit; M&A code diligence (target's outbound license vs. inbound licenses); shipping decision on a new feature; switching outbound license; preparing OSS attribution / NOTICE file; responding to a license-compliance inquiry; auditing AI model weights and training-data licenses (separately from code).

---

## Your Input

- **Jurisdiction:** [US federal copyright (17 U.S.C.) governs licenses on US-distributed software; foreign distribution may implicate other jurisdictions — note that OSS licenses are copyright licenses, and enforceability has been confirmed under US law (*Jacobsen v. Katzer*, Fed. Cir. 2008 — verify [CITE: ...])]
- **Project outbound license:** [The license under which the project ships — e.g., MIT / Apache-2.0 / GPL-3.0 / AGPL-3.0 / MPL-2.0 / proprietary / dual-license / SSPL — quote text or version]
- **Distribution model:** [Distributed binary / distributed source / SaaS-only (no distribution) / on-premises appliance / embedded / mobile app / library shipped to third parties]
- **Network-use posture:** [Whether the software is accessed over a network (relevant for AGPL §13 and SSPL §13)]
- **Linking posture:** [For each dependency: static linking / dynamic linking / process-separated / network API call only — this affects LGPL §4–§6, GPL combined-work analysis]
- **Dependency tree:** [Complete list — direct and transitive — with: name, version, license (SPDX identifier preferred), source URL, modification status (modified by us / unmodified)]
- **License text sources:** [Whether each license text is included verbatim from the upstream package — quote / paraphrase / `[NEED: ...]` if missing]
- **CLA / DCO posture:** [Whether contributors sign a CLA (e.g., Apache CLA) or assert DCO sign-off; whether inbound = outbound (Apache project default) or contributor grants extra rights]
- **Patent posture:** [Apache 2.0 §3 patent grant + termination; GPL-3.0 §11 patent grant; explicit patent reservations from any contributor]
- **Trademark posture:** [Any project marks subject to a trademark policy distinct from the copyright license — Apache, Mozilla, npm names]
- **Attribution surface:** [Where NOTICE / attribution will appear — about box, app store listing, distribution archive, documentation page]
- **AI model weights / training data (if applicable):** [Separate license analysis — Llama Community License, OpenRAIL, BigScience RAIL — these are not OSI-approved and may not be "open source" in the OSI sense; flag accordingly]

---

## Constraints

**Must:**
- Identify the license for **every** dependency (direct + transitive). An unidentified license is a blocker, not a finding.
- Classify each license by **copyleft tier**:
  - **Strong copyleft:** GPL-2.0, GPL-3.0, AGPL-3.0, SSPL-1.0 (note SSPL is not OSI-approved).
  - **Network copyleft:** AGPL-3.0 §13 (extends to remote network users); SSPL §13 (extends to providing service).
  - **Weak / file-level copyleft:** LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0, CDDL-1.0, CC-BY-SA-4.0 (for non-code).
  - **Permissive:** MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Unlicense, 0BSD.
  - **Public domain dedications:** CC0-1.0, Unlicense — verify enforceability in non-US jurisdictions.
  - **Non-OSS / "source-available":** SSPL, BSL (Business Source License), Elastic v2, RSAL, Confluent Community License, Llama Community License — these are not OSI-approved and may have field-of-use or anti-competition restrictions.
- Apply the **outbound-vs-inbound compatibility matrix**:
  - **Permissive ← Permissive:** generally compatible.
  - **Strong copyleft ← Permissive:** generally compatible into the copyleft work (the combined work goes out as copyleft).
  - **Permissive ← Strong copyleft:** **incompatible** if distributed as a combined work (GPL "viral" effect requires outbound under GPL).
  - **GPL-2.0-only ← Apache-2.0:** **incompatible** (Apache 2.0's patent-termination clause conflicts with GPL-2.0's "no further restrictions"). GPL-3.0 resolves this.
  - **GPL-3.0 ← Apache-2.0:** compatible into GPL-3.0.
  - **LGPL ← any:** allowed for library use; dynamic linking permits proprietary combined work; static linking imposes additional obligations.
  - **MPL-2.0 ← any:** file-level copyleft; modified MPL files must stay MPL but can combine with other licensed files in a larger work.
  - **AGPL-3.0 ← any:** strong copyleft + network-use trigger; any SaaS deployment makes source-disclosure obligation applicable to remote users.
- Evaluate **linking and combined-work analysis**:
  - **Static linking:** generally creates a combined work under GPL — strong copyleft propagates.
  - **Dynamic linking:** debated under GPL; FSF treats as combined work; some courts have not squarely ruled. LGPL §4–§6 expressly permits dynamic linking with relinking obligation.
  - **Process separation / IPC / network API:** generally not a combined work under FSF's view; safer boundary.
  - Note: legal treatment is unsettled and depends on the integration facts.
- Evaluate **network-use triggers**:
  - **AGPL-3.0 §13:** if the modified work is accessed by users over a network, source must be offered to those users.
  - **SSPL §13:** if the program is offered as a service, all programs used to provide the service must be released under SSPL (broader than AGPL).
- Surface **patent grant and termination provisions**:
  - **Apache 2.0 §3:** express patent grant from contributors; terminates if licensee initiates patent litigation alleging the work infringes.
  - **GPL-3.0 §11:** express patent grant; broad downstream coverage.
  - **MIT / BSD:** **no express patent grant** — only an implied license; M&A diligence often flags this.
- Surface **attribution and NOTICE duties**:
  - **MIT / BSD / Apache 2.0:** require including the license text and copyright notices in distributions.
  - **Apache 2.0 §4(d):** if the original work contained a NOTICE file, downstream must include it (read-only attribution).
  - **GPL family:** must include the license, source code (or written offer), and prominent notices on modifications.
- Surface **CLA / DCO posture** affecting outbound license decisions:
  - **CLA (Contributor License Agreement):** typically grants the project broader rights than the outbound license (e.g., relicensing power). Apache iCLA, GNU FSF copyright assignment, Google CLA.
  - **DCO (Developer Certificate of Origin):** Linux kernel model — sign-off attests the contributor has the right to contribute but does not transfer rights.
- Flag **non-OSS license restrictions** (BSL, SSPL, Elastic v2, Llama Community License) — field-of-use limits, anti-competition clauses, MAU/revenue caps, ethical-use ("do no harm") clauses.
- Produce a **per-dependency disposition**: pass / pass-with-remediation (with steps) / fail.

**Must Not:**
- Treat SPDX identifier as sufficient — verify the license text in the upstream repository matches the SPDX identifier (mismatches are common in third-party packages).
- Conflate "open source" with "free for commercial use." SSPL, BSL, Llama Community License, and most "source-available" licenses are not OSI-approved and may forbid the use case.
- Assume permissive licenses have no obligations — attribution and license-text inclusion are nearly always required.
- Treat dynamic vs. static linking as legally settled — it is not; rely on FSF guidance plus the integration facts and flag uncertainty.
- Skip transitive dependencies; the most common compliance failure is a GPL package deep in the tree.
- Treat AI model weights and training data as covered by the project's code license — they are governed separately, often by non-OSI licenses with field-of-use restrictions.
- Fabricate license text, version numbers, SPDX identifiers, or upstream URLs.
- Cite *Jacobsen v. Katzer*, *Artifex v. Hancom*, *SCO v. IBM*, *Software Freedom Conservancy v. Vizio*, or *Versata v. Ameriprise* without verifying — use `[CITE: ...]`.

---

## Instructions

1. **Header.** Project name, outbound license, distribution model, network-use posture, audit scope (direct only / direct + transitive), audit date.
2. **Dependency inventory table.** For each dependency: name, version, SPDX identifier, copyleft tier, linking posture, modification status, source URL.
3. **Per-dependency compatibility analysis.** For each dependency:
   - License classification and tier.
   - Compatibility with outbound license (apply the matrix).
   - Linking-specific analysis (static / dynamic / IPC / network).
   - Attribution / NOTICE duties triggered.
   - Patent grant / termination posture.
   - Modification disclosure obligations.
   - Disposition: pass / pass-with-remediation / fail.
4. **Cross-cutting obligations.**
   - NOTICE file aggregation (Apache 2.0 attribution).
   - SOURCE offer / availability obligation for GPL/LGPL/AGPL components.
   - AGPL §13 / SSPL §13 service-mode obligations.
   - License-text inclusion in the binary / archive / app store listing.
5. **CLA / DCO and inbound contributor flow.** Whether the project can relicense; whether contributors retain copyright; whether the patent grant flows in.
6. **Non-OSS license findings.** Each non-OSI license with field-of-use, MAU/revenue caps, anti-competition clauses, or ethical-use restrictions called out.
7. **AI model / training-data findings (if applicable).** Each non-code asset with its license; whether the use is permitted; field-of-use compliance.
8. **Remediation plan.** Ordered actions: replace dependency / re-engineer integration to process-separation / negotiate dual-license / dual-license outbound / open-source the combined work / remove feature.
9. **Final disposition.** Pass / Pass-with-Remediation (with item-by-item remediation tracking) / Fail.

---

## Output Format

```markdown
# Open Source License Compatibility Review — {Project}
**Outbound license:** {SPDX identifier + version}
**Distribution model:** {distributed binary / SaaS-only / on-premises / library / embedded}
**Network use:** {yes — AGPL §13 / SSPL §13 implicated | no}
**Audit scope:** {direct only | direct + transitive — N dependencies}
**Audit date:** {date}

## 1. Dependency Inventory
| # | Name | Version | SPDX | Tier | Linking | Modified? | Source |
|---|---|---|---|---|---|---|---|
| 1 | {pkg} | {v} | {MIT} | Permissive | static | no | {URL} |
| 2 | {pkg} | {v} | {GPL-3.0-only} | Strong copyleft | dynamic | no | {URL} |
| 3 | {pkg} | {v} | {Apache-2.0} | Permissive | static | yes | {URL} |
| ... | ... | ... | ... | ... | ... | ... | ... |

## 2. Per-Dependency Compatibility

### #1 — {pkg} v{version} ({SPDX})
**Classification:** {permissive — MIT — no express patent grant}
**Compatibility with outbound {outbound SPDX}:** {compatible — combined work goes out as {outbound}}
**Linking:** {static — no special obligation beyond attribution}
**Attribution / NOTICE duty:** {include license text + copyright notices in distribution}
**Patent posture:** {implied license only — flag for M&A diligence}
**Modification disclosure:** {n/a — unmodified}
**Disposition:** **PASS** — include MIT license text in NOTICE.

### #2 — {pkg} v{version} ({GPL-3.0-only})
**Classification:** {strong copyleft — GPL-3.0}
**Compatibility with outbound {outbound SPDX, e.g., MIT}:** **INCOMPATIBLE** — distributing a combined work would require outbound under GPL-3.0, not MIT.
**Linking:** {dynamic — FSF treats as combined work; legal treatment unsettled but conservative reading is combined work [CITE: FSF guidance]}
**Attribution / NOTICE duty:** {include GPL-3.0 license, source offer, prominent modification notices}
**Patent posture:** {express grant under §11; broad downstream coverage}
**Modification disclosure:** {if modified, must publish modifications under GPL-3.0}
**Disposition:** **FAIL** — remediation required.
**Remediation options:**
1. Replace with a permissive alternative (e.g., {permissive pkg}).
2. Re-architect to process-separation / network-API boundary; flag as still-debated under FSF's broader view.
3. Relicense project outbound under GPL-3.0 or compatible.
4. Remove the feature.

### #3 — {pkg} v{version} (Apache-2.0)
**Classification:** {permissive — express patent grant + termination}
**Compatibility with outbound {outbound}:** {compatible — note GPL-2.0-only incompatibility if relevant}
**Linking:** {static — no additional obligation}
**Attribution / NOTICE duty:** {if upstream NOTICE file exists, propagate per §4(d)}
**Patent posture:** {express grant; terminates upon licensee patent litigation against the work — §3}
**Modification disclosure:** {note modifications under §4(b)}
**Disposition:** **PASS** — propagate NOTICE; record modifications.

## 3. Cross-Cutting Obligations
- **NOTICE file aggregation:** {list of Apache 2.0 NOTICE entries to aggregate}
- **Source offer for GPL/LGPL/AGPL components:** {written offer location / source URL}
- **AGPL §13 / SSPL §13:** {applicable — modified AGPL source must be offered to network users via {mechanism}}
- **License-text inclusion:** {in /licenses dir of binary / about box / app store listing}

## 4. CLA / DCO and Inbound Flow
**CLA posture:** {Apache iCLA signed by all contributors / no CLA — inbound = outbound}
**DCO posture:** {sign-off required / not enforced}
**Relicensing capacity:** {project can relicense / cannot relicense without contributor consent}
**Patent grant flow:** {Apache 2.0 §3 / GPL-3.0 §11 / none — implied only}

## 5. Non-OSS License Findings (if any)
| Dependency | License | Restriction | Impact |
|---|---|---|---|
| {pkg} | {SSPL-1.0} | §13 service-source obligation | Forbids SaaS use without releasing all service code under SSPL |
| {pkg} | {BSL-1.1} | Change date / additional-use grant | Permitted use case is limited; verify use complies |
| {pkg} | {Elastic-2.0} | Anti-competition / managed-service prohibition | Cannot offer as a managed service competing with vendor |
| {pkg} | {Llama-Community-License} | MAU cap, ethical-use clause | Verify use case complies with field-of-use and conduct restrictions |

## 6. AI Model / Training-Data Findings (if applicable)
| Asset | License | OSI-approved? | Field-of-use | Disposition |
|---|---|---|---|---|
| {model weights} | {OpenRAIL-M} | No | Conduct restrictions | {pass with compliance check} |
| {dataset} | {CC-BY-4.0} | n/a (data) | Attribution required | {pass with attribution} |

## 7. Remediation Plan
| # | Action | Dependency | Owner | Target |
|---|---|---|---|---|
| 1 | Replace GPL pkg with permissive alternative | {pkg} | {team} | {date} |
| 2 | Move {pkg} to process-separated subprocess | {pkg} | {team} | {date} |
| 3 | Aggregate NOTICE file | (cross-cutting) | {team} | {date} |
| 4 | Update LICENSES dir in build artifact | (cross-cutting) | {team} | {date} |

## 8. Final Disposition
**{PASS | PASS-WITH-REMEDIATION | FAIL}**

{Summary statement with the specific blockers and the remediation status. If pass-with-remediation, list each open item.}

## Open Issues / NEEDs
- [NEED: SPDX identifier verification for {N dependencies with ambiguous license text}]
- [NEED: Confirm linking mode (static vs. dynamic) for {pkg}]
- [CITE: FSF guidance on dynamic-linking combined-work treatment — verify pinpoint]
- [NEED: AI model weights license confirmation]
```

---

## Verification

- [ ] Every direct **and transitive** dependency identified — none labeled "unknown."
- [ ] Each license classified by copyleft tier (strong / network / weak / permissive / public-domain dedication / non-OSS).
- [ ] Outbound-vs-inbound compatibility matrix applied to every dependency.
- [ ] Linking analysis (static / dynamic / IPC / network) performed for any (L)GPL-family dependency.
- [ ] AGPL §13 / SSPL §13 network-use triggers evaluated if SaaS or network-accessed.
- [ ] Apache 2.0 §3 / GPL-3.0 §11 patent grant + termination implications surfaced.
- [ ] Apache 2.0 §4(d) NOTICE-file propagation addressed.
- [ ] CLA / DCO posture documented; relicensing capacity stated.
- [ ] Non-OSS (BSL, SSPL, Elastic v2, Llama Community, OpenRAIL) licenses called out separately with their field-of-use restrictions.
- [ ] AI model weights and training-data licenses analyzed separately from code licenses.
- [ ] Remediation plan has owners and target dates for any pass-with-remediation items.
- [ ] No fabricated SPDX identifiers, license text, or upstream URLs.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Trusting SPDX identifier without checking actual LICENSE file | Upstream packages sometimes ship a mismatched LICENSE — read the actual text |
| Treating MIT/BSD as obligation-free | Attribution and license-text inclusion are required; M&A diligence flags missing NOTICE |
| Combining GPL-2.0-only with Apache-2.0 | GPL-2.0's "no further restrictions" conflicts with Apache 2.0 patent-termination; upgrade to GPL-3.0 or replace |
| Assuming SaaS use avoids all copyleft | AGPL §13 and SSPL §13 are network-use copyleft — SaaS triggers source-disclosure |
| Ignoring transitive dependencies | The most common GPL contamination is several levels deep — scan the full tree |
| Treating "source-available" as open source | SSPL, BSL, Elastic v2, Confluent, Llama Community License are not OSI-approved; restrictions can forbid the use case |
| Dynamic linking assumed safe under GPL | FSF treats as combined work; case law is thin; document the integration boundary |
| Process separation assumed to defeat GPL | FSF's view depends on the integration facts (shared memory, intimate data structures, simultaneous lifecycle) — analyze, do not assume |
| Patent grant assumed under MIT/BSD | MIT and BSD provide only implied patent license; Apache 2.0 and GPL-3.0 provide express grants |
| Confusing CLA and DCO | CLA typically grants the project relicensing power; DCO is only an attestation |
| Treating AI model weights as covered by the project's code license | Model weights and training-data licenses are separate — Llama Community, OpenRAIL, BigScience RAIL impose field-of-use restrictions |
| Fabricating SPDX identifiers or upstream URLs | Use `[NEED: ...]` and require verification before sign-off |
| Citing *Jacobsen*, *Vizio*, *Artifex* without verifying | Use `[CITE: ...]`; OSS-license case law is sparse and evolving |
