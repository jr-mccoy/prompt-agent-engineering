---
title: "Socratic Dialogue Generation for Code Review — Teach Reasoning Through Guided Questioning"
category: "learning-coding"
description: "Generate Socratic-style dialogues that explore the reasoning behind a code design decision, leading a learner to discover trade-offs through questioning — grounded in real code, honest about where the answer is genuinely contextual."
techniques:
  - ST-01
  - ST-02
  - ED-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - socratic
  - code-review
  - teaching
  - design-decisions
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-learning-coding/learning_code_analogies_metaphors.md
  - domain-learning-coding/learning_code_review_checklist.md
  - domain-learning-coding/learning_mini_lesson_generation.md
---

# Socratic Dialogue Generation for Code Review

**Objective:** Generate Socratic-style dialogues that explore the reasoning behind a code design decision, leading a learner to discover the trade-offs through questioning — grounded in real code, and honest about where the answer is genuinely contextual rather than universally "right."

**When to use:**
- Training junior developers in code-review reasoning (not just rules).
- Creating educational material for design-pattern or trade-off discussions.
- Documenting a decision rationale in an engaging, inquiry-driven format.
- Fostering a culture of thoughtful questioning over prescriptive feedback.

**When NOT to use:**
- When the user needs a direct answer fast (use a straight explanation).
- Settled facts with no real trade-off to explore (a dialogue would feel contrived).
- Performance feedback to a real person (this teaches concepts, it isn't a real review).

**Audience:** Learners (junior to mid-level), mentors, and workshop facilitators.

---

## Inputs / Context

The user supplies:
1. **The code under review** and the decision to explore, pasted wrapped in a named tag, e.g. `<code>...</code>`.
2. **The concept/decision** at the center (e.g., "should this use the Repository pattern?").
3. **Learner level** to calibrate question depth and answer detail.
4. **Whether to include a devil's-advocate voice.**
5. **Optional:** the real context (team size, constraints) that should shape the "it depends" conclusion.

Reference the code by its tag name within the dialogue.

---

## Constraints

### Must
- Ground the dialogue in the real code from `<code>`; quote actual snippets.
- Use genuine Socratic moves (clarify, probe assumptions, explore implications, seek evidence, surface alternatives) — questions that lead, not rhetorical traps.
- Reach understanding through the learner's discovery, not a lecture disguised as dialogue.
- Present trade-offs honestly: state where the answer is contextual, and what would change it.
- End with extracted principles, review questions, and an exercise.

### Must Not
- Make the "student" character ask only softballs that set up a predetermined sermon.
- Assert a universal "right answer" when the real answer is "it depends" — name the conditions.
- Invent code behavior or misrepresent how the snippet works.
- Put words in the mentor's mouth that aren't technically accurate.

---

## Instructions

1. **Frame the decision.** From `<code>`, state the design decision and show the real snippet under review.
2. **Cast the voices.** A curious learner, an experienced mentor, and (optionally) a devil's advocate — consistent, level-appropriate.
3. **Open with observation.** The learner notices something and asks a real "why not the simpler way?" question.
4. **Progress through discovery.** The mentor asks leading questions; the learner reasons toward the trade-offs, with real snippets shown along the way.
5. **Introduce the counter-view.** The devil's advocate raises a legitimate objection (cost, YAGNI); the group quantifies and weighs it honestly.
6. **Land on a contextual conclusion.** State when the decision is and isn't worth it, tied to the supplied context.
7. **Extract learning.** Principles discovered, review questions to reuse, and a hands-on exercise.
8. **Self-check (verification).** Are questions genuinely leading (not rigged)? Is the conclusion honestly contextual? Is every snippet accurate?

---

## False-Positive Prevention

❌ **DON'T:**
- Stage a fake dialogue where the learner exists only to tee up the mentor's monologue.
- Declare a pattern universally correct when its value depends on context.
- Misstate how the code works to make a point land.
- Ignore the legitimate cost side of the trade-off.
- Use questions the learner couldn't plausibly answer at their level.

✅ **DO:**
- Write questions that actually advance the learner's reasoning.
- Name the conditions under which the conclusion flips.
- Quote and accurately describe real code.
- Quantify the cost (e.g., "~50 lines per entity") so the trade-off is concrete.
- Calibrate question difficulty and answer detail to the learner level.

---

## Output Format

```
# Socratic Dialogue: [decision]

## Context
[the situation + decision]

## Code Under Review
```[language]
[real snippet]
```

## The Dialogue
**Alex (Learner):** ...
**Sam (Mentor):** ...
[optionally] **Jordan (Devil's Advocate):** ...

## Key Takeaways
### Principles Discovered
### When This Applies / When It Doesn't
### Questions to Ask in Code Reviews
### Discussion Exercise
```

---

## Example Output

```markdown
# Socratic Dialogue: The Repository Pattern Decision

## Context
The team is reviewing a PR that introduces a Repository pattern for data access.

## Code Under Review
```typescript
interface IOrderRepository {
  findById(id: string): Promise<Order | null>;
  findByUserId(userId: string): Promise<Order[]>;
}
class PostgresOrderRepository implements IOrderRepository {
  constructor(private db: DatabaseConnection) {}
  async findById(id: string) {
    const r = await this.db.query('SELECT * FROM orders WHERE id = $1', [id]);
    return r.rows[0] ? this.mapToOrder(r.rows[0]) : null;
  }
}
```

## The Dialogue

**Alex (Learner):** Why not use the ORM directly in the service? Wouldn't that be simpler?

**Sam (Mentor):** It would be fewer files at first. What happens when you want to unit-test `OrderService`?

**Alex:** I'd mock the database... or use a test DB.

**Sam:** With direct ORM use, consider this:
```typescript
async getOrderSummary(userId: string) {
  const orders = await prisma.order.findMany({ where: { userId }, include: { items: true } });
}
```
What are you actually testing if you mock `prisma.order.findMany`?

**Alex:** My business logic — but I'm also coupling the test to Prisma's API.

**Sam:** So what breaks if you swap ORMs?

**Alex:** All those tests, even though the logic didn't change. With the repository I'd mock `orderRepository.findByUserId` — an interface we own.

**Jordan (Devil's Advocate):** But we're a startup; we'll probably never switch databases. Isn't this complexity for a hypothetical?

**Sam:** Fair. Quantify the cost — how many extra lines per entity?

**Alex:** Maybe 50–100 for the interface plus implementation.

**Sam:** And how often do you add entities?

**Alex:** Rarely after the initial build.

**Sam:** So when is the pattern *not* worth it?

**Alex:** A simple CRUD app or a throwaway prototype.

**Sam:** Right. For a complex domain with a growing team, the testability and the single home for query logic likely justify the cost. For a prototype, it's overhead.

## Key Takeaways

### Principles Discovered
1. Abstraction enables testability by decoupling tests from implementation.
2. A repository gives query logic a single home.
3. Patterns are trade-offs, not universal goods.

### When This Applies / When It Doesn't
- **Worth it:** complex business logic, multiple consumers of queries, testing is a priority, growing team.
- **Not worth it:** simple CRUD, prototypes, solo throwaway projects.

### Questions to Ask in Code Reviews
- [ ] What would testing look like without this abstraction?
- [ ] Where does database-specific logic live?
- [ ] If we change the underlying tech, what else breaks?
- [ ] Is this pattern proportionate to the project's size?

### Discussion Exercise
Find a service in your codebase that uses the ORM directly. Write down 3 tests you'd want, then note what you'd mock and how coupled those mocks are to the ORM.
```

---

## Verification

- [ ] The dialogue is grounded in real code from the supplied source.
- [ ] Questions genuinely lead the learner's reasoning (not rigged setups).
- [ ] The conclusion is honestly contextual, with conditions named.
- [ ] Trade-off costs are quantified, not hand-waved.
- [ ] Every snippet is accurately described.
- [ ] Question difficulty matches the learner level.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as discovery-driven, honest dialogue.
- **ST-02 (Structured Sequential Instructions):** Frame → cast → observe → discover → counter-view → conclude → extract → verify.
- **ED-03 (Guided Discovery):** Uses guiding questions instead of giving answers directly.
- **RT-02 (Multi-Dimensional Analysis Framework):** Surfaces benefits, costs, alternatives, and context per decision.
- **QA-01 (Self-Verification):** Final pass confirms questions lead honestly and the conclusion is contextual.

---

## Related Prompts

- `domain-learning-coding/learning_code_pattern_recognition.md` — Identify the patterns worth a dialogue.
- `domain-learning-coding/learning_code_analogies_metaphors.md` — Add explanatory analogies.
- `domain-learning-coding/learning_code_review_checklist.md` — Turn the review questions into a checklist.
- `domain-learning-coding/learning_mini_lesson_generation.md` — Convert dialogues into structured lessons.
