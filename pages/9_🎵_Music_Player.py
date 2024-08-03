import streamlit as st
import os

st.set_page_config(
    page_title="Music Player",
    page_icon="🎵",
)

def get_audio_files(directory):
    audio_files = [file for file in os.listdir(directory) if file.endswith(('.mp3', '.wav'))]
    return audio_files

st.title("🎵Music Player")
uploaded_audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

audio_files = get_audio_files('songs')
selected_audio_file = st.selectbox("Select an audio file", [""] + audio_files)

if uploaded_audio_file is not None:
    audio_bytes = uploaded_audio_file.read()
    st.audio(audio_bytes, format='audio/' + uploaded_audio_file.type.split('/')[-1])
elif selected_audio_file:
    audio_path = os.path.join('songs', selected_audio_file)
    audio_bytes = open(audio_path, 'rb').read()
    st.audio(audio_bytes, format='audio/' + selected_audio_file.split('.')[-1])
else:
    st.info("Please upload an audio file or select one from the list.")
