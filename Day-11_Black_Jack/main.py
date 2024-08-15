import random
import os
from art import black_logo

print(black_logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def deal_initial_cards():
    """Deals 2 cards to both the player and the computer and returns them."""
    player_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    return player_cards, computer_cards


def calculate_score(card_list):
    """Calculate the score from a list of cards."""
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0  # Blackjack
    if 11 in card_list and score > 21:
        score -= 10  # Treat Ace as 1
    return score


def check_game_over(player_score):
    """Checks if the game is over based on the player's score."""
    return player_score == 0 or player_score > 21


def computer_play(computer_cards):
    """The computer will keep drawing cards as long as its score is less than 17."""
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())


def compare(user_score, computer_score):
    """Compares the user's score and the computer's score and determines the result."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a blackjack! You lose!"
    elif user_score == 0:
        return "You have a blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def get_user_input(prompt, valid_choices):
    """Gets validated user input based on the provided prompt and valid choices."""
    user_input = input(prompt).lower()
    while user_input not in valid_choices:
        user_input = input(f"Invalid input. {prompt}").lower()
    return user_input


def restart_game():
    """Prompt the user to restart or exit the game."""
    while True:
        user_choice = get_user_input(
            "Do you want to restart the game? Type 'Y' or 'N': ", ["y", "n"]
        )
        if user_choice == "n":
            print("Exiting the game...")
            break
        elif user_choice == "y":
            clear_screen()
            blackjack_game()


def clear_screen():
    """Clear the terminal screen and display the logo."""
    os.system("cls" if os.name == "nt" else "clear")
    print(black_logo)


def blackjack_game():
    # Initial dealing of cards
    player_cards, computer_cards = deal_initial_cards()

    game_over = False

    # Game loop for the player
    while not game_over:
        # Calculate scores
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Player's cards: {player_cards}, Score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game is over for the player
        if check_game_over(player_score):
            game_over = True
        else:
            should_continue = get_user_input(
                "Type 'y' to draw another card, 'n' to pass: ", ["y", "n"]
            )

            if should_continue == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn to play
    computer_play(computer_cards)

    # Final scores
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nFinal Player's cards: {player_cards}, Final Score: {player_score}")
    print(f"Final Computer's cards: {computer_cards}, Final Score: {computer_score}")

    # Determine the result using the compare function
    result = compare(player_score, computer_score)
    print(result)


def main():
    blackjack_game()
    restart_game()


if __name__ == "__main__":
    main()
