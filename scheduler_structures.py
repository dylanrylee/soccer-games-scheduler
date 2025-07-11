from typing import List, Optional, Union
import copy

class Slot:
    """
    Represents a time slot (s ∈ S).
    """
    # def __init__(self, day: str, start_time: str, max_games: int, min_games: int, max_practices: int, min_practices: int):
    #     self.day = day                              
    #     self.start_time = start_time                # Start time in "HH:MM" format
    #     self.max_games = max_games
    #     self.min_games = min_games
    #     self.max_practices = max_practices
    #     self.min_practices = min_practices
    #     self.assigned_games: List[str] = []
    #     self.assigned_practices: List[str] = []

    def __init__(self, day: str, start_time: str, max_games: int, min_games: int, max_practices: int, min_practices: int, assigned_games: List[str] = [], assigned_practices: List[str] = []):
        self.day = day                              
        self.start_time = start_time                # Start time in "HH:MM" format
        self.max_games = max_games
        self.min_games = min_games
        self.max_practices = max_practices
        self.min_practices = min_practices
        self.assigned_games: List[str] = copy.deepcopy(assigned_games)
        self.assigned_practices: List[str] = copy.deepcopy(assigned_practices)

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
    def __init__(self, identifier: str, league: str, age_group: str, tier: str, division: str, assigned_slot: Optional[Slot] = None, constraints: List[Union[str, Slot]] = []):
        self.identifier = identifier    # Unique game identifier
        self.league = league            
        self.age_group = age_group      
        self.tier = tier      
        self.division = division
        self.assigned_slot = assigned_slot
        self.constraints = constraints

    def assign_slot(self, slot: Slot):
        """
        Assigns the game to a specific slot.
        """          
        self.assigned_slot = slot
        slot.assigned_games.append(self.identifier)

    def __repr__(self):
        return (f"Game(ID={self.identifier}, League={self.league}, AgeGroup={self.age_group}, "
                f"Tier={self.tier}, Division={self.division}, AssignedSlot={self.assigned_slot})")

class Practice:
    """
    Represents a practice (p ∈ P).
    """
    def __init__(self, identifier: str, associated_game: Optional[str], type: str, assigned_slot: Optional[Slot] = None, constraints: List[Union[str, Slot]] = []):
        self.identifier = identifier                # Unique practice identifier
        self.associated_game = associated_game      # Game ID that this practice is linked to
        self.type = type
        self.assigned_slot = assigned_slot
        self.constraints = constraints

    def assign_slot(self, slot: Slot):
        """
        Assigns the practice to a specific slot.
        """
        self.assigned_slot = slot
        slot.assigned_practices.append(self.identifier)

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