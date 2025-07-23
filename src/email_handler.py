import smtplib
from email.message import EmailMessage
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_missing_docs_email(to_email, missing_docs):
    if not missing_docs:
        return

    msg = EmailMessage()
    msg["Subject"] = "Missing Documents for Your Application"
    msg["From"] = EMAIL
    msg["To"] = to_email

    missing_list = "\n".join(f"- {doc}" for doc in missing_docs)
    msg.set_content(f"""\
Hi,

Thank you for your application. However, the following required documents are missing:

{missing_list}

Please submit them within the next 3 days.

Regards,  
Team Ridipt
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
        print(f"Sent email to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")