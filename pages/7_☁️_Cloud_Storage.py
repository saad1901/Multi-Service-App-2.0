import streamlit as st
import os
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Cloud Storage",
    page_icon="☁️",
)

uploads_dir = "uploads"
os.makedirs(uploads_dir, exist_ok=True)
def get_available_files():
    files = []
    for filename in os.listdir(uploads_dir):
        files.append(filename)
    return files
def upload_file():
    uploaded_file = st.file_uploader("Choose a file to upload")
    if uploaded_file is not None:
        filepath = os.path.join(uploads_dir, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())
        st.success("File uploaded successfully!")
def download_file(filename):
    filepath = os.path.join(uploads_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            content = f.read()
        return content
    else:
        st.error(f"File '{filename}' not found")
st.subheader("Packages")
st.text("Upload Files")
st.info('under development :/ ("Uploaded files are temporary; they disappear once the app sleeps.")')
upload_file()
st.subheader("Download Files")
available_files = get_available_files()
if available_files:
    for filename in available_files:
        file_data = download_file(filename)
        if file_data is not None:
            st.download_button(label=filename, data=file_data, file_name=filename)
else:
    # st.info("No files uploaded yet!")
    pass