import streamlit as st
import convertapi
import os

st.set_page_config(
    page_title="File Converter",
    page_icon="♻️",
)

convertapi.api_secret = st.secrets["api_file"]

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        result = convertapi.convert('docx', {'File': pdf_path}, from_format='pdf')
        result.save_files(docx_path)
        st.toast("✅ Conversion successful!")
    except Exception as e:
        st.error(f"⚠️ Conversion failed: {e}")

def convert_jpg_to_pdf(jpg_path, pdf_path):
    try:
        result = convertapi.convert('pdf', {'File': jpg_path}, from_format='jpg')
        result.save_files(pdf_path)
        st.toast("✅ Conversion successful!")
    except Exception as e:
        st.error(f"⚠️ Conversion failed: {e}")

def convert_ppt_to_pdf(ppt_path, pdf_path):
    try:
        result = convertapi.convert('pdf', {'File': ppt_path}, from_format='pptx')
        result.save_files(pdf_path)
        st.toast("✅ Conversion successful!")
    except Exception as e:
        st.error(f"⚠️ Conversion failed: {e}")

t1, t2, t3 = st.tabs(["PDF to editable Docx", "JPG to PDF", "PPT to PDF"])

with t1:
    st.subheader("PDF to DOCX Converter")
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
    else:
        st.write("Upload a PDF file to convert it to a DOCX.")

with t2:
    st.subheader("JPG to PDF Converter")
    uploaded_file = st.file_uploader("Choose a JPG file", type="jpg")
    if uploaded_file is not None:
        jpg_path = "uploaded.jpg"
        original_filename = uploaded_file.name
        with open(jpg_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        prefix = "cnvtd_"
        pdf_filename = f"{prefix}{os.path.splitext(original_filename)[0]}.pdf"
        convert_jpg_to_pdf(jpg_path, pdf_filename)
        if os.path.exists(pdf_filename):
            with open(pdf_filename, "rb") as f:
                st.download_button("Download PDF", f, file_name=pdf_filename)
        else:
            st.error("PDF file not generated.")
    else:
        st.write("Upload a JPG file to convert it to a PDF.")

with t3:
    st.subheader("PPT to PDF Converter")
    uploaded_file = st.file_uploader("Choose a PPTX file", type="pptx")
    if uploaded_file is not None:
        ppt_path = "uploaded.pptx"
        original_filename = uploaded_file.name
        with open(ppt_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        prefix = "cnvtd_"
        pdf_filename = f"{prefix}{os.path.splitext(original_filename)[0]}.pdf"
        convert_ppt_to_pdf(ppt_path, pdf_filename)
        if os.path.exists(pdf_filename):
            with open(pdf_filename, "rb") as f:
                st.download_button("Download PDF", f, file_name=pdf_filename)
        else:
            st.error("PDF file not generated.")
    else:
        st.write("Upload a PPTX file to convert it to a PDF.")
