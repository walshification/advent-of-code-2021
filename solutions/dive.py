"""
Part One
========

Calculate the horizontal position and depth you would have after
following the planned course. What do you get if you multiply your
final horizontal position by your final depth?
"""
from dataclasses import dataclass


@dataclass
class Submarine:
    """Our transport. Tracks depth and horizontal position."""

    depth: int = 0
    horizontal_position: int = 0

    @property
    def final_value(self) -> int:
        """Multiply the sub's horizontal position by its depth."""
        return self.depth * self.horizontal_position

    def engage(self, command: str) -> "Submarine":
        """Given a command, make it so, Number One."""
        move, value = command.split(" ")
        try:
            MOVES[move](self, int(value))
        except KeyError:
            raise Exception(f"Unknown command '{move}'")
        else:
            return self


# Commands


def down(submarine: Submarine, change: int) -> None:
    """Add the change to the sub's depth."""
    submarine.depth += change


def forward(submarine: Submarine, change: int) -> None:
    """Add the change to the sub's horizontal position."""
    submarine.horizontal_position += change


def up(submarine: Submarine, change: int) -> None:
    """Subtract the change from the sub's depth."""
    submarine.depth -= change


MOVES = {
    "down": down,
    "forward": forward,
    "up": up,
}


if __name__ == "__main__":
    with open("inputs/dive.txt") as input:
        commands = [command for command in input]

    sub = Submarine()
    for command in commands:
        sub.engage(command)

    print(f"Part One: {sub.final_value}")
