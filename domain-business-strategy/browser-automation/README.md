# Browser / Workflow Automation Readiness

Prompts for the operational work that turns browser activity into scheduled automation safely: a weekly audit to find what's worth automating, a recording blueprint so the recording itself produces a robust workflow, a design for multi-tab intelligence-gathering operations, and a safety check that gates activation.

**Audience:** Ops lead, automation engineer, or individual contributor evaluating and building browser-based automation. Not an enterprise-platform selection cluster — this is the per-user, per-team execution layer.

**Core idea:** The automation is usually not the bottleneck. The bottleneck is (1) picking the right thing to automate, (2) designing before recording, (3) gating launch on real safety review, and (4) keeping the fleet from rotting. These four prompts are the operating cycle.

---

## Prompts

| Prompt | One-liner |
|--------|-----------|
| [browserauto_weekly_audit.md](browserauto_weekly_audit.md) | A 15–30 minute weekly scan of the week's activity that picks one candidate to prototype and one automation to retire. |
| [browserauto_recording_blueprint.md](browserauto_recording_blueprint.md) | Design the workflow — inputs, branches, error handling, dry-run, success criteria — before opening a recorder. |
| [browserauto_multi_tab_intel.md](browserauto_multi_tab_intel.md) | Design a multi-tab intelligence-gathering operation with source tiers, extraction schema, citation, and rot detection. |
| [browserauto_safety_check.md](browserauto_safety_check.md) | Pre-flight go/no-go: blast radius, authority, credentials, ToS, rollback, failure detection. |

---

## Operating cycle

```
Weekly audit → Blueprint → (record) → Dry-runs → Safety check → Schedule → Weekly audit ...
```

- **Weekly audit** surfaces this week's candidate.
- **Blueprint** is the design artifact; the recording follows from it.
- **Safety check** is a hard gate, not a soft review — holds block launch.
- The next **weekly audit** picks up whether the live automation is still worth keeping, producing retirement candidates when appropriate.

Skipping the blueprint in favor of "just record and see" is how brittle automations get scheduled. Skipping the safety check is how incidents happen. Skipping the audit is how the automation fleet bloats into zombies.

---

## When to use `browserauto_multi_tab_intel.md`

Only for recurring intelligence-gathering operations (5+ sources, cadenced, feeding a briefing consumer). For single-source scheduled extraction, use the blueprint prompt directly. For one-off research, use `domain-business-strategy/research/` prompts instead.

---

## Relationship to adjacent clusters

- **[chief-of-staff/](../chief-of-staff/)** — `cos_authority_boundaries.md` is required reading when the automation acts on the user's behalf under authority.
- **[automation/](../../domain-productivity/automation/)** — broader automation patterns beyond the browser (data sync, lead routing, daily check-ins).
- **[ai-patterns/](../../domain-engineering-workflows/ai-patterns/)** — `ai_pattern_agent_code_footgun_detector.md` applies when the automation is AI-agent-driven rather than recorded.
- **[research/](../research/)** — for one-off or less structured research, prefer the research prompts; this cluster is for cadenced operations with a consumer.
