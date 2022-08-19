#la idea sería hacer lo mismo pero segmentándolo en funciones.

from glob import glob
from operator import truediv
import random
replay = True
answer_valid = False
print("""  /$$$$$$                                                 /$$     /$$                                                         /$$                           /$$
 /$$__  $$                                               | $$    | $$                                                        | $$                          | $$
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$| $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/|__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$          
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$       /$$
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      |__/
                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               """)

def play_the_game():
    guess=0
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        Attempts = 10
    elif difficulty == "hard":
        Attempts = 5
    else:
        print("You didn't choose a valid option, so let's try the easy one.")
        Attempts = 10

    ActNumber = random.randint(1,100)

    while (guess != ActNumber) & (Attempts>=1):
        print(f"You have {Attempts} remaining to gess the number.")
        guess=int(input("Make a guess:"))
        if guess<ActNumber:
            print("Too low.\nGuess again.\n")
            Attempts-=1
        elif guess>ActNumber:
            print("Too high.\nGuess again.\n")
            Attempts-=1
        elif guess==ActNumber:
            print("You're right!")
        else:
            print("Please, guess only numbers.\nGuess again.\n")

    if guess==ActNumber:
        print("You won!")
    elif Attempts==0:
        print("You've run out of guesses, you lose.")
    else:
        print("Something went wrong, please contact the programmer")

play_the_game()

while (answer_valid == False)|(replay==True):

    replay_answer=input("Play again? [yes/no]: ")
    if replay_answer=="yes":
        replay = True
        answer_valid = True
        play_the_game()
    elif replay_answer=="no":
        replay = False
        answer_valid = True
        print("Bye bye!")
    else:
        print("Please type 'yes' or 'no'")
        answer_valid = False
