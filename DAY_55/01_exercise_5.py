# Question 5
# Snake Water Gun

# Snake, Water and Gun is a variation of the children's game "rock-paper-
# scissors" where players use hand gestures to represent a snake, water, or
# a gun. The gun beats the snake, the water beats the gun, and the snake
# beats the water. Write a python program to create a Snake Water Gun
# game in Python using if-else statements. Do not create any fancy GUI.
# Use proper functions to check for win.  


print('\n')
print("WELCOME TO \"SNAKE WATER GUN\" GAME")
import random
pc = int(random.randint(1,3))
while(True):
    user = int(input("Enter 1 for Snake\nEnter 2 for Water\nEnter 3 for Gun\nPlease Enter: "))
    if user == pc:
        print(f"You both entered same")
        print("Draw")    
    elif user == 1 and pc == 2:
        print("computer entered: Water")
        print("You Win")
        break 
    elif user == 1 and pc == 3: 
        print("computer entered: Gun")
        print("Computer Win")  
        break
    elif user == 2 and pc == 1: 
        print("computer entered: Snake")
        print("Computer Win")
        break
    elif user == 2 and pc == 3: 
        print("computer entered: Gun")
        print("You Win")  
        break    
    elif user == 3 and pc == 1:
        print("computer entered: Snake")
        print("You Win")
        break 
    elif user == 3 and pc == 2:
        print("computer entered: Water")
        print("You Win")    
        break 
    else:
        print("You enterd wrong number")    
        break   

