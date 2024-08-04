import random
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

# Check the conditions
winning_matrix = [
    ["Draw", "You Lose", "You Win"],
    ["You Win", "Draw", "You Lose"],
    ["You Lose", "You Win", "Draw"],
]

user_score = 0
computer_score = 0

# Play 5 rounds
for _ in range(5):

    # User choice
    try:
        user_choice = int(
            input("What do you choose? 0 for rock, 1 for paper, and 2 for scissors:\n ")
        )
        if user_choice not in [0, 1, 2]:
            print("Invalid choice. Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Generate computer choice
    computer_choice = random.randint(0, 2)

    print(
        f"Your choice:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}"
    )

    # Determine the result
    result = winning_matrix[user_choice][computer_choice]
    print(result)

    # Update scores
    if result == "You Win":
        user_score += 1
    elif result == "You Lose":
        computer_score += 1

# Display final scores and winner
print(f"\nFinal Scores:\nYou: {user_score}\nComputer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the set!")
elif user_score < computer_score:
    print("Sorry, the computer won the set.")
else:
    print("The set is a draw.")
