---
title: "Codebase Stakeholder Persona Generation"
category: business-strategy/analysis
description: "Infer stakeholder personas from the roles, permissions, and interactions implemented in a codebase, mapping each persona's goals and pain points to specific code functionality and surfacing gaps where needs go unmet."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - business-analysis
  - personas
  - stakeholder-analysis
  - codebase-analysis
  - user-roles
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/analysis/business_impact_analysis.md
  - domain-business-strategy/analysis/customer_journey_map_analysis.md
  - domain-business-strategy/analysis/tech_adoption_lifecycle_analysis.md
---

# Codebase Stakeholder Persona Generation

**Objective:** Infer the distinct stakeholder personas a system serves by reading the roles, permissions, and interaction surfaces present in the codebase, then map each persona's goals and pain points to specific functionality and flag where needs go unmet.

**When to use:**
- You inherited a system and need to understand who it is actually built for.
- Product/UX wants persona hypotheses grounded in what the code supports, as a starting point for real research.
- Planning access-control, navigation, or feature work that depends on knowing the user types.
- Onboarding a team and needing a shared model of the system's audiences.

**When NOT to use:**
- You need validated personas — these are code-derived hypotheses, not a substitute for user interviews.
- The codebase has no role differentiation or user-facing surface to infer from.
- You already have research-backed personas; this would only restate guesses.

**Audience:** Product managers, UX researchers, engineering managers, and architects.

---

## Inputs / Context

The user should supply (or the analysis should flag what is missing):

1. **The codebase** (or an inventory of roles, permissions, routes, and key flows).
2. **Product context:** what the product does and any known user types.
3. **Scope:** all stakeholders vs. a specific area (e.g., admin-side only).
4. **Known research** if any (existing personas, interviews) — to anchor inference vs. invention.
5. **Decision the personas feed:** access design, navigation, roadmap, onboarding.

---

## Constraints

### Must
- Derive each persona from **observable code evidence**: role enums, permission checks, route guards, role-specific UI, distinct flows. Cite the file/module.
- Distinguish **fact** (an "admin" role exists with these gated routes) from **inference** (this persona is *probably* time-pressed).
- For each persona, cover **role, goals/motivations, pain points, and key interactions**, and map each to specific code.
- **Prioritize** personas by how central they are to the system (primary vs. secondary vs. edge).
- Flag **gaps**: needs implied by a role but not supported in code, and label them as hypotheses to validate.

### Must Not
- Invent demographic detail, names of real people, or motivations unsupported by code or supplied research.
- Present an inferred persona trait as a confirmed user fact.
- Treat one role enum as definitive proof of a clean persona boundary if the code blurs it.
- Pad with generic persona boilerplate ("tech-savvy millennial") not grounded in evidence.

---

## Instructions

1. **Identify roles and interaction surfaces.** Scan for role/permission models, auth guards, role-conditional UI, and distinct entry points. Cite files.
2. **Cluster into candidate personas.** Group roles and interaction patterns into distinct stakeholder types. Note where the code supports a clean boundary vs. where it's ambiguous.
3. **Build each persona.** For each: role and context, likely goals/motivations, pain points (often visible as friction or missing capability in code), and key interactions with the system, each tied to a file/flow.
4. **Label evidence vs. inference.** Mark which persona attributes come from code and which are domain inference to be validated.
5. **Map functionality to needs.** Show which features serve each persona and how well.
6. **Identify gaps and prioritize.** Note unmet needs and rank personas by centrality; flag gaps as validation candidates.
7. **Self-check (verification step).** Re-read: any invented demographic or named person? Any inference dressed as fact? Are gaps and validation steps stated?

---

## False-Positive Prevention

❌ **DON'T:**
- Invent a real person's name, age, or biography for a persona.
- State "this persona values speed above all" as fact when it's a guess from code.
- Assume a role enum maps cleanly to a real-world persona without checking how it's used.
- Produce generic persona templates untethered to the actual codebase.
- Present code-derived hypotheses as research-validated personas.

✅ **DO:**
- Label each persona attribute **evidence-based** (from code) or **hypothesis** (inference).
- Cite the specific role/permission/route/flow behind each persona.
- Use clearly-illustrative placeholder labels (e.g., "Admin Alex (placeholder)") rather than real names.
- Acknowledge needs the code can't reveal and name what research would confirm.
- Suggest validation steps (interview 3 admins, review support tickets) before betting on a persona.

---

## Output Format

```
# Stakeholder Personas: [Product / Codebase]

## Context & Evidence Basis
- Product: [...]
- Roles found in code (file/module): [...]
- Research available: [list, or "none — personas are code-derived hypotheses"]

## Personas (most central first)
### [Persona label] — [role]  (Primary / Secondary / Edge)
- Evidence (file/module): [role enum, gated routes, role-specific UI]
- Goals & motivations: [...] (evidence / hypothesis)
- Pain points: [...] (evidence / hypothesis)
- Key interactions: [features/flows, with files]
- Needs met / unmet: [...]

## Persona–Functionality Map
| Persona | Served by (features/files) | Need coverage | Basis |
|---------|----------------------------|---------------|-------|
| ...     | ...                        | Full/Partial/None | evidence / hypothesis |

## Gaps & Validation
- [Unmet need or ambiguous boundary] → how to validate

## Self-Check
- Invented details / real names: [none / list]
- Inference labeled: [yes/no]
```

---

## Example Output

```
# Stakeholder Personas: ExampleCo SaaS Platform (placeholder)

## Context & Evidence Basis
- Product: team workflow SaaS (placeholder)
- Roles found in code: src/auth/roles.ts → ['owner', 'admin', 'member', 'viewer']
- Research available: none supplied — personas below are code-derived hypotheses

## Personas (most central first)
### Admin Alex (placeholder) — Workspace Admin  (Primary)
- Evidence: roles.ts 'admin'; gated routes in src/pages/admin/* behind requireRole('admin'); billing + member-management UI
- Goals & motivations: keep the team set up and paid (evidence: controls billing + seats); minimize support overhead (hypothesis)
- Pain points: member management is split across two screens (evidence: separate routes /admin/members and /admin/invites); likely friction (hypothesis)
- Key interactions: billing (src/billing/*), member CRUD (src/pages/admin/members), audit export (src/compliance/AuditExport.ts)
- Needs met / unmet: billing + members met; bulk member import NOT present (gap)

### Member Morgan (placeholder) — Individual Contributor  (Primary)
- Evidence: roles.ts 'member'; full access to project/workspace flows, no admin routes
- Goals & motivations: do daily work efficiently (evidence: shortcuts in src/ui/shortcuts.ts)
- Pain points: cannot self-serve role changes (evidence: no member-facing settings for role) — must ask Admin (hypothesis: adds friction)
- Key interactions: projects, tasks, collaboration features
- Needs met / unmet: core work met; self-service limited (gap)

### Viewer Val (placeholder) — Read-Only Stakeholder  (Edge)
- Evidence: roles.ts 'viewer'; UI hides all mutation controls via canEdit checks
- Goals & motivations: monitor without changing (evidence: read-only enforcement)
- Pain points: no export for offline review (evidence: export gated to admin) (hypothesis: blocks reporting)
- Needs met / unmet: read access met; export unmet (gap)

## Persona–Functionality Map
| Persona | Served by (features/files) | Need coverage | Basis |
|---------|----------------------------|---------------|-------|
| Admin Alex | billing, member mgmt, audit export | Partial (no bulk import) | evidence |
| Member Morgan | projects, tasks, shortcuts | Partial (no self-service role) | evidence + hypothesis |
| Viewer Val | read-only views | Partial (no export) | evidence + hypothesis |

## Gaps & Validation
- Bulk member import for Admin Alex → confirm demand via support tickets / sales notes.
- Viewer export need → validate with 2–3 read-only stakeholders before building.

## Self-Check
- Invented details / real names: none (placeholder labels only).
- Inference labeled: yes — each attribute marks evidence vs. hypothesis.
```

---

## Verification

- [ ] Every persona ties to observable role/permission/flow evidence (file/module cited).
- [ ] Each persona attribute labeled evidence-based or hypothesis.
- [ ] No invented demographics or real people; placeholder labels used.
- [ ] Each persona covers role, goals, pain points, and interactions.
- [ ] Personas prioritized by centrality.
- [ ] Gaps surfaced with validation steps.
- [ ] What research would confirm the hypotheses is stated.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as inferring code-grounded persona hypotheses, not validated personas.
- **RT-02 (Multi-Dimensional Analysis Framework):** Characterizes each persona across role, goals, pain points, and interactions.
- **DS-02 (Evidence-Based Decision Making):** Requires every persona attribute to trace to code evidence or supplied research, labeling inference.
- **DS-06 (Prioritization and Severity Guidance):** Ranks personas by centrality (primary/secondary/edge).
- **QA-01 (Self-Critique Triggers):** Final self-check audits for invented details and unlabeled inference.

---

## Related Prompts

- `domain-business-strategy/analysis/business_impact_analysis.md` — Translate features into prioritized business value for these stakeholders.
- `domain-business-strategy/analysis/customer_journey_map_analysis.md` — Map how these personas move through the product.
- `domain-business-strategy/analysis/tech_adoption_lifecycle_analysis.md` — Position the product and its audiences in the adoption lifecycle.
