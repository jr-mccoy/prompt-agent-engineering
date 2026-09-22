---
title: "Dependency Review"
description: "Review a service's third-party dependencies for unmaintained packages, license conflicts and single points of failure, and rank what to replace first."
tags:
  - dependencies
  - supply-chain
  - review
updated: "2026-07-01"
---

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

# Dependency Review

**Objective:** Review third-party dependencies and rank replacement candidates.

## When to Use

- A service's dependency list has grown without review.
- A package has gone unmaintained and you need to know how exposed you are.

## Method

1. List every direct dependency with its version and last release date.
2. Flag packages with no release in 18 months.
3. Flag license terms incompatible with the shipping licence.
4. Rank by blast radius times replacement difficulty.

## Output Format

A table of dependency, age, licence, blast radius, and replacement note.
