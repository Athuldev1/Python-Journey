import os
from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2 if n2 != 0 else "Error: Division by zero is not allowed."


def mul(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def get_number(prompt):
    """Prompt the user for a valid number and return it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! It must be a number. Please try again.")


def get_operation():
    """Prompt the user to select a valid operation and return it."""
    while True:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        if operation in operations:
            return operation
        print("Invalid operation! Please select only from the available options.")


def handle_user_decision(result):
    """Handle the user's decision to continue, start a new calculation, or exit the program."""
    decisions = {"Y": "continue", "N": "new", "S": "stop"}
    while True:
        decision = input(
            f"Type 'Y' to continue calculating with {result}, 'N' to start a new operation, or 'S' to stop the program: "
        ).upper()
        if decision == "S":
            confirmation = input("Are you sure you want to exit? Type 'Y' to confirm, 'N' to continue: ").upper()
            if confirmation == "Y":
                return decisions[decision]
            print("Continuing with the calculator...")
        elif decision in decisions:
            return decisions[decision]
        else:
            print("Invalid input! Please choose 'Y', 'N', or 'S'.")


def clear_screen():
    """Clear the terminal screen and display the logo."""
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


def calculator():
    """Main calculator function that controls the flow of operations."""
    clear_screen()
    first_number = get_number("Enter the first number: ")

    while True:
        operation = get_operation()
        second_number = get_number(f"Enter the second number to {operation} with {first_number}: ")
        result = operations[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}")

        decision = handle_user_decision(result)
        if decision == "continue":
            first_number = result
        elif decision == "new":
            clear_screen()
            first_number = get_number("Enter a new first number: ")
        elif decision == "stop":
            print("Exiting...")
            break


if __name__ == "__main__":
    calculator()
