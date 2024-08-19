import random


def start_game():
    computer_choice = random.randint(1, 50)
    print(f"Computer choice: {computer_choice}")
    attempts = 0
    is_user_guessed_correctly = False

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while not is_user_guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            elif user_guess < computer_choice:
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
                    f"Congratulations! You guessed it correctly in {attempts} attempts."
                )
                is_user_guessed_correctly = True
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
