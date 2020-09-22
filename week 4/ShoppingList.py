# This program prompts the user to enter a shopping list
# item by item, then repeats it back to the user.

# Study this code and understand it.

Products = {"Milk" : 1.1} # Add products to this list

print("Enter items of the shopping list one by one.")
print("Enter STOP when you are done")

ShoppingList=[] # ShoppingList = [ ["Milk", 2] ]
# this creates an empty list

ShopperEntry = ""

while ShopperEntry != "STOP":
    ShopperEntry = input("Enter next item: ")

    while not ShopperEntry.isalpha():
        print("Your entry must only contain letters of the alphabet. Try again")
        ShopperEntry = input("Enter next item ")

    # make the entry upper case
    ShopperEntry = ShopperEntry.upper()

    if ShopperEntry != "STOP":
        ShoppingList.append(ShopperEntry)

# Now sort the shopping list in alphabetic order.
ShoppingList.sort()

# Print the list back to the user - note the use of an iterator

Count = 0
for Item in ShoppingList:
    Count = Count + 1
    print("Item number " + str(Count) + " is " + Item)






