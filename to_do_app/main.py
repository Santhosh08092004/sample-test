
import user_options as uo


def main():
    while True:
        print("\n===== TODO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            uo.add_task()
        elif choice == "2":
            uo.view_tasks()
        elif choice == "3":
            uo.update_task()
        elif choice == "4":
            uo.complete_task()
        elif choice == "5":
            uo.delete_task()
        elif choice == "6":
            print("Thank you for using the ToDo Application!")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
