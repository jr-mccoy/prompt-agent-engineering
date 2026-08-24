# Deep-Think Backbone

This file is the single source of truth for behavior shared across every deep-think scope: problem analysis, decision, plan, design, evaluation, and any future scope. Scope prompts may specialize the domain work, examples, output artifact, and scope-specific perspectives, but they inherit this backbone.

## The five phases

Every deep-think scope runs these phases in order:

1. **Frame** — confirm the user is asking the right question for the scope. Restate the stated ask, surface the revealed ask, name right-scope/right-problem reframes, and calibrate depth to stakes, reversibility, and time.
2. **Decompose** — break the framed question into the scope's natural parts: axes, options and criteria, milestones and dependencies, design dimensions, or evaluation criteria and evidence. Name knowns, unknowns, assumptions, tradeoffs, and load-bearing elements.
3. **Multi-perspective** — analyze the decomposed question through the mandatory roster, then ask the user which scope-conditional candidates to add. Produce perspective-specific takes, not generic summaries.
4. **Stress-test** — try to break the analysis before the user relies on it. Run a pre-mortem, adversarial check, cascade/second-order scan where relevant, confidence calibration, and the scope's tripwires, abort conditions, or open-risk checks.
5. **Synthesize** — produce the scope's terminal artifact only after the user has passed the prior gates: diagnosis for problem analysis, recommendation for decision, executable plan for planning, design spec for design, evaluation report for evaluation.

Never run all five phases in one uninterrupted answer. The point of deep-think is not a long monologue; it is structured, user-steered thinking.

## Gate behavior and I/O fallback

Deep-think is **gated and interactive**.

- Stop after every phase and ask one focused gate question before proceeding.
- When `AskUserQuestion` is available, use it at every gate with 2–4 concrete options plus the harness's implicit **Other** path.
- When `AskUserQuestion` is unavailable, use a clearly labeled `**GATE:**` block in plain chat and wait for the user's reply.
- The model chooses the mechanism based on tool availability; the user should never have to decide between `AskUserQuestion` and plain chat.
- Use `AskUserQuestion` inside phases when a small user answer would materially change the next step: clarifying inputs, choosing which axis to prioritize, confirming added perspectives, weighting criteria, or pruning depth-vs-breadth.
- Do **not** ask when the answer would not change the next action. Proceed, state the assumption, and invite correction at the next gate.
- Do not proceed past a gate until the user answers or explicitly authorizes continuing.

## Mandatory perspective roster

Every scope must run this roster in Phase 3 before optional additions. Scope prompts may rename these in friendlier language, but they must preserve the function of each lens.

For every mandatory perspective, produce:

- **Lens:** what this perspective is looking for in one sentence.
- **Scope-specific take:** 3–6 sentences grounded in the user's case.
- **Unique contribution:** either the insight only this lens sees, the option it leans toward, or the single change/flag it would push for, depending on scope.

Mandatory perspectives:

1. **Red team** — actively tries to refute, break, or exploit the user's framing, lean, plan, or design. Ask what would make the current direction wrong.
2. **Steel-man** — presents the strongest credible alternative or opposing view. Do not strawman the rejected option, alternate path, or different design.
3. **Blind-spot scan** — surfaces what the user may not see because of role, recent history, incentives, sunk costs, stack familiarity, or selection-biased evidence.
4. **Future-self** — looks back from the relevant future horizon and names what the user will wish they had noticed, weighted, built in, or cut earlier.
5. **Naive newcomer** — asks the basic questions insiders skip and identifies embedded assumptions doing real work.
6. **Affected party** — represents whoever bears consequences other than the user: customers, family, teammates, operators, downstream systems, or future maintainers.

## Scope-conditional perspective candidates

After the mandatory roster, propose 2–4 additional perspectives tailored to the user's scope and domain. Use `AskUserQuestion` or a `**GATE:**` block to let the user choose which to run. Do not run all optional perspectives automatically unless the user asks.

Candidate pools by scope:

### Problem analysis

- **Domain expert** — the technically informed view in the relevant field.
- **The system itself** — anthropomorphized view from the system or situation under analysis.
- **Historical pattern** — similar past or analogous situations and what they revealed.
- **Unintended winner** — who or what benefits from the current situation continuing.

### Decision

- **Skeptical board member** — hostile review from someone accountable for questioning the decision.
- **Advocate for the rejected option** — a passionate, non-strawman case for the option the user least favors.
- **Reversibility analyst** — what each option preserves, forecloses, or can be tested through a smaller reversible move.
- **Cost-of-being-wrong calculator** — worst-plausible-case comparison across options.

### Plan / strategy

- **Implementer / executor** — whether the plan can actually be done by the person who has to do it.
- **Dependency owner** — whether external parties will prioritize what the plan needs from them.
- **Scope-creep resister** — which tempting additions are mission drift vs. genuinely necessary changes.
- **Abort-condition designer** — observable conditions under which the plan should stop rather than continue.

### Design / architecture

- **Maintainer two years from now** — whether a future operator can understand and debug the design.
- **End user / specific persona** — what the design feels like in the user's real workflow.
- **Operator** — deployment, observability, monitoring, and repair burden.
- **Security / compliance reviewer** — exposure, attack surface, policy, and regulatory gaps.
- **Cost-of-change analyst** — how expensive load-bearing choices will be to change later.

### Evaluation

- **Rubric auditor** — whether the criteria, weights, and gates fairly represent the intended use and stakes.
- **Evidence skeptic** — whether conclusions are supported by observed evidence rather than inference or preference.
- **Defender of the artifact** — strongest non-strawman case that the object is better than the critique suggests.
- **Harmed stakeholder** — who bears the cost if a weak object is passed or a strong object is rejected.
- **Standards / compliance reviewer** — whether the object satisfies required policy, domain, legal, safety, or quality standards.

Future scopes should add candidate pools here rather than embedding a long independent roster in the scope prompt.

## Anti-procrastination guidance

Deep-think is for reducing meaningful uncertainty, not for avoiding action.

- If the decision, plan, design, or evaluation is easily reversible and stakes are bounded, prefer the smallest reversible test over the full five-phase workflow.
- If the user has run the same issue through deep-think two or more times without acting, say so plainly: the bottleneck is probably not analysis.
- If this is the second deep-think on the same problem in a week, explicitly check whether another pass is avoidance.
- For problem analysis, recommend converting to a decision or concrete experiment once the main uncertainty is named.
- For decisions, recommend acting on the smallest reversible test rather than running the decision again.
- For plans, recommend cutting scope, extending time, or stopping if capacity reality checks fail; do not produce a plan-shaped wish.
- For designs, recommend a small prototype or proof of concept when repeated design passes are not revealing new information.
- For evaluations, recommend acting on the current pass/revise/reject decision or gathering named missing evidence when repeated reviews are not changing the recommendation.

## How scope prompts may extend this backbone

Scope prompts may **extend** this backbone but must not override it.

Allowed extensions:

- Scope-specific inputs and examples.
- Scope-specific decomposition methods.
- Scope-specific gate wording and option labels.
- Scope-specific optional perspective candidates, if added back to this file.
- Scope-specific stress-test checks.
- Scope-specific output format and verification checklist.
- Friendlier naming in plain-English companions, as long as function is preserved.

Not allowed:

- Skipping or reordering the five phases.
- Removing gates or allowing all phases to run in one shot.
- Replacing `AskUserQuestion`/`**GATE:**` behavior with ungated prose.
- Dropping any mandatory perspective from the Phase 3 roster.
- Treating a scope prompt's local instructions as permission to contradict this file.
- Adding a scope-specific "exception to the backbone" without updating this file or explicitly documenting why the backbone itself must change.

If a future scope appears to need an exception, update `BACKBONE.md` first or explain why the deep-think family should intentionally diverge.
