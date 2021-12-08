from solutions.treachery_of_whales import CrabFleet


def test_crab_fleet_finds_median():
    """The crab fleet can find its median position of subs."""
    assert CrabFleet([0, 1, 1, 1, 5]).median == 1


def test_crab_fleet_calculates_fuel():
    """The crab fleet can find how much fuel it needs to get into
    position.
    """
    fleet = CrabFleet([0, 1, 1, 1, 5])
    assert fleet.calculate_minimum_fuel(fleet.median) == 5


def test_part_one_input():
    """Test the part one input."""
    fleet = CrabFleet([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    assert fleet.calculate_minimum_fuel(fleet.median) == 37
