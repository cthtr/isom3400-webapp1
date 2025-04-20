import streamlit as st
st.title("Lab Task Instructions")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ol, ul{
    padding-left:20px;
}
</style>
''', unsafe_allow_html=True)

st.subheader("Task Premise")
st.write("You are given skeleton code for a web app that takes in your grades for different assessment components for ISOM3400. The app then calculates your final score for the course and tells you whether you will pass this course.")

st.caption("*Note: The actual grading of this course may differ from what is suggested in this lab. Please refer to information provided by instructors for the most accurate information.*")

'---'

st.header("Task Guide")
st.subheader("1. Setting up the page")
st.markdown ("""
            1. Set a page title for your web app using `st.set_page_config()`.
            2. Create a form to group the user input.
                - The form has been created for you using the 'with' notation. You can change it to the other method if you prefer.
                - A submit button has also been created for you - customize it!
""")

st.subheader("2. Collecting User Input")
st.markdown("""
            Allow users to input their scores in the form and validate their input.\\
            You can obtain numerical input by using either `st.number_input()` or `st.slider()`[:mag:](user_input#numeric-input).

            You should ask the user for four different values:
            1. Number of labs attended (max: 12)
            2. Assignment 1 score (out of 100)
            3. Assignment 2 score (out of 100)
            4. Final exam score (out of 100)

            Once the user has filled in all relevant values, they should click on a form submit button (`st.form_submit_button()`) to submit the entered values.
""")
st.caption("*Note: Pay attention to the data type of your input!*")

st.subheader("3. Calculating Scores")
st.markdown("""
            When the form submit button is clicked, all values inside the form will then be sent to the Streamlit server in a batch. It will then be possible to operate on the user-entered values.\n
            Detect when the button is clicked, then proceed to complete the following calculations.

""")
st.markdown("You are given a dictionary `grading`:")
st.code("""
        grading = {
        'Labs': 5,
        'Assignment 1': 15,
        'Assignment 2': 15,
        'Final Exam': 65
        }
""", "python")
st.markdown("""
            The keys are names of the four assessment components, and the values are the corresponding weightings of the components (/100).\n
            For lab attendance:
            - Each attended lab is worth 10% of the lab grade.
            - If a student has attended at least 10 labs, they will have full credit for the lab component.
            - There is no bonus for students who have attended all labs. (Sorry!)

            Sum up the weighted scores to calculate the total course score.
""")

st.subheader("4. Displaying Results")
st.markdown("""
            Depending on the calculated total score, two different messages should be shown:
            - If total score is lower than 50: the student may fail the course
            - Else: the student is likely to pass the course.

            Inform the student whether they are likely to pass the course or not!
""")


