---
name: threat-mitigation-mapping
description: Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness.
metadata:
  tags:
    - mapping
    - mitigation
    - risk
    - security
    - threat
    - threat-modeling
  updated: "2026-04-11"
---
# Threat Mitigation Mapping

Connect threats to controls for effective security planning.

## When to Use This Skill

- Prioritizing security investments
- Creating remediation roadmaps
- Validating control coverage
- Designing defense-in-depth
- Security architecture review
- Risk treatment planning

## Core Concepts

### 1. Control Categories

```
Preventive ────► Stop attacks before they occur
   │              (Firewall, Input validation)
   │
Detective ─────► Identify attacks in progress
   │              (IDS, Log monitoring)
   │
Corrective ────► Respond and recover from attacks
                  (Incident response, Backup restore)
```

### 2. Control Layers

| Layer | Examples |
|-------|----------|
| **Network** | Firewall, WAF, DDoS protection |
| **Application** | Input validation, authentication |
| **Data** | Encryption, access controls |
| **Endpoint** | EDR, patch management |
| **Process** | Security training, incident response |

### 3. Defense in Depth

```
                    ┌──────────────────────┐
                    │      Perimeter       │ ← Firewall, WAF
                    │   ┌──────────────┐   │
                    │   │   Network    │   │ ← Segmentation, IDS
                    │   │  ┌────────┐  │   │
                    │   │  │  Host  │  │   │ ← EDR, Hardening
                    │   │  │ ┌────┐ │  │   │
                    │   │  │ │App │ │  │   │ ← Auth, Validation
                    │   │  │ │Data│ │  │   │ ← Encryption
                    │   │  │ └────┘ │  │   │
                    │   │  └────────┘  │   │
                    │   └──────────────┘   │
                    └──────────────────────┘
```

## Templates

### Template 1: Mitigation Model

```python
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Set
from datetime import datetime

class ControlType(Enum):
    PREVENTIVE = "preventive"
    DETECTIVE = "detective"
    CORRECTIVE = "corrective"


class ControlLayer(Enum):
    NETWORK = "network"
    APPLICATION = "application"
    DATA = "data"
    ENDPOINT = "endpoint"
    PROCESS = "process"
    PHYSICAL = "physical"


class ImplementationStatus(Enum):
    NOT_IMPLEMENTED = "not_implemented"
    PARTIAL = "partial"
    IMPLEMENTED = "implemented"
    VERIFIED = "verified"


class Effectiveness(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


@dataclass
class SecurityControl:
    id: str
    name: str
    description: str
    control_type: ControlType
    layer: ControlLayer
    effectiveness: Effectiveness
    implementation_cost: str  # Low, Medium, High
    maintenance_cost: str
    status: ImplementationStatus = ImplementationStatus.NOT_IMPLEMENTED
    mitigates_threats: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    technologies: List[str] = field(default_factory=list)
    compliance_refs: List[str] = field(default_factory=list)

    def coverage_score(self) -> float:
        """Calculate coverage score based on status and effectiveness."""
        status_multiplier = {
            ImplementationStatus.NOT_IMPLEMENTED: 0.0,
            ImplementationStatus.PARTIAL: 0.5,
            ImplementationStatus.IMPLEMENTED: 0.8,
            ImplementationStatus.VERIFIED: 1.0,
        }
        return self.effectiveness.value * status_multiplier[self.status]


@dataclass
class Threat:
    id: str
    name: str
    category: str  # STRIDE category
    description: str
    impact: str  # Critical, High, Medium, Low
    likelihood: str
    risk_score: float


@dataclass
class MitigationMapping:
    threat: Threat
    controls: List[SecurityControl]
    residual_risk: str = "Unknown"
    notes: str = ""

    def calculate_coverage(self) -> float:
        """Calculate how well controls cover the threat."""
        if not self.controls:
            return 0.0

        total_score = sum(c.coverage_score() for c in self.controls)
        max_possible = len(self.controls) * Effectiveness.VERY_HIGH.value

        return (total_score / max_possible) * 100 if max_possible > 0 else 0

    def has_defense_in_depth(self) -> bool:
        """Check if multiple layers are covered."""
        layers = set(c.layer for c in self.controls if c.status != ImplementationStatus.NOT_IMPLEMENTED)
        return len(layers) >= 2

    def has_control_diversity(self) -> bool:
        """Check if multiple control types are present."""
        types = set(c.control_type for c in self.controls if c.status != ImplementationStatus.NOT_IMPLEMENTED)
        return len(types) >= 2


@dataclass
class MitigationPlan:
    name: str
    threats: List[Threat] = field(default_factory=list)
    controls: List[SecurityControl] = field(default_factory=list)
    mappings: List[MitigationMapping] = field(default_factory=list)

    def get_unmapped_threats(self) -> List[Threat]:
        """Find threats without mitigations."""
        mapped_ids = {m.threat.id for m in self.mappings}
        return [t for t in self.threats if t.id not in mapped_ids]

    def get_control_coverage(self) -> Dict[str, float]:
        """Get coverage percentage for each threat."""
        return {
            m.threat.id: m.calculate_coverage()
            for m in self.mappings
        }

    def get_gaps(self) -> List[Dict]:
        """Identify mitigation gaps."""
        gaps = []
        for mapping in self.mappings:
            coverage = mapping.calculate_coverage()
            if coverage < 50:
                gaps.append({
                    "threat": mapping.threat.id,
                    "threat_name": mapping.threat.name,
                    "coverage": coverage,
                    "issue": "Insufficient control coverage",
                    "recommendation": "Add more controls or improve existing ones"
                })
            if not mapping.has_defense_in_depth():
                gaps.append({
                    "threat": mapping.threat.id,
                    "threat_name": mapping.threat.name,
                    "coverage": coverage,
                    "issue": "No defense in depth",
                    "recommendation": "Add controls at different layers"
                })
            if not mapping.has_control_diversity():
                gaps.append({
                    "threat": mapping.threat.id,
                    "threat_name": mapping.threat.name,
                    "coverage": coverage,
                    "issue": "No control diversity",
                    "recommendation": "Add detective/corrective controls"
                })
        return gaps
```

### Template 2: Control Library

```python
class ControlLibrary:
    """Library of standard security controls."""

    STANDARD_CONTROLS = {
        # Authentication Controls
        "AUTH-001": SecurityControl(
            id="AUTH-001",
            name="Multi-Factor Authentication",
            description="Require MFA for all user authentication",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="Medium",
            maintenance_cost="Low",
            mitigates_threats=["SPOOFING"],
            technologies=["TOTP", "WebAuthn", "SMS OTP"],
            compliance_refs=["PCI-DSS 8.3", "NIST 800-63B"]
        ),
        "AUTH-002": SecurityControl(
            id="AUTH-002",
            name="Account Lockout Policy",
            description="Lock accounts after failed authentication attempts",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.MEDIUM,
            implementation_cost="Low",
            maintenance_cost="Low",
            mitigates_threats=["SPOOFING"],
            technologies=["Custom implementation"],
            compliance_refs=["PCI-DSS 8.1.6"]
        ),

        # Input Validation Controls
        "VAL-001": SecurityControl(
            id="VAL-001",
            name="Input Validation Framework",
            description="Validate and sanitize all user input",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="Medium",
            maintenance_cost="Medium",
            mitigates_threats=["TAMPERING", "INJECTION"],
            technologies=["Joi", "Yup", "Pydantic"],
            compliance_refs=["OWASP ASVS V5"]
        ),
        "VAL-002": SecurityControl(
            id="VAL-002",
            name="Web Application Firewall",
            description="Deploy WAF to filter malicious requests",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.NETWORK,
            effectiveness=Effectiveness.MEDIUM,
            implementation_cost="Medium",
            maintenance_cost="Medium",
            mitigates_threats=["TAMPERING", "INJECTION", "DOS"],
            technologies=["AWS WAF", "Cloudflare", "ModSecurity"],
            compliance_refs=["PCI-DSS 6.6"]
        ),

        # Encryption Controls
        "ENC-001": SecurityControl(
            id="ENC-001",
            name="Data Encryption at Rest",
            description="Encrypt sensitive data in storage",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.DATA,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="Medium",
            maintenance_cost="Low",
            mitigates_threats=["INFORMATION_DISCLOSURE"],
            technologies=["AES-256", "KMS", "HSM"],
            compliance_refs=["PCI-DSS 3.4", "GDPR Art. 32"]
        ),
        "ENC-002": SecurityControl(
            id="ENC-002",
            name="TLS Encryption",
            description="Encrypt data in transit using TLS 1.3",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.NETWORK,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="Low",
            maintenance_cost="Low",
            mitigates_threats=["INFORMATION_DISCLOSURE", "TAMPERING"],
            technologies=["TLS 1.3", "Certificate management"],
            compliance_refs=["PCI-DSS 4.1", "HIPAA"]
        ),

        # Logging Controls
        "LOG-001": SecurityControl(
            id="LOG-001",
            name="Security Event Logging",
            description="Log all security-relevant events",
            control_type=ControlType.DETECTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.MEDIUM,
            implementation_cost="Low",
            maintenance_cost="Medium",
            mitigates_threats=["REPUDIATION"],
            technologies=["ELK Stack", "Splunk", "CloudWatch"],
            compliance_refs=["PCI-DSS 10.2", "SOC2"]
        ),
        "LOG-002": SecurityControl(
            id="LOG-002",
            name="Log Integrity Protection",
            description="Protect logs from tampering",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.DATA,
            effectiveness=Effectiveness.MEDIUM,
            implementation_cost="Medium",
            maintenance_cost="Low",
            mitigates_threats=["REPUDIATION", "TAMPERING"],
            technologies=["Immutable storage", "Log signing"],
            compliance_refs=["PCI-DSS 10.5"]
        ),

        # Access Control
        "ACC-001": SecurityControl(
            id="ACC-001",
            name="Role-Based Access Control",
            description="Implement RBAC for authorization",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="Medium",
            maintenance_cost="Medium",
            mitigates_threats=["ELEVATION_OF_PRIVILEGE", "INFORMATION_DISCLOSURE"],
            technologies=["RBAC", "ABAC", "Policy engines"],
            compliance_refs=["PCI-DSS 7.1", "SOC2"]
        ),

        # Availability Controls
        "AVL-001": SecurityControl(
            id="AVL-001",
            name="Rate Limiting",
            description="Limit request rates to prevent abuse",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.APPLICATION,
            effectiveness=Effectiveness.MEDIUM,
            implementation_cost="Low",
            maintenance_cost="Low",
            mitigates_threats=["DENIAL_OF_SERVICE"],
            technologies=["API Gateway", "Redis", "Token bucket"],
            compliance_refs=["OWASP API Security"]
        ),
        "AVL-002": SecurityControl(
            id="AVL-002",
            name="DDoS Protection",
            description="Deploy DDoS mitigation services",
            control_type=ControlType.PREVENTIVE,
            layer=ControlLayer.NETWORK,
            effectiveness=Effectiveness.HIGH,
            implementation_cost="High",
            maintenance_cost="Medium",
            mitigates_threats=["DENIAL_OF_SERVICE"],
            technologies=["Cloudflare", "AWS Shield", "Akamai"],
            compliance_refs=["NIST CSF"]
        ),
    }

    def get_controls_for_threat(self, threat_category: str) -> List[SecurityControl]:
        """Get all controls that mitigate a threat category."""
        return [
            c for c in self.STANDARD_CONTROLS.values()
            if threat_category in c.mitigates_threats
        ]

    def get_controls_by_layer(self, layer: ControlLayer) -> List[SecurityControl]:
        """Get controls for a specific layer."""
        return [c for c in self.STANDARD_CONTROLS.values() if c.layer == layer]

    def get_control(self, control_id: str) -> Optional[SecurityControl]:
        """Get a specific control by ID."""
        return self.STANDARD_CONTROLS.get(control_id)

    def recommend_controls(
        self,
        threat: Threat,
        existing_controls: List[str]
    ) -> List[SecurityControl]:
        """Recommend additional controls for a threat."""
        available = self.get_controls_for_threat(threat.category)
        return [c for c in available if c.id not in existing_controls]
```

## Advanced Analysis, Control Testing, Best Practices & Resources

Risk reduction calculation (weighted by threat risk score), critical gap identification, budget optimization (greedy algorithm ranking controls by effectiveness/cost ratio), Phase 1/2 implementation roadmap (critical then high-impact threats), defense-in-depth analysis by layer, comprehensive report generation with format helpers, control effectiveness testing (ControlTest dataclass + ControlTester with async `run_tests`/`get_effectiveness_score`/`generate_test_report`), Best Practices (Do's/Don'ts), Resources (NIST/CIS/MITRE D3FEND).

See [references/advanced-analysis-and-testing.md](references/advanced-analysis-and-testing.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-analysis-and-testing.md` | MitigationAnalyzer, ControlEffectivenessTesting, best practices, resources |
