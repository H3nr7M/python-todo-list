# Description: A simple todo list program
# To add a sleep time for more user friendly experience
import time

# define the list to hold the tasks
tasks = []

# define a function to add a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: {task}")
    print()

# define a function to remove a task from the list
def remove_task():
    print('Your actual tasks are:')
    for i, task in enumerate(tasks):
        print(f"Index: {i}. {task}")
    task_index = int(input("Enter the index of the task to remove: "))
    task = tasks.pop(task_index)
    print(f"Removed task: {task}")
    print()

# define a function to print the current list of tasks
def print_tasks():
    print("Current tasks are:")
    for i, task in enumerate(tasks):
        print(f"Index: {i}. {task}")
    print()
    time.sleep(1)

# define a function to show the menu of options
def show_menu():
    print("Please select an option:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Print tasks")
    print("4. Exit")

# show the initial menu of options
show_menu()

# loop until the user chooses to exit
while True:
    choice = int(input("Enter option number: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        print_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid option")
    
    # show the menu of options again
    show_menu()

print("Goodbye!")
