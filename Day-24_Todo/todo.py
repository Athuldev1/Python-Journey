tasks = []


def add_task():
    """The function adds the tasks to the app"""
    title = input("Enter your task title: ")
    description = input("Enter the description: ")
    task = {"title": title, "description": description, "status": "Pending"}
    tasks.append(task)
    print(f"Task '{title}' added successfully.")


def remove_task():
    """Remove a task from the list."""
    title = input("Enter the task title to remove: ")

    # Filter tasks to exclude the one with the given title
    global tasks
    updated_tasks = [task for task in tasks if task["title"] != title]

    # Check if any tasks were removed
    if len(updated_tasks) == len(tasks):
        print("There are no active tasks with the specified title.")
    else:
        tasks = updated_tasks
        print(f"Task '{title}' removed successfully.")
