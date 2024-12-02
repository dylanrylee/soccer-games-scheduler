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

        # Iterate over all games in the current node
        for game in self.games:
            # Check if the game has not been assigned to a slot
            if game.assigned_slot is None:
                # Iterate over all available slots in the current node
                for slot in self.slots:
                    # Create a new list of slots where the current slot is copied to ensure immutability
                    new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]

                    # Create a new game object by copying the current game's attributes
                    new_game = Game(**game.__dict__)

                    # Assign the current slot to the new game
                    new_game.assign_slot(slot)

                    # Create a new child node with the updated slots, games, practices, and increment the depth by 1
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)

                    if constraints.constr(new_node):  # Stop if constraints are satisfied
                        # Append the new child node to the list of children
                        self.children.append(new_node)
        
        for practice in self.practices:
            if practice.assigned_slot is None:
                for slot in self.slots:
                    new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    new_practice = Practice(**practice.__dict__)
                    new_practice.assign_slot(slot)
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)

                    if constraints.constr(new_node):  # Stop if constraints are satisfied
                        self.children.append(new_node)

    def __repr__(self):
        return f"AndTreeNode(Depth={self.depth}, Slots={self.slots}, Games={self.games}, Practices={self.practices})"
