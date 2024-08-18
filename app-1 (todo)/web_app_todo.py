import streamlit as st
from functions import *


filePath = "todos.txt"
todos = getTodos(filePath)
time = currentTime()


def addTodo():
    todo = st.session_state["newTodo"]
    todos.append(todo.strip().title() + "\n")
    saveFile(filePath, todos)
    st.session_state["newTodo"]=""


st.write("""
         # My To-Do App
         ###### impove your productivity!
         """)

st.text_input(label="Add Task:", placeholder="Add Task:",
                      label_visibility="collapsed", on_change=addTodo,
                      key="newTodo"
                      )

        
st.write("Task need to be done!")

for item in todos:
    st.checkbox(item)
    

st.session_state