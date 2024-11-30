from typing import List
import math
from sheduler_structures import *


class Fbound:

    def __init__(self, L: List[Slot], threshold=0.4):
        self.L = L # This is the set of leaves
        self.threshold = threshold

    def f_bound(self):

        # This is the cutoff of the fbound
        cutoff = math.ceil(len(self.f_boundL) * (1-self.threshold))

        # this sorts the leaves by their evaluation function value, in reverse order.
        # So Eval(l_1) >= ... >= Eval(l_n)
        # Then we are deleting the first 40% of L, so only return the next 60%
        sorted_L = sorted(self.L, key=eval_func, reverse=True)[cutoff:]

        return sorted_L

# delete this when you have access to the soft constraints file
def eval_func():
    return 