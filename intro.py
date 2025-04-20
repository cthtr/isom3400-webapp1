import streamlit as st


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ol, ul{
    padding-left:20px;
}
</style>
''', unsafe_allow_html=True)

st.title("ISOM3400 Lab 11: Web App Development 1")
'---'
st.header("Introduction")
st.subheader("Objectives")
st.write("""
- To become familiar with basic Streamlit functionalities
- To create a simple interactive web app that responds to user input
""")
st.subheader("Before you start:")
st.markdown("""
- Software: VS Code and Anaconda are installed properly (Lab 1)
- Python interpreter & environment: Streamlit is installed (likely comes with Anaconda's 'base')
- Importing Streamlit: Streamlit is imported as st (`from streamlit import st`)
""")

st.subheader("To complete this lab:")
st.markdown("""
1. Download the lab file from Canvas and unzip it.
2. Complete the code according to the task instructions.
    - If you run into trouble / do not know how to use an element, you may refer to the relevant documentation.
3. If you belong to either LA3 or LA4 (Monday sections):
    - Complete Lab Canvas quiz by Tuesday 11:59pm.
""")
'---'
st.subheader("Beyond this lab:")
st.markdown("""
If you have completed the main portion of this lab, you can further experiment with the app. Here are some ideas:
- Change the layout of the app
- Use different input methods
- Display different content depending on the score
- ...
""")

