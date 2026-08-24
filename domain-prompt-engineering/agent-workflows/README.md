# Agent Workflows

Prompt-engineering patterns for autonomous and semi-autonomous agents: termination, planning, self-correction, state, delegation, observability, idempotency, authority, and human-in-loop.

| File | Description |
|------|-------------|
| `agent_loop_termination_designer.md` | Falsifiable termination conditions across categories |
| `agent_planner_worker_judge_prompts.md` | Three-prompt loop with revision cap |
| `agent_self_correction_loop.md` | Detect → diagnose → repair around an agent step |
| `agent_state_summary_for_compaction.md` | Resume-ready state summary at compaction time |
| `agent_subagent_brief_generator.md` | Self-contained delegation brief |
| `agent_progress_report_format.md` | Fixed-schema progress reports at intervals |
| `agent_authority_boundary_prompt.md` | Can Do / Ask First / Never matrix |
| `agent_observability_prompt_for_traces.md` | Structured event emission for telemetry |
| `agent_idempotency_prompt.md` | Pre-check / act / record pattern with deterministic keys |
| `agent_human_in_loop_handoff.md` | Pause / request / timeout / resume protocol |
