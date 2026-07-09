#!/usr/bin/env python3
"""
Refrigerant Pressure-Temperature Reference Tool

Look up saturation temperatures for common HVAC refrigerants at a given
pressure, or find the expected pressure for a given temperature. Includes
R-410A, R-22, R-32, and R-454B (the new A2L refrigerant replacing R-410A).

Helps diagnose improper charge: compare your measured pressures against
the PT chart to determine if refrigerant is low, normal, or overcharged.

Usage:
    python3 refrigerant-pt-chart.py                  # Interactive mode
    python3 refrigerant-pt-chart.py --temp 95         # Show pressures at 95°F
    python3 refrigerant-pt-chart.py --pressure 350    # Show saturation temps at 350 psi
    python3 refrigerant-pt-chart.py --refrigerant R-410A --temp 85

No dependencies beyond Python 3.6+ standard library.
"""

import argparse
import sys
import math

# Saturation pressure-temperature data points (°F → psig)
# Each entry: (temp_F, pressure_psig) for the saturated vapor line
# Data interpolated from ASHRAE refrigerant tables

PT_DATA = {
    "R-410A": [
        (-50, 10.2), (-45, 12.4), (-40, 14.9), (-35, 17.6), (-30, 20.7),
        (-25, 24.2), (-20, 28.1), (-15, 32.4), (-10, 37.1), (-5, 42.3),
        (0, 48.0), (5, 54.2), (10, 60.9), (15, 68.2), (20, 76.1),
        (25, 84.6), (30, 93.7), (35, 103.5), (40, 114.0), (45, 125.3),
        (50, 137.3), (55, 150.1), (60, 163.7), (65, 178.2), (70, 193.6),
        (75, 209.9), (80, 227.2), (85, 245.5), (90, 264.8), (95, 285.3),
        (100, 306.8), (105, 329.5), (110, 353.4), (115, 378.6), (120, 405.0),
        (125, 432.8), (130, 462.0), (135, 492.6), (140, 524.7), (145, 558.3),
        (150, 593.5),
    ],
    "R-22": [
        (-50, 5.6), (-45, 7.3), (-40, 9.3), (-35, 11.7), (-30, 14.5),
        (-25, 17.8), (-20, 21.6), (-15, 25.9), (-10, 30.8), (-5, 36.3),
        (0, 42.5), (5, 49.3), (10, 56.8), (15, 65.0), (20, 74.0),
        (25, 83.8), (30, 94.4), (35, 105.8), (40, 118.2), (45, 131.5),
        (50, 145.8), (55, 161.1), (60, 177.5), (65, 195.0), (70, 213.7),
        (75, 233.6), (80, 254.7), (85, 277.2), (90, 301.0), (95, 326.2),
        (100, 352.8), (105, 381.0), (110, 410.7), (115, 442.2), (120, 475.3),
        (125, 510.3), (130, 547.2), (135, 586.1), (140, 627.1), (145, 670.3),
        (150, 715.8),
    ],
    "R-32": [
        (-50, 6.8), (-40, 10.6), (-30, 15.8), (-25, 18.9), (-20, 22.4),
        (-15, 26.4), (-10, 30.8), (-5, 35.8), (0, 41.3), (5, 47.4),
        (10, 54.1), (15, 61.5), (20, 69.6), (25, 78.4), (30, 88.0),
        (35, 98.4), (40, 109.7), (45, 121.9), (50, 135.0), (55, 149.2),
        (60, 164.4), (65, 180.7), (70, 198.2), (75, 216.9), (80, 236.8),
        (85, 258.0), (90, 280.6), (95, 304.6), (100, 330.0), (105, 357.0),
        (110, 385.5), (115, 415.6), (120, 447.4), (125, 481.0), (130, 516.4),
        (135, 553.7), (140, 593.0), (145, 634.4), (150, 678.0),
    ],
    "R-454B": [
        (-50, 5.0), (-40, 8.1), (-30, 12.3), (-25, 14.9), (-20, 17.8),
        (-15, 21.1), (-10, 24.8), (-5, 29.0), (0, 33.7), (5, 38.9),
        (10, 44.7), (15, 51.1), (20, 58.1), (25, 65.8), (30, 74.2),
        (35, 83.4), (40, 93.4), (45, 104.2), (50, 115.9), (55, 128.5),
        (60, 142.1), (65, 156.7), (70, 172.4), (75, 189.2), (80, 207.2),
        (85, 226.4), (90, 246.8), (95, 268.6), (100, 291.7), (105, 316.2),
        (110, 342.2), (115, 369.7), (120, 398.8), (125, 429.5), (130, 462.0),
        (135, 496.2), (140, 532.3), (145, 570.3), (150, 610.3),
    ],
}

REFRIGERANT_NAMES = {
    "R-410A": "R-410A (most common in new systems, 2005+)",
    "R-22": "R-22 (older systems, being phased out)",
    "R-32": "R-32 (newer single-component refrigerant)",
    "R-454B": "R-454B (A2L mildly flammable, replacing 410A in 2025+)",
}

REFRIGERANT_DESCRIPTIONS = {
    "R-410A": (
        "The standard residential refrigerant since the R-22 phaseout. "
        "Operates at 1.6× higher pressures than R-22. Identified by the light "
        "pink drum color and the higher pressure readings (typical head "
        "pressure on a 95°F day: 275-325 psig)."
    ),
    "R-22": (
        "The longtime standard for residential AC, being phased out under the "
        "Montreal Protocol. Production ended in 2020; only reclaimed/recycled "
        "R-22 remains. Identified by the light green drum color. Widely "
        "present in systems manufactured before 2010. Typical head pressure "
        "on a 95°F day: 215-255 psig."
    ),
    "R-32": (
        "A single-component HFC refrigerant gaining adoption in ductless mini-splits "
        "and some residential systems. Class A2L (mildly flammable). Lower GWP than R-410A "
        "(675 vs 2088). Found in newer Daikin, Mitsubishi, and Fujitsu systems. "
        "Typical head pressure similar to R-410A but slightly higher."
    ),
    "R-454B": (
        "The designated R-410A replacement for 2025+ residential systems. A2L mildly "
        "flammable (requires special handling). 78% lower GWP than R-410A. Used by "
        "Carrier, Bryant, and ICP brands as Puron Advance. Similar pressure "
        "characteristics to R-410A — existing service tools mostly compatible. "
        "NOT retrofittable into existing R-410A systems."
    ),
}


def lerp(x1, y1, x2, y2, x):
    """Linear interpolation between two points."""
    if abs(x2 - x1) < 0.001:
        return (y1 + y2) / 2
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


def pressure_at_temp(refrigerant: str, temp_f: float) -> float:
    """Return saturation pressure (psig) for a given temperature (°F)."""
    data = PT_DATA.get(refrigerant)
    if not data:
        raise ValueError(f"Unknown refrigerant: {refrigerant}")

    # Clamp to range
    if temp_f <= data[0][0]:
        return data[0][1]
    if temp_f >= data[-1][0]:
        return data[-1][1]

    for i in range(len(data) - 1):
        t1, p1 = data[i]
        t2, p2 = data[i + 1]
        if t1 <= temp_f <= t2:
            return round(lerp(t1, p1, t2, p2, temp_f), 1)

    return data[-1][1]


def temp_at_pressure(refrigerant: str, pressure_psig: float) -> float:
    """Return saturation temperature (°F) for a given pressure (psig)."""
    data = PT_DATA.get(refrigerant)
    if not data:
        raise ValueError(f"Unknown refrigerant: {refrigerant}")

    if pressure_psig <= data[0][1]:
        return data[0][0]
    if pressure_psig >= data[-1][1]:
        return data[-1][0]

    for i in range(len(data) - 1):
        t1, p1 = data[i]
        t2, p2 = data[i + 1]
        if p1 <= pressure_psig <= p2:
            return round(lerp(p1, t1, p2, t2, pressure_psig), 1)

    return data[-1][0]


def print_pt_table(refrigerant: str, start_f: float = 30, end_f: float = 130, step: float = 5):
    """Print a formatted PT chart for a given refrigerant."""
    print(f"\n{'─' * 60}")
    print(f"  {REFRIGERANT_NAMES[refrigerant]}")
    print(f"  {REFRIGERANT_DESCRIPTIONS[refrigerant]}")
    print(f"{'─' * 60}")
    print(f"  {'Temp (°F)':<12} {'Pressure (psig)':<18} {'Notes'}")
    print(f"  {'─' * 10:<12} {'─' * 16:<18} {'─' * 28}")

    temp = start_f
    while temp <= end_f:
        press = pressure_at_temp(refrigerant, temp)
        note = ""
        if refrigerant in ("R-410A", "R-454B") and 90 <= temp <= 100:
            note = "← Typical condensing range"
        elif refrigerant == "R-22" and 90 <= temp <= 100:
            note = "← Typical condensing range"
        elif 35 <= temp <= 45:
            note = "← Typical evaporator range"
        print(f"  {temp:<12.0f} {press:<18.1f} {note}")
        temp += step

    print(f"{'─' * 60}\n")


def print_charge_diagnosis(refrigerant: str, outdoor_temp: float,
                           suction_pressure: float, head_pressure: float):
    """Interpret pressures and give a charge assessment."""
    print_header("Charge Analysis")

    if refrigerant not in PT_DATA:
        print(f"  No PT data for {refrigerant}.")
        return

    # Expected saturated condensing temp = outdoor temp + 25-35°F (condenser split)
    expected_condensing_f = outdoor_temp + 30
    expected_evaporator_f = 40  # Typical evaporator saturation

    expected_head = pressure_at_temp(refrigerant, expected_condensing_f)
    expected_suction = pressure_at_temp(refrigerant, expected_evaporator_f)

    print(f"  Outdoor ambient: {outdoor_temp:.0f}°F")
    print(f"  Expected head pressure: ~{expected_head:.0f} psig "
          f"(saturated condensing at ~{expected_condensing_f:.0f}°F)")
    print(f"  Expected suction pressure: ~{expected_suction:.0f} psig "
          f"(saturated evaporating at ~{expected_evaporator_f:.0f}°F)")
    print()

    # Analyze head pressure
    head_diff = head_pressure - expected_head
    head_pct = (head_pressure / expected_head) * 100 if expected_head > 0 else 100

    if head_diff < -50:
        print("  ⚠ LOW HEAD PRESSURE — Possible causes:")
        print("     - Undercharged refrigerant (most common)")
        print("     - Restriction in liquid line (filter drier blocked)")
        print("     - Condenser fan running too fast or wind-aided")
    elif head_pct > 115:
        print("  ⚠ HIGH HEAD PRESSURE — Possible causes:")
        print("     - Dirty condenser coil (most common in South Florida)")
        print("     - Overcharged refrigerant")
        print("     - Non-condensables in system (air/moisture)")
        print("     - Condenser fan not running or running slow")
        print("     - Recirculation (hot discharge air pulled back into coil)")
    else:
        print("  ✓ Head pressure within expected range.")

    # Analyze suction pressure
    suction_diff = suction_pressure - expected_suction
    if suction_diff < -10 and head_pct < 90:
        print("  ⚠ LOW SUCTION + LOW HEAD = UNDERCHARGED — Needs leak search + recharge")
    elif suction_diff > 15:
        print("  ⚠ HIGH SUCTION PRESSURE — Possible causes:")
        print("     - Overcharged refrigerant")
        print("     - TXV stuck open or overfeeding")
        print("     - Indoor airflow too high")
        print("     - Compressor valves failing (high suction + low head)")
        if head_pct < 85:
            print("     → COMBINED with low head = bad compressor valves or bypass")
    else:
        print("  ✓ Suction pressure within expected range.")

    print()
    print("  NOTE: This analysis is a guideline, not a substitute for")
    print("  proper superheat, subcooling, and subcooling measurements.")
    print(f"  For professional diagnosis, contact a licensed AC technician:")
    print(f"  https://ac-repair.today/services/ac-repair/")


def print_header(text: str) -> None:
    """Print a section header."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def interactive_mode() -> None:
    """Run the tool in interactive mode."""
    print_header("Refrigerant Pressure-Temperature Reference")

    # Choose refrigerant
    print("Available refrigerants:")
    ref_list = list(PT_DATA.keys())
    for i, ref in enumerate(ref_list, 1):
        print(f"  {i}. {REFRIGERANT_NAMES[ref]}")

    while True:
        try:
            choice = input(f"\nSelect refrigerant (1-{len(ref_list)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(ref_list):
                refrigerant = ref_list[idx]
                break
            print(f"  Please enter 1-{len(ref_list)}.")
        except (ValueError, IndexError):
            print(f"  Please enter 1-{len(ref_list)}.")

    # Print PT table
    print_pt_table(refrigerant, start_f=30, end_f=130, step=5)

    # Optional: diagnose charge
    print("Want to diagnose your system's refrigerant charge?")
    diag = input("  Enter outdoor temp (°F) or press Enter to skip: ").strip()
    if diag:
        try:
            outdoor = float(diag)
            suction = float(input("  Suction (low side) pressure (psig): "))
            head = float(input("  Head (high side) pressure (psig): "))
            print_charge_diagnosis(refrigerant, outdoor, suction, head)
        except ValueError:
            print("  Invalid input, skipping charge analysis.")

    print("\n  Need professional AC repair or refrigerant service?")
    print("  → https://ac-repair.today/services/ac-repair/")


def main():
    parser = argparse.ArgumentParser(
        description="Refrigerant Pressure-Temperature Reference Tool",
        epilog="No dependencies beyond Python 3.6+ standard library.",
    )
    parser.add_argument(
        "--refrigerant", "-r",
        choices=sorted(PT_DATA.keys()),
        default=None,
        help="Refrigerant type (default: interactive selection)",
    )
    parser.add_argument(
        "--temp", "-t",
        type=float,
        default=None,
        help="Look up pressure at this temperature (°F)",
    )
    parser.add_argument(
        "--pressure", "-p",
        type=float,
        default=None,
        help="Look up saturation temperature at this pressure (psig)",
    )
    parser.add_argument(
        "--table",
        action="store_true",
        help="Print full PT table for the selected refrigerant",
    )

    args = parser.parse_args()

    if args.refrigerant and args.temp is not None:
        # Single lookup: temp → press
        p = pressure_at_temp(args.refrigerant, args.temp)
        print(f"{args.refrigerant}: {args.temp:.0f}°F → {p:.1f} psig")
    elif args.refrigerant and args.pressure is not None:
        # Single lookup: press → temp
        t = temp_at_pressure(args.refrigerant, args.pressure)
        print(f"{args.refrigerant}: {args.pressure:.1f} psig → {t:.0f}°F")
    elif args.refrigerant and args.table:
        print_pt_table(args.refrigerant, start_f=30, end_f=130, step=5)
    elif args.refrigerant:
        print(f"Known refrigerants: {', '.join(sorted(PT_DATA.keys()))}")
        print(f"Use --table to show full PT chart, --temp or --pressure for a lookup.")
    elif not sys.stdin.isatty():
        print("No input detected. Run without arguments for interactive mode, or use --help.")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
