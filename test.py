import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Set up page configuration
st.set_page_config(
    page_title="Email Service",
    page_icon="📧",
    layout="centered"
)

# Add a logo and header
st.image('images/banner-app-Photoroom.png', use_column_width=True)
st.title('Email Service by saad.BrevoAPI')
st.subheader('Send emails easily with our service')

# Create a form for the email inputs
with st.form(key='email_form'):
    to = st.text_input("Enter Recipient's Address")
    subj = st.text_input("Subject of Email")
    msg = st.text_area('Enter Message to Send')

    # Form submit button
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    if to == "" or msg == "":
        st.warning("All fields are required")
    else:
        smtp_server = 'smtp-relay.brevo.com'
        smtp_port = 587
        smtp_username = st.secrets["smtp-usr"]
        smtp_password = st.secrets["smtp-pas"]

        from_email = 'business2saad@gmail.com'
        to_email = to
        subject = subj
        body = msg

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            succ = st.success("Email sent successfully!")
            time.sleep(3)
            succ.empty()

        except Exception as e:
            err = st.error(f"Failed to send email: {e}")
            time.sleep(2)
            err.empty()
