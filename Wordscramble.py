import random
def scramblewordgame():
    point = 0
    wordpool = ["Philadelphia", "North Carolina", "congregate", "funtion"]
    print("welcome to word scramble")
    randomwordselect = random.randint(0,3)
    correctword = ""
    if randomwordselect == 0:
        print (wordpool[0])
        correctword = wordpool[0]
    elif randomwordselect == 1:
        print(wordpool[1])
        correctword = wordpool[1]
    elif userGuess == correctword:
        point += 1
        print("this is correct")
    elif randomwordselect == 2:
        print(wordpool[2])
        correctword = wordpool[2]
    elif userGuess == correctword:
        point += 1
        print("this is correct")
    elif randomwordselect == 3:
        print(wordpool[3])
        correctword = wordpool[3]
    elif userGuess == correctword:
        point += 1
        print("this is correct")
    else:
        print("this is incorrect")

    convertedselection = list(correctword)
    random.shuffle(convertedselection)
    scrambled = "".join(convertedselection)
    
    print("guess the correct word" + scrambled)
    userGuess = input()
    if userGuess == correctword:
        point +=1
        print("correct")
        print("Here is your score:" + str(point)+ "/3")
        print(point)
    
    else:
     print("incorrect")
     print("Here is your score:" + str(point)+ "/3")
     print(point)
    
    print(convertedselection)

scramblewordgame()
