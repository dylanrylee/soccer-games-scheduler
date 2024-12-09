import math
from typing import List
from and_tree_node import AndTreeNode
from soft_constraints import SoftConstraints

class Fbound:
    """
    A class to filter and sort child nodes based on evaluation values.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        """
        Initialize the Fbound class with soft constraints.

        :param soft_constraints: An instance of SoftConstraints used to evaluate nodes.
        """
        self.soft_constraints = soft_constraints

    def filter_nodes(self, parent_node: AndTreeNode, children_nodes: List[AndTreeNode]) -> List[AndTreeNode]:
        """
        Filters and sorts child nodes of a parent node based on evaluation values.

        :param parent_node: The parent AndTreeNode.
        :param children_nodes: List of child AndTreeNode objects to evaluate.
        :return: The top 60% of child nodes sorted by their evaluation values.
        """
        if not children_nodes:
            return []

        if len(children_nodes) == 1:
            return children_nodes

        # Sort children by evaluation value (highest to lowest)
        # evaluated_children = sorted(children_nodes, key=self.soft_constraints.eval, reverse=True)

        # # Calculate how many nodes to remove (40% rounded up)
        # num_to_remove = math.ceil(0.4 * len(children_nodes))

        # # Retain the remaining 60%
        # remaining_children = evaluated_children[num_to_remove:]
        # return remaining_children

        retain_count = math.ceil(0.6 * len(children_nodes))
        return sorted(children_nodes, key=self.soft_constraints.eval, reverse=True)[:retain_count]

class Fleaf:
    """
    A class to choose a single leaf node with the lowest evaluation value.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        """
        Initialize the Fleaf class with soft constraints.

        :param soft_constraints: An instance of SoftConstraints used to evaluate nodes.
        """
        self.soft_constraints = soft_constraints

    def choose_lowest_eval_leaf(self, parent_node: AndTreeNode, filtered_children: List[AndTreeNode]) -> AndTreeNode:
        """
        Chooses the leaf node with the lowest evaluation value from the filtered nodes.

        :param parent_node: The parent AndTreeNode.
        :param filtered_children: List of filtered AndTreeNode objects to evaluate.
        :return: The child node with the lowest evaluation value.
        """
        if not filtered_children:
            raise ValueError("filtered_children is empty.")

        return min(filtered_children, key=self.soft_constraints.eval)

class Ftrans:
    """
    A class to decide whether to transition to a chosen leaf based on evaluation constraints.
    """
    def __init__(self, soft_constraints: SoftConstraints):
        """
        Initialize the Ftrans class with soft constraints.

        :param soft_constraints: An instance of SoftConstraints used to evaluate nodes.
        """
        self.soft_constraints = soft_constraints

    def transition_to_leaf(self, parent_node: AndTreeNode, chosen_leaf: AndTreeNode) -> AndTreeNode:
        """
        Determines whether to transition to the chosen leaf node based on its evaluation value.

        :param parent_node: The parent AndTreeNode.
        :param chosen_leaf: The chosen leaf AndTreeNode to potentially transition to.
        :return: The chosen leaf if the evaluation condition is satisfied; otherwise, None.
        """
        parent_eval = self.soft_constraints.eval(parent_node)
        leaf_eval = self.soft_constraints.eval(chosen_leaf)

        # Transition only if the leaf's evaluation is <= the parent's evaluation
        if leaf_eval <= parent_eval:
            return chosen_leaf
        return chosen_leaf