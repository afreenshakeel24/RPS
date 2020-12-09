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

from .rpshelp_sheldon import rpshelp_sheldon
import time
import random
import os
import image
import cv2
import matplotlib.pyplot as plt

class rpsgame_sheldon(rpshelp_sheldon):
    def __init__(self):
        rpshelp_sheldon.__init__(self)
    def display(self):
        rpshelp_sheldon.display_sheldon(self)
    def game_rps_sheldon(self):
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
                time.sleep(3)
                rpshelp_sheldon.display_sheldon(self)
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
                
            print("Enter \"Rock\",\"Paper\",\"Scissors\",\"Lizard\",\"Spock\" to play")
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
            elif inp.lower() == "lizard":
                player_move = 3
            elif inp.lower() == "spock":
                player_move = 4
            
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
            comp_move = random.randint(0, 4)

            # Print the computer move
            if comp_move == 0: print("Computer chooses... Rock")
            elif comp_move == 1: print("Computer chooses... Paper")
            elif comp_move == 2: print("Computer chooses... Scissor")
            elif comp_move == 3: print("Computer chooses... Lizard")
            elif comp_move == 4: print("Computer chooses... Spock")
            
            print()
            
            if player_move == comp_move: 
                print("IT'S A TIE! \n\n")
                
                #Tie code starts here
                Tie = cv2.imread("Images/Tie.png")
                plt.imshow(cv2.cvtColor(Tie, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Tie code ends here
                
            elif player_move == 2 and comp_move == 1: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                b1 = cv2.imread("Images/b1.png")
                plt.imshow(cv2.cvtColor(b1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 1 and comp_move == 2: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                b2 = cv2.imread("Images/b2.png")
                plt.imshow(cv2.cvtColor(b2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 1 and comp_move == 0: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                c1 = cv2.imread("Images/c1.png")
                plt.imshow(cv2.cvtColor(c1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 0 and comp_move == 1: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                c2 = cv2.imread("Images/c2.png")
                plt.imshow(cv2.cvtColor(c2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 0 and comp_move == 3: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                d1 = cv2.imread("Images/d1.png")
                plt.imshow(cv2.cvtColor(d1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 3 and comp_move == 0: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                d2 = cv2.imread("Images/d2.png")
                plt.imshow(cv2.cvtColor(d2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 3 and comp_move == 4: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                e1 = cv2.imread("Images/e1.png")
                plt.imshow(cv2.cvtColor(e1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 4 and comp_move == 3: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                e2 = cv2.imread("Images/e2.png")
                plt.imshow(cv2.cvtColor(e2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 4 and comp_move == 2: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                f1 = cv2.imread("Images/f1.png")
                plt.imshow(cv2.cvtColor(f1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 2 and comp_move == 4: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                f2 = cv2.imread("Images/f2.png")
                plt.imshow(cv2.cvtColor(f2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 2 and comp_move == 3: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                g1 = cv2.imread("Images/g1.png")
                plt.imshow(cv2.cvtColor(g1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 3 and comp_move == 2: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                g2 = cv2.imread("Images/g2.png")
                plt.imshow(cv2.cvtColor(g2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 3 and comp_move == 1: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                h1 = cv2.imread("Images/h1.png")
                plt.imshow(cv2.cvtColor(h1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 1 and comp_move == 3: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                h2 = cv2.imread("Images/h2.png")
                plt.imshow(cv2.cvtColor(h2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 1 and comp_move == 4: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                i1 = cv2.imread("Images/i1.png")
                plt.imshow(cv2.cvtColor(i1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 4 and comp_move == 1: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                i2 = cv2.imread("Images/i2.png")
                plt.imshow(cv2.cvtColor(i2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 4 and comp_move == 0: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                j1 = cv2.imread("Images/j1.png")
                plt.imshow(cv2.cvtColor(j1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 0 and comp_move == 4: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                j2 = cv2.imread("Images/j2.png")
                plt.imshow(cv2.cvtColor(j2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 0 and comp_move == 2: 
                print("PLAYER WINS \n\n")
                
                #Image code starts here
                k1 = cv2.imread("Images/k1.png")
                plt.imshow(cv2.cvtColor(k1, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            elif player_move == 2 and comp_move == 0: 
                print("COMPUTER WINS \n\n")
                
                #Image code starts here
                k2 = cv2.imread("Images/k2.png")
                plt.imshow(cv2.cvtColor(k2, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                #Image code ends here
                
            else: print("Nothing \n\n")
            time.sleep(5)
            print()