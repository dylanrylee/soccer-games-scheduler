from typing import List, Tuple
from scheduler_structures import *
from hard_constraints import *
import copy

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
                    # new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    new_slots = copy.deepcopy(self.slots)
                    # for item in new_slots:
                    #     print(f"    new_slot: {item.day}")

                    # print("  Slots")
                    # print(self.slots)
                    # print("")
                    # print(new_slots)

                    # Create a new game object by copying the current game's attributes
                    # new_game = Game(**game.__dict__)

                    new_games = copy.deepcopy(self.games)
                    # new_games = [g if g != game else Game(**game.__dict__) for g in self.games]

                    # print("  Before")
                    # print(f"    {self.games}")
                    # print(f"    {new_games}")
                    # print("")

                    # Assign the current slot to the new game
                    # self.assign_game(new_game, slot)
                    # new_game.assign_slot(slot)
                    assigned = False
                    for new_slot in new_slots:
                        # print(f"New {new_slot}")
                        # print(f"Original {slot}")
                        if new_slot.day == slot.day and new_slot.start_time == slot.start_time and assigned == False:
                            cont = True
                            
                            for new_game in new_games:
                                print(f"Game {game.identifier}")
                                print(f"New Identifier {new_game.identifier}")
                                if new_game.identifier == game.identifier:
                                    new_game.assign_slot(new_slot)
                                    print(f"Inner {new_slot}")

                                    # new_slot.assigned_games.append(new_game)
                                    assigned = True
                                    cont = False
                                    break
                            print(cont)
                            if cont == False:
                                break

                    # print("  After")
                    # print(f"    {self.games}")
                    # print(f"    {new_games}")
                    # print("")
                    print(f"Outside {new_slots}")
                    # Create a new child node with the updated slots, games, practices, and increment the depth by 1
                    new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)
                    # new_node = AndTreeNode(new_slots, new_games, self.practices, self.depth + 1)

                    # constraints.debug = True
                    print(new_node)
                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):  # Stop if constraints are satisfied
                        # print("      True")
                        # Append the new child node to the list of children
                        self.children.append(new_node)
                        # break
                    # else:
                        # print("      False")
        
        for practice in self.practices:
            if practice.assigned_slot is None:
                for slot in self.slots:
                    # new_slots = [s if s != slot else Slot(**slot.__dict__) for s in self.slots]
                    new_slots = copy.deepcopy(self.slots)
                    new_practices = copy.deepcopy(self.practices)
                    # new_practice.assign_slot(slot)
                    for new_slot in new_slots:
                        if new_slot.day == slot.day and new_slot.start_time == slot.start_time:
                            cont = True
                            for new_practice in new_practices:
                                if new_practice.identifier == practice.identifier:
                                    new_practice.assign_slot(new_slot)
                                    # new_slot.assigned_games.append(new_game)
                                    cont = False
                                    break
                            if cont == False:
                                break
                    # self.assign_practice(new_practice, slot)
                    # new_node = AndTreeNode(new_slots, self.games, self.practices, self.depth + 1)
                    new_node = AndTreeNode(new_slots, self.games, new_practices, self.depth + 1)

                    if constraints.constr(new_node.games, new_node.practices, new_node.slots):  # Stop if constraints are satisfied
                        self.children.append(new_node)
                        # break

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
        return f"AndTreeNode(Depth={self.depth},\n  Slots={self.slots},\n  Games={self.games},\n  Practices={self.practices},\n  Children={self.children})"
