# Threat Mitigation Mapping — Advanced Analysis & Control Testing

## Template 3: Mitigation Analysis

```python
class MitigationAnalyzer:
    """Analyze and optimize mitigation strategies."""

    def __init__(self, plan: MitigationPlan, library: ControlLibrary):
        self.plan = plan
        self.library = library

    def calculate_overall_risk_reduction(self) -> float:
        """Calculate overall risk reduction percentage."""
        if not self.plan.mappings:
            return 0.0

        weighted_coverage = 0
        total_weight = 0

        for mapping in self.plan.mappings:
            # Weight by threat risk score
            weight = mapping.threat.risk_score
            coverage = mapping.calculate_coverage()
            weighted_coverage += weight * coverage
            total_weight += weight

        return weighted_coverage / total_weight if total_weight > 0 else 0

    def get_critical_gaps(self) -> List[Dict]:
        """Find critical gaps that need immediate attention."""
        gaps = self.plan.get_gaps()
        critical_threats = {t.id for t in self.plan.threats if t.impact == "Critical"}

        return [g for g in gaps if g["threat"] in critical_threats]

    def optimize_budget(
        self,
        budget: float,
        cost_map: Dict[str, float]
    ) -> List[SecurityControl]:
        """Select controls that maximize risk reduction within budget."""
        # Simple greedy approach - can be replaced with optimization algorithm
        recommended = []
        remaining_budget = budget
        unmapped = self.plan.get_unmapped_threats()

        # Sort controls by effectiveness/cost ratio
        all_controls = list(self.library.STANDARD_CONTROLS.values())
        controls_with_value = []

        for control in all_controls:
            if control.status == ImplementationStatus.NOT_IMPLEMENTED:
                cost = cost_map.get(control.id, float('inf'))
                if cost <= remaining_budget:
                    # Calculate value as threats covered * effectiveness / cost
                    threats_covered = len([
                        t for t in unmapped
                        if t.category in control.mitigates_threats
                    ])
                    if threats_covered > 0:
                        value = (threats_covered * control.effectiveness.value) / cost
                        controls_with_value.append((control, value, cost))

        # Sort by value (higher is better)
        controls_with_value.sort(key=lambda x: x[1], reverse=True)

        for control, value, cost in controls_with_value:
            if cost <= remaining_budget:
                recommended.append(control)
                remaining_budget -= cost

        return recommended

    def generate_roadmap(self) -> List[Dict]:
        """Generate implementation roadmap by priority."""
        roadmap = []
        gaps = self.plan.get_gaps()

        # Phase 1: Critical threats with low coverage
        phase1 = []
        for gap in gaps:
            mapping = next(
                (m for m in self.plan.mappings if m.threat.id == gap["threat"]),
                None
            )
            if mapping and mapping.threat.impact == "Critical":
                controls = self.library.get_controls_for_threat(mapping.threat.category)
                phase1.extend([
                    {
                        "threat": gap["threat"],
                        "control": c.id,
                        "control_name": c.name,
                        "phase": 1,
                        "priority": "Critical"
                    }
                    for c in controls
                    if c.status == ImplementationStatus.NOT_IMPLEMENTED
                ])

        roadmap.extend(phase1[:5])  # Top 5 for phase 1

        # Phase 2: High impact threats
        phase2 = []
        for gap in gaps:
            mapping = next(
                (m for m in self.plan.mappings if m.threat.id == gap["threat"]),
                None
            )
            if mapping and mapping.threat.impact == "High":
                controls = self.library.get_controls_for_threat(mapping.threat.category)
                phase2.extend([
                    {
                        "threat": gap["threat"],
                        "control": c.id,
                        "control_name": c.name,
                        "phase": 2,
                        "priority": "High"
                    }
                    for c in controls
                    if c.status == ImplementationStatus.NOT_IMPLEMENTED
                ])

        roadmap.extend(phase2[:5])  # Top 5 for phase 2

        return roadmap

    def defense_in_depth_analysis(self) -> Dict[str, List[str]]:
        """Analyze defense in depth coverage."""
        layer_coverage = {layer.value: [] for layer in ControlLayer}

        for mapping in self.plan.mappings:
            for control in mapping.controls:
                if control.status in [ImplementationStatus.IMPLEMENTED, ImplementationStatus.VERIFIED]:
                    layer_coverage[control.layer.value].append(control.id)

        return layer_coverage

    def generate_report(self) -> str:
        """Generate comprehensive mitigation report."""
        risk_reduction = self.calculate_overall_risk_reduction()
        gaps = self.plan.get_gaps()
        critical_gaps = self.get_critical_gaps()
        layer_coverage = self.defense_in_depth_analysis()

        report = f"""
# Threat Mitigation Report

## Executive Summary
- **Overall Risk Reduction:** {risk_reduction:.1f}%
- **Total Threats:** {len(self.plan.threats)}
- **Total Controls:** {len(self.plan.controls)}
- **Identified Gaps:** {len(gaps)}
- **Critical Gaps:** {len(critical_gaps)}

## Defense in Depth Coverage
{self._format_layer_coverage(layer_coverage)}

## Critical Gaps Requiring Immediate Action
{self._format_gaps(critical_gaps)}

## Recommendations
{self._format_recommendations()}

## Implementation Roadmap
{self._format_roadmap()}
"""
        return report

    def _format_layer_coverage(self, coverage: Dict[str, List[str]]) -> str:
        lines = []
        for layer, controls in coverage.items():
            status = "✓" if controls else "✗"
            lines.append(f"- {layer}: {status} ({len(controls)} controls)")
        return "\n".join(lines)

    def _format_gaps(self, gaps: List[Dict]) -> str:
        if not gaps:
            return "No critical gaps identified."
        lines = []
        for gap in gaps:
            lines.append(f"- **{gap['threat_name']}**: {gap['issue']}")
            lines.append(f"  - Coverage: {gap['coverage']:.1f}%")
            lines.append(f"  - Recommendation: {gap['recommendation']}")
        return "\n".join(lines)

    def _format_recommendations(self) -> str:
        recommendations = []
        layer_coverage = self.defense_in_depth_analysis()

        for layer, controls in layer_coverage.items():
            if not controls:
                recommendations.append(f"- Add {layer} layer controls")

        gaps = self.plan.get_gaps()
        if any(g["issue"] == "No control diversity" for g in gaps):
            recommendations.append("- Add more detective and corrective controls")

        return "\n".join(recommendations) if recommendations else "Current coverage is adequate."

    def _format_roadmap(self) -> str:
        roadmap = self.generate_roadmap()
        if not roadmap:
            return "No additional controls recommended at this time."

        lines = []
        current_phase = 0
        for item in roadmap:
            if item["phase"] != current_phase:
                current_phase = item["phase"]
                lines.append(f"\n### Phase {current_phase}")
            lines.append(f"- [{item['priority']}] {item['control_name']} (for {item['threat']})")

        return "\n".join(lines)
```

---

## Template 4: Control Effectiveness Testing

```python
from dataclasses import dataclass
from typing import List, Callable, Any
import asyncio

@dataclass
class ControlTest:
    control_id: str
    test_name: str
    test_function: Callable[[], bool]
    expected_result: bool
    description: str


class ControlTester:
    """Test control effectiveness."""

    def __init__(self):
        self.tests: List[ControlTest] = []
        self.results: List[Dict] = []

    def add_test(self, test: ControlTest) -> None:
        self.tests.append(test)

    async def run_tests(self) -> List[Dict]:
        """Run all control tests."""
        self.results = []

        for test in self.tests:
            try:
                result = test.test_function()
                passed = result == test.expected_result
                self.results.append({
                    "control_id": test.control_id,
                    "test_name": test.test_name,
                    "passed": passed,
                    "actual_result": result,
                    "expected_result": test.expected_result,
                    "description": test.description,
                    "error": None
                })
            except Exception as e:
                self.results.append({
                    "control_id": test.control_id,
                    "test_name": test.test_name,
                    "passed": False,
                    "actual_result": None,
                    "expected_result": test.expected_result,
                    "description": test.description,
                    "error": str(e)
                })

        return self.results

    def get_effectiveness_score(self, control_id: str) -> float:
        """Calculate effectiveness score for a control."""
        control_results = [r for r in self.results if r["control_id"] == control_id]
        if not control_results:
            return 0.0

        passed = sum(1 for r in control_results if r["passed"])
        return (passed / len(control_results)) * 100

    def generate_test_report(self) -> str:
        """Generate test results report."""
        if not self.results:
            return "No tests have been run."

        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])

        report = f"""
# Control Effectiveness Test Report

## Summary
- **Total Tests:** {total}
- **Passed:** {passed}
- **Failed:** {total - passed}
- **Pass Rate:** {(passed/total)*100:.1f}%

## Results by Control
"""
        # Group by control
        controls = {}
        for result in self.results:
            cid = result["control_id"]
            if cid not in controls:
                controls[cid] = []
            controls[cid].append(result)

        for control_id, results in controls.items():
            score = self.get_effectiveness_score(control_id)
            report += f"\n### {control_id} (Effectiveness: {score:.1f}%)\n"
            for r in results:
                status = "✓" if r["passed"] else "✗"
                report += f"- {status} {r['test_name']}\n"
                if r["error"]:
                    report += f"  - Error: {r['error']}\n"

        return report
```

---

## Best Practices

### Do's
- **Map all threats** - No threat should be unmapped
- **Layer controls** - Defense in depth is essential
- **Mix control types** - Preventive, detective, corrective
- **Track effectiveness** - Measure and improve
- **Review regularly** - Controls degrade over time

### Don'ts
- **Don't rely on single controls** - Single points of failure
- **Don't ignore cost** - ROI matters
- **Don't skip testing** - Untested controls may fail
- **Don't set and forget** - Continuous improvement
- **Don't ignore people/process** - Technology alone isn't enough

## Resources

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Controls](https://www.cisecurity.org/controls)
- [MITRE D3FEND](https://d3fend.mitre.org/)
