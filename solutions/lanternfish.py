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

    @staticmethod
    def live(fish_ages: List[int], day_count: int = 80) -> int:
        """Manage fish populations for a given number of days. Returns
        fish count.
        """
        fishies = [Lanternfish(age) for age in fish_ages]
        for _ in range(1, day_count + 1):
            new_fish = []
            for fish in fishies:
                if fish.timer == 0:
                    fish.reset()
                    new_fish.append(Lanternfish())
                else:
                    fish.live()
            fishies += new_fish

        return len(fishies)


if __name__ == "__main__":
    with open("inputs/lanternfish.txt") as raw_ages:
        fish_ages = [int(age) for age in raw_ages.read().split(",")]

    print(f"Part One: {Ocean.live(fish_ages)}")
    print(f"Part Two: {Ocean.live(fish_ages, 256)}")
