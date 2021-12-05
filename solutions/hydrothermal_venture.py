"""
Part One
========

Determine the number of points where at least two lines overlap. In the
above example, this is anywhere in the diagram with a 2 or larger - a
total of 5 points.

Consider only horizontal and vertical lines. At how many points do at
least two lines overlap?
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(eq=True)
class Point:
    """x and y coordinates for a point on a grid."""

    x: int
    y: int


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
