from typing import List, Tuple
from scheduler_structures import *
from AndTreeNode import *

class SoftConstraints:
    def __init__(self, pen_game_min: int, pen_practice_min: int, w_min_filled: int,
                 slot_pref: List[Tuple[str, str, str, str]], w_pref: int,
                 pair_pref: List[Tuple[str, str]], pen_not_paired: int, w_pair: int,
                 pen_section: int, w_sec_diff: int):
        self.pen_game_min = pen_game_min
        self.pen_practice_min = pen_practice_min
        self.w_min_filled = w_min_filled
        self.slot_pref = slot_pref                  # Should be in the format of (day, start_time, identifier, penalty_if_missed)
        self.w_pref = w_pref
        self.pair_pref = pair_pref                  # Should be the identifiers for the pair
        self.w_pair = w_pair
        self.pen_not_paired = pen_not_paired
        self.pen_section = pen_section
        self.w_sec_diff = w_sec_diff

    def eval(self, node: AndTreeNode):
        return (SoftConstraints.consider_minimum_assignment(node.slots, self.pen_game_min, self.pen_practice_min) * self.w_min_filled +
                SoftConstraints.consider_slot_preference(node.slots, self.slot_pref) * self.w_pref +
                SoftConstraints.consider_pair_preference(node.slots, self.pair_pref, self.pen_not_paired) * self.w_pair +
                SoftConstraints.consider_city_soft_constraints(node.games, self.pen_section) * self.w_sec_diff)
    
    def __repr__(self):
        return (f"SoftConstraints(PenGameMin={self.pen_game_min}, "
                f"penPracticeMin={self.pen_practice_min}, WMinFilled={self.w_min_filled}, "
                f"SlotPref={self.slot_pref}, WPref={self.w_pref}), "
                f"PairPref={self.pair_pref}, WPair={self.w_pair}, "
                f"PenNotPaired={self.pen_not_paired}, PenSection={self.pen_section}, "
                f"WSecDiff={self.w_sec_diff})")

    def consider_minimum_assignment(slots: List[Slot], pen_game_min: int, pen_practice_min: int):
        penalty = 0
        for slot in slots:
            if len(slot.assigned_games) < slot.min_games:
                penalty += pen_game_min * (slot.min_games - len(slot.assigned_games))
            if len(slot.assigned_practices) < slot.min_practices:
                penalty += pen_practice_min * (slot.min_practices - len(slot.assigned_practices))
        return penalty
    
    def consider_slot_preference(slots: List[Slot], slot_pref: List[Tuple[str, str, str, str]]):
        penalty = 0
        for pref in slot_pref:
            for slot in slots:
                if (slot.day == pref[0] and slot.start_time == pref[1] and
                    pref[2] not in slot.assigned_games and pref[2] not in slot.assigned_practices):
                    penalty += int(pref[3])
                    break
        return penalty


    def consider_pair_preference(slots: List[Slot], pair_pref: List[Tuple[str, str]], pen_not_paired: int):
        penalty = 0
        for slot in slots:
            if ((pair_pref[0] in slot.assigned_games or pair_pref[0] in slot.assigned_practices) and
                (pair_pref[1] not in slot.assigned_games and pair_pref[1] not in slot.assigned_practices)):
                penalty += pen_not_paired
        return penalty

    def consider_city_soft_constraints(games: List[Game], pen_section: int):
        return SoftConstraints.consider_city_separate_divisions(games, pen_section)

    def consider_city_separate_divisions(games: List[Game], pen_section: int):
        penalty = 0
        for game in games:
            for other_game in games:
                if (game.identifier == other_game.identifier or
                    game.age_group != other_game.age_group or
                    game.tier != other_game.tier):
                    continue
                if (game.assigned_slot.day == other_game.assigned_slot.day and
                    game.assigned_slot.start_time == other_game.assigned_slot.start_time and
                    game.division != other_game.division):
                    penalty += pen_section
        return penalty