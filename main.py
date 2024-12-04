from scheduler_structures import *
from hard_constraints import *
from soft_constraints import *
from AndTreeNode import *
from search_process import *
from typing import Dict, Tuple
import sys


class Main:
    def __init__(self):
        self.slots: List[Slot] = []
        self.games: List[Game] = []
        self.practices: List[Practice] = []
        self.not_compatible: List[Tuple[str, str]] = []
        self.unwanted: List[Tuple[str, Slot]] =[]
        self.slot_preferences: List[Tuple[str, str, str, str]] = []
        self.pairs: List[Tuple[str, str]] = []
        self.partial_assignments: Dict[str, Slot] = {}

    def add_game_slot(self, slot: Slot):
        self.slots.append(slot)

    def add_practice_slot(self, slot: Slot):
        for check in self.slots:
            if check.day == slot.day and check.start_time == slot.start_time:
                check.max_practices = slot.max_practices
                check.min_practices = slot.min_practices
                return
        self.slots.append(slot)

    def add_game(self, game: Game):
        self.games.append(game)

    def add_practice(self, practice: Practice):
        self.practices.append(practice)

    def add_not_compatible(self, not_compatible: Tuple[str, str]):
        self.not_compatible.append(not_compatible)

    def add_unwanted(self, unwanted: Tuple[str, Slot]):
        self.unwanted.append(unwanted)

    def add_slot_preferences(self, slot_pref: Tuple[str, str, str, str]):
        self.slot_preferences.append(slot_pref)

    def add_pair(self, pair: Tuple[str, str]):
        self.pairs.append(pair)

    def add_partial_assignment(self, identifier: str, slot: Slot):
        self.partial_assignments[identifier] = slot

    def assign_games_to_slots(self):
        for game in self.games:
            for slot in self.slots:
                if game.assign_slot(slot):
                    print(f"Assigned {game.identifier} to slot.")
                    break
            else:
                print(f"Failed to assign {game.identifier} to any slot.")

    def assign_practices_to_slots(self):
        for practice in self.practices:
            for slot in self.slots:
                if practice.assign_slot(slot):
                    print(f"Assigned {practice.identifier} to slot.")
                    break
            else:
                print(f"Failed to assign {practice.identifier} to any slot.")
                
    def find_slot(self, day: str, start_time: str):
        for slot in self.slots:
            if slot.day == day and slot.start_time == start_time:
                return slot
        return Slot(day, start_time, 0, 0, 0, 0)

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def parse_sections(content: str):
    sections = content.split('\n\n')
    parsed_data = {}
    for section in sections:
        lines = section.split('\n')
        header = lines[0].strip(':')
        data = lines[1:]
        parsed_data[header] = data
    return parsed_data

# Example usage
if __name__ == "__main__":

    # Take in the command line arguments
    file_name = sys.argv[1]
    w_min_filled = sys.argv[2]
    w_pref = sys.argv[3]
    w_pair = sys.argv[4]
    w_sec_diff = sys.argv[5]
    pen_game_min = sys.argv[6]
    pen_practice_min = sys.argv[7]
    pen_not_paired = sys.argv[8]
    pen_section = sys.argv[9]

    # Read the file content
    file_content = read_file(file_name)

    # Parse the sections
    parsed_data = parse_sections(file_content)

    # Create Main object
    main = Main()

   # Create GameSlot objects from input strings and add them to Main
    for input_string in parsed_data['Game slots']:
        day, time, max_games, min_games = input_string.replace(",", "").split()
        slot = Slot(day, time, int(max_games), int(min_games), 0, 0)
        main.add_game_slot(slot)

    # Create PracticeSlot objects from input strings and add them to Main
    for input_string in parsed_data['Practice slots']:
        day, time, max_practices, min_practices = input_string.replace(",", "").split()
        slot = Slot(day, time, 0, 0, int(max_practices), int(min_practices))
        main.add_practice_slot(slot)

    # Create Game objects from input strings and add them to Main
    for input_string in parsed_data['Games']:
        values = input_string.split()
        game = Game(input_string, values[0], values[1][:3], values[1][3:], values[2] + " " + values[3])
        main.add_game(game)

    # Create Practice objects from input strings and add them to Main
    for input_string in parsed_data['Practices']:
        # practice = Practice.from_string(input_string)
        values = input_string.split()
        practice = Practice(input_string, f"{values[0]} {values[1]} {values[2]} {values[3]}", "")
        main.add_practice(practice)

    # Add incompatible pairs to Main
    for input_string in parsed_data['Not compatible']:
        values = input_string.split(",")
        values[1] = values[1].lstrip()
        not_com = tuple(values)
        # print(not_com)
        main.add_not_compatible(not_com)

    # print("Unwanted")
    # Add unwanted pairs to Main
    for input_string in parsed_data['Unwanted']:
        values = input_string.split(",")
        values[1] = values[1].lstrip()
        values[2] = values[2].lstrip()
        slot = main.find_slot(values[1], values[2])
        pair = (values[0], slot)
        # print(pair)
        main.add_unwanted(pair)
        
    # print("Slot preferences")
    # Add slot preferences to Main
    for input_string in parsed_data['Preferences']:
        values = input_string.split(",")
        values[1] = values[1].lstrip()
        values[2] = values[2].lstrip()
        values[3] = values[3].lstrip()
        slot_pref = tuple(values)
        # print(slot_pref)
        main.add_slot_preferences(slot_pref)

    # print("Pair preferences")
    # Add pair preferences to Main
    for input_string in parsed_data['Pair']:
        values = input_string.split(",")
        values[1] = values[1].lstrip()
        pair = tuple(values)
        # print(pair)
        main.add_pair(pair)

    # Add partial assignments to Main
    for input_string in parsed_data['Partial assignments']:
        values = input_string.split(",")
        identifier = values[0]
        day = values[1].lstrip()
        start_time = values[2].lstrip()
        slot = main.find_slot(day, start_time)
        main.add_partial_assignment(identifier, slot)
    
    hard_constraints = HardConstraints(main.not_compatible, main.partial_assignments,
                                       main.unwanted, False)
    soft_constraints = SoftConstraints(pen_game_min, pen_practice_min, w_min_filled,
                                       main.slot_preferences, w_pref, main.pairs,
                                       pen_not_paired, w_pair, pen_section, w_sec_diff)
    
    # print(hard_constraints)
    # print("\n\n")
    # print(soft_constraints)
    
    # root_node = AndTreeNode(main.slots, main.games, main.practices, 0)
    # search_process = SearchProcess(root_node, hard_constraints, soft_constraints)

    # Assign games and practices to slots
    # main.assign_games_to_slots()
    # main.assign_practices_to_slots()
