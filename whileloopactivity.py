def numberloop():
    numberinput = input("please enter a number")
    numberlist = []
    while numberinput != "quit":
      numberlist.append(numberinput)
      print(numberlist)
      numberinput = input("please enter number")
      print("code is working, please enter numbers")
    else:
       print("loop has ended")
       print("code is working, able to quit")