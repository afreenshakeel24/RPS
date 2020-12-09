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

import member
class Student(Member): # Student subclass, represents a student 
    def __init__(self, name, age, marks):
        Member.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def display(self):
        Member.display(self)
        print('Marks: "{:d}"'.format(self.marks))
