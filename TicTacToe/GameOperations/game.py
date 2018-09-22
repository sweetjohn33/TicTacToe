import numpy as np
import sys
from GameOperations.helpers import *

class GameBoard:

    def __init__(self, board_size):
        self.board = np.zeros((board_size, board_size), dtype=str)
        self.board_size = board_size

    def display(self):
        print(self.board)
        print("\n")


class GameLoop:

    def __init__(self, x_player, o_player, game_board):
        self.active_player = x_player
        self.inactive_player = o_player
        self.game_board = game_board

    def play(self):
        while not game_over(self.game_board.board)[0]:
            self.game_board.display()
            print("{}'s move: ".format(self.active_player.shape))
            self.active_player.move(self.game_board.board)
            temp = self.active_player
            self.active_player = self.inactive_player
            self.inactive_player = temp
        self.print_end_game()

    def print_end_game(self):
        print(self.game_board.board)
        if game_over(self.game_board.board)[1] == "tie":
            print("TicTacToe over, it's a tie!")
        else:
            print("game over, {}'s won.".format(self.inactive_player.shape))
