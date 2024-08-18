import streamlit as st
import pandas as pd
import os
import datetime

# File paths for the to-do lists, completed tasks, and archives

todosDoneExcelFile = "files/todos_done_summary.xlsx"
archiveExcelFile = "files/archived_tasks.xlsx"

# Determine today’s date
today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

# Function to initialize or load data from Excel
def initialize_excel_files():
    if not os.path.exists(todosDoneExcelFile):
        with pd.ExcelWriter(todosDoneExcelFile, engine='openpyxl') as writer:
            pd.DataFrame(columns=["To-Do Tasks"]).to_excel(writer, sheet_name='To-Do Tasks', index=False)
            pd.DataFrame(columns=["Completed Tasks"]).to_excel(writer, sheet_name='Completed Tasks', index=False)

    if not os.path.exists(archiveExcelFile):
        with pd.ExcelWriter(archiveExcelFile, engine='openpyxl') as writer:
            pd.DataFrame(columns=["Archived Tasks"]).to_excel(writer, sheet_name=today_str, index=False)

initialize_excel_files()

# Load existing tasks from Excel
def load_excel_data():
    with pd.ExcelFile(todosDoneExcelFile) as xls:
        todos_df = pd.read_excel(xls, sheet_name='To-Do Tasks')
        doneTodos_df = pd.read_excel(xls, sheet_name='Completed Tasks')
    return todos_df['To-Do Tasks'].tolist(), doneTodos_df['Completed Tasks'].tolist()

todos, doneTodos = load_excel_data()

# Function to save to-do lists and completed tasks to Excel
def save_todos_done_to_excel():
    df_todos = pd.DataFrame(todos, columns=["To-Do Tasks"])
    df_doneTodos = pd.DataFrame(doneTodos, columns=["Completed Tasks"])
    
    with pd.ExcelWriter(todosDoneExcelFile, mode='w', engine='openpyxl') as writer:
        df_todos.to_excel(writer, sheet_name='To-Do Tasks', index=False)
        df_doneTodos.to_excel(writer, sheet_name='Completed Tasks', index=False)

# Function to save archived tasks to Excel
def save_archived_to_excel():
    if os.path.exists(archiveExcelFile):
        with pd.ExcelFile(archiveExcelFile) as xls:
            sheet_dict = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
    else:
        sheet_dict = {}

    df_archive = pd.DataFrame(doneTodos, columns=["Archived Tasks"])
    sheet_dict[today_str] = df_archive

    with pd.ExcelWriter(archiveExcelFile, mode='w', engine='openpyxl') as writer:
        for sheet_name, df in sheet_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Function to handle checkbox changes
def handle_checkbox_change(item, index):
    if st.session_state.get(f"{item}_{index}"):
        doneTodos.append(item)
        todos.remove(item)
        save_todos_done_to_excel()
        save_archived_to_excel()

# Function to add a new task
def addTodo():
    todo = st.session_state["newTodo"]
    if todo.strip():
        todos.append(todo.strip().title())
        save_todos_done_to_excel()
        st.session_state["newTodo"] = ""

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
    st.checkbox(item, key=f"{item}_{i}", on_change=handle_checkbox_change, args=(item, i))

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

# Show archived tasks using a slider
st.markdown("---")
st.write("### View Archived Tasks")

def load_archive_dates():
    if os.path.exists(archiveExcelFile):
        with pd.ExcelFile(archiveExcelFile) as xls:
            return [datetime.datetime.strptime(sheet_name, '%Y-%m-%d').date() for sheet_name in xls.sheet_names]
    return []

archive_dates = load_archive_dates()

if len(archive_dates) > 1:
    min_date = min(archive_dates)
    max_date = max(archive_dates)
    
    selected_date = st.slider(
        "Select Date for Archived Tasks:",
        min_value=min_date,
        max_value=max_date,
        value=max_date,
        format="YYYY-MM-DD"
    )

    selected_date_str = selected_date.strftime('%Y-%m-%d')
    with pd.ExcelFile(archiveExcelFile) as xls:
        if selected_date_str in xls.sheet_names:
            df_archive = pd.read_excel(xls, sheet_name=selected_date_str)
            st.write(f"Archived Tasks for {selected_date_str}:")
            for task in df_archive['Archived Tasks']:
                st.write(f"- {task}")
        else:
            st.write(f"No archived tasks found for {selected_date_str}.")
else:
    st.write("Not enough data to show the slider. Only one date available.")
