from flask import Flask, render_template, request
import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load AWS and Brevo credentials from .env file
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')

# Flask setup
app = Flask(__name__)

# Configure S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME
)

# Home route for uploading files
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get the uploaded file
        file = request.files['file']

        if file:
            try:
                # Upload to AWS S3 without ACL
                s3_client.upload_fileobj(
                    file,
                    AWS_STORAGE_BUCKET_NAME,
                    file.filename
                )
                # Generate the file URL
                file_url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/{file.filename}"
                return render_template("upload_success.html", file_url=file_url)

            except NoCredentialsError:
                return "AWS credentials not available"
    
    return render_template("upload.html")

@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    file_url = request.form['file_url']

    # Brevo SMTP server credentials
    smtp_server = 'smtp-relay.brevo.com'
    smtp_port = 587
    smtp_username = os.getenv('BREVO_SMTP_USER')  # Brevo SMTP user from .env
    smtp_password = os.getenv('BREVO_SMTP_PASS')  # Brevo SMTP password from .env

    from_email = 'your-email@example.com'  # Replace with your email
    to_email = email
    subject = "File Link from FileShare"
    body = f"Hello,\n\nYou can access the file via the following link: {file_url}"

    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Brevo SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return f"Email sent to {email} successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

if __name__ == "__main__":
    app.run(debug=True)
