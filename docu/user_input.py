import streamlit as st

def int_float(num_str):
    try:
        num = int(num_str)
    except:
        try:
            num = float(num_str)
        except:
            if num_str:
                st.error("invalid input")
            return None
        finally:
            pass
    
    return num

st.header("Documentation - User Input")
st.markdown("""
            Streamlit allows users to interact with apps via [input widgets](https://docs.streamlit.io/develop/api-reference/widgets) such as buttons, sliders, and text inputs.
""")

st.subheader("Buttons")
st.markdown("""
            [`st.button()`](https://docs.streamlit.io/develop/api-reference/widgets/st.button) displays a button.\\
            It requires a 'label' string as an argument, which explains to the user what the button is for.\n
            In general, the default value stored in a button is `False`. When clicked, it returns `True`.\\
            Thus, it is possible to trigger actions by checking if the value stored is True or not:
""")
with st.container(border=True):
    with st.echo():
        button_state = st.button("Click me!")
        st.write(f"value stored in button_state: {button_state}")

        if button_state:
            st.write("The button is clicked!")
    
with st.expander("Button documentation", icon="📖"):
    with st.echo():
        st.help(st.button)

st.markdown("""
            Other buttons:
            - For downloads: [`st.download_button()`](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)
            - For forms: [`st.form_submit_button()`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button)
            - To display a link: [`st.link_button()`](https://docs.streamlit.io/develop/api-reference/widgets/st.link_button)
            - To link to another page: [`st.page_link()`](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)
            
""")

'---'
st.subheader("Numeric Input")
st.markdown("""
            Streamlit has two different methods for collecting numeric input:
            - [`st.number_input()`](https://docs.streamlit.io/develop/api-reference/widgets/st.number_input)
""")
with st.container(border=True):
    with st.echo():
        my_number = st.number_input("Please enter a number:")
        st.write(f"Value stored in my_number: {my_number} ({type(my_number)})")

with st.expander("number_input documentation", icon="📖"):
    with st.echo():
        st.help(st.number_input)

st.markdown("""
            - [`st.slider()`](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)
""")
with st.container(border=True):
    with st.echo():
        slider_number = st.slider("Please choose a number:")
        st.write(f"Value stored in slider_number: {slider_number} ({type(slider_number)})")

with st.expander("Slider documentation", icon="📖"):
    with st.echo():
        st.help(st.slider)

st.write("""You can further customize these input widgets by specifying restrictions such as max/min value, step, etc. \\
         Specifying integer values will force the widget to take and return integers. Note that the types for these values must be consistent (or `None` to use the default value).""")

with st.expander("Try and customize a slider widget!", icon="👇", expanded=True):

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        min_value = st.text_input("min_value")
        min_value = int_float(min_value)
        st.caption(f"{type(min_value)}")

    with col2:
        max_value = st.text_input("max_value")
        max_value = int_float(max_value)
        st.caption(f"{type(max_value)}")

    with col3:
        value = st.text_input("value (int/float/tuple)")

        if '(' and ',' and ')' in value: # Tuple
            vals = value.strip('()').split(',')
            value = tuple([int_float(val) for val in vals])
        else:
            value = int_float(value)

        st.caption(f"{type(value)}")

    with col4:
        step = st.text_input("step")
        step = int_float(step)
        st.caption(f"{type(step)}")
    
    try:
        with st.echo():
            my_number = st.slider("Number Input", min_value, max_value, value, step)
            st.write(f"Value stored in my_number: {my_number}")
            st.write(f"Type: {type(my_number)}")
    except BaseException as e:
        st.error(str(e))
