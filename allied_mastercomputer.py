import numpy as np

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

class Node:

    def __init__(self, state):
        self.state = state
        self.expanded = False
        self.nodes_to_expand = []

    def possible_moves(self):
        return Node.__generate_possible_expansions(self, self.state)

    def calculate_UCB(self):
        return self.prior_probability * math.sqrt(math.log(self.parent_node_simulations) / self.node_simulations) 

    def __generate_possible_moves(self, state):
        possible_expansions = [] 
        for row in range(15):
            for index in range(15):
                if state[row, index] == 0:
                    possible_expansions.append((row, index)) 
        return possible_expansions

    def __str__(self):
        return """
                Initial state:\n{}\n
                Parent:\n{}\n
                Children:\n{}\n
                Prior probability:\n{}\n
                Parent node simulations:\n{}\n
                Node simulations:\n{}\n
                Node expanded:\n{}\n
                """.format(self.state, self.parent, self.expansions, self.prior_probability, self.parent_node_simulations, self.node_simulations, self.expanded)

class GomokuAgent:

    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol

    def play(self, board):
        root_node = Node(board)
        current_node = root_node
        if not current_node.expanded:
            for move in current_node.possible_moves()):
                self.expand_node(current_node, move, board)

    def expand_node(self, node, move, board):
        board[move[0], move[1]] = self.agent_symbol
        node.nodes_to_expand.append(board)

    def simulate(self):
        return

initial_state = generate_initial_state(first_turn=False)

net = ProbabilityNetwork(initial_state)
net.run()



