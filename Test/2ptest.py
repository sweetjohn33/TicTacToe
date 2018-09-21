from GameOperations.game import GameBoard, GameLoop
from Agent.minimaxplayer import MinMaxPlayer
from GameOperations.player import Player
import numpy as np

if __name__ == "__main__":
    board = GameBoard(3)
    board.board = np.array([["x", "x", "o"], ["o", "o", "x"], ["", "", "x"]])
    #board.board = np.array([["x", "", ""],["o", "o", "x"],["", "", "x"]])

    x = Player("x")
    o = Player("o")
    game = GameLoop(o, x, board)
    game.play()
