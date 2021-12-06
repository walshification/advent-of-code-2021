"""
Part One
========

Find a way to simulate lanternfish. How many lanternfish would there be
after 80 days?
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Lanternfish:
    """A fishie that spaws once a week."""

    timer: int = 8

    def __repr__(self) -> str:
        """Return str info."""
        return str(self.timer)

    def live(self) -> None:
        """Live for a day."""
        self.timer -= 1

    def reset(self) -> None:
        """Restart the timer."""
        self.timer = 6


class Ocean:
    """A place for fishies."""

    def __init__(self, fish_ages: List[int]) -> None:
        """Create pre-existing fishies."""
        self.fishies = [Lanternfish(age) for age in fish_ages]

    def live_for_eighty_days(self, day_count: int = 80) -> int:
        """Manage fish populations for 80 days. Returns fish count."""
        for _ in range(1, day_count + 1):
            new_fish = []
            for fish in self.fishies:
                if fish.timer == 0:
                    fish.reset()
                    new_fish.append(Lanternfish())
                else:
                    fish.live()
            self.fishies += new_fish

        return len(self.fishies)


if __name__ == "__main__":
    with open("inputs/lanternfish.txt") as raw_ages:
        fish_ages = [int(age) for age in raw_ages.read().split(",")]

    ocean = Ocean(fish_ages)
    fish_count = ocean.live_for_eighty_days()
    print(f"Part One: {fish_count}")
