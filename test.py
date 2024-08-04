import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Function to generate a response
def generate_response(prompt):
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

# Streamlit interface
st.title("Chat with AI")
st.write("Ask me anything!")

# Input text box for user input
user_input = st.text_input("You: ", "")

if user_input:
    response = generate_response(user_input)
    st.text_area("AI: ", response, height=200)

# Run the Streamlit app
if __name__ == "__main__":
    st.run()
rasa --version