
tasks = []
next_id = 1


def add_task():
    global next_id

    description = input("Enter task description: ").strip()

    if not description:
        print("Task description cannot be empty.")
        return

    task = {
        "id": next_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")
    print(f"Task ID: {next_id}")

    next_id += 1


def view_tasks():
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"\nID     : {task['id']}")
        print(f"Task   : {task['description']}")
        print(f"Status : {task['status']}")


def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Task ID not found.")
        return

    description = input("Enter new task description: ").strip()

    if not description:
        print("Task description cannot be empty.")
        return

    task["description"] = description
    print("Task updated successfully!")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Task ID not found.")
    elif task["status"] == "Completed":
        print("Task is already completed.")
    else:
        task["status"] = "Completed"
        print("Task marked as completed!")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Task ID not found.")
    else:
        tasks.remove(task)
        print("Task deleted successfully!")
