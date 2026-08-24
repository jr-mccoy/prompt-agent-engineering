---
title: "Sensor Integration & Data Collection Pipeline Review"
category: software-engineering/embedded
description: "Analyze sensor integration code and data pipelines for accuracy, reliability, power efficiency, and data integrity."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - sensors
  - data-collection
  - adc
  - i2c
  - spi
  - filtering
  - calibration
  - telemetry
  - data-pipeline
updated: "2026-03-19"
---

# Sensor Integration & Data Collection Pipeline Review

**Objective:** Review a sensor data acquisition and processing pipeline for measurement accuracy, data integrity, power efficiency, and reliable delivery from sensor through to storage or cloud, then provide prioritized recommendations.

---

## Inputs / Context

**Required:**
- **Source code:** Sensor driver, data acquisition loop, processing/filtering, and transmission code
- **Sensor(s):** Type and model (e.g., BME280 temperature/humidity, MPU6050 IMU, ADS1115 ADC)
- **Pipeline scope:** How far the data flows — local logging, gateway, or cloud endpoint

**Optional:**
- Sensor datasheets or specifications
- Sampling rate requirements and measurement accuracy targets
- Power budget for the sensing system
- Data format and protocol for upstream transmission
- Environmental conditions (temperature range, vibration, electromagnetic interference)
- Calibration requirements or reference standards

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify sensor configuration matches datasheet recommendations for the target accuracy
- Check the complete data path from raw sensor reading to final stored/transmitted value
- Assess data integrity at each pipeline stage (acquisition → filtering → storage → transmission)
- Consider sensor physics: settling time, warm-up period, cross-sensitivity

**Must Not:**
- Assume sensor readings are accurate without calibration or validation checks
- Ignore the timing relationship between sampling rate and signal bandwidth (Nyquist)
- Recommend filtering without understanding the signal characteristics and noise sources

---

## Steps

1. **Sensor Configuration Review**
   For each sensor:
   a. **Interface Setup:** Verify bus configuration (I2C address, SPI mode, ADC reference voltage) matches sensor requirements
   b. **Operating Mode:** Check measurement mode (continuous, one-shot, triggered) matches sampling strategy
   c. **Resolution & Range:** Verify configured resolution and full-scale range are appropriate for the measured quantity
   d. **Sampling Rate:** Verify internal ODR (output data rate) is set correctly; check oversampling settings
   e. **Power Mode:** Assess power consumption of the chosen mode; flag unnecessarily high power modes
   f. **Initialization Sequence:** Verify warm-up time is respected before first reading; check self-test or WHO_AM_I register verification

2. **Data Acquisition Analysis**
   - **Timing:** Verify sample interval matches requirements; check for timing drift over long periods
   - **Read Sequence:** For multi-byte reads, verify byte order (MSB/LSB) and that all bytes are read atomically (data-ready latch)
   - **Data-Ready Handling:** Check for proper use of data-ready pin/interrupt vs. polling; flag reading when data is not fresh
   - **Multi-Sensor Synchronization:** If multiple sensors are read, check for time alignment between readings
   - **Conversion:** Verify raw-to-engineering-unit conversion formulas match the datasheet (scaling factors, offsets, compensation formulas)
   - **Overflow/Saturation:** Check behavior when sensor reading hits full-scale limits

3. **Signal Processing & Filtering**
   - **Noise Assessment:** Identify noise sources (quantization, EMI, sensor self-noise) and their frequency characteristics
   - **Filter Selection:** Evaluate filter choice for the application:
     | Filter Type | Good For | Watch Out For |
     |------------|---------|--------------|
     | Moving average | Smoothing white noise | Phase delay, step response lag |
     | Exponential (EMA) | Low-memory smoothing | Limited attenuation, tuning alpha |
     | Median filter | Spike/outlier removal | Poor for rapid changes |
     | Low-pass (IIR/FIR) | Band-limited signals | Computational cost, stability |
     | Kalman filter | Sensor fusion, prediction | Complexity, model accuracy |
   - **Filter Parameterization:** Verify cutoff frequency, window size, or alpha value is appropriate for the signal dynamics
   - **Outlier Handling:** Check for range validation, sanity checks, and anomaly detection before data enters the pipeline
   - **Calibration:** Verify offset and gain calibration is applied; check for temperature compensation if sensor is temperature-sensitive

4. **Data Integrity Through Pipeline**
   At each stage, verify:
   - **Buffering:** Ring buffer or queue sizing for burst handling; check for overflow behavior (drop oldest vs. block)
   - **Timestamping:** Each sample should carry a timestamp; verify clock source accuracy and drift compensation
   - **Data Loss Detection:** Check for sequence numbers or gap detection in the pipeline
   - **Type Safety:** Verify no precision loss in type conversions (uint16 → float, integer division rounding)
   - **Endianness:** Check byte order consistency when packing data for storage or transmission
   - **Serialization:** Verify encoding correctness (JSON field names, Protobuf field numbers, CBOR types)

5. **Storage & Transmission**
   - **Local Storage:**
     - File format efficiency (CSV vs. binary vs. structured)
     - Storage capacity planning (bytes per sample × samples per day × retention period)
     - Write wear management for flash storage (wear leveling, write buffering)
     - Corruption recovery (checksums, journaling, append-only writes)
   - **Transmission:**
     - Batch size optimization (transmission overhead vs. latency)
     - Retry and acknowledgment handling for failed transmissions
     - Compression opportunities for bandwidth-constrained links
     - Store-and-forward for intermittent connectivity

6. **Power Optimization**
   - Sensor duty cycling: power down between samples vs. continuous mode
   - MCU sleep between acquisition cycles; verify wake-up time fits the sampling window
   - Batch processing: accumulate data during low-power periods, process and transmit in bursts
   - Adaptive sampling: increase rate only when signal changes are detected

7. **Reliability & Edge Cases**
   - Sensor failure detection: stuck values, out-of-range readings, communication errors
   - Graceful degradation: continue operating with reduced sensor set if one fails
   - Environmental extremes: verify sensor accuracy at temperature/humidity boundaries
   - Long-term stability: sensor drift over weeks/months; recalibration triggers

---

## False-Positive Prevention

- ❌ Do NOT flag missing filtering for high-resolution, low-noise sensors in stable environments
- ❌ Do NOT flag JSON payload format on bandwidth-rich connections
- ❌ Do NOT flag continuous sensor mode when the sampling rate genuinely requires it
- ❌ Do NOT require Kalman filtering when a simple moving average meets accuracy requirements
- ✅ DO flag missing datasheet conversion formulas (raw → engineering units)
- ✅ DO flag missing data-ready checks before reading sensor registers
- ✅ DO flag buffer overflows that silently drop data without notification
- ✅ DO flag missing timestamps on sensor readings
- ✅ DO flag integer division in conversion formulas that causes precision loss

---

## Output Format

### Pipeline Overview
```
Sensors: [list with models and interfaces]
Sampling Rate: [Hz per sensor]
Processing: [filter types applied]
Storage: [local format / destination]
Transmission: [protocol / destination]
Pipeline Latency: [sensor → cloud estimated time]
```

### Sensor Configuration Audit
| Sensor | Interface | Mode | ODR | Range | Accuracy | Status |
|--------|----------|------|-----|-------|----------|--------|
| [model] | [I2C/SPI/ADC] | [mode] | [Hz] | [range] | [±units] | ✅/⚠️/❌ |

### Critical Findings
For each:
- **ID:** SENS-CRIT-[N]
- **Location:** [file:line]
- **Pipeline Stage:** [Acquisition | Processing | Storage | Transmission]
- **Issue:** [description]
- **Impact:** [data loss / measurement error / pipeline stall / power waste]
- **Fix:** [specific code change or configuration adjustment]

### Data Integrity Checklist
| Check | Status | Notes |
|-------|--------|-------|
| Raw → engineering unit conversion verified | ✅/❌ | |
| Timestamps on all samples | ✅/❌ | |
| Buffer overflow handling | ✅/❌ | |
| Sequence/gap detection | ✅/❌ | |
| Transmission retry on failure | ✅/❌ | |
| Storage corruption protection | ✅/❌ | |

### Power Budget (Sensing Subsystem)
| Phase | Current | Duration | Frequency | Daily Energy |
|-------|---------|----------|-----------|-------------|
| Sensor active | [mA] | [ms] | [per day] | [mAh] |
| MCU processing | [mA] | [ms] | [per day] | [mAh] |
| Transmission | [mA] | [ms] | [per day] | [mAh] |
| Sleep | [μA] | [hours] | continuous | [mAh] |

### Recommended Actions
| Priority | Action | Pipeline Stage | Effort |
|----------|--------|---------------|--------|
| Critical | [action] | [stage] | [estimate] |

---

## Verification

After completing the analysis, explicitly answer:
1. Did I verify conversion formulas against the sensor datasheet, not assumptions?
2. Did I trace the complete data path from raw register read to final output?
3. Did I check for data loss opportunities at every buffer boundary and transmission point?

---

**Techniques Used:** ST-01 (Clear Objective), ST-02 (Structured Sequential), RT-02 (Multi-Dimensional Analysis), RT-05 (Evidence-Based), DS-06 (Prioritization), CM-01 (Context Framing), QA-01 (Verification)
