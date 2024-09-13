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


def update_task():
    """The function for updating the tasks"""
    title = input("Enter the task you want to update: ")
    for task in tasks:
        if task["title"] == title:
            new_description = input("Enter the new description: ")
            task["description"] = new_description
            new_status = input("Update your status: ")
            print(f"Task '{title}' updated successfully.")
            return
    print(f"{title.capitalize()} not found")


def display_task():
    """Function for displaying the current tasks"""
    if not tasks:
        print("There are no tasks available")
    else:
        print("\n Current Tasks")
        for i, task in enumerate(tasks, 1):
            print(
                f"{i}.Title: {task['title']}\n Description: {task['description']}\n Status: {task['status']}"
            )


def mark_completed_task():
    """The function shows the the current status"""
    title = input("Enter the task title to mark as completed: ")
    for task in tasks:
        if task["title"] == title:
            task["status"] = "Completed"
            print(f"Task '{title}' marked as completed.")
            return
    print(f"{title.capitalize()} not found")
