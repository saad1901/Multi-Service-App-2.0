import streamlit as st
from docx2pdf import convert
import os

def convert_docx_to_pdf(docx_path, pdf_path):
    # Convert DOCX to PDF using docx2pdf
    convert(docx_path, pdf_path)

st.title("DOCX tooo PDF Converter")

uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")

if uploaded_file is not None:
    with open("uploaded.docx", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Convert the DOCX file to PDF
    convert_docx_to_pdf("uploaded.docx", "output.pdf")
    
    # Provide the PDF file for download
    with open("output.pdf", "rb") as f:
        st.download_button("Download PDF", f, file_name="output.pdf")

st.write("Upload a DOCX file and click the button to convert it to a PDF.")
