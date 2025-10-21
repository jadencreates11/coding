


def permintCheck(age):
   if age >= 16:
      print("allowed to get permint")
   else:
    print("not allowed to get permint")

def weather():
   weather = input("what is the weather like today")
   if weather == "sunny":
      print("its is beautiful outside, bring glasses")
   elif weather == 'rainy':
      print("bring umbrella")
   else:
      print("im not sure")
   

def numbercheck(number):
   if number >= 0:
      print ("this is a postive")
   else:
      print("this is a negative")

def gradecheck(grade):
   if grade >=90:
      print("your grade is an A")
   elif grade >=80:
      print("you have a B")
   elif grade >=70:
      print("your grade is a C")
   else:
      print("you have an F")

gradecheck()