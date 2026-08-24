---
title: "Hash Table Design and Collision Resolution"
category: algorithms
description: "Comprehensive guide for designing hash tables, selecting hash functions, and implementing collision resolution strategies"
tags:
  - algorithms
  - data-structures
  - hash-tables
  - hashing
  - collision-resolution
  - system-design
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-03  # Tree of Thoughts
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
  - ST-03  # Output Format Templates
difficulty: intermediate
version: "1.0"
updated: 2026-01-23
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_complexity_analysis.md
---

# Hash Table Design and Collision Resolution

**Objective:** Design efficient hash tables by selecting appropriate hash functions, collision resolution strategies, and sizing policies based on use case requirements.

**When to Use:** Use this prompt when implementing custom hash-based data structures, optimizing lookup-heavy systems, designing caches, building symbol tables, or solving problems requiring O(1) average-case operations.

## Instructions

### 1. Requirements Analysis

Before designing a hash table, analyze requirements:

**Key Characteristics:**
- **Key Type:** Integers, strings, objects, composite keys?
- **Key Distribution:** Uniform? Clustered? Sequential?
- **Key Size:** Fixed or variable length?
- **Key Uniqueness:** Unique keys or multimap (duplicate keys)?

**Operation Profile:**
| Operation | Frequency | Notes |
|-----------|-----------|-------|
| Insert | [High/Medium/Low] | |
| Lookup | [High/Medium/Low] | |
| Delete | [High/Medium/Low] | |
| Iterate | [High/Medium/Low] | Order matters? |
| Resize | [Expected frequency] | |

**Constraints:**
- **Expected Size (n):** How many elements?
- **Memory Budget:** Space constraints?
- **Load Factor Target:** Acceptable fill ratio?
- **Latency Requirements:** Worst-case acceptable?
- **Concurrency:** Single or multi-threaded?

### 2. Hash Function Design

A good hash function should:
1. **Deterministic:** Same key always produces same hash
2. **Uniform:** Distribute keys evenly across buckets
3. **Efficient:** Fast to compute
4. **Avalanche:** Small key changes produce large hash changes

#### Integer Hash Functions

**Division Method:**
```
h(k) = k mod m
```
- Simple but requires careful choice of m
- Choose m as prime not close to power of 2
- Avoid m = 2^p (only uses lowest p bits)

**Multiplication Method:**
```
h(k) = floor(m * (k * A mod 1))
where A ≈ 0.6180339887... (golden ratio - 1)
```
- Works well with any m
- Good bit mixing properties

**MurmurHash / xxHash:**
- High-quality, fast hash functions
- Excellent distribution properties
- Recommended for production use

#### String Hash Functions

**Polynomial Rolling Hash:**
```
h(s) = (s[0] * p^(n-1) + s[1] * p^(n-2) + ... + s[n-1]) mod m
where p = prime (31 or 37 commonly used)
```
- Good distribution for strings
- Can compute incrementally
- Watch for integer overflow

**djb2 Hash:**
```
def djb2(s):
    hash = 5381
    for c in s:
        hash = ((hash << 5) + hash) + ord(c)  # hash * 33 + c
    return hash
```
- Simple and effective
- Widely used

**FNV-1a Hash:**
```
def fnv1a(s):
    hash = 2166136261  # FNV offset basis
    for c in s:
        hash ^= ord(c)
        hash *= 16777619  # FNV prime
        hash &= 0xFFFFFFFF  # Keep 32 bits
    return hash
```
- Better avalanche than djb2
- Recommended for general use

#### Object/Composite Key Hashing

**Combine Component Hashes:**
```
def hash_composite(a, b, c):
    # XOR with prime multiplication
    h = 17
    h = h * 31 + hash(a)
    h = h * 31 + hash(b)
    h = h * 31 + hash(c)
    return h
```
- Order matters (different for (a,b) vs (b,a))
- Use prime multipliers for distribution

### 3. Collision Resolution Strategies

#### Strategy 1: Separate Chaining

**Concept:** Each bucket contains a linked list (or other container) of entries.

```
Bucket Array:
[0] → (k1, v1) → (k5, v5) → null
[1] → (k2, v2) → null
[2] → null
[3] → (k3, v3) → (k4, v4) → (k7, v7) → null
...
```

**Implementation:**
```python
class HashTableChaining:
    def __init__(self, capacity=16, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        bucket_idx = self._hash(key)
        for k, v in self.buckets[bucket_idx]:
            if k == key:
                return v
        return None  # or raise KeyError

    def delete(self, key):
        bucket_idx = self._hash(key)
        bucket = self.buckets[bucket_idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
```

**Complexity:**
| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n + m) | m = buckets |

**Advantages:**
- Simple to implement
- Deletion is straightforward
- Works well with high load factors
- Can store more items than buckets

**Disadvantages:**
- Extra memory for pointers
- Poor cache locality
- Worst case O(n) if all keys collide

**Optimizations:**
- Use dynamic arrays instead of linked lists
- Convert long chains to trees (Java 8+ HashMap)
- Use perfect hashing for static sets

---

#### Strategy 2: Open Addressing - Linear Probing

**Concept:** On collision, probe sequential buckets until empty slot found.

```
Probe sequence: h(k), h(k)+1, h(k)+2, ...

Insert k1, k2 (collision at index 3):
[0] [1] [2] [k1, 3] [k2, 4] [5] [6] [7]
                    ↑ k2 placed here
```

**Implementation:**
```python
class HashTableLinearProbing:
    DELETED = object()  # Tombstone marker

    def __init__(self, capacity=16, load_factor=0.5):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        idx = self._hash(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            if self.keys[idx] is self.DELETED:
                break  # Can reuse tombstone
            idx = (idx + 1) % self.capacity

        self.keys[idx] = key
        self.values[idx] = value
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
        return None

    def delete(self, key):
        idx = self._hash(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                self.values[idx] = None
                self.size -= 1
                return True
            idx = (idx + 1) % self.capacity
        return False
```

**Complexity:**
| Load Factor (α) | Expected Probes (Success) | Expected Probes (Failure) |
|-----------------|---------------------------|---------------------------|
| 0.5 | 1.5 | 2.5 |
| 0.75 | 2.5 | 8.5 |
| 0.9 | 5.5 | 50.5 |

**Advantages:**
- Better cache locality (sequential access)
- No extra pointer memory
- Simple implementation

**Disadvantages:**
- Primary clustering (consecutive runs)
- Deletion requires tombstones
- Performance degrades quickly above 70% load

---

#### Strategy 3: Open Addressing - Quadratic Probing

**Concept:** Probe at quadratic intervals to reduce clustering.

```
Probe sequence: h(k), h(k)+1², h(k)+2², h(k)+3², ...
             = h(k), h(k)+1, h(k)+4, h(k)+9, ...
```

**Alternative Formula (better coverage):**
```
Probe: h(k) + (i + i²) / 2 for i = 0, 1, 2, ...
```

**Advantages over Linear:**
- Reduces primary clustering
- Better distribution of probes

**Disadvantages:**
- Secondary clustering still occurs
- May not probe all buckets (capacity must be prime or power of 2)
- Slightly worse cache locality than linear

---

#### Strategy 4: Open Addressing - Double Hashing

**Concept:** Use second hash function to determine probe step.

```
Probe sequence: h1(k), h1(k)+h2(k), h1(k)+2*h2(k), ...

h1(k) = k mod m
h2(k) = 1 + (k mod (m-1))  // Must be non-zero
```

**Properties:**
- h2(k) must never be 0
- h2(k) and m should be coprime (guarantees full probing)
- If m is prime, any h2(k) in [1, m-1] works

**Advantages:**
- Nearly uniform probing (no clustering)
- Best theoretical performance for open addressing

**Disadvantages:**
- Two hash computations per probe
- More complex implementation
- Cache locality worse than linear

---

#### Strategy 5: Cuckoo Hashing

**Concept:** Use two hash tables with different hash functions. Each key has exactly two possible positions.

```
Table 1 (h1)     Table 2 (h2)
[0]              [0] k1
[1] k2           [1]
[2]              [2] k3
[3] k4           [3]

Insert k5:
- If T1[h1(k5)] empty: insert there
- If T2[h2(k5)] empty: insert there
- Else: kick out existing key and relocate it
```

**Implementation Sketch:**
```python
def insert(key, value):
    for _ in range(MAX_KICKS):
        idx1 = h1(key) % capacity
        if table1[idx1] is None:
            table1[idx1] = (key, value)
            return

        idx2 = h2(key) % capacity
        if table2[idx2] is None:
            table2[idx2] = (key, value)
            return

        # Kick out from table1 and relocate
        key, value, table1[idx1] = table1[idx1][0], table1[idx1][1], (key, value)

        # Try to place kicked key in table2
        idx2 = h2(key) % capacity
        if table2[idx2] is None:
            table2[idx2] = (key, value)
            return

        # Kick from table2 and continue
        key, value, table2[idx2] = table2[idx2][0], table2[idx2][1], (key, value)

    # Too many kicks - need to rehash
    rehash_with_new_functions()
    insert(key, value)
```

**Complexity:**
| Operation | Worst Case | Amortized |
|-----------|------------|-----------|
| Lookup | O(1) | O(1) |
| Insert | O(n) | O(1) |
| Delete | O(1) | O(1) |

**Advantages:**
- Guaranteed O(1) worst-case lookup
- No clustering
- High space utilization possible (~93%)

**Disadvantages:**
- Insert can trigger cascading relocations
- May need rehash if cycle detected
- More complex implementation

### 4. Dynamic Resizing

**When to Resize:**
- Load factor exceeds threshold (typically 0.75 for chaining, 0.5 for open addressing)
- Too many tombstones in open addressing

**Resize Strategy:**
```python
def _resize(self):
    old_buckets = self.buckets
    self.capacity *= 2  # or next prime
    self.buckets = [[] for _ in range(self.capacity)]
    self.size = 0

    for bucket in old_buckets:
        for key, value in bucket:
            self.put(key, value)  # Rehash all entries
```

**Amortized Analysis:**
- Doubling strategy: O(1) amortized insert
- Total work for n inserts: O(n + n/2 + n/4 + ...) = O(2n) = O(n)

### 5. Comparison Matrix

| Strategy | Avg Lookup | Worst Lookup | Cache Friendly | Delete Easy | Load Factor |
|----------|------------|--------------|----------------|-------------|-------------|
| Chaining | O(1+α) | O(n) | No | Yes | >1 OK |
| Linear Probing | O(1) | O(n) | Yes | Tombstone | <0.7 |
| Quadratic | O(1) | O(n) | Moderate | Tombstone | <0.7 |
| Double Hashing | O(1) | O(n) | No | Tombstone | <0.7 |
| Cuckoo | O(1) | O(1) | Moderate | Yes | <0.5 |

### 6. Decision Framework

```
Choose Collision Strategy:
│
├─ Need O(1) worst-case lookup?
│  └─ YES → Cuckoo Hashing
│
├─ Memory constrained + cache matters?
│  └─ YES → Linear Probing (keep α < 0.5)
│
├─ Expect many deletions?
│  └─ YES → Separate Chaining
│
├─ High load factor needed?
│  └─ YES → Separate Chaining with trees
│
├─ Simple implementation priority?
│  └─ YES → Separate Chaining or Linear Probing
│
└─ Default → Separate Chaining (most flexible)
```

## Expected Output

When designing a hash table, provide:

1. **Requirements Summary**
   - Key type and distribution
   - Operation frequencies
   - Constraints

2. **Hash Function Selection**
   - Chosen function with justification
   - Expected distribution quality
   - Implementation code

3. **Collision Strategy**
   - Selected strategy with rationale
   - Implementation code
   - Complexity analysis

4. **Sizing Policy**
   - Initial capacity
   - Load factor threshold
   - Resize strategy

5. **Performance Analysis**
   - Expected operation costs
   - Memory overhead
   - Worst-case scenarios

## Example: Design Hash Table for URL Shortener

**Requirements:**
- Keys: Short codes (6-10 alphanumeric characters)
- Operations: 95% lookups, 5% inserts, rare deletes
- Size: 100M URLs expected
- Latency: P99 < 1ms for lookups

**Analysis:**
- Read-heavy → optimize for lookup
- Rare deletes → tombstones acceptable
- String keys → need good string hash
- Large scale → memory efficiency matters

**Recommendation:**

**Hash Function:** FNV-1a (fast, good distribution for strings)
```python
def hash_short_code(code):
    h = 2166136261
    for c in code:
        h ^= ord(c)
        h = (h * 16777619) & 0xFFFFFFFF
    return h
```

**Collision Strategy:** Linear Probing
- Best cache locality for read-heavy workload
- Keep load factor at 0.5 for fast probes
- 100M URLs → 200M buckets → ~1.6GB for 8-byte entries

**Alternative for Distributed:**
- Consistent hashing across nodes
- Local hash tables with cuckoo hashing for guaranteed O(1)

## Quality Checklist

- [ ] Hash function distributes keys uniformly
- [ ] Collision strategy matches workload
- [ ] Load factor threshold is appropriate
- [ ] Resize strategy is implemented
- [ ] Deletion handling is correct
- [ ] Edge cases handled (empty, full, all collisions)
- [ ] Thread safety considered (if needed)

## Techniques Used

- **ST-01** (Clear Objective Statement) - Define hash table requirements
- **ST-02** (Structured Sequential Instructions) - Design process
- **RT-02** (Multi-Dimensional Analysis) - Compare strategies
- **RT-03** (Tree of Thoughts) - Decision framework
- **RT-05** (Evidence-Based Reasoning) - Complexity-based selection
- **DS-06** (Prioritization Guidance) - Trade-off analysis
- **ST-03** (Output Format Templates) - Consistent format

## Related Prompts

- `algorithms_data_structure_selection.md` - Choosing data structures
- `algorithms_complexity_analysis.md` - Analyzing hash table performance
- `code-analysis/performance/performance_bottleneck_identification.md` - Hash table optimization

## Customization Guide

**For Database Index:**
- Focus on disk-friendly hash functions
- Consider extendible hashing for growth
- Implement bucket overflow handling

**For Cache Implementation:**
- Add LRU/LFU eviction policy
- Consider clock algorithm for approximation
- Implement TTL-based expiration

**For Distributed Systems:**
- Implement consistent hashing
- Consider jump hash for balanced distribution
- Handle node addition/removal gracefully
