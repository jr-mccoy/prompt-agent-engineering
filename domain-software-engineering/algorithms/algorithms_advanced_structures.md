---
title: "Advanced Data Structures: Segment Trees, Fenwick Trees, and Beyond"
category: algorithms
description: "Framework for implementing advanced data structures for range queries, interval operations, and specialized algorithmic problems"
tags:
  - algorithms
  - data-structures
  - segment-tree
  - fenwick-tree
  - range-queries
  - competitive-programming
  - advanced
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-01  # Chain-of-Thought
  - RT-02  # Multi-Dimensional Analysis
  - ST-03  # Output Format Templates
  - DS-03  # Tool and Methodology Suggestions
difficulty: advanced
version: "1.0"
updated: 2026-01-23
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_tree_structures.md
---

# Advanced Data Structures: Segment Trees, Fenwick Trees, and Beyond

**Objective:** Implement and apply advanced data structures for efficiently solving range query problems, interval operations, and specialized algorithmic challenges.

**When to Use:** Use this prompt when problems require efficient range queries (sum, min, max), range updates, finding intervals, geometric queries, or when standard data structures are insufficient for the required time complexity.

## Instructions

### 1. Problem Classification

Identify the appropriate advanced structure:

**Query Type Analysis:**
```
Range Query Problems:
├── Point update + Range query
│   ├── Range sum → Fenwick Tree (BIT) or Segment Tree
│   ├── Range min/max → Segment Tree
│   └── Range GCD/LCM → Segment Tree
│
├── Range update + Point query
│   └── Fenwick Tree with difference array
│
├── Range update + Range query
│   ├── Add on range → Segment Tree with lazy propagation
│   └── Set on range → Segment Tree with lazy propagation
│
├── 2D range queries
│   ├── Static → 2D Fenwick Tree or 2D Segment Tree
│   └── Dynamic → Nested structures
│
└── Specialized queries
    ├── Interval stabbing → Interval Tree
    ├── Rectangle intersection → R-tree / K-D Tree
    └── Orthogonal range search → Range Tree
```

**Decision Quick Reference:**
| Problem Type | Best Structure | Complexity |
|--------------|----------------|------------|
| Point update, range sum | Fenwick Tree | O(log n) |
| Point update, range min/max | Segment Tree | O(log n) |
| Range update, range query | Segment Tree + Lazy | O(log n) |
| Count in range | Merge Sort Tree / Wavelet Tree | O(log² n) |
| Interval overlap | Interval Tree | O(log n + k) |

### 2. Fenwick Tree (Binary Indexed Tree)

#### Concept

**Key Insight:** Each index stores partial sum based on lowest set bit (LSB).

```
Array:    [-, 1, 2, 3, 4, 5, 6, 7, 8]  (1-indexed)
BIT:      [-, 1, 3, 3, 10, 5, 11, 7, 36]

Index 1: stores sum of [1, 1]     (LSB = 1)
Index 2: stores sum of [1, 2]     (LSB = 2)
Index 3: stores sum of [3, 3]     (LSB = 1)
Index 4: stores sum of [1, 4]     (LSB = 4)
Index 5: stores sum of [5, 5]     (LSB = 1)
Index 6: stores sum of [5, 6]     (LSB = 2)
Index 7: stores sum of [7, 7]     (LSB = 1)
Index 8: stores sum of [1, 8]     (LSB = 8)
```

**LSB Trick:** `i & (-i)` gives lowest set bit

#### Implementation

```python
class FenwickTree:
    """Binary Indexed Tree for range sum queries."""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        """Add delta to index i. O(log n)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Move to next responsible node

    def prefix_sum(self, i):
        """Sum of [1, i]. O(log n)."""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # Move to parent
        return total

    def range_sum(self, left, right):
        """Sum of [left, right]. O(log n)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    @classmethod
    def from_array(cls, arr):
        """Build from array in O(n)."""
        n = len(arr)
        bit = cls(n)
        bit.tree[1:] = arr[:]

        for i in range(1, n + 1):
            j = i + (i & (-i))
            if j <= n:
                bit.tree[j] += bit.tree[i]

        return bit
```

#### Fenwick Tree Variants

**Range Update, Point Query:**
```python
class FenwickTreeRangeUpdate:
    """Support range add, point query using difference array."""

    def __init__(self, n):
        self.bit = FenwickTree(n)

    def range_add(self, left, right, delta):
        """Add delta to all elements in [left, right]."""
        self.bit.update(left, delta)
        if right + 1 <= self.bit.n:
            self.bit.update(right + 1, -delta)

    def point_query(self, i):
        """Get value at index i."""
        return self.bit.prefix_sum(i)
```

**2D Fenwick Tree:**
```python
class FenwickTree2D:
    """2D BIT for rectangle sum queries."""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, r, c, delta):
        """Add delta at (r, c). O(log r * log c)."""
        i = r
        while i <= self.rows:
            j = c
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def prefix_sum(self, r, c):
        """Sum of rectangle [1,1] to [r,c]. O(log r * log c)."""
        total = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total

    def range_sum(self, r1, c1, r2, c2):
        """Sum of rectangle [r1,c1] to [r2,c2]."""
        return (self.prefix_sum(r2, c2)
                - self.prefix_sum(r1 - 1, c2)
                - self.prefix_sum(r2, c1 - 1)
                + self.prefix_sum(r1 - 1, c1 - 1))
```

### 3. Segment Tree

#### Concept

**Structure:** Binary tree where each node represents a range.
- Root represents [0, n-1]
- Each internal node splits range in half
- Leaves represent single elements

```
Array: [1, 3, 5, 7, 9, 11]

Segment Tree (sum):
              [36]           [0,5]
            /      \
        [9]        [27]      [0,2] [3,5]
       /   \       /   \
     [4]   [5]  [16]  [11]   [0,1] [2,2] [3,4] [5,5]
     / \         / \
   [1] [3]     [7] [9]
```

#### Basic Implementation

```python
class SegmentTree:
    """Segment tree for range minimum queries."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Sufficient size
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        """Build tree recursively. O(n)."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)

            self.tree[node] = min(self.tree[left_child], self.tree[right_child])

    def update(self, idx, val):
        """Update single element. O(log n)."""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if idx <= mid:
                self._update(left_child, start, mid, idx, val)
            else:
                self._update(right_child, mid + 1, end, idx, val)

            self.tree[node] = min(self.tree[left_child], self.tree[right_child])

    def query(self, left, right):
        """Range minimum query. O(log n)."""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # No overlap
        if right < start or end < left:
            return float('inf')

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_min = self._query(left_child, start, mid, left, right)
        right_min = self._query(right_child, mid + 1, end, left, right)

        return min(left_min, right_min)
```

#### Segment Tree with Lazy Propagation

**Use case:** Range updates (add value to entire range).

```python
class LazySegmentTree:
    """Segment tree with lazy propagation for range updates."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2*node+1, start, mid)
            self._build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def _push_down(self, node, start, end):
        """Propagate lazy value to children."""
        if self.lazy[node] != 0:
            mid = (start + end) // 2

            # Update children's tree values
            self.tree[2*node+1] += self.lazy[node] * (mid - start + 1)
            self.tree[2*node+2] += self.lazy[node] * (end - mid)

            # Pass lazy value to children
            self.lazy[2*node+1] += self.lazy[node]
            self.lazy[2*node+2] += self.lazy[node]

            # Clear current lazy value
            self.lazy[node] = 0

    def range_update(self, left, right, val):
        """Add val to all elements in [left, right]. O(log n)."""
        self._range_update(0, 0, self.n-1, left, right, val)

    def _range_update(self, node, start, end, left, right, val):
        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return

        self._push_down(node, start, end)

        mid = (start + end) // 2
        self._range_update(2*node+1, start, mid, left, right, val)
        self._range_update(2*node+2, mid+1, end, left, right, val)

        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def range_query(self, left, right):
        """Sum of [left, right]. O(log n)."""
        return self._range_query(0, 0, self.n-1, left, right)

    def _range_query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        self._push_down(node, start, end)

        mid = (start + end) // 2
        return (self._range_query(2*node+1, start, mid, left, right) +
                self._range_query(2*node+2, mid+1, end, left, right))
```

### 4. Interval Tree

**Use case:** Find all intervals that overlap with a query interval.

```python
class IntervalNode:
    def __init__(self, interval):
        self.interval = interval  # (low, high)
        self.max_end = interval[1]
        self.left = None
        self.right = None

class IntervalTree:
    """Store intervals and query overlapping intervals."""

    def __init__(self):
        self.root = None

    def insert(self, interval):
        """Insert interval (low, high). O(log n)."""
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):
        if node is None:
            return IntervalNode(interval)

        low = interval[0]
        if low < node.interval[0]:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        node.max_end = max(node.max_end, interval[1])
        return node

    def query_overlap(self, interval):
        """Find all intervals overlapping with query. O(log n + k)."""
        results = []
        self._query(self.root, interval, results)
        return results

    def _query(self, node, interval, results):
        if node is None:
            return

        # Check if current interval overlaps
        if self._overlaps(node.interval, interval):
            results.append(node.interval)

        # If left subtree could contain overlapping intervals
        if node.left and node.left.max_end >= interval[0]:
            self._query(node.left, interval, results)

        # If right subtree could contain overlapping intervals
        if node.right and node.interval[0] <= interval[1]:
            self._query(node.right, interval, results)

    def _overlaps(self, int1, int2):
        return int1[0] <= int2[1] and int2[0] <= int1[1]
```

### 5. Sparse Table

**Use case:** Static range minimum/maximum queries (no updates).

**Advantage:** O(1) query after O(n log n) preprocessing.

```python
import math

class SparseTable:
    """O(1) range minimum query for static arrays."""

    def __init__(self, arr):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self.k = int(math.log2(self.n)) + 1

        # Precompute logs
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        # sparse[i][j] = min of range starting at i with length 2^j
        self.sparse = [[0] * self.k for _ in range(self.n)]

        # Base case: ranges of length 1
        for i in range(self.n):
            self.sparse[i][0] = arr[i]

        # Build table
        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.sparse[i][j] = min(
                    self.sparse[i][j-1],
                    self.sparse[i + (1 << (j-1))][j-1]
                )

    def query(self, left, right):
        """Range minimum in O(1)."""
        length = right - left + 1
        k = self.log[length]
        return min(
            self.sparse[left][k],
            self.sparse[right - (1 << k) + 1][k]
        )
```

### 6. Disjoint Set Union (Union-Find)

**Use case:** Dynamic connectivity, component counting, cycle detection.

```python
class UnionFind:
    """Union-Find with path compression and union by rank."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        """Find root with path compression. Amortized O(α(n))."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union two sets. Amortized O(α(n))."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True

    def connected(self, x, y):
        """Check if x and y are in same set."""
        return self.find(x) == self.find(y)
```

### 7. Comparison Matrix

| Structure | Build | Point Update | Range Update | Point Query | Range Query | Space |
|-----------|-------|--------------|--------------|-------------|-------------|-------|
| Fenwick Tree | O(n) | O(log n) | O(log n)* | O(log n) | O(log n) | O(n) |
| Segment Tree | O(n) | O(log n) | O(log n)** | O(log n) | O(log n) | O(n) |
| Sparse Table | O(n log n) | N/A | N/A | O(1) | O(1) | O(n log n) |
| Interval Tree | O(n log n) | O(log n) | N/A | N/A | O(log n + k) | O(n) |

*With range-update variant
**With lazy propagation

### 8. Application Examples

#### Example 1: Count Inversions

```python
def count_inversions(arr):
    """Count pairs (i,j) where i < j and arr[i] > arr[j]."""
    # Coordinate compress values
    sorted_vals = sorted(set(arr))
    rank = {v: i+1 for i, v in enumerate(sorted_vals)}

    bit = FenwickTree(len(sorted_vals))
    inversions = 0

    # Process from right to left
    for val in reversed(arr):
        r = rank[val]
        inversions += bit.prefix_sum(r - 1)  # Count smaller seen
        bit.update(r, 1)

    return inversions
```

#### Example 2: Range Update, Range Sum

```python
# Using segment tree with lazy propagation
arr = [1, 3, 5, 7, 9]
st = LazySegmentTree(arr)

st.range_update(1, 3, 10)  # Add 10 to indices 1-3
print(st.range_query(0, 4))  # Sum of entire array
```

#### Example 3: Meeting Room Scheduling

```python
def min_meeting_rooms(intervals):
    """Find minimum rooms needed for all meetings."""
    events = []
    for start, end in intervals:
        events.append((start, 1))   # Meeting starts
        events.append((end, -1))    # Meeting ends

    events.sort()

    rooms = max_rooms = 0
    for _, delta in events:
        rooms += delta
        max_rooms = max(max_rooms, rooms)

    return max_rooms
```

### 9. Decision Framework

```
Advanced Structure Selection:
│
├─ Need range queries on static data?
│  └─ YES → Sparse Table (O(1) query)
│
├─ Need range sum with point updates?
│  └─ YES → Fenwick Tree (simpler)
│
├─ Need range min/max with point updates?
│  └─ YES → Segment Tree
│
├─ Need range updates AND range queries?
│  └─ YES → Segment Tree with Lazy Propagation
│
├─ Need to find overlapping intervals?
│  └─ YES → Interval Tree
│
├─ Need dynamic connectivity?
│  └─ YES → Union-Find
│
├─ 2D range queries?
│  └─ YES → 2D Fenwick Tree or 2D Segment Tree
│
└─ Count elements in range?
   └─ YES → Merge Sort Tree or Wavelet Tree
```

## Expected Output

When solving an advanced data structure problem:

1. **Problem Analysis**
   - Query/update type identification
   - Complexity requirements
   - Space constraints

2. **Structure Selection**
   - Chosen structure with justification
   - Why alternatives were rejected

3. **Implementation**
   - Complete, working code
   - Edge case handling
   - Template-ready for reuse

4. **Complexity Analysis**
   - Per-operation costs
   - Total complexity for problem

## Quality Checklist

- [ ] Correct structure for query type
- [ ] Lazy propagation implemented correctly (if needed)
- [ ] Edge cases handled (empty, single element)
- [ ] Index bounds correct (0-indexed vs 1-indexed)
- [ ] Tree size sufficient (4n for segment tree)
- [ ] Coordinate compression used if needed

## Techniques Used

- **ST-01** (Clear Objective Statement) - Define problem requirements
- **ST-02** (Structured Sequential Instructions) - Implementation steps
- **RT-01** (Chain-of-Thought) - Trace query operations
- **RT-02** (Multi-Dimensional Analysis) - Compare structures
- **ST-03** (Output Format Templates) - Consistent format
- **DS-03** (Tool and Methodology Suggestions) - Structure selection

## Related Prompts

- `algorithms_data_structure_selection.md` - Choosing structures
- `algorithms_tree_structures.md` - Tree fundamentals
- `algorithms_complexity_analysis.md` - Analyzing algorithms

## Customization Guide

**For Competitive Programming:**
- Memorize templates for BIT and Segment Tree
- Practice lazy propagation patterns
- Know when to use each structure instantly

**For Interview Preparation:**
- Focus on Fenwick Tree (simpler to implement)
- Understand segment tree concept without full implementation
- Practice union-find problems

**For Production Systems:**
- Consider thread-safety requirements
- Evaluate persistent versions for versioning
- Profile actual performance vs theoretical
