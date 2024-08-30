from  probability_network import Network
import numpy as np

board = np.zeros((15, 15))

board[0,0] = 1
board[0,1] = 1
board[0,2] = 1
board[0,3] = 1
board[0,4] = 1

WIN_LINE_LENGTH = 5

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

print(is_winner(board, (0, 4)))


