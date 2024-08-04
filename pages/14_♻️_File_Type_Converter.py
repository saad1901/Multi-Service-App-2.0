import streamlit as st
from docx import Document
from fpdf import FPDF
import os

tab1, tab2, tab3 = st.tabs(["Docx to PDF converter", "test", "test2"])

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Document Title', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def docx_to_text(docx_file_path):
    doc = Document(docx_file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def text_to_pdf(text, pdf_file_path):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title("Document Content")
    pdf.chapter_body(text)
    pdf.output(pdf_file_path)

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
