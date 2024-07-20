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

# User choice
try:
    user_choice = int(
        input("What do you choose? 0 for rock, 1 for paper, and 2 for scissors:\n ")
    )
    if user_choice not in [0, 1, 2]:
        print("Invalid choice. Please enter 0, 1, or 2.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)

# Generate computer choice
computer_choice = random.randint(0, 2)

print(
    f"Your choice:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}"
)

# Check the conditions
winning_matrix =[
                    ["Draw", "You Lose", "You Win"],
                    ["You Win", "Draw", "You Lose"],
                    ["You Lose", "You Win", "Draw"]
                ]   
    
print(winning_matrix[user_choice][computer_choice])