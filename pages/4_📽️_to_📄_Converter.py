import streamlit as st
import requests
import time

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Transcripter",
    page_icon="📄",
)

API_KEY_ID = st.secrets['vidtoaud1']
API_KEY_SECRET = st.secrets['vidtoaud2']
LANG = "en"
RESULT_TYPE = 4

headers = {"keyId": API_KEY_ID, "keySecret": API_KEY_SECRET}

def main():
    st.subheader("Transcripter (Video/Audio to Text)")

    uploaded_file = st.file_uploader("Choose a video or audio file", type=["wav", "mp3", "mp4", "m4a", "flac"])
    if st.button("Transcribe"):
        if uploaded_file:
            with st.spinner("Submitting the file for transcription..."):
                task_id = create(uploaded_file)

            if task_id:
                with st.spinner("Waiting for the transcription to complete..."):
                    transcription_result = query(task_id)

                if transcription_result:
                    st.code(transcription_result)
                else:
                    st.error("Failed to retrieve transcription result.")
        else:
            st.warning("Please upload a file.")

def create(uploaded_file):
    create_url = "https://api.speechflow.io/asr/file/v1/create"
    files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
    data = {
        "lang": LANG
    }

    response = requests.post(create_url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        create_result = response.json()
        if create_result["code"] == 10000:
            return create_result["taskId"]
        else:
            st.error(f"Create error: {create_result['msg']}")
            return None
    else:
        st.error(f"Create request failed with status code: {response.status_code}")
        st.error(f"Response text: {response.text}")
        return None

def query(task_id):
    query_url = f"https://api.speechflow.io/asr/file/v1/query?taskId={task_id}&resultType={RESULT_TYPE}"

    while True:
        response = requests.get(query_url, headers=headers)
        if response.status_code == 200:
            try:
                query_result = response.json()

                if query_result["code"] == 11000:
                    return extract_text(query_result)
                elif query_result["code"] == 11001:
                    time.sleep(3)
                else:
                    st.error(f"Transcription error: {query_result['msg']}")
                    return None
            except Exception as e:
                st.error(f"Error parsing JSON: {e}")
                st.write(f"Response text: {response.text}")
                return None
        else:
            st.error(f"Query request failed with status code: {response.status_code}")
            st.write(f"Response text: {response.text}")
            return None

def extract_text(data):
    try:
        if isinstance(data, dict) and 'result' in data:
            return data['result']
        else:
            st.error("Unexpected data format")
            return ""
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return ""

if __name__ == "__main__":
    main()
