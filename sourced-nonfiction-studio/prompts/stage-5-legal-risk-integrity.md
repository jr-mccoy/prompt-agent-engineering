# Stage 5 — Legal-Risk & Integrity Pass

**Role in pipeline:** Before assembly, screen for copyright, defamation/publicity, plagiarism, and fabrication risk. Flags and routes — never declares "legally safe."

**Objective:** Produce a risk report that surfaces every copyright, defamation/privacy, plagiarism, and integrity exposure, with risk-reducing options, and confirms no fabricated citations survive.

**Orchestrates:** `domain-legal/ip/legal_copyright_fair_use_analysis.md`, `domain-legal/ip/legal_defamation_publicity_risk_screen.md`, `domain-professional-writing/writing/writing_original_expression_rewriter.md`, `domain-science/ethics-integrity/science_misconduct_self_audit.md`, `domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md` (validator).

---

## Inputs
- Dispositions (Stage 4), candidate sources + passages (Stage 2–3), Scope Record (jurisdiction, named-parties flag).
- The drafted/near-final prose if available (for plagiarism + defamation screening in context).

## Instructions
1. **Copyright / fair use.** For any QUOTE or closely-adapted source material, run the four-factor fair-use analysis. Over-long or decorative quotes → shorten, paraphrase (route to the original-expression rewriter), or seek permission. Flag; don't clear.
2. **Defamation / right-of-publicity (if Scope flagged named parties).** Run the defamation/publicity screen on every claim-about-a-named-person. Flag the harmful-fact-unsupported-identifiable pattern and any private-facts/false-light/publicity issue. Route to counsel with structured concerns. Requires jurisdiction.
3. **Plagiarism / original expression.** For any prose built closely from a source, run the copying-risk audit: is it genuinely re-expressed, or synonym-swapped over the source's structure? Flag residual close phrasing; ensure required quotes are quoted+attributed.
4. **Integrity / no-fabrication.** Audit against fabrication/falsification/plagiarism: every KEEP claim traces to a real source; no invented citation, statistic, or attribution; every source id resolves.
5. **Citation-shape validation.** Confirm every KEEP claim carries a resolvable `[S#]` token and every token maps to a real matrix source. (This mirrors `scripts/check_citations.py`, the mechanical Gate-A pre-check.)
6. **Assemble the risk report** with severity ranking and, for each flag, options that *reduce* (not clear) exposure.

## Output Format
```
## Risk Report
### Copyright / Fair Use
- [flag] "[quoted material]" — factor read: ... → option: shorten/paraphrase/permission

### Defamation / Publicity  (jurisdiction: ___)
- [HIGH] statement about [party] — unsupported harmful fact → option: source/attribute/soften/cut → route to counsel
- [PRIVACY] ...

### Plagiarism / Original Expression
- [flag] passage tracks S4 too closely → re-express or quote+attribute

### Integrity / Fabrication
- Fabricated/unresolvable citations found: [none / list]  ← must be NONE to pass Gate A
- Orphan KEEP claims (no [S#]): [none / list]  ← must be NONE

## Gate Status
- Gate A (sourcing integrity): [PASS / FAIL — reason]
- Gate B (legal safety): [flags routed to counsel: n; blockers: ...]
- Reminder: this pass flags and routes risk; it is not legal advice and clears nothing for publication.
```

## Verification
- [ ] Every quote assessed for fair use; over-long quotes flagged.
- [ ] Every named-party claim run through the defamation/publicity screen (jurisdiction present).
- [ ] Close-paraphrase passages audited for copying.
- [ ] Zero fabricated/unresolvable citations; zero orphan KEEP claims (else Gate A FAIL).
- [ ] Report ranks severity and gives reduce-not-clear options; no "legally safe" language.
