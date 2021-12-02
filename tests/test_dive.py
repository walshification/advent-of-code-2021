from solutions.dive import Submarine


def test_sub_moves_forward():
    """Given a command to move forward, the sub changes horizontal
    position.
    """
    sub = Submarine()
    assert sub.engage("forward 5").horizontal_position == 5
