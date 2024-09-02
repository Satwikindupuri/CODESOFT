tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted!")
    else:
        print("Invalid task number!")

# Main program loop
while True:
    print("\nOptions: 1. Add Task 2. View Tasks 3. Delete Task 4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option (1-4).")
