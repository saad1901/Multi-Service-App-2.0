import streamlit as st
import convertapi
import os

# Set your ConvertAPI secret key
convertapi.api_secret = 'I6QNdcljjJWKTIN3'

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # Perform the conversion
        result = convertapi.convert('docx', {'File': pdf_path}, from_format='pdf')
        
        # Save the converted DOCX to the specified path
        result.save_files(docx_path)
        st.success("Conversion successful!")
    except Exception as e:
        st.error(f"Conversion failed: {e}")

st.title("PDF to DOCX Converter")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF file
    original_filename = uploaded_file.name
    pdf_path = "uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Generate the DOCX filename with the prefix
    prefix = "cnvt_"
    docx_filename = f"{prefix}{os.path.splitext(original_filename)[0]}.docx"
    
    # Convert the PDF file to DOCX
    convert_pdf_to_docx(pdf_path, docx_filename)
    
    # Provide the DOCX file for download
    if os.path.exists(docx_filename):
        with open(docx_filename, "rb") as f:
            st.download_button("Download DOCX", f, file_name=docx_filename)
    else:
        st.error("DOCX file not generated.")

st.write("Upload a PDF file and click the button to convert it to a DOCX.")
