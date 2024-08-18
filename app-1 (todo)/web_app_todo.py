import streamlit as st
from functions import getTodos, saveFile, currentTime

# File paths for the to-do lists
todosFile = "todos.txt"
doneTodosFile = "done_todos.txt"

# Load existing tasks
todos = getTodos(todosFile)
doneTodos = getTodos(doneTodosFile)

# Function to add a new task
def addTodo():
    todo = st.session_state["newTodo"]
    if todo.strip():  # Only add non-empty tasks
        todos.append(todo.strip().title() + "\n")
        saveFile(todosFile, todos)
        st.session_state["newTodo"] = ""  # Clear the input field

# App header
st.write("""
         # My To-Do App
         ###### Improve your productivity!
         """)

# Input for adding new tasks
st.text_input(label="Add Task:", placeholder="Add Task:",
              label_visibility="collapsed", on_change=addTodo,
              key="newTodo")

# Display tasks to be done
st.write("Tasks that need to be done:")

# List the current tasks with checkboxes, allowing duplicates
for i, item in enumerate(todos):
    checkbox = st.checkbox(item, key=f"{item}_{i}")  # Unique key by adding the index
    if checkbox:
        # Move the task to the done list
        doneTodos.append(todos[i])
        saveFile(doneTodosFile, doneTodos)
        
        # Remove the task from the to-do list
        todos.pop(i)
        saveFile(todosFile, todos)
        
        # Clear the session state for the checkbox
        del st.session_state[f"{item}_{i}"]
        st.rerun()  # Rerun to refresh the task list

# Separator and display of done tasks
st.markdown("---")
st.write("###### Done tasks, well done!")

# Display completed tasks with unique keys
for i, item in enumerate(doneTodos):
    st.checkbox(item, value=True, disabled=True, key=f"done_{item}_{i}")
