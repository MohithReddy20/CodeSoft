tasks = []
statuses = []

def add_task(task):
    tasks.append(task)
    statuses.append("Incomplete")
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, (task, status) in enumerate(zip(tasks, statuses), 1):
            print(f"{i}. {task} - {status}")

def remove_task(task_index):
    try:
        task = tasks.pop(task_index - 1)
        statuses.pop(task_index - 1)
        print(f"'{task}' removed.")
    except IndexError:
        print("Invalid task number.")

def mark_task_completed(task_index):
    try:
        statuses[task_index - 1] = "Completed"
        print(f"Task {task_index} marked as completed.")
    except IndexError:
        print("Invalid task number.")

def update_task(task_index, new_task):
    try:
        tasks[task_index - 1] = new_task
        print(f"Task {task_index} updated.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Update Task")
        print("6. Exit")
    
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task numbber to remove: "))
            remove_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to mark as completed: "))
            mark_task_completed(task_index)
        elif choice == '5':
            task_index = int(input("Enter task number to update: "))
            new_task = input("Enter new task to update: ")
            update_task(task_index, new_task)
        elif choice == '6':
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()