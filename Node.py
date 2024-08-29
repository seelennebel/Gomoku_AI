class Node:

    def __init__(self, state, parent, children, prior_probability, parent_node_simulations, node_simulations):
        self.state = state
        self.parent = parent
        self.children = children
        self.prior_probability = prior_probability
        self.parent_node_simulations = parent_node_simulations
        self.node_simulations = node_simulations

    def set_state(self, new_state):
        self.state = new_state

    def set_prior_probability(self, new_prior_probability):
        self.prior_probability = new_prior_probability

    def set_node_simulations(self, node_simulations_number):
        self.node_simulations = node_simulations_number

    def add_child(self, new_child):
        self.children.append(new_child)
    
    def expand(self):
        return self.children