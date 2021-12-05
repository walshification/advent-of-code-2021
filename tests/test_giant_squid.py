from solutions.giant_squid import Board, Square


def test_board_can_build_itself():
    """A board knows how to construct its grid from a list of numbers."""
    test_board = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    board = Board(test_board)
    assert board.state == {
        0: [Square(1), Square(2), Square(3), Square(4), Square(5)],
        1: [Square(6), Square(7), Square(8), Square(9), Square(10)],
        2: [Square(11), Square(12), Square(13), Square(14), Square(15)],
        3: [Square(16), Square(17), Square(18), Square(19), Square(20)],
        4: [Square(21), Square(22), Square(23), Square(24), Square(25)],
    }


def test_board_knows_horizontal_wins():
    """A board can identify horizontal wins."""
    test_board = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    board = Board(test_board)
    for square in board.state[0]:
        square.marked = True

    assert board.has_bingo


def test_board_knows_horizontal_wins():
    """A board can identify horizontal wins."""
    test_board = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    board = Board(test_board)
    for row in board.state.values():
        row[0].marked = True

    assert board.has_bingo
