"""
AND-Tree Node for Branch-and-Bound Search

Represents a node in the search tree where each node corresponds to a partial
schedule state. Nodes can be expanded to generate child states by assigning
games and practices to time slots.
"""

from typing import List, Tuple
from scheduler_structures import *
from hard_constraints import *
import copy

class AndTreeNode:
    """
    Represents a node in the AND/OR search tree.
    
    Each node contains a partial schedule state with:
    - slots: Available time slots
    - games: Games to be scheduled
    - practices: Practices to be scheduled
    - depth: Current depth in the search tree
    - children: Child nodes representing possible next assignments
    """
    def __init__(self, slots: List[Slot], games: List[Game], practices: List[Practice], depth: int = 0):
        self.slots = slots
        self.games = games
        self.practices = practices
        self.depth = depth
        self.children = []  # Subtrees for further exploration
        self.parent: AndTreeNode

    def expand(self, constraints: HardConstraints):
        """
        Expands the node by generating child nodes based on possible assignments.
        
        For each unassigned game or practice, creates child nodes by trying to
        assign it to each available slot. Only creates children that satisfy
        hard constraints.
        
        Args:
            constraints: Hard constraints that must be satisfied
        """
        # Expand by assigning games to slots
        for game in self.games:
            if game.assigned_slot is None:
                for slot in self.slots:
                    # Create deep copies to ensure state isolation
                    new_slots = copy.deepcopy(self.slots)
                    new_games = copy.deepcopy(self.games)
                    
                    # Find the corresponding slot and game in the copies
                    for new_slot in new_slots:
                        if new_slot.day == slot.day and new_slot.start_time == slot.start_time:
                            for new_game in new_games:
                                if new_game.identifier == game.identifier:
                                    new_game.assign_slot(new_slot)
                                    break
                            break
                    
                    # Create child node with the new assignment
                    new_node = AndTreeNode(new_slots, new_games, self.practices, self.depth + 1)
                    
                    # Only add child if it satisfies hard constraints
                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):
                        self.children.append(new_node)
        
        # Expand by assigning practices to slots
        for practice in self.practices:
            if practice.assigned_slot is None:
                for slot in self.slots:
                    # Create deep copies to ensure state isolation
                    new_slots = copy.deepcopy(self.slots)
                    new_practices = copy.deepcopy(self.practices)
                    
                    # Find the corresponding slot and practice in the copies
                    for new_slot in new_slots:
                        if new_slot.day == slot.day and new_slot.start_time == slot.start_time:
                            for new_practice in new_practices:
                                if new_practice.identifier == practice.identifier:
                                    new_practice.assign_slot(new_slot)
                                    break
                            break
                    
                    # Create child node with the new assignment
                    new_node = AndTreeNode(new_slots, self.games, new_practices, self.depth + 1)
                    
                    # Only add child if it satisfies hard constraints
                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):
                        self.children.append(new_node)

    def is_complete_schedule(self) -> bool:
        """
        Checks if this node represents a complete schedule.
        
        A schedule is complete if either:
        1. All games and practices are assigned to slots, OR
        2. All slots are filled to maximum capacity
        
        Returns:
            True if schedule is complete, False otherwise
        """
        total_games_assigned = sum(len(slot.assigned_games) for slot in self.slots)
        total_practices_assigned = sum(len(slot.assigned_practices) for slot in self.slots)

        # Check if all items are assigned
        if len(self.games) == total_games_assigned and len(self.practices) == total_practices_assigned:
            return True

        # Check if all slots are at maximum capacity
        max_capacity = sum(slot.max_games + slot.max_practices for slot in self.slots)
        if max_capacity == total_games_assigned + total_practices_assigned:
            return True

        return False
    
    def __repr__(self):
        return f"AndTreeNode(Depth={self.depth},\\n  Slots={self.slots},\\n  Games={self.games},\\n  Practices={self.practices},\\n  Children={self.children})"
