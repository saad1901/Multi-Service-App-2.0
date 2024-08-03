import streamlit as st
from PyPDF2 import PdfReader
import requests
import anthropic

st.set_page_config(
    page_title="File GPT",
    page_icon="📄",
)

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_word(docx_file):
    document = Document(docx_file)
    text = "\n".join([paragraph.text for paragraph in document.paragraphs])
    return text

def extract_text_from_ppt(ppt_file):
    presentation = Presentation(ppt_file)
    text = ""
    for slide in presentation.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + "\n"
    return text

def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_word(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.presentationml.presentation":
        return extract_text_from_ppt(file)
    else:
        return "Unsupported file format."

st.title("Document Q&A with Anthropic")
st.write("Upload a document (PDF, Word, PowerPoint) and ask a question or give a command to summarize the content.")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "pptx"])
prompt = st.text_input("Enter your prompt", placeholder="Summarize the document")

if uploaded_file and prompt:
    with st.spinner('Processing...'):
        article = extract_text(uploaded_file)
        prompt_text = f"{anthropic.HUMAN_PROMPT} Here's a document:\n\n{article}\n\n\n\n{prompt}{anthropic.AI_PROMPT}"

        try:
            headers = {
                "x-api-key": st.secrets["anthropic_api_key"],
                "Content-Type": "application/json",
            }
            data = {
                "prompt": prompt_text,
                "model": "claude-v1",
                "max_tokens": 100,
                "stop_sequences": [anthropic.HUMAN_PROMPT],
            }

            response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                st.write("### Response")
                st.write(result.get('completion', 'No completion found')) 
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            # st.error(f"An error occurred: {e}")
            st.warning('Sorry, No credits Left')

elif not uploaded_file:
    st.info("Please upload a document.")

elif not prompt:
    st.info("Please enter a prompt.")
