import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Add Images",
    page_icon="📷",
)

st.title("Add Images")

uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    image.save(f'images/{uploaded_image.name}')
    st.success(f"Image {uploaded_image.name} saved successfully.")
