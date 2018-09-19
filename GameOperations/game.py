import numpy as np
from GameOperations.player import Player


class GameBoard:

    def __init__(self, board_size):
        self.board = np.zeros((board_size, board_size), dtype=str)
        self.board_size = board_size

    def diagonals(self):
        diagonal = np.zeros(self.board_size, dtype=str)
        diagonals = [diagonal, diagonal]
        for i in range(self.board_size):
            diagonals[0][i] = self.board[i][i]
            diagonals[1][i] = self.board[i][self.board_size - i - 1]
        return diagonals

    def display(self):
        print(self.board)


class GameLoop:

    def __init__(self, x_player, o_player, game_board):
        self.active_player = x_player
        self.inactive_player = o_player
        self.game_board = game_board

    def play(self):
        while not self.game_over():
            self.game_board.display()
            self.active_player.move(self.game_board)
            temp = self.active_player
            self.active_player = self.inactive_player
            self.inactive_player = temp
        self.print_end_game()

    def game_over(self):
        for row in self.game_board.board:
            if self.active_player.shape not in row and '' not in row:
                return True
        for col_num in range(self.game_board.board.shape[1]):
            col = self.game_board.board[:,col_num]
            if self.active_player.shape not in col and '' not in col:
                return True
        for diagonal in self.game_board.diagonals():
            if self.active_player.shape not in diagonal and '' not in diagonal:
                return True
        return False

    def print_end_game(self):
        print(self.game_board.board)
        print("game over")


if __name__ == "__main__":
    board = GameBoard(3)
    x = Player("x")
    o = Player("o")
    game = GameLoop(x, o, board)
    game.play()
