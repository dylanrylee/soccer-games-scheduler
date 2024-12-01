from typing import List, Tuple
from scheduler_structures import *
from hard_constraints import *
from AndTreeNode import *

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
    """
    
    """
    def f_trans(self) -> AndTreeNode:

    
    

    def f_bound(self):

        return