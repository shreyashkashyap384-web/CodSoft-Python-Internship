# My To-Do List Program
# I learned lists and loops in class so I'm using them here

# This list will store all my tasks
my_tasks = []

# I use True so the loop runs forever until I break it
running = True

while running:

    # Showing the menu to the user
    print("\n--- TO-DO LIST ---")
    print("1. Add a task")
    print("2. See all tasks")
    print("3. Delete a task")
    print("4. Quit")

    # Asking the user what they want to do
    user_choice = input("What do you want to do? ")

    # If user picks 1, we add a task
    if user_choice == "1":
        new_task = input("Type your task: ")
        my_tasks.append(new_task)   # append adds to the end of list
        print("Task added!")

    # If user picks 2, we show all tasks
    elif user_choice == "2":

        # Check if the list is empty first
        if len(my_tasks) == 0:
            print("You have no tasks yet.")
        else:
            print("\nHere are your tasks:")
            # enumerate gives us a number and the item together
            for number, task in enumerate(my_tasks, start=1):
                print(number, ".", task)

    # If user picks 3, we delete a task
    elif user_choice == "3":

        if len(my_tasks) == 0:
            print("No tasks to delete.")
        else:
            # Show the tasks first so user knows the numbers
            for number, task in enumerate(my_tasks, start=1):
                print(number, ".", task)

            # Ask which number they want to remove
            pick = int(input("Enter task number to delete: "))

            # Make sure the number is valid
            if pick >= 1 and pick <= len(my_tasks):
                deleted_task = my_tasks.pop(pick - 1)  # pop removes by index
                print("Deleted:", deleted_task)
            else:
                print("That number doesn't exist!")

    # If user picks 4, stop the loop
    elif user_choice == "4":
        print("Bye!")
        running = False   # this stops the while loop

    # If they type something else
    else:
        print("Please enter 1, 2, 3, or 4 only.")