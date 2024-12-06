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
    def f_leaf(self, constraints: SoftConstraints, current_node: AndTreeNode):

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
    def __init__(self, chosen_leaf: AndTreeNode):
        self.chosen_leaf = chosen_leaf # This is the root of the set of leaves

    def f_trans(self, current_node: AndTreeNode, soft_constraints: SoftConstraints) -> AndTreeNode:
        """
        This function makes the transition to the state that has the lowest eval score
        within the current nodes' leaves set
        """
            
        # If the child state of the current state has the same eval
        if (self.chosen_leaf != None and soft_constraints.eval(self.chosen_leaf) <= soft_constraints.eval(current_node)):
            current_node.parent = current_node
            return self.chosen_leaf
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
        cutoff = math.ceil(len(L) * (1-self.threshold)) + 1

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        # If there is only one leaf, then don't delete the first 40%
        if len(L) == 1:
            sorted_L = sorted(L, key=self.constraints.eval, reverse=True)
        else:
            sorted_L = sorted(L, key=self.constraints.eval, reverse=True)[cutoff:]

        return sorted_L
    

# def SearchProcess(root_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):

#     # Create the initial state (root node)
#     completed_schdules: List[AndTreeNode] = []
#     # Initialize the classes
#     threshold = 0.6  # Example threshold value
#     fbound = Fbound(root_node, threshold, soft_constraints)
#     ftrans = Ftrans(root_node)

#     current_node = root_node
#     current_node.expand(hard_constraints)
#     # print(current_node)
#     for _ in range(100):
#         # print(i)
#         # print(current_node)
#         if (current_node == None or current_node.children == None):
#             # print("  break")
#             break
#         elif current_node.is_complete_schedule():
#             # print(f"  {current_node}")
#             completed_schdules.append(current_node)
#             break
#         else:
#             # print(f"  expand")
#             current_node.expand(hard_constraints)
#             current_node.children = Fbound(current_node, threshold, soft_constraints).f_bound()
#         print(current_node)
#         current_node = ftrans.f_trans(current_node, hard_constraints, soft_constraints)
    
#     best_schedule = None
#     if len(completed_schdules) > 0:
#         best_schedule = min(completed_schdules, key=soft_constraints.eval)
    
#     print(len(completed_schdules))
#     print(current_node.children)

#     return best_schedule    

def SearchProcess(root_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):
        """
        1. Expand the inputted node.
        2. Call f_bound on the leaf children to filter them.
        3. Use f_leaf to select the best leaf.
        4. Transition with f_trans.
        5. Repeat until complete schedules are collected.
        6. Return the best schedule.
        """
        current_node = root_node
        complete_schedules = []

        while True:
            # Step 1: Expand the current node
            current_node.expand(hard_constraints)

            # Step 2: Filter leaves using f_bound
            fbound = Fbound(current_node, threshold=0.4, constraints=soft_constraints)
            filtered_leaves = fbound.f_bound()

            if not filtered_leaves:
                break  # No more nodes to process

            # Step 3: Select the best leaf with f_leaf
            fleaf = Fleaf(root_node, hard_constraints, soft_constraints)
            chosen_leaf = fleaf.f_leaf(soft_constraints, current_node)

            # Step 4: Transition to the chosen leaf with f_trans
            ftrans = Ftrans(chosen_leaf)
            transitioned_leaf = ftrans.f_trans(current_node, soft_constraints)

            if transitioned_leaf == None:
                break  # Can't transition further

            # Step 5: Check if the schedule is complete
            if transitioned_leaf.is_complete_schedule():
                complete_schedules.append(transitioned_leaf)

            # Set the transitioned leaf as the current node for the next iteration
            current_node = transitioned_leaf

            print(current_node.depth)
        print(len(complete_schedules))
        
        # Step 6: Get the best schedule from all complete schedules
        if complete_schedules:
            best_schedule = min(complete_schedules, key=soft_constraints.eval)
            return best_schedule
        else:
            return None