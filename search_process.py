from typing import List, Tuple
from scheduler_structures import *
from AndTreeNode import *
import math

class SearchProcess:
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
    def f_leaf(current_node: AndTreeNode):

        "Eval is what is used to find score based from the soft constraints"
        node_to_expand : AndTreeNode = None

        "Checks every leaf in node and finds the node that is has the lowest evaluation score"
        for node in current_node.children:
            if node_to_expand == None or eval(node) < eval(node_to_expand): 
                node_to_expand = node

        return node_to_expand

class Ftrans:
    def __init__(self, root: AndTreeNode):
        self.root = root # This is the root of the set of leaves

    def f_trans(self) -> AndTreeNode:
        """
        This function makes the transition to the state that has the lowest eval score
        within the current nodes' leaves set
        """
        
        current_state = self.root

        # List of the current state's children
        next_states = self.root.children

        # This takes the state with the lowest eval value
        min_state = min(next_states, key=eval)
            
        # If the child state of the current state has the same eval
        if (eval(min_state) <= eval(current_state)):
            return min_state

class Fbound:
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