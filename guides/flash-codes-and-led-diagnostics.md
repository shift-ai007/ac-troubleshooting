# AC Control Board Flash Codes & LED Diagnostics

A complete guide to diagnosing AC problems by reading the LED error codes on your HVAC control board.

## Why Flash Codes Matter

When your AC stops working, the control board is the first component to know something is wrong. Before it shuts everything down, it blinks an error code through a small LED light that tells you — and a technician — exactly what triggered the fault.

Reading flash codes is the fastest way to diagnose an AC problem without special tools. In many cases, you can identify the root cause in 30 seconds without opening a multimeter.

## Common LED Locations

Most AC systems have a small LED indicator on the main control board inside the indoor air handler. You may find additional diagnostic LEDs on:

- **Indoor (air handler) control board**: The primary diagnostic LED. Usually green, amber, or red
- **Outdoor condenser control board**: Some modern split systems have a second LED near the compressor contactor
- **Furnace control board**: On gas-pack systems or dual-fuel setups
- **Thermostat sub-base**: Some communicating thermostats show error codes on the thermostat itself
- **Variable-speed blower module**: Separate LED for ECM blower motor diagnostics

## How to Read Flash Codes

### Safety First

1. **Turn off the system at the thermostat** — set it to OFF, not just a temperature change
2. **Locate the control board** — usually behind a metal access panel on the air handler. The panel is held by 1-4 screws (typically 5/16" or 1/4" hex head)
3. **Remove the panel carefully** — the door switch kills power to the board. If there is no door switch, shut off the breaker to the air handler
4. **Watch the LED** — note the pattern of short and long flashes

### Basic Pattern Interpretation

Flash codes use a simple convention:

| Pattern | Meaning |
|---------|---------|
| **1 flash, pause, repeat** | Normal operation / standby |
| **2 flashes, pause, repeat** | System fault or lockout |
| **3-7 flashes, pause, repeat** | Specific fault code |
| **Rapid flash (continuous)** | Polarity or wiring fault |
| **Solid on** | Board powered + no call for operation |
| **Solid off** | No power to board |
| **Alternating green/red** | Communicating protocol handshake |

### Common Code Ranges by Manufacturer

The exact meaning varies by brand, but most follow a loose standard:

**Carrier / Bryant / Payne** (when equipped with LED)
- 1 flash: Normal
- 2 flashes: Pressure switch lockout (high or low)
- 3 flashes: Temperature sensor fault
- 4 flashes: Lockout (auto-restart after 1 hour)
- 5 flashes: Rollout switch open
- 6 flashes: Communication error
- 7 flashes: Watchdog / board fault
- 8+ flashes: Check manufacturer manual (usually gas valve, inducer, or flame sense)

**Trane / American Standard**
- Green = normal operation
- Amber 1 flash = slow heartbeat (standby)
- Amber 2 flashes = demand not being met
- Amber 3+ flashes = specific fault reference required
- Red = error condition — check service manual

**Lennox**
- Green continuous = normal
- Green 1 flash/3s = standby
- Amber = warning (abnormal pressure or temp)
- Red = lockout condition — cycle power to reset
- Red/amber alternating = limit circuit fault

**Goodman / Amana / Daikin / ICP**
- 1 flash: Normal
- 2 flashes: Pressure switch open — check for dirty filter, blocked pipes, or refrigerant issues
- 3 flashes: Sensor fault — thermistor or temperature sensor
- 4 flashes: Lockout after 5 failed ignition attempts (furnace/gas-pack)
- 5 flashes: Rollout switch open or flame sensed without call
- 6 flashes: Communication error between indoor and outdoor units
- 7+ flashes: Various — reference specific model manual

**Rheem / Ruud**
- One flash every 10 seconds: Standby (normal)
- Two flashes: High pressure switch open
- Three flashes: Low pressure switch open  
- Four flashes: Freeze protection / low temperature
- Five flashes: Condensate overflow
- Six flashes: Communication loss
- Rapid flash: Reversed polarity

**York / Luxaire / Coleman**
- 1 blink: Normal
- 2 blinks: Low pressure fault
- 3 blinks: High pressure fault
- 4 blinks: Low voltage (<19VAC at control board)
- 5 blinks: Temperature sensor out of range
- 6 blinks: Communication fault

## What to Do After Reading the Code

### Codes You Can Reset Yourself

Some faults clear with a simple power cycle:

- **Pressure switch lockout** (2 flashes on most brands): If caused by temporary conditions — a dirty filter that's now clean, or a brief power sag — cycling power at the breaker (not the thermostat) may clear the code. Wait 5 minutes before restoring power. If the code returns within 24 hours, call a technician

- **Low voltage** (4 flashes on York, similar on others): Check the 24V transformer and main breaker. If your whole house experienced a brownout, the AC's transformer may have dropped below operating voltage. Once main power stabilizes, reset the breaker

- **Condensate overflow** (5 flashes on Rheem): The float switch detected water in the drain pan. Clear the condensate drain line (vinegar flush, wet-dry vacuum at the outdoor termination) and reset. If the code returns, the float switch may be stuck or the drain is permanently clogged

### When to Call a Professional

- **Sensor faults** (3 flashes on most brands): The thermistor or temperature sensor is out of range. These are inexpensive parts but require exact replacement and calibration
- **Communication errors** (6 flashes on many brands): The indoor and outdoor boards can't talk to each other. This is almost always a wiring problem or failed board — not a DIY fix
- **Compressor lockout** (4 flashes on some brands): The compressor protection has activated. This typically requires a multimeter and knowledge of compressor winding resistance values
- **Gas valve or ignition faults** (7+ flashes): These involve combustible gas. Leave this one to the pros

## Code Reset Procedure

For most systems, a controlled power reset is the only way to clear a fault code:

1. **Turn the thermostat OFF**
2. **Flip the AC breaker in your main panel** (the double-pole 30-50A breaker labeled "AC" or "Furnace")
3. **Wait 5 full minutes** — this allows the compressor head pressure to equalize. Less than 5 minutes can damage the compressor on restart
4. **Restore power** at the breaker
5. **Wait 2 minutes** for the control board to boot and run its self-test
6. **Set the thermostat to COOL, 5°F below room temperature**
7. **Watch the outdoor unit** — the contactor should engage, the fan should spin, and after 2-3 minutes the compressor should start

Count the LED flashes during startup. A brief double-flash during boot is normal (component check). A repeating flash pattern indicates the fault is still present.

## Special Cases: Communicating Equipment

Communicating systems (Carrier Infinity, Trane XL, Lennox iComfort, Daikin Fit) use a data protocol rather than simple 24V on/off signals. These have:

- **Two-wire data bus** (A/B terminals) instead of individual thermostat wires
- **Text-based error display** on the communicating thermostat screen
- **History logs** stored in the indoor and outdoor control boards

For these systems, skip the flash code reading — the thermostat screen will show a text error (e.g., "LC" for lockout, "88" for communication error, "E1" through "E9" for specific faults). A communicating system that shows no display at all is likely a 24V power issue at the transformer or data bus short.

## South Florida-Specific Code Patterns

Our climate creates predictable fault patterns that a knowledgeable homeowner can recognize:

- **Repeating 2-flash (pressure switch lockout) during summer afternoons**: Likely a high-pressure lockout from a dirty condenser coil. South Florida's combination of salt air, pollen, and construction dust fouls outdoor coils faster than anywhere in the continental US. A gentle coil rinse often clears this — see the [condenser maintenance guide](https://ac-repair.today/services/ac-maintenance/) for the correct wash procedure

- **Low pressure switch code after a temperature drop**: In South Florida's rare cold snaps (below 50°F), R-410A systems can trip low-pressure switches. If the code doesn't return when temperatures rise, no action needed

- **Condensate overflow in July-October**: Our rainy season saturates the ground around the drain pipe termination, which can cause the drain line to back up. A flooded drain pan during wet season that resolves when the ground dries is common — but if the code persists, the drain line likely has algae growth. Flush with a bleach solution monthly during rainy months

- **Temperature sensor faults in Miami-Dade**: The salt air causes connector corrosion on thermistor plugs at the control board. Cleaning the pins with electrical contact cleaner and applying dielectric grease often resolves intermittent sensor faults without replacing the sensor itself

## Resources

- For online manuals: look up your condenser model number (on the rating plate, usually on the side of the outdoor unit) and search for the diagnostic guide or service manual
- Most manufacturers provide a sticker on the inside of the air handler access panel with the flash code legend for your specific model
- For professional diagnostic help in South Florida: [AC Repair Today](https://ac-repair.today/services/ac-repair/) — licensed, same-day service available for all brands

## Important Note

Flash codes are manufacturer-specific. The codes listed here cover the most common brands and patterns, but always verify against the service manual for your specific model before making any decisions about repair. An incorrect diagnosis can lead to replacing parts unnecessarily. When in doubt, call a licensed HVAC technician.

---

*This guide is for informational purposes. Electrical troubleshooting carries risk of shock or equipment damage. If you're not comfortable removing access panels or working near live electrical components, skip the DIY diagnosis and call a licensed professional.*
