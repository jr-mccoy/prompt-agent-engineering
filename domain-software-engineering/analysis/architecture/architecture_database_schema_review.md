---
title: "Architecture Database Schema Review"
category: code-analysis
description: "Reviews database schema design for normalization, indexing, constraints, and performance optimization opportunities"
tags:
  - architecture
  - code-analysis
  - review
updated: "2026-03-19"
---

## Database Schema Review 

**Objective:** Review the database schema for normalization, indexing, and potential performance bottlenecks, providing recommendations for improvement based on best practices.

**Instructions:**

1. **Analyze the database schema:**  Obtain the schema definition (tables, columns, data types, relationships, keys, constraints, etc.) 
2. **Evaluate normalization levels:** Determine the normalization level of the schema (e.g., 1NF, 2NF, 3NF). Identify any tables that might benefit from further normalization to reduce data redundancy and improve data integrity.
3. **Assess indexing strategy:**
    * Analyze existing indexes and their effectiveness.
    * Identify columns or combinations of columns that are frequently used in query WHERE clauses or JOIN conditions and might benefit from indexing.
4. **Identify potential performance bottlenecks:** 
    * Look for large tables, complex queries, or inefficient data types that could negatively impact performance. 
    * Check for the appropriate use of primary and foreign keys for efficient data retrieval. 
5. **Suggest improvements and optimizations:**  Based on your analysis:
    * Recommend specific normalization steps if needed.
    * Suggest indexes to improve query performance. 
    * Recommend changes to data types or table structures to enhance efficiency.
    * Provide general recommendations for database optimization based on best practices. 

**Expected Output:** A comprehensive database schema review report that includes:

1. An assessment of normalization levels.
2. An evaluation of the indexing strategy.
3. Identification of potential performance bottlenecks.
4. Concrete and actionable recommendations for improving the schema design and performance.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with clear database schema review objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic schema evaluation
- RT-02 (Multi-Dimensional Analysis Framework) - Analyzes multiple dimensions (normalization, indexing, performance)
- DT-02 (Specific Focus Areas with Examples) - Specific analysis categories (normalization levels, indexing strategy, performance bottlenecks)
- ST-03 (Output Format Templates) - Defines comprehensive review report structure
