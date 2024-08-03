import streamlit as st

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
)

msg = "Coming Soon"

def stream_data():
    for word in msg.split(" "):
        yield word + " "
        time.sleep(0.02)



st.write_stream(stream_data)