# STRIDE Analysis Patterns — DFD Analysis & STRIDE per Interaction

## Template 3: Data Flow Diagram Analysis

```python
from dataclasses import dataclass
from typing import List, Set, Tuple
from enum import Enum

class ElementType(Enum):
    EXTERNAL_ENTITY = "external"
    PROCESS = "process"
    DATA_STORE = "datastore"
    DATA_FLOW = "dataflow"


@dataclass
class DFDElement:
    id: str
    name: str
    type: ElementType
    trust_level: int  # 0 = untrusted, higher = more trusted
    description: str = ""


@dataclass
class DataFlow:
    id: str
    name: str
    source: str
    destination: str
    data_type: str
    protocol: str
    encrypted: bool = False


class DFDAnalyzer:
    """Analyze Data Flow Diagrams for STRIDE threats."""

    def __init__(self):
        self.elements: Dict[str, DFDElement] = {}
        self.flows: List[DataFlow] = []

    def add_element(self, element: DFDElement) -> None:
        self.elements[element.id] = element

    def add_flow(self, flow: DataFlow) -> None:
        self.flows.append(flow)

    def find_trust_boundary_crossings(self) -> List[Tuple[DataFlow, int]]:
        """Find data flows that cross trust boundaries."""
        crossings = []
        for flow in self.flows:
            source = self.elements.get(flow.source)
            dest = self.elements.get(flow.destination)
            if source and dest and source.trust_level != dest.trust_level:
                trust_diff = abs(source.trust_level - dest.trust_level)
                crossings.append((flow, trust_diff))
        return sorted(crossings, key=lambda x: x[1], reverse=True)

    def identify_threats_per_element(self) -> Dict[str, List[StrideCategory]]:
        """Map applicable STRIDE categories to element types."""
        threat_mapping = {
            ElementType.EXTERNAL_ENTITY: [
                StrideCategory.SPOOFING,
                StrideCategory.REPUDIATION,
            ],
            ElementType.PROCESS: [
                StrideCategory.SPOOFING,
                StrideCategory.TAMPERING,
                StrideCategory.REPUDIATION,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
                StrideCategory.ELEVATION_OF_PRIVILEGE,
            ],
            ElementType.DATA_STORE: [
                StrideCategory.TAMPERING,
                StrideCategory.REPUDIATION,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
            ],
            ElementType.DATA_FLOW: [
                StrideCategory.TAMPERING,
                StrideCategory.INFORMATION_DISCLOSURE,
                StrideCategory.DENIAL_OF_SERVICE,
            ],
        }

        result = {}
        for elem_id, elem in self.elements.items():
            result[elem_id] = threat_mapping.get(elem.type, [])
        return result

    def analyze_unencrypted_flows(self) -> List[DataFlow]:
        """Find unencrypted data flows crossing trust boundaries."""
        risky_flows = []
        for flow in self.flows:
            if not flow.encrypted:
                source = self.elements.get(flow.source)
                dest = self.elements.get(flow.destination)
                if source and dest and source.trust_level != dest.trust_level:
                    risky_flows.append(flow)
        return risky_flows

    def generate_threat_enumeration(self) -> List[Dict]:
        """Generate comprehensive threat enumeration."""
        threats = []
        element_threats = self.identify_threats_per_element()

        for elem_id, categories in element_threats.items():
            elem = self.elements[elem_id]
            for category in categories:
                threats.append({
                    "element_id": elem_id,
                    "element_name": elem.name,
                    "element_type": elem.type.value,
                    "stride_category": category.name,
                    "description": f"{category.name} threat against {elem.name}",
                    "trust_level": elem.trust_level
                })

        return threats
```

---

## Template 4: STRIDE per Interaction

```python
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Interaction:
    """Represents an interaction between two components."""
    id: str
    source: str
    target: str
    action: str
    data: str
    protocol: str


class StridePerInteraction:
    """Apply STRIDE to each interaction in the system."""

    INTERACTION_THREATS = {
        # Source type -> Target type -> Applicable threats
        ("external", "process"): {
            "S": "External entity spoofing identity to process",
            "T": "Tampering with data sent to process",
            "R": "External entity denying sending data",
            "I": "Data exposure during transmission",
            "D": "Flooding process with requests",
            "E": "Exploiting process to gain privileges",
        },
        ("process", "datastore"): {
            "T": "Process tampering with stored data",
            "R": "Process denying data modifications",
            "I": "Unauthorized data access by process",
            "D": "Process exhausting storage resources",
        },
        ("process", "process"): {
            "S": "Process spoofing another process",
            "T": "Tampering with inter-process data",
            "I": "Data leakage between processes",
            "D": "One process overwhelming another",
            "E": "Process gaining elevated access",
        },
    }

    def analyze_interaction(
        self,
        interaction: Interaction,
        source_type: str,
        target_type: str
    ) -> List[Dict]:
        """Analyze a single interaction for STRIDE threats."""
        threats = []
        key = (source_type, target_type)

        applicable_threats = self.INTERACTION_THREATS.get(key, {})

        for stride_code, description in applicable_threats.items():
            threats.append({
                "interaction_id": interaction.id,
                "source": interaction.source,
                "target": interaction.target,
                "stride_category": stride_code,
                "threat_description": description,
                "context": f"{interaction.action} - {interaction.data}",
            })

        return threats

    def generate_threat_matrix(
        self,
        interactions: List[Interaction],
        element_types: Dict[str, str]
    ) -> List[Dict]:
        """Generate complete threat matrix for all interactions."""
        all_threats = []

        for interaction in interactions:
            source_type = element_types.get(interaction.source, "unknown")
            target_type = element_types.get(interaction.target, "unknown")

            threats = self.analyze_interaction(
                interaction, source_type, target_type
            )
            all_threats.extend(threats)

        return all_threats
```

---

## Best Practices

### Do's
- **Involve stakeholders** - Security, dev, and ops perspectives
- **Be systematic** - Cover all STRIDE categories
- **Prioritize realistically** - Focus on high-impact threats
- **Update regularly** - Threat models are living documents
- **Use visual aids** - DFDs help communication

### Don'ts
- **Don't skip categories** - Each reveals different threats
- **Don't assume security** - Question every component
- **Don't work in isolation** - Collaborative modeling is better
- **Don't ignore low-probability** - High-impact threats matter
- **Don't stop at identification** - Follow through with mitigations

## Resources

- [Microsoft STRIDE Documentation](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [Threat Modeling: Designing for Security](https://www.wiley.com/en-us/Threat+Modeling%3A+Designing+for+Security-p-9781118809990)
