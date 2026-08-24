# Algorithms & Data Structures Prompts

This category contains prompts for classic computer science algorithms, data structures, and algorithmic problem-solving.

## Overview

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [algorithms_data_structure_selection.md](algorithms_data_structure_selection.md) | Systematic framework for selecting optimal data structures | Intermediate |
| [algorithms_tree_structures.md](algorithms_tree_structures.md) | BST, AVL, Red-Black, and B-trees implementation and analysis | Intermediate-Advanced |
| [algorithms_hash_table_design.md](algorithms_hash_table_design.md) | Hash table design and collision resolution strategies | Intermediate |
| [algorithms_heap_priority_queue.md](algorithms_heap_priority_queue.md) | Heaps and priority queue applications | Intermediate |
| [algorithms_trie_string_matching.md](algorithms_trie_string_matching.md) | Tries, suffix structures, and string matching | Intermediate-Advanced |
| [algorithms_advanced_structures.md](algorithms_advanced_structures.md) | Segment trees, Fenwick trees, and advanced structures | Advanced |

## Use Cases

### Data Structure Selection
Use `algorithms_data_structure_selection.md` when:
- Designing systems requiring efficient data storage and retrieval
- Choosing between multiple data structure options
- Preparing for system design interviews
- Optimizing existing code with performance issues

### Tree-Based Solutions
Use `algorithms_tree_structures.md` when:
- Implementing ordered collections
- Building database indices
- Solving problems requiring efficient search/insert/delete
- Working with hierarchical data

### Hash-Based Solutions
Use `algorithms_hash_table_design.md` when:
- Implementing custom hash tables or caches
- Optimizing lookup-heavy systems
- Solving symbol table problems
- Designing key-value stores

### Priority-Based Processing
Use `algorithms_heap_priority_queue.md` when:
- Finding k largest/smallest elements
- Implementing scheduling systems
- Solving graph problems (Dijkstra, Prim)
- Processing events by priority

### String Processing
Use `algorithms_trie_string_matching.md` when:
- Building autocomplete systems
- Implementing spell checkers
- Solving prefix-based problems
- Pattern matching in text

### Range Queries
Use `algorithms_advanced_structures.md` when:
- Processing range sum/min/max queries
- Handling range updates efficiently
- Solving interval overlap problems
- Working with dynamic connectivity

## Quick Reference: Problem → Prompt

| Problem Type | Recommended Prompt |
|--------------|-------------------|
| "Which data structure should I use?" | `algorithms_data_structure_selection.md` |
| "Implement balanced tree" | `algorithms_tree_structures.md` |
| "Design hash function" | `algorithms_hash_table_design.md` |
| "Find k largest elements" | `algorithms_heap_priority_queue.md` |
| "Autocomplete system" | `algorithms_trie_string_matching.md` |
| "Range sum queries" | `algorithms_advanced_structures.md` |
| "Maintain sorted order" | `algorithms_tree_structures.md` |
| "O(1) lookup by key" | `algorithms_hash_table_design.md` |
| "Prefix search" | `algorithms_trie_string_matching.md` |
| "Interval overlap" | `algorithms_advanced_structures.md` |

## Complexity Cheat Sheet

### Data Structure Operations

| Structure | Insert | Delete | Search | Min/Max | Space |
|-----------|--------|--------|--------|---------|-------|
| Array | O(n) | O(n) | O(n) | O(n) | O(n) |
| Sorted Array | O(n) | O(n) | O(log n) | O(1) | O(n) |
| Linked List | O(1)* | O(1)* | O(n) | O(n) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(n) | O(n) |
| BST | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) | O(n) |
| AVL/Red-Black | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Binary Heap | O(log n) | O(log n) | O(n) | O(1) | O(n) |
| Trie | O(m) | O(m) | O(m) | - | O(ALPHABET × n × m) |

*With pointer to location

### Advanced Structures

| Structure | Build | Point Update | Range Query | Range Update |
|-----------|-------|--------------|-------------|--------------|
| Fenwick Tree | O(n) | O(log n) | O(log n) | O(log n)* |
| Segment Tree | O(n) | O(log n) | O(log n) | O(log n)** |
| Sparse Table | O(n log n) | N/A | O(1) | N/A |

*With difference array technique
**With lazy propagation

## Learning Path

### Beginner
1. Start with `algorithms_data_structure_selection.md` to understand when to use what
2. Learn arrays, linked lists, stacks, queues fundamentals

### Intermediate
1. Master `algorithms_hash_table_design.md` for O(1) operations
2. Study `algorithms_heap_priority_queue.md` for priority-based processing
3. Learn basic BST from `algorithms_tree_structures.md`

### Advanced
1. Deep dive into balanced trees (AVL, Red-Black)
2. Master `algorithms_trie_string_matching.md` for string problems
3. Study `algorithms_advanced_structures.md` for competitive programming

## Interview Preparation Focus

### Data Structures You Must Know
1. **Hash Tables** - Most frequently asked
2. **Binary Trees/BST** - Traversals, search, balanced variants
3. **Heaps** - k-largest, merge sorted lists
4. **Tries** - Autocomplete, word search

### Common Interview Patterns
- Two-pointer technique
- Sliding window
- BFS/DFS on trees
- Heap for top-k problems
- Hash map for O(1) lookup
- Trie for prefix problems

## Related Categories

- `code-analysis/performance/` - Performance optimization
- `learning/` - Learning and teaching algorithms
- `engineering/` - System design with data structures

## Techniques Used

All prompts in this category use these core techniques:

- **ST-01** (Clear Objective Statement) - Define the algorithmic problem
- **ST-02** (Structured Sequential Instructions) - Step-by-step implementation
- **RT-01** (Chain-of-Thought) - Trace through algorithm execution
- **RT-02** (Multi-Dimensional Analysis) - Compare approaches
- **RT-05** (Evidence-Based Reasoning) - Complexity analysis
- **ST-03** (Output Format Templates) - Consistent solution format
- **DS-03** (Tool and Methodology Suggestions) - Algorithm selection

## Contributing

When adding new algorithm prompts:

1. Follow the naming convention: `algorithms_{topic}.md`
2. Include complexity analysis for all operations
3. Provide implementation templates
4. Add decision frameworks for when to use
5. Include practical application examples
6. List edge cases to handle
7. Add to the comparison matrices where applicable
