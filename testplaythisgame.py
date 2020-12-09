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
import playthisgame

def setUp_class(Testplaythisgame):
    self.a = playthisgame.Maingame()
    self.b = playthisgame.Maingame()
def tearDown_class(Testplaythisgame):
    self.a = None
    self.b = None

class Testplaythisgame(unittest.TestCase):# test class
    def setUp(self):
        self.a = playthisgame.Maingame()
        self.b = playthisgame.Maingame()
    def tearDown(self):
        self.a = None
        self.b = None
    def test_game(self):
        a = playthisgame.Maingame()
        self.assertNotIn('Rock', self.a.models)
        self.assertNotIn('Lizard', self.a.models)
        self.assertNotIn('Scissors', self.a.models)
        self.assertNotIn('Spock', self.a.models)
        self.assertNotIn('Paper', self.a.models)     
    def test_display(self):
        a1 = self.a.display()
        b1 = self.b.display()
        self.assertNotEqual(self.a.display , '')
        self.assertIsInstance(self.a, playthisgame.Maingame)
        self.assertIsInstance(self.b, playthisgame.Maingame)
        self.assertEqual(a1, b1)
        
unittest.main(argv=[''], verbosity=2, exit=False)
# -


