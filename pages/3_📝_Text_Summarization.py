import streamlit as st

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
)
msg = "COMING SOON!!"

for word in msg.split(" "):
    message_container.markdown(f"## {word}")
    time.sleep(0.5)  # Adjust the delay as needed
    
# st.header("Coming Soon")
st.snow()