import streamlit as st
import subprocess
import platform

st.set_page_config(
    page_title="Python Compiler",
    page_icon="🐍",
)

py_version = platform.python_version()
st.header(f"🐍Mini Python Compiler {py_version}")

code = st.text_area("Enter your Python code: (currently it doesn't support inputs)")
input_code = st.text_input('Input for code')
run_button = st.button("RUN")

if code and run_button:
    with open("temp_code.py", "w") as f:
        f.write(code)
    output = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True).stdout
    st.subheader(output)
