import math
from typing import List
from and_tree_node import AndTreeNode
from soft_constraints import SoftConstraints


class Fbound:
    """
    Filters and sorts child nodes based on evaluation values.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        self.soft_constraints = soft_constraints

    def filter_nodes(self, parent_node: AndTreeNode, children_nodes: List[AndTreeNode]) -> List[AndTreeNode]:
        if not children_nodes:
            return []

        if len(children_nodes) == 1:
            return children_nodes

        # Sort children and retain the top 60%
        retain_count = math.ceil(0.6 * len(children_nodes))
        return sorted(children_nodes, key=self.soft_constraints.eval, reverse=True)[:retain_count]


class Fleaf:
    """
    Chooses the leaf node with the lowest evaluation value.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        self.soft_constraints = soft_constraints

    def choose_lowest_eval_leaf(self, parent_node: AndTreeNode, filtered_children: List[AndTreeNode]) -> AndTreeNode:
        if not filtered_children:
            raise ValueError("Cannot choose from an empty list of filtered children.")

        return min(filtered_children, key=self.soft_constraints.eval)


class Ftrans:
    """
    Decides whether to transition to a chosen leaf based on evaluation constraints.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        self.soft_constraints = soft_constraints

    def transition_to_leaf(self, parent_node: AndTreeNode, chosen_leaf: AndTreeNode) -> AndTreeNode:
        """
        Transition only if the leaf's evaluation is <= the parent's evaluation.
        """
        if self.soft_constraints.eval(chosen_leaf) <= self.soft_constraints.eval(parent_node):
            return chosen_leaf
        return chosen_leaf
