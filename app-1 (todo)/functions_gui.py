#titel bar gui black
import pywinstyles
import sys
import sv_ttk
from functions import *
from functions_gui import *
import tkinter as tk
from tkinter import ttk




def apply_theme_to_titlebar(root):
    """
    Applies a theme to the window title bar based on the current Windows version and sv_ttk theme.

    Parameters:
    root (Tk): The main Tkinter window.
    """
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        # Set the title bar color for better appearance on Windows 11
        color = "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa"
        pywinstyles.change_header_color(root, color)
    elif version.major == 10:
        # Apply style to the title bar on Windows 10
        theme = "dark" if sv_ttk.get_theme() == "dark" else "normal"
        pywinstyles.apply_style(root, theme)

        # Force the window to update its title bar color
        root.update_idletasks()
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)


# File path for the todo list
filePath = "files/todos.txt"

# Global variable to track edit mode
is_editing = False
edit_index = None

# Function to add a task
def add_task(input_field, tasks_listbox, error_label):
    todo = input_field.get().strip().title()
    if todo:
        todos = getTodos(filePath)
        todos.append(todo + "\n")
        saveFile(filePath, todos)
        input_field.delete(0, tk.END)  # Clear the input field
        show_tasks(tasks_listbox)  # Refresh the task display
        error_label.config(text="")  # Clear any previous error messages
    else:
        error_label.config(text="Task cannot be empty.")

# Function to show tasks in the Listbox
def show_tasks(tasks_listbox):
    todos = getTodos(filePath)
    tasks_listbox.delete(0, tk.END)  # Clear current content
    for index, item in enumerate(todos):
        tasks_listbox.insert(tk.END, f"{index + 1}. {item.strip()}")

# Function to toggle edit mode and populate the edit_field widget
def edit_or_submit_task(tasks_listbox, edit_field, error_label):
    global is_editing, edit_index

    if not is_editing:
        selected_index = tasks_listbox.curselection()
        if selected_index:
            edit_index = selected_index[0]
            todos = getTodos(filePath)
            selected_task = todos[edit_index].strip()
            edit_field.delete(0, tk.END)
            edit_field.insert(0, selected_task)
            is_editing = True
            error_label.config(text="")  # Clear any previous error messages
        else:
            error_label.config(text="Please select a task to edit.")
    else:
        edited_task = edit_field.get().strip().title() + '\n'
        if edited_task:
            todos = getTodos(filePath)
            todos[edit_index] = edited_task
            saveFile(filePath, todos)
            show_tasks(tasks_listbox)  # Refresh the task display
            edit_field.delete(0, tk.END)  # Clear the edit field
            is_editing = False
            edit_index = None
            error_label.config(text="")  # Clear any previous error messages
        else:
            error_label.config(text="Task cannot be empty.")

# Function to complete a task
def complete_task(tasks_listbox, error_label):
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        todos = getTodos(filePath)
        todos.pop(index)
        saveFile(filePath, todos)
        show_tasks(tasks_listbox)  # Refresh the task display
        error_label.config(text="")  # Clear any previous error messages
    else:
        error_label.config(text="Please select a task to complete.")