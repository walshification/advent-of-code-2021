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

Part Two
========

Next, you should verify the life support rating, which can be
determined by multiplying the oxygen generator rating by the CO2
scrubber rating.
"""
from collections import Counter
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


class BinaryCounter(Counter):
    """Subclass of Counter for specific most common functionality."""

    def most_common(
        self, do_honor_ties: bool = False, winner: str = "1"
    ) -> Optional[Tuple[str, int]]:
        """If there is a definitive most_common, return that. Return
        "1" for ties.
        """
        most_common = super().most_common()
        if len(most_common) < 2:
            return most_common

        if do_honor_ties:
            if most_common[0][1] == most_common[1][1]:
                return winner
        return most_common


def binary_to_int(binary_number: str) -> int:
    """Convert a given binary number to an int."""
    # This feels like cheating.
    # return int(binary_number, 2)
    return sum(
        int(digit) * (2 ** power) for power, digit in enumerate(binary_number[::-1])
    )


@dataclass
class DiagnosticReport:
    """Tracks gamma rate, epsilon rate, and calculates power
    consumption.
    """

    binary_numbers: List[str]
    binary_length: int = 0
    binary_gamma: str = ""
    binary_epsilon: str = ""
    binary_oxygen_scrubber_rating: str = ""
    binary_co2_scrubber_rating: str = ""
    gamma_rate: int = 0
    epsilon_rate: int = 0
    oxygen_generator_rating: int = 0
    co2_scrubber_rating: int = 0
    counters: List[BinaryCounter] = field(default_factory=list)

    def __post_init__(self):
        """Process the binary numbers through the counters and assign
        gamma and epsilon rates.
        """
        # Give us a counter for each digit placeholder, depending on the number length.
        self.binary_length = len(self.binary_numbers[0])

        for _ in range(self.binary_length):
            self.counters.append(BinaryCounter())

        for number in self.binary_numbers:
            for idx, digit in enumerate(number):
                self.counters[idx].update(digit)

        for counter in self.counters:
            # Concatenate most common digits
            self.binary_gamma += counter.most_common()[0][0]
            # Concatenate least common digits
            self.binary_epsilon += counter.most_common()[:-13:-1][0][0]

        self.gamma_rate = binary_to_int(self.binary_gamma)
        self.epsilon_rate = binary_to_int(self.binary_epsilon)
        self.binary_oxygen_generator_rating = self.calculate_oxygen_generator_rating(
            self.binary_numbers
        )
        self.binary_co2_scrubber_rating = self.calculate_co2_scrubber_rating(
            self.binary_numbers
        )
        self.oxygen_generator_rating = binary_to_int(
            self.binary_oxygen_generator_rating
        )
        self.co2_scrubber_rating = binary_to_int(self.binary_co2_scrubber_rating)

    @property
    def power_consumption(self) -> int:
        """Calculates power consumption based on gamma and epsilon
        rates.
        """
        return self.gamma_rate * self.epsilon_rate

    @property
    def life_support_rating(self) -> int:
        """Calculate life support rating based on oxygen generator and
        CO2 scrubber ratings.
        """
        return self.oxygen_generator_rating * self.co2_scrubber_rating

    def calculate_oxygen_generator_rating(self, filtered: List[str]) -> int:
        """Filter numbers till most common concatenation is left."""
        for idx in range(self.binary_length):
            # Filter based on most common in the filtered list.
            counter = BinaryCounter([number[idx] for number in filtered])
            key = counter.most_common(do_honor_ties=True)[0][0]
            filtered = list(filter(lambda x: x[idx] == key, filtered))
            # If we have one number, we don't need to filter any more.
            if len(filtered) == 1:
                break

        return filtered[0]

    def calculate_co2_scrubber_rating(self, filtered: List[str]) -> int:
        """Filter numbers till least common concatenation is left."""
        for idx in range(self.binary_length):
            # Filter based on least common in the filtered list.
            counter = BinaryCounter([number[idx] for number in filtered])
            key = counter.most_common(do_honor_ties=True, winner="0")[:-13:-1][0][0]
            filtered = list(filter(lambda x: x[idx] == key, filtered))
            # If we have one number, we don't need to filter any more.
            if len(filtered) == 1:
                break

        return filtered[0]


if __name__ == "__main__":
    with open("inputs/binary_diagnostic.txt") as input:
        binary_numbers = input.read().splitlines()

    report = DiagnosticReport(binary_numbers)
    print(f"Part One: {report.power_consumption}")
    print(f"Part Two: {report.life_support_rating}")
