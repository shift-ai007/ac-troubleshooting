# TXV (Thermal Expansion Valve) Diagnostic Guide

The thermal expansion valve (TXV) is a precision metering device that controls how much liquid refrigerant enters your AC's evaporator coil. When it fails, your system loses its ability to regulate cooling — causing temperature swings, poor dehumidification, and compressor damage.

## What a TXV Does

Unlike older fixed-orifice systems that use a simple brass restrictor, a TXV actively adjusts refrigerant flow based on conditions:

```
TXV parts:
  Sensing bulb (on suction line) → measures superheat temperature
  Equalizer tube → measures suction pressure
  Diaphragm → compares temperature vs pressure
  Needle valve → opens/closes to adjust flow
```

The TXV's job is to maintain a constant superheat (typically 8-12°F) at the evaporator outlet — regardless of indoor temperature, outdoor temperature, or load conditions. This makes modern high-SEER systems more efficient but also more sensitive to component failure.

## TXV vs Fixed Orifice

| Feature | Fixed Orifice | TXV |
|---------|---------------|-----|
| Cost | $5-15 | $40-120 |
| Efficiency | Lower (especially on mild days) | Higher across all conditions |
| Failure rate | Very low (no moving parts) | Moderate |
| Diagnostic complexity | Simple | Requires pressure/temperature measurements |
| Best for | Budget systems, simple climates | High-SEER systems, variable conditions |

South Florida's wide temperature swings (68°F mornings to 95°F afternoons) are exactly the conditions where a TXV outperforms a fixed orifice — when it's working correctly.

## Common TXV Failures

### Stuck Open

The TXV allows too much liquid refrigerant into the evaporator. Liquid refrigerant returns to the compressor (slugging).

**Symptoms**:
- Suction line feels abnormally cold (could ice up)
- Liquid flooding sound at the compressor
- System may trip on low-superheat or freeze-protection lockout
- Compressor runs rough or noisy
- Eventually: [compressor lockout protection](ac-lockout-protection.md) engages

### Stuck Closed

The TXV restricts refrigerant flow too much. The evaporator starves.

**Symptoms**:
- Evaporator coil only partially cold
- Suction pressure reads low
- Superheat reads high (30°F+)
- System runs continuously but never reaches set temperature
- High discharge temperature — can damage compressor valves

### Sensing Bulb Failure

The TXV's sensing bulb (clamped to the suction line) must make perfect thermal contact. If the bulb loses contact, the TXV gets wrong temperature readings.

**Symptoms**:
- Erratic superheat readings (wildly fluctuating on consecutive measurements)
- Symptoms alternate between stuck-open and stuck-closed behavior
- May be temperature-sensitive (works at night, fails mid-afternoon)

### External Equalizer Blockage

The equalizer tube connects the TXV diaphragm to the evaporator outlet. If blocked (by debris, kink, or ice), the TXV can't sense evaporator pressure.

**Symptoms**:
- Superheat drifts over time
- System never stabilizes after startup
- Responds poorly to load changes

## Diagnosing TXV Problems

### Tools Needed
- **Manifold gauge set** or digital pressure probes
- **Clamp thermometer** (for suction line temperature)
- **K-type thermocouple** for superheat/subcooling calculation

### Step 1: Check for Basic Problems First

Before assuming TXV failure, rule out simpler causes:

1. [Dirty air filter](not-cooling.md) — Restricted airflow changes evaporator conditions
2. Dirty evaporator coil — Same effect as clogged filter
3. [Bad capacitor](capacitor-testing-guide.md) — Low voltage to compressor affects pressures
4. [Low refrigerant](wont-turn-on.md) — Undercharge mimics stuck-closed TXV

### Step 2: Measure Superheat

1. Run the system for 15+ minutes to stabilize
2. Measure suction pressure (low side) → convert to saturation temperature using a PT chart
3. Measure actual suction line temperature (6 inches from compressor on the large line)
4. Subtract: **Actual Temp - Saturation Temp = Superheat**

| Superheat Reading | Likely Cause |
|-------------------|-------------|
| 0-5°F | TXV stuck open (or overcharged) |
| 8-12°F | Normal range — good TXV |
| 15-25°F | TXV stuck closed (or undercharged) |
| 30°F+ | TXV stuck closed (severe) — stop running system |
| Fluctuates wildly | Sensing bulb issue, equalizer blockage |

### Step 3: Check Subcooling

1. Measure liquid pressure (high side) → convert to saturation temp
2. Measure actual liquid line temperature
3. Subtract: **Saturation Temp - Actual Temp = Subcooling**

Normal subcooling for a TXV system: **8-14°F** (varies by manufacturer — check the unit nameplate).

- **High subcooling** (18°F+): Refrigerant backed up in condenser — points toward TXV restricting flow
- **Low subcooling** (below 5°F): Low refrigerant or TXV overfeeding

### Step 4: Thermal Response Test

1. Warm the TXV sensing bulb with your hand (or a warm cloth)
2. A working TXV should respond by opening — suction pressure rises
3. Cool the bulb with a cold cloth or ice pack (wrapped in a bag)
4. A working TXV should respond by closing — suction pressure drops

If the TXV doesn't respond to temperature changes, the valve is mechanically stuck and needs replacement.

## TXV Replacement Considerations

| Factor | Details |
|--------|---------|
| Cost (part) | $40-120 depending on brand and capacity |
| Cost (labor) | $300-600 — requires refrigerant recovery and evacuation |
| Total with refrigerant | $500-900 |
| Time | 2-3 hours |
| Compatibility | Must match system tonnage AND refrigerant type |
| **Versus replacement** | If system is 12+ years old, [replacement](https://ac-repair.today/services/ac-replacement/) often costs less per year of remaining life |

**⚠️ Important**: TXV replacement requires:
- Full refrigerant recovery and storage (EPA requirement)
- Deep vacuum below 500 microns
- Proper charge by subcooling (superheat method doesn't work for TXV systems)
- Replacement of filter-drier (always replaced when the system is opened)

## South Florida-Specific TXV Issues

### Power Surge Damage
Frequent thunderstorms mean power surges. Surges can damage the TXV's internal components (especially on electronically controlled TXVs found in 18+ SEER systems). Install a whole-home surge protector if you have a high-efficiency system.

### Heat-Related Failure
TXV bodies mounted inches above hot condenser coils can exceed their rated temperature range. Some TXV installations near compressor discharge lines suffer bulb corrosion from constant heat cycling — another reason why coastal corrosion accelerates TXV failures.

### Waxy Buildup
Older R-22 systems with wax-contaminated oil can clog TXV orifices. This manifests as a gradual performance decline (month over month, not day over day) and is a sign the system has internal contamination that won't clear on its own.

## The Bottom Line

A failing TXV can mimic almost every other AC problem — low refrigerant, a bad compressor, restricted airflow. Accurate diagnosis requires gauges and temperature measurements, not guesswork. If you suspect a TXV issue, call a [licensed AC repair technician](https://ac-repair.today/services/ac-repair/) who carries manifold gauges and understands superheat/subcooling diagnostics.

On systems older than 12 years with a confirmed TXV failure, the total repair cost ($500-900) often exceeds the remaining equipment value. Consider a [complete system replacement](https://ac-repair.today/services/ac-replacement/) for the best long-term value.

---

*TXV diagnosis and replacement requires EPA Section 608 certification and specialized tools. Always hire a licensed HVAC professional for any work involving refrigerant or expansion devices.*

*Built by [AC Repair Today](https://ac-repair.today) — South Florida AC repair and installation | Serving since 2015 | CAC1824118*
