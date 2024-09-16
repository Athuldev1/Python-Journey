tasks = []

PENDING = "Pending"
COMPLETED = "Completed"


def find_task_by_title(title):
    """Helper function to find a task by title."""
    for task in tasks:
        if task["title"].lower() == title.lower():
            return task
    return None


def add_task():
    """The function adds tasks to the app."""
    title = input("Enter your task title: ")
    description = input("Enter the description: ")
    task = {"title": title, "description": description, "status": PENDING}
    tasks.append(task)
    print(f"Task '{title}' added successfully.")


def remove_task():
    """Remove a task from the list."""
    title = input("Enter the task title to remove: ")
    task = find_task_by_title(title)

    if task:
        tasks.remove(task)
        print(f"Task '{title}' removed successfully.")
    else:
        print(f"No active tasks with the title '{title}' found.")


def update_task():
    """The function for updating the tasks."""
    title = input("Enter the task you want to update: ")
    task = find_task_by_title(title)

    if task:
        task["description"] = input("Enter the new description: ")
        task["status"] = input(
            "Update your status (Pending/Completed): ").capitalize()
        print(f"Task '{title}' updated successfully.")
    else:
        print(f"{title.capitalize()} not found.")


def display_task():
    """Function for displaying the current tasks."""
    if not tasks:
        print("There are no tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, 1):
            print(
                f"{i}. Title: {
                    task['title']}\n   Description: {
                    task['description']}\n   Status: {
                    task['status']}\n")


def mark_completed_task():
    """The function to mark a task as completed."""
    title = input("Enter the task title to mark as completed: ")
    task = find_task_by_title(title)

    if task:
        task["status"] = COMPLETED
        print(f"Task '{title}' marked as completed.")
    else:
        print(f"{title.capitalize()} not found.")


def search_task():
    """The function that searches tasks."""
    if not tasks:
        print("No tasks available to search.")
        return

    print("Search filter\n")
    title = input("Enter the title name to search: ").lower()
    status = input("Enter the status: (Pending or Completed)").capitalize()

    if status not in [PENDING, COMPLETED]:
        print("Invalid status. Please enter 'Pending' or 'Completed'.")
        return

    found = False
    for i, task in enumerate(tasks, 1):
        if title in task["title"].lower() and task["status"] == status:
            print(
                f"{i}. Title: {
                    task['title']}\n   Description: {
                    task['description']}\n   Status: {
                    task['status']}\n")
            found = True

    if not found:
        print(
            f"No tasks found with the title containing '{title}' and status '{status}'.")
