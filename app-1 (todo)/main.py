print("Welcom to your Todo List!")
tasks= []

while True :
    user_action = input("Type add, show or exit: ")
    
    match user_action:
        case 'add':
            todo = input("Enter a Task: ")
            tasks.append(todo)
        case 'show':
            print(tasks)
        case 'exit':
            break

print(f"******\nYou quit your Todo List.\nThese are your Tasks: {tasks} \n******")