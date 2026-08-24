---
title: "Architecture Layer Identification"
category: code-analysis
description: "Identifies and analyzes architectural layers evaluating separation of concerns and dependency flow between layers"
tags:
  - architecture
  - code-analysis
updated: "2026-03-19"
---

**Objective:** Analyze the codebase and identify different architectural layers (e.g., presentation, business logic, data access), highlighting inconsistencies or deviations from common architectural patterns.

**Instructions:**

1. **Analyze the codebase structure:** Examine the directory structure, modules, and classes to understand how code is organized.
2. **Identify distinct layers:** Look for code sections responsible for:
    * **Presentation:** Handling user interface, user input, and displaying information (e.g., UI components, views, controllers).
    * **Business Logic:** Implementing business rules, workflows, and data processing (e.g., services, business objects, use case classes).
    * **Data Access:** Interacting with databases or external data sources (e.g., repositories, data access objects, API clients).
3. **Document each identified layer:**
    * Name the layer (e.g., "Presentation Layer", "Domain Layer", "Persistence Layer").
    * Describe its purpose and responsibilities.
    * List the key components or modules belonging to that layer.

4. **CRITICAL: Verify architectural assessments before flagging issues.** For each suspected violation:
    * **Understand the intended architecture** - Consider what pattern the codebase is following:
      - Is this a traditional layered architecture, or something else (vertical slices, feature-based)?
      - Does the project use Clean Architecture, Hexagonal, or other patterns with different boundaries?
      - Are apparent "violations" actually following a different valid pattern?
    * **Check for intentional design decisions** - Some "violations" are deliberate:
      - ViewModels in MVVM intentionally contain presentation logic
      - Aggregate roots in DDD combine domain logic with data
      - Feature-based organization deliberately mixes layers per feature
    * **Consider framework constraints** - Many frameworks blur layer boundaries:
      - Android ViewModels are presentation layer by design
      - React components legitimately contain UI logic
      - ORM entities may have behavior (Active Record pattern)
    * **Verify actual negative impact** - Does this deviation cause problems?

5. **Analyze adherence to architectural patterns:**
    * Determine if the codebase follows any recognizable architectural patterns (e.g., Model-View-Controller, Model-View-ViewModel, Layered Architecture).
    * Highlight VERIFIED inconsistencies or deviations that cause actual problems.
    * Acknowledge when code follows a different-but-valid pattern.
6. **Provide specific code examples:**  Illustrate your findings by referencing relevant code snippets that clearly demonstrate the separation (or intentional organization) between architectural components.

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT assume all codebases must follow strict layered architecture
- ❌ Do NOT flag ViewModels containing presentation logic as "business logic in presentation"
- ❌ Do NOT flag feature-based organization as "layer violations"
- ❌ Do NOT flag ORM entities with methods as "data layer containing logic"
- ❌ Do NOT assume "business logic in controller" without verifying it's not just orchestration
- ✅ DO identify what architectural pattern the codebase is actually following
- ✅ DO recognize valid alternatives to layered architecture (vertical slices, feature folders)
- ✅ DO distinguish between orchestration code and business logic
- ✅ DO state confidence level for each architectural assessment

**Expected Output:** A clear and well-structured report that:

1. Identifies the architectural pattern(s) actually used in the codebase (not assumed).
2. Describes the purpose and responsibilities of each architectural component.
3. Provides concrete code examples to support the analysis.
4. Analyzes the codebase's adherence to its OWN architectural patterns, with **confidence levels**.
5. Distinguishes between actual architectural problems and valid alternative patterns.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with unambiguous layer identification objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic layer analysis
- DT-02 (Specific Focus Areas with Examples) - Specific layer categories (presentation, business logic, data access)
- DS-01 (Framework Application) - Applies established architectural patterns (MVC, MVVM, Layered Architecture)
- RT-05 (Evidence-Based Reasoning) - Requires specific code snippets to demonstrate findings
