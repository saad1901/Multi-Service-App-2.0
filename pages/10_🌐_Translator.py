import streamlit as st
from googletrans import Translator

st.set_page_config(
    page_title="Translator",
    page_icon="🌐",
)

st.title("Language Translator")
translator = Translator()

text = st.text_area("Enter text to translate:")
src_lang = st.selectbox("Source Language", ["auto", "en", "es", "fr", "de", "zh-cn"])
dest_lang = st.selectbox("Destination Language", ["en", "es", "fr", "de", "zh-cn"])
translate_button = st.button("Translate")

if translate_button and text:
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    st.code(f"Translated text: {translation.text}")
