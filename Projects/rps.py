"I will make a function that takes a random word, either rock, paper, or scissors and then the user will type out a word and you will either get a draw, win, or lose"

"It will be able to compare, it will take numbers and ccomapre them, we can also loop"

#how will the program flow
"Welcomes the user to the game"
"give them the option to play the game or look at game tutorials"
"if user selects rules. show them the rule, else start the game"
"inform them that the game has started and give them the option of RPS"
"computer makes a random selection"
"inform the player if they have lost, won, or tied"

def rpsGame():
    rpsoptions_cpu = ["rock", "paper", "scissors"]
    print("Welcome to RPS GAME")
    print("please select P for rule and P to start game")
    selection = input()
    if selection == "r":
        print("here are the game rulea...")
    elif selection == "p":
        print("here")
rpsGame()