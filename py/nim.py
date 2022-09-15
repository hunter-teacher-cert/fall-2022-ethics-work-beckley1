# nim.py
# Ben Eckley
# CSCI 77800 Fall 2022
# collaborators: none 
# consulted:lots and lots of internet

#   GOAL: Be the player to remove the last stone.
#   RULES:
#   - bag contains 12 stones initially
#   - a move consists of removing 1-3 stones from the bag
#   CODE:
#   - turn starts with prompting user for num of stones to remove
#   - tell user how many AI removed (random 1-3)
#   - continue until there is a winner
# Welcome message
print("Welcome to the Wonderful Game of Nim!")
# make starting bag of stones with 12 stones
stones = 12

player = 1

def nextplayer():
    if (player == 1):
        player == 2
    else:
        player = 1
    
choice = input("You may remove between 1 and 3 stones. What is your choice? ")
#after player 1 takes a stone it subtractsinput from current value of stones
stones = stones - int(choice)
#need a print statement saying how many are left
print("You chose",choice,".","There are now",stones,"in the bag.")

#need a loop that'll countdown until there are no stones in the bag
while (stones > 0):
    choice
    stones = stones - int(choice)
    print("You chose",choice,".","There are now",stones,"in the bag.")
    
    if (stones == 0):
        print("Congratulations player",player,"!","You won!")
        
    else:
        nextplayer
       
    
