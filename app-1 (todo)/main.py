print("-------------------------")
print("Welcom to your Todo List!")
print("-------------------------")

while True :
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    
    with open("files/todos.txt", "r") as f:
        todos = f.readlines()
        
    todo_list = [item.strip('\n') for item in todos]
            
    # Add tasks
    if user_action.startswith("add"):
        parts = user_action.split(" ")
        todo = " ".join(parts[1:]).title()
        if todo is "":
            todo = input("Add a Task: ").strip().title()
            
        todos.append(todo + "\n")
        
        with open("files/todos.txt", "w") as f:
            f.writelines(todos)
        
    # Show all task
    elif user_action == "show":
        #print all tasks
        print("Your todos:")
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")

    # Edit task
    elif user_action.startswith("edit"):
        try:
            parts = user_action.split(" ")
            if len(parts) > 1 and parts[1].isdigit():
                nb = int(parts[1])
            else:
                nb = int(input("Add the number of the task to Edit it: ").strip())
                
            if 1 <= nb <= len(todos):
                edited = input(f"Edit {todo_list[nb - 1]} : ").strip().title() + '\n'
                todos[nb - 1] = edited
                
                #save/overwrite todos to the file
                with open("files/todos.txt", "w") as f:
                    f.writelines(todos)
                    
            else:
                print(f"Out of range the number should be between 1 and {len(todos)}")
                
        except KeyboardInterrupt as e:
            print(f"An error occurred: {e}")
            
            
    # Complete task
    elif user_action.startswith("complete"):
        
        parts = user_action.split(" ")
        if len(parts) > 1 and parts[1].isdigit():
            nb = int(parts[1])
        else:
            nb = int(input("Add the number of the task that u Completed: ").strip())
        
        if 1 <= nb <= len(todos):
            print(f"Task {todo_list[nb - 1]} is Complete Well Done!!!")
            todos.pop(nb - 1)
            #save/overwrite todos to the file
            with open("files/todos.txt", "w") as f:
                f.writelines(todos)

        else:
            print(f"Out of range the number should be between 1 and {len(todos)}")

    # Exit
    elif user_action.startswith("exit"):
        print()
        print("**********")
        print()

        print(f"You quit your Todo List!!\n")
        print(f"These are your {len(todos)} todos: {todo_list}")

        print()
        print("**********")
        print()
        break
    
    else:
        print("Invalid Action!")