"""
Part One
========

You need to use the binary numbers in the diagnostic report to generate
two new binary numbers (called the gamma rate and the epsilon rate).
The power consumption can then be found by multiplying the gamma rate
by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common
bit in the corresponding position of all numbers in the diagnostic
report.

The epsilon rate is calculated by the least common bit from each
position is used.

Multiplying the gamma rate by the epsilon rate produces the power
consumption.
"""
from collections import Counter
from dataclasses import dataclass, field
from typing import List


def binary_to_int(binary_number: str) -> int:
    """Convert a given binary number to an int."""
    # This feels like cheating.
    # return int(binary_number, 2)
    return sum(
        int(digit) * (2**power) for power, digit in enumerate(binary_number[::-1])
    )


@dataclass
class DiagnosticReport:
    """Tracks gamma rate, epsilon rate, and calculates power
    consumption.
    """

    binary_numbers: List[str]
    binary_gamma: str = ""
    binary_epsilon: str = ""
    gamma_rate: int = 0
    epsilon_rate: int = 0
    counters: List[Counter] = field(default_factory=list)

    def __post_init__(self):
        """Process the binary numbers through the counters and assign
        gamma and epsilon rates.
        """
        # Give us a counter for each digit placeholder, depending on the number length.
        for _ in range(len(self.binary_numbers[0])):
            self.counters.append(Counter())

        for number in self.binary_numbers:
            for idx, digit in enumerate(number):
                self.counters[idx].update(digit)

        for counter in self.counters:
            # Concatenate most common digits
            self.binary_gamma += counter.most_common()[0][0]
            # Concatenate least common digits
            self.binary_epsilon += counter.most_common()[:-13:-1][0][0]

    @property
    def power_consumption(self) -> int:
        """Calculates power consumption based on gamma and epsilon
        rates.
        """
        pass
