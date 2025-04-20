import streamlit as st
st.set_page_config("ISOM3400 Web App Dev 1 Lab Manual", page_icon="🖥️")

pages = {
    "🧪Lab Instructions": [
        st.Page("intro.py", title="Lab Introduction"),
        st.Page("task_instructions.py", title="Lab Task Guide"),
    ],
    "📚Relevant Documentation": [
        st.Page("docu/display_data.py", title="Displaying Data"),
        st.Page("docu/user_input.py", title="User Input"),
        st.Page("docu/forms.py", title="Forms")
    ]
}

pg = st.navigation(pages)
pg.run()


