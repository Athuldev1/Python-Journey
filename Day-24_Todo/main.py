from todo import add_task, remove_task


def main_menu():
    """Display the main menu and handle user input."""
    print("\n=== To-Do List Application ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    else:
        print("Invalid choice. Please try again.")

while True:
    main_menu()
