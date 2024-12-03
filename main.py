from scheduler_structures import *
from typing import Dict, Tuple


class Main:
    def __init__(self):
        self.game_slots: List[Slot] = []
        self.practice_slots: List[Slot] = []
        self.games: List[Game] = []
        self.practices: List[Practice] = []
        self.pairs: List[Tuple[str, str]] = []
        self.partial_assignments: Dict[str, Slot] = {}

    def add_game_slot(self, slot: Slot):
        self.game_slots.append(slot)

    def add_practice_slot(self, slot: Slot):
        self.practice_slots.append(slot)

    def add_game(self, game: Game):
        self.games.append(game)

    def add_practice(self, practice: Practice):
        self.practices.append(practice)

    def add_pair(self, pair: Tuple[str, str]):
        self.pairs.append(pair)

    def add_partial_assignment(self, identifier: str, slot: Slot):
        self.partial_assignments[identifier] = slot

    def assign_games_to_slots(self):
        for game in self.games:
            for slot in self.game_slots:
                if game.assign_slot(slot):
                    print(f"Assigned {game.identifier} to slot.")
                    break
            else:
                print(f"Failed to assign {game.identifier} to any slot.")

    def assign_practices_to_slots(self):
        for practice in self.practices:
            for slot in self.practice_slots:
                if practice.assign_slot(slot):
                    print(f"Assigned {practice.identifier} to slot.")
                    break
            else:
                print(f"Failed to assign {practice.identifier} to any slot.")

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

    # Read the file content
    file_content = read_file('C:/Users/dylan/OneDrive/Desktop/AIProject/CPSC433F24-LargeInput1.txt')

    # Parse the sections
    parsed_data = parse_sections(file_content)

    # Create Main object
    main = Main()

   # Create GameSlot objects from input strings and add them to Main
    for input_string in parsed_data['Game slots']:
        day, time, max_games, max_practices = input_string.split(", ")
        slot = Slot(day, time, int(max_games), int(max_practices))
        main.add_game_slot(slot)

    # Create PracticeSlot objects from input strings and add them to Main
    for input_string in parsed_data['Practice slots']:
        day, time, max_games, max_practices = input_string.split(", ")
        slot = Slot(day, time, int(max_games), int(max_practices))
        main.add_practice_slot(slot)

    # Create Game objects from input strings and add them to Main
    for input_string in parsed_data['Games']:
        game = Game.from_string(input_string)
        main.add_game(game)

    # Create Practice objects from input strings and add them to Main
    for input_string in parsed_data['Practices']:
        practice = Practice.from_string(input_string)
        main.add_practice(practice)

    # Add pairs to Main
    for input_string in parsed_data['Pairs']:
        pair = tuple(input_string.split(", "))
        main.add_pair(pair)

    # Add partial assignments to Main
    for input_string in parsed_data['Partial assignments']:
        identifier, slot_info = input_string.split(", ")
        day, time, max_games, max_practices = slot_info.split(", ")
        slot = Slot(day, time, int(max_games), int(max_practices))
        main.add_partial_assignment(identifier, slot)


    # Assign games and practices to slots
    main.assign_games_to_slots()
    main.assign_practices_to_slots()

