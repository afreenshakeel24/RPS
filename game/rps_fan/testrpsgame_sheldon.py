# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import unittest
import rpsgame_sheldon

def setUp_class(Testrpsgame_sheldon):
    self.a = rpsgame_sheldon.rpsgame_sheldon()
    self.b = rpsgame_sheldon.rpsgame_sheldon()
def tearDown_class(Testrpsgame_sheldon):
    self.a = None
    self.b = None

class Testrpsgame_sheldon(unittest.TestCase): # test class
    def setUp(self):
        self.a = rpsgame_sheldon.rpsgame_sheldon()
        self.b = rpsgame_sheldon.rpsgame_sheldon()
    def tearDown(self):
        self.a = None
        self.b = None
    def test_display(self):
        a1 = self.a.display()
        b1 = self.b.display()
        self.assertNotEqual(self.a.display() , '')
        self.assertIsInstance(self.a, rpsgame_sheldon.rpsgame_sheldon)
        self.assertIs(a1, b1)
    def test_game_rps_sheldon(self):
        c1 = self.a.game_rps_sheldon
        d1 = self.b.game_rps_sheldon
        self.assertIsNotNone(c1)
        self.assertIsNotNone(d1)        
    def test_sheldonmodel(self):
        self.assertIn('Rock', self.a.models)
        self.assertIn('Lizard', self.a.models)
        self.assertIn('Scissors', self.a.models)
        self.assertIn('Spock', self.a.models)
        
unittest.main(argv=[''], verbosity=2, exit=False)
# -


