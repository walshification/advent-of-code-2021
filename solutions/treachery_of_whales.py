"""
Determine the horizontal position that the crabs can align to using the
least fuel possible. How much fuel must they spend to align to that
position?
"""
from dataclasses import dataclass
from typing import List


@dataclass
class CrabFleet:
    """A collection of righteous crabs to protect you."""

    crab_positions: List[int]

    @property
    def median(self) -> int:
        """Returns the median of the crab positions."""
        total = len(self.crab_positions)
        return sorted(self.crab_positions)[total // 2]
