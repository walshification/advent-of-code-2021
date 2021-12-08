"""
Determine the horizontal position that the crabs can align to using the
least fuel possible. How much fuel must they spend to align to that
position?
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CrabFleet:
    """A collection of righteous crabs to protect you."""

    crab_positions: List[int]
    _median: Optional[int] = None

    @property
    def median(self) -> int:
        """Returns the median of the crab positions."""
        if self._median is None:
            total = len(self.crab_positions)
            self._median = sorted(self.crab_positions)[total // 2]
        return self._median

    def calculate_minimum_fuel(self, position: int) -> int:
        """Calculate the minimum-needed fuel to align to the median."""
        total_fuel = 0
        for position in self.crab_positions:
            while not position == self.median:
                if position > self.median:
                    position -= 1
                else:
                    position += 1
                total_fuel += 1

        return total_fuel


if __name__ == "__main__":
    with open("inputs/treachery_of_whales.txt") as input:
        positions = [int(position) for position in input.read().split(",")]

    fleet = CrabFleet(positions)
    print(f"Part One: {fleet.calculate_minimum_fuel(fleet.median)}")
