class Player:
    def __init__(self, i_d, cell_type):
        self.id = i_d
        self.cell_type = cell_type

    def play(self, tic_tac_toe, position):
        tic_tac_toe.mark_board(self.id, position)
