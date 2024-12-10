from typing import List, Dict
from hard_constraints import *
from soft_constraints import *
from and_tree_node import *
from search_process import *
import re
import sys

def parse_input(file_path: str) -> Tuple[List[Slot], List[Game], List[Practice], Dict[str, List]]:
    """
    Parses the input file to extract game slots, practice slots, games, practices, and constraints.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize containers
    slots = []
    games = []
    practices = []
    not_compatible = []
    unwanted = []
    pair = []
    part_assign = []
    preferences = []

    # Parse the file
    section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Identify sections
        if line.startswith("Game slots:"):
            section = "game_slots"
            continue
        elif line.startswith("Practice slots:"):
            section = "practice_slots"
            continue
        elif line.startswith("Games:"):
            section = "games"
            continue
        elif line.startswith("Practices:"):
            section = "practices"
            continue
        elif line.startswith("Not compatible:"):
            section = "not_compatible"
            continue
        elif line.startswith("Unwanted:"):
            section = "unwanted"
            continue
        elif line.startswith("Pair:"):
            section = "pair"
            continue
        elif line.startswith("Partial assignments:"):
            section = "partial_assignments"
            continue
        elif line.startswith("Preferences:"):
            section = "preferences"
            continue

        # Parse each section
        if section == "game_slots":
            day, time, max_games, min_games = line.split(", ")[:4]
            slots.append(Slot(day, time, int(max_games), int(min_games), 0, 0))
        elif section == "practice_slots":
            day, time, max_practices, min_practices = line.split(", ")
            slots.append(Slot(day, time, 0, 0, int(max_practices), int(min_practices)))
        elif section == "games":
            split = line.split()
            league = split[0]
            age = split[1][:3]
            tier = split[1][3:]
            division = f"{split[2]} {split[3]}"
            games.append(Game(line, league, age, tier, division))
            if league == "CMSA" and age == "U12" and tier == "T1":
                for slot in slots:
                    if slot.day == "TU" and slot.start_time == "18:00":
                        slot.assigned_practices.append("CMSA U12T1S")
            elif league == "CMSA" and age == "U13" and tier == "T1":
                for slot in slots:
                    if slot.day == "TU" and slot.start_time == "18:00":
                        slot.assigned_practices.append("CMSA U13T1S")
        elif section == "practices":
            # Parse practice ID
            match = re.match(r"^(.*) (PRC|OPN) \d+$", line)
            if match:
                game_id = match.group(1)
                practice_id = line
                # Find or create the corresponding game
                if "DIV" in game_id:
                    game = next((g for g in games if g.identifier == game_id), None)
                    if game:
                        practice = Practice(practice_id, game, match.group(2))  
                        game.practices.append(practice)
                        practices.append(practice)
                else:
                    practice = Practice(practice_id, Game(game_id, "", "", "", ""), match.group(2))
                    practices.append(practice)
        elif section == "not_compatible":
            items = line.split(", ")[:2]
            not_compatible.append((items[0], items[1]))
        elif section == "unwanted":
            parts = line.split(", ")[:3]
            identifier = parts[0]
            day = parts[1]
            time = parts[2]
            unwanted.append((identifier, Slot(day, time, 0, 0, 0, 0)))
        elif section == "pair":
            split = line.split(", ")[:2]
            first = split[0]
            second = split[1]
            pair.append((first, second))
        elif section == "partial_assignments":
            split = line.split(", ")
            identifier = split[0]
            day = split[1]
            time = split[2]
            part_assign.append((Slot(day, time, 0, 0, 0, 0), identifier))
        elif section == "preferences":
            split = line.split(", ")[:4]
            preferences.append([split[0], split[1], split[2], split[3]])

    constraints = {
        "not_compatible": not_compatible,
        "unwanted": unwanted,
        "pair": pair,
        "preferences": preferences,
        "part_assign": part_assign
    }
    return slots, games, practices, constraints

# Recursively explore the tree, depth first
def TraverseTree(current_node: AndTreeNode, hard_constraints: HardConstraints, soft_constraints: SoftConstraints) -> List[AndTreeNode]:
    # Initialize empty lists
    completed_schedules: List[AndTreeNode] = []
    unchecked_leaves: List[AndTreeNode] = []

    # Generate valid child nodes, checking against hard constraints
    current_node.expand(constrained_expansion_logic, hard_constraints)
    
    # If none were generated, check to see if this is a full schedule. If so, return it
    if not current_node.children:
        if (len(current_node.get_remaining_games()) == 0
            and len(current_node.get_remaining_practices()) == 0):
            return [current_node]
        else:
            return []
    # If children were generated, iterate over the children
    else:
        for child in current_node.children:
            unchecked_leaves.append(child)

    # Sort the leaves by eval
    filtered_leaves = sorted(unchecked_leaves, key=soft_constraints.eval, reverse=True)
    # Recursively explore the sorted list, sorted by lowest penalty first
    for leaf in filtered_leaves:
        for schedule in TraverseTree(leaf, hard_constraints, soft_constraints):
            completed_schedules.append(schedule)

    return completed_schedules

# If a full schedule exists, display the best one. Otherwise, declare there is no valid solution
def PrintBestSchedule(completed_schedules: List[AndTreeNode], soft_constraints: SoftConstraints):
    if completed_schedules:
        best_schedule = min(completed_schedules, key=soft_constraints.eval)

        # Print games and practices schedule by iterating through slots
        print("Eval:", soft_constraints.eval(best_schedule))

        # Iterate over all slots in the best schedule
        output_list: List[str] = []
        for slot in best_schedule.slots:
            # Check if there are any games assigned to the slot
            if slot.assigned_games:
                for game in slot.assigned_games:
                    # Print the game assigned to this slot
                    output_list.append(f"{game}             : {slot.day}, {slot.start_time}")
                    
            if slot.assigned_practices:
                for practice in slot.assigned_practices:
                    buffer = " " * (30 - len(practice))
                    output_list.append(f"{practice}{buffer}: {slot.day}, {slot.start_time}")

        grr = sorted(output_list)

        for elem in grr:
            print(elem)
    else:
        print("No valid solution")

# Start the program
if __name__ == "__main__":

    file_path = sys.argv[1]
    w_min_filled = sys.argv[2]
    w_pref = sys.argv[3]
    w_pair = sys.argv[4]
    w_sec_diff = sys.argv[5]
    pen_game_min = sys.argv[6]
    pen_practice_min = sys.argv[7]
    pen_not_paired = sys.argv[8]
    pen_section = sys.argv[9]
    
    # Parse the file
    slots, games, practices, constraints = parse_input(file_path)

    # Initialize hard constraints
    hard_constraints = HardConstraints(
        not_compatible=constraints["not_compatible"],
        part_assign=constraints["part_assign"],
        unwanted=constraints["unwanted"],
        debug=False
    )

    # SoftConstraints
    soft_constraints = SoftConstraints(
        pen_game_min=int(pen_game_min),
        pen_practice_min=int(pen_practice_min),
        w_min_filled=int(w_min_filled),
        slot_pref=constraints["preferences"],
        w_pref=int(w_pref),
        pair_pref=constraints["pair"],
        pen_not_paired=int(pen_not_paired),
        w_pair=int(w_pair),
        pen_section=int(pen_section),
        w_sec_diff=int(w_sec_diff)
    )

    # Create the root node
    current_node = AndTreeNode(slots=slots, games=games, practices=practices)

    completed_schedules = TraverseTree(current_node, hard_constraints, soft_constraints)

    PrintBestSchedule(completed_schedules, soft_constraints)