import streamlit as st
from PIL import Image
import os

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Gallery",
    page_icon="🖼️",
)

st.title("Gallery")

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
