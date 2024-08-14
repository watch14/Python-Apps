import PySimpleGUI as sg
from functions import *
from functions_gui import *

# Define the layout
layout = [
    [sg.Text("To-Do List")],
    [sg.InputText(key='-INPUT-'), sg.Button("Add")]
]


# Create the window
window = sg.Window("To-Do List", layout, font=('Helvetica', 10))

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add":
        # Handle the Add button click
        todo_item = values['-INPUT-']
        print(f"Added: {todo_item}")

window.close()
