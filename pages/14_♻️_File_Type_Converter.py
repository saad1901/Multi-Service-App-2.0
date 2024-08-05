import streamlit as st
import convertapi
import os
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')

st.set_page_config(
    page_title="File Converter",
    page_icon="♻️",
)

t1,t2,t3 = st.tabs(["PDF to editable Docx","JPG to PDF","PPT to PDF"])

with t1:
    convertapi.api_secret = st.secrets["api_file"]
    def convert_pdf_to_docx(pdf_path, docx_path):
        try:
            result = convertapi.convert('docx', {'File': pdf_path}, from_format='pdf')
            result.save_files(docx_path)
            st.toast("✅Conversion successful!")
        except Exception as e:
            st.error(f"⚠️Conversion failed: {e}")
    st.title("PDF to DOCX Converter")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_path = "uploaded.pdf"
        original_filename = uploaded_file.name
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        prefix = "cnvtd_"
        docx_filename = f"{prefix}{os.path.splitext(original_filename)[0]}.docx"
        convert_pdf_to_docx(pdf_path, docx_filename)
        if os.path.exists(docx_filename):
            with open(docx_filename, "rb") as f:
                st.download_button("Download DOCX", f, file_name=docx_filename)
        else:
            st.error("DOCX file not generated.")

    st.write("Upload a PDF file and click the button to convert it to a DOCX.")

