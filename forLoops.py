
#For loopd - a type of construct that runs code instructions
# a finite amount of times over a group of data

#halloweenCandy = ["snickers", "kit kat", "M&MS"]

#for i in halloweenCandy:
   # print(i)

#numbers = [1,2,3,4,5,6,7,8,9]
#for i in numbers:
     #multi = i * 3
    # div = multi / 1.5
    # print("these numbers are multiplies by 3 and divided by 1.5" + str(div))



#while i in range(0,50):
     #print("x")

#for x in range(5):
    #word = input("please type in a word")
    #print(word)

word = "python"
for letter in word:
    print(letter)
    if letter =="P":
        print("did you mean paper")
    elif letter == "Y":
        print("did you mean python")


shopping = [3.00, 5.20, 7.40, 9.00]
total = 0
for items in shopping:
    total += items


print(total)



studentbody =["a","b","c"]
presnt = []
tardy =[]
absent = []
for student in studentbody:
    print("these students are present")
    print(presnt)
    ptint("these students are absent")
    print(absent)