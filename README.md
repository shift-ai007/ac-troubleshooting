# AC Troubleshooting Guide

A practical, step-by-step guide to diagnosing air conditioning problems before calling a technician. Designed for homeowners in warm climates — especially South Florida — where AC downtime is more than an inconvenience.

When your AC stops working on a 95-degree day with 80% humidity, you need answers fast. This guide walks you through the most common AC failures, helps you identify the likely cause, and tells you whether it's a DIY fix or a job for a licensed tech.

## Interactive Diagnostic Tool

For a guided troubleshooting experience, run the **[interactive AC diagnostic tool](tools/ac-diagnostic.py)**:

```bash
python3 tools/ac-diagnostic.py
```

This Python script walks you through a decision-tree diagnostic — answering yes/no questions about your AC's symptoms to narrow down the cause and recommend next steps. No dependencies beyond Python 3.6+.

## How to Use This Guide

1. **Try the interactive tool** — `python3 tools/ac-diagnostic.py`
2. **Identify your symptom** from the list below
3. **Follow the flowchart** — each one walks you through simple checks in order
4. **Try the safe DIY fixes** marked with a wrench icon
5. **Call a pro** for anything involving refrigerant, electrical, or internal components

## Troubleshooting by Symptom

### Airflow & Cooling Issues
- **[AC Not Cooling at All](guides/not-cooling.md)** — System runs but no cold air comes out
- **[Weak Airflow](guides/weak-airflow.md)** — Cold air comes out but barely any volume
- **[Uneven Cooling](guides/uneven-cooling.md)** — Some rooms cold, others warm
- **[AC Blowing Warm Air](guides/warm-air.md)** — System is on but air feels warm or room temperature

### System Behavior
- **[AC Won't Turn On](guides/wont-turn-on.md)** — No response from the system at all
- **[Breaker & Electrical Panel Guide](guides/breaker-and-electrical.md)** — Check breakers, GFCI, and disconnect switches safely
- **[AC Short Cycling](guides/short-cycling.md)** — System turns on and off every few minutes
- **[AC Runs Continuously](guides/runs-continuously.md)** — Unit never shuts off, runs 24/7

### Strange Symptoms
- **[Unusual Noises](guides/unusual-noises.md)** — Banging, squealing, clicking, or buzzing sounds
- **[Water Leaks Inside](guides/water-leaks.md)** — Water pooling around the indoor unit
- **[Ice on AC Unit](guides/ice-buildup.md)** — Frost or ice forming on pipes or the outdoor unit
- **[Bad Smell from Vents](guides/bad-smells.md)** — Musty, burning, or chemical odors

### Cost & Efficiency
- **[High Electric Bills](guides/high-bills.md)** — Energy costs suddenly spiked without usage change

## Quick Decision Flowcharts

Visual flowcharts for fast diagnosis:

- [Complete Diagnostic Flowchart](flowcharts/diagnostic-overview.md) — Start here if you're not sure
- [Is It the Thermostat?](flowcharts/thermostat-check.md) — Rule out the simplest cause first
- [Electrical vs Mechanical](flowcharts/electrical-vs-mechanical.md) — Narrow down the failure type

## Before You Start: Safety First

**Never** attempt any troubleshooting that involves:

- Opening the electrical panel on your AC unit
- Handling or checking refrigerant lines
- Working on the compressor or capacitor
- Any repair while the system is energized (always kill the breaker first)

**Safe homeowner checks include:**
- Thermostat settings and batteries
- Air filter inspection and replacement
- Breaker panel (just flipping the switch back)
- Drain line visual inspection
- Outdoor unit clearance and debris removal
- Vent registers (open/closed check)

## Common Causes at a Glance

| Symptom | Most Likely Cause | DIY? |
|---------|------------------|------|
| No cooling | Dirty filter, thermostat issue | Yes |
| Weak airflow | Clogged filter, blocked ducts | Partially |
| Short cycling | Oversized unit, dirty filter | Check filter |
| Water leak | Clogged drain line | Yes (vinegar flush) |
| Ice buildup | Low refrigerant, restricted airflow | No — call pro |
| Strange noise | Loose parts, failing motor | No — call pro |
| Won't start | Breaker tripped, thermostat dead | Check breaker |
| High bills | Dirty system, duct leaks, age | Maintenance helps |

## South Florida Specifics

South Florida conditions affect troubleshooting:

- **Drain line clogs are the #1 service call** — Our humidity means condensate drain lines clog faster than anywhere else. Flush with vinegar monthly.
- **Salt corrosion** — If you're within 3 miles of the coast, condenser coil corrosion is the most likely cause of gradual cooling loss.
- **Mold in ducts** — That musty smell from vents is almost always mold growth in ductwork. This requires professional remediation.
- **Oversized systems are epidemic** — Many South Florida homes have AC systems sized for northern climates. An oversized unit short-cycles, never dehumidifies properly, and fails faster.

## Reference

- [Florida HVAC License Lookup](reference/florida-licensing.md) — How to verify your contractor
- [SEER Rating Explained](reference/seer-ratings.md) — What those numbers actually mean for your bill
- [Refrigerant Types](reference/refrigerants.md) — R-22 vs R-410A and the transition timeline

## South Florida Resources

- [Directory of licensed AC contractors in South Florida](https://ac-repair.today) — Licensed, insured professionals covering Miami-Dade, Broward, and Palm Beach counties.

## Contributing

Found an inaccuracy? Have a troubleshooting tip we missed? Pull requests welcome.

## About

Need a professional? [AC Repair Today](https://ac-repair.today/services/ac-repair/) services all of South Florida with same-day emergency repairs. Licensed, insured, and available 7 days a week.

Florida License CAC1824118 | (305) 850-6810 | [ac-repair.today](https://ac-repair.today)

---

*This guide is for informational purposes only. Electrical and refrigerant work must be performed by licensed professionals. Improper AC repair can cause injury, property damage, or void manufacturer warranties.*
