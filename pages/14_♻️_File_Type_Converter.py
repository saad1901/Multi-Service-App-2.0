import streamlit as st
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')

st.set_page_config(
    page_title="File Converter",
    page_icon="♻️",
)
t1,t2,t3 = st.tabs(["Docx to PDF","JPG to PDF","PPT to PDF"])

with t1:
    st.header('Coming very Soon')

