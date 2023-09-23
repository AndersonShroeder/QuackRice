import streamlit as st
import pandas as pd


col1, col2 = st.columns([.5, .5])

if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=["Task Name", "Task Priority", "Active", "Completed"])

# Column containing Tasks
with col1:
    st.header("Tasks")
    priority_options = ["Very High", "High", "Medium", "Low", "Very Low"]

    task_name = st.text_input("Enter Task Name")
    priority = st.selectbox("Select A Task Priority", priority_options)

    edited_df = st.data_editor(st.session_state.tasks, 
                               num_rows = "dynamic",
                               column_config={"Active": st.column_config.CheckboxColumn("Active", default=False),
                                              "Task Priority" : st.column_config.SelectboxColumn("Priority", options = priority_options)
                                              },
                                hide_index = True)
    
    if st.button("Add New Task"):
        if task_name:
            st.session_state.tasks.loc[len(st.session_state.tasks)] = [task_name, priority, False, False]

    st.session_state.new_df = edited_df[edited_df['Active']]
    st.write(st.session_state.new_df)


# Column contained completed/current tasks and visual representation of schedule
with col2:
    current_col, completed_col = st.columns(2)

    with current_col:
        st.header("Current")

    with completed_col:
        st.header("Completed")

    st.bar_chart()