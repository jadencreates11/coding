#List - a collection system for storing and organizing multiple
#places of data.

# List syntax (how it is written)
# when we want to create a list we first create a variable, and then
# assign it to the square brackets [].
shoppinglist = ["apples", "oranges", "water", 1,2,3, True, ["bread", "milk"]]

print()

#if we ant to access an item from a list, we use the index systems.
# we write thwe list variable name, and then use the brackets and pass in the
# number postition.

# List are zero based indexed; meaning the lsit count always starts at zero(0)

print()
trunkparty = ["laptop", "tv", "fridge"]

def addItemForCollage(list):
    newItem =input("please add new item to your list")
    list.append(newItem)

    def removeItemFromList(list):
        Cart = ["food", "juice", 'crayon']
        item =input("please type what to remove")
        Cart.remove(item)
numeberlist = [100, 23, 450, 63, 1, 6, 19, 1000]
def numberlist(NewNumber):
 numeberlist.append(NewNumber)
 print(numeberlist)

numeberlist()