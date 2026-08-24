---
title: "Trie and String Matching Structures"
category: algorithms
description: "Framework for implementing tries, suffix structures, and solving string-related algorithmic problems efficiently"
tags:
  - algorithms
  - data-structures
  - trie
  - string-matching
  - suffix-tree
  - autocomplete
  - text-processing
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-01  # Chain-of-Thought
  - RT-02  # Multi-Dimensional Analysis
  - ST-03  # Output Format Templates
  - DS-03  # Tool and Methodology Suggestions
difficulty: intermediate-advanced
version: "1.0"
updated: 2026-01-23
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_tree_structures.md
---

# Trie and String Matching Structures

**Objective:** Implement and apply trie-based data structures and string matching algorithms to solve problems involving prefixes, pattern matching, autocomplete, and text processing efficiently.

**When to Use:** Use this prompt when working with prefix-based search (autocomplete, spell checking), dictionary problems, longest common prefix queries, pattern matching in text, DNA sequence analysis, or IP routing tables.

## Instructions

### 1. Problem Classification

Identify the appropriate string structure based on problem requirements:

**Problem Type Mapping:**
```
Prefix-based operations?
├── Prefix search (autocomplete) → Trie
├── Prefix counting → Trie with count
├── Longest common prefix → Trie
└── Word validation → Trie

Substring operations?
├── Find all occurrences → Suffix Array + LCP
├── Longest repeated substring → Suffix Array/Tree
├── Longest common substring → Generalized Suffix Tree
└── Pattern matching → Suffix Array, KMP, or Aho-Corasick

Multiple pattern matching?
├── Fixed patterns, streaming text → Aho-Corasick
├── Regex patterns → NFA/DFA
└── Approximate matching → Edit distance + Trie

Word games / constraints?
├── Wordle-like constraints → Trie with filtering
├── Crossword filling → Trie with wildcard
└── Anagram grouping → Sorted key + Hash
```

### 2. Trie (Prefix Tree)

#### Basic Trie Structure

**Concept:** Tree where each path from root represents a prefix. Each node represents a character.

```
Words: ["cat", "car", "card", "care", "dog"]

        (root)
        /    \
       c      d
       |      |
       a      o
      /|\     |
     t r g    g*
       |
       d* e*

* = word ending
```

**Complexity:**
| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| Prefix search | O(m) | O(1) |
| Delete | O(m) | O(1) |
| Total space | | O(ALPHABET × n × m) |

Where m = word length, n = number of words

#### Standard Trie Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False
        # Optional augmentations:
        # self.count = 0      # Words ending here
        # self.prefix_count = 0  # Words with this prefix
        # self.word = None    # Store full word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into trie. O(m) time."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Check if exact word exists. O(m) time."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix. O(m) time."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        """Find node corresponding to prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def delete(self, word: str) -> bool:
        """Delete word from trie. O(m) time."""
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete = _delete(node.children[char], word, depth + 1)

            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end

            return False

        return _delete(self.root, word, 0)
```

#### Trie with Prefix Count

```python
class CountingTrie:
    """Trie that tracks count of words with each prefix."""

    def __init__(self):
        self.root = TrieNode()
        self.root.prefix_count = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node.children[char].prefix_count = 0
            node = node.children[char]
            node.prefix_count += 1
        node.is_end = True

    def count_prefix(self, prefix: str) -> int:
        """Count words starting with prefix. O(m) time."""
        node = self._find_node(prefix)
        return node.prefix_count if node else 0
```

### 3. Trie Variants

#### Compressed Trie (Radix Tree / Patricia Trie)

**Concept:** Merge chains of single-child nodes into one node with string edge.

```
Standard Trie:          Compressed Trie:
    (root)                  (root)
      |                     /    \
      c                  "ca"   "dog"
      |                  /  \
      a               "t"  "r"
     /|\                   / \
    t r d                "d" "e"
      |
      d

Space: O(total characters) instead of O(nodes × alphabet)
```

**Advantages:**
- Much less memory for sparse tries
- Faster traversal (skip multiple characters)

**Use cases:**
- IP routing tables
- Sparse dictionaries
- When many words share long prefixes

#### Array-Based Trie

```python
class ArrayTrie:
    """Trie using array children for fixed alphabet (e.g., lowercase)."""

    def __init__(self):
        self.root = [None] * 27  # 26 letters + is_end flag
        self.root[26] = False

    def _idx(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        node = self.root
        for char in word:
            idx = self._idx(char)
            if node[idx] is None:
                node[idx] = [None] * 27
                node[idx][26] = False
            node = node[idx]
        node[26] = True
```

**Trade-offs:**
- Faster child access: O(1) vs O(alphabet) hash lookup
- More memory if alphabet is large or trie is sparse
- Best for small fixed alphabets (DNA: 4, lowercase: 26)

### 4. Advanced String Structures

#### Suffix Trie

**Concept:** Trie of all suffixes of a string.

```
String: "banana$"
Suffixes: banana$, anana$, nana$, ana$, na$, a$, $

All inserted into one trie.
```

**Complexity:**
- Space: O(n²) - can be quadratic
- Build: O(n²)
- Substring search: O(m)

**Limitation:** Quadratic space makes it impractical for long strings.

#### Suffix Array

**Concept:** Sorted array of all suffix starting positions.

```
String: "banana$" ($ = sentinel, smallest char)
Index:   0123456

Suffixes:
0: banana$
1: anana$
2: nana$
3: ana$
4: na$
5: a$
6: $

Sorted: $ < a$ < ana$ < anana$ < banana$ < na$ < nana$
Suffix Array: [6, 5, 3, 1, 0, 4, 2]
```

**Complexity:**
| Operation | Time | Space |
|-----------|------|-------|
| Build (naive) | O(n² log n) | O(n) |
| Build (DC3/SA-IS) | O(n) | O(n) |
| Search pattern | O(m log n) | O(1) |
| With LCP array | O(m + log n) | O(n) |

**LCP Array:** Longest Common Prefix between adjacent suffixes in sorted order.

```python
def build_suffix_array_naive(s):
    """Build suffix array in O(n² log n). Use SA-IS for O(n)."""
    s = s + '$'  # Sentinel
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]

def search_pattern(text, pattern, sa):
    """Binary search for pattern in suffix array. O(m log n)."""
    left, right = 0, len(sa)

    # Find leftmost occurrence
    while left < right:
        mid = (left + right) // 2
        suffix = text[sa[mid]:]
        if suffix < pattern:
            left = mid + 1
        else:
            right = mid

    start = left

    # Find rightmost occurrence
    right = len(sa)
    while left < right:
        mid = (left + right) // 2
        suffix = text[sa[mid]:]
        if suffix.startswith(pattern):
            left = mid + 1
        elif suffix < pattern:
            left = mid + 1
        else:
            right = mid

    return sa[start:left]  # All positions where pattern occurs
```

#### Suffix Tree

**Concept:** Compressed trie of all suffixes. O(n) space.

**Construction:** Ukkonen's algorithm - O(n) time

**Capabilities:**
- Find pattern in O(m) time
- Find longest repeated substring
- Find longest common substring of two strings
- Count occurrences of pattern

**Use when:**
- Multiple queries on same text
- Need O(m) search, not O(m log n)
- Complex substring operations

### 5. Pattern Matching Algorithms

#### KMP (Knuth-Morris-Pratt)

**Problem:** Find all occurrences of pattern in text.

**Idea:** Precompute failure function to avoid re-examining characters.

```python
def compute_lps(pattern):
    """Compute Longest Proper Prefix which is also Suffix."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps

def kmp_search(text, pattern):
    """Find all occurrences of pattern in text. O(n + m)."""
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches = []

    i = j = 0  # i: text index, j: pattern index
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return matches
```

**Complexity:** O(n + m) time, O(m) space

#### Aho-Corasick

**Problem:** Find all occurrences of multiple patterns simultaneously.

**Concept:** Build trie of patterns + failure links (like KMP for tries).

```python
from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.goto = [{}]  # goto[state][char] -> next_state
        self.fail = [0]   # fail[state] -> fallback_state
        self.output = [[]]  # output[state] -> list of pattern indices

    def build(self, patterns):
        """Build automaton from patterns. O(total pattern length)."""
        # Build trie (goto function)
        for idx, pattern in enumerate(patterns):
            state = 0
            for char in pattern:
                if char not in self.goto[state]:
                    self.goto.append({})
                    self.fail.append(0)
                    self.output.append([])
                    self.goto[state][char] = len(self.goto) - 1
                state = self.goto[state][char]
            self.output[state].append(idx)

        # Build failure function (BFS)
        queue = deque()
        for char, state in self.goto[0].items():
            queue.append(state)
            self.fail[state] = 0

        while queue:
            curr = queue.popleft()
            for char, next_state in self.goto[curr].items():
                queue.append(next_state)

                # Find failure state
                fallback = self.fail[curr]
                while fallback and char not in self.goto[fallback]:
                    fallback = self.fail[fallback]

                self.fail[next_state] = self.goto[fallback].get(char, 0)
                self.output[next_state] += self.output[self.fail[next_state]]

    def search(self, text):
        """Find all pattern occurrences. O(n + number of matches)."""
        state = 0
        results = []

        for i, char in enumerate(text):
            while state and char not in self.goto[state]:
                state = self.fail[state]
            state = self.goto[state].get(char, 0)

            for pattern_idx in self.output[state]:
                results.append((i, pattern_idx))

        return results
```

**Complexity:**
- Build: O(sum of pattern lengths)
- Search: O(n + number of matches)

**Use cases:**
- Keyword filtering
- DNA sequence matching
- Network intrusion detection

### 6. Common Applications

#### Application 1: Autocomplete System

```python
class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.freq = {}  # word -> frequency

        for sentence, count in zip(sentences, times):
            self.trie.insert(sentence)
            self.freq[sentence] = count

        self.current_input = ""

    def input(self, c):
        if c == '#':
            # End of input - record sentence
            self.trie.insert(self.current_input)
            self.freq[self.current_input] = self.freq.get(self.current_input, 0) + 1
            self.current_input = ""
            return []

        self.current_input += c
        return self._get_suggestions(self.current_input)

    def _get_suggestions(self, prefix, k=3):
        """Get top k suggestions for prefix."""
        node = self.trie._find_node(prefix)
        if not node:
            return []

        # Collect all words with this prefix
        words = []
        self._collect_words(node, prefix, words)

        # Sort by frequency (desc), then lexicographically
        words.sort(key=lambda w: (-self.freq.get(w, 0), w))
        return words[:k]

    def _collect_words(self, node, prefix, words):
        if node.is_end:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)
```

#### Application 2: Word Search with Wildcards

```python
class WildcardTrie:
    """Support search with '.' as wildcard."""

    def search_with_wildcard(self, word):
        """Search allowing '.' to match any character."""
        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]
            if char == '.':
                # Try all children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)
```

#### Application 3: Longest Common Prefix

```python
def longest_common_prefix(words):
    """Find LCP of all words using trie."""
    if not words:
        return ""

    trie = Trie()
    for word in words:
        trie.insert(word)

    # Follow path while only one child and not end of any word
    prefix = []
    node = trie.root

    while len(node.children) == 1 and not node.is_end:
        char = next(iter(node.children))
        prefix.append(char)
        node = node.children[char]

    return ''.join(prefix)
```

#### Application 4: Word Break Problem

```python
def word_break(s, word_dict):
    """Check if s can be segmented into dictionary words."""
    trie = Trie()
    for word in word_dict:
        trie.insert(word)

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if not dp[i]:
            continue

        node = trie.root
        for j in range(i, n):
            if s[j] not in node.children:
                break
            node = node.children[s[j]]
            if node.is_end:
                dp[j + 1] = True

    return dp[n]
```

### 7. Decision Framework

```
String problem decision tree:
│
├─ Prefix operations only?
│  ├─ Small alphabet → Array-based Trie
│  ├─ Large/sparse alphabet → HashMap Trie
│  └─ Memory constrained → Compressed Trie
│
├─ Need substring search?
│  ├─ Single pattern → KMP
│  ├─ Multiple patterns → Aho-Corasick
│  ├─ Multiple queries, same text → Suffix Array/Tree
│  └─ Longest repeated substring → Suffix Tree
│
├─ Wildcard/regex matching?
│  ├─ Simple wildcards (.) → Trie with DFS
│  └─ Full regex → NFA/DFA
│
└─ Other string operations?
   ├─ Anagrams → Sorted key hashing
   ├─ Edit distance → DP or BK-tree
   └─ Palindromes → Manacher's algorithm
```

## Expected Output

When solving a string/trie problem, provide:

1. **Problem Analysis**
   - Type of string operation needed
   - Query patterns (single vs multiple)
   - Space/time trade-offs

2. **Data Structure Selection**
   - Chosen structure with justification
   - Variant selection (compressed, array-based, etc.)

3. **Implementation**
   - Core data structure
   - Required operations
   - Edge case handling

4. **Complexity Analysis**
   - Time: per operation and total
   - Space: structure overhead

## Quality Checklist

- [ ] Correct trie property maintained
- [ ] End-of-word markers handled properly
- [ ] Empty string case handled
- [ ] Alphabet assumptions documented
- [ ] Memory efficiency considered for large inputs
- [ ] Pattern matching handles overlapping matches

## Techniques Used

- **ST-01** (Clear Objective Statement) - Define string problem
- **ST-02** (Structured Sequential Instructions) - Implementation steps
- **RT-01** (Chain-of-Thought) - Trace through trie operations
- **RT-02** (Multi-Dimensional Analysis) - Compare string structures
- **ST-03** (Output Format Templates) - Consistent format
- **DS-03** (Tool and Methodology Suggestions) - Algorithm selection

## Related Prompts

- `algorithms_data_structure_selection.md` - Choosing structures
- `algorithms_tree_structures.md` - Tree fundamentals
- `learning/learning_algorithmic_storytelling.md` - Teaching trie concepts

## Customization Guide

**For Interview Preparation:**
- Implement trie from scratch quickly
- Know autocomplete and word search patterns
- Practice trie + DFS combinations

**For Text Processing:**
- Focus on suffix arrays for large texts
- Learn efficient construction algorithms
- Consider memory-mapped structures

**For Search Systems:**
- Implement fuzzy matching with edit distance
- Consider inverted indices for documents
- Combine with ranking/scoring
