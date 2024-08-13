print("-------------------------")
print("Welcom to your Todo List!")
print("-------------------------")

while True :
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    
    with open("files/todos.txt", "r") as f:
        todos = f.readlines()
        
    todo_list = [item.strip('\n') for item in todos]
            
    if 'add' in user_action:
        parts = user_action.split(" ")
        todo = " ".join(parts[1:]).title()

        todos.append(todo)
        
        with open("files/todos.txt", "w") as f:
            f.writelines(todos)
        
    elif 'show' in user_action:
        #print all of the tasks
        print("Your todos:")
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")

    elif 'edit' in user_action:
        
        parts = user_action.split(" ")
        nb = int(" ".join(parts[1:]))
            
        if 1 <= nb <= len(todos):
            edited = input(f"Edit {todo_list[nb - 1]} : ").strip().title() + '\n'
            todos[nb - 1] = edited
            #save/overwrite todos to the file
            with open("files/todos.txt", "w") as f:
                f.writelines(todos)
                
        else:
            print(f"Out of range the number should be between 1 and {len(todos)}")
            
    elif 'complete' in user_action:
        
        parts = user_action.split(" ")
        nb = int(" ".join(parts[1:]))
        
        if 1 <= nb <= len(todos):
            print(f"Task {todo_list[nb - 1]} is Complete Well Done!!!")
            todos.pop(nb - 1)
            #save/overwrite todos to the file
            with open("files/todos.txt", "w") as f:
                f.writelines(todos)

        else:
            print(f"Out of range the number should be between 1 and {len(todos)}")

    elif 'exit' in user_action:
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
        print("Invalid action!")