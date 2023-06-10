import unittest

from model.generator import RandomClassGenerator


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self.generator = RandomClassGenerator()

    def test_add_weapon(self):
        self.generator.add_weapon("M16")
        self.assertTrue("M16" in self.generator.weapons)

    def test_generate_random_class(self):


    # def test_get_random_weapon(self):
    #     random_weapon = self.generator.get_random_weapon()
    #     self.assertEqual("Weapon1", random_weapon)
