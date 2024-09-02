import numpy

class Node:
    
    def __init__(self, state):
        self.state = state
        self.children = []
        self.expanded = False

    def add_child(self, node):
        self.children.append(node)

    def generate_possible_moves(self):
        possible_expansions = []
        for row in range(15):
            for index in range(15):
                if self.state[row, index] == 0:
                    possible_expansions.append((row, index))
        return possible_expansions

    def expand(self, agent_symbol, opponent_symbol):
        possible_moves = self.generate_possible_moves()
        for move in possible_moves:
            new_board = self.state.copy()
            new_board[move[0], move[1]] = agent_symbol
            child_node = Node(new_board)
            self.add_child(child_node)
        self.expanded = True


class GomokuAgent:

    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.name = "Boss Gomoku Killer Chat-GPT Destroyer 1000000LVL"
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol

    def run(self, state):

        root = Node(state)

        root.expand(self.agent_symbol, self.opponent_symbol)

        # EXPAND root
        action_probs, value = model.predict(state)
        valid_moves = self.game.get_valid_moves(state)
        action_probs = action_probs * valid_moves  # mask invalid moves
        action_probs /= np.sum(action_probs)
        root.expand(state, to_play, action_probs)

        for _ in range(self.args['num_simulations']):
            node = root
            search_path = [node]

        # SELECT
        while node.expanded():
            action, node = node.select_child()
            search_path.append(node)

        parent = search_path[-2]
        state = parent.state
        # Now we're at a leaf node and we would like to expand
        # Players always play from their own perspective
        next_state, _ = self.game.get_next_state(state, player=1, action=action)
        # Get the board from the perspective of the other player
        next_state = self.game.get_canonical_board(next_state, player=-1)

        # The value of the new state from the perspective of the other player
        value = self.game.get_reward_for_player(next_state, player=1)
        if value is None:
        # If the game has not ended:
        # EXPAND
        action_probs, value = model.predict(next_state)
        valid_moves = self.game.get_valid_moves(next_state)
        action_probs = action_probs * valid_moves  # mask invalid moves
        action_probs /= np.sum(action_probs)
        node.expand(next_state, parent.to_play * -1, action_probs)

        self.backpropagate(search_path, value, parent.to_play * -1)

        return root

    def play(self, board):
        best_action = self.run(board)
        return best_action
