from solutions.hydrothermal_venture import Grid, Line, Point


def test_lines_from_strings():
    """Given a string of a certain format, lines can be made."""
    line = Line.from_string("0,9 -> 3,9")
    assert line.points == [Point(0, 9), Point(1, 9), Point(2, 9), Point(3, 9)]


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


def test_the_test_input():
    """Test the test input."""
    raw_input = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]

    lines = [Line.from_string(raw_line) for raw_line in raw_input]

    assert Grid.map_horizontal_and_vertical(lines) == 5


def test_the_full_test_input():
    """Test the full test input."""
    raw_input = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]

    lines = [Line.from_string(raw_line) for raw_line in raw_input]

    assert Grid.map(lines) == 12
