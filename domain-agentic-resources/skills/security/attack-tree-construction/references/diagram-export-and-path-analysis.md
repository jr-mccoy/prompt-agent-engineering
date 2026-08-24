# Attack Tree Construction — Diagram Export & Path Analysis

## Template 3: Mermaid Diagram Generator

```python
class MermaidExporter:
    """Export attack trees to Mermaid diagram format."""

    def __init__(self, tree: AttackTree):
        self.tree = tree
        self._lines: List[str] = []
        self._node_count = 0

    def export(self) -> str:
        """Export tree to Mermaid flowchart."""
        self._lines = ["flowchart TD"]
        self._export_node(self.tree.root, None)
        return "\n".join(self._lines)

    def _export_node(self, node: AttackNode, parent_id: Optional[str]) -> str:
        """Recursively export nodes."""
        node_id = f"N{self._node_count}"
        self._node_count += 1

        # Node shape based on type
        if node.node_type == NodeType.OR:
            shape = f"{node_id}(({node.name}))"
        elif node.node_type == NodeType.AND:
            shape = f"{node_id}[{node.name}]"
        else:  # LEAF
            # Color based on difficulty
            style = self._get_leaf_style(node)
            shape = f"{node_id}[/{node.name}/]"
            self._lines.append(f"    style {node_id} {style}")

        self._lines.append(f"    {shape}")

        if parent_id:
            connector = "-->" if node.node_type != NodeType.AND else "==>"
            self._lines.append(f"    {parent_id} {connector} {node_id}")

        for child in node.children:
            self._export_node(child, node_id)

        return node_id

    def _get_leaf_style(self, node: AttackNode) -> str:
        """Get style based on attack attributes."""
        colors = {
            Difficulty.TRIVIAL: "fill:#ff6b6b",  # Red - easy attack
            Difficulty.LOW: "fill:#ffa06b",
            Difficulty.MEDIUM: "fill:#ffd93d",
            Difficulty.HIGH: "fill:#6bcb77",
            Difficulty.EXPERT: "fill:#4d96ff",  # Blue - hard attack
        }
        color = colors.get(node.attributes.difficulty, "fill:#gray")
        return color


class PlantUMLExporter:
    """Export attack trees to PlantUML format."""

    def __init__(self, tree: AttackTree):
        self.tree = tree

    def export(self) -> str:
        """Export tree to PlantUML."""
        lines = [
            "@startmindmap",
            f"* {self.tree.name}",
        ]
        self._export_node(self.tree.root, lines, 1)
        lines.append("@endmindmap")
        return "\n".join(lines)

    def _export_node(self, node: AttackNode, lines: List[str], depth: int) -> None:
        """Recursively export nodes."""
        prefix = "*" * (depth + 1)

        if node.node_type == NodeType.OR:
            marker = "[OR]"
        elif node.node_type == NodeType.AND:
            marker = "[AND]"
        else:
            diff = node.attributes.difficulty.name
            marker = f"<<{diff}>>"

        lines.append(f"{prefix} {marker} {node.name}")

        for child in node.children:
            self._export_node(child, lines, depth + 1)
```

---

## Template 4: Attack Path Analysis

```python
from typing import Set, Tuple

class AttackPathAnalyzer:
    """Analyze attack paths and coverage."""

    def __init__(self, tree: AttackTree):
        self.tree = tree

    def get_all_paths(self) -> List[List[AttackNode]]:
        """Get all possible attack paths."""
        paths = []
        self._collect_paths(self.tree.root, [], paths)
        return paths

    def _collect_paths(
        self,
        node: AttackNode,
        current_path: List[AttackNode],
        all_paths: List[List[AttackNode]]
    ) -> None:
        """Recursively collect all paths."""
        current_path = current_path + [node]

        if node.node_type == NodeType.LEAF:
            all_paths.append(current_path)
            return

        if not node.children:
            all_paths.append(current_path)
            return

        if node.node_type == NodeType.OR:
            # Each child is a separate path
            for child in node.children:
                self._collect_paths(child, current_path, all_paths)
        else:  # AND
            # Must combine all children
            child_paths = []
            for child in node.children:
                child_sub_paths = []
                self._collect_paths(child, [], child_sub_paths)
                child_paths.append(child_sub_paths)

            # Combine paths from all AND children
            combined = self._combine_and_paths(child_paths)
            for combo in combined:
                all_paths.append(current_path + combo)

    def _combine_and_paths(
        self,
        child_paths: List[List[List[AttackNode]]]
    ) -> List[List[AttackNode]]:
        """Combine paths from AND node children."""
        if not child_paths:
            return [[]]

        if len(child_paths) == 1:
            return [path for paths in child_paths for path in paths]

        # Cartesian product of all child path combinations
        result = [[]]
        for paths in child_paths:
            new_result = []
            for existing in result:
                for path in paths:
                    new_result.append(existing + path)
            result = new_result
        return result

    def calculate_path_metrics(self, path: List[AttackNode]) -> Dict:
        """Calculate metrics for a specific path."""
        leaves = [n for n in path if n.node_type == NodeType.LEAF]

        total_difficulty = sum(n.attributes.difficulty.value for n in leaves)
        total_cost = sum(n.attributes.cost.value for n in leaves)
        total_time = sum(n.attributes.time_hours for n in leaves)
        max_detection = max((n.attributes.detection_risk.value for n in leaves), default=0)

        return {
            "steps": len(leaves),
            "total_difficulty": total_difficulty,
            "avg_difficulty": total_difficulty / len(leaves) if leaves else 0,
            "total_cost": total_cost,
            "total_time_hours": total_time,
            "max_detection_risk": max_detection,
            "requires_insider": any(n.attributes.requires_insider for n in leaves),
            "requires_physical": any(n.attributes.requires_physical for n in leaves),
        }

    def identify_critical_nodes(self) -> List[Tuple[AttackNode, int]]:
        """Find nodes that appear in the most paths."""
        paths = self.get_all_paths()
        node_counts: Dict[str, Tuple[AttackNode, int]] = {}

        for path in paths:
            for node in path:
                if node.id not in node_counts:
                    node_counts[node.id] = (node, 0)
                node_counts[node.id] = (node, node_counts[node.id][1] + 1)

        return sorted(
            node_counts.values(),
            key=lambda x: x[1],
            reverse=True
        )

    def coverage_analysis(self, mitigated_attacks: Set[str]) -> Dict:
        """Analyze how mitigations affect attack coverage."""
        all_paths = self.get_all_paths()
        blocked_paths = []
        open_paths = []

        for path in all_paths:
            path_attacks = {n.id for n in path if n.node_type == NodeType.LEAF}
            if path_attacks & mitigated_attacks:
                blocked_paths.append(path)
            else:
                open_paths.append(path)

        return {
            "total_paths": len(all_paths),
            "blocked_paths": len(blocked_paths),
            "open_paths": len(open_paths),
            "coverage_percentage": len(blocked_paths) / len(all_paths) * 100 if all_paths else 0,
            "open_path_details": [
                {"path": [n.name for n in p], "metrics": self.calculate_path_metrics(p)}
                for p in open_paths[:5]  # Top 5 open paths
            ]
        }

    def prioritize_mitigations(self) -> List[Dict]:
        """Prioritize mitigations by impact."""
        critical_nodes = self.identify_critical_nodes()
        paths = self.get_all_paths()
        total_paths = len(paths)

        recommendations = []
        for node, count in critical_nodes:
            if node.node_type == NodeType.LEAF and node.mitigations:
                recommendations.append({
                    "attack": node.name,
                    "attack_id": node.id,
                    "paths_blocked": count,
                    "coverage_impact": count / total_paths * 100,
                    "difficulty": node.attributes.difficulty.name,
                    "mitigations": node.mitigations,
                })

        return sorted(recommendations, key=lambda x: x["coverage_impact"], reverse=True)
```

---

## Best Practices

### Do's
- **Start with clear goals** - Define what attacker wants
- **Be exhaustive** - Consider all attack vectors
- **Attribute attacks** - Cost, skill, and detection
- **Update regularly** - New threats emerge
- **Validate with experts** - Red team review

### Don'ts
- **Don't oversimplify** - Real attacks are complex
- **Don't ignore dependencies** - AND nodes matter
- **Don't forget insider threats** - Not all attackers are external
- **Don't skip mitigations** - Trees are for defense planning
- **Don't make it static** - Threat landscape evolves

## Resources

- [Attack Trees by Bruce Schneier](https://www.schneier.com/academic/archives/1999/12/attack_trees.html)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [OWASP Attack Surface Analysis](https://owasp.org/www-community/controls/Attack_Surface_Analysis_Cheat_Sheet)
