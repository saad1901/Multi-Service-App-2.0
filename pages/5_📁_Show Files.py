import streamlit as st
import os
import time

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Files",
    page_icon="📁",
)
tab1,tab2 = st.tabs(["Files","Add a File"])

with tab1:
    st.header('🚀FILES')
    # passw = st.text_input('Enter Password', type="password")
    def read_file_content(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    valid_extensions = ('txt','py','cpp','java','json','js','html','css','bat','c','kt')
    files = [''] + [file for file in os.listdir() if file.endswith(valid_extensions)]
    selected_file = st.selectbox('Select file', files)
    if selected_file:
        if selected_file != '':
            st.header(f"{selected_file}")
            content = read_file_content(selected_file)
            st.code(content, language='python')
        else:
            st.info("Select a file from the dropdown to view its content.")
    else:
        st.text("Please select a file from the dropdown.")
    # elif passw != st.secrets["psd"] and passw != '' :
    #     st.error('wrong person !!')

with tab2:
    st.text("⚠️Note: The Files won't be stored in Github")
    st.text("They'll be only available in RAM until the app is running and cache isn't cleared")
    passwd = st.text_input('Enter Password ', type="password")

    # if passwd == st.secrets['psd2']:

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
    with st.form("form",clear_on_submit=True):
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

    # elif passwd != st.secrets["psd2"] and passwd != '':
    #     st.error('Wrong password!')