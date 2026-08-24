---
title: "Architecture Database Schema Documentation"
category: code-analysis
description: "Generates comprehensive database schema documentation including ERD, table descriptions, and relationship explanations"
tags:
  - architecture
  - code-analysis
updated: "2026-03-19"
---

## Generate Database Schema Documentation

**Objective:** Create clear, comprehensive, and well-structured documentation for the provided database schema, including descriptions of tables, columns, relationships, indexes, and constraints. 

**Instructions:**

1. **Access the database schema:** Obtain the schema definition, including information about:
    * Tables: Names, primary keys, foreign keys, indexes, and any other constraints.
    * Columns: Names, data types, default values, constraints (e.g., NOT NULL, UNIQUE), and whether they are part of a primary or foreign key.
    * Relationships:  How tables are related to each other (one-to-one, one-to-many, many-to-many).
2. **Organize the documentation:**  Structure the documentation logically, for example:
    * By table: Provide a dedicated section for each table in the schema. 
    * By relationship: Group tables based on their relationships (e.g., orders and order items).
3. **Provide clear and concise descriptions:**  
    * **Table Descriptions:**  Explain the purpose of each table and the type of data it stores. 
    * **Column Descriptions:** Explain the purpose of each column, its data type, allowed values, and any relevant business rules.
    * **Relationship Descriptions:** Clearly describe how tables are related, including cardinality (one-to-one, etc.).  
4. **Consider using visuals:**  Incorporate diagrams (like Entity-Relationship Diagrams) to visually represent relationships between tables.

**Expected Output:**  Well-structured and informative database schema documentation that can be:

* Easily understood by both technical and non-technical audiences.
* Used for reference, onboarding new team members, or generating data dictionaries.
* Output formats could be:
    * Markdown files (`.md`)
    * HTML pages
    * Database schema documentation tools (e.g., SchemaSpy).

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise documentation generation objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic schema documentation
- DT-02 (Specific Focus Areas with Examples) - Detailed categories (tables, columns, relationships, indexes, constraints)
- ST-03 (Output Format Templates) - Specifies multiple output formats (Markdown, HTML, schema tools)
- DS-05 (Visualization and Communication Guidance) - Recommends ER diagrams for relationship representation
