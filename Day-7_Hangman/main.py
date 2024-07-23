import random
import os
from hangman_art import stages, logo
from hangman_words import players


lives = 6



print(logo)
chosen_word = random.choice(players).lower()
print(f"Pssst, the solution is {chosen_word}.")

display = ["_"] * len(chosen_word)
print(" ".join(display))

is_game_over = False
while not is_game_over and lives > 0:
    user_guess = input("Enter your guess: ").lower()
    # Clear screen
    os.system("cls" if os.name == "nt" else "clear")

    if user_guess in display:
        print(f"The letter {user_guess}is already guessed. Guess different letter")

    guess_correct = False

    for index, letter in enumerate(chosen_word):
        if letter == user_guess:
            display[index] = letter
            guess_correct = True

    if not guess_correct:
        lives -= 1
        print(f"Wrong guess. Lives remaining: {lives}")
        print(stages[lives])
    print(" ".join(display))

    if "_" not in display:
        is_game_over = True
        print("Congratulations! You've guessed the word correctly.")
    elif lives == 0:
        is_game_over = True
        print(f"You lose. The word was '{chosen_word}'. Better luck next time!")
