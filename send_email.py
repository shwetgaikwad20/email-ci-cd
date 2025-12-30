import smtplib
from email.mime.text import MIMEText

//commit change 1

SMTP_SERVER = "mail.eidiko-india.com"
SMTP_PORT = 465

EMAIL_FROM = "shwetshailendra.gaikwad@eidiko-india.com"
EMAIL_TO = "pratham.paunikar@eidiko-india.com"
EMAIL_PASSWORD = "Gaikwad@123"

msg = MIMEText("This email was sent using GitHub Actions CI/CD.")
msg['Subject'] = "CI/CD Email Test"
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email sent successfully")

