import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="✅",
    layout="wide"
)

# Custom CSS for styling
def add_bg_color():
    st.markdown("""
        <style>
        body {
            background-color: #f0f2f6;
        }
        </style>
        """, unsafe_allow_html=True)
add_bg_color()

# Header section
st.title("Your Name")
st.subheader("Your Profession/Title")
st.image("your_profile_pic.jpg")

# About section
st.header("About Me")
st.write("A brief summary of your background and goals.")

# Skills section
st.header("Skills")
st.write("List of your skills with icons or progress bars")

# Projects section
st.header("Projects")
# Display projects with images, descriptions, and links

# Experience section
st.header("Experience")
# Display work experience with company names, roles, and dates

# Education section
st.header("Education")
# Display educational qualifications with degrees, institutions, and dates

# Contact section
st.header("Contact")
# Display contact information with email, phone number, and social media links

# Footer
st.write("Copyright © Your Name")
