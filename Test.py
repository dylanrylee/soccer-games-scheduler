from typing import List, Tuple
from sheduler_structures import *
from hard_constraints import *
from AndTreeNode import AndTreeNode
from search_instance import SearchInstance
from search_process import SearchProcess

# Define slots, games, practices, and constraints
slots = [Slot("MO", "10:00", 3, 1, 2, 1), Slot("TU", "14:00", 2, 1, 1, 0)]
games = [Game("G1", "CMSA", "U12", "T1", "DIV 9"), Game("G2", "CMSA", "U13", "T1", "DIV 9")]
practices = [Practice("P1", "G1", "Regular"), Practice("P2", "G2", "Special")]

constraints = HardConstraints(games, practices, slots, [], [], [], debug=True)

# Create initial state and search process
root_node = AndTreeNode(slots, games, practices, 0)
search_instance = SearchInstance(slots, games, practices, constraints)
search_process = SearchProcess(root_node, constraints)

# Start the search
search_process.depth_first_search()
