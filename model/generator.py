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
        self.field_upgrades = []
        self.kill_streaks = {}

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
        random_index = random.randint(0, len(all_tacticals) - 1)
        self.tactical = all_tacticals[random_index]

    def randomize_lethal(self):
        random_index = random.randint(0, len(all_lethals) - 1)
        self.lethal = all_lethals[random_index]

    def randomize_field_upgrades(self):
        field_upgrades = all_field_upgrades.copy()
        self._add_field_upgrade_to_field_upgrades(field_upgrades)
        self._add_field_upgrade_to_field_upgrades(field_upgrades)

    def _add_field_upgrade_to_field_upgrades(self, field_upgrades):
        random_index = random.randint(0, len(field_upgrades) - 1)
        self.field_upgrades.append(field_upgrades[random_index])
        del field_upgrades[random_index]

    def randomize_kill_streaks(self):
        kill_streaks = all_kill_streaks.copy()
        self._add_kill_streak_to_kill_streaks(kill_streaks)
        self._add_kill_streak_to_kill_streaks(kill_streaks)
        self._add_kill_streak_to_kill_streaks(kill_streaks)

        self.kill_streaks = dict(sorted(
            self.kill_streaks.items(),
            key=lambda item: item[1]))

    def _add_kill_streak_to_kill_streaks(self, kill_streaks):
        streak = random.choice(list(kill_streaks.keys()))
        kills = kill_streaks[streak]
        self.kill_streaks[streak] = kills

        self._delete_kill_streaks_that_have_same_number_of_kills(kills, kill_streaks)

    def _delete_kill_streaks_that_have_same_number_of_kills(self, kills, kill_streaks):
        keys_to_delete = []
        for key, value in kill_streaks.items():
            if value == kills:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del kill_streaks[key]

    def randomize_weapon(self):
        pass

    def randomize_attachments(self, weapon):
        pass

    def clear(self):
        self.primary_weapon = ""
        self.secondary_weapon = ""
        self.primary_attachments = []
        self.secondary_attachments = []
        self.tactical = ""
        self.lethal = ""
        self.perks = []
        self.field_upgrades = []
        self.kill_streaks = {}
