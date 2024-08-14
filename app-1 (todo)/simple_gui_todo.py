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
    
    todos = getTodos(filePath)
    
    print("event:",event)
    print("values:",values)

    if event == "Add":
        # Handle the Add button click
        todo_item = values['-TODO-'].strip().title() + "\n"
        todos.append(todo_item)
        
        saveFile(filePath, todos)
        window['-TODOS-'].update(values=todos)
        
        
    elif event == "Edit":
        todoToEdit = values["-TODOS-"][0]
        todoEdited= values['-TODO-'].strip().title() + "\n"
        
        i = todos.index(todoToEdit)
        todos[i] = todoEdited
        
        saveFile(filePath, todos)
        window['-TODOS-'].update(values=todos)
        
        
    elif event == "Complete":
        todoToEdit = values["-TODOS-"][0]
        
        i = todos.index(todoToEdit)
        todos.pop(i)
        
        saveFile(filePath, todos)
        
        window['-TODOS-'].update(values=todos)
            
    elif event == "-TODOS-":
        window['-TODO-'].update(value=values["-TODOS-"][0].strip())
        
    elif event == sg.WIN_CLOSED:
        break

window.close()
