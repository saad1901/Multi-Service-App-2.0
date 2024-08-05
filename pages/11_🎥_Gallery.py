import streamlit as st
from PIL import Image
import time
import os

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Add Images",
    page_icon="📷",
)
a,b = st.tab(["Add Images","Gallery"])

with a:
    st.subheader("Add Images")
    def save_captured_photo(uploaded_file):
        photos_dir = "photos"
        if not os.path.exists(photos_dir):
            os.makedirs(photos_dir)
        filename = f"image_{int(time.time())}.jpg"
        filepath = os.path.join(photos_dir, filename)
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

with b:
    st.subheader("Gallery")
    def load_images(directory):
        images = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.jpg', '.png', '.jpeg'))]
        return images

    image_files = load_images('photos')

    if image_files:
        selected_image = st.selectbox("Select an image", image_files)
        if selected_image:
            image = Image.open(selected_image)
            st.image(image, caption=os.path.basename(selected_image), use_column_width=True)
    else:
        st.info("No images found. Please add images in the 'Add Images' section.")