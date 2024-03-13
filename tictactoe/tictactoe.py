from tictactoegame.exception import FilledPositionError
from tictactoegame.player import Player
from tictactoegame.valueofcell import ValueOfCell


class TicTacToe:
    def __init__(self):
        self.board = [[ValueOfCell.EMPTY for _ in range(3)] for _ in range(3)]
        self.player_one = Player(1, ValueOfCell.X)
        self.player_two = Player(1, ValueOfCell.O)
        self.players = [self.player_one, self.player_two]

    def get_board(self):
        return self.board

    def get_number_of_players(self):
        return len(self.players)

    def mark_board(self, player_id, position):
        self.validate_position(position)
        row = self.convert_to_row_from(position)
        column = self.convert_to_column_from(position)

        cell = ValueOfCell.X if player_id == 1 else ValueOfCell.O
        if self.board[row][column] == ValueOfCell.EMPTY:
            self.board[row][column] = cell
        raise FilledPositionError("Position has already been played")

    @staticmethod
    def convert_to_row_from(position):
        return (position - 1) // 3

    @staticmethod
    def convert_to_column_from(position):
        return (position - 1) % 3

    @staticmethod
    def validate_position(position):
        if position < 0 or position > 9:
            raise IndexError("Position is invalid")
