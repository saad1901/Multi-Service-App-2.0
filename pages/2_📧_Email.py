import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Email Service",
    page_icon="📧",
)
a,b = st.columns(2)
st.header('Email Service by saad.BrevoAPI')
to = a.text_input("Enter Recipient's Address")
subj = b.text_input("Subject of Email")
msg = st.text_area('Enter Message to Send')

sub = st.button('Send')
if sub:
    if to == "" or msg == "":
        warn = st.warning("Fields required")
        time.sleep(2)
        warn.empty()
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
