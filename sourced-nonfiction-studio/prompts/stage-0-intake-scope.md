# Stage 0 — Intake & Scope

**Role in pipeline:** First stage. Sets the parameters every later stage depends on. No sourcing happens yet.

**Objective:** Establish the project's scope: what the author is writing, which field source-standards profile governs it, the citation style, whether living people/organizations are named, the jurisdiction for the legal pass, and the deliverable format.

---

## Inputs
- The author's raw material (braindump, outline, or existing draft) — wrap in `<material>...</material>`.
- Any stated target publication, audience, or length.

## Instructions
1. **Classify the field** → select a profile from `config/source-standards-profiles.yaml` (`general` if none fits). Record the `minimum_anchor_tier` and `recency_caution_years` that will govern Stage 3.
2. **Pick the citation style** from `config/citation-styles.yaml` (default `inline_numbered`; if a target outlet is named, prefer its house style and record the override).
3. **Named-parties flag:** scan for identifiable living people or organizations. If any exist, mark the project **"names real parties → Stage 5 defamation/publicity screen REQUIRED"** and capture the jurisdiction (country + US state). If jurisdiction is unknown, record `US-common-law-default; CONFIRM`.
4. **Deliverable confirmation:** confirm the terminal outputs — fact→source matrix + cited manuscript + risk report (the default triplet), or a subset.
5. **Stakes flag:** note if the content is health/legal/financial/safety (raises the sourcing bar in Stages 3–4).
6. **Write the scope record** (below). This record is passed to every downstream stage.

## Output Format
```
## Scope Record
- Field / profile: [profile id] (min anchor tier: N; recency caution: N yrs)
- Citation style: [style id] [+ outlet override if any]
- Names real living parties? [yes → jurisdiction: ___ / no]
- Stage 5 defamation screen: [REQUIRED / optional]
- Stakes: [general / health / legal / financial / safety]
- Deliverables: [matrix + manuscript + risk report / subset]
- Source material form: [braindump / outline / existing draft]
- Open items to confirm with author: [jurisdiction, target outlet, etc. or none]
```

## Verification
- [ ] A concrete profile is selected (not left blank).
- [ ] Named-parties flag set; jurisdiction captured if any names.
- [ ] Citation style chosen.
- [ ] Deliverables confirmed.
- [ ] Stakes flagged.
