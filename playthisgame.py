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
import random
import os
import image
import cv2
import matplotlib.pyplot as plt
import simpleaudio as sa


class MyInputError(Exception):
    pass

class Maingame:
    def __init__(self):
        self.models = []
        self.x = "Loading Traditional version..."
        self.y = "Loading Sheldon's version..."
        self.z = "YOU HAD ONE TINY JOB \n"
    def display(self): 
        print('You have to choose between 0 and 73. Enter 0 to choose the Traditional version or enter 73 to choose Sheldon Cooper\'s version ')
        for model in self.models:
            print('%s ' % model)
        time.sleep(2)
        #x = "Loading Traditional version..."
        try:
            i = int(input("Player chooses :"))
            if i == 0:
                print(self.x)
                time.sleep(3)
                rpsgame.rpsgame.game_rps(self)
            elif i == 73:
                print(self.y)
                time.sleep(3)
                rpsgame_sheldon.rpsgame_sheldon.game_rps_sheldon(self)
            else:
                raise MyInputError()
        except MyInputError:
            print(self.z)
            #One_Job image code starts here
            One_Job = cv2.imread("Images/One_Job.png")
            plt.imshow(cv2.cvtColor(One_Job, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
            #One_Job image code ends here
            
        except ValueError:
            print(self.z)
            #One_Job image code starts here
            One_Job = cv2.imread("Images/One_Job2.png")
            plt.imshow(cv2.cvtColor(One_Job, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
            #One_Job image code ends here
            
        
# -



