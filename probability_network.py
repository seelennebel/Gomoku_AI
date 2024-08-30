#example of state:
# [[-1. -1. -1. -1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]

import numpy as np

from node import Node

#either create an empty numpy array or randomly put single enemy point
def generate_initial_state(first_turn):

    board = np.zeros((15, 15))

    if first_turn:
        return board
    else:
        x = np.random.randint(0, 15, dtype=int)
        y = np.random.randint(0, 15, dtype=int) 
        board[x, y] = -1
        return board

inittial_state = generate_initial_state(first_turn = False)

class Network:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.initial_node = Node(initial_state, None, None, 1, None, 0)
        self.current_node = initial_node

    def expand_node(self, node):
        return

    def is_winner(board, move):
        i, j = move
        player = board[i, j]

        def check(values):
            counter = 0
            for value in values:
                if value == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= WIN_LINE_LENGTH:
                    return True
            return False

        c1 = check(board[i, :])
        c2 = check(board[:, j])
        c3 = check(board.diagonal(j-i))
        c4 = check(np.fliplr(board).diagonal(board.shape[0]-i-j-1))
        
        if c1 or c2 or c3 or c4:
            return player
        
        return False

    def run(self):
        if current_node.expanded == False:
            current_node.expand()

