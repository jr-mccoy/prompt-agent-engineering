# SBOM Formats Reference

> Comprehensive comparison of SPDX and CycloneDX SBOM formats.

## Overview

Two primary SBOM formats dominate the industry:

| Format | Organization | Focus | Standard |
|--------|-------------|-------|----------|
| **SPDX** | Linux Foundation | License compliance + security | ISO/IEC 5962:2021 |
| **CycloneDX** | OWASP | Security-first, lightweight | ECMA-424 |

Both formats can represent the same core information but have different strengths.

---

## SPDX (Software Package Data Exchange)

### Overview

SPDX originated for license compliance but has evolved to support security use cases. It's the only SBOM format with ISO standardization.

### Versions

| Version | Released | Key Features |
|---------|----------|--------------|
| SPDX 2.2 | 2020 | Relationships, annotations |
| SPDX 2.3 | 2022 | Security references, improved packaging |
| SPDX 3.0 | 2024 | Profiles (lite, security, licensing), AI/ML support |

### Output Formats

- **JSON** (`.spdx.json`) - Most common for automation
- **Tag-Value** (`.spdx`) - Human-readable text format
- **RDF/XML** - For semantic web integration
- **YAML** - Human-readable structured format
- **Spreadsheet** - For manual review

### Structure (SPDX 2.3 JSON)

```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "my-application",
  "documentNamespace": "https://example.com/sbom/my-application-1.0.0",
  "creationInfo": {
    "created": "2024-01-15T10:30:00Z",
    "creators": [
      "Tool: syft-0.98.0",
      "Organization: Example Corp"
    ]
  },
  "packages": [
    {
      "SPDXID": "SPDXRef-Package-lodash",
      "name": "lodash",
      "versionInfo": "4.17.21",
      "supplier": "Organization: Lodash",
      "downloadLocation": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "filesAnalyzed": false,
      "licenseConcluded": "MIT",
      "licenseDeclared": "MIT",
      "copyrightText": "NOASSERTION",
      "externalRefs": [
        {
          "referenceCategory": "SECURITY",
          "referenceType": "cpe23Type",
          "referenceLocator": "cpe:2.3:a:lodash:lodash:4.17.21:*:*:*:*:*:*:*"
        },
        {
          "referenceCategory": "PACKAGE-MANAGER",
          "referenceType": "purl",
          "referenceLocator": "pkg:npm/lodash@4.17.21"
        }
      ],
      "checksums": [
        {
          "algorithm": "SHA256",
          "checksumValue": "abc123..."
        }
      ]
    }
  ],
  "relationships": [
    {
      "spdxElementId": "SPDXRef-DOCUMENT",
      "relationshipType": "DESCRIBES",
      "relatedSpdxElement": "SPDXRef-Package-my-application"
    },
    {
      "spdxElementId": "SPDXRef-Package-my-application",
      "relationshipType": "DEPENDS_ON",
      "relatedSpdxElement": "SPDXRef-Package-lodash"
    }
  ]
}
```

### Key Fields

| Field | Description | Required |
|-------|-------------|----------|
| `spdxVersion` | SPDX spec version | Yes |
| `SPDXID` | Unique identifier for element | Yes |
| `name` | Package name | Yes |
| `versionInfo` | Package version | No (recommended) |
| `downloadLocation` | Where to get package | Yes |
| `licenseConcluded` | License determination | Yes |
| `externalRefs` | PURLs, CPEs, security refs | No |
| `checksums` | File/package hashes | No (recommended) |
| `relationships` | How packages relate | No |

### Relationship Types

| Type | Meaning |
|------|---------|
| `DEPENDS_ON` | Runtime dependency |
| `DEV_DEPENDENCY_OF` | Development dependency |
| `BUILD_TOOL_OF` | Used to build |
| `CONTAINS` | Package contains file/subpackage |
| `GENERATES` | Source generates artifact |
| `ANCESTOR_OF` | Older version |

### Strengths

- ISO standardized (ISO/IEC 5962:2021)
- Rich licensing information
- Strong relationship modeling
- Government/enterprise adoption (NTIA minimum elements)
- Multiple serialization formats

### Limitations

- More verbose than CycloneDX
- Historically focused on licensing
- Steeper learning curve

---

## CycloneDX

### Overview

Created by OWASP specifically for security use cases. Designed to be lightweight and easy to generate/consume.

### Versions

| Version | Released | Key Features |
|---------|----------|--------------|
| CycloneDX 1.4 | 2022 | Vulnerabilities, services |
| CycloneDX 1.5 | 2023 | Machine learning BOM, formulation |
| CycloneDX 1.6 | 2024 | Attestations, cryptographic assets |

### Output Formats

- **JSON** (`.cdx.json`) - Most common
- **XML** (`.cdx.xml`) - Original format
- **Protocol Buffers** - For high-performance systems

### Structure (CycloneDX 1.5 JSON)

```json
{
  "$schema": "http://cyclonedx.org/schema/bom-1.5.schema.json",
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "serialNumber": "urn:uuid:3e671687-395b-41f5-a30f-a58921a69b79",
  "version": 1,
  "metadata": {
    "timestamp": "2024-01-15T10:30:00Z",
    "tools": [
      {
        "vendor": "Anchore",
        "name": "syft",
        "version": "0.98.0"
      }
    ],
    "authors": [
      {
        "name": "Security Team",
        "email": "security@example.com"
      }
    ],
    "component": {
      "type": "application",
      "name": "my-application",
      "version": "1.0.0"
    }
  },
  "components": [
    {
      "type": "library",
      "bom-ref": "pkg:npm/lodash@4.17.21",
      "name": "lodash",
      "version": "4.17.21",
      "purl": "pkg:npm/lodash@4.17.21",
      "licenses": [
        {
          "license": {
            "id": "MIT"
          }
        }
      ],
      "hashes": [
        {
          "alg": "SHA-256",
          "content": "abc123..."
        }
      ],
      "externalReferences": [
        {
          "type": "website",
          "url": "https://lodash.com"
        },
        {
          "type": "vcs",
          "url": "https://github.com/lodash/lodash"
        }
      ]
    }
  ],
  "dependencies": [
    {
      "ref": "pkg:npm/my-application@1.0.0",
      "dependsOn": [
        "pkg:npm/lodash@4.17.21"
      ]
    }
  ],
  "vulnerabilities": [
    {
      "id": "CVE-2021-23337",
      "source": {
        "name": "NVD",
        "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-23337"
      },
      "ratings": [
        {
          "source": {
            "name": "NVD"
          },
          "score": 7.2,
          "severity": "high",
          "method": "CVSSv3"
        }
      ],
      "affects": [
        {
          "ref": "pkg:npm/lodash@4.17.21"
        }
      ]
    }
  ]
}
```

### Key Fields

| Field | Description | Required |
|-------|-------------|----------|
| `bomFormat` | Always "CycloneDX" | Yes |
| `specVersion` | CycloneDX version | Yes |
| `serialNumber` | Unique UUID | No (recommended) |
| `metadata` | Document metadata | No |
| `components` | List of packages | No |
| `dependencies` | Dependency graph | No |
| `vulnerabilities` | Known vulns | No |
| `services` | External services used | No |

### Component Types

| Type | Description |
|------|-------------|
| `application` | Software application |
| `library` | Software library |
| `framework` | Application framework |
| `container` | Container image |
| `operating-system` | OS component |
| `device` | Hardware device |
| `firmware` | Device firmware |
| `file` | Individual file |
| `machine-learning-model` | ML model (v1.5+) |
| `data` | Dataset (v1.5+) |

### Strengths

- Security-focused from inception
- Native vulnerability tracking
- Lightweight and easy to parse
- Rapid specification evolution
- Service dependencies modeling
- ML/AI asset support (v1.5+)

### Limitations

- Less mature than SPDX
- Fewer serialization formats
- Less extensive relationship modeling

---

## Format Comparison

### Feature Matrix

| Feature | SPDX 2.3 | CycloneDX 1.5 |
|---------|----------|---------------|
| **License tracking** | Excellent | Good |
| **Vulnerability tracking** | Via external refs | Native |
| **Dependency graph** | Relationships | Dependencies |
| **File-level detail** | Excellent | Good |
| **Service dependencies** | Limited | Native |
| **ML/AI components** | SPDX 3.0 | Native (1.5+) |
| **Cryptographic assets** | No | Native (1.6) |
| **ISO standardized** | Yes | No (ECMA-424) |
| **JSON support** | Yes | Yes |
| **XML support** | Via RDF | Yes |
| **Human-readable** | Tag-value format | No |

### Size Comparison

For the same application, typical file sizes:

| Format | File Size |
|--------|-----------|
| SPDX JSON | 1.5x baseline |
| SPDX Tag-Value | 1.2x baseline |
| CycloneDX JSON | 1.0x baseline |
| CycloneDX XML | 1.1x baseline |

### Tool Support

| Tool | SPDX | CycloneDX |
|------|------|-----------|
| Syft | Yes | Yes |
| Trivy | Yes | Yes |
| cdxgen | No | Yes |
| spdx-sbom-generator | Yes | No |
| Grype (vulnerability scan) | Yes | Yes |
| Dependency-Track | Yes | Yes (native) |
| OWASP Dependency-Check | No | Yes |

---

## Decision Guide

### Choose SPDX when:

- **License compliance is primary concern**
  - Legal/compliance teams need detailed license info
  - Government contracts require SPDX

- **ISO standardization required**
  - Enterprise policies mandate ISO standards
  - International compliance requirements

- **Rich file-level detail needed**
  - Tracking individual file licenses
  - Detailed copyright attribution

- **NTIA minimum elements required**
  - US government SBOM requirements
  - SPDX designed to meet these

### Choose CycloneDX when:

- **Security is primary concern**
  - Vulnerability tracking is key
  - Integration with security tools

- **Lightweight format preferred**
  - High-volume SBOM generation
  - CI/CD pipeline integration

- **Modern tech stack**
  - ML/AI components
  - Microservices architecture
  - Cloud-native applications

- **Rapid iteration needed**
  - Frequent specification updates
  - Modern features (attestations, etc.)

### Using Both

Many organizations generate both formats:

```yaml
# Generate both formats
- name: Generate SPDX SBOM
  run: syft scan . -o spdx-json=sbom.spdx.json

- name: Generate CycloneDX SBOM
  run: syft scan . -o cyclonedx-json=sbom.cdx.json
```

---

## Conversion

### SPDX to CycloneDX

```bash
# Using cdx-cli
cyclonedx convert --input sbom.spdx.json --output sbom.cdx.json

# Using protobom
protobom convert sbom.spdx.json --format cyclonedx
```

### CycloneDX to SPDX

```bash
# Using cdx-cli
cyclonedx convert --input sbom.cdx.json --output sbom.spdx.json --format spdx

# Note: Some CycloneDX fields may not have SPDX equivalents
```

### Conversion Limitations

| Direction | Potential Data Loss |
|-----------|---------------------|
| SPDX → CycloneDX | Detailed file relationships, some license nuances |
| CycloneDX → SPDX | Vulnerability details, service info, ML components |

---

## Minimum Viable SBOM

Per NTIA minimum elements, an SBOM should include:

| Element | SPDX Field | CycloneDX Field |
|---------|------------|-----------------|
| Supplier name | `supplier` | `supplier.name` |
| Component name | `name` | `name` |
| Version | `versionInfo` | `version` |
| Unique identifier | `SPDXID` + `externalRefs[purl]` | `bom-ref` + `purl` |
| Dependency relationship | `relationships` | `dependencies` |
| Author of SBOM | `creationInfo.creators` | `metadata.authors` |
| Timestamp | `creationInfo.created` | `metadata.timestamp` |

---

## Resources

### SPDX
- [SPDX Specification](https://spdx.github.io/spdx-spec/)
- [SPDX Tools](https://tools.spdx.org/)
- [SPDX License List](https://spdx.org/licenses/)

### CycloneDX
- [CycloneDX Specification](https://cyclonedx.org/specification/overview/)
- [CycloneDX Tool Center](https://cyclonedx.org/tool-center/)
- [CycloneDX Use Cases](https://cyclonedx.org/use-cases/)

### General
- [NTIA SBOM Minimum Elements](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)
- [CISA SBOM Resources](https://www.cisa.gov/sbom)
