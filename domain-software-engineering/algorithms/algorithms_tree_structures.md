---
title: "Tree Data Structures Problem Solver"
category: algorithms
description: "Framework for implementing, analyzing, and applying tree data structures including BST, AVL, Red-Black, and B-trees"
tags:
  - algorithms
  - data-structures
  - trees
  - binary-search-tree
  - balanced-trees
  - interview-prep
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-01  # Chain-of-Thought
  - RT-02  # Multi-Dimensional Analysis
  - RT-04  # Analogical Reasoning
  - ST-03  # Output Format Templates
  - ED-01  # Iterative Scaffolding
difficulty: intermediate-advanced
version: "1.0"
updated: 2026-01-23
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_complexity_analysis.md
---

# Tree Data Structures Problem Solver

**Objective:** Analyze tree-based data structure problems, select the appropriate tree variant, and implement efficient solutions with proper balancing and optimization.

**When to Use:** Use this prompt when working with hierarchical data, implementing ordered collections, building database indices, solving problems requiring efficient search/insert/delete operations, or preparing for technical interviews involving tree structures.

## Instructions

### 1. Problem Classification

First, classify the problem to determine which tree structure is most appropriate:

**Access Pattern Analysis:**
```
What operations are most frequent?
├── Search dominant → BST family (BST, AVL, Red-Black)
├── Range queries → B-Tree, B+ Tree, or Augmented BST
├── Prefix/string operations → Trie (separate prompt)
├── Interval queries → Interval Tree
├── Multi-dimensional → K-D Tree
└── Disk-based storage → B-Tree, B+ Tree
```

**Balance Requirements:**
```
How important is worst-case guarantee?
├── Average case OK, simple implementation → Basic BST
├── Must have O(log n) guarantee → Balanced tree required
│   ├── Strict balance needed → AVL Tree
│   ├── Frequent modifications → Red-Black Tree
│   └── Disk I/O optimization → B-Tree
└── Amortized OK → Splay Tree
```

### 2. Tree Structure Reference

#### Binary Search Tree (BST)

**Core Property:** For every node N:
- All values in left subtree < N.value
- All values in right subtree > N.value

**Complexity:**
| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Space | O(n) | O(n) |

**Implementation Pattern:**
```
Node Structure:
- value: comparable data
- left: pointer to left child
- right: pointer to right child
- (optional) parent: pointer to parent

Key Operations:
1. Search: Compare and recurse left/right
2. Insert: Search for position, add leaf
3. Delete: Three cases
   - Leaf: Simply remove
   - One child: Replace with child
   - Two children: Replace with successor/predecessor
4. Traversal: In-order gives sorted sequence
```

**When to Use BST:**
- Simple ordered data with mostly balanced input
- Educational purposes
- Building block for other structures
- When average case is acceptable

**When to Avoid BST:**
- Sorted input (degenerates to linked list)
- Need guaranteed O(log n)
- High-frequency modifications

---

#### AVL Tree

**Core Property:** BST + Height-balanced
- For every node: |height(left) - height(right)| <= 1
- Strictly balanced = faster lookups

**Balance Factor:** height(left subtree) - height(right subtree)
- Valid values: -1, 0, +1

**Complexity:**
| Operation | Time | Notes |
|-----------|------|-------|
| Search | O(log n) | Guaranteed |
| Insert | O(log n) | 1-2 rotations max |
| Delete | O(log n) | O(log n) rotations possible |
| Space | O(n) | Extra: height/balance per node |

**Rotation Operations:**
```
Right Rotation (LL case):     Left Rotation (RR case):
      y                            x
     / \                          / \
    x   T3   →    x              T1   y
   / \           / \                 / \
  T1  T2        T1  y               T2  T3
                   / \
                  T2  T3

Left-Right (LR):              Right-Left (RL):
First left rotate on x,       First right rotate on y,
then right rotate on y        then left rotate on x
```

**Insertion Algorithm:**
```
1. Standard BST insert
2. Update heights bottom-up
3. Check balance factor at each ancestor
4. If |BF| > 1, determine case and rotate:
   - BF > 1 and key < left.key → Right rotate (LL)
   - BF > 1 and key > left.key → Left-Right rotate (LR)
   - BF < -1 and key > right.key → Left rotate (RR)
   - BF < -1 and key < right.key → Right-Left rotate (RL)
```

**When to Use AVL:**
- Lookup-heavy workloads (more reads than writes)
- Need strict O(log n) guarantee
- Database indexing (read-optimized)
- Applications where tree height matters

**When to Avoid AVL:**
- Write-heavy workloads (frequent rebalancing)
- Memory constrained (needs height storage)
- Simpler solution acceptable

---

#### Red-Black Tree

**Core Properties:**
1. Every node is Red or Black
2. Root is Black
3. All leaves (NIL) are Black
4. Red node's children must be Black (no red-red)
5. All paths from node to descendant NIL have same black count

**Key Insight:** Less strictly balanced than AVL, but rebalancing is cheaper.

**Complexity:**
| Operation | Time | Notes |
|-----------|------|-------|
| Search | O(log n) | Guaranteed |
| Insert | O(log n) | Max 2 rotations |
| Delete | O(log n) | Max 3 rotations |
| Space | O(n) | Extra: 1 bit per node for color |

**Height Bounds:**
- Maximum height: 2 * log₂(n + 1)
- AVL height: ~1.44 * log₂(n)
- Red-Black is slightly taller but rebalances faster

**Insertion Cases:**
```
After standard BST insert (new node is Red):

Case 1: Uncle is Red
→ Recolor parent, uncle, grandparent
→ Move problem up (grandparent becomes new focus)

Case 2: Uncle is Black, node is inner child
→ Rotate to make it Case 3

Case 3: Uncle is Black, node is outer child
→ Rotate and recolor

Key insight: At most 2 rotations needed for insert
```

**When to Use Red-Black:**
- Balanced read/write workloads
- Standard library implementations (Java TreeMap, C++ std::map)
- When simpler rebalancing logic is preferred
- General-purpose ordered map/set

**When to Avoid Red-Black:**
- Pure lookup workloads (AVL slightly faster)
- Need simpler conceptual model
- Memory extremely constrained (color bit overhead)

---

#### B-Tree

**Core Properties:**
- Multi-way search tree (not binary)
- All leaves at same level
- Node has between t-1 and 2t-1 keys (t = minimum degree)
- Root can have minimum 1 key

**Structure:**
```
Node with keys k₁, k₂, ..., kₙ has n+1 children:
- Child 0: all keys < k₁
- Child i: keys between kᵢ and kᵢ₊₁
- Child n: all keys > kₙ
```

**Complexity:**
| Operation | Time | Disk I/O |
|-----------|------|----------|
| Search | O(log n) | O(log_t n) |
| Insert | O(log n) | O(log_t n) |
| Delete | O(log n) | O(log_t n) |
| Space | O(n) | |

**Why B-Trees for Disk:**
- Large branching factor = fewer levels = fewer disk seeks
- Node size matches disk block size
- Typically t chosen so node fits in one disk page (e.g., 4KB)

**Insertion Algorithm:**
```
1. Search for appropriate leaf
2. If leaf has room (< 2t-1 keys): insert and done
3. If leaf is full: split
   - Middle key moves up to parent
   - Node splits into two nodes with t-1 keys each
   - Recursively split parent if needed
4. If root splits: tree grows one level
```

**When to Use B-Tree:**
- Database indexing
- File systems
- Any disk-based storage
- When minimizing I/O operations matters

---

#### B+ Tree

**Difference from B-Tree:**
- All data stored in leaves only
- Internal nodes only store keys (routing)
- Leaves are linked (sequential access)

**Advantages over B-Tree:**
- More keys per internal node = shorter tree
- Range queries traverse linked leaves
- Full scans don't need internal nodes

**When to Use B+ Tree:**
- Range queries are common
- Sequential access patterns
- Database systems (most use B+ trees)

### 3. Problem-Solving Framework

When given a tree problem, follow this approach:

**Step 1: Identify the Core Challenge**
```
Common tree problem types:
- Traversal: Process nodes in specific order
- Search: Find nodes meeting criteria
- Modification: Insert, delete, update
- Construction: Build tree from data
- Verification: Check tree properties
- Transformation: Convert between representations
- Path problems: Find paths with properties
- Subtree problems: Operations on subtrees
```

**Step 2: Choose Traversal Strategy**
```
In-order (LNR): Sorted sequence for BST
Pre-order (NLR): Copy tree, serialize
Post-order (LRN): Delete tree, evaluate expressions
Level-order (BFS): Level-by-level processing
Morris Traversal: O(1) space traversal
```

**Step 3: Identify Required Augmentation**
```
Common augmentations:
- Size: Count of subtree nodes (order statistics)
- Height: For balancing, diameter calculations
- Sum: Subtree sum for range queries
- Parent pointer: For upward traversal
- Min/Max: Subtree extremes
```

**Step 4: Consider Edge Cases**
```
Always handle:
- Empty tree (root is null)
- Single node tree
- Unbalanced/skewed tree
- Duplicate values (if allowed)
- Overflow/underflow during operations
```

### 4. Implementation Templates

**BST Node Template:**
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # Optional augmentations:
        # self.parent = None
        # self.size = 1
        # self.height = 0
```

**Recursive Search Template:**
```
def search(node, target):
    if node is None:
        return None
    if target == node.val:
        return node
    if target < node.val:
        return search(node.left, target)
    else:
        return search(node.right, target)
```

**Iterative Search Template:**
```
def search_iterative(root, target):
    current = root
    while current is not None:
        if target == current.val:
            return current
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return None
```

**In-order Traversal (Iterative):**
```
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```

### 5. Analysis Template

For each tree solution, document:

```markdown
## Solution Analysis

### Approach
[Describe the algorithm in plain language]

### Tree Type Selected
[BST/AVL/Red-Black/B-Tree] because:
- [Reason 1]
- [Reason 2]

### Complexity Analysis
- Time: O(?) because [reasoning]
- Space: O(?) because [reasoning]
- Amortized considerations: [if applicable]

### Key Invariants Maintained
1. [Property 1 maintained by...]
2. [Property 2 maintained by...]

### Edge Cases Handled
- Empty tree: [how handled]
- Single node: [how handled]
- [Other cases]: [how handled]

### Potential Optimizations
- [Optimization 1]
- [Optimization 2]
```

## Expected Output

When solving a tree problem, provide:

1. **Problem Analysis**
   - Classification of problem type
   - Appropriate tree structure selection
   - Required operations identified

2. **Solution Design**
   - Algorithm description
   - Tree variant choice with justification
   - Augmentation requirements

3. **Implementation**
   - Clean, commented code
   - Key helper functions
   - Proper null/edge case handling

4. **Complexity Analysis**
   - Time complexity with reasoning
   - Space complexity breakdown
   - Best/worst/average case if different

5. **Testing Strategy**
   - Edge cases to test
   - Example inputs and expected outputs

## Example Problem: Kth Smallest Element in BST

**Problem:** Given a BST, find the kth smallest element.

**Analysis:**
- Problem type: Search/Order statistics
- Tree type: BST (given)
- Key insight: In-order traversal of BST gives sorted order

**Approach 1: In-order Traversal**
```python
def kth_smallest(root, k):
    # In-order traversal counts nodes until k
    count = [0]  # Mutable container for closure
    result = [None]

    def inorder(node):
        if not node or result[0] is not None:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]
```
- Time: O(H + k) where H is height
- Space: O(H) for recursion stack

**Approach 2: Augmented BST (if frequent queries)**
```python
# Augment nodes with subtree size
# Then: if left.size == k-1, return node
#       if left.size >= k, recurse left
#       else recurse right with k -= left.size + 1
```
- Time: O(H) per query
- Space: O(1) per query, O(n) for augmentation

**Recommendation:**
- Single query: Approach 1
- Frequent queries: Approach 2 with augmentation

## Quality Checklist

Before finalizing a tree solution:

- [ ] BST property maintained after modifications
- [ ] Balance property preserved (for balanced trees)
- [ ] All rotations correctly implemented
- [ ] Null pointers handled gracefully
- [ ] Parent pointers updated (if used)
- [ ] Augmented data updated correctly
- [ ] Edge cases tested
- [ ] Complexity analysis complete

## Techniques Used

- **ST-01** (Clear Objective Statement) - Define tree problem clearly
- **ST-02** (Structured Sequential Instructions) - Step-by-step solving
- **RT-01** (Chain-of-Thought) - Trace through tree operations
- **RT-02** (Multi-Dimensional Analysis) - Compare tree variants
- **RT-04** (Analogical Reasoning) - Relate to familiar patterns
- **ST-03** (Output Format Templates) - Consistent solution format
- **ED-01** (Iterative Scaffolding) - Build understanding progressively

## Related Prompts

- `algorithms_data_structure_selection.md` - Choosing the right structure
- `algorithms_complexity_analysis.md` - Analyzing tree algorithms
- `algorithms_trie_string_matching.md` - Trie-based solutions
- `learning/learning_algorithmic_storytelling.md` - Teaching tree concepts

## Customization Guide

**For Interview Preparation:**
- Practice implementing rotations from memory
- Know when to choose AVL vs Red-Black
- Be ready to augment BST for order statistics
- Practice common patterns: LCA, diameter, balanced check

**For Database Development:**
- Focus on B-Tree and B+ Tree
- Understand page splits and merges
- Consider concurrent access patterns
- Study index optimization

**For Competitive Programming:**
- Memorize Fenwick tree and segment tree templates
- Know augmentation patterns for range queries
- Practice tree DP problems
- Study Euler tour technique
