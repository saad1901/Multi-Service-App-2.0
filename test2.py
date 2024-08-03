import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587
smtp_username = '79ca6d002@smtp-brevo.com'
smtp_password = 'yjfW90zasYIdnRrQ'

from_email = 'business2saad@gmail.com'
to_email = 'business2saad@gmail.com'
subject = 'from file test4'
body = 'This is a test email sent from a Python script using Brevo SMTP.'

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
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
