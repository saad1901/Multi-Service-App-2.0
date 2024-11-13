import streamlit as st
import time
import urllib.parse

st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Hello From Saad",
    page_icon="🙋🏻‍♂️",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 45px;
        color: #3498db;
        margin-bottom: 30px;
    }
    .section-title {
        color: #2ecc71;
        font-size: 30px;
        border-bottom: 2px solid #2ecc71;
        margin-bottom: 10px;
    }
    .content-box {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .contact-box {
        background-color: #e74c3c;
        padding: 20px;
        color: white;
        text-align: center;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<div class='main-title'>Mohammad Saad</div>", unsafe_allow_html=True)
st.write("##")

# About Me
st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
I am a final-year IT student at Government College of Engineering, Aurangabad, specializing in software development and cloud technologies. I love building projects with Python, Streamlit, and AWS services.
</div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
<strong>Programming:</strong> C++, Python, SQL, Data Structures  <br>
<strong>Cloud & Automation:</strong> AWS, Docker, Bash Scripting  <br>
<strong>Web Development:</strong> Streamlit, HTML, CSS  <br>
<strong>Other Technologies:</strong> Git, Networking, Linux, OOP  
</div>
""", unsafe_allow_html=True)

# Education Section
st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
<strong>B.Tech in Information Technology</strong>  <br>
Government College of Engineering, Aurangabad (2021-2025)  <br>
CGPA: 7.475  <br><br>

<strong>High School:</strong>  <br>
Al-Irfan Jr College, Aurangabad (2019-2021)  <br>
95% in HSC  
</div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
<strong><a href='https://bloodmatch.streamlit.app/'>DonorSync</a>:</strong>  <br>
A platform for connecting blood donors and recipients. Built using Streamlit, SQLite, and Mail APIs.  <br><br>

<strong><a href='https://saadapp.streamlit.app/'>Cloud File Storage Application</a>:</strong>  <br>
Developed with AWS S3 and EC2, this project allows scalable file storage and management using Boto3.  <br><br>

<strong>AppHub:</strong>  <br>
A comprehensive platform that includes cloud storage, translation, text summarization, and document querying using the Anthropic API.
</div>
""", unsafe_allow_html=True)

# Certifications Section
st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
<strong>Python Essentials 1 & 2</strong> - Cisco  <br>
<strong>AWS Architecting</strong>  
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown("""
<div class='contact-box'>
    📧 Email: saadiqbal1921@gmail.com | 📍 Location: Aurangabad, India  
</div>
""", unsafe_allow_html=True)

# Links for GitHub and LinkedIn
st.markdown("""
[GitHub](https://github.com/saad1901) | [LinkedIn](http://www.linkedin.com/in/saad99)
""")




# a,b,c = st.tabs(["About Me","Projects","Contact"])

# with a:
#     st.header("Hello, Saad here !")
#     # st.subheader("Welcome to My Application")

# with b:
#     pass

# with c:
#     pass

# st.write("# Welcome to Streamlit! 👋")


# st.toast('Open SideBar for Other Application')
# use st.tab for personal info
# if st.button('hello'):
#     st.toast('this is a toast msg')
# st.snow()

# st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)


# FOR LINKEDIN
# st.page_link("http://www.google.com", label="Google", icon="")

