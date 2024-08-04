import streamlit as st
import subprocess
import os

tab1, tab2, tab3 = st.tabs(["Docx to PDF converter", "test", "test2"])

with tab1:
    def convert_docx_to_pdf(docx_file_paths):
        pdf_files = []
        for docx_file_path in docx_file_paths:
            try:
                pdf_file_path = os.path.splitext(docx_file_path)[0] + '.pdf'
                subprocess.run(['pandoc', docx_file_path, '-o', pdf_file_path], check=True)
                pdf_files.append(pdf_file_path)
            except subprocess.CalledProcessError as e:
                st.error(f"Error converting {docx_file_path}: {str(e)}")
        return pdf_files

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

            pdf_files = convert_docx_to_pdf(file_paths)

            st.success("Conversion successful!")
            for pdf_file in pdf_files:
                with open(pdf_file, "rb") as f:
                    st.download_button(
                        label=f"Download {os.path.basename(pdf_file)}",
                        data=f,
                        file_name=os.path.basename(pdf_file),
                        mime="application/pdf"
                    )
