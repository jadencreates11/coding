
def Calculator():
    print("What subject is this for")
    subject = input()
    print(" This Subject is" + subject)
    gradelist = []
    week = 1
    print("What is the grade number for this week" + str(week))
    gradenumber = input("type your grade number please")
    while gradenumber != "OverAll":
        grade = int(gradenumber)
        gradelist.append(grade)
        print(gradelist)
        gradenumber = input("type in a number")
    else:
        x = sum(gradelist)
        print("This is the overall grade" + x / 17)
Calculator()