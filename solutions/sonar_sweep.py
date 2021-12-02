"""
Part One
========

The first order of business is to figure out how quickly the depth
increases, just so you know what you're dealing with - you never know
if the keys will get carried into deeper water by an ocean current or a
fish or something.

To do this, count the number of times a depth measurement increases
from the previous measurement.

Part Two
========
Count the number of times the sum of measurements in this sliding
window increases from the previous sum. So, compare A with B, then
compare B with C, then C with D, and so on. Stop when there aren't
enough measurements left to create a new three-measurement sum.
"""
from typing import List


def count_increases(measurements: List[int]) -> int:
    """Count the number of times the depth measurement increases."""
    total = 0
    past = 9999999  # Make the first comparison arbitrarily large.
    for measurement in measurements:
        if measurement > past:
            total += 1
        past = measurement

    return total


def count_windows(measurements: List[int]) -> int:
    """Count the number of times the total depth of a three-measurement
    window increases.
    """
    total = 0
    first = measurements[0]
    second = measurements[1]
    third = measurements[2]
    past = sum([first, second, third])
    for measurement in measurements[3:]:
        first = second
        second = third
        third = measurement
        new = sum([first, second, third])
        if new > past:
            total += 1
        past = new

    return total


if __name__ == "__main__":
    with open("inputs/sonar_sweep.txt") as input:
        measurements = [int(measurement) for measurement in input]

    print(f"Part One: {count_increases(measurements)}")
    print(f"Part Two: {count_windows(measurements)}")
