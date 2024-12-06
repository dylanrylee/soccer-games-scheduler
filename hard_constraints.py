from typing import List, Tuple
from scheduler_structures import Game, Practice, Slot

class HardConstraints:
    def __init__(self, not_compatible: List[Tuple[str, str]],
                 part_assign: List[Tuple[Slot, str]], unwanted: List[Tuple[str, Slot]],
                 debug: bool):
        self.not_compatible = not_compatible        # Both elements of each pair should be game or practice identifiers
        self.part_assign = part_assign              # The pair should include the Slot to enforce, as well as the game or practice identifier string ("$" is ignored).
        self.unwanted = unwanted                    # The pair should include the game or practice identifier string, as well as the Slot to avoid
        self.debug = debug                          # True if you want debug messaging to be printed to the terminal

    def constr(self, games: List[Game], practices: List[Practice], slots: List[Slot]):
        val = (HardConstraints.enforce_game_max(slots, self.debug) and
            HardConstraints.enforce_practice_max(slots, self.debug) and
            HardConstraints.enforce_no_simultaneous_assignment(games, practices, self.debug) and
            HardConstraints.enforce_respect_not_compatible(self.not_compatible, slots, self.debug) and
            HardConstraints.enforce_respect_part_assign(slots, self.part_assign, self.debug) and
            HardConstraints.enforce_respect_unwanted(slots, self.unwanted, self.debug) and
            HardConstraints.enforce_city_hard_constraints(slots, games, practices, self.debug))
        # print(val)
        return val
    
    def __repr__(self):
        return (f"HardConstraints(NotCompatible={self.not_compatible}, "
                f"PartAssign={self.part_assign}, Unwanted={self.unwanted}, "
                f"Debug={self.debug})")

    def enforce_game_max(slots: List[Slot], debug = False):
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
    
    def enforce_practice_max(slots: List[Slot], debug = False):
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
    
    def enforce_no_simultaneous_assignment(games: List[Game], practices: List[Practice], debug = False):
        if (debug):
            print("enforce_no_simultaneous_assignment:")
        for game in games:
            if (debug):
                print("  " + game.__repr__())
            for practice in practices:
                if (debug):
                    print("    " + practice.__repr__())
                if (game.assigned_slot != None and practice.assigned_slot != None and
                    game.identifier == practice.associated_game and game.assigned_slot == practice.assigned_slot):
                    if (debug):
                        print("      False")
                    return False
        if (debug):
            print("  True")
        return True
    
    def enforce_respect_not_compatible(not_compatible, slots: List[Slot], debug = False):
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

    def enforce_respect_part_assign(slots: List[Slot], part_assign: List[Tuple[Slot, str]], debug = False):
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

    def enforce_respect_unwanted(slots: List[Slot], unwanted: List[Tuple[str, Slot]], debug = False):
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
    
    def enforce_city_hard_constraints(slots: List[Slot], games: List[Game], practices: List[Practice], debug = False):
        if (debug):
            print("")
        return (HardConstraints.enforce_city_abstract_slots(slots, debug) and
                HardConstraints.enforce_city_evening_division_assignment(games, practices, debug) and
                HardConstraints.enforce_city_avoid_overlap(games, debug) and
                HardConstraints.enforce_city_admin_meeting(games, debug) and
                HardConstraints.enforce_city_tryout_bookings(games, practices, debug))
    
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
    
    def enforce_city_evening_division_assignment(games: List[Game], practices: List[Practice], debug = False):
        if (debug):
            print("enforce_evening_division_assignment")
        for game in games:
            if (debug):
                print(f"  {game}")
            if "DIV 9" not in game.division or game.assigned_slot == None:
                continue
            if game.assigned_slot.day == "MO" and game.assigned_slot.start_time not in ["18:00", "19:00", "20:00"]:
                if (debug):
                    print("    False")
                return False
            if game.assigned_slot.day == "TU" and game.assigned_slot.start_time != "18:30":
                if (debug):
                    print("    False")
                return False
        for practice in practices:
            if (debug):
                print(f"  {practice}")
            evening_div = False
            for game in games:
                if (debug):
                    print(f"    {game}")
                if (game.identifier == practice.associated_game):
                    evening_div = "DIV 9" in game.division
                    break
            if (evening_div == False or practice.assigned_slot == None):
                continue
            if practice.assigned_slot.day in ["MO", "TU"] and practice.assigned_slot.start_time not in ["18:00", "19:00", "20:00"]:
                if (debug):
                    print("    False")
                return False
            if practice.assigned_slot.day == "FR" and practice.assigned_slot.start_time != "18:00":
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_avoid_overlap(games: List[Game], debug = False):
        if (debug):
            print("enforce_city_avoid_overlap")
        for game in games:
            if (debug):
                print(f"  {game}")
            if game.division not in ["U15", "U16", "U17", "U19"]:
                continue
            for other_game in games:
                if (debug):
                    print(f"    {other_game}")
                if (game.identifier == other_game.identifier or
                    game.assigned_slot.day != other_game.assigned_slot.day or
                    game.assigned_slot.start_time != other_game.assigned_slot.start_time):
                    continue
                if other_game.division in ["U15", "U16", "U17", "U19"]:
                    if (debug):
                        print("      False")
                    return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_admin_meeting(games: List[Game], debug = False):
        if (debug):
            print("enforce_city_admin_meeting")
        for game in games:
            if (debug):
                print(f"  {game}")
            if game.assigned_slot != None and game.assigned_slot.day == "TU" and game.assigned_slot.start_time == "11:00":
                if (debug):
                    print("    False")
                return False
        if (debug):
            print("  True")
        return True
    
    def enforce_city_tryout_bookings(games: List[Game], practices: List[Practice], debug = False):
        if (debug):
            print("enforce_city_tryout_bookings")
        u12_id = ""
        u13_id = ""
        u12_tryout_id = ""
        u13_tryout_id = ""
        for game in games:
            if game.assigned_slot == None:
                continue
            if game.tier == "T1S" and game.league == "CMSA" and game.age_group == "U12":
                if game.assigned_slot.day != "TU" or game.assigned_slot.start_time != "18:00":
                    return False
                u12_tryout_id = game.identifier
                continue
            if game.tier == "T1S" and game.league == "CMSA" and game.age_group == "U13":
                if game.assigned_slot.day != "TU" or game.assigned_slot.start_time != "18:00":
                    return False
                u13_tryout_id = game.identifier
                continue
            if game.tier == "T1" and game.league == "CMSA" and game.age_group == "U12":
                if game.assigned_slot.day == "TU" or game.assigned_slot.start_time == "18:00":
                    u12_id = game.identifier
                continue
            if game.tier == "T1" and game.league == "CMSA" and game.age_group == "U13":
                if game.assigned_slot.day == "TU" or game.assigned_slot.start_time == "18:00":
                    u13_id = game.identifier
                continue
        if (u12_tryout_id != "" and u12_id != "") or (u13_tryout_id != "" and u13_id != ""):
            return False
        for practice in practices:
            if ((practice.associated_game == u12_id or practice.associated_game == u12_tryout_id or
                practice.associated_game == u13_id or practice.associated_game == u13_tryout_id) and
                (practice.assigned_slot != None and
                 practice.assigned_slot.start_time == "18:00" and practice.assigned_slot.day == "TU")):
                return False
        return True