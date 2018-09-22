from GameOperations.game import GameBoard
from Agent.minimaxplayer import MinMaxPlayer
from GameOperations.game import GameLoop
from GameOperations.player import Player

if __name__ == "__main__":
    board = GameBoard(3)
    x = MinMaxPlayer("x", "o")
    #o = MinMaxPlayer("o", "x")
    o = Player("o")
    game = GameLoop(x, o, board)
    game.play()