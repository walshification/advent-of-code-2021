from solutions.sonar_sweep import main


def test_increments_increases():
    """If the depth increases, increment."""
    result = main([199, 200])
    assert result == 1


def test_skips_decreases():
    """If the depth decreases, skip."""
    assert main([200, 199]) == 0


def test_sample():
    """Test the sample input."""
    assert main([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7
