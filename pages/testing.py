import streamlit as st
import time

def fake_show():
    text = "Hello, this is an AI-generated text appearing word by word in Streamlit."

    time.sleep(5)

    placeholder = st.empty()
    # Split the text into words
    words = text.split()

    # Loop through each word and display it with a delay
    for word in words:
        with placeholder.container():
            st.code(" ".join(words[:words.index(word)+1]))  # Display the text up to the current word
        time.sleep(0.3)  # Delay in seconds between each word

    # Final output without delay
    placeholder.write(text)
