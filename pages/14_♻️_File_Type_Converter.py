import streamlit as st

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')

t1,t2 = st.tabs(["Docx to PDF","JPG to PDF","PPT to PDF"])

st.set_page_config(
    page_title="File Converter",
    page_icon="♻️",
)
with t1:
    st.header('Coming very Soon')