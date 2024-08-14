import PySimpleGUI as sg
from functions import *
from functions_gui import *


filePath = "files/todos.txt"

# Define the layout
layout = [
    [sg.Text(currentTime())],
    [sg.Text("To-Do List")],
    [sg.InputText(key='-TODO-'), sg.Button("Add")],
    [sg.Listbox(values=getTodos(filePath), key='-TODOS-',
                enable_events=True, size=[49, 10])],
    [sg.Button("Edit"), sg.Button("Complete")],
]


# Create the window
window = sg.Window("To-Do List", layout, font=('Helvetica', 10))

while True:
    event, values = window.read()
    print("event:",event)
    print("values:",values)

    if event == "Add":
        # Handle the Add button click
        todos = getTodos(filePath)
        todo_item = values['-TODO-'].strip().title() + "\n"
        todos.append(todo_item)
        
        saveFile(filePath, todos)
        
        
    elif event == "Edit":
        todoToEdit = values["-TODOS-"]
        # todoToEdit = todoToEdit[0].strip("\n")
        todoEdited= values['-TODO-'].strip().title() + "\n"
        
        todos = getTodos(filePath)
        for i, item in enumerate(todos):
            if item in todoToEdit:
                todos[i] = todoEdited
        
        print(todos)
        saveFile(filePath, todos)
        
        
    elif event == "Complete":
        todoToEdit = values["-TODOS-"]
        # todoToEdit = todoToEdit[0].strip("\n")
        todoEdited= values['-TODO-'].strip().title() + "\n"
        
        todos = getTodos(filePath)
        for i, item in enumerate(todos):
            if item in todoToEdit:
                todos.pop(i)
        
        print(todos)
        saveFile(filePath, todos)
            
    
    elif event == sg.WIN_CLOSED:
        break

window.close()
