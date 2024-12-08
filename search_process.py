from typing import List, Tuple
from scheduler_structures import *
from soft_constraints import *
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
    def f_leaf(constraints: SoftConstraints, current_node: AndTreeNode):

        "Eval is what is used to find score based from the soft constraints"
        node_to_expand : AndTreeNode = None

        "Checks every leaf in node and finds the node that is has the lowest evaluation score"
        for node in current_node.children:
            if node_to_expand == None or constraints.eval(node) < constraints.eval(node_to_expand): 
                node_to_expand = node

        return node_to_expand

class Ftrans:
    """
    
    """
    def __init__(self, root: AndTreeNode):
        self.root = root # This is the root of the set of leaves

    def f_trans(self, current_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints) -> AndTreeNode:
        """
        This function makes the transition to the state that has the lowest eval score
        within the current nodes' leaves set
        """

        chosen_leaf = Fleaf.f_leaf(soft_constraints, current_node)
<<<<<<< Updated upstream
=======
        # print(chosen_leaf)
>>>>>>> Stashed changes
            
        # If the child state of the current state has the same eval
        if (chosen_leaf != None and soft_constraints.eval(chosen_leaf) <= soft_constraints.eval(current_node)):
            current_node.parent = current_node
            return chosen_leaf
        else:
            return None

class Fbound:

    def __init__(self, root: AndTreeNode, threshold: float, constraints: SoftConstraints):
        self.root = root # This is the root of the set of leaves
        self.threshold = threshold
        self.constraints = constraints

    def f_bound(self):

        L = self.root.children

        # This is the cutoff of the fbound
        cutoff = math.ceil(len(L) * (1-self.threshold))

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        # If there is only one leaf, then don't delete the first 40%
        if len(L) == 1:
            sorted_L = sorted(L, key=self.constraints.eval, reverse=True)
        else:
            sorted_L = sorted(L, key=self.constraints.eval, reverse=True)[cutoff:]

        return sorted_L
    

def SearchProcess(root_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):

    # Create the initial state (root node)
    completed_schdules: List[AndTreeNode] = []
    # Initialize the classes
    threshold = 0.6  # Example threshold value
    fbound = Fbound(root_node, threshold, soft_constraints)
    ftrans = Ftrans(root_node)

    current_node = root_node
    current_node.expand(hard_constraints)
<<<<<<< Updated upstream
    for i in range(100):
        print(i)
        if (current_node == None or current_node.children == None):
            print("  break")
            break
        elif current_node.is_complete_schedule():
            print(f"  {current_node}")
            completed_schdules.append(current_node)
            current_node = current_node.parent
            current_node.children.remove[0]
        else:
            print(f"  expand")
            current_node.expand(hard_constraints)
            current_node.children = Fbound(current_node, threshold, soft_constraints).f_bound()
=======
    # print(current_node)
    for i in range(100):
        # print(i)
        # print(current_node)
        if (current_node == None or current_node.children == None):
            # print("  break")
            break
        elif current_node.is_complete_schedule():
            # print(f"  {current_node}")
            completed_schdules.append(current_node)
            # for child in current_node.children:
            #     completed_schdules.append(SearchProcess(child, hard_constraints, soft_constraints))
            break
            # current_node = current_node.parent
            # current_node.children.remove[0]
        else:
            # print(f"  expand")
            current_node.expand(hard_constraints)
            current_node.children = Fbound(current_node, threshold, soft_constraints).f_bound()
        # print(current_node)
>>>>>>> Stashed changes
        current_node = ftrans.f_trans(current_node, hard_constraints, soft_constraints)
    
    best_schedule = None
    if len(completed_schdules) > 0:
        best_schedule = min(completed_schdules, key=soft_constraints.eval)
    
    return best_schedule
        