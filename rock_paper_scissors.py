import random    # importing random function
import sys    # importing sys function to terminate run

user_action = input("Enter a choice (rock, paper, scissors): ")   # allow the user to input
possible_actions = ["rock", "paper", "scissors"]   # list of possible actions by the user
computer_action = random.choice(possible_actions)  # randomize the computer's choice
if user_action in possible_actions:   # if the user's input is in the list of possible actions, print below 
    print(f"You chose {user_action}, computer chose {computer_action}.")
else:   # otherwise print below
    print('Invalid Input!, please enter either rock, paper or scissors')
    return  

if user_action == computer_action:  
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
