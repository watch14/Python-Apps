print("Welcom to your Todo List!")
tasks= ['eat', 'sleep', 'repeat']

while True :
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()
    
    match user_action:
        case 'add':
            todo = input("Enter a Task: ").strip()
            tasks.append(todo)
            
        case 'show':
            for index, item in enumerate(tasks):
                print(f"{index+1}. {item}")
            
        case 'edit':
            nb = int(input("Enter the number of the task to edit: ").strip())
            if 1 <= nb <= len(tasks):
                edited = input(f"Edit {tasks[nb - 1]}: ")
                tasks[nb - 1] = edited
            else:
                print(f"Out of range the number should be between 1 and {len(tasks)}")
                
        case 'complete':
            nb = int(input("Enter the number of the task that u Completed: ").strip())
            if 1 <= nb <= len(tasks):
                print(f"Task {tasks[nb - 1]} is Complete Well Done!!!")
                tasks.pop(nb - 1)
            else:
                print(f"Out of range the number should be between 1 and {len(tasks)}")

        case 'exit':
            break
        
        case _:
            print("Invalid action!")

print(f"******\nYou quit your Todo List!!\nThese are your {len(tasks)} Tasks: {tasks}  \n******")