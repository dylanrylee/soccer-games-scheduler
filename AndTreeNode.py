from typing import List, Tuple
from scheduler_structures import *
from hard_constraints import *

class AndTreeNode:
    """
    Represents a node in the AND/OR search tree.
    """
    def __init__(self, slots: List[Slot], games: List[Game], practices: List[Practice], depth: int = 0):
        self.slots = slots
        self.games = games
        self.practices = practices
        self.depth = depth
        self.children = []  # Subtrees for further exploration

    def expand(self, constraints: HardConstraints):
        """
        Expands the node by generating child nodes based on possible assignments.
        """
        if constraints.constr():  # Stop if constraints are satisfied
            return True

        # Explore all possible slot assignments for unassigned games or practices
        for game in self.games:
            if game.assigned_slot is None:
                for slot in self.slots:
                    new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    new_game = Game(**game.__dict__)
                    new_game.assign_slot(slot)
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)
                    self.children.append(new_node)
        return False

    def __repr__(self):
        return f"AndTreeNode(Depth={self.depth}, Slots={self.slots}, Games={self.games}, Practices={self.practices})"
