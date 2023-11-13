def show_name(name):
    return f"Hello, {name}!"

def main():
    user_name = input("Enter your name: ")
    greeting = show_name(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
def show_name(name):
    return f"Hello, {name}!"

def main():
    useclass TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' completed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to complete: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()r_name = input("Enter your name: ")
    greeting = show_name(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
