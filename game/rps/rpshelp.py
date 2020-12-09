class rpshelp:
    def __init__(self):
        self.models = ['Rock', 'Paper', 'Scissors']
    def display(self): 
        print('You have to choose from: ') 
        for model in self.models:
            print('%s ' % model)
        print("\n \n How does it work? \n \n")
        print("Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock")