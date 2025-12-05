def pyhthonQuiz():
    grade = 0
    print("1. what color is the sky?")
    print("A. Blue")
    print("B. Red")
    print("C. Pink")
    print("D.Green")
    testAnswer = input("")
    correctanswer = "a"
    if testAnswer == correctanswer:
        grade += 1
        print("correct")
    else:
        print("incorrect")
    print("2. What animal is a fish")
    print("A. dog")
    print("B. Cat")
    print("C. shark")
    print("D. cow")
    testAnswer = input("")
    correctanswer = "c"
    if testAnswer == correctanswer:
        grade += 1
        print("correct")
    else:
     print("incorrect")
    print ("3.How many states are in the USA ")
    print("A. 60")
    print("B. 50")
    print("C. 100")
    print("D. 52")
    testAnswer = input("")
    correctanswer = "b"
    if testAnswer == correctanswer:
            grade +=1
            print("correct")
            print("Here is your final grade:" + str(grade)+ "/3")
            print(grade)
    
    else:
     print("incorrect")
     print("Here is your final grade:" + str(grade)+ "/3")
     print(grade)
    
pyhthonQuiz()