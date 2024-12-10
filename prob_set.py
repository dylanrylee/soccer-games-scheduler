from typing import List, Optional, Union
import copy

class Slot:
    """
    Represents a time slot for games and practices.

    Attributes:
        identifier (str): A unique identifier for the slot based on the day and start time.
        day (str): The day of the slot (e.g., "Monday").
        start_time (str): The start time of the slot in "HH:MM" format.
        max_games (int): The maximum number of games allowed in this slot.
        min_games (int): The minimum number of games required in this slot.
        max_practices (int): The maximum number of practices allowed in this slot.
        min_practices (int): The minimum number of practices required in this slot.
        assigned_games (List[str]): A list of games assigned to this slot.
        assigned_practices (List[str]): A list of practices assigned to this slot.
    """
    def __init__(self, day: str, start_time: str, max_games: int, min_games: int, max_practices: int, min_practices: int, 
                 assigned_games: List[str] = [], assigned_practices: List[str] = []):
        self.identifier = day + ", " + start_time # Unique slot identifier
        self.day = day                              
        self.start_time = start_time                # Start time in "HH:MM" format
        self.max_games = max_games                  
        self.min_games = min_games
        self.max_practices = max_practices
        self.min_practices = min_practices
        self.assigned_games: List[str] = copy.deepcopy(assigned_games)
        self.assigned_practices: List[str] = copy.deepcopy(assigned_practices)
    
    def __repr__(self):
        """
        Returns a string representation of the Slot object,
        including its day, start time, constraints, and assigned activities.
        """
        return (f"Slot(Day={self.day}, StartTime={self.start_time}, "
                f"MaxGames={self.max_games}, MinGames={self.min_games}, "
                f"MaxPractices={self.max_practices}, MinPractices={self.min_practices}, "
                f"AssignedGames={self.assigned_games}, AssignedPractices={self.assigned_practices})")


class Game:
    """
    Represents a game (g ∈ G).

    Attributes:
        identifier (str): A unique identifier for the game.
        league (str): The league associated with the game.
        age_group (str): The age group for the game (e.g., "U12").
        tier (str): The tier or skill level of the game.
        division (str): The division to which the game belongs.
        assigned_slot (Slot or None): The slot assigned to this game (default is None).
        constraints (List[Union[str, Slot]]): List of constraints associated with the game, 
            which may include specific slots or other conditions.
        practices (List[Practice]): Practices associated with this game (empty by default).
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
        Assigns the game to a specific slot and updates the slot's assigned games.

        Args:
            slot (Slot): The time slot to assign this game to.
        """
        self.assigned_slot = slot
        slot.assigned_games.append(self.identifier)

    def get_practices(self):
        """
        Retrieves all practices associated with this game, sorted in ascending order.

        Returns:
            List[Practice]: A sorted list of practices for this game.
        """
        sorted_practices = sorted(self.practices)
        return sorted_practices

    def __repr__(self):
        """
        Returns a string representation of the Game object, including its identifier, 
        league, age group, tier, division, assigned slot, and associated practices.

        Returns:
            str: A string representation of the Game instance.
        """
        return (f"Game(ID={self.identifier}, League={self.league}, AgeGroup={self.age_group}, "
                f"Tier={self.tier}, Division={self.division}, AssignedSlot={self.assigned_slot}, "
                f"Practices={[p.identifier for p in self.practices]})")


class Practice:
    """
    Represents a practice (p ∈ P).

    Attributes:
        identifier (str): A unique identifier for the practice.
        associated_game (Game): The game to which this practice is linked.
        type (str): The type of practice (e.g., "regular", "special").
        assigned_slot (Slot or None): The slot assigned to this practice (default is None).
        constraints (List[Union[str, Slot]]): A list of constraints associated with the practice, 
            which may include specific slots or other scheduling conditions.
    """
    def __init__(self, identifier: str, associated_game: Game, type: str, constraints: List[Union[str, Slot]] = []):
        self.identifier = identifier                # Unique practice identifier
        self.associated_game = associated_game      # Game that this practice is linked to
        self.type = type
        self.assigned_slot = None
        self.constraints = constraints

    def assign_slot(self, slot: Slot):
        """
        Assigns the practice to a specific slot and updates the slot's assigned practices.

        Args:
            slot (Slot): The time slot to assign this practice to.
        """
        self.assigned_slot = slot
        slot.assigned_practices.append(self.identifier)

    def __repr__(self):
        """
        Returns a string representation of the Practice object, including its identifier, 
        associated game, type, and assigned slot.

        Returns:
            str: A string representation of the Practice instance.
        """
        return (f"Practice(ID={self.identifier}, AssociatedGame={self.associated_game.identifier if self.associated_game else None}, "
                f"Type={self.type}, AssignedSlot={self.assigned_slot})")