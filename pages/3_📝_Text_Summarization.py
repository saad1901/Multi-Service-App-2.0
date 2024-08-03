import streamlit as st

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
)
msg = "COMING SOON!!"

for word in msg.split(" "):
        yield word + " "
        time.sleep(0.2)
# st.header("Coming Soon")
st.snow()