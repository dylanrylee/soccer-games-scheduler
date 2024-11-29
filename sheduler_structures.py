from typing import List, Optional, Union

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

class State:
    """
    Represents a state in the scheduling process.
    A state is a mapping of slots to assigned games and practices.
    """
    def __init__(self, slots: List[Slot]):
        self.slots = {slot: {"games": [], "practices": []} for slot in slots}

    def assign_game(self, game: Game, slot: Slot) -> bool:
        """
        Assigns a game to a slot if constraints are met.
        Returns True if assignment is successful, False otherwise.
        """
        if len(self.slots[slot]["games"]) < slot.max_games:
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

    def __repr__(self):
        return f"State(Slots={self.slots})"


