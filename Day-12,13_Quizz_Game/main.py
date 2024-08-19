import os

questions = [
    "What is the capital of India?\nA. Kerala\nB. Kolkata\nC. New Delhi\nD. Mumbai",
    "Who is the prime minister of India?\nA. Narendra Modi\nB. Manmohan Singh\nC. Rahul Gandhi\nD. Athul",
    "Which river is known as the lifeline of India?\nA. Ganga\nB. Yamuna\nC. Brahmaputra\nD. Godavari",
    "Which monument is located in Agra?\nA. Qutub Minar\nB. Charminar\nC. Gateway of India\nD. Taj Mahal",
]

answers = ["C", "A", "A", "D"]


def clear_screen():
    """Clear the terminal screen and display the logo."""
    os.system("cls" if os.name == "nt" else "clear")


def start_quiz():
    score = 0
    print("Welcome to the Quizzer Game!")
    print("Game Rules:\nThere are 4 questions, and each carries 1 mark.")

    # Game loop
    for i in range(len(questions)):
        print("\n" + "=" * 30)
        print(questions[i])

        # Validate user input
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input! Please enter (A/B/C/D): ").upper()

        # Check answer
        if user_answer == answers[i]:
            print("You are correct!\n")
            score += 1
        else:
            print(f"You are incorrect! The correct answer is {answers[i]}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")
    if score == 0:
        print("You are not supposed to be a indian!")


def main():
    while True:
        start_game = input("\nPress 'S' to start the game or 'Q' to quit: ").lower()
        if start_game == "s":
            clear_screen()
            start_quiz()
        elif start_game == "q":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Type 'S' to start or 'Q' to quit.")


if __name__ == "__main__":
    main()
