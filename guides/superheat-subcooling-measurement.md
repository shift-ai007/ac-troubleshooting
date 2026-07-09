# Superheat & Subcooling Measurement Guide

Superheat and subcooling are the two most important measurements for diagnosing refrigerant circuit problems. Together they tell you whether a system is properly charged, whether the metering device is working, and whether there's a restriction. This guide explains how to measure both and what the readings mean.

## What You Need

- Digital manifold gauge set (R-410A rated for modern systems)
- Temperature clamp or probe on the line near the service valves
- PT chart or the [refrigerant PT reference tool](../tools/refrigerant-pt-chart.py)
- Knowledge of the metering device type (piston/TXV/electronic)

## Superheat — Measuring Evaporator Performance

Superheat is the number of degrees a vapor is heated **above** its saturation temperature after all liquid has boiled off. It tells you if enough refrigerant is reaching the evaporator.

### How to Measure (Fixed Orifice / Piston Systems)

1. Run the system for 15+ minutes to stabilize
2. Measure **suction line temperature** at the service valve (or as close to the evaporator outlet as possible)
3. Read **suction pressure** (low side) on your gauges
4. Find the **saturation temperature** for that pressure on your PT chart
5. **Superheat = actual line temperature − saturation temperature**

```text
Example:
  Suction pressure: 120 psig (R-410A)
  Saturation temp at 120 psig: 40°F (from PT chart)
  Actual suction line temp: 58°F
  Superheat = 58°F − 40°F = 18°F
```

### Target Superheat Values

| System Type | Target Superheat |
|-------------|-----------------|
| Fixed orifice (piston), standard efficiency | 12–20°F |
| Fixed orifice, high-efficiency | 10–15°F |
| TXV systems | 8–12°F (at evaporator outlet) |
| Mini-splits (manufacturer-dependent) | 2–8°F |

### What Superheat Tells You

**High superheat (>20°F):**
- Low refrigerant charge (most common cause)
- Restricted liquid line (filter drier, kinked line)
- Metering device underfeeding (partially blocked piston)
- Indoor airflow too high (blower on high speed)

**Low superheat (<5°F):**
- Overcharged system
- TXV overfeeding (stuck open, power element lost charge)
- Indoor airflow too low (dirty filter, blower issue)
- Flooding evaporator — liquid may reach compressor

**Zero or negative superheat:**
- Liquid slugging the compressor (emergency — shut down immediately)
- TXV hunting severely
- Flooded system from severe overcharge

## Subcooling — Measuring Condenser Performance

Subcooling is the number of degrees a liquid is cooled **below** its saturation temperature after all vapor has condensed. It tells you how much liquid is stacked in the condenser — a measure of charge level on TXV systems.

### How to Measure

1. Run the system for 15+ minutes to stabilize
2. Measure **liquid line temperature** near the service valve (before the filter drier)
3. Read **head pressure** (high side) on your gauges
4. Find the **saturation temperature** for that pressure on your PT chart
5. **Subcooling = saturation temperature − actual liquid line temperature**

```text
Example:
  Head pressure: 310 psig (R-410A)
  Saturation temp at 310 psig: 100°F
  Actual liquid line temp: 90°F
  Subcooling = 100°F − 90°F = 10°F
```

### Target Subcooling Values

| System Type | Target Subcooling |
|-------------|------------------|
| TXV systems | 8–14°F |
| Fixed orifice | 5–10°F |
| Mini-splits | 2–6°F (check manual) |

### What Subcooling Tells You

**High subcooling (>15°F):**
- Overcharged refrigerant (most common)
- Restricted condenser airflow (dirty coil, blocked condenser)
- Condenser fan running slow
- Non-condensables in system (air/moisture)

**Low subcooling (<5°F):**
- Undercharged refrigerant
- TXV overfeeding (sending liquid back to compressor)
- Restriction after liquid line (but before measurement point)
- High heat load on evaporator

**Rising subcooling during operation:**
- Non-condensables in system (air or moisture)
- Gradual restriction forming (wax, sludge, desiccant breakdown)

## Charging Methods by Metering Device

### Fixed Orifice / Piston — Charge by Superheat

Fixed orifice systems use superheat to judge charge because the orifice is a fixed restriction — the pressure drop depends entirely on conditions.

1. Measure outdoor ambient temperature and indoor wet-bulb temperature
2. Consult the manufacturer's charging chart (or standard superheat chart)
3. Add refrigerant until superheat matches the target for current conditions
4. Remove refrigerant if superheat is too low

### TXV — Charge by Subcooling

TXV systems regulate superheat automatically, so superheat is not a reliable charge indicator. Use subcooling instead.

1. Run system until pressures and temperatures stabilize
2. Measure subcooling per the procedure above
3. Add refrigerant if subcooling is below target
4. Recover if subcooling is above target
5. Let the system run 10 minutes between adjustments

## Mixed Signals — Diagnosing Complex Problems

Sometimes superheat and subcooling tell contradictory stories. Here's how to interpret them:

| Superheat | Subcooling | Diagnosis |
|-----------|-----------|-----------|
| High | Low | **Undercharged** (classic 410A pattern) |
| High | High | **Restriction** after liquid receiver, or overcharged + underfeeding |
| Low | High | **Overcharged**, or TXV stuck open + overcharged |
| Low | Low | **Low airflow** across evaporator, or TXV hunting, or non-condensables |

## Temperature Split (Delta T): The Quick Check

Before hooking up gauges, measure the temperature split:

1. Measure supply air temperature at the closest register to the air handler
2. Measure return air temperature at the return grille
3. **Delta T = Return − Supply**

**Target delta T for South Florida:** 16–22°F on a 90–95°F day
- Below 16°F: Low charge, dirty coil, or poor airflow
- Above 22°F: Very low airflow or overcharged (less common)

A low delta T with compressor running is the most common early warning of low refrigerant. If you see this, use the [refrigerant PT reference tool](../tools/refrigerant-pt-chart.py) to check your pressures.

## Safety Notes

- **R-410A operates at 1.6× the pressure of R-22** — use gauges and hoses rated for 800 psig
- **R-32 and R-454B are A2L mildly flammable** — no open flames, no extension cords, ventilate the area
- **Never add refrigerant without knowing the correct type** — mixing refrigerants destroys the system
- **Weigh in refrigerant by the manufacturer's specification** — do not rely on pressures alone
- Always recover refrigerant, never vent to atmosphere (EPA fine up to $44,539 per day)

---

*For professional refrigerant diagnostics and AC repair in South Florida: [AC Repair Today](https://ac-repair.today/services/ac-repair/) — Florida-licensed CAC1824118.*
