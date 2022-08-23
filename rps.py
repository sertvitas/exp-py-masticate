import random

computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("Do you want rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("It's a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you win")
else:
    print("loser")
