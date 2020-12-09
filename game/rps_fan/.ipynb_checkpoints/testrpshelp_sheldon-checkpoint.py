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
import rpshelp_sheldon

def setUp_class(Testrpshelp_sheldon):
    self.a = rpshelp_sheldon.rpshelp_sheldon()
    self.b = rpshelp_sheldon.rpshelp_sheldon()
def tearDown_class(Testrpshelp_sheldon):
    self.a = None
    self.b = None

class Testrpshelp_sheldon(unittest.TestCase): # test class
    def setUp(self):
        self.a = rpshelp_sheldon.rpshelp_sheldon()
        self.b = rpshelp_sheldon.rpshelp_sheldon()
    def tearDown(self):
        self.a = None
        self.b = None
    def test_display(self):
        a1 = self.a.display_sheldon()
        b1 = self.b.display_sheldon()
        self.assertNotEqual(self.a.display_sheldon() , '')
        self.assertIsInstance(self.a, rpshelp_sheldon.rpshelp_sheldon)
        self.assertIs(a1, b1)
        self.assertIsNot(self.a, a1)    
    def test_sheldonmodel(self):
        self.assertIn('Rock', self.a.models)
        self.assertIn('Lizard', self.a.models)
        self.assertIn('Scissors', self.a.models)
        self.assertIn('Spock', self.a.models)
        
unittest.main(argv=[''], verbosity=2, exit=False)
# -


