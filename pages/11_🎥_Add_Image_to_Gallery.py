import streamlit as st
from PIL import Image
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Add Images",
    page_icon="📷",
)

st.title("Add Images")

def save_captured_photo(uploaded_file):
        filename = f"FromWeb_{int(time.time())}.jpg"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "wb") as buffer:
            buffer.write(uploaded_file.getvalue())
        st.success(f"Image saved successfully as '{filepath}'.")
uploaded_files = st.file_uploader("Upload multiple photos", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        save_captured_photo(uploaded_file)
on = st.toggle('Open Camera')
if on:
    captured_photo = st.camera_input(":red[OR Take a picture]")
    upload = st.button('upload')
    if captured_photo is not None and upload:
        save_captured_photo(captured_photo)
