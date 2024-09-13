from todo import add_task, remove_task, update_task, display_task, mark_completed_task


def main_menu():
    """Display the main menu and handle user input."""
    print("\n=== To-Do List Application ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Mark Task as Completed")
    print("6. Exit")

    try:
        choice = input("Enter your choice (1-6): ")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        display_task()
    elif choice == "5":
        mark_completed_task()
    elif choice == "6":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")


while True:
    main_menu()
