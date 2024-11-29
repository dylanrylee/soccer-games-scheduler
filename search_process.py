from typing import List, Tuple
from sheduler_structures import *
from hard_constraints import *
from AndTreeNode import *

class SearchProcess:
    """
    Handles the search process for finding feasible scheduling solutions.
    """
    def __init__(self, root: AndTreeNode, constraints: HardConstraints):
        self.root = root
        self.constraints = constraints

    def depth_first_search(self):
        """
        Perform a depth-first search to find a valid schedule.
        """
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if self.constraints.constr():
                print("Solution found!")
                return current_node

            current_node.expand(self.constraints)
            stack.extend(current_node.children)

        print("No valid solution found.")
        return None

    def __repr__(self):
        return f"SearchProcess(Root={self.root})"
