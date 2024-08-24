import os
import random
from art import logo

EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def start_game():
    computer_choice = random.randint(MIN_NUMBER, MAX_NUMBER)
    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess what it is?")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Invalid choice. Please choose 'easy' or 'hard': ").lower()

    attempts = EASY_MODE_ATTEMPTS if difficulty == "easy" else HARD_MODE_ATTEMPTS

    print(f"You have {attempts} attempts remaining.")

    while attempts > 0:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess < MIN_NUMBER or user_guess > MAX_NUMBER:
                print(f"Please guess a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            else:
                attempts -= 1
                if user_guess == computer_choice:
                    print(f"Congratulations! You guessed it correctly with {attempts} attempts remaining.")
                    return
                elif abs(computer_choice - user_guess) <= 5:
                    feedback = "You are close!"
                elif user_guess < computer_choice:
                    feedback = "You are too low!"
                else:
                    feedback = "You are too high!"
                print(feedback)

            if attempts > 0:
                print(f"You have {attempts} attempts remaining.")
            else:
                print(f"Sorry, you've run out of attempts. The correct number was {computer_choice}.")
                return

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        clear_screen()
        start_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
