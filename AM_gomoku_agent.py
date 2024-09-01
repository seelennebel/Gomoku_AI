import numpy as np

def generate_initial_state(first_turn):

    board = np.zeros((15, 15))

    if first_turn:
        return board
    else:
        x = np.random.randint(0, 15, dtype=int)
        y = np.random.randint(0, 15, dtype=int) 
        board[x, y] = -1
        return board

class Node:

    def __init__(self, state):
        self.state = state
        self.expanded = False
        self.nodes_to_expand = []
        self.children = []

    def possible_moves(self):
        return self.generate_possible_moves()

    def calculate_UCB(self):
        return self.prior_probability * math.sqrt(math.log(self.parent_node_simulations) / self.node_simulations) 

    def generate_possible_moves(self):
        possible_expansions = [] 
        for row in range(15):
            for index in range(15):
                if self.state[row, index] == 0:
                    possible_expansions.append((row, index)) 
        return possible_expansions

    def __str__(self):
        return "Node: {}".format(self.state)

class GomokuAgent:

    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol

    def play(self, board):
        root_node = Node(board)
        current_node = root_node
        if not current_node.expanded:

            for move in current_node.possible_moves():
                self.expand_agent_node(current_node, move, board.copy())

            for node in current_node.nodes_to_expand:
                current_node.children.insert(-1, node)
                self.simulate(node, agent_turn=False)

    def expand_agent_node(self, node, move, board):
        board[move[0], move[1]] = self.agent_symbol
        new_node = Node(board)
        node.nodes_to_expand.insert(-1, new_node)

    def backpropagate(self)
        
    def simulate(self, node, agent_turn = False):

        if not agent_turn:

            possible_moves = node.generate_possible_moves()

            for move in possible_moves:

                random_move_index = np.random.randint(0,len(possible_moves))
                node.state[move[0], move[1]] = self.opponent_symbol

                if self.is_winner(node.state, move):
                    self.backpropagate()

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

initial_state = generate_initial_state(first_turn=False)

net = GomokuAgent(1, 0, -1)
net.play(initial_state)
