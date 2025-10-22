#numberinput = input("please enter a number")
    ## print(numberlist)
     # numberinput = input("please enter number")
     # print("code is working, please enter numbers")
   # else:
      # print("loop has ended")
      # print("code is working, able to quit")

#i = 1
#while i < 3:
   # print(i)
    #print("beginning of the story")
    #x = input("type something")
    #print ("middle of story")
    #y = input("type something")
   # print("end of story")
   # z = input("type something")
   # i +1
   # print(i)
  
#def numberlistloop():
    #numberlist = []
    #usernumber = input("type your number please")
    #while usernumber != "quit":
       # newNumber = int(usernumber)
       # numberlist.append(newNumber)
       # print(numberlist)
       # usernumber = input("type in a number")
   # else:
        #print("loop has stopped")

#numberlistloop()

def addnumberlist():
    numberlist = []
    usernumber = input("type your number please")
    while usernumber != "quit":
        newNumber = int(usernumber)
        numberlist.append(newNumber)
        print(numberlist)
        usernumber = input("type in a number")
    else:
        x = sum(numberlist)
        print(x)

addnumberlist()