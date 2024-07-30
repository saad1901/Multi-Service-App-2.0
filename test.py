import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

summarizer = pipeline("summarization")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text):
    max_chunk = 1000
    text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
    for chunk in text_chunks:
        summary_text = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        summary += summary_text + "\n"
    return summary

st.title("PDF Content Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(text)

    if st.button("Summarize"):
        with st.spinner("Summarizing content..."):
            summary = summarize_text(text)
        st.subheader("Summary:")
        st.write(summary)
