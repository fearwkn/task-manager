import json
import os

# -- TaskManager --#
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
# Save tasks to a JSON file
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        print("Tasks saved.")

# Load tasks from a JSON file
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded.")
        else:
            print("No saved tasks found.")

# Add a new task
    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append({"name": task, "done": False})
        self.save_tasks()
        more = input("Would you like to add another task? (y/n): ")
        if more.lower() == "y":
            self.add_task()
        else:
            print("Task(s) added.")

# View all tasks
    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks yet.")
            return

        print("Here are your tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['name']} [{status}]")

 # Update an existing task
    def update_task(self):
        self.view_tasks()
        index = int(input("Enter the task number to update: ")) - 1
        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        new_name = input("Enter the new task name: ")
        self.tasks[index]["name"] = new_name
        self.save_tasks()
        print("Task updated.")

# Mark a task as complete
    def mark_task_complete(self):
        self.view_tasks()
        index = int(input("Enter the task you completed: ")) - 1
        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        self.tasks[index]["done"] = True
        self.save_tasks()
        print(f"Task '{self.tasks[index]['name']}' marked as complete.")

# Delete a task
    def delete_task(self):
        self.view_tasks()
        index = int(input("Enter the task number to delete: ")) - 1
        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        deleted = self.tasks.pop(index)
        self.save_tasks()
        print(f"Task '{deleted['name']}' deleted.")

# Main menu for the task manager
    def run(self):
        while True:
            print("\nTask Manager Menu")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Mark task as Complete")
            print("5. Delete task")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.mark_task_complete()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

# Launch the app
if __name__ == "__main__":
    app = TaskManager()
    app.run()
