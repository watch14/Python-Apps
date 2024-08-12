print("Welcom to your Todo List!")


while True :
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    
    f= open("todos.txt", "r")
    todos = f.readlines()
    f.close()
            
    match user_action:
        case 'add':
            todo = input("Enter a Task: ").strip().title() + '\n'

            todos.append(todo)
            
            f = open("todos.txt", "w")
            f.writelines(todos)
            f.close()
            
        case 'show':

            print("Your todos:")
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

            
        case 'edit':
            nb = int(input("Enter the number of the task to edit: ").strip())
            if 1 <= nb <= len(todos):
                edited = input(f"Edit {todos[nb - 1]}: ")
                todos[nb - 1] = edited
            else:
                print(f"Out of range the number should be between 1 and {len(todos)}")
                
        case 'complete':
            nb = int(input("Enter the number of the task that u Completed: ").strip())
            if 1 <= nb <= len(todos):
                print(f"Task {todos[nb - 1]} is Complete Well Done!!!")
                todos.pop(nb - 1)
            else:
                print(f"Out of range the number should be between 1 and {len(todos)}")

        case 'exit':
            break
        
        case _:
            print("Invalid action!")
            
print("***************")
print(f"You quit your Todo List!!\n")
print(f"These are your {len(todos)} todos: {todos}")
print("***************")
