"""
Part One
========

Find a way to simulate lanternfish. How many lanternfish would there be
after 80 days?

Part Two
========
How many lanternfish would there be after 256 days?
"""
from collections import Counter
from typing import List


class Ocean:
    """A place for fishies."""

    @staticmethod
    def live(fish_ages: List[int], day_count: int = 80) -> int:
        """Manage fish populations for a given number of days. Returns
        fish count.
        """
        # Create some fish buckets
        fishies = Counter(fish_ages)
        for _ in range(1, day_count + 1):
            # Fishies at 0 make babies
            babies = fishies[0]
            for bucket in range(8):
                # Shift the aging fish to their new age bucket.
                fishies[bucket] = fishies[bucket + 1]

            # Add the babies to the babies bucket.
            fishies[8] = babies
            # Add the reset fish (same as babies) to the reset bucket.
            fishies[6] += babies

        return sum(fishies.values())


if __name__ == "__main__":
    with open("inputs/lanternfish.txt") as raw_ages:
        fish_ages = [int(age) for age in raw_ages.read().split(",")]

    print(f"Part One: {Ocean.live(fish_ages)}")
    print(f"Part Two: {Ocean.live(fish_ages, 256)}")
