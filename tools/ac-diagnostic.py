#!/usr/bin/env python3
"""
AC Troubleshooting Diagnostic Tool — Interactive Guide

A decision-tree diagnostic tool that walks homeowners through
common AC problems step by step. Run it when your AC acts up to
narrow down the cause and decide whether it's a DIY fix or a
professional service call.

Usage:
    python3 ac-diagnostic.py

No dependencies beyond Python 3.6+ standard library.
"""

import sys
import time


def print_header(text: str) -> None:
    """Print a section header with decorative border."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{'=' * width}")
    print(f"  {text}")
    print(f"{'=' * width}\n")


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please answer 'y' or 'n'.")


def press_enter() -> None:
    """Wait for user to press Enter."""
    input("\n  [Press Enter to continue...]")


def diagnose_power() -> dict:
    """Diagnose power-related issues — system won't turn on."""
    print_header("Step 1: Check the Basics")

    # Thermostat check
    print("  First, check your thermostat:")
    print("  - Is it set to COOL mode?")
    print("  - Is the set temperature lower than room temperature?")
    print("  - Does the display turn on?\n")

    if ask_yes_no("Does the thermostat display show any activity?"):
        print("\n  Good — the thermostat has power. Let's check the settings.")
        if ask_yes_no("Is the thermostat set to COOL and the temp set below room temp?"):
            return {"diagnosis": "thermostat_settings_correct",
                    "summary": "Thermostat settings look correct.",
                    "next_step": "breaker_check"}
        else:
            return {"diagnosis": "thermostat_settings_wrong",
                    "summary": "Adjust thermostat to COOL mode and lower the set temperature.",
                    "action": "diy",
                    "fix": "Set thermostat to COOL and 5°F below room temperature. Wait 5 minutes.",
                    "target_page": None}
    else:
        print("\n  The thermostat may be dead. Try these:")
        print("  1. Replace batteries (if battery-powered)")
        print("  2. Check if the circuit breaker for the thermostat/furnace is on")
        print("  3. For smart thermostats, check if the C-wire is connected")
        if ask_yes_no("Did replacing batteries or checking the breaker help?"):
            return {"diagnosis": "thermostat_power_fixed",
                    "summary": "Thermostat power issue resolved.",
                    "action": "diy",
                    "fix": "Replaced thermostat batteries or reset breaker.",
                    "target_page": None}
        return {"diagnosis": "no_power_to_thermostat",
                "summary": "No power to thermostat after basic checks.",
                "action": "call_pro",
                "fix": "Likely a blown transformer, tripped breaker at the main panel, or wiring issue.",
                "target_page": "ac-repair"}


def check_breaker() -> dict:
    """Check the circuit breaker for the AC system."""
    print_header("Step 2: Check the Circuit Breaker")

    print("  Locate your electrical panel and look for:")
    print("  - A breaker labeled 'AC', 'HVAC', 'Condenser', or 'Furnace'")
    print("  - Breakers that are in the middle position (tripped) vs fully ON or OFF")
    print("  - DO NOT touch any breaker if you see signs of burning or melting\n")

    if ask_yes_no("Is the AC breaker tripped (in the middle position)?"):
        print("\n  Reset it by flipping fully OFF, then fully back ON.")
        print("  Wait 5-10 minutes for the AC system to restart.")
        if ask_yes_no("Did the AC start working after resetting the breaker?"):
            return {"diagnosis": "breaker_tripped_reset_ok",
                    "summary": "Tripped breaker was the cause. AC is working now.",
                    "action": "diy",
                    "fix": "Reset the AC breaker. Monitor for future trips — repeated tripping indicates an electrical fault needing professional attention.",
                    "target_page": None}
        else:
            return {"diagnosis": "breaker_tripped_ac_still_off",
                    "summary": "Breaker was tripped, reset didn't restore AC.",
                    "action": "call_pro",
                    "fix": "Possible short circuit, failed compressor, or capacitor. Requires a licensed HVAC technician.",
                    "target_page": "ac-repair"}
    else:
        print("\n  Breaker looks fine. Let's move to the outdoor unit.")
        press_enter()
        return {"diagnosis": "breaker_ok",
                "summary": "Breaker is not tripped.",
                "next_step": "outdoor_check"}


def check_outdoor_unit() -> dict:
    """Inspect the outdoor condenser unit."""
    print_header("Step 3: Inspect the Outdoor Unit")

    print("  Go outside and find your condenser unit. Check for:\n")
    print("  1. Is the unit running? Listen for the fan and compressor")
    print("  2. Is the fan spinning freely?")
    print("  3. Are there leaves, grass, or debris blocking the sides?")
    print("  4. Is there ice or frost on the copper lines or the unit itself?")
    print("  5. Is the unit level and on a solid surface?\n")

    if ask_yes_no("Is the outdoor unit running (fan spinning, compressor humming)?"):
        return {"diagnosis": "outdoor_unit_running",
                "summary": "Outdoor unit is running but air isn't cooling.",
                "next_step": "airflow_check"}
    else:
        print("\n  The outdoor unit is not running. Let's check why.\n")

        if ask_yes_no("Can you hear a humming sound from the unit but the fan isn't spinning?"):
            return {"diagnosis": "capacitor_failed",
                    "summary": "Humming + non-spinning fan = failed capacitor (most common AC failure).",
                    "action": "call_pro",
                    "fix": "The run capacitor needs replacement. This is a common, affordable repair ($150-250) but requires a licensed technician — capacitors store dangerous voltage even when power is off.",
                    "target_page": "ac-repair"}

        if ask_yes_no("Is the unit blocked by debris, vegetation, or overgrown bushes?"):
            return {"diagnosis": "blocked_condenser",
                    "summary": "Blocked condenser unit restricts airflow and causes overheating.",
                    "action": "diy",
                    "fix": "Clear at least 24 inches of space around all sides of the unit. Trim vegetation back. Gently hose off dirt from the coils.",
                    "target_page": "ac-maintenance"}

        return {"diagnosis": "outdoor_unit_dead",
                "summary": "Outdoor unit not running — no power, no sound.",
                "action": "call_pro",
                "fix": "Could be a tripped safety switch, failed contactor, blown fuse, or compressor issue.",
                "target_page": "ac-repair"}


def check_airflow() -> dict:
    """Check indoor airflow — air filter, registers, ducts."""
    print_header("Step 4: Airflow Check")

    print("  Now check inside for airflow problems:\n")

    # Air filter
    print("  Air filter — the single most overlooked cause of AC problems.")
    if ask_yes_no("Have you checked or replaced the air filter in the last 3 months?"):
        print("\n  Good. Let's check the registers.\n")
    else:
        print("\n  A dirty filter is the #1 cause of poor cooling. Check it now.")
        print("  Location: usually in the return air grille, furnace cabinet,")
        print("  or in a slot near the thermostat.\n")
        if ask_yes_no("Was the filter dirty?"):
            return {"diagnosis": "dirty_filter",
                    "summary": "Dirty air filter was restricting airflow.",
                    "action": "diy",
                    "fix": "Replace with a new filter of the same size and type. Use MERV 8-11 for residential. Change every 1-3 months.",
                    "target_page": "ac-maintenance"}

    # Registers
    if ask_yes_no("Are all supply vents (registers) open and unobstructed?"):
        print("\n  Good. Vents are clear.\n")
    else:
        return {"diagnosis": "blocked_registers",
                "summary": "Blocked or closed registers restrict airflow.",
                "action": "diy",
                "fix": "Open all supply registers and ensure furniture, curtains, or rugs aren't blocking them.",
                "target_page": None}

    return {"diagnosis": "airflow_ok",
            "summary": "Airflow appears normal. The issue is likely refrigerant-related.",
            "next_step": "refrigerant_check"}


def check_refrigerant() -> dict:
    """Check refrigerant-related symptoms."""
    print_header("Step 5: Refrigerant Check")

    print("  Refrigerant issues show specific symptoms:")
    print("  - Ice or frost on the copper lines or outdoor unit")
    print("  - Hissing or bubbling sounds from the unit")
    print("  - AC runs but never cools enough")
    print("  - Higher than normal electric bills\n")

    if ask_yes_no("Do you see ice or frost on any AC pipes or the outdoor unit?"):
        return {"diagnosis": "low_refrigerant",
                "summary": "Ice/frost indicates low refrigerant charge — the most common serious AC issue.",
                "action": "call_pro",
                "fix": "Low refrigerant means there's a leak. A technician must locate and repair the leak, then recharge the system. Running the AC with low refrigerant will damage the compressor. Licensed HVAC contractor required — refrigerant handling is EPA-regulated.",
                "target_page": "ac-repair"}

    if ask_yes_no("Do you hear a hissing or gurgling sound near the indoor or outdoor unit?"):
        return {"diagnosis": "refrigerant_leak",
                "summary": "Audible hissing/gurgling indicates a refrigerant leak.",
                "action": "call_pro",
                "fix": "Refrigerant leaks require EPA-certified technician repair. Call a licensed HVAC pro.",
                "target_page": "ac-repair"}

    return {"diagnosis": "likely_other",
            "summary": "No obvious refrigerant symptoms found.",
            "action": "call_pro",
            "fix": "Could be a failing compressor, TXV valve issue, or electrical problem. A technician with gauges and diagnostic tools can pinpoint the cause.",
            "target_page": "ac-repair"}


def print_result(result: dict) -> None:
    """Print the diagnostic result with action guidance."""
    print_header("DIAGNOSTIC RESULT")
    print(f"  {result.get('summary', 'No clear diagnosis.')}\n")

    action = result.get("action", "unknown")
    if action == "diy":
        print("  VERDICT: DIY FIX")
        print(f"  Fix: {result.get('fix', '')}\n")
        print("  Safety: Turn off power at the breaker before any hands-on work.")
    elif action == "call_pro":
        print("  VERDICT: CALL A PROFESSIONAL")
        print(f"  Reason: {result.get('fix', '')}\n")
        print("  Do NOT attempt electrical or refrigerant repairs yourself.")
        print("  Licensed technicians have the training, tools, and EPA certification.\n")

        target = result.get("target_page", "ac-repair")
        if target == "ac-repair":
            print("  Need emergency AC repair in South Florida?")
            print("  Same-day service available — (305) 850-6810")
            print("  Licensed & insured | FL CAC1824118")
        elif target == "ac-maintenance":
            print("  Schedule a maintenance tune-up to prevent future issues:")
            print("  Learn more at https://ac-repair.today/services/ac-maintenance/")
    else:
        print(f"  Next step: {result.get('next_step', 'Consult the full guide for next steps.')}")


def run_diagnostic() -> None:
    """Run the full interactive diagnostic sequence."""
    print_header("AC DIAGNOSTIC TOOL")
    print("  This tool guides you through common AC problems step by step.")
    print("  Answer each question honestly — the result will tell you")
    print("  whether it's a DIY fix or time to call a professional.")
    print("\n  Have your thermostat and electrical panel accessible.")

    press_enter()

    result = diagnose_power()

    while "next_step" in result:
        step = result["next_step"]
        if step == "breaker_check":
            result = check_breaker()
        elif step == "outdoor_check":
            result = check_outdoor_unit()
        elif step == "airflow_check":
            result = check_airflow()
        elif step == "refrigerant_check":
            result = check_refrigerant()
        else:
            result = {"diagnosis": "unknown",
                      "summary": "Could not complete the diagnostic. Consult the full guide for manual troubleshooting.",
                      "action": "call_pro",
                      "fix": "Please refer to the AC Troubleshooting Guide at https://github.com/shift-ai007/ac-troubleshooting",
                      "target_page": "ac-repair"}
            break

    print_result(result)


def main() -> None:
    try:
        run_diagnostic()
    except KeyboardInterrupt:
        print("\n\n  Diagnostic cancelled. Stay cool!")
        sys.exit(0)


if __name__ == "__main__":
    main()
