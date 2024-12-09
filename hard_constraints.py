from typing import List, Tuple
from prob_set import Game, Practice, Slot

class HardConstraints:
    def __init__(self, not_compatible: List[Tuple[str, str]],
                 part_assign: List[Tuple[Slot, str]], unwanted: List[Tuple[str, Slot]],
                 debug: bool):
        self.not_compatible = not_compatible        # Both elements of each pair should be game or practice identifiers
        self.part_assign = part_assign              # The pair should include the Slot to enforce, as well as the game or practice identifier string ("$" is ignored).
        self.unwanted = unwanted                    # The pair should include the game or practice identifier string, as well as the Slot to avoid
        self.debug = debug                          # True if you want debug messaging to be printed to the terminal

    def constr(self, slots: List[Slot]):
        val = (HardConstraints.enforce_game_max(slots, self.debug) and
            HardConstraints.enforce_practice_max(slots, self.debug) and
            HardConstraints.enforce_no_simultaneous_assignment(slots, self.debug) and
            HardConstraints.enforce_respect_not_compatible(self.not_compatible, slots, self.debug) and
            HardConstraints.enforce_respect_part_assign(slots, self.part_assign, self.debug) and
            HardConstraints.enforce_respect_unwanted(slots, self.unwanted, self.debug) and
            HardConstraints.enforce_city_hard_constraints(slots, self.debug))
        return val
    
    def __repr__(self):
        return (f"HardConstraints(NotCompatible={self.not_compatible}, "
                f"PartAssign={self.part_assign}, Unwanted={self.unwanted}, "
                f"Debug={self.debug})")

    def enforce_game_max(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_game_max:")
        for slot in slots:
            if (debug):
                print("  " + slot.__repr__())
            if len(slot.assigned_games) > slot.max_games:
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True
    
    def enforce_practice_max(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_practice_max:")
        for slot in slots:
            if (debug):
                print("  " + slot.__repr__())
            if len(slot.assigned_practices) > slot.max_practices:
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True

    def enforce_no_simultaneous_assignment(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_no_simultaneous_assignment:")
        for game_slot in slots:
            if not game_slot.assigned_games:
                continue
            for practice_slot in slots:
                if not practice_slot.assigned_practices:
                    continue
                if (game_slot.day == "MO" and (practice_slot.day != "MO" and practice_slot.day != "FR")) or \
                    (game_slot.day == "MO" and game_slot.start_time != practice_slot.start_time):
                    continue
                if game_slot.day == "TU" and practice_slot.day != "TU":
                    continue
                elif game_slot.start_time == "8:00":
                    if practice_slot.start_time != "8:00" and practice_slot.start_time != "9:00":
                        continue
                elif game_slot.start_time == "9:30":
                    if practice_slot.start_time != "9:00" and practice_slot.start_time != "10:00":
                        continue
                elif game_slot.start_time == "11:00":
                    if practice_slot.start_time != "11:00" and practice_slot.start_time != "12:00":
                        continue
                elif game_slot.start_time == "12:30":
                    if practice_slot.start_time != "12:00" and practice_slot.start_time != "13:00":
                        continue
                elif game_slot.start_time == "14:00":
                    if practice_slot.start_time != "14:00" and practice_slot.start_time != "15:00":
                        continue
                elif game_slot.start_time == "15:30":
                    if practice_slot.start_time != "15:00" and practice_slot.start_time != "16:00":
                        continue
                elif game_slot.start_time == "17:00":
                    if practice_slot.start_time != "17:00" and practice_slot.start_time != "18:00":
                        continue
                elif game_slot.start_time == "18:30":
                    if practice_slot.start_time != "18:00" and practice_slot.start_time != "19:00":
                        continue
                for game in game_slot.assigned_games:
                    for practice in practice_slot.assigned_practices:
                        if "DIV" in practice:
                            if game in practice:
                                return False
                        elif game[:10] in practice:
                            return False
        if (debug):
            print("  True")
        return True
    
    def enforce_respect_not_compatible(not_compatible, slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_respect_not_compatible:")
        for slot in slots:
            if (debug):
                print("  " + slot.__repr__())
            for exclusion in not_compatible:
                if (debug):
                    print("    " + exclusion[0] + ":" + exclusion[1])
                if ((exclusion[0] in slot.assigned_games or exclusion[0] in slot.assigned_practices) and
                    (exclusion[1] in slot.assigned_games or exclusion[1] in slot.assigned_practices)):
                    if (debug):
                        print("      False")
                    return False
        if (debug):
            print("  True")
        return True

    def enforce_respect_part_assign(slots: List[Slot], part_assign: List[Tuple[Slot, str]], debug = False) -> bool:
        if (debug):
            print("enforce_respect_part_assign:")
        for assign in part_assign:
            if (debug):
                print(f"  {assign[0].day},{assign[0].start_time}->{assign[1]}")
            if (assign[1] == "$"):
                continue
            for slot in slots:
                if (debug):
                    print(f"    {slot}")
                if (slot.day == assign[0].day and slot.start_time == assign[0].start_time and
                    assign[1] not in slot.assigned_games and assign[1] not in slot.assigned_practices):
                    return False
        if (debug):
            print("  True")
        return True

    def enforce_respect_unwanted(slots: List[Slot], unwanted: List[Tuple[str, Slot]], debug = False) -> bool:
        if (debug):
            print("enforce_respect_unwanted:")
        for avoid in unwanted:
            if (debug):
                print(f"  {avoid[0]}/>{avoid[1].day},{avoid[1].start_time}")
            for slot in slots:
                if (debug):
                    print(f"    {slot}")
                if (slot.day == avoid[1].day and slot.start_time == avoid[1].start_time and
                    (avoid[0] in slot.assigned_games or avoid[0] in slot.assigned_practices)):
                    if (debug):
                        print("      False")
                    return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_hard_constraints(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("")
        val = (HardConstraints.enforce_city_abstract_slots(slots, debug) and
                HardConstraints.enforce_city_evening_division_assignment(slots, debug) and
                HardConstraints.enforce_city_avoid_overlap(slots, debug) and
                HardConstraints.enforce_city_admin_meeting(slots, debug) and
                HardConstraints.enforce_city_tryout_bookings(slots, debug))
        return val
    
    def enforce_city_abstract_slots(slots: List[Slot], debug: bool):
        if (debug):
            print("enforce_city_abstract_slots")
        for slot in slots:
            if (debug):
                print(f"  {slot}")
            if slot.day not in ["MO", "TU", "FR"]:
                if (debug):
                    print("    False")
                return False
            if slot.day == "FR" and len(slot.assigned_games) > 0:
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_evening_division_assignment(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_evening_division_assignment")
        for slot in slots:
            if ((slot.day == "MO" and slot.start_time not in ["18:00", "19:00", "20:00"]) or
                (slot.day == "TU" and slot.start_time != "18:30")):
                for game in slot.assigned_games:
                    if "DIV 9" in game:
                        if debug:
                            print("  False")
                        return False
            if ((slot.day in ["MO", "TU"] and slot.start_time not in ["18:00", "19:00", "20:00"]) or
                (slot.day == "FR" and slot.start_time != "18:00")):
                for practice in slot.assigned_practices:
                    if "DIV 9" in practice:
                        if debug:
                            print("  False")
                        return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_avoid_overlap(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_city_avoid_overlap")
        for slot in slots:
            for game in slot.assigned_games:
                if "U15" not in game and "U16" not in game and "U17" not in game and "U19" not in game:
                    continue
                for other_game in slot.assigned_games:
                    if (game != other_game and 
                        (("U15" in game and "U15" in other_game) or ("U16" in game and "U16" in other_game) or
                         ("U17" in game and "U17" in other_game) or ("U19" in game and "U19" in other_game))):
                        return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_admin_meeting(slots: List[Slot], debug = False):
        if (debug):
            print("enforce_city_admin_meeting")
        for slot in slots:
            if slot.day == "TU" and slot.start_time == "11:00" and len(slot.assigned_games) != 0:
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_tryout_bookings(slots: List[Slot], debug = False) -> bool:
        if (debug):
            print("enforce_city_tryout_bookings")
        for slot in slots:
            if slot.day == "TU" and (slot.start_time == "17:00" or slot.start_time == "18:30"):
                for game in slot.assigned_games:
                    if "CMSA U12T1" in game:
                        return False
                    if "CMSA U13T1" in game:
                        return False
            if slot.day == "TU" and slot.start_time == "18:00":
                for practice in slot.assigned_practices:
                    if "CMSA U12T1" in practice and "CMSA U12T1S" not in practice:
                        return False
                    if "CMSA U13T1" in practice and "CMSA U13T1S" not in practice:
                        return False
        return True