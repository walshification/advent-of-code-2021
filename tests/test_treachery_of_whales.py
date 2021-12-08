from solutions.treachery_of_whales import CrabFleet


def test_crab_fleet_finds_median():
    """The crab fleet can find its median position of subs."""
    assert CrabFleet([0, 1, 1, 1, 5]).median == 1
