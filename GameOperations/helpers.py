import numpy as np
import copy

def game_over(board):
    for row in board:
        if np.unique(row).size == 1 and '' not in row:
            return True, 'victory'
    for col_num in range(board.shape[1]):
        col = board[:, col_num]
        if np.unique(col).size == 1 and '' not in col:
            return True, 'victory'
    for diagonal in diagonals(board):
        if np.unique(diagonal).size == 1 and '' not in diagonal:
            return True, 'victory'
    if '' not in board:
        return True, 'tie'
    return False, ''

def open_squares(board):
    board_length = board.shape[0]
    open_squares = []
    for row_num in range(board_length):
        for col_num in range(board_length):
            if board[row_num][col_num] == '':
                open_squares.append((row_num, col_num))
    return open_squares

def child(node, square, shape):
    child = copy.copy(node)
    child[square] = shape
    return child

def children(node, shape):
    children = []
    for square in open_squares(node):
        child = copy.copy(node)
        child[square] = shape
        children.append(child)
    return children

def check_winning_lst(lst, winning_shape):
    winner = True
    for shape in lst:
        if shape != winning_shape:
            winner = False
            break
    if winner:
        return True
    else:
        return False

def diagonals(board):
    diagonal1 = np.zeros(board.shape[0], dtype=str)
    diagonal2 = np.zeros(board.shape[0], dtype=str)
    diagonals = [diagonal1, diagonal2]
    for i in range(board.shape[0]):
        diagonals[0][i] = board[i][i]
        diagonals[1][i] = board[i][board.shape[0] - i - 1]
    return diagonals