# Compressor Overheating & Thermal Overload Tripping

Your AC compressor draws the most current and generates the most heat of any component in the system. When it overheats, an internal thermal overload protector (KLIXON) disconnects power to prevent permanent damage. The compressor cools down, the overload resets, and the system restarts — only to overheat again.

This cycle is common in South Florida, where compressors operate in extreme conditions year-round. Here's how to identify the cause and fix it.

## What Thermal Overload Tripping Looks Like

- AC runs for 10-30 minutes, then shuts off completely (blower may still run)
- System stays off for 15-60 minutes, then restarts
- The cycle repeats throughout the afternoon but may work fine at night or on cooler days
- The outdoor unit may be visibly hot — you can feel heat radiating from the access panel
- No error codes on most basic thermostats (some smart thermostats show "lockout" events)

## Six Causes of Overheating

### 1. Dirty Condenser Coils (Most Common)

Over 80% of thermal overload trips in South Florida are caused by restricted airflow across the condenser coil. When the coil is caked with dirt, salt, cottonwood seeds, or grass clippings, heat can't escape into the outdoor air.

**Check**: Look at the condenser coils through the grille. Can you see bare metal, or is there a mat of debris between the fins? Shine a flashlight through — if you can't see light on the other side, the coil is significantly blocked.

**Fix**: 
1. **Kill power** at the disconnect switch (usually a pull-out block or breaker within sight of the unit)
2. Remove the top grille and fan assembly (4-6 screws)
3. **Gently** spray the coils from the inside out with a garden hose nozzle — start from the top and work down
4. Let the coil dry before restoring power
5. If the debris is caked on, use an AC coil cleaner (alkaline foaming cleaner, available at any hardware store)

Keep vegetation at least 2 feet away from the unit on all sides, 5 feet above.

### 2. Bad Run Capacitor

The run capacitor provides additional current to keep the compressor running efficiently. A weak capacitor causes the compressor to draw higher-than-normal running current, generating excess heat.

**Check**: A multimeter reading on the run capacitor should be within 6% of the rated microfarads (µF). Common signs:
- Bulging or leaking capacitor (top is domed instead of flat)
- Capacitor rated for 370V but system calls for 440V (always replace with equal or higher voltage)

**Fix**: Replace with an identical-rated capacitor. See our [capacitor testing guide](capacitor-testing-guide.md) for detailed instructions on safe testing and replacement.

### 3. Low Refrigerant Charge

Undercharged systems have reduced cooling capacity, but the compressor still draws nearly full current. The refrigerant returning to the compressor (suction gas) is supposed to cool the compressor windings internally. With low charge, there's less suction gas, so the compressor runs hotter.

**Check**: Low refrigerant often pairs with:
- Short cycling on hot days
- Ice on the suction line (larger copper line) at the outdoor unit
- Higher-than-normal discharge temperature (requires gauges)
- Gradual loss of cooling over weeks or months — not sudden

**Fix**: A technician must locate and repair the leak, then evacuate and recharge to the nameplate specification. If you see ice on the lines or suspect a leak — call a [licensed AC repair technician](https://ac-repair.today/services/ac-repair/) immediately. Running a system low on charge will destroy the compressor.

### 4. High Head Pressure (Overcharge or Non-Condensables)

Too much refrigerant, or the presence of non-condensable gases (air, nitrogen) in the system, causes excessively high discharge pressure. The compressor must work harder, generating more heat.

**Check**: High head pressure causes:
- Thermal overload on the hottest days only
- Noisy compressor operation (a deep humming or groaning sound)
- Discharge line temperatures above 220°F (requires temperature probe)
- Short-cycling on high-pressure switch (if equipped)

**Fix**: The technician must recover the full charge, evacuate the system to remove non-condensables, and recharge by weight per the nameplate. Never "top off" refrigerant — it should always be recovered and re-weighed.

### 5. Restricted Metering Device

A clogged thermal expansion valve (TXV) or piston orifice restricts refrigerant flow into the evaporator. This causes high superheat and low suction pressure — making the compressor run hot even though the condenser looks fine.

**Check**: 
- Suction pressure lower than normal with high superheat (requires gauges)
- Evaporator coil may have frost patches on some circuits
- Temperature drop across the liquid line filter-drier is more than 3°F (indicates restriction)

**Fix**: A technician must replace the metering device and filter-drier, then evacuate and recharge. See our [TXV diagnostics guide](txv-diagnostics.md) for more details.

### 6. Voltage Issues (Brownout or Undersized Wiring)

South Florida experiences voltage sags during afternoon thunderstorms and peak summer usage. When voltage drops below 208V for a 240V system, the compressor draws proportionally MORE current to maintain power output — generating excess heat.

**Check**:
- Measure voltage at the disconnect while the compressor is running
- Voltage should be within 10% of nameplate (±24V for 240V system)
- Voltage sag below 210V on a 240V system is problematic
- Loose connections at the contactor, disconnect, or breaker panel cause voltage drop

**Fix**: 
- Loose connections → tighten or replace
- Undersized wiring → electrician upgrade (rare but happens in older homes)
- Grid brownout → a [whole-home surge protector with undervoltage protection](https://ac-repair.today/services/thermostat-installation/) can help
- In severe cases, a buck-boost transformer may be needed

## Compressor Temperature Diagnostics

If you have an infrared thermometer:

| Temperature Reading (Discharge Line, 6" from compressor) | Condition |
|-----------------------------------------------------------|-----------|
| 120-180°F | Normal operation |
| 180-220°F | Warm — check for coil cleanliness |
| 220-260°F | Hot — likely condenser coil or capacitor issue |
| 260°F+ | Critical — imminent thermal overload, shut down |

| Temperature Reading (Compressor Dome - Top Center) | Condition |
|-----------------------------------------------------|-----------|
| 140-180°F | Normal (scroll compressors) |
| 180-220°F | Warm — check refrigerant charge |
| 220°F+ | Overheating — do not operate |

*Measurements are approximate and vary by compressor model. These are screening values, not diagnostic values.*

## When Thermal Overload Won't Reset

If the compressor has been overheating repeatedly:

1. **Check compressor winding resistance**: Measure between terminals C-R, C-S, R-S. All readings should be within 20% of each other. A reading to ground (any terminal to copper tube) should show infinite resistance (OL on multimeter).
2. **Megger test**: A licensed technician can perform an insulation resistance test. Readings below 1 megohm indicate internal winding damage — the compressor needs replacement.
3. **Seized compressor**: If the compressor hums but won't start and the capacitor is good, the compressor may be mechanically seized. This requires replacement.

## Permanent Fixes

Once you've identified the cause, here are the lasting solutions:

| Cause | Quick Fix | Permanent Fix |
|-------|-----------|---------------|
| Dirty coils | Spray with garden hose | Monthly cleaning during summer + seasonal pro cleaning |
| Bad capacitor | Replace capacitor (DIY) | Upgrade to higher-temperature rated capacitor (70°C+) |
| Low refrigerant | — | Find and seal leak, full recharge |
| Overcharge | — | Recover and recharge by weight |
| Blocked TXV | — | Replace TXV and filter-drier |
| Voltage sag | — | Electrician to verify wire gauge, tighten connections |
| Oversized/undersized system | — | Manual J calculation (next replacement cycle) |

## Prevention Steps

South Florida is uniquely hard on compressors. Here's how to protect yours:

1. **Clean condenser coils monthly during summer** — May through October. A garden sprayer with plain water is enough.
2. **Replace the run capacitor every 3-4 years** — Capacitors drift down over time and fail faster in heat. Proactive replacement costs $15-30.
3. **Install a hard-start kit** — Adds starting torque and reduces startup current. Helpful for older compressors and systems with long refrigerant lines.
4. **Keep the outdoor unit shaded** — Direct sun on the compressor adds 10-15°F to operating temperature. A shade structure or landscaping (with 2+ feet clearance) helps.
5. **Fix refrigerant leaks early** — The most expensive repair is a burned-out compressor from running low on charge. If cooling is gradually declining, don't wait.
6. **Monitor with a smart thermostat** — Many smart thermostats log runtime and can alert you to abnormal cycling patterns before the compressor fails.

## When to Call a Professional

Call a [licensed HVAC contractor](https://ac-repair.today/) if:

- You've cleaned the condenser coils and the overheating continues
- The compressor won't restart after cooling down (humming but not running)
- You suspect refrigerant issues
- Voltage readings are abnormal
- The system is more than 8 years old and overheating regularly

Continuing to operate an overheating compressor will cause terminal failure. The thermal overload is a safety device, not a band-aid — if it's tripping, something needs attention.

For same-day service in Miami-Dade, Broward, or Palm Beach: [AC Repair Today](https://ac-repair.today/services/ac-repair/) — FL License CAC1824118 | (305) 850-6810

---

*Part of the AC Troubleshooting Guide — practical diagnostic resources for South Florida homeowners.*
