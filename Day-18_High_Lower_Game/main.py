import random
import os
from art import logo, vs
from game_data import data


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def display_comparison(option, label):
    print(
        f"Compare {label}: {option['name']}, {option['description']}, from {option['country']}"
    )


def validate_user_answer(answer, a, b):
    return (answer == "a" and a["follower_count"] > b["follower_count"]) or (
        answer == "b" and b["follower_count"] > a["follower_count"]
    )


def play_game():
    score = 0
    continue_game = True
    compare_a = random.choice(data)

    while continue_game:
        clear_screen()
        compare_b = random.choice(data)

        # Ensure compare_b is different from compare_a
        while compare_a["name"] == compare_b["name"]:
            compare_b = random.choice(data)

        display_comparison(compare_a, "A")
        print(vs)
        display_comparison(compare_b, "B")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if answer not in ["a", "b"]:
            print("Invalid option. Please type A or B.")
            continue

        if validate_user_answer(answer=answer, a=compare_a, b=compare_b):
            score += 1
            print(f"You're right! Current score: {score}.")
            compare_a = compare_b
        else:
            print(f"You're wrong! Final score: {score}.")
            restart_game = input(
                "Do you want to restart the game? Type 'Y' or 'N': "
            ).lower()
            if restart_game == "y":
                play_game()  # Reset game state
            continue_game = False


play_game()
