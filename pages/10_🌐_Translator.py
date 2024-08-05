import streamlit as st
from deep_translator import GoogleTranslator
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
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
a,b = st.columns(2)
src_lang = a.selectbox("Source Language", list(languages.keys()))
dest_lang = b.selectbox("Destination Language", list(languages_dest.keys()))
translate_button = st.button("Translate")

if translate_button and text:
    try:
        translator = Translator()  # GoogleTranslator from `googletrans` or any similar library
        translation = translator.translate(text, src=src_lang, dest=dest_lang).text
        st.text_area("Translated text:", value=translation, height=200)  # Adjust the height as needed
    except Exception as e:
        st.error(f"Translation failed: {e}")


