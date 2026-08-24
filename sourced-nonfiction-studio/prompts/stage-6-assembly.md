# Stage 6 — Assembly

**Role in pipeline:** Terminal stage. Produces the three deliverables from everything upstream. Only runs after Gate A passes.

**Objective:** Emit (1) the fact→source matrix (audit trail), (2) the publish-ready cited manuscript, and (3) the risk report, in the chosen citation style.

**Orchestrates:** `domain-research-academic/research_secondary_source_synthesis.md` (drafting engine), `domain-education-teaching/learner-writing/learnwrite_citation_helper.md` (style formatting), `config/citation-styles.yaml`.

**Precondition:** Gate A (Stage 5) = PASS. If FAIL, do not assemble — return to Stage 4 for the offending claims.

---

## Inputs
- Dispositions + rewrites (Stage 4), Claim Verdicts + sources (Stage 3), Risk Report (Stage 5), Scope Record (citation style).

## Instructions
1. **Build the fact→source matrix.** One row per claim: claim text, type, disposition, verdict, anchor source `[S#]` with full reference, licensed certainty, and any REFRAMED/UNVERIFIED marker. This is the audit trail — it must let anyone trace every kept claim to a real source.
2. **Draft the manuscript.**
   - KEEP claims → stated as fact with inline citation in the chosen style.
   - SOFTEN → the calibrated wording + citation.
   - REFRAME → the explicitly attributive ("In my experience…") wording, with the `[author's professional judgment]` marker where helpful — no citation, because it isn't presented as external fact.
   - QUOTE → quoted + attributed (fair-use-cleared length from Stage 5).
   - CUT claims → absent.
   - Preserve the author's voice; use the original-expression discipline so sourced facts are in the author's own words.
3. **Render citations** per `config/citation-styles.yaml`: convert internal `[S#]` tokens to the chosen style's inline form + build the reference list.
4. **Attach the risk report** and a short **disclosure note**: which parts are the author's judgment vs sourced fact, that sourcing was AI-assisted and requires human verification, and any UNVERIFIED items that remain.
5. **Surface the residue** prominently for the author: every REFRAMED, CUT, and UNVERIFIED item, plus every counsel-routed risk flag.

## Output Format
```
## 1. Fact→Source Matrix
| # | Claim | Type | Disposition | Verdict | Source [S#] | Reference | Certainty | Marker |

## 2. Cited Manuscript
[Publish-ready prose with inline citations in the chosen style.]

### References
[Reference list in the chosen style.]

## 3. Risk Report
[From Stage 5, with counsel-routed flags.]

## 4. Author Disclosure & Residue
- Sourced-fact vs author-judgment split: ...
- Reframed (judgment, not fact): [...]
- Cut: [...]
- Still UNVERIFIED (if any kept with [UNVERIFIED] marker): [...]
- Counsel-review items: [...]
- Note: sourcing was AI-assisted; verify all citations against the originals before publishing.
```

## Verification
- [ ] Gate A confirmed PASS before assembly.
- [ ] Every KEEP claim in the manuscript has a resolvable citation in the matrix.
- [ ] REFRAME claims are attributive and uncited (not dressed as fact).
- [ ] Citation style rendered consistently; reference list complete and resolvable.
- [ ] All three deliverables present + disclosure/residue surfaced.
