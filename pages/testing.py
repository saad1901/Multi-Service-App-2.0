import streamlit as st
from docx import Document
import pdfkit
import os

def convert_docx_to_pdf(docx_path, pdf_path):
    # Read the DOCX file
    doc = Document(docx_path)
    html_content = ''
    
    # Convert DOCX content to HTML
    for para in doc.paragraphs:
        html_content += f'<p>{para.text}</p>'
    
    # Save HTML content to a temporary file
    temp_html_path = 'temp.html'
    with open(temp_html_path, 'w') as f:
        f.write(html_content)
    
    # Convert HTML to PDF using pdfkit
    pdfkit.from_file(temp_html_path, pdf_path)
    
    # Remove the temporary HTML file
    os.remove(temp_html_path)

st.title("DOCX to PDF Converter")

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
