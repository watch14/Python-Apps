import PySimpleGUI as sg
from functions import *
from functions_gui import *


filePath = "files/todos.txt"
fonts = ('Helvetica', 10)
# Define the layout
layout = [
    [sg.Text("", key='-TIME-')],
    [sg.Text("My To-Do List")],
    [sg.InputText(key='-TODO-'), sg.Button("Add")],
    [sg.Listbox(values=getTodos(filePath), key='-TODOS-',
                enable_events=True, size=[49, 10])],
    [sg.Button("Edit"), sg.Button("Complete")],
]


# Create the window
window = sg.Window("To-Do List", layout, font=fonts)

while True:
    event, values = window.read(timeout=100)
    time = currentTime()
    window['-TIME-'].update(value=time)
    
    todos = getTodos(filePath)
    
    # print("event:",event)
    # print("values:",values)

    if event == "Add":
        # Handle the Add button click
        todo_item = values['-TODO-'].strip().title() + "\n"
        todos.append(todo_item)
        
        saveFile(filePath, todos)
        window['-TODOS-'].update(values=todos)
        window['-TODO-'].update(value='')
        
        
    elif event == "Edit":
        try:
            todoToEdit = values["-TODOS-"][0]
            todoEdited= values['-TODO-'].strip().title() + "\n"
            
            i = todos.index(todoToEdit)
            todos[i] = todoEdited
            
            saveFile(filePath, todos)
            window['-TODOS-'].update(values=todos)
            window['-TODO-'].update(value='')
        except IndexError:
            sg.popup("Select a task to Edit!", font=fonts)
        
        
    elif event == "Complete":
        try:
            todoToEdit = values["-TODOS-"][0]
            
            i = todos.index(todoToEdit)
            todos.pop(i)
            
            saveFile(filePath, todos)
            
            window['-TODOS-'].update(values=todos)
            window['-TODO-'].update(value='')
        except IndexError:
            sg.popup("Select a task to Complete!", font=fonts)
         
            
    elif event == "-TODOS-":
        window['-TODO-'].update(value=values["-TODOS-"][0].strip())
        
    elif event == sg.WIN_CLOSED:
        break

window.close()
