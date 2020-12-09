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

from .rpshelp import rpshelp
import time
import random
import os
import image
import cv2
import matplotlib.pyplot as plt

class rpsgame(rpshelp):
    def __init__(self):
        rpshelp.__init__(self)
    def display(self):
        rpshelp.display_(self)
    def game_rps(self):
        print()
        
        #All_Set image code starts here
        All_Set = cv2.imread("Images/All_Set.png")
        plt.imshow(cv2.cvtColor(All_Set, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
        time.sleep(3)
        #All_Set image code ends here
        
        #Read instruction image code starts here
        Reading_Ins = cv2.imread("Images/Reading_Ins.png")
        plt.imshow(cv2.cvtColor(Reading_Ins, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
        #Read instruction image code ends here
        
        while True:
            #Code to print instructions starts here
            
            ins = input("Do you want to see the instructions? Type yes or no :")
            
            if ins.lower() == "yes":
                print("Loading instructions...")
                time.sleep(2)
                rpshelp.display_(self)
            elif ins.lower() == "no":
                pass
            else: 
                print()
                #One_Job image code starts here
                One_Job = cv2.imread("Images/One_Job.png")
                plt.imshow(cv2.cvtColor(One_Job, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #One_Job image code ends here
                continue
            time.sleep(2)
            #Code to print instructions ends here
            
            #Code for player move starts here
            print()
            
            #Ready Steady Go image code starts here
            Ready_Steady_Go = cv2.imread("Images/Ready_Steady_Go.png")
            plt.imshow(cv2.cvtColor(Ready_Steady_Go, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
            #Ready Steady Go image code ends here
            
            print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
            print("Enter \"exit\" to quit")
            print("--------------------------------------")
            time.sleep(2)
            inp = input("Enter your move : ")
            if inp.lower() == "exit":
                break  
            elif inp.lower() == "rock":
                player_move = 0
            elif inp.lower() == "paper":
                player_move = 1    
            elif inp.lower() == "scissors":
                player_move = 2
            else:
                print("TYPE IT PROPERLY. \n") 
                #Rocket_Science code starts here
                Rocket_Science = cv2.imread("Images/Rocket_Science.png")
                plt.imshow(cv2.cvtColor(Rocket_Science, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Rocket_Science code ends here
                continue
            #Code for player move ends here
            
            #Code for computer move starts here
            print("Computer making a move...")
            comp_move = random.randint(0, 2)
            if comp_move == 0: print("Computer chooses... Rock")
            elif comp_move == 1: print("Computer chooses... Paper")
            elif comp_move == 2: print("Computer chooses... Scissor")
            
            print()
            #Code for computer move ends here
            
            #Winner code starts 
            if player_move == comp_move: 
                print("IT'S A TIE! \n\n")
                #Tie code starts here
                Tie = cv2.imread("Images/Tie.png")
                plt.imshow(cv2.cvtColor(Tie, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Tie code ends here
            
            #Player Rock; Computer Paper; 
            elif player_move == 0 and comp_move == 1: 
                print("COMPUTER WINS \n\n")
                
                #Player Rock loses image code starts here
                Rock_Lose = cv2.imread("Images/Rock_Lose.png")
                plt.imshow(cv2.cvtColor(Rock_Lose, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Rock loses image code ends here
             
            #Player Paper; Computer Rock
            elif player_move == 1 and comp_move == 0: 
                print("PLAYER WINS \n\n")
                
                #Player Paper wins image code starts here
                Paper_Win = cv2.imread("Images/Paper_Win.png")
                plt.imshow(cv2.cvtColor(Paper_Win, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Paper wins image code ends here
            
            #Player Scissor; Computer Rock    
            elif player_move == 2 and comp_move == 0: 
                print("COMPUTER WINS \n\n")
                
                #Player Scissor loses image code starts here
                Scissor_Lose = cv2.imread("Images/Scissor_Lose.png")
                plt.imshow(cv2.cvtColor(Scissor_Lose, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Scissor loses image code ends here
                
            #Player Rock; Computer Scissor    
            elif player_move == 0 and comp_move == 2: 
                print("PLAYER WINS \n\n")
                
                #Player Rock win image code starts here
                Rock_Win = cv2.imread("Images/Rock_Win.png")
                plt.imshow(cv2.cvtColor(Rock_Win, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Rock win image code ends here
            
            #Player Paper; Computer Scissor
            elif player_move == 1 and comp_move == 2: 
                print("COMPUTER WINS \n\n")
                
                #Player Paper loses image code starts here
                Paper_Lose = cv2.imread("Images/Paper_Lose.png")
                plt.imshow(cv2.cvtColor(Paper_Lose, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Paper loses image code ends here
                
            elif player_move == 2 and comp_move == 1: 
                print("PLAYER WINS \n\n")
                
                #Player Scissor wins image code starts here
                Scissor_Win = cv2.imread("Images/Scissor_Win.png")
                plt.imshow(cv2.cvtColor(Scissor_Win, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Player Scissor wins image code ends here
                
            else: print("Nothing \n\n")
            time.sleep(6)
            print()
            #Winner code ends here