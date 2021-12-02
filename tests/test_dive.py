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


def test_sub_follows_path_to_final_position_value():
    """Sub can follow a path and calculate its final position's value."""
    sub = Submarine()
    commands = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    for command in commands:
        sub.engage(command)

    assert sub.horizontal_position == 15
    assert sub.depth == 10
    assert sub.final_value == 150
