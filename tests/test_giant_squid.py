import pytest

from solutions.giant_squid import Board, Game, Square


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


def test_game_advances(board):
    """A game advances and marks squares."""
    game = Game([board])
    game.advance(4)
    assert not game.boards[0].state[0][2].marked
    assert game.boards[0].state[0][3].marked
    assert not game.boards[0].state[0][4].marked


def test_game_advances_until_a_bingo(board):
    """A game advances and marks squares."""
    game = Game([board])
    turns = [1, 2, 3, 4, 5]
    final_score = game.play(turns)

    assert final_score == (sum(TEST_SQUARE_VALUES) - sum(turns)) * 5


def test_correctly_plays_test_game():
    """Correctly plays."""
    turns = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]

    boards = [
        Board(
            [
                22,
                13,
                17,
                11,
                0,
                8,
                2,
                23,
                4,
                24,
                21,
                9,
                14,
                16,
                7,
                6,
                10,
                3,
                18,
                5,
                1,
                12,
                20,
                15,
                19,
            ]
        ),
        Board(
            [
                3,
                15,
                0,
                2,
                22,
                9,
                18,
                13,
                17,
                5,
                19,
                8,
                7,
                25,
                23,
                20,
                11,
                10,
                24,
                4,
                14,
                21,
                16,
                12,
                6,
            ]
        ),
        Board(
            [
                14,
                21,
                17,
                24,
                4,
                10,
                16,
                15,
                9,
                19,
                18,
                8,
                23,
                26,
                20,
                22,
                11,
                13,
                6,
                5,
                2,
                0,
                12,
                3,
                7,
            ]
        ),
    ]

    game = Game(boards)

    assert game.play(turns) == 4512
