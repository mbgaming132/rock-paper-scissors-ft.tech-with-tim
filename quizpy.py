from optparse import Option
import random

user_wins = 0
computer_wins = 0

Option = ["r", "p", "s"]

Option[0]

while True:
    user_input = input("Type Rock/paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break


    if user_input not in Option:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = Option[random_number]
    print("Computer picked", computer_pick + ".")
    
    # the player win

    if user_input == "p" and computer_pick == "r":
        print("You won! ")
        user_wins += 1
        continue

    if user_input == "r" and computer_pick == "s":
        print("You won! ")
        user_wins += 1
        continue

    if user_input == "s" and computer_pick == "p":
        print("You won! ")
        user_wins += 1
        continue

    # the computer win

    if computer_pick == "p" and user_input == "r":
        print("the computer won! ")
        computer_wins += 1
        continue
        

    if computer_pick == "r" and user_input == "s":
        print(" the computer You won! ")
        computer_wins += 1
        continue
        

    if computer_pick == "s" and user_input == "p":
        print("the computer You won! ")
        computer_wins += 1
        continue

input("did you enjoy? ")


print("GoodBye ")
