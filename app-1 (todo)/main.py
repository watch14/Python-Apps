print("Welcom to your Todo List!")
tasks= ['eat', 'sleep', 'repeat']

while True :
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip().lower()
    
    match user_action:
        case 'add':
            todo = input("Enter a Task: ")
            tasks.append(todo)
        case 'show':
            print(tasks)
        case 'edit':
            nb = int(input("Enter the nomber of the task to edit: "))
            if nb >= len(tasks):
                print(f"Out of range the number should be no more than {len(tasks)}")
                
            print(tasks[nb])
        case 'exit':
            break

print(f"******\nYou quit your Todo List!!\nThese are your Tasks: {tasks} \n******")