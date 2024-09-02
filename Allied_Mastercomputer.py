import numpy as np
import math

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
    def __init__(self, state, move=None, parent=None):
        self.state = state
        self.move = move
        self.parent = parent
        self.children = []
        self.value = 0
        self.node_visits = 0
        self.expanded = False

    def add_child(self, node):
        self.children.append(node)

    def calculate_UCB(self, total_visits, exploration_param=math.sqrt(2)):
        if self.node_visits == 0:
            return float('inf')  # Prioritize unvisited nodes
        return (self.value / self.node_visits) + exploration_param * math.sqrt(math.log(total_visits) / self.node_visits)

    def generate_possible_moves(self):
        possible_expansions = []
        for row in range(15):
            for index in range(15):
                if self.state[row, index] == 0:
                    possible_expansions.append((row, index))
        return possible_expansions

class GomokuAgent:
    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.name = "Boss Mastercomputer Gomoku Killer 100000LVL"
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol

    def play(self, board):
        best_move = self.run(board)
        return best_move

    def run(self, board):
        MAX_ITERATIONS = 1000
        root_node = Node(board)
        for _ in range(MAX_ITERATIONS):
            selected_node = self.select(root_node)
            reward = self.simulate(selected_node)
            self.backpropagate(selected_node, reward)
        
        best_child = max(root_node.children, key=lambda node: node.node_visits)
        return best_child.move

    def select(self, node):
        while node.expanded and node.children:
            total_visits = sum(child.node_visits for child in node.children)
            node = max(node.children, key=lambda child: child.calculate_UCB(total_visits))
        if not node.expanded:
            self.expand(node)
        return node

    def expand(self, node):
        possible_moves = node.generate_possible_moves()
        for move in possible_moves:
            new_board = node.state.copy()
            new_board[move[0], move[1]] = self.agent_symbol
            child_node = Node(new_board, move, node)
            node.add_child(child_node)
        node.expanded = True

    def simulate(self, node, agent_turn=False):
        current_state = node.state.copy()
        possible_moves = node.generate_possible_moves()
        move_count = 0

        turn = self.opponent_symbol if agent_turn else self.agent_symbol

        while move_count < len(possible_moves):
            random_move_index = np.random.randint(0, len(possible_moves))
            move = possible_moves.pop(random_move_index)
            current_state[move[0], move[1]] = turn
            turn = self.agent_symbol if turn == self.opponent_symbol else self.opponent_symbol
            move_count += 1

            result = GomokuAgent.is_winner(current_state, move)
            if result:
                return result
        return 0  # Draw

    def backpropagate(self, node, reward):
        while node is not None:
            node.node_visits += 1
            node.value += reward
            node = node.parent

    @staticmethod
    def is_winner(board, move):
        i, j = move
        player = board[i, j]
        WIN_LINE_LENGTH = 5

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
        
        return player if c1 or c2 or c3 or c4 else False
