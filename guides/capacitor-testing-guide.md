# AC Capacitor Testing Guide

Capacitors are one of the most common failure points in residential AC systems, yet they're also one of the easiest to diagnose if you know what to look for. This guide covers the role capacitors play in your AC system, how to identify signs of failure, and when it's safe to handle a replacement versus when to call a pro.

## What Capacitors Do in Your AC

Capacitors store electrical energy and release it in a controlled burst to start motors and keep them running efficiently. Your AC system has at least two:

- **Run capacitor** — Connected to the compressor and condenser fan motor. It stays in the circuit during operation to improve motor efficiency and power factor. A failed run capacitor causes motors to run hot and draw excessive current.
- **Start capacitor** — Found on larger compressors and motors, provides a high-torque boost during startup, then drops out of the circuit. A failed start capacitor means the motor may hum but not start.
- **Dual run capacitor** — A single capacitor that serves both the compressor and condenser fan motor. Three terminals: C (common), HERM (compressor), FAN (fan). This is the most common type in modern residential systems.

## Why Capacitors Fail in South Florida

South Florida's climate accelerates capacitor failure for specific reasons:

- **Heat exposure** — Capacitors contain an electrolytic fluid that dries out over time. Ambient temperatures above 90°F plus the heat from the electrical compartment push internal temperatures well beyond the capacitor's 70°C rating, reducing life from 10+ years to 3-5 years.
- **Voltage fluctuations** — Florida thunderstorms cause brief surges and sags that stress capacitor dielectric layers. Each surge micro-damages the internal foil structure.
- **Salt corrosion** — Coastal salt air attacks capacitor terminal connections, increasing resistance and causing heat buildup at the connection point itself.
- **Poor ventilation** — Many South Florida outdoor units are installed on concrete pads with the electrical compartment facing a wall, restricting airflow around the capacitor.

## Signs of a Failing Capacitor

### Visual Signs

Capacitors may show physical symptoms before complete failure:

- **Bulging or domed top** — A healthy capacitor has a flat or slightly indented top. A bulging top means internal pressure has increased — the capacitor is failing and should be replaced.
- **Cracked or leaking case** — Electrolyte leakage appears as oily residue around the base or terminals. This is a hazardous condition and the capacitor must be replaced immediately.
- **Corroded terminals** — Green or white crust on terminal connections indicates moisture and salt intrusion.
- **Burnt smell near the electrical compartment** — The capacitor's internal pressure relief valve may have opened, releasing electrolyte and a distinct chemical odor.

### Performance Signs

- **AC hums but won't start** — The compressor or fan motor makes a humming sound but never kicks into operation. This is the classic sign of a failed run capacitor.
- **Fan spins slowly or erratically** — A weak capacitor delivers less than full voltage to the fan motor, causing it to run below rated speed.
- **Intermittent cooling** — The AC works sometimes but not others, especially on the hottest days when the capacitor is weakest.
- **Tripped breakers** — A failing capacitor causes motors to draw higher starting current, which can trip the breaker.
- **Higher electric bills** — Motors running without proper capacitance draw 15-25% more current than designed, wasting electricity.

## Capacitor Testing (Safely)

**⚠️ SAFETY WARNING:** Capacitors store electrical charge even after power is disconnected. A standard AC run capacitor can deliver a painful or dangerous shock. If you are not comfortable working near live electrical components, skip this section and call a professional.

### What You'll Need

- Digital multimeter (DMM) with capacitance measurement mode — most $40+ meters have this
- Insulated screwdriver for discharging the capacitor
- Safety glasses
- Voltage-rated gloves recommended

### Procedure

**Step 1: Kill power.** Turn off the disconnect switch at the outdoor unit and the breaker at the main panel. Verify power is off using your multimeter's voltage setting between each terminal and ground.

**Step 2: Discharge the capacitor.** With the power off, place an insulated screwdriver across the terminals of the capacitor — touch the metal shaft to both terminals at once. You should see a small spark as the stored charge dissipates. Wait 30 seconds and do it again to ensure full discharge.

**Step 3: Remove the capacitor.** Take a photo of the wiring before removing anything. Then disconnect the wires from the capacitor terminals (marked C, HERM, FAN on a dual capacitor). Remove the capacitor from its mounting bracket.

**Step 4: Check the label.** Every capacitor has a rated capacitance printed on the side, measured in microfarads (µF or MFD). Note the rating and tolerance (typically ±5% or ±6%). Common values: 30+5 µF, 35+5 µF, 40+5 µF for dual capacitors; 5 µF, 7.5 µF, 10 µF for single fan capacitors; 45-80 µF for dedicated compressor run capacitors.

**Step 5: Measure with the multimeter.** Set your DMM to capacitance mode (often marked with a "–|(–" symbol). Connect the probes to the capacitor terminals:

- **Dual capacitor:** Measure between C and HERM (compressor reading), C and FAN (fan reading), and HERM and FAN (should show the sum of both)
- **Single capacitor:** Connect across the two terminals

**Step 6: Interpret the reading.** Compare your measurement to the rated value:
- Reading within ±6% of rated value → Capacitor is good
- Reading 6-15% below rated → Capacitor is degraded and likely to fail within 6-12 months. Replace proactively.
- Reading more than 15% below rated → Capacitor is failing. Replace immediately.
- Reading zero or OL (open line) → Capacitor has failed completely. Replace.

### Example

If you have a labeled 35+5 µF dual capacitor:
- Expected C to HERM: 35 µF
- Expected C to FAN: 5 µF
- Actual reading of 28 µF on HERM circuit → 20% below rated → failing, replace

## Capacitor Replacement (DIY)

If you're comfortable working with basic electrical components and have verified the power is off, replacing a capacitor is straightforward:

1. **Buy the exact match** — Same µF rating and voltage rating (or higher voltage). A 370V capacitor can be replaced with a 440V, but not vice versa. The physical size must fit in the mounting bracket.
2. **Standard sizes available at supply houses** — Fasco, Titan Pro, and AmRad are common brands. Expect to pay $15-35 at a local supply house versus $60-100 for an emergency service call replacement.
3. **Wire orientation doesn't matter** — Capacitors are not polarity-sensitive (except the discharge resistor side).
4. **Secure the new capacitor** — Use the factory mounting bracket. A loose capacitor can vibrate and short against the cabinet.
5. **Restore power** and verify the system starts and runs normally.

**When NOT to DIY:**

- The capacitor is hard-wired and would require cutting/splicing (most have push-on terminals — these are fine)
- The terminals are corroded or damaged — the underlying wiring may need replacement too
- You see any burn marks on the contactor, wiring, or refrigerant lines — there may be a larger electrical issue
- The system immediately trips the breaker after capacitor replacement — the compressor or fan motor may have failed as well

## Professional Capacitor Testing

A licensed AC technician's capacitor testing typically costs $80-150 as part of a diagnostic call and includes:

- Metered capacitance testing of both run and start capacitors
- Micro-ohm testing of internal winding resistance to catch compressor damage
- Contactor contact resistance measurement (pitted contacts stress capacitors)
- Voltage logging during compressor startup to catch intermittent failures
- Recommendations on pre-emptive replacement before the coming cooling season

An annual [AC maintenance checkup](https://ac-repair.today/services/ac-maintenance/) always includes capacitor testing as part of the electrical safety inspection.

## The Capacitor Lifecycle in South Florida

| Year | Capacitor Condition | Recommended Action |
|------|-------------------|-------------------|
| 1-2 | Factory fresh, within tolerance | None |
| 3-4 | Mild degradation (full rating still within spec) | Annual test, baseline recorded |
| 4-6 | Noticeable drop (10-15% below spec for many units) | Consider proactive replacement before summer |
| 6-8 | 15-25% below spec for most salt-air installations | Replace proactively — higher failure risk |
| 8+ | Beyond useful life in coastal Florida | Replace regardless of measured value |

A proactive capacitor replacement every 4-5 years ($15-35 part) prevents the most common "AC won't start on a 95-degree day" emergency service call ($150-300 diagnostic + $60-100 capacitor markup).

---

*Need a quick capacitor check or other AC diagnostics in South Florida? [AC Repair Today](https://ac-repair.today/services/ac-repair/) serves Miami-Dade, Broward, and Palm Beach with same-day service. Licensed FL CAC1824118.*
