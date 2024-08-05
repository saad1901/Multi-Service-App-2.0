import streamlit as st
import convertapi
import os

# Set your ConvertAPI secret key
convertapi.api_secret = 'I6QNdcljjJWKTIN3'

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Perform the conversion
        result = convertapi.convert('pdf', {'File': docx_path}, from_format='docx')
        
        # Save the converted PDF to the specified path
        result.save_files(pdf_path)
        st.success("Conversion successful!")
    except Exception as e:
        st.error(f"Conversion failed: {e}")

st.title("DOCX to PDF Converter")

uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")

if uploaded_file is not None:
    # Save the uploaded DOCX file
    with open("uploaded.docx", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Convert the DOCX file to PDF
    convert_docx_to_pdf("uploaded.docx", "output.pdf")
    
    # Provide the PDF file for download
    if os.path.exists("output.pdf"):
        with open("output.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="output.pdf")
    else:
        st.error("PDF file not generated.")

st.write("Upload a DOCX file and click the button to convert it to a PDF.")
