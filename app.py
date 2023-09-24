import streamlit as st
import pandas as pd
from streamlit_timeline import st_timeline

st.set_page_config(layout="wide")

class WebApp:
    def __init__(self):
        self.col1, self.col2 = st.columns([.4, .6])
        self.current_df = None
        self.completed_df = None
        self.task_columns = ["Task Name", "Task Priority", "Active", "Completed"]


    def new_task_column(self):
        with self.col1:
            st.header("All Tasks")
            priority_options = ["Very High", "High", "Medium", "Low", "Very Low"]

            task_name = st.text_input("Enter Task Name")
            priority = st.selectbox("Select A Task Priority", priority_options)

            if st.button("Add New Task"):
                if task_name:
                    st.session_state.tasks.loc[len(st.session_state.tasks)] = [task_name, priority, False, False]

            edited_df = st.data_editor(st.session_state.tasks, num_rows = "dynamic",
                                    column_config={"Active": st.column_config.CheckboxColumn("Active", default=False),
                                                "Task Priority" : st.column_config.SelectboxColumn("Priority", options = priority_options)},
                                        hide_index = True)
            

            self.current_df = edited_df[edited_df['Active']]
            self.completed_df = edited_df[edited_df['Completed']]

    def active_task_column(self):
        with self.col2:
            current_col, completed_col = st.columns(2)

            with current_col:
                st.header("Active Tasks")
                st.dataframe(self.current_df, hide_index = True)

            with completed_col:
                st.header("Completed Tasks")
                st.dataframe(self.completed_df, hide_index = True)
    

    def generate_timeline_contents(self, task_dict):
        items = []
        id = 0
        
        for i in task_dict:
            items.append({"id":id, "content": i, "start": task_dict[i][0], "end": task_dict[i][0]})

        return items
    
    def plot_timeline(self, task_dict):
        timeline = st_timeline(self.generate_timeline_contents(task_dict), groups=[], options={}, height="300px")

    def run(self):
        if 'tasks' not in st.session_state:
            st.session_state.tasks = pd.DataFrame(columns=self.task_columns)

        self.new_task_column()
        self.active_task_column()

webapp = WebApp()
webapp.run()
