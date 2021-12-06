from solutions.lanternfish import Lanternfish


def test_initial_fish():
    """Initial fish can get a set age and reset properly."""
    fish = Lanternfish(2)
    assert fish.timer == 2

    fish.live()
    assert fish.timer == 1

    fish.live()
    assert fish.timer == 0

    fish.live()
    assert fish.timer == 6
