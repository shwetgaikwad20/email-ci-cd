import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "mail.eidiko-india.com"
SMTP_PORT = 465

EMAIL_FROM = os.environ["EMAIL_FROM"]
EMAIL_TO = os.environ["EMAIL_TO"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

msg = EmailMessage()
msg["Subject"] = "CI/CD Email Test"
msg["From"] = EMAIL_FROM
msg["To"] = EMAIL_TO
msg.set_content("This email was sent using GitHub Actions CI/CD.")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email sent successfully")

