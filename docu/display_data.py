import streamlit as st

st.header("Documentation - Displaying Data")
st.markdown("""
            Streamlit provides a variety of methods to display data on an app.\\
            In general, Streamlit displays the web app from top to bottom according to the code.\n
            [`st.write()`](https://docs.streamlit.io/develop/api-reference/write-magic/st.write) is the Swiss Army Knife of Streamlit commands. 
            It takes in any type of argument, and displays it on the app accordingly. Multiple elements can also be passed in.\n
            Other specific elements can be used if you would like to further customize how the data is displayed.""")

st.subheader("Text Elements")
st.markdown("""
            Streamlit provides a variety of [text elements](https://docs.streamlit.io/develop/api-reference/text).\\
            To display text on your app, you can pass in a string into a text element.
            - Plain text: `st.text()`
            - Formatted text: [`st.markdown()`](https://docs.streamlit.io/develop/api-reference/text/st.markdown)
                - Styled using GitHub-flavored markdown
                - Supports emojis and symbols 
            - Page titles: [`st.title()`](https://docs.streamlit.io/develop/api-reference/text/st.title)
            - Headers: [`st.header()`](https://docs.streamlit.io/develop/api-reference/text/st.header)
            - Subheaders: [`st.subheader()`](https://docs.streamlit.io/develop/api-reference/text/st.subheader)
            - ...
            """)
with st.expander("Text element examples", expanded=True):
    with st.echo():
        st.text("Plain text")
        st.markdown("I can format text and put in emojis :stuck_out_tongue:")
        st.title("This is a title!")
        st.header("This is a header~")
        st.subheader("This is a subheader.")

st.subheader("Data Elements")
st.write("🚧 We will take a look at data elements next lab :P")