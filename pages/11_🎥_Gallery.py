import streamlit as st
from PIL import Image
import time
import os

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Image Gallery",
    page_icon="📷",
)
a,b = st.tabs(["Add Images","Gallery"])

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
        # Number of columns in the grid
        num_columns = 3
        columns = st.columns(num_columns)

        for i, image_file in enumerate(image_files):
            # Open the image
            image = Image.open(image_file)

            # Display the image in the appropriate column
            col = columns[i % num_columns]
            with col:
                st.image(image, caption=os.path.basename(image_file), width=300)  # Adjust the width as needed
    else:
        st.info("No images found. Please add images in the 'Add Images' section.")
