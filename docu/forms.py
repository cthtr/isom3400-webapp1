import streamlit as st

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ol, ul{
    padding-left:20px;
}
</style>
''', unsafe_allow_html=True)

st.header("Documentation - Forms")
st.markdown("""
            When a user modifies a widget's value, the Python script will be rerun. If you have a small app, this will not cause much issues, but for a large and complex app, this rerun behavior may make it much less efficient. Furthermore, if an app depends on a set of input rather than individual pieces, it may be more convenient to bundle them together.
         
            In this situation, you can use a Form (`st.form()`) to group elements and widgets together. Any input passed to the form will only be sent to the server once the submit button is pressed. Note that each form must have a form submit button (`st.form_submit_button()`).
            
""")

st.write("""
         There are two methods to use a form object:
            1. using the `with` notation
            2. calling methods directly on the form object""")

st.subheader("1.`with` notation")
st.markdown("""
    You can create a form using Python's `with` notation as follows. All code indented under the `with` statement will be included in the form, and code outside of the code block will be rendered outside of the form.
""")
with st.container(border=True):
    with st.echo():
        with st.form("Form 1"):
            st.write("Using with notation")
            form1_number = st.number_input("Enter a number from 1 to 100.", 1, 100)
            st.form_submit_button("Submit")
        st.write(f"I am outside the form. The number you chose is: {form1_number}")

st.subheader("2. Calling directly on form object")
st.markdown("""
            When using this method, first define a variable as a form object:
""")
st.code("my_form = st.form(\"Form 2\")")
st.markdown("""
            Then, other elements can be added into the form by calling methods on the form object instead of using `st.`. The same level of indentation can be used.
""")
st.code("""
        my_form.write(\"I am writing to the form!\")
        my_form.input("Type something here!")
        my_form.form_submit_button("Submit form")
        
""")

with st.container(border=True):
    my_form = st.form("Form 2")
    my_form.write("I am writing in the form!")
    my_form.text_input("Type something here!")
    my_form.form_submit_button("Submit form")


with st.expander("Form documentation", icon="📖"):
    with st.echo():
        st.help(st.form)