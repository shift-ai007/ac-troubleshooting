#!/usr/bin/env python3
"""
Refrigerant Pressure-Temperature Reference Tool

Look up saturation temperatures for common HVAC refrigerants at a given
pressure, or find the expected pressure for a given temperature. Includes
R-410A, R-22, R-32, and R-454B.

Usage:
    python3 refrigerant-pt-chart.py                  # Interactive mode
    python3 refrigerant-pt-chart.py --temp 95         # Show pressures at 95F
    python3 refrigerant-pt-chart.py --pressure 350    # Show saturation temps
    python3 refrigerant-pt-chart.py --refrigerant R-410A --temp 85

No dependencies beyond Python 3.6+ standard library.
"""

import argparse
import sys

PT_DATA = {
    "R-410A": [
        (-50, 10.2), (-40, 14.9), (-30, 20.7), (-20, 28.1), (-10, 37.1),
        (0, 48.0), (10, 60.9), (20, 76.1), (30, 93.7), (40, 114.0),
        (50, 137.3), (60, 163.7), (70, 193.6), (80, 227.2), (90, 264.8),
        (100, 306.8), (110, 353.4), (120, 405.0), (130, 462.0), (140, 524.7), (150, 593.5),
    ],
    "R-22": [
        (-50, 5.6), (-40, 9.3), (-30, 14.5), (-20, 21.6), (-10, 30.8),
        (0, 42.5), (10, 56.8), (20, 74.0), (30, 94.4), (40, 118.2),
        (50, 145.8), (60, 177.5), (70, 213.7), (80, 254.7), (90, 301.0),
        (100, 352.8), (110, 410.7), (120, 475.3), (130, 547.2), (140, 627.1), (150, 715.8),
    ],
    "R-32": [
        (-50, 6.8), (-40, 10.6), (-30, 15.8), (-20, 22.4), (-10, 30.8),
        (0, 41.3), (10, 54.1), (20, 69.6), (30, 88.0), (40, 109.7),
        (50, 135.0), (60, 164.4), (70, 198.2), (80, 236.8), (90, 280.6),
        (100, 330.0), (110, 385.5), (120, 447.4), (130, 516.4), (140, 593.0), (150, 678.0),
    ],
    "R-454B": [
        (-50, 5.0), (-40, 8.1), (-30, 12.3), (-20, 17.8), (-10, 24.8),
        (0, 33.7), (10, 44.7), (20, 58.1), (30, 74.2), (40, 93.4),
        (50, 115.9), (60, 142.1), (70, 172.4), (80, 207.2), (90, 246.8),
        (100, 291.7), (110, 342.2), (120, 398.8), (130, 462.0), (140, 532.3), (150, 610.3),
    ],
}

REFRIGERANT_NAMES = {
    "R-410A": "R-410A (most common in new systems, 2005+)",
    "R-22": "R-22 (older systems, phased out)",
    "R-32": "R-32 (newer single-component refrigerant)",
    "R-454B": "R-454B (A2L mildly flammable, replacing 410A 2025+)",
}

def lerp(x1, y1, x2, y2, x):
    if abs(x2 - x1) < 0.001:
        return (y1 + y2) / 2
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

def pressure_at_temp(refrigerant, temp_f):
    data = PT_DATA.get(refrigerant)
    if not data:
        raise ValueError(f"Unknown refrigerant: {refrigerant}")
    if temp_f <= data[0][0]:
        return data[0][1]
    if temp_f >= data[-1][0]:
        return data[-1][1]
    for i in range(len(data) - 1):
        t1, p1 = data[i]; t2, p2 = data[i + 1]
        if t1 <= temp_f <= t2:
            return round(lerp(t1, p1, t2, p2, temp_f), 1)
    return data[-1][1]

def temp_at_pressure(refrigerant, pressure_psig):
    data = PT_DATA.get(refrigerant)
    if not data:
        raise ValueError(f"Unknown refrigerant: {refrigerant}")
    if pressure_psig <= data[0][1]:
        return data[0][0]
    if pressure_psig >= data[-1][1]:
        return data[-1][0]
    for i in range(len(data) - 1):
        t1, p1 = data[i]; t2, p2 = data[i + 1]
        if p1 <= pressure_psig <= p2:
            return round(lerp(p1, t1, p2, t2, pressure_psig), 1)
    return data[-1][0]

def print_pt_table(refrigerant, start_f=30, end_f=130, step=5):
    print(f"\n{'─'*60}")
    print(f"  {REFRIGERANT_NAMES.get(refrigerant, refrigerant)}")
    print(f"{'─'*60}")
    print(f"  {'Temp(F)':<12} {'Pressure(psig)':<18}")
    print(f"  {'─'*10:<12} {'─'*16:<18}")
    temp = start_f
    while temp <= end_f:
        press = pressure_at_temp(refrigerant, temp)
        print(f"  {temp:<12.0f} {press:<18.1f}")
        temp += step
    print(f"{'─'*60}")

def interactive_mode():
    print("\n" + "="*60)
    print("  Refrigerant Pressure-Temperature Reference")
    print("="*60)
    ref_list = list(PT_DATA.keys())
    for i, r in enumerate(ref_list, 1):
        print(f"  {i}. {REFRIGERANT_NAMES[r]}")
    try:
        choice = int(input(f"\nSelect refrigerant (1-{len(ref_list)}): ")) - 1
        if 0 <= choice < len(ref_list):
            refrigerant = ref_list[choice]
            print_pt_table(refrigerant)
            print(f"\n  Need professional AC repair? https://ac-repair.today/services/ac-repair/")
    except ValueError:
        print("  Invalid selection.")

def main():
    parser = argparse.ArgumentParser(description="Refrigerant PT Reference Tool")
    parser.add_argument("--refrigerant", "-r", choices=sorted(PT_DATA.keys()))
    parser.add_argument("--temp", "-t", type=float, help="Pressure at this temp (F)")
    parser.add_argument("--pressure", "-p", type=float, help="Temp at this pressure (psig)")
    parser.add_argument("--table", action="store_true", help="Print PT table")
    args = parser.parse_args()
    if args.refrigerant and args.temp is not None:
        p = pressure_at_temp(args.refrigerant, args.temp)
        print(f"{args.refrigerant}: {args.temp:.0f}F -> {p:.1f} psig")
    elif args.refrigerant and args.pressure is not None:
        t = temp_at_pressure(args.refrigerant, args.pressure)
        print(f"{args.refrigerant}: {args.pressure:.1f} psig -> {t:.0f}F")
    elif args.refrigerant and args.table:
        print_pt_table(args.refrigerant)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
