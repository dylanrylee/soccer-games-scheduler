from typing import List, Optional, Union
from hard_constraints import *

class Slot:
    """
    Represents a time slot (s ∈ S).
    """
    def __init__(self, day: str, start_time: str, max_games: int, min_games: int, max_practices: int, min_practices: int):
        self.day = day                              
        self.start_time = start_time                # Start time in "HH:MM" format
        self.max_games = max_games
        self.min_games = min_games
        self.max_practices = max_practices
        self.min_practices = min_practices
        self.assigned_games: List[str] = []
        self.assigned_practices: List[str] = []

    def get_assigned_games(self):
        return self.assigned_games

    def get_assigned_practices(self):
        return self.assigned_practices
    
    def __repr__(self):
        return (f"Slot(Day={self.day}, StartTime={self.start_time}, "
                f"MaxGames={self.max_games}, MinGames={self.min_games}, "
                f"MaxPractices={self.max_practices}, MinPractices={self.min_practices}, "
                f"AssignedGames={self.assigned_games}, AssignedPractices={self.assigned_practices})")

class Game:
    """
    Represents a game (g ∈ G).
    """
    def __init__(self, identifier: str, league: str, age_group: str, tier: str, division: str):
        self.identifier = identifier    # Unique game identifier
        self.league = league            
        self.age_group = age_group      
        self.tier = tier      
        self.division = division
        self.assigned_slot: Optional[Slot] = None
        self.constraints: List[Union[str, Slot]] = []

    def assign_slot(self, slot: Slot):
        """
        Assigns the game to a specific slot.
        """          
        self.assigned_slot = slot
        slot.assigned_games.insert(len(slot.assigned_games), self.identifier)

    def __repr__(self):
        return (f"Game(ID={self.identifier}, League={self.league}, AgeGroup={self.age_group}, "
                f"Tier={self.tier}, Division={self.division}, AssignedSlot={self.assigned_slot})")

class Practice:
    """
    Represents a practice (p ∈ P).
    """
    def __init__(self, identifier: str, associated_game: Optional[str], type_: str):
        self.identifier = identifier                # Unique practice identifier
        self.associated_game = associated_game      # Game ID that this practice is linked to
        self.type = type_
        self.assigned_slot: Optional[Slot] = None
        self.constraints: List[Union[str, Slot]] = []

    def assign_slot(self, slot: Slot):
        """
        Assigns the practice to a specific slot.
        """
        self.assigned_slot = slot
        slot.assigned_practices.insert(len(slot.assigned_practices), self.identifier)

    def __repr__(self):
        return (f"Practice(ID={self.identifier}, AssociatedGame={self.associated_game}, "
                f"Type={self.type}, AssignedSlot={self.assigned_slot})")
    

    from typing import List, Dict, Optional

def get_total_games_assigned(slot_list: List[Slot]) -> int:
    num_games_assigned_total = 0

    for Slot in slot_list:
        num_games_assigned_total += len(Slot.assigned_games)

    return num_games_assigned_total

def get_total_practices_assigned(slot_list: List[Slot]) -> int:
    num_practices_assigned_total = 0

    for Slot in slot_list:
        num_practices_assigned_total += len(Slot.assigned_practices)

    return num_practices_assigned_total

class State:

    def __init__(self, slots: List[Slot]):
        """
        For each slot in the List[Slot], we initialize each slot with 0 games and practices
        """
        self.slots = {slot: {"games": [], "practices": []} for slot in slots}

    def assign_game(self, game: Game, slot: Slot) -> bool:
        """
        Assigns a game to a slot if constraints are met.
        Returns True if assignment is successful, False otherwise.
        """
        if HardConstraints.enforce_game_max(self.slots[slot]["games"]):
            self.slots[slot]["games"].append(game.identifier)
            game.assign_slot(slot)
            return True
        return False

    def assign_practice(self, practice: Practice, slot: Slot) -> bool:
        """
        Assigns a practice to a slot if constraints are met.
        Returns True if assignment is successful, False otherwise.
        """
        if len(self.slots[slot]["practices"]) < slot.max_practices:
            self.slots[slot]["practices"].append(practice.identifier)
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

    def is_goal_state(self, games: List[Game], practices: List[Practice], slot_list: List[Slot]) -> bool:
        """
        This returns whether the state has all the games and practices in the input assigned to a time slot
        or all the time slots are filled to max
        """
        total_games_assigned = sum(len(assignments["games"]) for assignments in self.slots.values())
        total_practices_assigned = sum(len(assignments["practices"]) for assignments in self.slots.values())

        if len(games) == total_games_assigned and len(practices) == total_practices_assigned:
            return True

        max_capacity = sum(slot.max_games + slot.max_practices for slot in slot_list)
        if max_capacity == total_games_assigned + total_practices_assigned:
            return True

        return False

    def __repr__(self):
        return f"State(Slots={self.slots})"