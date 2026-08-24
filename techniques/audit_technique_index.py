#!/usr/bin/env python3
"""Pre-commit integrity audit for MASTER_TECHNIQUE_INDEX.md (stdlib only).

Checks (fenced ``` code blocks are skipped entirely — examples/templates don't count):
  1. Every referenced technique ID resolves to a definition.               [HARD]
  2. No ID has more than one PRIMARY definition heading.                   [HARD]
  3. No dead new-techniques/ links.                                        [HARD]
  4. Every "ID (Proper Name)" pairing matches the ID's canonical name.     [SOFT]
  5. Header count reconciles with the primary-definition count.            [SOFT]

Definition forms recognized (outside fences):
  - "### ID: Name"  /  "#### ID: Name"                         (heading)
  - "**ID: Name**"                                             (bold entry)
  - multi-ID group   "**ID1/ID2/ID3: Name**"                   (defines each)
  - merge source     "*(Merged from A + B)*"                   (A, B resolvable)
  - deprecation stub "### ID: Name → **Merged into TARGET**"   (ID resolvable)
  - alias            "(also ID)"                               (ID resolvable)

An undefined reference is only flagged if its prefix is a real technique
namespace (i.e. that prefix has >=1 primary definition) — this excludes
external IDs like AP-* anti-patterns, GPT-4/5, UTF-8.

Hard checks gate a commit (exit non-zero). Soft checks warn only.
Usage:  python3 audit_technique_index.py [MASTER_TECHNIQUE_INDEX.md]
"""
import re, sys, collections

ID = r'[A-Z]{2,3}-\d+'
ID_RE = re.compile(ID)
GROUP = r'[A-Z]{2,3}-\d+(?:/[A-Z]{2,3}-\d+)*'
# PRIMARY = a "### ID:" / "#### ID:" structural heading (the authoritative definition).
PRIMARY_RE = re.compile(r'^#{2,4}\s+(' + GROUP + r')\s*[:*]')
# SECONDARY = a "**ID: Name**" bold catalog entry (resolvable, not dup-checked).
BOLD_RE = re.compile(r'^\*\*(' + GROUP + r')\s*:')
MERGED_FROM_RE = re.compile(r'\(Merged from ([^)]+)\)')
ALIAS_RE = re.compile(r'\(also (' + ID + r')\)')
DEPRECATED_RE = re.compile(r'Merged into|DEPRECATED', re.I)

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def is_proper_name(s):
    s = s.strip()
    if re.search(r'\d{4}-\d{2}-\d{2}', s) or re.match(r'^\d', s) or 'variant' in s.lower():
        return False
    words = [w for w in re.split(r'[\s/&-]+', s) if w]
    return bool(words) and sum(1 for w in words if w[:1].isupper()) >= max(1, (len(words)+1)//2)

def content_lines(text):
    """Yield (lineno, line) for lines OUTSIDE fenced code blocks."""
    fence = False
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.lstrip().startswith('```'):
            fence = not fence
            continue
        if not fence:
            yield i, ln

def main(path):
    text = open(path, encoding='utf-8').read()
    body = list(content_lines(text))

    primary = collections.Counter()   # ID -> count of "### ID:" structural headings
    canon = {}                         # ID -> canonical name
    defined = set()                    # all resolvable IDs (primary + bold + merged + alias)
    deprecated = set()                 # IDs that are merged-away / deprecated stubs
    for _, ln in body:
        mh, mb = PRIMARY_RE.match(ln), BOLD_RE.match(ln)
        m = mh or mb
        if m:
            ids = m.group(1).split('/')
            for tid in ids:
                defined.add(tid)
                if mh:
                    primary[tid] += 1
                if DEPRECATED_RE.search(ln):
                    deprecated.add(tid)
            nm = ln.split(':', 1)[1] if ':' in ln else ''
            nm = re.split(r'\s*(?:\*\(|→|✓|\*\*)', nm)[0].strip().strip('*').strip()
            if nm and len(ids) == 1:
                canon.setdefault(ids[0], nm)
        for grp in MERGED_FROM_RE.findall(ln):
            defined.update(ID_RE.findall(grp))
        for a in ALIAS_RE.findall(ln):
            defined.add(a)

    valid_prefixes = {t.split('-')[0] for t in defined}
    referenced = collections.Counter()
    for _, ln in body:
        for tid in ID_RE.findall(ln):
            referenced[tid] += 1
    undefined = sorted(t for t in referenced
                       if t not in defined and t.split('-')[0] in valid_prefixes)

    mislabeled = []
    for _, ln in body:
        for tid, name in re.findall(r'\b(' + ID + r')\s*\(([^)]{2,60})\)', ln):
            if tid in canon and is_proper_name(name):
                c = canon[tid]
                if norm(name) and norm(name) not in norm(c) and norm(c) not in norm(name):
                    mislabeled.append((tid, name, c))
    mislabeled = sorted(set(mislabeled))

    dead = [i for i, ln in body if '[Full documentation: new-techniques/' in ln]
    dups = sorted(t for t, c in primary.items() if c > 1)

    active = sorted(t for t in defined if t not in deprecated)
    hdr = re.search(r'(\d+)\s+active technique definitions', text)
    hdr_n = int(hdr.group(1)) if hdr else None

    print(f"Active technique definitions (resolvable) .. {len(active)}")
    print(f"  of which structural (### heading) ........ {len(primary)}")
    print(f"  deprecated / merged-away stubs ........... {len(deprecated)}")
    print(f"Header-stated active count ................. {hdr_n if hdr_n is not None else '?'}")
    print(f"[HARD] Referenced-but-UNDEFINED IDs ........ {len(undefined)}  {undefined}")
    print(f"[HARD] Duplicate structural definitions .... {dups or 'none'}")
    print(f"[HARD] Dead new-techniques/ links .......... {len(dead)}  {dead}")
    print(f"[SOFT] Mislabeled 'ID (Name)' pairings ..... {len(mislabeled)}")
    for tid, name, c in mislabeled:
        print(f"        {tid} cited as '{name}' — canonical: '{c}'")
    if hdr_n is not None and hdr_n != len(active):
        print(f"[SOFT] Header count {hdr_n} != active count {len(active)}")

    hard_fail = bool(undefined) or bool(dead) or bool(dups)
    print("\nRESULT:", "FAIL (hard checks)" if hard_fail else "PASS (hard checks)")
    return 1 if hard_fail else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'MASTER_TECHNIQUE_INDEX.md'))
