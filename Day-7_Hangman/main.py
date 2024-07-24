import os
import random
from hangman_art import stages, logo
from hangman_words import players

print(logo)
chosen_word = random.choice(players).lower()
# print(f"Pssst, the solution is {chosen_word}") for debugging

# Display blanks and handle spaces
display = []
for char in chosen_word:
    if char == " ":
        display.append(" ")
    else:
        display.append("_")

print(" ".join(display))

lives = 6
is_game_over = False

# Game loop
while not is_game_over and lives > 0:
    user_guess = input("Enter your guess: ").lower()
    # Clear screen
    os.system("cls" if os.name == "nt" else "clear")

    if user_guess in display:
        print(f"The letter '{user_guess}' is already guessed. Guess different letter")
        continue
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
