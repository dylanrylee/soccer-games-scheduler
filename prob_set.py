from typing import List, Optional, Union
import copy

class Slot:
    """
    Represents a time slot (s ∈ S).
    """
    def __init__(self, day: str, start_time: str, max_games: int, min_games: int, max_practices: int, min_practices: int, 
                 assigned_games: List[str] = [], assigned_practices: List[str] = []):
        self.identifier = day + ", " + start_time
        self.day = day                              
        self.start_time = start_time                # Start time in "HH:MM" format
        self.max_games = max_games
        self.min_games = min_games
        self.max_practices = max_practices
        self.min_practices = min_practices
        self.assigned_games: List[str] = copy.deepcopy(assigned_games)
        self.assigned_practices: List[str] = copy.deepcopy(assigned_practices)
    
    def __repr__(self):
        return (f"Slot(Day={self.day}, StartTime={self.start_time}, "
                f"MaxGames={self.max_games}, MinGames={self.min_games}, "
                f"MaxPractices={self.max_practices}, MinPractices={self.min_practices}, "
                f"AssignedGames={self.assigned_games}, AssignedPractices={self.assigned_practices})")


class Game:
    """
    Represents a game (g ∈ G).
    """
    def __init__(self, identifier: str, league: str, age_group: str, tier: str, division: str, constraints: List[Union[str, Slot]] = []):
        self.identifier = identifier    # Unique game identifier
        self.league = league            
        self.age_group = age_group      
        self.tier = tier      
        self.division = division
        self.assigned_slot = None
        self.constraints = constraints
        self.practices: List[Practice] = []  # Practices associated with this game

    def assign_slot(self, slot: Slot):
        """
        Assigns the game to a specific slot.
        """
        self.assigned_slot = slot
        slot.assigned_games.append(self.identifier)

    def get_practices(self):
        sorted_practices = sorted(self.practices)
        return sorted_practices

    def __repr__(self):
        return (f"Game(ID={self.identifier}, League={self.league}, AgeGroup={self.age_group}, "
                f"Tier={self.tier}, Division={self.division}, AssignedSlot={self.assigned_slot}, "
                f"Practices={[p.identifier for p in self.practices]})")


class Practice:
    """
    Represents a practice (p ∈ P).
    """
    def __init__(self, identifier: str, associated_game: Game, type: str, constraints: List[Union[str, Slot]] = []):
        self.identifier = identifier                # Unique practice identifier
        self.associated_game = associated_game      # Game that this practice is linked to
        self.type = type
        self.assigned_slot = None
        self.constraints = constraints

    def assign_slot(self, slot: Slot):
        """
        Assigns the practice to a specific slot.
        """
        self.assigned_slot = slot
        slot.assigned_practices.append(self.identifier)

    def __repr__(self):
        return (f"Practice(ID={self.identifier}, AssociatedGame={self.associated_game.identifier if self.associated_game else None}, "
                f"Type={self.type}, AssignedSlot={self.assigned_slot})")