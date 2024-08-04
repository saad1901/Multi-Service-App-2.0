import streamlit as st
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

tab1, tab2, tab3 = st.tabs(["Docx to PDF converter", "test", "test2"])

def docx_to_text(docx_file_path):
    doc = Document(docx_file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def text_to_pdf(text, pdf_file_path):
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    width, height = letter
    lines = text.split('\n')
    y = height - 40
    for line in lines:
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()

with tab1:
    st.title("Batch DOCX to PDF Converter")

    uploaded_files = st.file_uploader("Choose DOCX files", type="docx", accept_multiple_files=True)

    if uploaded_files:
        with st.spinner('Converting...'):
            # Save uploaded files to a temporary directory
            temp_dir = "temp_docs"
            os.makedirs(temp_dir, exist_ok=True)
            file_paths = []
            for uploaded_file in uploaded_files:
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                file_paths.append(file_path)

            pdf_files = []
            for file_path in file_paths:
                try:
                    text = docx_to_text(file_path)
                    pdf_file_path = os.path.splitext(file_path)[0] + '.pdf'
                    text_to_pdf(text, pdf_file_path)
                    pdf_files.append(pdf_file_path)
                except Exception as e:
                    st.error(f"Error converting {file_path}: {str(e)}")

            st.success("Conversion successful!")
            for pdf_file in pdf_files:
                with open(pdf_file, "rb") as f:
                    st.download_button(
                        label=f"Download {os.path.basename(pdf_file)}",
                        data=f,
                        file_name=os.path.basename(pdf_file),
                        mime="application/pdf"
                    )
