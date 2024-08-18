import streamlit as st
import pandas as pd
import os
import datetime
from functions import getTodos, saveFile

# File paths for the to-do lists, completed tasks, and archives
todosFile = "files/todos.txt"
doneTodosFile = "files/done_todos.txt"
todosDoneExcelFile = "files/todos_done_summary.xlsx"
archiveExcelFile = "files/archived_tasks.xlsx"



# Determine today’s date
today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

# Function to reset the done list
def resetDailyDoneList():
    if not os.path.exists(doneTodosFile) or not os.path.getsize(doneTodosFile):
        with open(doneTodosFile, 'w') as f:
            f.write("")

# Function to add a new task
def addTodo():
    todo = st.session_state["newTodo"]
    if todo.strip():
        todos.append(todo.strip().title() + "\n")
        saveFile(todosFile, todos)
        st.session_state["newTodo"] = ""

# Reset the done list for today
resetDailyDoneList()

# Load existing tasks
todos = getTodos(todosFile)
doneTodos = getTodos(doneTodosFile)

# App header
st.write("""
         # My Daily To-Do App
         ###### Improve your productivity each day!
         """)

# Input for adding new tasks
st.text_input(label="Add Task:", placeholder="Add Task:",
              label_visibility="collapsed", on_change=addTodo,
              key="newTodo")

# Display tasks to be done
st.write("Tasks that need to be done:")

# List the current tasks with checkboxes
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

# Separator
st.markdown("---")


# Calculate counts
completed_count = len(doneTodos)
total_count = completed_count + len(todos)
completion_percentage = (completed_count / total_count) if total_count > 0 else 0

# Display progress bar
st.write(f"## Task Completion Progress: {completed_count}/{total_count} tasks completed")
st.progress(completion_percentage)

# Motivational message
if completed_count > 0:
    completion_ratio = completed_count / total_count
    if completion_ratio > 0.75:
        st.write("### Fantastic job! You've completed a significant portion of your tasks. You're doing great!")
    elif completion_ratio > 0.50:
        st.write("### Well done! You've completed more than half of your tasks. Keep pushing forward!")
    elif completion_ratio > 0.25:
        st.write("### Good work! You've made solid progress. Keep working to reach your goal!")
    else:
        st.write("### Keep going! You've made a good start. Stay focused and continue making progress!")
else:
    st.write("### Get started! Add some tasks and start working towards your goals!")

# Archive completed tasks at the end of the day
st.markdown("---")
st.write(f"### Archived Tasks for {today_str}")


# Save todos and doneTodos to Excel
def save_todos_done_to_excel():
    # Create DataFrames
    df_todos = pd.DataFrame(todos, columns=["To-Do Tasks"])
    df_doneTodos = pd.DataFrame(doneTodos, columns=["Completed Tasks"])
    
    # Write to Excel file
    with pd.ExcelWriter(todosDoneExcelFile, mode='w', engine='openpyxl') as writer:
        df_todos.to_excel(writer, sheet_name='To-Do Tasks', index=False)
        df_doneTodos.to_excel(writer, sheet_name='Completed Tasks', index=False)

# Call the function to save todos and doneTodos to Excel
save_todos_done_to_excel()

# Save archived tasks to Excel
def save_archived_to_excel():
    # Read existing Excel file if it exists
    if os.path.exists(archiveExcelFile):
        with pd.ExcelFile(archiveExcelFile) as xls:
            # Read existing sheets into a dictionary
            sheet_dict = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
    else:
        sheet_dict = {}

    # Create DataFrame for today's archived tasks
    df_archive = pd.DataFrame(doneTodos, columns=["Archived Tasks"])
    
    # Add today's archived tasks to the dictionary
    sheet_dict[f'Archived_{today_str}'] = df_archive

    # Write all sheets back to the Excel file
    with pd.ExcelWriter(archiveExcelFile, mode='w', engine='openpyxl') as writer:
        for sheet_name, df in sheet_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Call the function to save archived tasks to Excel
save_archived_to_excel()

# Using an expander to keep the page compact
with st.expander(f"Done tasks, well done! ({completed_count})"):
    for i, item in enumerate(doneTodos):
        st.checkbox(item, value=True, disabled=True, key=f"done_{item}_{i}")
