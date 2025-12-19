"""
Branch-and-Bound Search Algorithm

Implements exhaustive tree search with pruning to find optimal scheduling
solutions that minimize soft constraint violations.
"""

from typing import List, Tuple, Optional
from scheduler_structures import *
from soft_constraints import *
from and_tree_node import *
import math

class BranchAndBound:
    """
    Implements branch-and-bound search for finding optimal scheduling solutions.
    Explores all valid branches with pruning based on the best solution found so far.
    """
    def __init__(self, root: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):
        self.root = root
        self.hard_constraints = hard_constraints
        self.soft_constraints = soft_constraints
        self.best_solution: Optional[AndTreeNode] = None
        self.best_score: float = float('inf')  # Upper bound for pruning
        self.nodes_explored = 0
        self.nodes_pruned = 0
        
    def search(self, node: AndTreeNode) -> Optional[AndTreeNode]:
        """
        Recursive branch-and-bound search.
        
        Process:
        1. Check if current node is a complete schedule
        2. If complete, update best solution if better
        3. If not complete, expand node and recursively search children
        4. Prune branches where current eval >= best_score
        """
        self.nodes_explored += 1
        
        # Base case: Check if this is a complete schedule
        if node.is_complete_schedule():
            current_score = self.soft_constraints.eval(node)
            if current_score < self.best_score:
                self.best_solution = node
                self.best_score = current_score
                print(f"Found better solution! Score: {self.best_score}, Depth: {node.depth}")
            return node
        
        # Pruning: Skip this branch if current evaluation >= best known solution
        current_eval = self.soft_constraints.eval(node)
        if current_eval >= self.best_score:
            self.nodes_pruned += 1
            return None
        
        # Expand the current node to generate children
        node.expand(self.hard_constraints)
        
        # If no valid children, this is a dead end
        if not node.children:
            return None
        
        # Apply f_bound to filter out worst candidates (keep best 60%)
        filtered_children = self._apply_fbound(node.children, threshold=0.4)
        
        # Recursively search all filtered children
        for child in filtered_children:
            self.search(child)
        
        return self.best_solution
    
    def _apply_fbound(self, children: List[AndTreeNode], threshold: float) -> List[AndTreeNode]:
        """
        Filters children to keep only the best (1-threshold)% of them.
        
        Args:
            children: List of child nodes to filter
            threshold: Fraction to remove (e.g., 0.4 means remove worst 40%, keep best 60%)
        
        Returns:
            Filtered list of children sorted by eval score (best first)
        """
        if not children:
            return []
        
        # Sort children by evaluation score (lower is better)
        sorted_children = sorted(children, key=self.soft_constraints.eval)
        
        # Calculate how many to keep
        if len(sorted_children) == 1:
            return sorted_children
        
        # Keep the best (1-threshold) fraction
        num_to_keep = max(1, int(len(sorted_children) * (1 - threshold)))
        
        return sorted_children[:num_to_keep]


def SearchProcess(root_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints) -> Optional[AndTreeNode]:
    """
    Main entry point for branch-and-bound search.
    
    Explores the search tree exhaustively with pruning to find the optimal schedule
    that minimizes soft constraint violations while satisfying all hard constraints.
    
    Args:
        root_node: Initial empty state
        hard_constraints: Hard constraints that must be satisfied
        soft_constraints: Soft constraints to minimize
    
    Returns:
        Best complete schedule found, or None if no valid schedule exists
    """
    print("Starting branch-and-bound search...")
    print(f"Total games: {len(root_node.games)}, Total practices: {len(root_node.practices)}")
    print(f"Total slots: {len(root_node.slots)}")
    
    bb = BranchAndBound(root_node, hard_constraints, soft_constraints)
    result = bb.search(root_node)
    
    print(f"\nSearch complete!")
    print(f"Nodes explored: {bb.nodes_explored}")
    print(f"Nodes pruned: {bb.nodes_pruned}")
    
    if result:
        print(f"Best solution score: {bb.best_score}")
        print(f"Solution depth: {result.depth}")
    else:
        print("No valid solution found.")
    
    return result