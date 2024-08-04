import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Cloud Storage",
    page_icon="☁️",
)

st.title("AWS S3 Cloud Storage")
st.info('Due to Charges, the App is currently Down !')
st.info("""WORKING:
1. **Access Keys**: 
   The AWS access keys (Access Key ID and Secret Access Key) are set up to interact with AWS S3.

2. **File Upload Interface**: 
   Provides a file uploader for users to choose a file for upload, and text inputs to specify the bucket name and file name for S3.

3. **Upload Functionality**: 
   Includes a function `upload_to_aws` that uses `boto3` to handle file uploads to S3. This function handles potential errors such as file not found and credential issues.

4. **Error Handling**: 
   Implements error handling for cases where the file is not found or credentials are not available.
""")

video_url = "cloud Project.mp4"
st.video(video_url, format="video/mp4")


st.subheader("Here's the Code")

code = """
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = st.secrets["aws_access_key"]
SECRET_KEY = st.secrets["aws_secret_key"]

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        st.success(f"Upload Successful: {s3_file}")
    except FileNotFoundError:
        st.error("The file was not found")
    except NoCredentialsError:
        st.error("Credentials not available")

uploaded_file = st.file_uploader("Choose a file to upload")
bucket_name = st.text_input("Enter the bucket name:")
file_name = st.text_input("Enter the S3 file name:")

if st.button("Upload") and uploaded_file and bucket_name and file_name:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    upload_to_aws(uploaded_file.name, bucket_name, file_name)
"""

st.code(code, language='python')
# ACCESS_KEY = st.secrets["aws_access_key"]
# SECRET_KEY = st.secrets["aws_secret_key"]

# def upload_to_aws(local_file, bucket, s3_file):
#     s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
#     try:
#         s3.upload_file(local_file, bucket, s3_file)
#         st.success(f"Upload Successful: {s3_file}")
#     except FileNotFoundError:
#         st.error("The file was not found")
#     except NoCredentialsError:
#         st.error("Credentials not available")

# uploaded_file = st.file_uploader("Choose a file to upload")
# bucket_name = st.text_input("Enter the bucket name:")
# file_name = st.text_input("Enter the S3 file name:")

# if st.button("Upload") and uploaded_file and bucket_name and file_name:
#     with open(uploaded_file.name, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     upload_to_aws(uploaded_file.name, bucket_name, file_name)
