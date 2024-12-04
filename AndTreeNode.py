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
        self.parent: AndTreeNode

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
                    # print(f"    slot: {slot.day}")
                    # Create a new list of slots where the current slot is copied to ensure immutability
                    new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    # for item in new_slots:
                    #     print(f"    new_slot: {item.day}")

                    # Create a new game object by copying the current game's attributes
                    new_game = Game(**game.__dict__)

                    # Assign the current slot to the new game
                    # self.assign_game(new_game, slot)
                    new_game.assign_slot(slot)

                    # Create a new child node with the updated slots, games, practices, and increment the depth by 1
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)

                    constraints.debug = True
                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):  # Stop if constraints are satisfied
                        # print("      True")
                        # Append the new child node to the list of children
                        self.children.append(new_node)
                    # else:
                        # print("      False")
        
        for practice in self.practices:
            if practice.assigned_slot is None:
                for slot in self.slots:
                    new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    new_practice = Practice(**practice.__dict__)
                    new_practice.assign_slot(slot)
                    # self.assign_practice(new_practice, slot)
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)

                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):  # Stop if constraints are satisfied
                        self.children.append(new_node)

        """
        Assigns a game to a slot if constraints are met.
        Returns True if assignment is successful, False otherwise.
        """
    def assign_game(self, game: Game, slot: Slot) -> bool:
        if HardConstraints.enforce_game_max(self.slots):
            # self.slots[slot]["games"].append(game.identifier)
            game.assign_slot(slot)
            return True
        return False

    def assign_practice(self, practice: Practice, slot: Slot) -> bool:
        """
        Assigns a practice to a slot if constraints are met.
        Returns True if assignment is successful, False otherwise.
        """
        if len(self.slots) < slot.max_practices:
            # self.slots[slot].append(practice.identifier)
            practice.assign_slot(slot)
            return True
        return False

    def is_valid(self) -> bool:
        """
        Validates the state to ensure all slots respect their constraints.
        """
        for slot, assignments in self.slots.items():
            if len(assignments["games"]) > slot.max_games:
                return False  
            if len(assignments["practices"]) > slot.max_practices:
                return False
        return True

    def is_complete_schedule(self) -> bool:
        """
        This returns whether the state has all the games and practices in the input assigned to a time slot
        or all the time slots are filled to max
        """
        total_games_assigned = sum(len(assignments.assigned_games) for assignments in self.slots)
        total_practices_assigned = sum(len(assignments.assigned_practices) for assignments in self.slots)

        if len(self.games) == total_games_assigned and len(self.practices) == total_practices_assigned:
            return True

        max_capacity = sum(slot.max_games + slot.max_practices for slot in self.slots)
        if max_capacity == total_games_assigned + total_practices_assigned:
            return True

        return False
    
    def __repr__(self):
        return f"AndTreeNode(Depth={self.depth}, Slots={self.slots}, Games={self.games}, Practices={self.practices})"
