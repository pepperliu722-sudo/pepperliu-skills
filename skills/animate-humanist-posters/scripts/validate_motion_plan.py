#!/usr/bin/env python3
"""Validate a humanist poster motion-plan JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_ZONE_FIELDS = {
    "name",
    "role",
    "components",
    "motion_type",
    "cadence",
    "neighbor_variation",
    "cause",
    "background_restoration",
    "loop_behavior",
}


def validate(plan: dict) -> list[str]:
    errors: list[str] = []

    duration = plan.get("duration_seconds")
    if not isinstance(duration, (int, float)) or not 5 <= duration <= 8:
        errors.append("duration_seconds must be between 5 and 8")

    fps = plan.get("fps")
    if fps not in {24, 25, 30}:
        errors.append("fps must be 24, 25, or 30")

    if not isinstance(plan.get("text_locked"), bool):
        errors.append("text_locked must be a boolean")

    zones = plan.get("motion_zones")
    if not isinstance(zones, list) or not 2 <= len(zones) <= 3:
        errors.append("motion_zones must contain 2 or 3 readable zones")
        return errors

    for index, zone in enumerate(zones, start=1):
        if not isinstance(zone, dict):
            errors.append(f"zone {index} must be an object")
            continue

        missing = sorted(REQUIRED_ZONE_FIELDS - set(zone))
        if missing:
            errors.append(f"zone {index} missing fields: {', '.join(missing)}")

        components = zone.get("components")
        if not isinstance(components, list) or len(components) < 2:
            errors.append(f"zone {index} must list at least 2 sub-components")

        variation = zone.get("neighbor_variation")
        if not isinstance(variation, list) or len(variation) < 2:
            errors.append(
                f"zone {index} must vary neighbors in at least 2 properties"
            )

        for field in ("cause", "background_restoration", "loop_behavior"):
            value = zone.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"zone {index} field {field} must be non-empty")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()

    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate(plan)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Motion plan is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
