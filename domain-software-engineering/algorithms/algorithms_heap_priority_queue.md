---
title: "Heap and Priority Queue Applications"
category: algorithms
description: "Framework for implementing heaps and solving problems using priority queues, including variants and advanced applications"
tags:
  - algorithms
  - data-structures
  - heap
  - priority-queue
  - scheduling
  - graph-algorithms
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-01  # Chain-of-Thought
  - RT-02  # Multi-Dimensional Analysis
  - ST-03  # Output Format Templates
  - DS-03  # Tool and Methodology Suggestions
difficulty: intermediate
version: "1.0"
updated: 2026-01-23
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_scheduling_problem_solver.md
---

# Heap and Priority Queue Applications

**Objective:** Understand heap data structures, implement efficient priority queues, and apply them to solve scheduling, selection, and graph algorithm problems.

**When to Use:** Use this prompt when problems require repeatedly finding/removing minimum or maximum elements, implementing efficient scheduling systems, solving graph problems like Dijkstra's algorithm, or when you need a data structure that maintains partial ordering efficiently.

## Instructions

### 1. Problem Recognition

Identify if a heap/priority queue is appropriate:

**Heap Indicator Patterns:**
```
✓ "Find the k largest/smallest elements"
✓ "Continuously process highest/lowest priority item"
✓ "Merge k sorted lists"
✓ "Find median of streaming data"
✓ "Schedule tasks by priority"
✓ "Dijkstra's shortest path"
✓ "Prim's minimum spanning tree"
✓ "Huffman coding"
✓ "Event-driven simulation"
```

**Key Question:** Do you need fast access to extreme (min or max) element while also supporting insertions?

### 2. Heap Fundamentals

#### Binary Heap Structure

**Definition:** Complete binary tree where parent-child relationship satisfies heap property.

**Min-Heap Property:** Parent ≤ Children (root is minimum)
**Max-Heap Property:** Parent ≥ Children (root is maximum)

**Array Representation:**
```
For node at index i (0-indexed):
- Parent: (i - 1) / 2
- Left child: 2*i + 1
- Right child: 2*i + 2

Visual (Min-Heap):
        1
       / \
      3   2
     / \ / \
    7  4 5  6

Array: [1, 3, 2, 7, 4, 5, 6]
Index:  0  1  2  3  4  5  6
```

**Complexity:**
| Operation | Time | Notes |
|-----------|------|-------|
| find-min/max | O(1) | Root element |
| insert | O(log n) | Bubble up |
| extract-min/max | O(log n) | Remove root, heapify |
| decrease/increase-key | O(log n) | Bubble up/down |
| build-heap | O(n) | Bottom-up construction |
| heapify | O(log n) | Restore heap property |
| Space | O(n) | Array storage |

### 3. Core Operations Implementation

#### Min-Heap Implementation

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        """Add element and bubble up to maintain heap property."""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        """Move element up until heap property is satisfied."""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        """Remove and return minimum element."""
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, i):
        """Move element down until heap property is satisfied."""
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self._heapify_down(smallest)

    def peek(self):
        """Return minimum without removing."""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def decrease_key(self, i, new_val):
        """Decrease value at index i and restore heap property."""
        if new_val > self.heap[i]:
            raise ValueError("New value is greater than current")
        self.heap[i] = new_val
        self._bubble_up(i)

    @staticmethod
    def build_heap(arr):
        """Build heap from array in O(n) time."""
        heap = MinHeap()
        heap.heap = arr[:]
        # Start from last non-leaf and heapify down
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap._heapify_down(i)
        return heap
```

#### Heap Sort

```python
def heap_sort(arr):
    """Sort array using heap - O(n log n) time, O(1) space."""
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify_max(arr, i, 0)  # Heapify reduced heap

def heapify_max(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)
```

### 4. Heap Variants

#### Indexed Heap (with decrease-key support)

**Use case:** Dijkstra's algorithm, Prim's algorithm - need to update priorities of existing elements.

```python
class IndexedMinHeap:
    """Heap with O(log n) decrease-key operation."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [None] * capacity     # heap[i] = node ID
        self.index = [-1] * capacity       # index[nodeID] = position in heap
        self.keys = [float('inf')] * capacity  # keys[nodeID] = priority

    def contains(self, node_id):
        return self.index[node_id] != -1

    def insert(self, node_id, key):
        if self.contains(node_id):
            raise ValueError("Node already in heap")

        self.heap[self.size] = node_id
        self.index[node_id] = self.size
        self.keys[node_id] = key
        self._bubble_up(self.size)
        self.size += 1

    def decrease_key(self, node_id, new_key):
        if not self.contains(node_id):
            raise ValueError("Node not in heap")
        if new_key > self.keys[node_id]:
            raise ValueError("New key is larger")

        self.keys[node_id] = new_key
        self._bubble_up(self.index[node_id])

    def extract_min(self):
        if self.size == 0:
            raise IndexError("Heap is empty")

        min_node = self.heap[0]
        self.size -= 1

        if self.size > 0:
            self.heap[0] = self.heap[self.size]
            self.index[self.heap[0]] = 0
            self._heapify_down(0)

        self.index[min_node] = -1
        return min_node, self.keys[min_node]

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.keys[self.heap[i]] < self.keys[self.heap[parent]]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _heapify_down(self, i):
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < self.size and self.keys[self.heap[left]] < self.keys[self.heap[smallest]]:
                smallest = left
            if right < self.size and self.keys[self.heap[right]] < self.keys[self.heap[smallest]]:
                smallest = right

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def _swap(self, i, j):
        self.index[self.heap[i]] = j
        self.index[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
```

#### D-ary Heap

**Concept:** Each node has d children instead of 2.

**Trade-offs:**
- Decrease-key faster: O(log_d n) bubble-up
- Extract-min slower: O(d * log_d n) heapify-down
- Better for decrease-key heavy workloads (Dijkstra)
- d = 4 often optimal in practice

#### Fibonacci Heap

**Complexity (amortized):**
| Operation | Binary Heap | Fibonacci Heap |
|-----------|-------------|----------------|
| insert | O(log n) | O(1) |
| find-min | O(1) | O(1) |
| extract-min | O(log n) | O(log n) |
| decrease-key | O(log n) | O(1) |
| merge | O(n) | O(1) |

**When to use:** Theory (Dijkstra optimal), rarely in practice due to high constants.

#### Pairing Heap

- Simpler than Fibonacci heap
- Good practical performance
- O(1) insert, O(log n) amortized extract-min
- Recommended when Fibonacci heap seems overkill

### 5. Common Applications

#### Application 1: K Largest/Smallest Elements

**Problem:** Find k largest elements from n elements.

**Approach 1: Min-heap of size k (O(n log k))**
```python
import heapq

def k_largest(nums, k):
    """Use min-heap of size k."""
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)  # pop and push

    return sorted(min_heap, reverse=True)
```

**Approach 2: Quickselect (O(n) average)**
Better for single query, heap better for streaming.

---

#### Application 2: Merge K Sorted Lists

**Problem:** Merge k sorted lists into one sorted list.

```python
import heapq

def merge_k_sorted(lists):
    """O(n log k) where n = total elements, k = number of lists."""
    result = []
    # Heap entries: (value, list_index, element_index)
    heap = []

    # Initialize with first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

---

#### Application 3: Running Median

**Problem:** Maintain median as numbers stream in.

```python
import heapq

class MedianFinder:
    """Two heaps: max-heap for lower half, min-heap for upper half."""

    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap

    def add_num(self, num):
        # Add to appropriate heap
        if not self.lo or num <= -self.lo[0]:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)

        # Balance heaps (lo can have at most 1 more than hi)
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

---

#### Application 4: Dijkstra's Shortest Path

```python
import heapq

def dijkstra(graph, start):
    """O((V + E) log V) with binary heap."""
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    heap = [(0, start)]  # (distance, vertex)
    visited = set()

    while heap:
        d, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if v not in visited and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))

    return dist
```

---

#### Application 5: Task Scheduling

**Problem:** Schedule tasks with deadlines and profits.

```python
import heapq

def schedule_tasks(tasks):
    """
    Tasks: [(deadline, profit), ...]
    Maximize profit by scheduling one task per time slot.
    """
    # Sort by deadline
    tasks.sort(key=lambda x: x[0])

    max_heap = []  # Profits of scheduled tasks (negated)
    time = 0

    for deadline, profit in tasks:
        if time < deadline:
            # Can schedule this task
            heapq.heappush(max_heap, -profit)
            time += 1
        elif max_heap and -max_heap[0] < profit:
            # Replace least profitable task
            heapq.heapreplace(max_heap, -profit)

    return -sum(max_heap)  # Total profit
```

---

#### Application 6: Huffman Coding

```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """Build Huffman tree for optimal prefix-free encoding."""
    freq = Counter(text)

    # Create leaf nodes and add to heap
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # Build tree by combining lowest frequency nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None
```

### 6. Decision Framework

```
When to use heap/priority queue:
│
├─ Need repeated min/max extraction?
│  └─ YES → Binary heap
│
├─ Also need decrease-key frequently?
│  ├─ Graph algorithms → Indexed heap or Fibonacci heap
│  └─ Other → Consider indexed heap
│
├─ Need to merge heaps?
│  └─ YES → Binomial or Fibonacci heap
│
├─ K largest/smallest from stream?
│  └─ YES → Heap of size k
│
├─ Maintain median?
│  └─ YES → Two heaps (max-heap + min-heap)
│
├─ Event-driven simulation?
│  └─ YES → Min-heap of events by time
│
└─ Simple priority scheduling?
   └─ YES → Standard binary heap
```

## Expected Output

When solving a heap problem, provide:

1. **Problem Analysis**
   - Why heap is appropriate
   - Min-heap vs max-heap decision
   - Any special requirements (decrease-key, merge)

2. **Solution Design**
   - Heap variant selection
   - Algorithm description
   - State maintained in heap

3. **Implementation**
   - Clean, commented code
   - Edge case handling
   - Correct heap usage

4. **Complexity Analysis**
   - Time: operation breakdown
   - Space: heap size bounds

## Quality Checklist

- [ ] Heap property maintained after all operations
- [ ] Correct choice of min-heap vs max-heap
- [ ] Efficient use of heapify for initialization
- [ ] Edge cases handled (empty heap, single element)
- [ ] Complexity is optimal for the problem
- [ ] Library heap used correctly (heapq is min-heap)

## Techniques Used

- **ST-01** (Clear Objective Statement) - Define heap problem
- **ST-02** (Structured Sequential Instructions) - Implementation steps
- **RT-01** (Chain-of-Thought) - Trace heap operations
- **RT-02** (Multi-Dimensional Analysis) - Compare heap variants
- **ST-03** (Output Format Templates) - Consistent solution format
- **DS-03** (Tool and Methodology Suggestions) - Library usage

## Related Prompts

- `algorithms_data_structure_selection.md` - Choosing structures
- `algorithms_graph_problem_solver.md` - Graph algorithms using heaps
- `algorithms_scheduling_problem_solver.md` - Scheduling with priority queues

## Customization Guide

**For Interview Preparation:**
- Know heap property and operations by heart
- Practice implementing heap from scratch
- Master k-largest/smallest pattern
- Understand heap vs BST trade-offs

**For System Design:**
- Consider thread-safe priority queues
- Distributed priority queues (Redis, Kafka)
- Memory-bounded heaps with eviction

**For Competitive Programming:**
- Use language's priority queue library
- Know how to handle custom comparators
- Practice dual-heap median pattern
