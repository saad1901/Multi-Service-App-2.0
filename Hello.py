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
    .skills-box {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .projects-box {
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
st.write("I am a final-year IT student at Government College of Engineering, Aurangabad, specializing in software development and cloud technologies. I love building projects with Python, Streamlit, and AWS services.")

# Skills Section
st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
st.markdown("""
<div class='skills-box'>
- **Programming:** C++, Python, SQL, Data Structures  
- **Cloud & Automation:** AWS, Docker, Bash Scripting  
- **Web Development:** Streamlit, HTML, CSS  
- **Other Technologies:** Git, Networking, Linux, OOP  
</div>
""", unsafe_allow_html=True)

# Education Section
st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
st.write("""
- **B.Tech in Information Technology**  
  Government College of Engineering, Aurangabad (2021-2025)  
  CGPA: 7.475  
- **High School:**  
  Al-Irfan Jr College, Aurangabad (2019-2021)  
  95% in HSC  
""")

# Projects Section
st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
st.markdown("""
<div class='projects-box'>
- **[DonorSync](https://bloodmatch.streamlit.app/):**  
  A platform for connecting blood donors and recipients. Built using Streamlit, SQLite, and Mail APIs.
  
- **[Cloud File Storage Application](https://saadapp.streamlit.app/):**  
  Developed with AWS S3 and EC2, this project allows scalable file storage and management using Boto3.
  
- **AppHub:**  
  A comprehensive platform that includes cloud storage, translation, text summarization, and document querying using the Anthropic API.
</div>
""", unsafe_allow_html=True)

# Certifications Section
st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)
st.write("""
- **Python Essentials 1 & 2** - Cisco  
- **AWS Architecting**  
""")

# Contact Information
st.markdown("""
<div class='contact-box'>
    📧 Email: saadiqbal1921@gmail.com | 📍 Location: Aurangabad, India  
</div>
""", unsafe_allow_html=True)

# Links for GitHub and LinkedIn (outside HTML to ensure they work)
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

