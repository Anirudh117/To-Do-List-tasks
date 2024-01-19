import json
import os

TODO_FILE = 'todo.json'

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            try:
                todo_list = json.load(file)
            except json.JSONDecodeError:
                todo_list = []
    else:
        todo_list = []
    return todo_list

def save_todo(todo_list):
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)

def display_todo(todo_list):
    print("\nTo-Do List:")
    print("============")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['task']} {'(Completed)' if task['completed'] else ''}")

def add_task(todo_list, task):
    todo_list.append({'task': task, 'completed': False})
    save_todo(todo_list)
    print(f"Task '{task}' added to the to-do list.")

def delete_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        deleted_task = todo_list.pop(index - 1)
        save_todo(todo_list)
        print(f"Task '{deleted_task['task']}' deleted from the to-do list.")
    else:
        print("Invalid task index.")

def mark_completed(todo_list, index):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1]['completed'] = True
        save_todo(todo_list)
        print(f"Task marked as completed: '{todo_list[index - 1]['task']}'")
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_todo(todo_list)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            delete_task(todo_list, index)
        elif choice == '4':
            index = int(input("Enter the task index to mark as completed: "))
            mark_completed(todo_list, index)
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
