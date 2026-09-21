import streamlit as st

st.markdown("""
<style>


.stApp {
    background-color: #f5ede4;
}


.main-title {
    color: #b24e63;
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    font-family: Georgia, serif;
}


.subtitle {
    color: #b24e63;
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    margin-top: 5px;
}


.welcome-card {
background-color: #fffaf5;
padding: 1px 15px 1px 15px;
border-radius: 20px;
margin-top: 40px;
}


.welcome-card h2 {
    color: #b23e63;
    font-size: 35px;
    font-weight: 650;
    margin-bottom: 0px;
    line-height: 1.2;
}


.welcome-card p {
    color: #6f5559;
    font-size: 17px;
    font-weight: 420;
    margin-top: 0px;
    line-height: 1;
}


.stButton > button {
background-color: #b24e63;
color: white;
border-radius: 12px;
}


.task-message{
color: #b24e63;
}


.stButton {
    margin-left: 5px;
    margin-top: -2px;
}


.option-card {
    background-color: #fffaf5;
    padding: 2px 20px 2px 20px;
    margin-top: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}


.option-card:hover {
    box-shadow: 0 7px 18px rgba(178, 78, 99, 0.18);
}


.option-card h3 {
    color: #b24e63;
    font-weight: 500;
    font-size: 24px;
}


.option-card p {
    color: #6f5559;
    font-weight: 400;
    font-size: 15px;
}


</style>
""", unsafe_allow_html=True)





st.markdown("""
<div class="main-title">
    ━━━ Study Planner ━━━
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="subtitle">
    stay organised 𓂃✍︎
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="welcome-card">
    <h2>Welcome Back! </h2>
    <p>⤷ ready to get some studying done?</p>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("""
        <div class="option-card">
        <h3> + Add Task </h3>
        <p> create a new study task </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("&nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp;", key="add_task_button"):
            st.markdown("""
            <div class="task-message">
                You clicked 'Add Task'!
            </div>
            """, unsafe_allow_html=True)
    

with col2:
    with st.container():
        st.markdown("""
        <div class="option-card">
            <h3> ⌕ View Tasks</h3>
            <p>see all your current tasks</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("&nbsp;&nbsp;&nbsp; ⌕ &nbsp;&nbsp;&nbsp;", key="view_tasks_button"):
            st.markdown("""
            <div class="task-message">
                You clicked 'View Task'!
            </div>
            """, unsafe_allow_html=True)



col3, col4 = st.columns(2)

with col3:
    with st.container():
        st.markdown("""
        <div class="option-card">
        <h3> ✔︎ Mark Complete </h3>
        <p> mark a task as finished </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("&nbsp;&nbsp;&nbsp; ✔︎ &nbsp;&nbsp;&nbsp;", key="complete_task_button"):
            st.markdown("""
            <div class="task-message">
                You clicked 'Mark Complete'!
                </div>
            """, unsafe_allow_html=True)


    with col4:
        with st.container():
            st.markdown("""
            <div class="option-card">
                <h3>🗑 Delete Task</h3>
                <p>remove a task from your planner</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("&nbsp;&nbsp;&nbsp; 🗑 &nbsp;&nbsp;&nbsp;", key="delete_task_button"):
                st.markdown("""
                <div class="task-message">
                    You clicked 'Delete Task'!
                </div>
                """, unsafe_allow_html=True)
            

