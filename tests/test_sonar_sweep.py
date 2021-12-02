from solutions.sonar_sweep import count_increases, count_windows


def test_increments_increases():
    """If the depth increases, increment."""
    result = count_increases([199, 200])
    assert result == 1


def test_skips_decreases():
    """If the depth decreases, skip."""
    assert count_increases([200, 199]) == 0


def test_sample():
    """Test the sample input."""
    assert count_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7


def test_part_two():
    """Test part two with the sample input."""
    assert count_windows([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5
