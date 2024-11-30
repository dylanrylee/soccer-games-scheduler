from typing import List
import math
from sheduler_structures import *
from AndTreeNode import *


class Fbound:

    def __init__(self, root: AndTreeNode, threshold=0.4):
        self.root = root # This is the of the set of leaves
        self.threshold = threshold

    def f_bound(self):

        L = self.root.children

        # This is the cutoff of the fbound
        cutoff = math.ceil(len(L) * (1-self.threshold))

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        sorted_L = sorted(L, key=eval, reverse=True)[cutoff:]

        return sorted_L

# delete this when you have access to the soft constraints file
def eval():
    return 