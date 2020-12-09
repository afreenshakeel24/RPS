game
    rps
        rpsgame.py
        rpshelp.py
    rps_fan
        rpsgame_sheldon.py
        rpshelp_sheldon.py

# Package
We have a package called game. This package asks the user which game it wants to play - the traditional version of rock paper scissor or the Sheldon Cooper's version which is rock paper scissor lizard spock. On the basis of user's choice, it goes to either of the sub package rps or rps_fan

## Sub Package1 - rps
This sub package contains two modules
    1. rpshelp.py
        This module contains two methods - init and display
        init initializes the elements needed for the game
        display will show the elements and basic set of rules on how to play the game
    2. rpsgame.py
        This module contains three methods - init, display and game_rps
        init inherites the package rpshelp.py to initialize the elements needed for the game
        display inherites the package rpshelp.py to show the elements and basic set of rules on how to play the game
        game_rps will play the acutal game where it asks the user to begin the game where user chooses an element and computer also chooses and element. Based upon both the choices, a winer is decided.

        
## Sub Package2 - rps_fan
This sub package contains two modules
    1. rpshelp_sheldon.py
        This module contains two methods - init and display
        init initializes the elements needed for the game
        display will show the elements and basic set of rules on how to play the game
    2. rpsgame.py
        This module contains three methods - init, display and game_rps
        init inherites the package rpshelp.py to initialize the elements needed for the game
        display inherites the package rpshelp.py to show the elements and basic set of rules on how to play the game
        game_rps will play the acutal game where it asks the user to begin the game where user chooses an element and computer also chooses and element. Based upon both the choices, a winer is decided.