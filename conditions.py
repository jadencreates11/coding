
down = input("what down is it?")
yards = input("how many yards do you need to get another first down")

if down == 3 and yards == 2:
    print("run the ball")
elif down == 2 and yards < 0:
    print('pass the ball')
elif down ==3 and yards ==6:
    print('run the ball')

else: #this is the exit, assumes it is 4th down
    print("punt")

def permintCheck(age):
   if age >= 16:
      print("allowed to get permint")
   else:
    print("not allowed to get permint")


