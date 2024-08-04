import streamlit as st
import subprocess
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="CLI",
    page_icon="💻",
)

st.title("Command Line Interface")

command = st.text_input("Enter command to execute:")
execute_button = st.button("Execute")

if execute_button and command:
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        st.subheader("Output")
        st.text(result.stdout)
        if result.stderr:
            st.subheader("Error")
            st.text(result.stderr)
    except Exception as e:
        st.error(f"An error occurred: {e}")
