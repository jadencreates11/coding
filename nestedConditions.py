
# Nested Conditions = A conditional statement that has other conditional
# statements within it. Conditions inside of conditions.

def sandwichSchore():
    print("welcome to jaden foods, what would you like")
    print("1.Meatball Sandwich")
    print("2.turkey sandwich")
    print("3.honey turkey sandwich")
    print("4.buffalo chicken sandwich")
selection= int(input("please give me meatball sand"))
if selection == 1:
    print("you have selected meatball sandwich")
    print("what side do you want")
    print("1.chips")
    print("2.salads")
    print("3.fries")
    side = int(input())
    if side == 1:
        print("great you have meatball sandwich and chips")
    elif side == 2:
        print("great, you have a meatball sandwich and salad")
    elif side == 3:
        print("great you have a meatball sandwich with fries")
    else:
        ("sorry I dont understand")
    if selection == 2:
        print("sorry we are out of turkey sandwiches")
    


    def atm():
        balance = 2000
        pin = 1234

        userpin = input("please type in your bank pin number")
        if userpin == pin:
            print("welcome, what you like to do")
            print("withdrawl money")
            print("deposit money")
            print("check your balance")
            selection = int(input())
            if selection ==1:
                amount = int(input("how mcuh do you want to take out"))
                if amount > balance:
                    print("you dont have enough in your account")
                else:
                    newBalance = balance - amount
                    print("your new balance is :" + str(newBalance))
                    if selection ==2:
                        amount = int(input("how much would you like to deposit"))
                newBalance= balance + amount
                print("you are adding" + str(amount))
                print("your new balance is" + str(newBalance))
                if selection ==3:
                    print("your balnce is"+ str(balance))
                else:
                    print("sorry I dont understand your selection")



#python lists = a way to organize data, regardless of data tyoe.
#write the data you want in your list in the square brackets