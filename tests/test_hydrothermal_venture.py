from solutions.hydrothermal_venture import Grid, Line, Point


def test_line_can_draw_horizontally_with_points():
    """Given a start and an end, a line can draw the intermediary
    points.
    """
    start = Point(0, 0)
    end = Point(2, 0)
    line = Line(start, end)
    assert line.points == [start, Point(1, 0), end]


def test_line_can_draw_backwards():
    """Given a start and an end that goes left, the line can still draw
    itself.
    """
    start = Point(2, 0)
    end = Point(0, 0)
    line = Line(start, end)
    assert line.points == [start, Point(1, 0), end]


def test_line_can_draw_vertically_with_points():
    """Given a start and an end, a line can draw the intermediary
    points.
    """
    start = Point(0, 0)
    end = Point(0, 2)
    line = Line(start, end)
    assert line.points == [start, Point(0, 1), end]


def test_line_can_draw_backwards_vertically():
    """Given a start and an end that goes left, the line can still draw
    itself.
    """
    start = Point(0, 2)
    end = Point(0, 0)
    line = Line(start, end)
    assert line.points == [start, Point(0, 1), end]


def test_grid_tracks_double_points():
    """Grid returns the number of points marked twice."""
    lines = [Line(Point(0, 0), Point(2, 0)), Line(Point(0, 2), Point(0, 0))]
    double_count = Grid.map(lines)
    assert double_count == 1
