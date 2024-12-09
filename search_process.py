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
        # Handle the case where there is only one child
        if len(children_nodes) == 1:
            return children_nodes

        # Evaluate each child node
        # evaluated_children = [(child, self.soft_constraints.eval(child)) for child in children_nodes]
        evaluated_children = sorted(children_nodes, key=self.soft_constraints.eval, reverse=True)
        # print(len(evaluated_children))

        # Sort children by evaluation value (highest to lowest)
        # evaluated_children.sort(key=lambda x: x[1], reverse=True)

        # Calculate how many nodes to remove (40% rounded up)
        num_to_remove = math.ceil(0.4 * len(children_nodes))

        # Retain the remaining 60%
        remaining_children = evaluated_children[num_to_remove:]
        # print(len(remaining_children))

        # for child in remaining_children:
        #     print(self.soft_constraints.eval(child))

        # Extract the nodes from the tuples and return
        return remaining_children
    
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
        :param children_nodes: List of child AndTreeNode objects to evaluate.
        :return: The child node with the lowest evaluation value.
        """

        lowest_eval_leaf = min(filtered_children, key=self.soft_constraints.eval)
        return lowest_eval_leaf
    
class Ftrans:
    """
    A class to decide whether to transition to a chosen leaf based on evaluation constraints.
    """
    def __init__(self, soft_constraints: SoftConstraints):
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

        # print(parent_eval)
        # print(leaf_eval)
        # Transition only if the leaf's evaluation is <= the parent's evaluation
        if leaf_eval <= parent_eval:
            return chosen_leaf
        return chosen_leaf
