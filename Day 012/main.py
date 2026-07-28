import random
import sys
from os import system


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        print("You have 5 attempts remaining to guess the number.")
        lives = 5
        return lives
    elif difficulty == "easy":
        print("You have 10 attempts remaining to guess the number.")
        lives = 10
        return lives
    else:
        print("pls enter 'easy' or 'hard'")
        sys.exit()


def play_game():
    while input("play? 'y' or 'n': ").lower() == "y":
        system("clear")
        lives = choose_difficulty()

        random_number = random.randint(1, 100)

        won = False
        while lives >= 1:
            # game
            guess = int(input("Make a guess: "))

            if random_number < guess:
                lives -= 1
                if lives == 0:
                    print("Too high.")
                else:
                    print("Too high.\nGuess again.")
                    print(f"You have {lives} attempts remaining to guess the number.")

            elif random_number > guess:
                lives -= 1
                if lives == 0:
                    print("Too low.")
                else:
                    print("Too low.\nGuess again.")
                    print(f"You have {lives} attempts remaining to guess the number.")

            elif random_number == guess:
                print(f"You got it! The answer was {random_number}.")
                won = True
                break

        if not won:
            print(
                f"You've run out of guesses. Refresh the page to run again. {random_number}"
            )


def main():
    system("clear")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    play_game()


main()
