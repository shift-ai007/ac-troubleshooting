# Crankcase Heater and Compressor Restart Delay Diagnostics

When your AC compressor kicks on, it faces a battle against physics — refrigerant has a tendency to migrate to the coldest part of the system overnight. In tropical climates like South Florida, that means liquid refrigerant can pool in the compressor crankcase, waiting to cause damage on the next startup.

This guide covers two related systems that protect your compressor from this damage: the crankcase heater (which keeps refrigerant where it belongs) and the time-delay relay (which prevents the compressor from restarting before internal pressures equalize).

## What Is a Crankcase Heater and Why Does It Matter?

A crankcase heater is an electric heating element wrapped around or inserted into the bottom of the compressor. Its job is to keep the compressor oil a few degrees warmer than the rest of the system, preventing refrigerant from condensing and pooling in the crankcase overnight.

### Why Refrigerant Migration Is Destructive

Refrigerant seeks the coldest spot in a static system. When the compressor sits idle for hours — overnight, during work hours, or in mild weather — vapor refrigerant migrates to the compressor crankcase, where it condenses into liquid and mixes with the oil. Here's what happens at the next startup:

- **Foaming**: The liquid refrigerant in the oil flashes to vapor when the compressor starts, creating foam. Foam doesn't lubricate bearings.
- **Washout**: Liquid refrigerant washes the oil film off bearing surfaces, causing metal-to-metal contact during the first seconds of operation.
- **Slugging**: Large amounts of liquid refrigerant entering the compression chamber can physically break valves or bend connecting rods.
- **Acid formation**: Every start-up with liquid-refrigerant dilution creates minor wear. Over years, this generates acid in the oil, which attacks motor windings.

A functioning crankcase heater prevents all of this by keeping the compressor warm enough that refrigerant stays in vapor form.

### How Crankcase Heaters Fail

Crankcase heaters fail in two ways:

1. **Open circuit** — the heating element burns out and produces no heat. This is the most common failure mode. The compressor can still run, but every cold start does incremental damage.

2. **Short circuit** — the heater short-circuits to ground, usually tripping the system's low-voltage fuse or causing a control board error. This is rarer but more noticeable because the system stops.

Signs of crankcase heater failure include:
- Extended "hard start" symptoms especially on first startup of the day
- Compressor that hums but won't start on the first try
- Higher-than-normal amp draw during startup
- A compressor that slowly loses efficiency over months

## How to Test a Crankcase Heater

**Safety warning**: Crankcase heaters operate at line voltage (208-240V) in most residential systems. Disconnect all power to the system at the disconnect switch and confirm zero voltage before touching any terminals. Testing is best done by a licensed professional or with appropriate PPE and training.

### Visual Inspection
1. Kill power at the disconnect (and confirm with a meter)
2. Remove the compressor access panel
3. Locate the crankcase heater — it's either a resistance band clamped around the bottom of the compressor shell or a cartridge heater inserted into a well in the compressor sump
4. Look for obvious damage: burned insulation, discoloration, or signs of arcing

### Resistance Test
1. Disconnect the heater wires at the terminal block
2. Set your multimeter to ohms range
3. Measure across the heater terminals:
   - A reading near zero indicates a shorted heater (bad)
   - An open line (OL or infinite) indicates a burned-out heater (bad)
   - A reading between 20 and 200 ohms (depending on wattage) indicates the heater is intact (good)

### Current Draw Test
1. Reconnect power to the system
2. Clamp an ammeter around one of the heater wires (the compressor must be OFF for the heater to be energized — most crankcase heaters are powered by a normally-closed contactor)
3. A functioning 40-80 watt heater draws 0.15-0.35 amps at 240V
4. Zero amp draw means the heater circuit is open

### Temperature Rise Test (Most Definitive)
1. With the system off, let the compressor sit for 2+ hours
2. Measure the temperature of the compressor shell at the bottom
3. Turn on the system's thermostat (set to OFF or as high as possible) so the compressor contactor stays open but the system has power
4. After 30-60 minutes, measure the compressor shell temperature again
5. A functioning crankcase heater raises the shell temperature 10-30°F above ambient
6. No temperature rise = heater not working

## Compressor Restart Delay

A time-delay relay (TDR) — also called an anti-short-cycle timer — prevents the compressor from restarting for 3-5 minutes after it shuts off. This wait allows high-side and low-side pressures to equalize through the metering device, so the compressor starts against a balanced load rather than full head pressure.

### Why These Fail

Time-delay relays are solid-state devices and rarely fail, but they can:
- **Weld closed** — the compressor can restart immediately after stopping, causing hard starts and potential damage
- **Fail open** — the compressor never gets the start signal, making the system appear dead
- **Drift timing** — internal component aging can shorten or lengthen the delay

### Testing a Time-Delay Relay

1. With the thermostat calling for cooling, note the time the compressor shuts off
2. Immediately set the thermostat to call for cooling again
3. Time how long before the compressor energizes:
   - 3-5 minutes = normal
   - Under 2 minutes = timing has drifted (may need replacement)
   - Instant restart = relay has failed closed
   - Never restarts = relay has failed open (or the control board has a fault)
4. If the compressor starts instantly on restart, it's under full head pressure — this causes high amp draw and puts extra stress on the start winding and capacitor. Repeated instant restarts shorten compressor life significantly.

A failed TDR combined with a weak crankcase heater is especially damaging — the compressor starts against high pressure AND with inadequate lubrication. This combination causes many "compressor locked rotor" failures that could have been prevented.

## Prevention Checklist

- **Crankcase heater**: Confirm it's warm to the touch 30 minutes after the system gets power (compressor not running). Replace if open or shorted.
- **Time-delay relay**: Verify a minimum 3-minute restart delay. Replace if timing has drifted below 2 minutes.
- **Power interruptions**: After any power outage, wait 10 minutes before restarting the system to let the crankcase heater do its job and allow pressure equalization.
- **Seasonal startup**: At the beginning of cooling season, turn the thermostat ON at least 4-6 hours before you actually need cooling — this powers the crankcase heater without cycling the compressor.

## When to Call a Professional

If your system shows any of these signs, schedule an [AC repair](https://ac-repair.today/services/ac-repair/) evaluation:
- Compressor hums but won't start, especially on the first hot day after a cool spell
- Repeated breaker trips on start-up after system has been off for a few hours
- You measure zero crankcase heater resistance or no temperature rise
- The system restarts immediately after shutting off (TDR failure)

For compressors that are already showing signs of wear from repeated hard starts, early intervention saves the compressor. An [AC maintenance](https://ac-repair.today/services/ac-maintenance/) visit that includes crankcase heater testing takes 15 minutes and can prevent a $2,500+ compressor replacement.

## About

This resource is provided by [AC Repair Today](https://ac-repair.today/) — a licensed Florida HVAC contractor (CAC1824118) serving Miami-Dade, Broward, and Palm Beach counties with same-day service and honest diagnostics.
