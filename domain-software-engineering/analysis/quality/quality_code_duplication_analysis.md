---
title: "Code Duplication Analysis"
category: code-analysis/quality
description: "Identify duplicated code fragments and suggest refactoring opportunities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: beginner
tags:
  - code-quality
  - duplication
  - dry
  - refactoring
  - maintainability
updated: "2026-03-19"
---

# Code Duplication Analysis

**Objective:** Analyze the codebase to identify duplicated code fragments, providing insights into potential maintainability issues and suggesting refactoring opportunities.

**Instructions:**

1. Review the codebase and identify instances of duplicated code.

2. **CRITICAL: Verify each potential duplication before reporting.** For each suspected duplication:
   * **Assess whether duplication is actually problematic** - Not all duplication is bad:
     - Similar-looking code may handle different cases that need to diverge
     - 2-3 lines of similar code is often clearer than an abstraction
     - "Duplication" across test files is usually intentional and acceptable
     - Boilerplate required by frameworks isn't harmful duplication
   * **Consider the abstraction tradeoff** - Would refactoring improve or harm the code?
     - Premature abstraction creates coupling and reduces clarity
     - Some repetition is better than the wrong abstraction
     - Code that may diverge in the future shouldn't be prematurely unified
   * **Check if the duplication is intentional** - Look for:
     - Comments explaining why code is deliberately similar
     - Different contexts that require independent evolution
     - Copy-paste that's appropriate for isolated modules

3. For each VERIFIED problematic duplication, analyze:

   a. Location:
      - File paths of affected files
      - Line numbers in each file

   b. Duplication Details:
      - Length of the duplicated code fragment (in lines of code)
      - Content or purpose of the duplicated code
      - **Why this duplication is actually problematic** (not just that it exists)

   c. Impact Assessment:
      - Potential impact on code maintainability
      - Risks associated with the duplication (e.g., inconsistent updates)
      - **Confidence level** (High/Medium/Low) that refactoring would improve things

   d. Refactoring Opportunities:
      - Suggestions for extracting duplicated code into reusable functions or classes
      - Potential design patterns or architectural changes to eliminate duplication
      - **Tradeoffs** of the suggested refactoring

4. Identify patterns or trends in code duplication across the codebase.

5. Assess the overall impact of code duplication on the project's maintainability and scalability.

6. Suggest improvements to reduce code duplication, considering:
   - Priority areas based on the extent and impact of duplication
   - Refactoring strategies that align with the project's architecture
   - Tools or processes to prevent future code duplication

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag short (2-5 line) similar code as duplication—explicit code is often clearer
- ❌ Do NOT flag test file duplication—tests should be independent and explicit
- ❌ Do NOT flag framework-required boilerplate as duplication
- ❌ Do NOT suggest abstraction if the code may need to diverge in the future
- ❌ Do NOT flag similar-looking code that handles genuinely different cases
- ✅ DO consider whether abstraction would actually improve the code
- ✅ DO check if the duplication serves a purpose (isolation, clarity, future divergence)
- ✅ DO flag duplication only when changes need to be synchronized across locations
- ✅ DO state confidence level and acknowledge when duplication might be intentional

**Expected Output:** A comprehensive analysis of the codebase's code duplication, including:

1. An overview of the duplication analysis findings
2. Detailed breakdowns for each identified duplication
3. General recommendations for reducing and preventing code duplication
4. If applicable, a summary of duplication trends or patterns observed in the codebase

For each identified duplication, use the following format:

Files:
- [file path 1]
- [file path 2]
Line(s): 
- [file 1 line numbers]
- [file 2 line numbers]
Length: [number of duplicated lines]
Impact: [potential impact on maintainability]
Suggestions:
- [refactoring suggestion 1]
- [refactoring suggestion 2]
- ...

If no significant duplications are found, provide a summary stating that the codebase has minimal code duplication.

Conclude with an overall assessment of the code duplication in the project, including recommendations for addressing the most critical instances and strategies for maintaining a DRY (Don't Repeat Yourself) codebase.

**Example Output:**

```markdown
## Code Duplication Analysis Report

### Overview
Analysis identified **12 instances of significant code duplication** totaling approximately **340 duplicated lines**. The most critical duplications are in the API response handling and validation logic.

### Critical Duplications

---

**Files:**
- `src/controllers/UserController.ts`
- `src/controllers/ProductController.ts`
- `src/controllers/OrderController.ts`

**Line(s):**
- UserController.ts: 23-45
- ProductController.ts: 31-53
- OrderController.ts: 18-40

**Length:** 22 lines (repeated 3 times = 66 total duplicated lines)

**Duplicated Code:**
```typescript
// Error handling pattern duplicated across all controllers
try {
  const result = await service.process(data);
  if (!result.success) {
    return res.status(400).json({
      error: result.error,
      code: result.errorCode,
      timestamp: new Date().toISOString()
    });
  }
  return res.status(200).json({
    data: result.data,
    timestamp: new Date().toISOString()
  });
} catch (error) {
  logger.error('Operation failed', { error });
  return res.status(500).json({
    error: 'Internal server error',
    timestamp: new Date().toISOString()
  });
}
```

**Impact:**
- High maintainability risk - changes require updates in 3 locations
- Inconsistency risk if one instance is updated but others are not
- Violates DRY principle

**Suggestions:**
- Extract into a `ResponseHandler` utility class
- Use middleware pattern for consistent error handling
- Consider implementing a base controller class

**Refactored Solution:**
```typescript
// src/utils/responseHandler.ts
export class ResponseHandler {
  static success<T>(res: Response, data: T): Response {
    return res.status(200).json({
      data,
      timestamp: new Date().toISOString()
    });
  }

  static error(res: Response, error: string, code: string, status = 400): Response {
    return res.status(status).json({
      error,
      code,
      timestamp: new Date().toISOString()
    });
  }
}

// Usage in controller
const result = await service.process(data);
return result.success
  ? ResponseHandler.success(res, result.data)
  : ResponseHandler.error(res, result.error, result.errorCode);
```

---

**Files:**
- `src/validators/userValidator.ts`
- `src/validators/productValidator.ts`

**Line(s):**
- userValidator.ts: 12-35
- productValidator.ts: 8-31

**Length:** 23 lines

**Impact:** Medium - validation logic changes would require updates in multiple files

**Suggestions:**
- Create a generic `ValidationBuilder` class
- Use schema-based validation (Joi, Zod, or Yup)

---

### Duplication Summary

| Category | Instances | Total Lines | Priority |
|----------|-----------|-------------|----------|
| Error Handling | 3 | 66 | Critical |
| Validation Logic | 4 | 92 | High |
| Data Transformation | 3 | 45 | Medium |
| Logging Patterns | 2 | 24 | Low |

### Recommendations

1. **Immediate Action**: Refactor error handling into shared utility (saves 66 lines)
2. **Short-term**: Implement validation framework to eliminate validation duplication
3. **Process Improvement**: Add duplication detection to CI pipeline (e.g., jscpd, SonarQube)
4. **Code Review**: Include duplication check in PR review checklist
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic analysis
- RT-02 (Multi-Dimensional Analysis Framework) - Location, Details, Impact, Refactoring structure
- ST-03 (Output Format Templates) - Specific format for each identified duplication
- OC-04 (Conditional Output Logic) - Handles case when no significant duplications found
- DS-04 (Pattern Recognition Requests) - Requests identification of duplication trends
- DS-06 (Prioritization and Severity Guidance) - Priority areas based on extent and impact