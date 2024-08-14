"""
Installation:
You can install the required packages using pip:

    pip install sv_ttk pywinstyles darkdetect
"""
import sv_ttk
import os
from functions import *
from functions_gui import *
import tkinter as tk
from tkinter import ttk



filePath = "todos.txt"

if not os.path.exists(filePath):
    with open(filePath, 'w') as f:
        pass


# Function to exit the application
def exit_application():
    root.destroy()

# Initialize the root window
root = tk.Tk()
root.title("My Todo List")

# Dark windows title
sv_ttk.set_theme("dark")
apply_theme_to_titlebar(root)

# Set the window size
window_width = 600
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Apply dark theme
sv_ttk.set_theme("dark")

# Title Label
title_label = ttk.Label(root, text="My Todo List", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(20, 10))

# Frame for input field and add button
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(pady=10, fill="x")

input_field = ttk.Entry(input_frame, width=40)
input_field.pack(side="left", padx=(0, 10), fill="x", expand=True)

add_button = ttk.Button(input_frame, text="Add", command=lambda: add_task(input_field, tasks_listbox, error_label))
add_button.pack(side="right")

# Frame for showing tasks and editing
tasks_frame = ttk.Frame(root, padding="10")
tasks_frame.pack(pady=10, fill="both", expand=True)

tasks_listbox = tk.Listbox(tasks_frame, height=15, width=70, selectmode=tk.SINGLE, bg="#2e2e2e", fg="#ffffff", borderwidth=0, highlightthickness=0)
tasks_listbox.pack(side="left", fill="both", expand=True)

# Scrollbar for tasks_listbox
scrollbar = ttk.Scrollbar(tasks_frame, command=tasks_listbox.yview)
scrollbar.pack(side="right", fill="y")
tasks_listbox.config(yscrollcommand=scrollbar.set)

# Frame for editing tasks
edit_frame = ttk.Frame(root, padding="10")
edit_frame.pack(pady=10, fill="x")

edit_field = ttk.Entry(edit_frame, width=40)
edit_field.pack(side="left", padx=(0, 10), fill="x", expand=True)

edit_button = ttk.Button(edit_frame, text="Edit", command=lambda: edit_or_submit_task(tasks_listbox, edit_field, error_label))
edit_button.pack(side="left", padx=5)

complete_button = ttk.Button(edit_frame, text="Complete", command=lambda: complete_task(tasks_listbox, error_label))
complete_button.pack(side="left", padx=5)

error_label = ttk.Label(root, foreground="red")
error_label.pack(pady=5)

# Exit Button
exit_button = ttk.Button(root, text="Exit", command=exit_application)
exit_button.pack(side="bottom", anchor="e", padx=10, pady=10)

# Show tasks on startup
show_tasks(tasks_listbox)

# Start the main loop
sv_ttk.set_theme("dark")
root.mainloop()

