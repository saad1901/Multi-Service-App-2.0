import streamlit as st
import time

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Hello From Saad",
    page_icon="🙋🏻‍♂️",
)

st.write("# Welcome to Streamlit! 👋")


# st.toast('Open SideBar for Other Application')
# use st.tab for personal info
if st.button('hello'):
    st.toast('this is a toast msg')
# st.snow()

# st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)


# FOR LINKEDIN
# st.page_link("http://www.google.com", label="Google", icon="")

