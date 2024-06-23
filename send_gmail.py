import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "canlong878@gmail.com"
receiver_email = "congminh25112002@gmail.com"
password = "apsajwmcxaymesvq"
encoded_password = base64.b64encode(password.encode()).decode()

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test email"

body = "This is a test email."
message.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
except Exception as e:
    print(f"Error: {e}")
