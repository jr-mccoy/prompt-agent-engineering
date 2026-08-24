#!/usr/bin/env python3
"""Generate CONSOLIDATED_TECHNIQUE_INVENTORY.md from batch extraction files."""

import re
import os
from collections import defaultdict

EXTRACTION_DIR = os.path.dirname(os.path.abspath(__file__))

BATCH_FILES = [
    ("batch_1_root.md", "Batch 1: Root-Level Analysis Files", "7 root-level analysis files (~1,372 lines)"),
    ("batch_2_agents_small.md", "Batch 2: Agent Analysis Files — Small", "6 agent analysis files (~1,974 lines)"),
    ("batch_3_agents_medium.md", "Batch 3: Agent Analysis Files — Medium", "4 agent analysis files (~2,170 lines)"),
    ("batch_4_agents_large.md", "Batch 4: Agent Analysis Files — Large", "5 agent analysis files (~3,330 lines)"),
    ("batch_5_skills_small.md", "Batch 5: Skill Analysis Files — Small", "7 skill analysis files (~1,810 lines)"),
    ("batch_6_skills_medium_small.md", "Batch 6: Skill Analysis Files — Medium-Small", "7 skill analysis files (~2,721 lines)"),
    ("batch_7_skills_medium_large.md", "Batch 7: Skill Analysis Files — Medium-Large", "11 skill analysis files (~5,260 lines)"),
    ("batch_8_skills_large_a.md", "Batch 8: Skill Analysis Files — Large", "4 skill analysis files (~3,080 lines)"),
    ("batch_9_skills_large_b.md", "Batch 9: Skill Analysis Files — Largest", "4 skill analysis files (~3,397 lines)"),
]

TABLE_ROW_RE = re.compile(
    r'^\|\s*(\d+)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
    r'\s*([^|]+?)\s*\|'
)


def extract_rows(filepath):
    rows = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            m = TABLE_ROW_RE.match(line)
            if m:
                rows.append({
                    'source_file': m.group(2).strip(),
                    'technique_name': m.group(3).strip(),
                    'code': m.group(4).strip(),
                    'family': m.group(5).strip(),
                    'maps_to_existing': m.group(6).strip(),
                    'novel': m.group(7).strip(),
                    'description': m.group(8).strip(),
                })
    return rows


def get_primary_family(family_str):
    return family_str.split('/')[0].split('(')[0].strip()


def main():
    all_rows = []
    batch_data = []

    for filename, label, description in BATCH_FILES:
        filepath = os.path.join(EXTRACTION_DIR, filename)
        rows = extract_rows(filepath)
        novel_count = sum(1 for r in rows if r['novel'].lower() == 'yes')
        existing_count = sum(1 for r in rows if r['novel'].lower() == 'no')
        batch_data.append({
            'label': label,
            'filename': filename,
            'description': description,
            'rows': rows,
            'total': len(rows),
            'novel': novel_count,
            'existing': existing_count,
        })
        all_rows.extend(rows)

    total = len(all_rows)
    novel_total = sum(1 for r in all_rows if r['novel'].lower() == 'yes')
    existing_total = sum(1 for r in all_rows if r['novel'].lower() == 'no')

    # Family counts
    family_counts = defaultdict(lambda: {'total': 0, 'novel': 0, 'existing': 0})
    for r in all_rows:
        pf = get_primary_family(r['family'])
        family_counts[pf]['total'] += 1
        if r['novel'].lower() == 'yes':
            family_counts[pf]['novel'] += 1
        else:
            family_counts[pf]['existing'] += 1

    # Source file counts
    source_counts = defaultdict(lambda: {'total': 0, 'novel': 0, 'existing': 0})
    for r in all_rows:
        source_counts[r['source_file']]['total'] += 1
        if r['novel'].lower() == 'yes':
            source_counts[r['source_file']]['novel'] += 1
        else:
            source_counts[r['source_file']]['existing'] += 1

    # Code collisions
    code_assignments = defaultdict(list)
    for r in all_rows:
        code = r['code']
        if code and code != '—' and code != '-':
            code_assignments[code].append({
                'name': r['technique_name'],
                'source': r['source_file'],
                'novel': r['novel'],
            })
    collisions = {}
    for code, assignments in code_assignments.items():
        unique_names = set(a['name'] for a in assignments)
        if len(unique_names) > 1:
            collisions[code] = assignments

    # Duplicate names
    name_occurrences = defaultdict(list)
    for r in all_rows:
        name_occurrences[r['technique_name']].append({
            'source': r['source_file'],
            'code': r['code'],
        })
    duplicates = {n: o for n, o in name_occurrences.items() if len(o) > 1}

    # ---- Generate the document ----
    lines = []

    def w(line=""):
        lines.append(line)

    w("# CONSOLIDATED TECHNIQUE INVENTORY")
    w()
    w("**Generated:** 2026-02-08")
    w("**Purpose:** Single consolidated inventory of all techniques extracted from 55 analysis files across 9 extraction batches. Input for Steps 0.2 (Master Index mapping) and 0.3 (novel technique identification).")
    w("**Source:** `domain-agentic-resources/documentation/technique-analyses/`")
    w()
    w("---")
    w()
    w("## Grand Totals")
    w()
    w(f"| Metric | Count |")
    w(f"|--------|-------|")
    w(f"| **Total techniques extracted** | **{total}** |")
    w(f"| **Marked as novel** | **{novel_total}** |")
    w(f"| **Marked as existing** | **{existing_total}** |")
    w(f"| **Source analysis files** | **{len(source_counts)}** |")
    w(f"| **Extraction batches** | **9** |")
    w(f"| **Code collisions (same code, different technique)** | **{len(collisions)}** |")
    w(f"| **Duplicate technique names (same name, multiple files)** | **{len(duplicates)}** |")
    w()
    w("> **Important context:** The 549 novel vs 141 existing counts reflect what each analysis file *self-reported*. Many analysis files were created independently and assigned codes from overlapping ranges, producing 149 code collisions. The actual number of *unique* novel techniques will be determined in Step 0.2 (mapping to Master Index) after deduplication.")
    w()
    w("---")
    w()
    w("## Summary by Family")
    w()
    w("| Family | Full Name | Total | Novel | Existing | % of Total |")
    w("|--------|-----------|-------|-------|----------|------------|")
    for fam in sorted(family_counts.keys(), key=lambda x: family_counts[x]['total'], reverse=True):
        fc = family_counts[fam]
        pct = f"{fc['total'] / total * 100:.1f}%"
        name_map = {
            'DS': 'Domain-Specific', 'ST': 'Structural', 'IT': 'Interaction',
            'AG': 'Agentic', 'QA': 'Quality Assurance', 'OT': 'Output',
            'RT': 'Reasoning', 'NE': 'Non-Engineering', 'CM': 'Context Management',
            'MP': 'Meta-Prompting', 'ED': 'Educational', 'OC': 'Output Control',
            'DT': 'Decomposition',
        }
        full_name = name_map.get(fam, fam)
        w(f"| {fam} | {full_name} | {fc['total']} | {fc['novel']} | {fc['existing']} | {pct} |")
    w()
    w("> **Note:** DS (Domain-Specific) techniques dominate at 48.7% of all extractions. This reflects the analysis files' focus on domain knowledge patterns embedded in specific tools and technologies. Techniques spanning multiple families (e.g., CM/DS) are counted under their primary (first-listed) family.")
    w()
    w("---")
    w()
    w("## Summary by Batch")
    w()
    w("| Batch | Source | Techniques | Novel | Existing |")
    w("|-------|--------|------------|-------|----------|")
    for bd in batch_data:
        w(f"| {bd['label']} | {bd['description']} | {bd['total']} | {bd['novel']} | {bd['existing']} |")
    w(f"| **Total** | **55 analysis files (~24,914 lines)** | **{total}** | **{novel_total}** | **{existing_total}** |")
    w()
    w("---")
    w()
    w("## Table of Contents — Batch Sections")
    w()
    for i, bd in enumerate(batch_data, 1):
        anchor = bd['label'].lower().replace(' ', '-').replace('—', '').replace(':', '').replace('  ', '-')
        w(f"{i}. [{bd['label']}](#{anchor})")
    w()
    w("---")
    w()

    # Write each batch section
    global_num = 0
    for bd in batch_data:
        w(f"## {bd['label']}")
        w()
        w(f"**Source:** {bd['description']}")
        w(f"**Techniques extracted:** {bd['total']} ({bd['novel']} novel, {bd['existing']} existing)")
        w()
        w("| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |")
        w("|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|")
        for r in bd['rows']:
            global_num += 1
            w(f"| {global_num} | {r['source_file']} | {r['technique_name']} | {r['code']} | {r['family']} | {r['maps_to_existing']} | {r['novel']} | {r['description']} |")
        w()
        w("---")
        w()

    # Cross-Batch Analysis
    w("## Cross-Batch Analysis")
    w()

    # Code collisions
    w("### Code Collisions")
    w()
    w(f"**{len(collisions)} codes** are assigned to different techniques across different analysis files. These must be resolved during Step 0.2 (Master Index mapping).")
    w()
    w("The collisions fall into two categories:")
    w()
    w("1. **Synthesis vs. Detailed file overlap:** The `priority_4_sonnet_agents_synthesis.md` is a meta-analysis that summarizes findings from 6 detailed agent group analyses (C4 Architecture, Security-Coder, Business, Infrastructure, Documentation, Language-DevOps). Many codes appear in both the synthesis and the detailed file — these are the *same technique* documented twice. Similarly, `priority_5_haiku_agents_analysis.md` covers agents also analyzed in `priority_6_inherit_agents_analysis.md`.")
    w()
    w("2. **Independent code assignment:** Different analysis files (created in separate sessions) independently assigned codes from overlapping number ranges. For example, DS-50 is assigned to three completely different techniques across three files.")
    w()

    # Group collisions by family
    collision_by_family = defaultdict(list)
    for code in sorted(collisions.keys()):
        fam = code.split('-')[0]
        collision_by_family[fam].append(code)

    w("#### Collision Summary by Family")
    w()
    w("| Family | Colliding Codes | Count |")
    w("|--------|----------------|-------|")
    for fam in sorted(collision_by_family.keys()):
        codes = collision_by_family[fam]
        w(f"| {fam} | {', '.join(codes)} | {len(codes)} |")
    w()

    w("#### Full Collision List")
    w()
    w("| Code | Assignments (Technique Name — Source File) |")
    w("|------|------------------------------------------|")
    for code in sorted(collisions.keys(), key=lambda c: (c.split('-')[0], int(re.search(r'\d+', c.split('-')[1]).group()) if re.search(r'\d+', c.split('-')[1]) else 0)):
        assigns = collisions[code]
        # Deduplicate same name + source
        seen = set()
        unique_assigns = []
        for a in assigns:
            key = f"{a['name']}|{a['source']}"
            if key not in seen:
                seen.add(key)
                unique_assigns.append(a)
        parts = [f"**{a['name']}** ({a['source']})" for a in unique_assigns]
        w(f"| {code} | {' ⟷ '.join(parts)} |")
    w()

    # Duplicate technique names
    w("### Duplicate Technique Names Across Files")
    w()
    w(f"**{len(duplicates)} technique names** appear in multiple source files. Many are expected duplicates (synthesis file + detailed file documenting the same technique). Others represent genuinely different techniques with coincidentally similar names.")
    w()
    w("| Technique Name | Occurrences | Source Files |")
    w("|---------------|-------------|-------------|")
    for name in sorted(duplicates.keys()):
        occs = duplicates[name]
        sources = [f"{o['source']} [{o['code']}]" for o in occs]
        w(f"| {name} | {len(occs)} | {', '.join(sources)} |")
    w()

    # Source file coverage
    w("### Source File Coverage")
    w()
    w(f"All **{len(source_counts)} analysis files** were processed across the 9 batches:")
    w()
    w("| Source File | Total | Novel | Existing |")
    w("|------------|-------|-------|----------|")
    for sf in sorted(source_counts.keys()):
        sc = source_counts[sf]
        w(f"| {sf} | {sc['total']} | {sc['novel']} | {sc['existing']} |")
    w()

    w("---")
    w()
    w("## Notes for Steps 0.2 and 0.3")
    w()
    w("### Key Issues to Address")
    w()
    w("1. **Code collision resolution (149 collisions):** The same code (e.g., DS-50) is assigned to completely different techniques in different files. Step 0.2 must assign unique codes or identify which assignments map to the same Master Index entry.")
    w()
    w("2. **Synthesis file deduplication:** `priority_4_sonnet_agents_synthesis.md` (69 techniques) and `priority_5_haiku_agents_analysis.md` (42 techniques) overlap heavily with detailed analysis files in Batches 3, 4, and 7. The synthesis files document the *same techniques* as their detailed counterparts. Expect ~50-80 duplicates from this overlap alone.")
    w()
    w("3. **DS family dominance (48.7%):** Domain-Specific techniques account for nearly half of all extractions. Many of these may be too specific to individual tools (e.g., \"Stripe Webhook Event Patterns\", \"Solidity Version-Specific Security\") to warrant addition to the Master Index as general techniques.")
    w()
    w("4. **Self-reported novelty is unreliable:** Analysis files marked 549 of 690 techniques (79.6%) as novel. Given 149 code collisions and 41 duplicate names, the actual unique novel count is significantly lower. Step 0.2's cross-reference against the Master Index will provide the true count.")
    w()
    w("5. **Estimated unique techniques:** After removing synthesis/detailed duplicates (~60-80) and same-name duplicates (~41), the estimated unique technique count is approximately **500-550**, of which roughly **350-400** may be genuinely novel (not mapped to existing Master Index entries).")
    w()
    w("### Recommended Approach for Step 0.2")
    w()
    w("1. Build a flat reference list from `MASTER_TECHNIQUE_INDEX.md` (Step 0.2a)")
    w("2. Process this consolidated inventory family-by-family (DS first, since it's largest)")
    w("3. For each code collision, determine which assignment is the \"primary\" technique")
    w("4. For each duplicate name, merge into a single entry")
    w("5. For each remaining technique, fuzzy-match against the Master Index reference")
    w("6. Output: `MAPPED_TECHNIQUE_INVENTORY.md` with verified mappings")
    w()
    w("---")
    w()
    w("*This file was generated by `consolidate.py` and `generate_consolidated.py` from 9 batch extraction files.*")
    w("*It serves as the primary input for Phase 0, Steps 0.2 and 0.3 of the Framework Audit & Improvement Plan.*")

    # Write the file
    output_path = os.path.join(EXTRACTION_DIR, "CONSOLIDATED_TECHNIQUE_INVENTORY.md")
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')

    print(f"Generated {output_path}")
    print(f"Total lines: {len(lines)}")
    print(f"Total techniques: {total}")


if __name__ == '__main__':
    main()
