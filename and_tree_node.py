from typing import List, Callable
import copy
from hard_constraints import *

class AndTreeNode:
    """
    Represents a node in an AND-Tree for scheduling games and practices.
    """
    def __init__(self, slots: List[Slot], games: List[Game], practices: List[Practice], depth=0, parent=None):
        """
        Initialize a tree node with scheduling state.
        :param slots: List of available Slot objects.
        :param games: List of unassigned Game objects.
        :param practices: List of unassigned Practice objects.
        :param depth: Depth of the node in the tree.
        :param parent: Reference to the parent node.
        """
        self.slots = copy.deepcopy(slots)
        self.games = copy.deepcopy(games)
        self.practices = copy.deepcopy(practices)
        self.remaining_games = {game.identifier for game in games}  # Initialize set of remaining games
        self.remaining_practices = {practice.identifier for practice in practices}  # Initialize set of remaining practices
        self.children = []  # List of child nodes
        self.depth = depth
        self.parent = parent  # Reference to the parent node

    def expand(self, expansion_logic: Callable, hard_constraints: "HardConstraints"):
        """
        Expands the current node using the provided expansion logic.
        :param expansion_logic: A callable that takes (slots, games, practices) and returns a list of child states.
        :param hard_constraints: An instance of the HardConstraints class to validate potential child nodes.
        """
        if self.games or self.practices:
            child_states = expansion_logic(self.slots, self.games, self.practices)
            for child_slots, child_games, child_practices in child_states:
                # Check hard constraints before adding a child node
                if hard_constraints.constr(child_games, child_practices, child_slots) == True:
                    child_node = AndTreeNode(
                        slots=child_slots,
                        games=child_games,
                        practices=child_practices,
                        depth=self.depth + 1,
                        parent=self  # Set current node as parent
                    )
                    self.children.append(child_node)

    def get_remaining_games(self) -> set:
        """
        Returns the set of remaining games to be assigned.
        :return: A set of remaining game identifiers.
        """
        return self.remaining_games

    def get_remaining_practices(self) -> set:
        """
        Returns the set of remaining practices to be assigned.
        :return: A set of remaining practice identifiers.
        """
        return self.remaining_practices

    def print_node(self):
        """
        Prints the current node with its slots and assignments.
        """
        print(f"Node at Depth {self.depth}:")
        if self.parent:
            print(f"  Parent Node Depth: {self.parent.depth}")
        else:
            print("  Root Node (No Parent)")
        for slot in self.slots:
            print(f"  {slot}")
        print(f"  Remaining Games: {self.get_remaining_games()}")
        print(f"  Remaining Practices: {self.get_remaining_practices()}")
        print(f"  Children Count: {len(self.children)}")
        print("-" * 40)

def constrained_expansion_logic(slots: List[Slot], games: List[Game], practices: List[Practice]):
    """
    Expansion logic: Assign the first unassigned game or practice to an available slot.
    - For MO slots, create WE and FR slots with the same time for the same game.
    - For TU slots, create TH slots with the same time for the same game or practice.
    - For MO slots, create WE slots with the same time for the same practice.
    """
    new_states = []
    if games:
        # Assign the first unassigned game to all possible slots
        game_to_assign = games[0]
        for slot in slots:
            if len(slot.assigned_games) < slot.max_games:  # Slot has capacity
                new_slots = copy.deepcopy(slots)
                new_games = copy.deepcopy(games[1:])  # Remove assigned game
                new_practices = copy.deepcopy(practices)

                # Assign the game
                new_slots[slots.index(slot)].assigned_games.append(game_to_assign.identifier)

                # Handle MO slot: Create WE and FR slots
                if slot.day == "MO":
                    time = slot.start_time
                    we_slot = Slot(day="WE", start_time=time, max_games=1, min_games=1,
                                   max_practices=slot.max_practices, min_practices=slot.min_practices,
                                   assigned_games=[game_to_assign.identifier])
                    fr_slot = Slot(day="FR", start_time=time, max_games=1, min_games=1,
                                   max_practices=slot.max_practices, min_practices=slot.min_practices,
                                   assigned_games=[game_to_assign.identifier])

                    # Ensure these slots are only used for the assigned game
                    new_slots.append(we_slot)
                    new_slots.append(fr_slot)

                # Handle TU slot: Create TH slot
                elif slot.day == "TU":
                    time = slot.start_time
                    th_slot = Slot(day="TH", start_time=time, max_games=1, min_games=1,
                                   max_practices=slot.max_practices, min_practices=slot.min_practices,
                                   assigned_games=[game_to_assign.identifier])

                    # Ensure this slot is only used for the assigned game
                    new_slots.append(th_slot)

                # Add new state
                new_states.append((new_slots, new_games, new_practices))

    elif practices:
        # Assign the first unassigned practice to all possible slots
        practice_to_assign = practices[0]
        for slot in slots:
            if len(slot.assigned_practices) < slot.max_practices:  # Slot has capacity
                new_slots = copy.deepcopy(slots)
                new_games = copy.deepcopy(games)
                new_practices = copy.deepcopy(practices[1:])  # Remove assigned practice

                # Assign the practice
                new_slots[slots.index(slot)].assigned_practices.append(practice_to_assign.identifier)

                # Handle TU slot: Create TH slot
                if slot.day == "TU":
                    time = slot.start_time
                    th_slot = Slot(day="TH", start_time=time, max_games=slot.max_games, min_games=slot.min_games,
                                   max_practices=1, min_practices=1,
                                   assigned_practices=[practice_to_assign.identifier])

                    # Ensure this slot is only used for the assigned practice
                    new_slots.append(th_slot)

                # Handle MO slot: Create WE slot
                elif slot.day == "MO":
                    time = slot.start_time
                    we_slot = Slot(day="WE", start_time=time, max_games=slot.max_games, min_games=slot.min_games,
                                   max_practices=1, min_practices=1,
                                   assigned_practices=[practice_to_assign.identifier])

                    # Ensure this slot is only used for the assigned practice
                    new_slots.append(we_slot)

                # Add new state
                new_states.append((new_slots, new_games, new_practices))
    
    return new_states
