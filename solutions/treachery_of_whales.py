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


def gauss_burn(units: int) -> int:
    """Return the total fuel burned in at a cumulative rate."""
    return sum(unit for unit in range(1, units + 1))


@dataclass
class CrabFleet:
    """A collection of righteous crabs to protect you."""

    crab_positions: List[int]
    _median: Optional[int] = None
    _mean: Optional[int] = None

    @property
    def mean(self) -> int:
        """Returns the mean of the crab positions."""
        if self._mean is None:
            self._mean = sum(self.crab_positions) // len(self.crab_positions)
        return self._mean

    @property
    def median(self) -> int:
        """Returns the median of the crab positions."""
        if self._median is None:
            total = len(self.crab_positions)
            self._median = sorted(self.crab_positions)[total // 2]
        return self._median

    def calculate_minimum_fuel(
        self, destination: Optional[int] = None, burn_rate: Callable = constant_burn
    ) -> int:
        """Calculate the minimum-needed fuel to align to the median."""
        if destination is None:
            # Find the minimum
            return min(
                sum(
                    [
                        burn_rate(abs(goal - position))
                        for position in self.crab_positions
                    ]
                )
                # Consider the positions bound by half the length of the collection,
                # +/- the average position.
                for goal in range(
                    (self.mean - (len(self.crab_positions) // 2)),
                    (self.mean + (len(self.crab_positions) // 2) + 1),
                )
            )
        return sum(
            burn_rate(abs(destination - position)) for position in self.crab_positions
        )


if __name__ == "__main__":
    with open("inputs/treachery_of_whales.txt") as input:
        positions = [int(position) for position in input.read().split(",")]

    fleet = CrabFleet(positions)
    print(f"Part One: {fleet.calculate_minimum_fuel(fleet.median)}")
