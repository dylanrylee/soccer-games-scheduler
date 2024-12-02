from typing import List, Tuple
from scheduler_structures import *
from AndTreeNode import *
import math

class Fleaf:
    """
    Handles the search process for finding feasible scheduling solutions.
    """
    def __init__(self, root: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):
        self.root = root
        self.hard_constraints = hard_constraints
        self.soft_constraints = soft_constraints
    
    """
    Decides which of the current_node children to expand and returns the best child
    """
    def f_leaf(current_node: List[AndTreeNode]):

        "Eval is what is used to find score based from the soft constraints"
        node_to_expand : AndTreeNode = None

        "Checks every leaf in node and finds the node that is has the lowest evaluation score"
        for node in current_node:
            if node_to_expand == None or eval(node) < eval(node_to_expand): 
                node_to_expand = node

        return node_to_expand

class Ftrans:
    """
    
    """
    def __init__(self, root: AndTreeNode):
        self.root = root # This is the root of the set of leaves

    def f_trans(self) -> AndTreeNode:
        """
        This function makes the transition to the state that has the lowest eval score
        within the current nodes' leaves set
        """
        
        current_state = self.root

        chosen_leaf = Fleaf.f_leaf(current_state.children)
            
        # If the child state of the current state has the same eval
        if (eval(chosen_leaf) <= eval(current_state)):
            return chosen_leaf

class Fbound:

    def __init__(self, root: AndTreeNode):
        self.root = root # This is the root of the set of leaves

    def f_bound(self):

        L = self.root.children

        # This is the cutoff of the fbound
        cutoff = math.ceil(len(L) * (1-self.threshold))

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        # If there is only one leaf, then don't delete the first 40%
        if len(L) == 1:
            sorted_L = sorted(L, key=eval, reverse=True)
        else:
            sorted_L = sorted(L, key=eval, reverse=True)[cutoff:]

        return sorted_L
    

def main():

    # Create the initial state (root node)
    root_node = AndTreeNode(slots, games, practices, depth=0)

    # Initialize the classes
    threshold = 0.6  # Example threshold value
    fbound = Fbound(root_node, threshold)
    fleaf = Fleaf(root_node, hard_constraints, soft_constraints)
    ftrans = Ftrans(root_node)

    # Apply fbound to filter the leaves
    filtered_leaves = fbound.f_bound()

    # Apply fleaf to select the best leaf from the filtered leaves
    best_leaf = fleaf.f_leaf(filtered_leaves)

    # Apply ftrans to transition to the selected leaf
    new_state = ftrans.f_trans()