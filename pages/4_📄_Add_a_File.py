import streamlit as st
import os
import time

st.set_page_config(
    page_title="Add a File",
    page_icon="📄",
)

st.text("⚠️Note: The Files won't be stored in Github")
st.text("They'll be only available in RAM until the app is running and cache isn't cleared")
passwd = st.text_input('Enter Password ', type="password")

if passwd == st.secrets['psd2']:

    def write_file(text, filename, extension):
        full_filename = filename + "." + extension
        if os.path.exists(full_filename):
            warn = st.warning(f"Warning: File '{full_filename}' already exists.(changes not made)")
            time.sleep(3)
            warn.empty()
            return
        with open(full_filename, "w") as file:
            file.write(text)
        succ = st.success(f"File '{full_filename}' saved successfully.")
        time.sleep(3)
        succ.empty()

    with st.form("form"):
        x, y = st.columns(2)
        fname = x.text_input('Enter Filename')
        ext = y.selectbox('Select Extension', ('txt', 'py', 'cpp', 'java', 'json', 'js', 'html', 'css', 'bat', 'c', 'kt'))
        text2 = st.text_area('Enter File Contents')
        button_save = st.form_submit_button('Save')

    if button_save and fname != '' and text2 != '':
        write_file(text2, fname, ext)
    elif button_save:
        er = st.error('Above fields are mandatory')
        time.sleep(3)
        er.empty()

elif passwd != st.secrets["psd2"] and passwd != '':
    st.error('Wrong password!')
