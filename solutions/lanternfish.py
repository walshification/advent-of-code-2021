"""
Part One
========

Find a way to simulate lanternfish. How many lanternfish would there be
after 80 days?
"""
from dataclasses import dataclass


@dataclass
class Lanternfish:
    """A fishie that spaws once a week."""

    timer: int = 8

    def live(self) -> None:
        """Live for a day."""
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
