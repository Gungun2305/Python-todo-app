# TO-DO List Application...

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task,tasks):
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")

def remove_task(index,tasks):
    try:
        task = tasks[index]
        confirm = input(f"Are you sure you want to remove '{task}'? (y/n): ").lower()
        if confirm == 'y':
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task removed: {removed}")
        else:
            print("Task not removed.")
    except IndexError:
        print("Invalid task number.")

def mark_done(index,tasks):
    try:
        if tasks[index].endswith("✅"):
            print("Task is already marked as done.")
        else:
            tasks[index] += " ✅"
            save_tasks(tasks)
            print(f"🎉 Task marked as done: {tasks[index]}")
    except IndexError:
        print("⚠️ Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("📋 Your To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            add_task(task, tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index, tasks)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(index, tasks)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting To-Do List App. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
