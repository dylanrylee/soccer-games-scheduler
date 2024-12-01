from typing import List, Tuple
from scheduler_structures import *
from hard_constraints import *
from AndTreeNode import *
import math

class SearchProcess:
    """
    Handles the search process for finding feasible scheduling solutions.
    """
    def __init__(self, root: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints):
        self.root = root
        self.hard_constraints = hard_constraints
        self.soft_constraints = soft_constraints
    
    """
    Decides which of the AndTreeNodes children to expand and expands the AndTree Node
    """
    def f_leaf(self, games: List[Game], practices: List[Practice]) -> Union[Game, Practice]:
        
        best_game = Game
        best_practice =  Practice
        
        "Eval is what is used to find score based from the soft constraints"
        for AndTreeNode in self.root.children:
            for game in games:
                if Eval(self, game) > Eval(self, best_game):
                    best_game = game
                elif Eval(self, game) == Eval(self, best_game):
                    best_game = f_select(self, game, best_game)
            for practice in practices:
                if Eval(practice) > Eval(best_practice):
                    best_practice = practice
                elif Eval(practice) == Eval(best_practice):
                    best_practice = f_select(self, practice, best_practice)
        
        if Eval(self, best_game) > Eval(self, best_practice):
            self.root.expand(best_game)
        elif Eval(self, best_game) < Eval(self, best_practice):
            self.root.expand(best_practice)
        else: 
            f_select(self, best_game, best_practice)

class Ftrans:
    def __init__(self, root: AndTreeNode):
        self.root = root # This is the root of the set of leaves

    def f_trans(self) -> AndTreeNode:
        """
        This function makes the transition to the state that has the lowest eval score
        within the current nodes' leaves set
        """
        
        current_state = self.root

        # List of the current state's children
        next_states = self.root.children

        # This takes the state with the lowest eval value
        min_state = min(next_states, key=eval)
            
        # If the child state of the current state has the same eval
        if (eval(min_state) <= eval(current_state)):
            return min_state
    
    
class Fbound:

    def __init__(self, root: AndTreeNode, threshold=0.4):
        self.root = root # This is the root of the set of leaves
        self.threshold = threshold

    def f_bound(self):

        L = self.root.children

        # This is the cutoff of the fbound
        cutoff = math.ceil(len(L) * (1-self.threshold))

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        # If there is only one leaf, then don't delete the first 40%
        if len(L) == 1:
            sorted_L = sorted(L, key=eval, reverse=True)
        else:
            sorted_L = sorted(L, key=eval, reverse=True)[cutoff:]

        return sorted_L