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
from game.rps import rpsgame
from game.rps_fan import rpsgame_sheldon
import time

class Maingame:
    def __init__(self):
        self.models = ['Enter 0 to choose Traditional version', 'Enter 73 to choose Sheldon Cooper\'s version']
    def display(self): 
        print('You have to choose from: ') 
        for model in self.models:
            print('%s ' % model)
        time.sleep(2)
        i = input("Player chooses :")
        if i == '0':
            print("Loading Tradtional version...")
            time.sleep(3)
            rpsgame.rpsgame.game_rps(self)
        elif i == '73':
            print("Loading Sheldon's version...")
            time.sleep(3)
            rpsgame_sheldon.rpsgame_sheldon.game_rps_sheldon(self)
        else: 
            print("YOU HAD ONE TINY JOB \n")
        
# -




