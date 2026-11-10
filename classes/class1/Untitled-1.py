#!/usr/bin/env python3
from datetime import datetime


def randomfunction():
    a = 1
    print(a)
    return "This is a random function"


def report_velocity(target: str, semi_major_axis_au: float, period_days: float) -> str:
    # Breakpoint idea: inspect `mean_motion` and `velocity` below.
    mean_motion = 2 * 3.14159 / period_days
    velocity = mean_motion * semi_major_axis_au * 1.496e8 / 86400
    timestamp = datetime.now().isoformat(timespec="seconds")
    randomfunction()
    return f"{timestamp} | {target:<12} | {velocity:7.2f} km/s"


if __name__ == "__main__":
    planets = [
        ("TRAPPIST-1e", 0.029, 6.1),
        ("GJ 486b", 0.017, 1.5),
        ("K2-18b", 0.160, 33.0),
    ]
    for target, axis, period in planets:
        print(report_velocity(target, axis, period))
