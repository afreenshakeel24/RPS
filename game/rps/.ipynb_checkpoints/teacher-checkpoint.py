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
import member

class Teacher(Member): # Teacher subclass, represents a teacher 
    def __init__(self, name, age, salary):
        Member.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def display(self):
        Member.display(self)
        print('Salary: "{:d}"'.format(self.salary))
