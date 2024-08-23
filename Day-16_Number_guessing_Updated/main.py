import os
import random
from art import logo


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def start_game():
    computer_choice = random.randint(1, 100)
    is_user_guessed_correctly = False

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty choice. Starting with 'easy' mode by default.")
        attempts = 10

    print(f"You have {attempts} attempts remaining.")

    while not is_user_guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))

            if attempts == 1 and user_guess != computer_choice:
                print(
                    f"Sorry, you’ve run out of attempts. The correct number was {computer_choice}."
                )
                return

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            else:
                attempts -= 1
                if user_guess < computer_choice:
                    if computer_choice - user_guess <= 5:
                        print("You are close, but still a bit low!")
                    else:
                        print("You are too low!")
                elif user_guess > computer_choice:
                    if user_guess - computer_choice <= 5:
                        print("You are close, but still a bit high!")
                    else:
                        print("You are too high!")
                else:
                    print(
                        f"Congratulations! You guessed it correctly with {attempts} attempts remaining."
                    )
                    is_user_guessed_correctly = True

            if not is_user_guessed_correctly:
                print(f"You have {attempts} attempts remaining.")
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
