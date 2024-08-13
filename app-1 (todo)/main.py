from functions import *
print("-------------------------")
print("Welcom to your Todo List!")
print("-------------------------")

while True :
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    
    todos = getTodos("files/todos.txt")
            
    # Add tasks
    if user_action.startswith("add"):
        parts = user_action.split(" ")
        todo = " ".join(parts[1:]).title()
        if todo is "":
            todo = input("Add a Task: ").strip().title()
            
        todos.append(todo + "\n")
        
        saveFile("files/todos.txt", todos)
            

        
    # Show all task
    elif user_action == "show":
        #print all tasks
        printToods("files/todos.txt")

    # Edit task
    elif user_action.startswith("edit"):
        try:
            parts = user_action.split(" ")
            if len(parts) > 1 and parts[1].isdigit():
                nb = int(parts[1])
            else:
                nb = int(input("Add the number of the task to Edit it: ").strip())
                
            if 1 <= nb <= len(todos):
                edited = input(f"Edit {todos[nb - 1].strip("\n")} : ").strip().title() + '\n'
                todos[nb - 1] = edited
                
                #save/overwrite todos to the file
                saveFile("files/todos.txt", todos)
                    
            else:
                print(f"Out of range the number should be between 1 and {len(todos)}")
                
        except Exception as e:
            print(f"An error occurred: {e}")
            
            
    # Complete task
    elif user_action.startswith("complete"):
        
        parts = user_action.split(" ")
        try:
            if len(parts) > 1 and parts[1].isdigit():
                nb = int(parts[1])
            else:
                nb = int(input("Add the number of the task that u Completed: ").strip())
            
            if 1 <= nb <= len(todos):
                print(f"Task {todos[nb - 1].strip("\n")} is Complete Well Done!!!")
                todos.pop(nb - 1)
                #save/overwrite todos to the file
                saveFile("files/todos.txt", todos)

            else:
                print(f"Out of range the number should be between 1 and {len(todos)}")
                
        except Exception as e:
            print(f"An error occurred: {e}")

    # Exit
    elif user_action == "exit":
        print()
        print("**********")
        print()
        print(f"You quit your Todo List!!\n")
        print(f"These are your {len(todos)} todos: {todos}")
        print()
        print("**********")
        print()
        break
    
    else:
        print("Invalid Action!")