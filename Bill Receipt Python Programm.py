# Write a python program which will keep adding a stream of numbers inputted by the user.
# The adding stops as soon as user presses q key on the keyboard ?
print("="*50,'\n                Welcome to our Shop\n',"="*50,sep="")
sum = 0
Iteams = []
ItemList = []
ItemPrice = []
while True:
    UserChoice = input("Press y for continue and Press any key  for stop : ")
    if UserChoice == 'y':
        UserItemName = input("Enter the item name : ")
        UserInput = input("Enter the item price : ")
        sum = sum + int(UserInput)
        print("Purchased Item  : ",UserItemName)
        print("Purchased Item Price : ",UserInput)
        print(f"Order total so far : {sum}",sep="")
        #Iteams[UserItemName]=UserInput
        #ItemList.append(UserItemName)
        #ItemPrice.append(UserInput)
    else:
        #print(Iteams)
        print("="*50,'\n                Welcome to our Shop\n',"="*50,sep="")
        #print(ItemList)
        #print(ItemPrice)
        print(f"\nYour Total bill is {sum}. \n\nThanks for shopping with us.")
        break