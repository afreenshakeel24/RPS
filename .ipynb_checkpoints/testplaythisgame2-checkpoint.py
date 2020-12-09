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
        
class Testplaythisgame2(unittest.TestCase):# test class
    def setUp(self):
        self.a = playthisgame.Maingame()
        self.b = playthisgame.Maingame()
    def tearDown(self):
        self.a = None
        self.b = None
    def test_playgame_len(self):
        a = playthisgame.Maingame()
        self.assertEqual(len(self.a.models), 0)
        self.assertEqual(len(self.a.x), 30)
        self.assertEqual(len(self.a.y), 28)
        self.assertEqual(len(self.a.z), 22)        
    def test_playgame_type(self):
        b = playthisgame.Maingame()
        self.assertEqual(type(self.b.models), list)
        self.assertEqual(type(self.b.x), str)
        self.assertEqual(type(self.b.y), str)
        self.assertNotEqual(type(self.b.z), int)
        
unittest.main(argv=[''], verbosity=2, exit=False)
# -


