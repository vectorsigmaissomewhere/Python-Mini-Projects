#a simple lottery game in python
import random
number=random.randint(1,101)
guess=int(input("Guess a number to win a lottery"))
while guess!=number:
    guess=int(input("Guess a number to win a lotter"))
    if guess<number:
        print("Guess Higher Number")
    elif guess>number:
        print("Guess Lower Number")
    elif guess==number:
        print("You won the lottery")
