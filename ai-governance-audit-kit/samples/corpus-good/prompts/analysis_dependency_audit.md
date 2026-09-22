---
title: "Dependency Audit"
description: "Audit third-party dependencies for unmaintained packages, licence conflicts and single points of failure, then rank which to replace first."
tags:
  - dependencies
  - supply-chain
  - audit
updated: "2026-07-14"
---

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

# Dependency Audit

**Objective:** Audit third-party dependencies and rank what to replace.

## When to Use

- Before a release, to know which dependencies are unmaintained.
- A licence review flagged a package and you need the surrounding picture.

## Method

1. Enumerate direct dependencies, versions and release dates.
2. Mark anything unreleased for 18 months.
3. Mark licence terms that conflict with the shipping licence.
4. Order by blast radius and replacement difficulty.

## Output Format

A table of dependency, age, licence, blast radius, replacement note.
