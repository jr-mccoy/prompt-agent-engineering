#!/usr/bin/env python3
"""Consolidate all batch extraction files into a single inventory."""

import re
import os
from collections import defaultdict

EXTRACTION_DIR = os.path.dirname(os.path.abspath(__file__))

BATCH_FILES = [
    ("batch_1_root.md", "Batch 1: Root-Level Analysis Files"),
    ("batch_2_agents_small.md", "Batch 2: Agent Analysis Files — Small"),
    ("batch_3_agents_medium.md", "Batch 3: Agent Analysis Files — Medium"),
    ("batch_4_agents_large.md", "Batch 4: Agent Analysis Files — Large"),
    ("batch_5_skills_small.md", "Batch 5: Skill Analysis Files — Small"),
    ("batch_6_skills_medium_small.md", "Batch 6: Skill Analysis Files — Medium-Small"),
    ("batch_7_skills_medium_large.md", "Batch 7: Skill Analysis Files — Medium-Large"),
    ("batch_8_skills_large_a.md", "Batch 8: Skill Analysis Files — Large"),
    ("batch_9_skills_large_b.md", "Batch 9: Skill Analysis Files — Largest"),
]

# Regex to match table rows: | # | Source File | Technique Name | Code | Family | Maps To Existing | Novel? | Brief Description |
TABLE_ROW_RE = re.compile(
    r'^\|\s*(\d+)\s*\|'          # row number
    r'\s*([^|]+?)\s*\|'          # source file
    r'\s*([^|]+?)\s*\|'          # technique name
    r'\s*([^|]+?)\s*\|'          # code
    r'\s*([^|]+?)\s*\|'          # family
    r'\s*([^|]+?)\s*\|'          # maps to existing
    r'\s*([^|]+?)\s*\|'          # novel?
    r'\s*([^|]+?)\s*\|'          # brief description
)


def extract_rows(filepath):
    """Extract all technique rows from a batch file."""
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
    """Extract primary family from strings like 'CM/DS' or 'AG'."""
    # Take the first family mentioned
    return family_str.split('/')[0].split('(')[0].strip()


def main():
    all_rows = []
    batch_stats = []

    for filename, label in BATCH_FILES:
        filepath = os.path.join(EXTRACTION_DIR, filename)
        rows = extract_rows(filepath)
        batch_stats.append({
            'label': label,
            'filename': filename,
            'total': len(rows),
            'novel': sum(1 for r in rows if r['novel'].lower() == 'yes'),
            'existing': sum(1 for r in rows if r['novel'].lower() == 'no'),
        })
        for r in rows:
            r['batch'] = label
            r['batch_file'] = filename
        all_rows.extend(rows)

    # Compute family stats
    family_counts = defaultdict(lambda: {'total': 0, 'novel': 0, 'existing': 0})
    for r in all_rows:
        pf = get_primary_family(r['family'])
        family_counts[pf]['total'] += 1
        if r['novel'].lower() == 'yes':
            family_counts[pf]['novel'] += 1
        else:
            family_counts[pf]['existing'] += 1

    # Compute source file stats
    source_counts = defaultdict(lambda: {'total': 0, 'novel': 0, 'existing': 0})
    for r in all_rows:
        source_counts[r['source_file']]['total'] += 1
        if r['novel'].lower() == 'yes':
            source_counts[r['source_file']]['novel'] += 1
        else:
            source_counts[r['source_file']]['existing'] += 1

    # Find code collisions (same code, different technique names)
    code_assignments = defaultdict(list)
    for r in all_rows:
        code = r['code']
        if code and code != '—' and code != '-':
            code_assignments[code].append({
                'name': r['technique_name'],
                'source': r['source_file'],
                'batch': r['batch'],
                'novel': r['novel'],
            })

    collisions = {}
    for code, assignments in code_assignments.items():
        unique_names = set(a['name'] for a in assignments)
        if len(unique_names) > 1:
            collisions[code] = assignments

    # Count duplicate technique names (same name across batches)
    name_occurrences = defaultdict(list)
    for r in all_rows:
        name_occurrences[r['technique_name']].append({
            'source': r['source_file'],
            'batch': r['batch'],
            'code': r['code'],
        })

    duplicates = {name: occs for name, occs in name_occurrences.items() if len(occs) > 1}

    # Print stats for debugging
    total = len(all_rows)
    novel = sum(1 for r in all_rows if r['novel'].lower() == 'yes')
    existing = sum(1 for r in all_rows if r['novel'].lower() == 'no')

    print(f"Total techniques: {total}")
    print(f"Novel: {novel}")
    print(f"Existing: {existing}")
    print(f"Source files: {len(source_counts)}")
    print(f"Code collisions: {len(collisions)}")
    print(f"Duplicate names: {len(duplicates)}")
    print()

    print("Family breakdown:")
    for fam in sorted(family_counts.keys(), key=lambda x: family_counts[x]['total'], reverse=True):
        fc = family_counts[fam]
        print(f"  {fam}: {fc['total']} (novel={fc['novel']}, existing={fc['existing']})")

    print()
    print("Per-batch stats:")
    for bs in batch_stats:
        print(f"  {bs['label']}: {bs['total']} total, {bs['novel']} novel, {bs['existing']} existing")

    print()
    print(f"Code collisions ({len(collisions)}):")
    for code in sorted(collisions.keys()):
        assigns = collisions[code]
        names = [f"'{a['name']}' ({a['source']})" for a in assigns]
        print(f"  {code}: {' vs '.join(set(names))}")

    print()
    print(f"Duplicate technique names ({len(duplicates)}):")
    for name in sorted(duplicates.keys()):
        occs = duplicates[name]
        sources = [f"{o['source']} [{o['code']}]" for o in occs]
        print(f"  '{name}': {', '.join(sources)}")

    # Return data for use
    return {
        'all_rows': all_rows,
        'batch_stats': batch_stats,
        'family_counts': dict(family_counts),
        'source_counts': dict(source_counts),
        'collisions': collisions,
        'duplicates': duplicates,
        'total': total,
        'novel': novel,
        'existing': existing,
    }


if __name__ == '__main__':
    main()
