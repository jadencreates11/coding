import random
def wordScrambler():
    wordPool = ["latitude",'arithmetic','sophisticated','pyscosis']
    correctWord =""

    print("Welcome to scrambled! ")
    randomSelect = random.randint(0,3)

    if randomSelect == 0:
        correctWord = wordPool[0]
    elif randomSelect == 1:
        correctWord = wordPool[1]
    elif randomSelect == 2:
        correctWord = wordPool[2]
    elif randomSelect == 3:
        correctWord = wordPool[3]
    
    convertedString = list(correctWord)
    
    random.shuffle(convertedString)
    scrambled = "".join(convertedString)
    

# While Loop Solution
    attempts = 0
    while attempts != 3:
        print("Please guess the correct word: " + scrambled)
        userGuess = input()

        if userGuess == correctWord:
            print("You Win!")
            break
        else:
            print("Sorry, you lose.")
            attempts += 1 

# For Loop Solution
    for  attempts in range(1,4):
        print("Please guess the correct word: " + scrambled)
        userGuess = input()
        if userGuess == correctWord:
            print("You Win!")
            print('this is your ' + str(attempts))
            break
        else:
            print("Sorry, you lose.")
            print('this is your ' + str(attempts))


wordScrambler()   
  