
def Calculator():
    print("What subject is this for")
    subject = input()
    print(" This Subject is" + subject)
    gradelist = []
    week = 1 
    print("What is the grade number for this week" + str(week))
    gradenumber = input("WHat is the grade for this week")
    while gradenumber != "Overall":
         grade = int(gradenumber)
         gradelist.append(grade)
         print(gradelist)
         gradenumber = input("type in the grade for next week")
    else:
          x = sum(gradelist)
          print(x / 17)
    if grade >=90:
      print("your grade is an A")
    elif grade >=80:
      print("you have a B")
    elif grade >=70:
      print("your grade is a C")
    elif grade >= 60:
       print("you have a D")
    else:
      print("you have an F")



Calculator()