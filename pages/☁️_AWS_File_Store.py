import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError

st.set_page_config(
    page_title="Cloud Storage",
    page_icon="☁️",
)

st.title("AWS S3 Cloud Storage")

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
