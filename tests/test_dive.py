from solutions.dive import Submarine


def test_sub_moves_forward():
    """Given a command to move forward, the sub changes horizontal
    position.
    """
    sub = Submarine()
    assert sub.engage("forward 5").horizontal_position == 5


def test_sub_moves_down():
    """Given a command to move down, the sub changes depth."""
    sub = Submarine()
    assert sub.engage("down 5").depth == 5


def test_sub_moves_up():
    """Given a command to move up, the sub changes depth."""
    sub = Submarine()
    assert sub.engage("up 5").depth == -5
