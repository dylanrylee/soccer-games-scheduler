from typing import List, Tuple
from sheduler_structures import *
from hard_constraints import *
from AndTreeNode import *

class SearchInstance:
    """
    Represents a single instance of the scheduling problem.
    """
    def __init__(self, slots: List[Slot], games: List[Game], practices: List[Practice], constraints: HardConstraints):
        self.slots = slots
        self.games = games
        self.practices = practices
        self.constraints = constraints

    def is_solution(self):
        """
        Checks if the current instance is a valid solution.
        """
        return self.constraints.constr()

    def __repr__(self):
        return f"SearchInstance(Slots={self.slots}, Games={self.games}, Practices={self.practices})"
