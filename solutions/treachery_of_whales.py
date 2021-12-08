"""
Determine the horizontal position that the crabs can align to using the
least fuel possible. How much fuel must they spend to align to that
position?
"""
from dataclasses import dataclass
from typing import Callable, List, Optional


def constant_burn(units: int) -> int:
    """Return the total fuel burned to move the given number of
    units.
    """
    return units


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

    def calculate_minimum_fuel(
        self, destination: int, burn_rate: Callable = constant_burn
    ) -> int:
        """Calculate the minimum-needed fuel to align to the median."""
        return sum(
            burn_rate(abs(destination - position)) for position in self.crab_positions
        )


if __name__ == "__main__":
    with open("inputs/treachery_of_whales.txt") as input:
        positions = [int(position) for position in input.read().split(",")]

    fleet = CrabFleet(positions)
    print(f"Part One: {fleet.calculate_minimum_fuel(fleet.median)}")
