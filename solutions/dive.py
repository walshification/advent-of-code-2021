"""
Part One
========

Calculate the horizontal position and depth you would have after
following the planned course. What do you get if you multiply your
final horizontal position by your final depth?

Part Two
========

In addition to horizontal position and depth, you'll also need to track
a third value, aim, which also starts at 0. The commands also mean
something entirely different than you first thought:

* down X increases your aim by X units.
* up X decreases your aim by X units.
* forward X does two things:
  * It increases your horizontal position by X units.
  * It increases your depth by your aim multiplied by X.
"""
from dataclasses import dataclass
from typing import Callable, Dict


# Commands


def down(submarine: "Submarine", change: int) -> None:
    """Add the change to the sub's depth."""
    submarine.depth += change


def forward(submarine: "Submarine", change: int) -> None:
    """Add the change to the sub's horizontal position."""
    submarine.horizontal_position += change


def up(submarine: "Submarine", change: int) -> None:
    """Subtract the change from the sub's depth."""
    submarine.depth -= change


def aim_down(submarine: "Submarine", change: int) -> None:
    """Add the change to the sub's aim."""
    submarine.aim += change


def aim_up(submarine: "Submarine", change: int) -> None:
    """Subtract the change to the sub's aim."""
    submarine.aim -= change


def move_forward(submarine: "Submarine", change: int) -> None:
    """Move based on the aim."""
    submarine.horizontal_position += change
    submarine.depth += submarine.aim * change


MOVES = {
    "down": down,
    "forward": forward,
    "up": up,
}

PART_TWO_MOVES = {
    "down": aim_down,
    "forward": move_forward,
    "up": aim_up,
}


@dataclass
class Submarine:
    """Our transport. Tracks depth and horizontal position."""

    aim = 0
    depth: int = 0
    horizontal_position: int = 0

    @property
    def final_value(self) -> int:
        """Multiply the sub's horizontal position by its depth."""
        return self.depth * self.horizontal_position

    def engage(self, command: str, moves: Dict[str, Callable] = MOVES) -> "Submarine":
        """Given a command, make it so, Number One."""
        move, value = command.split(" ")
        try:
            moves[move](self, int(value))
        except KeyError:
            raise Exception(f"Unknown command '{move}'")
        else:
            return self


if __name__ == "__main__":
    with open("inputs/dive.txt") as input:
        commands = [command for command in input]

    sub = Submarine()
    for command in commands:
        sub.engage(command)

    print(f"Part One: {sub.final_value}")

    sub = Submarine()
    for command in commands:
        sub.engage(command, PART_TWO_MOVES)

    print(f"Part Two: {sub.final_value}")
