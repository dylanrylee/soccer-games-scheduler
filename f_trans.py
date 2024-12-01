from AndTreeNode import *
from scheduler_structures import *
from search_process import *

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

# Delete this when the soft constraints class is done
def eval():
    return