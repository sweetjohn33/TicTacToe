from GameOperations.player import Player
from GameOperations.helpers import *
import time

def timeit(f):
    def helper(*args):
        start = time.time()
        result = f(*args)
        finish = time.time()
        print("It took {} seconds to move.".format(finish-start))
        return result
    return helper

def memoize(f):
    memo = {}
    def helper(x, *args):
        x_imm = tuple(map(tuple,x))
        if x_imm not in memo:
            memo[x_imm] = f(x, *args)
        return memo[x_imm]
    return helper

@memoize
def minimax(node, depth, maximizingPlayer, alpha, beta, current_shape, next_shape):
    # function minimax(node, depth, maximizingPlayer)
    #     if depth = 0 or node is a terminal node
    #         return the heuristic value of node
    #     if maximizingPlayer
    #         value := −∞
    #         for each child of node do
    #             value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
    #             if α == −∞
    #                 α := max(α, value)
    #             else
    #                 α := max(α, value)
    #                 if α ≥ β then
    #                     break (* β cut-off *)
    #         return value

    #     else
    #         value := +∞
    #         for each child of node do
    #             value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
    #             if β == +∞
    #                 β := min(β, value)
    #             else
    #                 β := min(β, value)
    #                 if α ≥ β then
    #                     break (* α cut-off *)
    #         return value

    # base case
    terminal_state, status = game_over(node)
    if depth == 0 or terminal_state:
        if status == 'tie':
            return 0
        elif maximizingPlayer:
            return -1
        else:
            return 1

    if maximizingPlayer:
        best_val = -100000
        for move in open_squares(node):
            child_node = child(node, move, current_shape)
            best_val = max(best_val, minimax(child_node, depth-1, False, alpha, beta, next_shape, current_shape))
            alpha = max(best_val, alpha)
            if alpha >= beta:
                    break

        return best_val

    else:
        best_val = 100000
        for move in open_squares(node):
            child_node = child(node, move, current_shape)
            best_val = min(best_val, minimax(child_node, depth-1, True, alpha, beta, next_shape, current_shape))
            beta = min(best_val, beta)
            if alpha >= beta:
                break

        return best_val

class MinMaxPlayer(Player):

    def __init__(self, shape, opp_shape):
        super().__init__(shape)
        self.opp_shape = opp_shape

    @timeit
    def move(self, board):
        v = -10000
        best_moves = []
        for move in open_squares(board):
            score = minimax(child(board, move, self.shape), 50, False, -100000, 100000, self.opp_shape, self.shape)
            if score > v:
                v = score
                best_moves = [move]
            elif score == v:
                best_moves.append(move)
        best_move = best_moves[np.random.randint(0, len(best_moves))]
        board[best_move] = self.shape


