# AC Troubleshooting Guide

A practical, step-by-step guide to diagnosing air conditioning problems before calling a technician. Designed for homeowners in warm climates — especially South Florida — where AC downtime is more than an inconvenience.

When your AC stops working on a 95-degree day with 80% humidity, you need answers fast. This guide walks you through the most common AC failures, helps you identify the likely cause, and tells you whether it's a DIY fix or a job for a licensed tech.

## Interactive Diagnostic Tool

For a guided troubleshooting experience, run the **[interactive AC diagnostic tool](tools/ac-diagnostic.py)**:

```bash
python3 tools/ac-diagnostic.py
```

This Python script walks you through a decision-tree diagnostic — answering yes/no questions about your AC's symptoms to narrow down the cause and recommend next steps. No dependencies beyond Python 3.6+.

### Getting Started with Component Testing
Before diving into symptom guides, two component-level diagnostic resources help you narrow down problems faster:

- **[Compressor Contactor Testing](guides/contactor-testing.md)** — How to test the electromechanical switch that powers your compressor. Covers visual inspection, coil resistance checks, energized testing, and the specific contactor failure patterns caused by South Florida's salt air and ant infestations.
- **[TXV (Thermal Expansion Valve) Diagnostics](guides/txv-diagnostics.md)** — How to identify a failing expansion valve using superheat and subcooling measurements. TXV failures mimic low refrigerant, and misdiagnosis costs hundreds in unnecessary refills.

## How to Use This Guide

1. **Try the interactive tool** — `python3 tools/ac-diagnostic.py`
2. **Identify your symptom** from the list below
3. **Follow the flowchart** — each one walks you through simple checks in order
4. **Try the safe DIY fixes** marked with a wrench icon
5. **Call a pro** for anything involving refrigerant, electrical, or internal components

## Troubleshooting by Symptom

### Airflow & Cooling Issues
- **[Pre-Season AC Checklist](guides/pre-season-checklist.md)** — Getting your system ready for South Florida summer
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
- **[Gurgling or Bubbling Water Sounds](guides/gurgling-water-sounds.md)** — That gurgling, sloshing, or bubbling noise from your AC — when it is a harmless drain-trap sound and when it signals refrigerant migration that silently damages your compressor. Covers the difference between normal condensate drain gurgling (brief, on start/stop) and continuous sloshing from refrigerant liquid flooding the compressor, step-by-step diagnosis by sound location, how to flush the drain line, and when a gurgling sound warrants a same-day [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) call.
- **[Water Leaks Inside](guides/water-leaks.md)** — Water pooling around the indoor unit
- **[Ice on AC Unit](guides/ice-buildup.md)** — Frost or ice forming on pipes or the outdoor unit
- **[Bad Smell from Vents](guides/bad-smells.md)** — Musty, burning, or chemical odors

### Humidity & Air Quality
- **[Humidity & IAQ Effects on AC Performance](guides/humidity-iaq-effects.md)** — How high humidity and poor indoor air quality increase runtime, clog drains, overload coils, and damage components — plus diagnostic checks you can do yourself

### Electrical & Thermostat
- **[Thermostat & Electrical Diagnostics](guides/thermostat-electrical-diagnostics.md)** — Quick electrical checks before calling a tech

### Cost & Efficiency
- **[High Electric Bills](guides/high-bills.md)** — Energy costs suddenly spiked without usage change

### Advanced Diagnostics
- **[Fan Speed & Airflow Diagnostics](guides/fan-speed-diagnostics.md)** — Everything you can check about blower performance, static pressure, and airflow before calling a tech
- **[Zoning System Troubleshooting](guides/zoning-troubleshooting.md)** — How to diagnose stuck dampers, zone panel lockouts, and thermostat conflicts in zoned AC systems
- **[Power-Surge & Lightning Damage Diagnostics](guides/power-surge-damage-diagnostics.md)** — A field sequence for telling surge damage apart from ordinary failures: the component vulnerability map, breaker-behavior decision tree, visual surge fingerprints, storm-season mimics like a tripped float switch, and why a weakened capacitor warrants a same-day [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) before it takes the compressor down
- **[Compressor Hard-Start Diagnostics](guides/hard-start-diagnostics.md)** — Why your lights dim when the AC kicks on, what "hard-starting" does to the compressor, the common causes (weak capacitor, unequalized pressures, low voltage, aging windings), the observation-only checks you can safely do, why installing a hard-start kit yourself can mask a dying compressor, and when an early [AC repair](https://ac-repair.today/services/ac-repair/) prevents an expensive failure
- **[Crankcase Heater & Restart Delay Diagnostics](guides/crankcase-heater-diagnostics.md)** — What the crankcase heater does, why refrigerant migration destroys compressors during cold starts, how to test the heater and the time-delay relay, and the two-minute check that can prevent a $2,500+ compressor replacement. Essential reading before every cooling season.
- **[Intermittent Cooling Loss Diagnostics](guides/intermittent-cooling-diagnostics.md)** — Why your AC works fine for hours then stops, only to restart on its own: thermal overload trips on hot afternoons, the condensate float switch in coastal Florida homes, loose connections and voltage sags from peak-hour grid load, and when a failing run capacitor explains the intermittent pattern. Includes the diagnostic framework, tool recommendations, and when to call for an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) before the intermittent fault becomes a full failure.

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

### Component Diagnostics
- **[Control Board Flash Codes & LED Diagnostics](guides/flash-codes-and-led-diagnostics.md)** — How to read AC control board LED error codes for Carrier, Trane, Lennox, Goodman, Rheem, York, and other brands. Covers common flash code patterns, what each code means, safe DIY resets vs professional service calls, and South Florida-specific code patterns tied to salt air and humidity. The fastest diagnostic tool you can use without a multimeter.
- **[Circuit Board Moisture Damage in Humid Climates](guides/circuit-board-moisture-damage.md)** — South Florida humidity kills AC control boards: why repeated condensation creates conductive mineral deposits across solder joints, how intermittent symptoms (random shutdowns, temperature-dependent failures) mimic thermostat or compressor problems, the simple "dry-out test" that confirms root cause before you pay for misdiagnosis, and the $10 drip-shield fix that prevents recurrence. Includes the visual inspection checklist and voltage test sequence for determining if your board needs [professional AC repair](https://ac-repair.today/services/ac-repair/).
- **[Refrigerant Line Set Diagnostics](guides/refrigerant-line-set-diagnostics.md)** — The copper tubes connecting your condenser to evaporator face unique challenges in coastal Florida: crushed or kinked lines from landscaping equipment, UV-degraded insulation, salt-air pinhole corrosion, and improper slope that prevents oil return. Covers the temperature-split method for locating restrictions, standing-pressure nitrogen testing for hidden leaks, the three-symptom diagnostic table, and when line set replacement is more cost-effective than chasing leaks. Ideal read before calling for [licensed AC repair](https://ac-repair.today/services/ac-repair/).
- **[Control Board Diagnostics: The Complete Walkthrough](guides/control-board-diagnostics.md)** — When the board itself fails, blinking LEDs won't tell the whole story. Covers visual inspection (burn marks, bulging caps, corroded traces, cracked solder joints), the fuse test, transformer voltage check, the R-to-Y thermostat bypass test, interpreting error codes, when a board can be repaired vs must be replaced, and the specific reasons Florida's climate kills control boards faster (lightning surges, attic-heat capacitor death, humidity corrosion). Includes the one safety rule you must never skip.
- **[Metering Device Diagnostics](guides/metering-device-diagnostics.md)** — Comprehensive guide to piston (fixed orifice), TXV, and EEV metering devices. How each works, how each fails, diagnostic flowcharts, superheat/subcooling interpretation tables, South Florida-specific failure patterns (salt-air TXV corrosion, ant-infested sensing bulbs, EEV stepper motor failure), and safe homeowner checks before calling a pro.
- **[Capacitor Testing Guide](guides/capacitor-testing-guide.md)** — How to test AC run and start capacitors, interpret multimeter readings, identify failure modes, and safely replace them. South Florida's heat and salt air shorten capacitor life to 3-5 years.
- **[Compressor Thermal Overload Protection](guides/thermal-overload-protection.md)** — Why your AC shuts off mid-afternoon on the hottest days and restarts 30 minutes later. Covers the six most common causes (dirty condenser coil, failing fan motor, refrigerant charge issues, voltage sag, liquid line restriction, ambient heat), a diagnostic decision tree, safe homeowner checks, and when it signals an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) before compressor damage.
- **[AC Lockout Protection](guides/ac-lockout-protection.md)** — What lockout means, why modern ACs have it, and how to reset. Covers high-pressure, low-pressure, and freeze-protection lockout scenarios common in South Florida.
- **[Refrigerant Leak Detection](guides/refrigerant-leak-detection.md)** — How to spot early signs of refrigerant leaks, distinguish them from airflow problems, understand professional detection methods, and decide when repair beats replacement. Essential reading for South Florida's salt-air environment.
- **[Compressor Overheating & Thermal Overload](guides/compressor-overheating.md)** — Why your compressor shuts off after 10-30 minutes on hot days, six causes from dirty coils to bad capacitors to voltage sag, and how to diagnose with basic tools. Essential for South Florida's extreme heat.
- **[Tracing Low-Voltage Shorts](guides/low-voltage-short-tracing.md)** — Systematic guide to finding 24V control circuit shorts: blown fuse method, thermostat wiring inspection, resistance testing, component-level diagnostics (contactor coils, dampers, float switches), and Florida-specific failure points like rooftop penetrations and salt-air corrosion.
- **[Blower Motor Diagnostics](guides/blower-motor-diagnostics.md)** — When the indoor fan won't spin
- **[ECM Blower Motor Diagnostics](guides/ecm-blower-motor-diagnostics.md)** — How to diagnose variable-speed ECM motors when they act up: control module failure, Hall sensor errors, communication signal loss, bearing failure, error code interpretation by manufacturer (Genteq, Regal Beloit, Emerson), bypass testing procedures, and the symptom-to-cause lookup table. Covers the unique failure modes that modern electronically commutated motors introduce over traditional PSC motors.: how to tell a PSC motor (hum-no-spin = dead capacitor) from a modern ECM (surge-sensitive control module), a symptom-to-cause table, why South Florida heat and lightning kill blower motors early, the safe homeowner checklist, and when a stationary blower becomes an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/) on a hot day.
- **[AC Keeps Shutting Off — Tripped Condensate Float Switch](guides/float-switch-shutoff.md)** — The #1 reason South Florida systems shut themselves off: a clogged condensate drain backs up and the safety float switch opens the 24V circuit. Covers the tell-tale "dead unit, healthy breaker, works again later" pattern, a symptom table, the safe wet-vac-and-vinegar homeowner fix, monthly prevention, and when a recurring clog needs professional [AC repair](https://ac-repair.today/services/ac-repair/).
- **[Condenser Fan Motor Diagnostics](guides/condenser-fan-motor-diagnostics.md)** — The outdoor unit hums but the top fan won't spin and the air inside is warm — a failure that can destroy a compressor in minutes. Covers the safe "stick test," telling a failed run capacitor (most common) from a seized motor or stuck contactor, what's safe to check yourself, and why a fan that needs a manual push is an [emergency AC repair](https://ac-repair.today/services/emergency-ac-repair/), not a wait-and-see.

### Thermostat & Controls
- **[Wi-Fi Thermostat Connectivity Troubleshooting](guides/thermostat-wifi-connectivity.md)** — Why smart thermostats drop Wi-Fi in South Florida homes: signal attenuation through concrete masonry construction, the C-wire vs power-stealing problem that causes intermittent disconnections during cooling cycles, 2.4 GHz channel congestion in dense neighborhoods, the RSSI diagnostic that tells you if the signal is marginal, brand-specific quirks (ecobee, Nest, Honeywell, Sensi), and when the real problem is a failing 24V transformer rather than network interference.
- **[Communicating Thermostat System Malfunctions](guides/communicating-thermostat-diagnostics.md)** — Modern systems (Carrier Infinity, Trane ComfortLink, Lennox iComfort) use proprietary data-link communication instead of conventional 24V wiring. When the data link breaks, the entire system goes dead — no display, no fan, no compressor. Covers the four distinct failure modes (data-link loss, wrong configuration, software glitch, outdoor-unit communication fault), brand-specific wiring and error codes, and the smart-homeowner troubleshooting steps before you call a pro. Includes a quick-decision table and which brands require dealer-only diagnostic tools.

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

Need a professional in South Florida? [AC Repair Today](https://ac-repair.today/services/ac-repair/) services Miami-Dade, Broward, and Palm Beach with same-day emergency repairs — licensed, insured, and available 7 days a week. Read our [thermostat and electrical diagnostic guide](https://ac-repair.today/services/ac-maintenance/) to learn about common electrical causes of AC failure.

Florida License CAC1824118 | (305) 850-6810 | [ac-repair.today](https://ac-repair.today) | [AC Maintenance Plans](https://ac-repair.today/services/ac-maintenance/)

---

*This guide is for informational purposes only. Electrical and refrigerant work must be performed by licensed professionals. Improper AC repair can cause injury, property damage, or void manufacturer warranties.*
