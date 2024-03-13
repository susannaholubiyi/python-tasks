import unittest

from tictactoegame.tictactoe import TicTacToe
from tictactoegame.valueofcell import ValueOfCell


class TicTacToeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tictactoe = TicTacToe()

    def test_that_game_board_is_empty(self):
        expected = [[ValueOfCell.EMPTY, ValueOfCell.EMPTY, ValueOfCell.EMPTY],
                    [ValueOfCell.EMPTY, ValueOfCell.EMPTY, ValueOfCell.EMPTY],
                    [ValueOfCell.EMPTY, ValueOfCell.EMPTY, ValueOfCell.EMPTY]]
        self.assertEquals(expected, self.tictactoe.get_board())

    def test_that_there_are_two_players(self):
        number_of_players = self.tictactoe.get_number_of_players()
        self.assertEquals(2, number_of_players)

    def test_that_when_player_one_makes_a_move_X_is_played(self):
        player_one = self.tictactoe.players[0]
        player_one.play(self.tictactoe, 1)
        self.assertEquals(ValueOfCell.X, self.tictactoe.get_board()[0][0])

