import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Loads tasks from the todo.txt file."""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    """Saves tasks to the todo.txt file."""
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    """Displays all tasks with their corresponding numbers."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("-----------------------")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def update_task(tasks):
    """Updates an existing task."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input(f"Enter the new description for task '{tasks[task_num - 1]}': ").strip()
            if new_task:
                tasks[task_num - 1] = new_task
                save_tasks(tasks)
                print(f"Task {task_num} updated to '{new_task}'.")
            else:
                print("Task description cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("-----------------------")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()