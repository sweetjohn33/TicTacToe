from GameOperations.player import Player
from GameOperations.helpers import *

class MinMaxPlayer(Player):

    def __init__(self, shape, opp_shape):
        super().__init__(shape)
        self.opp_shape = opp_shape

    def move(self, board):
        v = -10000
        best_moves = []
        for move in open_squares(board):
            score = self.minimax(child(board, move, self.shape), 50, False, self.opp_shape, self.shape)
            if score > v:
                v = score
                best_moves = [move]
            elif score == v:
                best_moves.append(move)
        best_move = best_moves[np.random.randint(0, len(best_moves))]
        board[best_move] = self.shape

    def minimax(self, node, depth, maximizingPlayer, current_shape, next_shape):
        # function minimax(node, depth, maximizingPlayer)
        #     if depth = 0 or node is a terminal node
        #         return the heuristic value of node
        #     if maximizingPlayer
        #         bestValue: = −∞
        #         for each child of node
        #             v: = minimax(child, depth − 1, FALSE)
        #             bestValue: = max(bestValue, v)
        #         return bestValue
        #     else (*minimizing player *)
        #         bestValue: = +∞
        #         for each child of node
        #             v: = minimax(child, depth − 1, TRUE)
        #             bestValue: = min(bestValue, v)
        #         return bestValue

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
            best_move = None
            for move in open_squares(node):
                child_node = child(node, move, current_shape)
                v = self.minimax(child_node, depth-1, False, next_shape, current_shape)
                if v > best_val:
                    best_val = v
                    best_move = move
            return best_val

        else:
            best_val = 100000
            best_move = None
            for move in open_squares(node):
                child_node = child(node, move, current_shape)
                v = self.minimax(child_node, depth-1, True, next_shape, current_shape)
                if v < best_val:
                    best_val = v
                    best_move = move
            return best_val


