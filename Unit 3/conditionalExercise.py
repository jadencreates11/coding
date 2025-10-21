def Votecheck(age):
    if age >= 18:
        print("You are allowed to vote")
    else:
        print("sorry, you are not allowed to vote yet")

def TicketCheck():
    if age <= 13:
        print("ticket is 10.00")
    elif age >= 14 and age <25:
        print("your ticket is 15.00")
    elif age >= 25 and age <55:
        print("your ticket is 20.00")
    else:
        print("yot ticket is 10.00")

TicketCheck(26)

def maxnumber():
    a = int(input("please enter your first numer"))
    b = int(input("please enter your second numer"))
    c = int(input("please enter your third numer"))
    hinumber = max(a,b,c)

    print()

