import unittest

from model.weapon import Weapon


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("TestWeapon")

    # def test_add_slot_to_weapon(self):
    #     self.weapon.add_slot_to_weapon("Slot1")
    #     self.assertTrue("Slot1" in self.weapon.slots_to_attachments)
    #     self.assertTrue("Slot2" not in self.weapon.slots_to_attachments)

    def test_add_attachment_to_slot__slot_exists_in_weapon(self):
        self.weapon.add_attachment_to_slot("Attachment1", "Slot1")
        self.assertTrue("Attachment1" in self.weapon.attachments["Slot1"])

    def test_add_attachment_to_slot__slot_does_not_exist_in_weapon(self):
        self.weapon.add_attachment_to_slot("Attachment1", "Slot1")
        self.assertTrue("Attachment1" in self.weapon.attachments["Slot1"])