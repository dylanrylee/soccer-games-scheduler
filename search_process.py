from typing import List, Tuple
from sheduler_structures import *
from hard_constraints import *
from AndTreeNode import *

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

    """
    
    """
    def f_select(self, option_1: Union[Game, Practice],option_2 :Union[Game, Practice]) -> Union[Game, Practice]:
        
        return
    
    
    """
    
    """
    def f_bound(self):

        return