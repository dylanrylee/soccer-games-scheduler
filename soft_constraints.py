from typing import List, Tuple
from prob_set import *
from and_tree_node import AndTreeNode

class SoftConstraints:
    """
    Represents soft constraints used in scheduling games and practices.

    Attributes:
        pen_game_min (int): Penalty for not meeting the minimum number of games in a slot.
        pen_practice_min (int): Penalty for not meeting the minimum number of practices in a slot.
        w_min_filled (int): Weight for penalties related to unfilled slots.
        slot_pref (List[Tuple[str, str, str, str]]): Preferences for specific slots in the format 
            (day, start_time, identifier, penalty_if_missed).
        w_pref (int): Weight for slot preferences.
        pair_pref (List[Tuple[str, str]]): Pairs of identifiers that should be scheduled together.
        pen_not_paired (int): Penalty for failing to schedule preferred pairs together.
        w_pair (int): Weight for pair preferences.
        pen_section (int): Penalty for scheduling games of the same division in the same slot.
        w_sec_diff (int): Weight for penalties related to sectional differences.
    """
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
        """
        Evaluates the soft constraints for a given scheduling node.

        Args:
            node (AndTreeNode): The current node in the scheduling tree containing slots and assignments.

        Returns:
            int: The total penalty value for soft constraint violations.
        """
        val = (SoftConstraints.consider_minimum_assignment(node.slots, self.pen_game_min, self.pen_practice_min) * self.w_min_filled +
                SoftConstraints.consider_slot_preference(node.slots, self.slot_pref) * self.w_pref +
                SoftConstraints.consider_pair_preference(node.slots, self.pair_pref, self.pen_not_paired) * self.w_pair +
                SoftConstraints.consider_city_soft_constraints(node.slots, self.pen_section) * self.w_sec_diff)
        return val
    
    def __repr__(self):
        """
        Returns a string representation of the SoftConstraints object.

        Returns:
            str: A string showing the parameters of the SoftConstraints instance.
        """
        return (f"SoftConstraints(PenGameMin={self.pen_game_min}, "
                f"penPracticeMin={self.pen_practice_min}, WMinFilled={self.w_min_filled}, "
                f"SlotPref={self.slot_pref}, WPref={self.w_pref}), "
                f"PairPref={self.pair_pref}, WPair={self.w_pair}, "
                f"PenNotPaired={self.pen_not_paired}, PenSection={self.pen_section}, "
                f"WSecDiff={self.w_sec_diff})")

    def consider_minimum_assignment(slots: List[Slot], pen_game_min: int, pen_practice_min: int):
        """
        Calculates penalties for not meeting the minimum game or practice requirements.

        Args:
            slots (List[Slot]): List of slots to evaluate.
            pen_game_min (int): Penalty for each missing game.
            pen_practice_min (int): Penalty for each missing practice.

        Returns:
            int: Total penalty for all slots.
        """
        penalty = 0
        for slot in slots:
            if len(slot.assigned_games) < slot.min_games:
                penalty += pen_game_min * (slot.min_games - len(slot.assigned_games))
            if len(slot.assigned_practices) < slot.min_practices:
                penalty += pen_practice_min * (slot.min_practices - len(slot.assigned_practices))
        return penalty
    
    def consider_slot_preference(slots: List[Slot], slot_pref: List[Tuple[str, str, str, str]]):
        """
        Calculates penalties for failing to meet slot preferences.

        Args:
            slots (List[Slot]): List of slots to evaluate.
            slot_pref (List[Tuple[str, str, str, str]]): Slot preferences in the format (day, start_time, identifier, penalty).

        Returns:
            int: Total penalty for slot preference violations.
        """
        penalty = 0
        for pref in slot_pref:
            for slot in slots:
                if (slot.day == pref[0] and slot.start_time == pref[1] and
                    pref[2] not in slot.assigned_games and pref[2] not in slot.assigned_practices):
                    penalty += int(pref[3])
        return penalty


    def consider_pair_preference(slots: List[Slot], pair_pref: List[Tuple[str, str]], pen_not_paired: int):
        """
        Calculates penalties for failing to schedule paired preferences together.

        Args:
            slots (List[Slot]): List of slots to evaluate.
            pair_pref (List[Tuple[str, str]]): Pairs of identifiers that should be scheduled together.
            pen_not_paired (int): Penalty for failing to pair identifiers.

        Returns:
            int: Total penalty for pair preference violations.
        """
        penalty = 0
        for slot in slots:
            for pair in pair_pref: 
                if ((pair[0] in slot.assigned_games or pair[0] in slot.assigned_practices) and
                    (pair[1] not in slot.assigned_games and pair[1] not in slot.assigned_practices)):
                    penalty += pen_not_paired
        return penalty

    def consider_city_soft_constraints(slots: List[Slot], pen_section: int):
        """
        Delegates the evaluation of city-specific constraints.

        Args:
            slots (List[Slot]): List of slots to evaluate.
            pen_section (int): Penalty for violating city-specific constraints.

        Returns:
            int: Total penalty for city constraints violations.
        """
        return SoftConstraints.consider_city_separate_divisions(slots, pen_section)

    def consider_city_separate_divisions(slots: List[Slot], pen_section: int):
        """
        Calculates penalties for scheduling games from the same division in the same slot.

        Args:
            slots (List[Slot]): List of slots to evaluate.
            pen_section (int): Penalty for violating sectional constraints.

        Returns:
            int: Total penalty for sectional constraints violations.
        """
        penalty = 0
        for slot in slots:
            for index, game in enumerate(slot.assigned_games):
                for other_game in slot.assigned_games[index:]:
                    if game != other_game:
                        if game[:10] == other_game[:10]:
                            penalty += pen_section
        return penalty