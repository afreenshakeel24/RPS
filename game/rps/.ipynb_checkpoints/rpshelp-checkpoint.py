class rpshelp:
    def __init__(self):
        self.models = ['Rock', 'Paper', 'Scissors']
    def display_(self): 
        lst = ['Rock', 'Paper', 'Scissors']
        print('You have to choose from: ') 
        for model in lst:
            print(model)
        print("\n \n How does it work? \n \n")
        print("Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock")