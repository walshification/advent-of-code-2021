"""
The first order of business is to figure out how quickly the depth
increases, just so you know what you're dealing with - you never know
if the keys will get carried into deeper water by an ocean current or a
fish or something.

To do this, count the number of times a depth measurement increases
from the previous measurement.
"""
from typing import List


def main(measurements: List[int]) -> int:
    """Count the number of times the depth measurement increases."""
    total = 0
    past = 9999999  # Make the first comparison arbitrarily large.
    # import ipdb; ipdb.set_trace()
    for measurement in measurements:
        if measurement > past:
            total += 1
        past = measurement

    return total


if __name__ == "__main__":
    with open("inputs/sonar_sweep.txt") as input:
        measurements = [int(measurement) for measurement in input]

    print(f"Part One: {main(measurements)}")
