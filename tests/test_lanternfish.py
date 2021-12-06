from solutions.lanternfish import Lanternfish, Ocean


def test_initial_fish():
    """Initial fish can get a set age and live."""
    fish = Lanternfish(2)
    assert fish.timer == 2

    fish.live()
    assert fish.timer == 1

    fish.live()
    assert fish.timer == 0


def test_ocean_measures_population_after_eighty_days():
    """Test the test input."""
    fish_count = Ocean.live([3, 4, 3, 1, 2])
    assert fish_count == 5934
