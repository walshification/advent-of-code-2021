from solutions.lanternfish import Ocean


def test_ocean_measures_population_after_eighty_days():
    """Test the test input."""
    fish_count = Ocean.live([3, 4, 3, 1, 2])
    assert fish_count == 5934
