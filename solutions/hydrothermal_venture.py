"""
Part One
========

Determine the number of points where at least two lines overlap. In the
above example, this is anywhere in the diagram with a 2 or larger - a
total of 5 points.

Consider only horizontal and vertical lines. At how many points do at
least two lines overlap?
"""
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(eq=True)
class Point:
    """x and y coordinates for a point on a grid."""

    x: int
    y: int

    def __repr__(self) -> str:
        """Point as a string."""
        return f"({self.x}, {self.y})"


@dataclass
class Line:
    """Grid representation of a line from two points."""

    start: Point
    end: Point
    points: List[Point] = field(default_factory=list)
    _delta_x: Optional[int] = None
    _delta_y: Optional[int] = None

    def __post_init__(self) -> None:
        """Draw the points of the line given a start and end."""
        self.draw()

    @classmethod
    def from_string(cls, string: str) -> "Line":
        """Given a string of the format "x1,y1 -> x2,y2", construct a
        line.
        """
        raw_start, raw_end = string.split(" -> ")
        start_x, start_y = raw_start.split(",")
        start = Point(int(start_x), int(start_y))

        end_x, end_y = raw_end.split(",")
        end = Point(int(end_x), int(end_y))

        return cls(start, end)

    @property
    def delta_x(self) -> int:
        """The change in x from start to end."""
        if self._delta_x is None:
            self._delta_x = self.end.x - self.start.x
        return self._delta_x

    @property
    def delta_y(self) -> int:
        """The change in y from start to end."""
        if self._delta_y is None:
            self._delta_y = self.end.y - self.start.y
        return self._delta_y

    @property
    def is_horizontal(self) -> bool:
        """Returns whether a line is horizontal or not."""
        return self.delta_y == 0

    @property
    def is_vertical(self) -> bool:
        """Returns whether a line is vertical or not."""
        return self.delta_x == 0

    def draw(self) -> None:
        """Deduce the points of the line given its start and end."""
        current_point = self.start
        self.points.append(current_point)
        while current_point != self.end:
            new_x = current_point.x
            if self.delta_x > 0:
                new_x += 1
            elif self.delta_x < 0:
                new_x -= 1

            new_y = current_point.y
            if self.delta_y > 0:
                new_y += 1
            elif self.delta_y < 0:
                new_y -= 1

            current_point = Point(new_x, new_y)
            self.points.append(current_point)


@dataclass
class Grid:
    """Grid on which to map the lines."""

    @staticmethod
    def map(lines: List[Line]) -> int:
        """Draw the lines on the grid and count how many times a point
        is drawn over.
        """
        point_counter = defaultdict(int)
        for line in lines:
            for point in line.points:
                point_counter[str(point)] += 1

        return sum(1 for count in point_counter.values() if count > 1)

    @staticmethod
    def map_horizontal_and_vertical(lines: List[Line]) -> int:
        """Draw the lines on the grid and count how many times a point
        is drawn over but only for horizontal and vertical lines.
        """
        point_counter = defaultdict(int)
        for line in lines:
            if line.is_vertical or line.is_horizontal:
                for point in line.points:
                    point_counter[str(point)] += 1

        return sum(1 for count in point_counter.values() if count > 1)


if __name__ == "__main__":
    with open("inputs/hydrothermal_venture.txt") as input:
        lines = [Line.from_string(raw_line) for raw_line in input]

    print(f"Part One: {Grid.map_horizontal_and_vertical(lines)}")
    print(f"Part Two: {Grid.map(lines)}")
