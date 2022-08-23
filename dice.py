import random

roll = random.randint(1, 6)

# print("The dice came up " + str(roll))

guess = int(input("pick a number between 1-6:\n"))

if guess == roll:
    print("winner!")
else:
    print(
        "You loser...you picked "
        + str(guess)
        + ", but the dice came up "
        + str(roll)
        + "....\n Better luck next time."
    )
