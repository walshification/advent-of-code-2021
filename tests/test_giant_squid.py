import pytest

from solutions.giant_squid import Board, Square


TEST_SQUARE_VALUES = [
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


@pytest.fixture
def board():
    return Board(TEST_SQUARE_VALUES)


def test_board_can_build_itself(board):
    """A board knows how to construct its grid from a list of numbers."""
    assert board.state == {
        0: [Square(1), Square(2), Square(3), Square(4), Square(5)],
        1: [Square(6), Square(7), Square(8), Square(9), Square(10)],
        2: [Square(11), Square(12), Square(13), Square(14), Square(15)],
        3: [Square(16), Square(17), Square(18), Square(19), Square(20)],
        4: [Square(21), Square(22), Square(23), Square(24), Square(25)],
    }


def test_board_knows_horizontal_wins(board):
    """A board can identify horizontal wins."""
    for square in board.state[0]:
        square.marked = True

    assert board.has_bingo


def test_board_knows_horizontal_wins(board):
    """A board can identify horizontal wins."""
    for row in board.state.values():
        row[0].marked = True

    assert board.has_bingo


def test_board_final_score(board):
    """Board can caluclate its final score."""
    assert board.calculate_final_score(10) == sum(TEST_SQUARE_VALUES) * 10


def test_board_final_score_ignores_marked_squares(board):
    """Board can caluclate its final score without marked squares."""
    board.state[4][-1].marked = True
    assert board.calculate_final_score(10) == (sum(TEST_SQUARE_VALUES) - 25) * 10
