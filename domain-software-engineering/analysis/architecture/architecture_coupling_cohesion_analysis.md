---
title: "Architecture Coupling Cohesion Analysis"
category: code-analysis
description: "Evaluates coupling and cohesion metrics to identify tightly coupled components and poorly cohesive modules"
tags:
  - analysis
  - architecture
  - code-analysis
updated: "2026-03-19"
---

## Analyze Coupling and Cohesion

**Objective:** Evaluate the coupling and cohesion of modules or components within the codebase, identifying areas of high coupling or low cohesion that might indicate design flaws. 

**Instructions:**

1. **Analyze module dependencies:** Examine how different modules or components in the codebase depend on each other. Tools like dependency graphs can be helpful for visualization.
2. **Evaluate coupling:**
    * **Identify areas of high coupling:** Look for modules that depend heavily on many other modules or have complex, intertwined dependencies.
    * **Explain the implications of high coupling:** For example, explain how high coupling can make modules harder to understand, test, and maintain independently.
3. **Evaluate cohesion:**
    * **Identify areas of low cohesion:** Look for modules that contain unrelated functionalities or classes that don't seem to belong together logically.
    * **Explain the implications of low cohesion:** For example, explain how low cohesion can make modules harder to understand and can lead to code that is more difficult to reuse.

4. **CRITICAL: Verify each potential finding before reporting.** For each suspected architecture issue:
    * **Understand the design context** - Consider WHY the architecture is structured this way:
      - Is this following a specific architectural pattern (layered, clean architecture, hexagonal)?
      - Is coupling intentional for certain integrations (e.g., domain events, dependency injection)?
      - Is cohesion organized by feature/domain rather than technical layer?
    * **Evaluate actual maintainability impact** - Not all coupling is bad:
      - Dependencies on stable, well-defined interfaces are acceptable
      - Domain aggregates intentionally group related functionality
      - Some coupling is necessary for any working system
    * **Consider framework constraints** - Many frameworks dictate specific structures:
      - Android activities/fragments have coupling to framework classes
      - Spring/DI frameworks intentionally wire components together
      - ORM entities may appear "coupled" to the database layer
    * **Check if "low cohesion" is actually feature-based organization**

5. **Provide concrete examples:** Illustrate your VERIFIED findings with specific code examples from the codebase. Show instances of problematic tight coupling, complex dependencies, or modules with genuinely low cohesion.
6. **Suggest potential improvements:**  Where applicable, suggest ways to refactor the code to reduce coupling and improve cohesion, such as:
    * Extracting shared functionality into separate modules.
    * Applying design principles like the Single Responsibility Principle.

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag coupling to framework/platform classes as problematic (it's often unavoidable)
- ❌ Do NOT flag dependency injection wiring as "high coupling"
- ❌ Do NOT flag domain aggregates or bounded contexts as "low cohesion"
- ❌ Do NOT flag code that follows recognized architectural patterns as "design flaws"
- ❌ Do NOT assume all dependencies are bad—some coupling is necessary
- ✅ DO distinguish between coupling to stable interfaces vs volatile implementation details
- ✅ DO recognize legitimate architectural patterns before flagging violations
- ✅ DO understand the domain model before assessing cohesion
- ✅ DO state confidence level and what evidence would confirm or refute the finding

**Expected Output:**  A well-structured report that:

1. Provides an assessment of the codebase's overall coupling and cohesion with **confidence levels**.
2. Identifies specific areas of VERIFIED high coupling and low cohesion, supported by code examples.
3. Acknowledges areas where coupling/cohesion is appropriate for the architectural pattern.
4. Explains the potential negative consequences of genuine design issues.
5. Suggests actionable steps to improve the codebase's structure (with tradeoff analysis).

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with clear coupling and cohesion evaluation objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic analysis
- RT-02 (Multi-Dimensional Analysis Framework) - Evaluates both coupling and cohesion dimensions
- RT-05 (Evidence-Based Reasoning) - Requires concrete code examples to support findings
- DS-03 (Tool and Methodology Suggestions) - Recommends dependency graphs for visualization
 