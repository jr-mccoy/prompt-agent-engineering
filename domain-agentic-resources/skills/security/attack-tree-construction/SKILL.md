---
name: attack-tree-construction
description: Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders.
metadata:
  tags:
    - attack
    - attack-trees
    - construction
    - security
    - threat-modeling
    - tree
  updated: "2026-04-11"
---
# Attack Tree Construction

Systematic attack path visualization and analysis.

## When to Use This Skill

- Visualizing complex attack scenarios
- Identifying defense gaps and priorities
- Communicating risks to stakeholders
- Planning defensive investments
- Penetration test planning
- Security architecture review

## Core Concepts

### 1. Attack Tree Structure

```
                    [Root Goal]
                         |
            ┌────────────┴────────────┐
            │                         │
       [Sub-goal 1]              [Sub-goal 2]
       (OR node)                 (AND node)
            │                         │
      ┌─────┴─────┐             ┌─────┴─────┐
      │           │             │           │
   [Attack]   [Attack]      [Attack]   [Attack]
    (leaf)     (leaf)        (leaf)     (leaf)
```

### 2. Node Types

| Type | Symbol | Description |
|------|--------|-------------|
| **OR** | Oval | Any child achieves goal |
| **AND** | Rectangle | All children required |
| **Leaf** | Box | Atomic attack step |

### 3. Attack Attributes

| Attribute | Description | Values |
|-----------|-------------|--------|
| **Cost** | Resources needed | $, $$, $$$ |
| **Time** | Duration to execute | Hours, Days, Weeks |
| **Skill** | Expertise required | Low, Medium, High |
| **Detection** | Likelihood of detection | Low, Medium, High |

## Templates

### Template 1: Attack Tree Data Model

```python
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Union
import json

class NodeType(Enum):
    OR = "or"
    AND = "and"
    LEAF = "leaf"


class Difficulty(Enum):
    TRIVIAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    EXPERT = 5


class Cost(Enum):
    FREE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class DetectionRisk(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CERTAIN = 4


@dataclass
class AttackAttributes:
    difficulty: Difficulty = Difficulty.MEDIUM
    cost: Cost = Cost.MEDIUM
    detection_risk: DetectionRisk = DetectionRisk.MEDIUM
    time_hours: float = 8.0
    requires_insider: bool = False
    requires_physical: bool = False


@dataclass
class AttackNode:
    id: str
    name: str
    description: str
    node_type: NodeType
    attributes: AttackAttributes = field(default_factory=AttackAttributes)
    children: List['AttackNode'] = field(default_factory=list)
    mitigations: List[str] = field(default_factory=list)
    cve_refs: List[str] = field(default_factory=list)

    def add_child(self, child: 'AttackNode') -> None:
        self.children.append(child)

    def calculate_path_difficulty(self) -> float:
        """Calculate aggregate difficulty for this path."""
        if self.node_type == NodeType.LEAF:
            return self.attributes.difficulty.value

        if not self.children:
            return 0

        child_difficulties = [c.calculate_path_difficulty() for c in self.children]

        if self.node_type == NodeType.OR:
            return min(child_difficulties)
        else:  # AND
            return max(child_difficulties)

    def calculate_path_cost(self) -> float:
        """Calculate aggregate cost for this path."""
        if self.node_type == NodeType.LEAF:
            return self.attributes.cost.value

        if not self.children:
            return 0

        child_costs = [c.calculate_path_cost() for c in self.children]

        if self.node_type == NodeType.OR:
            return min(child_costs)
        else:  # AND
            return sum(child_costs)

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.node_type.value,
            "attributes": {
                "difficulty": self.attributes.difficulty.name,
                "cost": self.attributes.cost.name,
                "detection_risk": self.attributes.detection_risk.name,
                "time_hours": self.attributes.time_hours,
            },
            "mitigations": self.mitigations,
            "children": [c.to_dict() for c in self.children]
        }


@dataclass
class AttackTree:
    name: str
    description: str
    root: AttackNode
    version: str = "1.0"

    def find_easiest_path(self) -> List[AttackNode]:
        """Find the path with lowest difficulty."""
        return self._find_path(self.root, minimize="difficulty")

    def find_cheapest_path(self) -> List[AttackNode]:
        """Find the path with lowest cost."""
        return self._find_path(self.root, minimize="cost")

    def find_stealthiest_path(self) -> List[AttackNode]:
        """Find the path with lowest detection risk."""
        return self._find_path(self.root, minimize="detection")

    def _find_path(
        self,
        node: AttackNode,
        minimize: str
    ) -> List[AttackNode]:
        """Recursive path finding."""
        if node.node_type == NodeType.LEAF:
            return [node]

        if not node.children:
            return [node]

        if node.node_type == NodeType.OR:
            # Pick the best child path
            best_path = None
            best_score = float('inf')

            for child in node.children:
                child_path = self._find_path(child, minimize)
                score = self._path_score(child_path, minimize)
                if score < best_score:
                    best_score = score
                    best_path = child_path

            return [node] + (best_path or [])
        else:  # AND
            # Must traverse all children
            path = [node]
            for child in node.children:
                path.extend(self._find_path(child, minimize))
            return path

    def _path_score(self, path: List[AttackNode], metric: str) -> float:
        """Calculate score for a path."""
        if metric == "difficulty":
            return sum(n.attributes.difficulty.value for n in path if n.node_type == NodeType.LEAF)
        elif metric == "cost":
            return sum(n.attributes.cost.value for n in path if n.node_type == NodeType.LEAF)
        elif metric == "detection":
            return sum(n.attributes.detection_risk.value for n in path if n.node_type == NodeType.LEAF)
        return 0

    def get_all_leaf_attacks(self) -> List[AttackNode]:
        """Get all leaf attack nodes."""
        leaves = []
        self._collect_leaves(self.root, leaves)
        return leaves

    def _collect_leaves(self, node: AttackNode, leaves: List[AttackNode]) -> None:
        if node.node_type == NodeType.LEAF:
            leaves.append(node)
        for child in node.children:
            self._collect_leaves(child, leaves)

    def get_unmitigated_attacks(self) -> List[AttackNode]:
        """Find attacks without mitigations."""
        return [n for n in self.get_all_leaf_attacks() if not n.mitigations]

    def export_json(self) -> str:
        """Export tree to JSON."""
        return json.dumps({
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "root": self.root.to_dict()
        }, indent=2)
```

### Template 2: Attack Tree Builder

```python
class AttackTreeBuilder:
    """Fluent builder for attack trees."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self._node_stack: List[AttackNode] = []
        self._root: Optional[AttackNode] = None

    def goal(self, id: str, name: str, description: str = "") -> 'AttackTreeBuilder':
        """Set the root goal (OR node by default)."""
        self._root = AttackNode(
            id=id,
            name=name,
            description=description,
            node_type=NodeType.OR
        )
        self._node_stack = [self._root]
        return self

    def or_node(self, id: str, name: str, description: str = "") -> 'AttackTreeBuilder':
        """Add an OR sub-goal."""
        node = AttackNode(
            id=id,
            name=name,
            description=description,
            node_type=NodeType.OR
        )
        self._current().add_child(node)
        self._node_stack.append(node)
        return self

    def and_node(self, id: str, name: str, description: str = "") -> 'AttackTreeBuilder':
        """Add an AND sub-goal (all children required)."""
        node = AttackNode(
            id=id,
            name=name,
            description=description,
            node_type=NodeType.AND
        )
        self._current().add_child(node)
        self._node_stack.append(node)
        return self

    def attack(
        self,
        id: str,
        name: str,
        description: str = "",
        difficulty: Difficulty = Difficulty.MEDIUM,
        cost: Cost = Cost.MEDIUM,
        detection: DetectionRisk = DetectionRisk.MEDIUM,
        time_hours: float = 8.0,
        mitigations: List[str] = None
    ) -> 'AttackTreeBuilder':
        """Add a leaf attack node."""
        node = AttackNode(
            id=id,
            name=name,
            description=description,
            node_type=NodeType.LEAF,
            attributes=AttackAttributes(
                difficulty=difficulty,
                cost=cost,
                detection_risk=detection,
                time_hours=time_hours
            ),
            mitigations=mitigations or []
        )
        self._current().add_child(node)
        return self

    def end(self) -> 'AttackTreeBuilder':
        """Close current node, return to parent."""
        if len(self._node_stack) > 1:
            self._node_stack.pop()
        return self

    def build(self) -> AttackTree:
        """Build the attack tree."""
        if not self._root:
            raise ValueError("No root goal defined")
        return AttackTree(
            name=self.name,
            description=self.description,
            root=self._root
        )

    def _current(self) -> AttackNode:
        if not self._node_stack:
            raise ValueError("No current node")
        return self._node_stack[-1]


# Example usage
def build_account_takeover_tree() -> AttackTree:
    """Build attack tree for account takeover scenario."""
    return (
        AttackTreeBuilder("Account Takeover", "Gain unauthorized access to user account")
        .goal("G1", "Take Over User Account")

        .or_node("S1", "Steal Credentials")
            .attack(
                "A1", "Phishing Attack",
                difficulty=Difficulty.LOW,
                cost=Cost.LOW,
                detection=DetectionRisk.MEDIUM,
                mitigations=["Security awareness training", "Email filtering"]
            )
            .attack(
                "A2", "Credential Stuffing",
                difficulty=Difficulty.TRIVIAL,
                cost=Cost.LOW,
                detection=DetectionRisk.HIGH,
                mitigations=["Rate limiting", "MFA", "Password breach monitoring"]
            )
            .attack(
                "A3", "Keylogger Malware",
                difficulty=Difficulty.MEDIUM,
                cost=Cost.MEDIUM,
                detection=DetectionRisk.MEDIUM,
                mitigations=["Endpoint protection", "MFA"]
            )
        .end()

        .or_node("S2", "Bypass Authentication")
            .attack(
                "A4", "Session Hijacking",
                difficulty=Difficulty.MEDIUM,
                cost=Cost.LOW,
                detection=DetectionRisk.LOW,
                mitigations=["Secure session management", "HTTPS only"]
            )
            .attack(
                "A5", "Authentication Bypass Vulnerability",
                difficulty=Difficulty.HIGH,
                cost=Cost.LOW,
                detection=DetectionRisk.LOW,
                mitigations=["Security testing", "Code review", "WAF"]
            )
        .end()

        .or_node("S3", "Social Engineering")
            .and_node("S3.1", "Account Recovery Attack")
                .attack(
                    "A6", "Gather Personal Information",
                    difficulty=Difficulty.LOW,
                    cost=Cost.FREE,
                    detection=DetectionRisk.NONE
                )
                .attack(
                    "A7", "Call Support Desk",
                    difficulty=Difficulty.MEDIUM,
                    cost=Cost.FREE,
                    detection=DetectionRisk.MEDIUM,
                    mitigations=["Support verification procedures", "Security questions"]
                )
            .end()
        .end()

        .build()
    )
```

## Diagram Export, Path Analysis, Best Practices & Resources

Mermaid flowchart export (MermaidExporter with OR/AND/leaf node shapes + difficulty-based color coding), PlantUML mindmap export (PlantUMLExporter with OR/AND/difficulty markers), complete attack path analysis (AttackPathAnalyzer with get_all_paths/calculate_path_metrics/identify_critical_nodes/coverage_analysis with mitigated attack set/prioritize_mitigations by coverage impact), Best Practices (Do's/Don'ts), Resources (Schneier/MITRE ATT&CK/OWASP).

See [references/diagram-export-and-path-analysis.md](references/diagram-export-and-path-analysis.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/diagram-export-and-path-analysis.md` | Mermaid/PlantUML export, AttackPathAnalyzer, best practices, resources |
