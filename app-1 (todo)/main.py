user_prompt = "Enter another task or type 'x' to exit: "

tasks= []
while True :
    task = input(user_prompt)
    if task == "x":
        break
    tasks.append(task)

print(tasks)