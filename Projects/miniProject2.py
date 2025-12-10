#def GradeSum ():
    #grade = []
    #print (" What subject would you like to grade")
   # print("Math")
    #print("History")
    #print("English")
    #Selection = input("")
    #Choice = "Math"
    #Choice = "History"
    #Choice = "English"
    #if Selection == Choice:
        #print("You may now enter the score")
    #else:
        #print("Sorry, that subject doesn't exist")
    #if grade >=90:
      #print("A")
   # elif grade >=80:
     #print("B")
    #elif grade >=70:
     #print("C")
    #elif grade >= 60:
       #print("D")
    #else:
     # print("F")
      #print(grade)

def SumOfGradeList():
    Grade = []
    number = input("type your number please")
    while GradeNumber != "quit":
        GradeNumber = int(number)
        Grade.append(GradeNumber)
        print(Grade)
        usernumber = input("type in a number")
    else:
        x = sum(Grade)
        print(x)

SumOfGradeList()

 