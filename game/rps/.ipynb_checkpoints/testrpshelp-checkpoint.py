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
import rpshelp

def setUp_class(Testrpshelp):
    self.a = rpshelp.rpshelp()
    self.b = rpshelp.rpshelp()
def tearDown_class(Testrpshelp):
    self.a = None
    self.b = None

class Testrpshelp(unittest.TestCase): # test class
    def setUp(self):
        self.a = rpshelp.rpshelp()
        self.b = rpshelp.rpshelp()
    def tearDown(self):
        self.a = None
        self.b = None
    def test_display_(self):
        a1 = self.a.display_()
        b1 = self.b.display_()
        self.assertNotEqual(self.a.display_() , '')
        self.assertIsInstance(self.a, rpshelp.rpshelp)
        self.assertIs(a1, b1)
        self.assertIsNot(self.a, a1)     
    def test_traditionalmodel(self):
        self.assertIn('Rock', self.a.models)
        self.assertIn('Paper', self.a.models)
        self.assertIn('Scissors', self.a.models)
        self.assertNotIn('Spock', self.a.models)
        
unittest.main(argv=[''], verbosity=2, exit=False)
# -


