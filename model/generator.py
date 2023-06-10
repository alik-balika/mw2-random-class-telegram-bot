import random

from model.weapon import Weapon
from model.data import *

class RandomClassGenerator:
    def __init__(self):
        self.weapons = {}
        self.primary_weapon = ""
        self.secondary_weapon = ""
        self.primary_attachments = []
        self.secondary_attachments = []
        self.tactical = ""
        self.lethal = ""
        self.perks = []
        self.fieldUpgrades = []
        self.killStreaks = []

    def add_weapon(self, weapon_name):
        if weapon_name not in self.weapons:
            self.weapons[weapon_name] = Weapon(weapon_name)

    def get_weapon(self, weapon_name):
        return self.weapons[weapon_name]

    def generate_random_class(self):
        self.randomize_perks()
        self.randomize_tactical()
        self.randomize_lethal()
        self.randomize_field_upgrades()
        self.randomize_kill_streaks()

    def randomize_perks(self):
        base_perks = all_perks["base"].copy()
        bonus_perks = all_perks["bonus"].copy()
        ultimate_perks = all_perks["ultimate"].copy()

        self._add_perk_to_perks(base_perks)
        self._add_perk_to_perks(base_perks)
        self._add_perk_to_perks(bonus_perks)
        self._add_perk_to_perks(ultimate_perks)

    def _add_perk_to_perks(self, perks_list):
        random_index = random.randint(0, len(perks_list) - 1)
        self.perks.append(perks_list[random_index])
        del perks_list[random_index]

    def randomize_tactical(self):
        pass

    def randomize_lethal(self):
        pass

    def randomize_field_upgrades(self):
        pass

    def randomize_kill_streaks(self):
        pass

    def randomize_weapon(self):
        pass

    def randomize_attachments(self, weapon):
        pass
