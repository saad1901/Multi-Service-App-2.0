import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Translator",
    page_icon="🌐",
)

st.title("Language Translator")
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Hindi": "hi",
    "Urdu": "ur",
    "Marathi": "mr"
}
languages_dest = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Hindi": "hi",
    "Urdu": "ur",
    "Marathi": "mr"
}

text = st.text_area("Enter text to translate:")
src_lang = st.selectbox("Source Language", list(languages.keys()))
dest_lang = st.selectbox("Destination Language", list(languages_dest.keys()))
translate_button = st.button("Translate")

if translate_button and text:
    try:
        translator = GoogleTranslator(source=languages[src_lang], target=languages[dest_lang])
        translation = translator.translate(text)
        st.code(f"Translated text: {translation}")
    except Exception as e:
        st.error(f"Translation failed: {e}")

