import random
import sys

def play_game():
    """Implements the core logic of the guessing game."""
    secret_number = random.randint(1, 100)
    guesses_left = 10

    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. You have 10 guesses.")

    while guesses_left > 0:
        try:
            guess_str = input(f"Guess #{11 - guesses_left}: ")
            guess = int(guess_str)
            if not (1 <= guess <= 100):
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.") # Basic error handling for now
            continue


        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You found the number!")
            return

        guesses_left -= 1
        if guesses_left > 0:
            print(f"You have {guesses_left} guesses left.")

    print(f"Sorry, you've run out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    while True:
        play_game()
        while True:
            play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again_input == "yes":
                break  # Breaks the inner loop, continues the outer loop for a new game
            elif play_again_input == "no":
                print("Thanks for playing!")
                sys.exit()  # Exits the program cleanly
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
