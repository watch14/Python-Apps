user_action = "add ".strip()
# Splitting the string by spaces
parts = user_action.split(" ")
print("parts",parts)  # Output: Hello World!


# Joining the list back into a string
todo = " ".join(parts[1:])
print("todo",todo)  # Output: Hello World!

if todo is "":
    task = input("Add a Task: ").strip().title()
    print(task)
    
