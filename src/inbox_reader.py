from imap_tools import MailBox, AND
from src.file_utils import save_attachments
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

def check_inbox(attachment_senders):
    print("Connecting to inbox...")
    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD) as mailbox:
        for msg in mailbox.fetch(AND(seen=F)):
            print(f"\nFrom: {msg.from_}")
            print(f"Subject: {msg.subject}")
            save_attachments(msg, sender=msg.from_, attachment_senders=attachment_senders)

