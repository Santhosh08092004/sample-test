
import os

folder = "To-do"

if not os.path.exists(folder):
    os.mkdir(folder)


def add_task():
    name = input("Enter task name: ").strip()

    if name == "":
        print("Task name cannot be empty!")
        return

    filename = name.replace(" ", "_") + ".txt"
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        print("Task already exists!")
        return

    with open(path, "w") as file:
        file.write("Task: " + name + "\n")
        file.write("Status: Pending\n")

    print("Task created successfully!")


def view_tasks():
    files = os.listdir(folder)

    if not files:
        print("No tasks found!")
        return

    for filename in files:
        path = os.path.join(folder, filename)

        with open(path, "r") as file:
            print("\n" + file.read())


def find_task():
    name = input("Enter task name: ").strip()
    filename = name.replace(" ", "_") + ".txt"
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        return path

    print("Task not found!")
    return None


def update_task():
    path = find_task()

    if path is None:
        return

    new_name = input("Enter new task name: ").strip()

    if new_name == "":
        print("Task name cannot be empty!")
        return

    with open(path, "r") as file:
        content = file.readlines()

    status = content[1].strip()

    new_path = os.path.join(
        folder, new_name.replace(" ", "_") + ".txt"
    )

    if os.path.exists(new_path) and new_path != path:
        print("A task with that name already exists!")
        return

    with open(new_path, "w") as file:
        file.write("Task: " + new_name + "\n")
        file.write(status + "\n")

    if path != new_path:
        os.remove(path)

    print("Task updated successfully!")


def complete_task():
    path = find_task()

    if path is None:
        return

    with open(path, "r") as file:
        content = file.readlines()

    if content[1].strip() == "Status: Completed":
        print("Task is already completed!")
        return

    content[1] = "Status: Completed\n"

    with open(path, "w") as file:
        file.writelines(content)

    print("Task completed successfully!")


def delete_task():
    path = find_task()

    if path is not None:
        os.remove(path)
        print("Task deleted successfully!")
