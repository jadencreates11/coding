
def gpaCalculator():
    print(' What subject is this GPA for? ')
    subject = input()
    print("the user entered: "+ subject)
    week = 1
    sum = 0
    for x in range (17):
        print('Please enter the grade for week : ' + str(week))
        grade = int(input())
        sum += grade
        week += 1
        gpa = sum / 17
    if gpa > 70 and gpa < 80:
        print('C')
    elif gpa > 80  and gpa < 90:
        print('B')
    elif gpa > 90  and gpa <100:
        print('A')
    else:
        print('F')
    print('your gpa for '+ subject + ' is ' + str(gpa))

gpaCalculator()

