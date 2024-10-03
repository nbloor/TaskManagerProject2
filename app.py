import streamlit as st
from datetime import datetime, date

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Helper function to add a new task
def add_task(description, due_date):
    task = {
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    st.session_state.tasks.append(task)

# Helper function to delete a task
def delete_task(index):
    del st.session_state.tasks[index]

# Helper function to mark task as complete/incomplete
def toggle_task_status(index):
    st.session_state.tasks[index]['completed'] = not st.session_state.tasks[index]['completed']

# Streamlit app title
st.title("Task Manager")

# Task input section
st.subheader("Add New Task")
description = st.text_input("Task Description")
due_date = st.date_input("Due Date", min_value=date.today())

if st.button("Add Task"):
    if description.strip() == "":
        st.error("Task description cannot be empty.")
    else:
        add_task(description, due_date)
        st.success("Task added successfully!")

# Task list section
st.subheader("Tasks List")

if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        task_text = f"**{task['description']}** (Due: {task['due_date']})"
        task_status = "Completed" if task['completed'] else "Incomplete"

        col1, col2, col3 = st.columns([6, 2, 2])
        
        # Display task description and status
        with col1:
            st.write(f"{task_text} - {task_status}")

        # Mark task as complete/incomplete
        with col2:
            if st.button(f"Toggle Status", key=f"toggle_{index}"):
                toggle_task_status(index)
        
        # Delete task
        with col3:
            if st.button("Delete", key=f"delete_{index}"):
                delete_task(index)
                st.experimental_rerun()
else:
    st.write("No tasks available.")

# Display the task count
st.write(f"Total tasks: {len(st.session_state.tasks)}")
