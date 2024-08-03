tasks = []

def show_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter the task : ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if tasks :
        print("\nYour tasks: ")
        for i,task in enumerate(tasks, 1):
            print(f'{i}.{task}')
    else:
        print("no tasks saved")

def remove_task():
    view_tasks()
    remove_number = int(input('Enter the task number to remove'))
    if 0 < remove_number <= len(tasks):
        removed_task = tasks.pop(remove_number - 1)
        print(f'{removed_task} removed')
    else:
        print("Invalid input number")


while True:
    show_menu()
    choice = input("Choose an option : ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye break")
        break
    else:
        print("Invalid choice, please choose again.")
