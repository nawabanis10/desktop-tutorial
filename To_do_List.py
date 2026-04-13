TASK_FILE="task.txt"

task = []

 
while True:

    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. Show task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'add task' or choice == '1':
        user_input = input("Enter your task: ").strip()
        task.append(user_input)

        file=open(TASK_FILE,'a')
        file.write(user_input + '\n')
        file.close()

        print("Task added ✔️")

    elif choice == 'show task' or choice == '2':
        if len(task) == 0:
            print("No task available ❌")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(task, start=1):
                print(f"{i}. {t}")

    elif choice == 'delete task' or choice == '3':
        if len(task) == 0:
            print("No task to delete ❌")
        else:
            for i, t in enumerate(task, start=1):
                print(f"{i}. {t}")

            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(task):
                    removed = task.pop(index - 1)
                    print(f"Deleted: {removed} ✔️")
                else:
                    print("Invalid number ❌")
            except:
                print("Please enter a valid number ❌")

    elif choice == 'exit' or choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice ❌")



 