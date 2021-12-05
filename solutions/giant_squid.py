"""
Part One
========

To guarantee victory against the giant squid, figure out which board
will win first. What will your final score be if you choose that board?
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Square:
    """Representation of a single square on a Bingo board."""

    value: int
    marked: bool = False


class Board:
    """Representation of a Bingo board."""

    def __init__(self, numbers: List[int]) -> None:
        """Parse the numbers into a 5x5 Bingo board."""
        self.state = {
            0: [Square(number) for number in numbers[:5]],
            1: [Square(number) for number in numbers[5:10]],
            2: [Square(number) for number in numbers[10:15]],
            3: [Square(number) for number in numbers[15:20]],
            4: [Square(number) for number in numbers[20:]],
        }

    @property
    def has_bingo(self) -> bool:
        """Returns whether or not the board has a bingo."""
        return self.has_horizontal_bingo or self.has_vertical_bingo

    @property
    def has_horizontal_bingo(self) -> bool:
        """Returns if any of the board's rows' squares are all marked."""
        return any(all(square.marked for square in row) for row in self.state.values())

    @property
    def has_vertical_bingo(self) -> bool:
        """Returns whether any of the board's columns' squares are all
        marked.
        """
        return any(all(row[i].marked for row in self.state.values()) for i in range(5))

    def mark_square(self, number: int) -> None:
        """Check for a square of the numbered value and mark it if it
        exists.
        """
        for row in self.state.values():
            for square in row:
                if square.value == number:
                    square.marked = True

    def calculate_final_score(self, number: int) -> int:
        """Return the sum of the unmarked squares multiplied by the
        final value before the bingo.
        """
        return (
            sum(
                square.value
                for row in self.state.values()
                for square in row
                if not square.marked
            )
            * number
        )


@dataclass
class Game:
    """A game of Bingo played with supplied boards."""

    boards: List[Board]

    def advance(self, number: int) -> None:
        """Take a turn of a game."""
        for board in self.boards:
            board.mark_square(number)
            if board.has_bingo:
                return board.calculate_final_score(number)

    def play(self, turns: List[int]) -> int:
        """Advance turns until there is a winner or no more turns."""
        for turn in turns:
            if final_score := self.advance(turn):
                return final_score
