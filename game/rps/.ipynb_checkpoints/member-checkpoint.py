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

class Member: # Super class, any university member
    def __init__(self, name, age): # initialize name and age
        self.name = name
        self.age = age
        print('(Initialized Member: {})'.format(self.name))
    def display(self): # display name and age 
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))
