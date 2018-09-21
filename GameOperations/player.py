import numpy as np

class Player:

    def __init__(self, shape):
        self.shape = shape

    def move(self, board):
        user_move = tuple(int(x.strip()) for x in input().split(','))
        while self.invalid(user_move, board):
            user_move = tuple(int(x.strip()) for x in input().split(','))
        board[user_move] = self.shape

    def invalid(self, move, board):
        try:
            square = board[move]
        except IndexError:
            return True
        if square != '':
            return True
        else:
            return False