import streamlit as st
import os
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Files",
    page_icon="📁",
)

st.header('🚀Github FILES')
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